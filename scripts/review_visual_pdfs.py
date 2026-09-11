"""Render both local visual editions and verify their text, fonts, and links."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import math
from pathlib import Path
import re
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFont
import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf"


def compact(text):
    return re.sub(r"\s+", "", text).replace("\u00ad", "")


def font_embedded(font):
    if font.get("/Subtype") == "/Type0":
        return all(font_embedded(item.get_object()) for item in font["/DescendantFonts"])
    descriptor = font.get("/FontDescriptor")
    if descriptor:
        descriptor = descriptor.get_object()
        return any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3"))
    return font.get("/Subtype") == "/Type3" and bool(font.get("/CharProcs"))


def contact_sheet(images, labels, output, columns=4, width=300):
    margin, label_height = 16, 24
    thumb_height = round(width * 1.25)
    rows = math.ceil(len(images) / columns)
    canvas = Image.new("RGB", (columns * (width + margin) + margin, rows * (thumb_height + label_height + margin) + margin), "#ececf0")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=16)
    for index, (image_path, label) in enumerate(zip(images, labels)):
        x = margin + index % columns * (width + margin)
        y = margin + index // columns * (thumb_height + label_height + margin)
        with Image.open(image_path) as image:
            image.thumbnail((width, thumb_height), Image.Resampling.LANCZOS)
            canvas.paste(image, (x, y))
        draw.text((x, y + thumb_height + 4), label, fill="#302d36", font=font)
    canvas.save(output)


def review(locale, renderer, layout):
    pdf = OUTPUT / f"UAIS_Visual_Edition_{locale.upper()}_Candidate3.pdf"
    reader = PdfReader(pdf)
    content = json.loads((ROOT / "docs" / "data" / f"{locale}-content.json").read_text(encoding="utf-8"))
    text = compact("\n".join(page.extract_text() or "" for page in reader.pages))
    missing = []
    for page in content["pages"]:
        for note in page.get("notes", []):
            for value in [note.get("body", ""), *note.get("items", [])]:
                if value and compact(value) not in text:
                    missing.append({"page": page["id"], "text": value})
    for term in content["terms"]:
        if compact(term["definition"]) not in text:
            missing.append({"term": term["id"]})
        if locale == "ru" and compact(term["canonical"]) not in text:
            missing.append({"canonical": term["id"]})
    if missing:
        raise ValueError(f"{locale}: PDF text missing: {missing}")
    assert len(reader.pages) == layout["pageCount"], "Unexpected print pagination"
    assert pdf.stat().st_size < 100_000_000, "PDF exceeds 100 MB"
    assert "≠" in text and "\ufffd" not in text, "Unicode extraction failure"
    fonts = {}
    external_links, internal_links = 0, 0
    for page in reader.pages:
        for font in page["/Resources"].get("/Font", {}).values():
            font = font.get_object()
            fonts[str(font.get("/BaseFont"))] = font_embedded(font)
        for annotation in page.get("/Annots", []):
            annotation = annotation.get_object()
            action = annotation.get("/A", {})
            uri = action.get("/URI", "")
            if uri:
                assert not uri.startswith("http://127.0.0.1"), f"Localhost link in PDF: {uri}"
                external_links += 1
            if annotation.get("/Dest") or action.get("/S") == "/GoTo":
                internal_links += 1
    assert fonts and all(fonts.values()), f"Unembedded fonts: {fonts}"
    assert external_links > 0 and internal_links > 0, "Missing PDF links"
    with pdfplumber.open(pdf) as document:
        outside = [
            {"page": index + 1, "text": char["text"]}
            for index, page in enumerate(document.pages)
            for char in page.chars
            if char["text"].strip() and (
                char["x0"] < 12 or char["x1"] > page.width - 12
                or char["top"] < 12 or char["bottom"] > page.height - 12
            )
        ]
    assert not outside, f"Glyphs outside the printable page: {outside[:20]}"

    rendered = ROOT / "tmp" / "task15-pdf-pages" / locale
    rendered.mkdir(parents=True, exist_ok=True)
    for pattern in ("page-*.png", "phone-*.png", "review-*.png"):
        for previous in rendered.glob(pattern):
            previous.unlink()
    midpoint = math.ceil(len(reader.pages) / 2)

    def render_range(bounds):
        first, last = bounds
        subprocess.run([renderer, "-f", str(first), "-l", str(last), "-r", "190", "-png", str(pdf), str(rendered / "page")], check=True)

    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(render_range, [(1, midpoint), (midpoint + 1, len(reader.pages))]))
    images = sorted(rendered.glob("page-*.png"), key=lambda item: int(item.stem.split("-")[-1]))
    assert len(images) == len(reader.pages), "Rendered page count mismatch"
    labels = [f"{locale.upper()} {index + 1:02d} / {page_id}" for index, page_id in enumerate(layout["pages"])]
    contact_sheet(images, labels, OUTPUT / f"UAIS_Visual_Edition_{locale.upper()}_contact_sheet.png")
    # Four pages per board support review of every page at a useful resolution.
    for start in range(0, len(images), 4):
        contact_sheet(images[start:start + 4], labels[start:start + 4], rendered / f"review-{start // 4 + 1:02d}.png", columns=2, width=700)
    for index, image_path in enumerate(images):
        with Image.open(image_path) as image:
            image.resize((390, 488), Image.Resampling.LANCZOS).save(rendered / f"phone-{index + 1:02d}.png")
    return {"locale": locale, "pages": len(reader.pages), "sizeMB": round(pdf.stat().st_size / 1_000_000, 2), "dpi": 190, "missingText": 0, "glyphsOutsidePage": 0, "fonts": fonts, "externalLinks": external_links, "internalLinks": internal_links}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdftoppm", default=shutil.which("pdftoppm"))
    parser.add_argument("--locale", choices=["en", "ru"])
    args = parser.parse_args()
    if not args.pdftoppm:
        parser.error("Pass --pdftoppm with the path to Poppler's renderer")
    layouts = json.loads((OUTPUT / "visual_pdf_layout_qa.json").read_text(encoding="utf-8"))
    for layout in layouts:
        if args.locale and layout["locale"] != args.locale:
            continue
        result = review(layout["locale"], args.pdftoppm, layout)
        (OUTPUT / f"visual_pdf_file_qa_{layout['locale']}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
