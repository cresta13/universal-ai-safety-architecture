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
TARGETS = [
    (ROOT / "docs" / "data" / "en-content.json", ROOT / "public" / "pdfs" / "UAIS-Manifesto-EN.pdf"),
    (ROOT / "docs" / "data" / "ru-content.json", ROOT / "public" / "pdfs" / "UAIS-Manifesto-RU.pdf"),
]
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

GLOSSARY_REQUIRED_IDS = [
    "capability",
    "authority",
    "legitimate-authority",
    "effective-reachable-authority",
    "illicit-reachable-authority",
    "authority-ceiling",
    "capability-boundary",
    "consequence-interface",
    "guardian",
    "evidence-carrying-alert",
    "structured-evidence-package",
    "deterministic-evidence-verifier",
    "human-sovereignty",
    "manual-sovereignty-controller",
    "physical-sovereignty",
    "physical-sovereignty-threshold",
    "safety-passport",
    "consumer-ai-safety-class",
    "safety-assurance-level",
    "ai-trustworthiness",
    "authority-expansion-event",
]

RU_PDF_GLOSSARY_SUMMARY = {
    "capability": "Технически доступное действие системы.",
    "legitimate-authority": "Выданное право действовать в заданных пределах.",
    "effective-reachable-authority": "Практически достижимый путь к значимому действию.",
    "illicit-reachable-authority": "Достижимый путь без выданного права.",
    "authority-ceiling": "Максимум полномочий без нового внешнего решения.",
    "capability-boundary": "Контролируемая граница значимой возможности.",
    "consequence-interface": "Место, где действие достигает человека, имущества или среды.",
    "guardian": "Ограниченный наблюдатель, выпускающий доказательства, а не команды.",
    "evidence-carrying-alert": "Предупреждение, связанное с проверяемыми доказательствами.",
    "structured-evidence-package": "Пакет наблюдений, допущений, неопределённости и срока действия.",
    "deterministic-evidence-verifier": "Проверяет механические свойства доказательств, не истину мира.",
    "human-sovereignty": "Независимый внешний контроль на критических границах.",
    "manual-sovereignty-controller": "Независимый ручной способ остановить значимую функцию.",
    "physical-sovereignty": "Значимая физическая деятельность без критической зависимости от людей.",
    "physical-sovereignty-threshold": "Порог потери эффективного внешнего физического ограничения.",
    "safety-passport": "Понятная карточка конфигурации, опасностей, контролей и ограничений.",
    "consumer-ai-safety-class": "Профиль защитных механизмов и доказательств.",
    "safety-assurance-level": "Сила процедур и доказательств; не разрешение на внедрение.",
    "ai-trustworthiness": "Наблюдаемая надёжность конкретной версии в конкретной области.",
    "authority-expansion-event": "Переход, требующий внешней проверки расширения полномочий.",
}


def register_fonts() -> None:
    candidates = [
        (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/arialbd.ttf")),
        (
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ),
    ]
    for regular, bold in candidates:
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont("UAISRegular", str(regular)))
            pdfmetrics.registerFont(TTFont("UAISBold", str(bold)))
            return
    raise RuntimeError("No Unicode TTF font found for PDF generation")


def wrap_text(text: str, width: int, max_lines: int | None = None) -> list[str]:
    lines: list[str] = []
    for paragraph in str(text or "").split("\n"):
        lines.extend(textwrap.wrap(paragraph, width=width, break_long_words=False) or [""])
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        if lines:
            lines[-1] = lines[-1].rstrip(". ") + "..."
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: int,
    size: float,
    font: str = "UAISRegular",
    leading: float | None = None,
    max_lines: int | None = None,
) -> float:
    c.setFont(font, size)
    leading = leading or size * 1.28
    for line in wrap_text(text, width, max_lines=max_lines):
        c.drawString(x, y, line)
        y -= leading
    return y


def term_title(term: dict) -> str:
    return term.get("label") or term.get("ru") or term.get("canonical") or ""


def term_summary(data: dict, term: dict) -> str:
    if term.get("pdfSummary"):
        return term["pdfSummary"]
    if data.get("locale") == "ru":
        return RU_PDF_GLOSSARY_SUMMARY.get(term["id"], term["definition"])
    return term.get("definition", "")


def source_file(source: str) -> str:
    return source.split(":")[0].strip()


