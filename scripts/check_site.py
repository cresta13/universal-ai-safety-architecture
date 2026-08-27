from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCS = [
    "CONTENT_COVERAGE_RU.md",
    "RUSSIAN_GLOSSARY.md",
    "QA_REPORT_RU.md",
    "TRANSLATION_READINESS.md",
]
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
    "architecture-map",
    "glossary-source",
}


def fail(message: str) -> None:
    raise SystemExit(f"site check failed: {message}")


def load_json(site: Path) -> dict:
    path = site / "data" / "ru-content.json"
    if not path.exists():
        fail(f"missing {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def assert_cyrillic(value: str, field: str) -> None:
    if not re.search(r"[А-Яа-яЁё]", value or ""):
        fail(f"{field} must contain Russian text")


def check_content(data: dict) -> None:
    if data.get("locale") != "ru":
        fail("only ru locale may be active in phase 1")
    if data.get("dir") != "ltr":
        fail("ru locale must be ltr")
    future = data.get("futureLocales", [])
    if not future or any(item.get("status") != "planned" for item in future):
        fail("future locales must be configuration-only and planned")
    pages = data.get("pages", [])
    if len(pages) < 17:
        fail("not enough book pages")
    slugs = [page.get("slug") for page in pages]
    if len(slugs) != len(set(slugs)):
        fail("page slugs must be unique")
    missing = REQUIRED_SLUGS.difference(slugs)
    if missing:
        fail(f"missing required page slugs: {sorted(missing)}")
    terms = {term.get("id") for term in data.get("terms", [])}
    for page in pages:
        for field in ["id", "slug", "title", "lead", "layout", "accent"]:
            if not page.get(field):
                fail(f"page {page.get('id')} has empty {field}")
        assert_cyrillic(page["title"] + " " + page["lead"], page["slug"])
        for term_id in page.get("terms", []):
            if term_id not in terms:
                fail(f"page {page['slug']} references missing term {term_id}")
        for note in page.get("notes", []):
            text = " ".join(str(note.get(key, "")) for key in ["title", "body"])
            if note.get("items"):
                text += " " + " ".join(note["items"])
            if not text.strip():
                fail(f"empty note on page {page['slug']}")
    for term in data.get("terms", []):
        for field in ["canonical", "ru", "definition", "avoid", "pages"]:
            if not term.get(field):
                fail(f"term {term.get('id')} has empty {field}")


def check_files(site: Path, data: dict, source_mode: bool) -> None:
    html = site / "index.html"
    if not html.exists():
        fail("missing index.html")
    text = html.read_text(encoding="utf-8")
    if 'lang="ru"' not in text:
        fail("index.html must declare lang ru")
    if 'lang="en"' in text:
        fail("index.html must not declare English active locale")
    if "Скачать PDF" not in text:
        fail("PDF button text missing")
    if "language" in text.lower() or "язык" in text.lower():
        fail("phase 1 must not expose an active language switcher")
    for asset in ["styles.css", "app.js", "assets/uais-favicon.svg", "assets/og-ru.png", "robots.txt", "sitemap.xml"]:
        if not (site / asset).exists():
            fail(f"missing {asset}")
    pdf_path = site / data["meta"]["pdfPath"]
    if source_mode and not pdf_path.exists():
        pdf_path = ROOT / "public" / data["meta"]["pdfPath"]
    if not pdf_path.exists() or pdf_path.stat().st_size < 10_000:
        fail(f"PDF missing or too small: {pdf_path}")
    if source_mode:
        for doc in REQUIRED_DOCS:
            if not (site / doc).exists():
                fail(f"missing {doc}")
        for shot in ["desktop-cover.png", "desktop-guardian.png", "mobile-cover.png", "mobile-scroll.png"]:
            if not (site / "qa" / "screenshots" / shot).exists():
                fail(f"missing screenshot {shot}")


def check_source_links(data: dict) -> None:
    for page in data["pages"]:
        for source in page.get("sourceSections", []):
            file_name = source.split(":")[0].strip()
            candidates = [ROOT / "spec" / file_name, ROOT / file_name]
            if not any(path.exists() for path in candidates):
                fail(f"source reference not found for page {page['slug']}: {file_name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="docs", help="site directory to validate")
    args = parser.parse_args()
    site = (ROOT / args.site).resolve()
    data = load_json(site)
    check_content(data)
    check_source_links(data)
    check_files(site, data, source_mode=site == (ROOT / "docs").resolve())
    print(f"Site check passed for {site}")


if __name__ == "__main__":
    main()
