from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PAGE_COUNT = 20
REQUIRED_SLUGS = {
    "cover",
    "contents",
    "what-is-uais",
    "how-uais-emerged",
    "ten-principles-1",
    "ten-principles-2",
    "stage-i-stage-ii",
    "capability-authority-reachability",
    "guardian-architecture",
    "authority-ceiling-expansion",
    "la-era-ira",
    "classification",
    "human-physical-sovereignty",
    "metrics-assurance",
    "hazard-disclosure-passport",
    "replication-production-coalitions",
    "aive-evolution-open-research",
    "architecture-map",
    "aria-refunds-example",
    "glossary-source",
}
PUBLIC_QA_ARTIFACTS = [
    "CONTENT_COVERAGE_RU.md",
    "RUSSIAN_GLOSSARY.md",
    "QA_REPORT_RU.md",
    "TRANSLATION_READINESS.md",
    "qa",
]
FORBIDDEN_PUBLIC_STRINGS = [
    "QA-отчёт",
    "QA report",
    "CONTENT_COVERAGE",
    "TRANSLATION_READINESS",
    "Translation readiness",
    "RUSSIAN_GLOSSARY",
    "Проверочные материалы",
    "Переводы не опубликованы",
    "этап 1",
    "ЭТАП 1",
]


def fail(message: str) -> None:
    raise SystemExit(f"site check failed: {message}")


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing {path}")
    return path.read_text(encoding="utf-8")