def draw_sources(c: canvas.Canvas, page: dict, data: dict) -> None:
    files = [source_file(source) for source in page.get("sourceSections", [])]
    source_text = (data.get("ui", {}).get("sources") or "Sources: ") + "; ".join(files)
    c.setFillColor(PALETTE["soft"])
    c.setFont("UAISRegular", 6.7)
    draw_wrapped(c, source_text, 18 * mm, 12 * mm, 112, 6.7, "UAISRegular", 8, max_lines=2)


def estimate_note_height(
    title: str,
    body: str,
    w: float,
    items: list[str] | None = None,
    canonical: str | None = None,
    compact: bool = False,
) -> float:
    text_width = max(24, int((w / mm) * 0.58))
    title_lines = wrap_text(title, max(18, text_width - 4), max_lines=2)
    canonical_lines = wrap_text(canonical or "", max(18, text_width - 2), max_lines=2)
    body_lines = wrap_text(body or "", text_width, max_lines=5 if compact else 7)
    item_lines: list[str] = []
    for item in items or []:
        item_lines.extend(wrap_text(f"- {item}", max(18, text_width - 2), max_lines=2))
    min_h = 23 * mm if compact else 29 * mm
    content_h = (
        len(title_lines) * 11.3
        + len(canonical_lines) * 7.4
        + len(body_lines) * (8.8 if compact else 9.7)
        + len(item_lines) * (8.7 if compact else 9.5)
        + 17
    )
    return max(min_h, content_h)


def draw_note(
    c: canvas.Canvas,
    x: float,
    y: float,
    w: float,
    title: str,
    body: str,
    accent: str,
    items: list[str] | None = None,
    canonical: str | None = None,
    compact: bool = False,
) -> float:
    text_width = max(24, int((w / mm) * 0.58))
    h = estimate_note_height(title, body, w, items=items, canonical=canonical, compact=compact)
    c.setFillColor(PALETTE.get(accent, PALETTE["cream"]))
    c.setStrokeColor(colors.Color(0.18, 0.17, 0.21, alpha=.22))
    c.roundRect(x, y - h, w, h, 4, stroke=1, fill=1)
    c.setFillColor(colors.Color(0.62, 0.52, 0.62, alpha=.45))
    c.rect(x + w - 27 * mm, y - 3 * mm, 20 * mm, 5 * mm, stroke=0, fill=1)
    c.setFillColor(PALETTE["ink"])
    cursor = y - 8 * mm
    c.setFont("UAISBold", 8.8 if compact else 10)
    for line in wrap_text(title, max(18, text_width - 4), max_lines=2):
        c.drawString(x + 6 * mm, cursor, line)
        cursor -= 10.5 if compact else 12
    if canonical:
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISBold", 6.2 if compact else 6.8)
        for line in wrap_text(canonical, max(18, text_width - 2), max_lines=2):
            c.drawString(x + 6 * mm, cursor, line)
            cursor -= 7.2 if compact else 8
        c.setFillColor(PALETTE["ink"])
    cursor -= 1.5
    if body:
        cursor = draw_wrapped(
            c,
            body,
            x + 6 * mm,
            cursor,
            text_width,
            7.2 if compact else 8,
            "UAISRegular",
            8.8 if compact else 10,
            max_lines=5 if compact else 7,
        )
    for item in items or []:
        cursor = draw_wrapped(
            c,
            f"- {item}",
            x + 6 * mm,
            cursor,
            max(18, text_width - 2),
            7.2 if compact else 8,
            "UAISRegular",
            8.7 if compact else 10,
            max_lines=2,
        )
    return y - h - 5 * mm


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
    c.setFont("UAISBold", 20)
    cursor = PAGE_H - 30 * mm
    for line in wrap_text(page["title"], 36, max_lines=2):
        c.drawString(margin + 4 * mm, cursor, line)
        cursor -= 18
    if page.get("subtitle"):
        c.setFont("UAISRegular", 9.5)
        for line in wrap_text(page["subtitle"], 88, max_lines=2):
            c.drawString(margin + 4 * mm, cursor - 1 * mm, line)
            cursor -= 11
    if page.get("canonical"):
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISBold", 7.5)
        c.drawString(margin + 4 * mm, cursor - 1 * mm, page["canonical"])
        cursor -= 10
    return min(PAGE_H - 51 * mm, cursor - 8 * mm)


