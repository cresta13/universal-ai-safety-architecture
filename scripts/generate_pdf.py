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

PDF_GLOSSARY_SUMMARY = {
    "capability": "Технически доступное действие системы.",
    "legitimate-authority": "Выданное право действовать в заданных пределах.",
    "effective-reachable-authority": "Практически достижимый путь к значимому действию.",
    "illicit-reachable-authority": "Достижимый путь без выданного права.",
    "authority-ceiling": "Максимум полномочий без нового внешнего решения.",
    "capability-boundary": "Обязательная проверка перед защищённым последствием.",
    "consequence-interface": "Место, где действие достигает человека, имущества или среды.",
    "guardian": "Ограниченный наблюдатель, выпускающий доказательства, а не команды.",
    "evidence-carrying-alert": "Предупреждение, связанное с проверяемыми доказательствами.",
    "structured-evidence-package": "Пакет наблюдений, допущений, неопределённости и срока действия.",
    "deterministic-evidence-verifier": "Проверяет механические свойства доказательств, не истину мира.",
    "human-sovereignty": "Подотчётное человеческое или внешне легитимное решение.",
    "manual-sovereignty-controller": "Независимый ручной способ остановить значимую функцию.",
    "physical-sovereignty": "Внешние зависимости уже почти не ограничивают автономность.",
    "physical-sovereignty-threshold": "Порог потери эффективного внешнего ограничения.",
    "safety-passport": "Понятная карточка конфигурации, опасностей, контролей и ограничений.",
    "consumer-ai-safety-class": "Потребительский профиль видимых защитных механизмов.",
    "safety-assurance-level": "Сила процедур и доказательств; не разрешение на внедрение.",
    "ai-trustworthiness": "Наблюдаемая надёжность конкретной версии в конкретной области.",
    "authority-expansion-event": "Переход, требующий внешней проверки расширения полномочий.",
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


def draw_sources(c: canvas.Canvas, page: dict) -> None:
    files = [source.split(":")[0].strip() for source in page.get("sourceSections", [])]
    source_text = "Источники: " + "; ".join(files)
    c.setFillColor(PALETTE["soft"])
    c.setFont("UAISRegular", 6.7)
    draw_wrapped(c, source_text, 18 * mm, 12 * mm, 112, 6.7, "UAISRegular", 8)


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
) -> float:
    text_width = max(24, int((w / mm) * 0.58))
    title_lines = wrap_text(title, max(18, text_width - 4))
    canonical_lines = wrap_text(canonical or "", max(18, text_width - 2))
    body_lines = wrap_text(body or "", text_width)
    item_lines: list[str] = []
    for item in items or []:
        item_lines.extend(wrap_text(f"- {item}", max(18, text_width - 2)))
    h = max(31 * mm, (len(title_lines) * 13 + len(canonical_lines) * 8 + len(body_lines) * 10 + len(item_lines) * 10 + 20) * 1.05)
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
    if canonical_lines:
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISBold", 6.8)
        for line in canonical_lines:
            c.drawString(x + 7 * mm, cursor, line)
            cursor -= 8
        c.setFillColor(PALETTE["ink"])
    cursor -= 2
    if body:
        cursor = draw_wrapped(c, body, x + 7 * mm, cursor, text_width, 8, "UAISRegular", 10)
    if items:
        for item in items:
            cursor = draw_wrapped(c, f"- {item}", x + 7 * mm, cursor, max(18, text_width - 2), 8, "UAISRegular", 10)
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
    cursor = PAGE_H - 30 * mm
    for line in wrap_text(page["title"], 34)[:2]:
        c.drawString(margin + 4 * mm, cursor, line)
        cursor -= 19
    if page.get("subtitle"):
        c.setFont("UAISRegular", 10)
        for line in wrap_text(page["subtitle"], 82)[:2]:
            c.drawString(margin + 4 * mm, cursor - 1 * mm, line)
            cursor -= 12
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
    c.drawString(24 * mm, PAGE_H - 73 * mm, "Universal AI Safety Architecture")
    c.setFont("UAISBold", 19)
    c.drawString(24 * mm, PAGE_H - 100 * mm, "Может сделать ≠ имеет право сделать.")
    y = draw_wrapped(c, page["lead"], 24 * mm, PAGE_H - 117 * mm, 74, 11, "UAISRegular", 15)
    y -= 7 * mm
    notes = page["notes"]
    if notes:
        y = draw_note(c, 24 * mm, y, PAGE_W - 48 * mm, notes[0]["title"], notes[0].get("body", ""), notes[0].get("accent", "cream"), notes[0].get("items"), notes[0].get("canonical"))
    col_w = (PAGE_W - 54 * mm) / 2
    col_y = [y, y]
    for note_index, note in enumerate(notes[1:]):
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
        )
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
        c.roundRect(x, local_y - 23 * mm, col_w, 21.5 * mm, 3, stroke=1, fill=1)
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISBold", 6.6)
        cursor = local_y - 4.5 * mm
        for line in wrap_text(term["ru"], 27)[:2]:
            c.drawString(x + 3 * mm, cursor, line)
            cursor -= 6.9
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISBold", 5.2)
        for line in wrap_text(term["canonical"], 31)[:2]:
            c.drawString(x + 3 * mm, cursor, line)
            cursor -= 5.8
        c.setFillColor(PALETTE["ink"])
        c.setFont("UAISRegular", 5.1)
        summary = PDF_GLOSSARY_SUMMARY.get(term["id"], term["definition"])
        for line in wrap_text(summary, 34)[:4]:
            c.drawString(x + 3 * mm, cursor, line)
            cursor -= 5.8
        col_y[col] = local_y - 24.5 * mm


def draw_glossary(c: canvas.Canvas, data: dict, page: dict, index: int) -> None:
    y = draw_header(c, page, index + 1, len(data["pages"]))
    c.setFillColor(PALETTE["ink"])
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 84, 10, "UAISRegular", 13) - 3 * mm
    authority = next((term for term in data.get("terms", []) if term.get("id") == "authority"), None)
    if authority:
        y = draw_note(c, 18 * mm, y, PAGE_W - 36 * mm, authority["ru"], authority["definition"], "cream", canonical=authority["canonical"])
    version = next((note for note in page.get("notes", []) if note.get("title") == "Версия"), None)
    if version:
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISRegular", 6.8)
        y = draw_wrapped(c, version.get("body", ""), 18 * mm, y + 2 * mm, 118, 6.8, "UAISRegular", 8) - 2 * mm
    draw_glossary_terms(c, data, y)
    rights = next((note for note in page.get("notes", []) if note.get("title") == "Права"), None)
    if rights:
        c.setFillColor(PALETTE["soft"])
        c.setFont("UAISRegular", 6.6)
        draw_wrapped(c, rights.get("body", ""), 18 * mm, 24 * mm, 112, 6.6, "UAISRegular", 8)
    draw_sources(c, page)


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
    y = draw_wrapped(c, page["lead"], 18 * mm, y, 84, 10, "UAISRegular", 13) - 5 * mm
    col_w = (PAGE_W - 42 * mm) / 2
    x_positions = [18 * mm, 24 * mm + col_w]
    col_y = [y, y]
    notes = page.get("notes", [])
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
            note.get("canonical"),
        )
    draw_sources(c, page)


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