def load_json(site: Path, name: str) -> dict:
    path = site / "data" / name
    if not path.exists():
        fail(f"missing {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def page_by_id(data: dict, page_id: str) -> dict:
    for page in data.get("pages", []):
        if page.get("id") == page_id:
            return page
    fail(f"missing page {page_id}")


def collect_page_text(page: dict) -> str:
    chunks = [
        str(page.get("title", "")),
        str(page.get("subtitle", "")),
        str(page.get("lead", "")),
    ]
    for note in page.get("notes", []):
        chunks.extend(str(note.get(key, "")) for key in ["title", "canonical", "body"])
        chunks.extend(str(item) for item in note.get("items", []))
    if page.get("route"):
        chunks.extend(str(item) for item in page["route"])
    if page.get("strip"):
        chunks.extend(str(item) for item in page["strip"])
    return "\n".join(chunks)


def all_content_text(data: dict) -> str:
    term_text = "\n".join(
        "\n".join(str(term.get(key, "")) for key in ["canonical", "label", "ru", "definition", "pdfSummary"])
        for term in data.get("terms", [])
    )
    return "\n".join(collect_page_text(page) for page in data.get("pages", [])) + "\n" + term_text


def check_content_shape(data: dict, locale: str) -> None:
    if data.get("locale") != locale:
        fail(f"{locale} content declares wrong locale: {data.get('locale')}")
    if data.get("dir") != "ltr":
        fail(f"{locale} content must be ltr")
    pages = data.get("pages", [])
    if len(pages) != REQUIRED_PAGE_COUNT:
        fail(f"{locale}: expected {REQUIRED_PAGE_COUNT} pages, got {len(pages)}")
    slugs = [page.get("slug") for page in pages]
    if len(slugs) != len(set(slugs)):
        fail(f"{locale}: page slugs must be unique")
    missing = REQUIRED_SLUGS.difference(slugs)
    if missing:
        fail(f"{locale}: missing required page slugs: {sorted(missing)}")
    terms = {term.get("id") for term in data.get("terms", [])}
    for page in pages:
        for field in ["id", "slug", "title", "lead", "layout", "accent"]:
            if not page.get(field):
                fail(f"{locale}: page {page.get('id')} has empty {field}")
        for term_id in page.get("terms", []):
            if term_id not in terms:
                fail(f"{locale}: page {page['slug']} references missing term {term_id}")
        for note in page.get("notes", []):
            text = " ".join(str(note.get(key, "")) for key in ["title", "body"])
            if note.get("items"):
                text += " " + " ".join(note["items"])
            if not text.strip():
                fail(f"{locale}: empty note on page {page['slug']}")
    for term in data.get("terms", []):
        for field in ["canonical", "definition", "avoid", "pages"]:
            if not term.get(field):
                fail(f"{locale}: term {term.get('id')} has empty {field}")
        if locale == "ru" and not term.get("ru"):
            fail(f"ru: term {term.get('id')} has empty ru label")
        if locale == "en" and not term.get("label"):
            fail(f"en: term {term.get('id')} has empty label")


def check_ru_semantics(data: dict) -> None:
    text = all_content_text(data)
    forbidden = [
        "системно-нейтральная",
        "Consumer Safety Passport",
        "незаконно достижимое",
        "Материальное расширение capability",
        "Unknown не является",
        "законное полномочие",
        "Три вида полномочий",
        "фактически достижимый объём",
    ]
    for phrase in forbidden:
        if phrase in text:
            fail(f"ru: forbidden stale wording remains: {phrase}")

    p00 = page_by_id(data, "P00")
    if "этап" in p00.get("kicker", "").lower():
        fail("ru: P00 must not expose phase/stage marker")
    p07 = collect_page_text(page_by_id(data, "P07"))
    if "Работающий технический путь не превращается в легитимное полномочие" not in p07:
        fail("ru: P07 key sentence is missing")
    p10 = page_by_id(data, "P10")
    if p10.get("title") != "Три представления о полномочиях: LA, ERA и IRA":
        fail("ru: P10 title is wrong")
    if p10.get("subtitle") != "Что выдано, что фактически достижимо и что достижимо без легитимного мандата":
        fail("ru: P10 subtitle is wrong")
    p11 = collect_page_text(page_by_id(data, "P11"))
    if "Насколько сильное физическое воздействие система способна вызвать" not in p11:
        fail("ru: P11 Physical Consequence wording is missing")
    p18 = collect_page_text(page_by_id(data, "P18"))
    for phrase in [
        "LA: легитимно разрешены возвраты до $50",
        "ERA: технически достижим путь возврата до $10 000",
        "IRA: достижимая часть сверх выданного легитимного полномочия",
        "Три месяца в этом примере — условный срок компании",
    ]:
        if phrase not in p18:
            fail(f"ru: P18 missing required text: {phrase}")
    terms = {term["id"]: term for term in data.get("terms", [])}
    exact_terms = {
        "capability-boundary": "Контролируемая граница, через которую система получает, использует или пытается расширить значимую возможность.",
        "consequence-interface": "Точка, через которую действие достигает защищаемого мира: денег, цифровых систем, физических устройств, производства, людей, имущества или среды.",
        "human-sovereignty": "Сохранение независимого внешнего контроля и легитимного решения на критических границах.",
        "physical-sovereignty": "Способность автономной системы поддерживать и расширять значимую физическую деятельность без критической зависимости от контролируемой людьми инфраструктуры.",
        "physical-sovereignty-threshold": "Порог, после которого критические человечески контролируемые зависимости больше не удерживают способность системы поддерживать и расширять значимую физическую деятельность.",
        "consumer-ai-safety-class": "Профиль применимых защитных механизмов и доказательств для заявленного диапазона последствий; не общий балл безопасности и не разрешение на работу.",
    }
    for term_id, expected in exact_terms.items():
        if terms.get(term_id, {}).get("definition") != expected:
            fail(f"ru: term {term_id} definition is not the Task12 wording")


def check_en_semantics(data: dict) -> None:
    if data.get("meta", {}).get("title") != "UAIS — Intelligence Does Not Imply Authority":
        fail("en: title is wrong")
    if data.get("meta", {}).get("description") != (
        "A plain-language visual introduction to the Universal AI Safety Architecture (UAIS): "
        "capability boundaries, legitimate authority, reachable authority, evidence, human sovereignty, "
        "safety assurance, and open research."
    ):
        fail("en: description is wrong")
    text = all_content_text(data)
    for phrase in [
        "Can do ≠ may do",
        "UAIS does not limit intelligence. It limits unaccountable power.",
        "A working technical path does not become legitimate authority because it works.",
        "SAL indicates the strength of procedures and evidence. It does not grant authority",
        "This is a research architecture and public draft, not a promise of complete implementability.",
    ]:
        if phrase not in text:
            fail(f"en: missing required semantic text: {phrase}")
    p18 = collect_page_text(page_by_id(data, "P18"))
    for phrase in [
        "LA: legitimate refunds up to $50 are granted",
        "ERA: a refund path up to $10,000 is technically reachable",
        "IRA: the reachable part above the granted legitimate authority",
    ]:
        if phrase not in p18:
            fail(f"en: P18 missing required notation: {phrase}")


def check_source_links(*datasets: dict) -> None:
    for data in datasets:
        for page in data["pages"]:
            for source in page.get("sourceSections", []):
                file_name = source.split(":")[0].strip()
                candidates = [ROOT / "spec" / file_name, ROOT / file_name]
                if not any(path.exists() for path in candidates):
                    fail(f"source reference not found for page {page['slug']}: {file_name}")


def check_public_files(site: Path, source_mode: bool) -> None:
    root_html = read_text(site / "index.html")
    ru_html = read_text(site / "ru" / "index.html")
    if '<html lang="en"' not in root_html:
        fail("root index.html must declare English")
    if "<title>UAIS — Intelligence Does Not Imply Authority</title>" not in root_html:
        fail("root title is wrong")
    if 'href="ru/' in root_html or 'href="/ru/' in root_html or "Русская версия" in root_html:
        fail("root must not expose the hidden Russian route")
    if '<html lang="ru"' not in ru_html:
        fail("ru/index.html must declare Russian")
    if 'name="robots" content="noindex, nofollow"' not in ru_html:
        fail("ru/index.html must be noindex")
    for name, html in [("root", root_html), ("ru", ru_html)]:
        for phrase in FORBIDDEN_PUBLIC_STRINGS:
            if phrase in html:
                fail(f"{name}: forbidden public QA/stage text remains: {phrase}")
    for asset in [
        "styles.css",
        "app.js",
        "assets/uais-favicon.svg",
        "assets/og-en.png",
        "assets/og-ru.png",
        "robots.txt",
        "sitemap.xml",
        "data/en-content.json",
        "data/ru-content.json",
    ]:
        if not (site / asset).exists():
            fail(f"missing {asset}")
    for artifact in PUBLIC_QA_ARTIFACTS:
        if (site / artifact).exists():
            fail(f"public QA/development artifact must not be shipped: {artifact}")
    sitemap = read_text(site / "sitemap.xml")
    if "/ru/" in sitemap:
        fail("sitemap must not expose hidden Russian route")
    if "universal-ai-safety-architecture/" not in sitemap:
        fail("sitemap must include public root")
    pdf_base = site if not source_mode else ROOT / "public"
    for pdf in ["pdfs/UAIS-Manifesto-EN.pdf", "pdfs/UAIS-Manifesto-RU.pdf"]:
        path = pdf_base / pdf
        if not path.exists() or path.stat().st_size < 10_000:
            fail(f"PDF missing or too small: {path}")


def check_app_for_hardcoding(site: Path) -> None:
    app = read_text(site / "app.js")
    for phrase in ["data/ru-content.json", "Ссылка на текущий лист скопирована.", "Источники: "]:
        if phrase in app:
            fail(f"app.js still hardcodes localized text: {phrase}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="docs", help="site directory to validate")
    args = parser.parse_args()
    site = (ROOT / args.site).resolve()
    source_mode = site == (ROOT / "docs").resolve()
    en = load_json(site, "en-content.json")
    ru = load_json(site, "ru-content.json")
    check_content_shape(en, "en")
    check_content_shape(ru, "ru")
    check_en_semantics(en)
    check_ru_semantics(ru)
    check_source_links(en, ru)
    check_public_files(site, source_mode=source_mode)
    check_app_for_hardcoding(site)
    print(f"Site check passed for {site}")


if __name__ == "__main__":
    main()