def draw_cover(c: canvas.Canvas, data: dict, page: dict) -> None:
    c.setFillColor(PALETTE["paper"])
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(PALETTE["mauve"])
    c.rect(19 * mm, PAGE_H - 64 * mm, PAGE_W - 38 * mm, 26 * mm, stroke=0, fill=1)
    c.setFillColor(PALETTE["ink"])
    c.setFont("UAISBold", 31)
    c.drawString(24 * mm, PAGE_H - 55 * mm, "UAIS")
    c.setFont("UAISBold", 18)
    c.drawString(24 * mm, PAGE_H - 73 * mm, page.get("subtitle") or "Universal AI Safety Architecture")
    claim = next((note for note in page.get("notes", []) if note.get("kind") == "claim"), {})
    if claim.get("body"):
        c.setFont("UAISBold", 19)
        c.drawString(24 * mm, PAGE_H - 100 * mm, claim["body"])
    y = draw_wrapped(c, page["lead"], 24 * mm, PAGE_H - 117 * mm, 76, 10.5, "UAISRegular", 14, max_lines=5)
    y -= 7 * mm
    notes = [note for note in page.get("notes", []) if note.get("kind") != "claim"]
    col_w = (PAGE_W - 54 * mm) / 2
    col_y = [y, y]
    for note_index, note in enumerate(notes):
        col = note_index % 2
        col_y[col] = draw_note(
            c,
            24 * mm + col * (col_w + 6 * mm),
            col_y[col],
            col_w,
            note["title"],
            note.get("body", ""),
            note.get("accent", "cream"),
            note.get("items"),
            note.get("canonical"),
            compact=len(notes) > 2,
        )
    c.setFillColor(PALETTE["soft"])
    c.setFont("UAISRegular", 8)
    c.drawString(24 * mm, 18 * mm, data["meta"]["version"])
    c.drawRightString(PAGE_W - 24 * mm, 18 * mm, "cresta13.github.io/universal-ai-safety-architecture/")
    c.linkURL(data["meta"]["canonicalUrl"], (24 * mm, 12 * mm, PAGE_W - 24 * mm, 25 * mm), relative=0)


def draw_toc(c: canvas.Canvas, data: dict, page: dict) -> None:
    y = draw_header(c, page, 2, len(data["pages"]))
    c.setFillColor(PALETTE["ink"])
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 88, 9.5, "UAISRegular", 12) - 4 * mm
    for item in data["pages"]:
        c.setFillColor(PALETTE["cream"])
        c.roundRect(18 * mm, y - 8.5 * mm, PAGE_W - 36 * mm, 8 * mm, 3, stroke=0, fill=1)
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISBold", 8)
        c.drawString(21 * mm, y - 5.7 * mm, f"{item['id']}  {item['title']}")
        y -= 9.4 * mm


def draw_glossary_terms(c: canvas.Canvas, data: dict, y: float) -> None:
    terms_by_id = {term["id"]: term for term in data.get("terms", [])}
    terms = [terms_by_id[term_id] for term_id in GLOSSARY_REQUIRED_IDS if term_id in terms_by_id and term_id != "authority"]
    x0 = 18 * mm
    gap = 4 * mm
    col_w = (PAGE_W - 36 * mm - 2 * gap) / 3
    col_y = [y, y, y]
    for index, term in enumerate(terms):
        col = index % 3
        x = x0 + col * (col_w + gap)
        local_y = col_y[col]
        c.setFillColor(PALETTE["cream"])
        c.setStrokeColor(colors.Color(0.18, 0.17, 0.21, alpha=.16))
        c.roundRect(x, local_y - 22.5 * mm, col_w, 21.5 * mm, 3, stroke=1, fill=1)
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISBold", 6.4)
        cursor = local_y - 4.5 * mm
        for line in wrap_text(term_title(term), 27, max_lines=2):
            c.drawString(x + 3 * mm, cursor, line)
            cursor -= 6.7
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISBold", 5.1)
        for line in wrap_text(term["canonical"], 31, max_lines=2):
            c.drawString(x + 3 * mm, cursor, line)
            cursor -= 5.7
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISRegular", 5.05)
        for line in wrap_text(term_summary(data, term), 34, max_lines=4):
            c.drawString(x + 3 * mm, cursor, line)
            cursor -= 5.7
        col_y[col] = local_y - 24 * mm


