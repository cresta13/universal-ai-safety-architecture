# Local visual editions

The visual PDF exporter uses the live web-book renderer, its complete localized
content, and `docs/styles.css`. `visual_pdf.css` only supplies print dimensions,
spacing, and pagination rules. Text is never summarized for export.

Run from the repository root with Python, Node.js, and Playwright Chromium
available. The current Windows exports embed the web-book's installed Trebuchet
MS and Segoe Print fonts. Other platforms may use the CSS fallback fonts and
must be visually reviewed again.

```sh
python scripts/build_site.py
node scripts/mobile_scroll_qa.js
node scripts/export_visual_pdfs.js --capture-web
python scripts/review_visual_pdfs.py --pdftoppm /path/to/pdftoppm
```

Candidates, contact sheets, and machine-readable checks are written only to
`output/pdf/`. The exporter never overwrites `public/pdfs/` or deploys anything.
The reviewer renders every page at 190 DPI, checks extracted content, embedded
fonts and links, and creates review boards and 390-pixel previews in
`tmp/task15-pdf-pages/`. Visual inspection remains necessary.

The entire 41-term glossary is included in both languages. Russian canonical
English labels are preserved. Dense sheets continue across pages; labels retain
the original P00-P19 conceptual sheet identifiers alongside PDF page numbers.

`--capture-web-only` refreshes source screenshots without recreating PDFs.
`review_visual_pdfs.py --locale en` or `--locale ru` checks one edition.

Publication uses the explicitly reviewed files committed in `public/pdfs/`.
The Pages workflow does not regenerate them. `generate_pdf.py` is the legacy
ReportLab exporter and is not used for the visual edition or deployment.
