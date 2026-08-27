from __future__ import annotations

import json
import textwrap
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "docs" / "data" / "ru-content.json"
OUT_PATH = ROOT / "public" / "pdfs" / "UAIS-Manifesto-RU.pdf"
PAGE_W, PAGE_H = A4

PALETTE = {
    "mauve": colors.HexColor("#DDB6D5"),
    "blue": colors.HexColor("#AEC6E8"),
    "pistachio": colors.HexColor("#C8DFB4"),
    "peach": colors.HexColor("#F4C6A8"),
    "cream": colors.HexColor("#F6ECD9"),
    "ink": colors.HexColor("#302D36"),
    "soft": colors.HexColor("#6A6472"),
    "paper": colors.HexColor("#FFFDF8"),
}


def register_fonts() -> None:
    candidates = [
        (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/arialbd.ttf")),
        (Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")),
    ]
    for regular, bold in candidates:
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont("UAISRegular", str(regular)))
            pdfmetrics.registerFont(TTFont("UAISBold", str(bold)))
            return
    raise RuntimeError("No Unicode TTF font found for PDF generation")


def wrap_text(text: str, width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        lines.extend(textwrap.wrap(paragraph, width=width, break_long_words=False) or [""])
    return lines


def draw_wrapped(c: canvas.Canvas, text: str, x: float, y: float, width: int, size: int, font: str = "UAISRegular", leading: float | None = None) -> float:
    c.setFont(font, size)
    leading = leading or size * 1.28
    for line in wrap_text(text, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_note(c: canvas.Canvas, x: float, y: float, w: float, title: str, body: str, accent: str, items: list[str] | None = None) -> float:
    title_lines = wrap_text(title, 28)
    body_lines = wrap_text(body or "", 44)
    item_lines: list[str] = []
    for item in items or []:
        item_lines.extend(wrap_text(f"- {item}", 42))
    h = max(31 * mm, (len(title_lines) * 13 + len(body_lines) * 10 + len(item_lines) * 10 + 19) * 1.05)
    c.setFillColor(PALETTE.get(accent, PALETTE["cream"]))
    c.setStrokeColor(colors.Color(0.18, 0.17, 0.21, alpha=.22))
    c.roundRect(x, y - h, w, h, 4, stroke=1, fill=1)
    c.setFillColor(colors.Color(0.62, 0.52, 0.62, alpha=.45))
    c.rect(x + w - 29 * mm, y - 3 * mm, 22 * mm, 6 * mm, stroke=0, fill=1)
    c.setFillColor(PALETTE["ink"])
    cursor = y - 9 * mm
    c.setFont("UAISBold", 10)
    for line in title_lines:
      c.drawString(x + 7 * mm, cursor, line)
      cursor -= 12
    cursor -= 2
    if body:
        cursor = draw_wrapped(c, body, x + 7 * mm, cursor, 48, 8, "UAISRegular", 10)
    if items:
        for item in items:
            cursor = draw_wrapped(c, f"- {item}", x + 7 * mm, cursor, 45, 8, "UAISRegular", 10)
    return y - h - 6 * mm


def draw_header(c: canvas.Canvas, page: dict, number: int, total: int) -> float:
    margin = 16 * mm
    c.setFillColor(PALETTE["paper"])
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(PALETTE.get(page.get("accent"), PALETTE["mauve"]))
    c.rect(margin, PAGE_H - 35 * mm, PAGE_W - 2 * margin, 16 * mm, stroke=0, fill=1)
    c.setFillColor(PALETTE["soft"])
    c.setFont("UAISBold", 8)
    c.drawString(margin, PAGE_H - 16 * mm, f"{page.get('kicker', 'UAIS')} · {page['id']} · {number}/{total}")
    c.setFillColor(PALETTE["ink"])
    c.setFont("UAISBold", 21)
    c.drawString(margin + 4 * mm, PAGE_H - 30 * mm, page["title"])
    if page.get("subtitle"):
        c.setFont("UAISRegular", 10)
        c.drawString(margin + 4 * mm, PAGE_H - 39 * mm, page["subtitle"])
    return PAGE_H - 51 * mm


def draw_cover(c: canvas.Canvas, data: dict, page: dict) -> None:
    c.setFillColor(PALETTE["paper"])
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(PALETTE["mauve"])
    c.rect(19 * mm, PAGE_H - 64 * mm, PAGE_W - 38 * mm, 26 * mm, stroke=0, fill=1)
    c.setFillColor(PALETTE["ink"])
    c.setFont("UAISBold", 31)
    c.drawString(24 * mm, PAGE_H - 55 * mm, "UAIS")
    c.setFont("UAISBold", 18)
    c.drawString(24 * mm, PAGE_H - 73 * mm, "Universal AI Safety Architecture")
    c.setFont("UAISBold", 19)
    c.drawString(24 * mm, PAGE_H - 100 * mm, "Может сделать ≠ имеет право сделать.")
    y = draw_wrapped(c, page["lead"], 24 * mm, PAGE_H - 117 * mm, 74, 11, "UAISRegular", 15)
    y -= 7 * mm
    for note in page["notes"]:
        y = draw_note(c, 24 * mm, y, PAGE_W - 48 * mm, note["title"], note.get("body", ""), note.get("accent", "cream"), note.get("items"))
    c.setFillColor(PALETTE["soft"])
    c.setFont("UAISRegular", 8)
    c.drawString(24 * mm, 18 * mm, data["meta"]["version"])
    c.drawRightString(PAGE_W - 24 * mm, 18 * mm, "cresta13.github.io/universal-ai-safety-architecture/")
    c.linkURL(data["meta"]["canonicalUrl"], (24 * mm, 12 * mm, PAGE_W - 24 * mm, 25 * mm), relative=0)


def draw_toc(c: canvas.Canvas, data: dict, page: dict) -> None:
    y = draw_header(c, page, 2, len(data["pages"]))
    c.setFillColor(PALETTE["ink"])
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 84, 10, "UAISRegular", 13) - 5 * mm
    for item in data["pages"]:
        c.setFillColor(PALETTE["cream"])
        c.roundRect(18 * mm, y - 9 * mm, PAGE_W - 36 * mm, 8 * mm, 3, stroke=0, fill=1)
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISBold", 8.5)
        c.drawString(21 * mm, y - 6 * mm, f"{item['id']}  {item['title']}")
        y -= 10 * mm


def draw_page(c: canvas.Canvas, data: dict, page: dict, index: int) -> None:
    if page["layout"] == "cover":
        draw_cover(c, data, page)
        return
    if page["layout"] == "toc":
        draw_toc(c, data, page)
        return
    y = draw_header(c, page, index + 1, len(data["pages"]))
    c.setFillColor(PALETTE["ink"])
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 84, 10, "UAISRegular", 13) - 5 * mm
    col_w = (PAGE_W - 42 * mm) / 2
    x_positions = [18 * mm, 24 * mm + col_w]
    col_y = [y, y]
    notes = page.get("notes", [])
    if page["layout"] == "glossary":
        notes = notes + [
            {
                "title": f"{term['canonical']} -> {term['ru']}",
                "body": term["definition"],
                "accent": "cream",
            }
            for term in data.get("terms", [])[:6]
        ]
    for note_index, note in enumerate(notes):
        col = note_index % 2
        col_y[col] = draw_note(
            c,
            x_positions[col],
            col_y[col],
            col_w,
            note.get("title", ""),
            note.get("body", ""),
            note.get("accent", "cream"),
            note.get("items"),
        )
    c.setFillColor(PALETTE["soft"])
    c.setFont("UAISRegular", 7.5)
    c.drawString(18 * mm, 12 * mm, "Источники: " + "; ".join(page.get("sourceSections", []))[:125])


def main() -> None:
    register_fonts()
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT_PATH), pagesize=A4)
    c.setTitle(data["meta"]["title"])
    c.setAuthor(data["meta"]["author"])
    c.setSubject(data["meta"]["description"])
    for index, page in enumerate(data["pages"]):
        draw_page(c, data, page, index)
        c.showPage()
    c.save()
    print(f"Generated {OUT_PATH}")


if __name__ == "__main__":
    main()