def draw_glossary(c: canvas.Canvas, data: dict, page: dict, index: int) -> None:
    y = draw_header(c, page, index + 1, len(data["pages"]))
    c.setFillColor(PALETTE["ink"])
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 88, 9.3, "UAISRegular", 12, max_lines=4) - 3 * mm
    authority = next((term for term in data.get("terms", []) if term.get("id") == "authority"), None)
    if authority:
        canonical = authority.get("canonical") if authority.get("canonical") != term_title(authority) else None
        y = draw_note(
            c,
            18 * mm,
            y,
            PAGE_W - 36 * mm,
            term_title(authority),
            authority["definition"],
            "cream",
            canonical=canonical,
            compact=True,
        )
    version_title = "Версия" if data.get("locale") == "ru" else "Version"
    version = next((note for note in page.get("notes", []) if note.get("title") == version_title), None)
    if version:
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISRegular", 6.8)
        y = draw_wrapped(c, version.get("body", ""), 18 * mm, y + 2 * mm, 118, 6.8, "UAISRegular", 8, max_lines=2) - 2 * mm
    draw_glossary_terms(c, data, y)
    rights_title = "Права" if data.get("locale") == "ru" else "Rights"
    rights = next((note for note in page.get("notes", []) if note.get("title") == rights_title), None)
    if rights:
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISRegular", 6.5)
        draw_wrapped(c, rights.get("body", ""), 18 * mm, 24 * mm, 112, 6.5, "UAISRegular", 8, max_lines=3)
    draw_sources(c, page, data)


def draw_route(c: canvas.Canvas, page: dict, y: float) -> float:
    items = page.get("route") or [note_item for note in page.get("notes", []) for note_item in note.get("items", []) if note.get("kind") == "route"]
    if not items:
        return y
    x = 18 * mm
    gap = 3 * mm
    w = (PAGE_W - 36 * mm - gap * (min(len(items), 5) - 1)) / min(len(items), 5)
    colors_by_index = ["blue", "pistachio", "mauve", "peach", "cream"]
    for index, item in enumerate(items[:5]):
        c.setFillColor(PALETTE[colors_by_index[index % len(colors_by_index)]])
        c.roundRect(x + index * (w + gap), y - 12 * mm, w, 10 * mm, 3, stroke=0, fill=1)
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISBold", 6.7)
        for line_idx, line in enumerate(wrap_text(item, 16, max_lines=2)):
            c.drawCentredString(x + index * (w + gap) + w / 2, y - 5 * mm - line_idx * 7, line)
    return y - 17 * mm


def draw_page(c: canvas.Canvas, data: dict, page: dict, index: int) -> None:
    if page["layout"] == "cover":
        draw_cover(c, data, page)
        return
    if page["layout"] == "toc":
        draw_toc(c, data, page)
        return
    if page["layout"] == "glossary":
        draw_glossary(c, data, page, index)
        return
    y = draw_header(c, page, index + 1, len(data["pages"]))
    c.setFillColor(PALETTE["ink"])
    note_count = len(page.get("notes", []))
    compact = note_count >= 7
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 88, 9.2 if compact else 9.8, "UAISRegular", 12, max_lines=4 if compact else 6) - 5 * mm
    if page.get("route"):
        y = draw_route(c, page, y)
    if page.get("strip"):
        y = draw_route(c, {"route": page["strip"]}, y)
    col_w = (PAGE_W - 42 * mm) / 2
    x_positions = [18 * mm, 24 * mm + col_w]
    col_y = [y, y]
    for note in page.get("notes", []):
        col = 0 if col_y[0] >= col_y[1] else 1
        col_y[col] = draw_note(
            c,
            x_positions[col],
            col_y[col],
            col_w,
            note.get("title", ""),
            note.get("body", ""),
            note.get("accent", "cream"),
            note.get("items"),
            note.get("canonical"),
            compact=compact,
        )
    if min(col_y) < 20 * mm:
        raise RuntimeError(f"PDF page content overflow: {data['locale']} {page['id']} {page['slug']}")
    draw_sources(c, page, data)


def build_pdf(data_path: Path, out_path: Path) -> None:
    data = json.loads(data_path.read_text(encoding="utf-8"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out_path), pagesize=A4)
    c.setTitle(data["meta"]["title"])
    c.setAuthor(data["meta"]["author"])
    c.setSubject(data["meta"]["description"])
    for index, page in enumerate(data["pages"]):
        draw_page(c, data, page, index)
        c.showPage()
    c.save()
    print(f"Generated {out_path}")


def main() -> None:
    register_fonts()
    for data_path, out_path in TARGETS:
        build_pdf(data_path, out_path)


if __name__ == "__main__":
    main()
