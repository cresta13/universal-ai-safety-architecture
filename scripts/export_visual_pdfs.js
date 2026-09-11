const fs = require("fs/promises");
const http = require("http");
const path = require("path");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const site = path.join(root, "dist");
const output = path.join(root, "output", "pdf");
const pageWidth = 1000;
const pageHeight = 1250;
const mime = { ".html": "text/html", ".css": "text/css", ".js": "application/javascript", ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png" };

async function startServer() {
  const server = http.createServer(async (req, res) => {
    try {
      const url = new URL(req.url, "http://127.0.0.1");
      const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "");
      let file = path.resolve(site, relative);
      if (file !== site && !file.startsWith(`${site}${path.sep}`)) throw new Error("Invalid path");
      if ((await fs.stat(file)).isDirectory()) file = path.join(file, "index.html");
      res.writeHead(200, { "Content-Type": `${mime[path.extname(file)] || "application/octet-stream"}; charset=utf-8` });
      res.end(await fs.readFile(file));
    } catch {
      res.writeHead(404);
      res.end("Not found");
    }
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  return { server, url: `http://127.0.0.1:${server.address().port}` };
}

async function prepareExport(page, locale) {
  return page.evaluate(async (language) => {
    const script = document.querySelector("script[data-content]");
    const data = await fetch(script.dataset.content).then((response) => response.json());
    const originals = [...document.querySelectorAll("#book-stage > .sheet")];
    const sample = "UAIS Intelligence Возможности полномочия ≠";
    await Promise.all([
      '900 38px "Segoe Print"', '900 27px "Segoe Print"', '900 24px "Segoe Print"',
      '900 21px "Segoe Print"', '720 21px "Trebuchet MS"',
      '720 18px "Trebuchet MS"', '720 16px "Trebuchet MS"',
    ].map((font) => document.fonts.load(font, sample)));
    const exportRoot = document.createElement("main");
    exportRoot.id = "pdf-export";
    document.body.replaceChildren(exportRoot);
    document.title = `UAIS Visual Edition ${language.toUpperCase()} - Candidate 3`;

    function mount(sheet, id) {
      const wrapper = document.createElement("section");
      wrapper.className = "pdf-page";
      wrapper.dataset.pageId = id;
      wrapper.append(sheet);
      exportRoot.append(wrapper);
      return wrapper;
    }

    function fits(sheet) {
      const rect = sheet.getBoundingClientRect();
      const bottom = rect.bottom - parseFloat(getComputedStyle(sheet).paddingBottom);
      return [...sheet.children].every((child) => child.getBoundingClientRect().bottom <= bottom + 1)
        && [...sheet.querySelectorAll(".note")].every((note) => note.scrollHeight <= note.clientHeight + 2);
    }

    function emptyCopy(original, id) {
      const copy = original.cloneNode(true);
      copy.id = `pdf-${id.toLowerCase()}`;
      copy.querySelectorAll(".notes").forEach((notes) => notes.remove());
      return copy;
    }

    function makeNotes(sheet) {
      const notes = document.createElement("div");
      notes.className = "notes";
      sheet.insertBefore(notes, sheet.querySelector(".source-list"));
      return notes;
    }

    // Measure the real rendered cards. Pagination never shortens the source text.
    function paginate(original, cards, id, extraClass = "") {
      const pages = [];
      let sheet;
      let notes;
      function next() {
        sheet = emptyCopy(original, `${id}-${pages.length + 1}`);
        if (extraClass) sheet.classList.add(extraClass);
        notes = makeNotes(sheet);
        mount(sheet, id);
        pages.push(sheet);
      }
      next();
      for (let i = 0; i < cards.length; i += 2) {
        const row = cards.slice(i, i + 2).map((card) => card.cloneNode(true));
        const previousCount = notes.children.length;
        notes.append(...row);
        if (!fits(sheet)) {
          row.forEach((card) => card.remove());
          if (!previousCount) throw new Error(`${language} ${id}: a card row does not fit`);
          next();
          notes.append(...row);
          if (!fits(sheet)) throw new Error(`${language} ${id}: a card row does not fit on a new page`);
        }
      }
      // Redistribute complete rows so the last glossary page is not almost empty.
      for (let pass = 0; pass < pages.length; pass++) {
        for (let i = pages.length - 1; i > 0; i--) {
          const previous = pages[i - 1].querySelector(":scope > .notes");
          const current = pages[i].querySelector(":scope > .notes");
          if (previous.children.length < current.children.length + 3) continue;
          const row = [...previous.children].slice(-2);
          current.prepend(...row);
          if (!fits(pages[i])) previous.append(...row);
        }
      }
      if (pages.length > 1) pages.forEach((item, i) => {
        item.classList.add("pdf-continuation");
        item.dataset.part = `${i + 1}/${pages.length}`;
      });
      return pages;
    }

    const glossary = data.pages.find((item) => item.layout === "glossary");
    for (const original of originals) {
      const source = data.pages.find((item) => item.slug === original.dataset.slug);
      if (source.layout === "glossary") {
        const [sourceNotes, termNotes] = original.querySelectorAll(":scope > .notes");
        const terms = [...termNotes.children];
        terms.forEach((note, index) => {
          note.dataset.termId = data.terms[index].id;
          note.classList.remove("accent-cream");
          note.classList.add(`accent-${["cream", "blue", "pistachio", "mauve", "peach"][index % 5]}`);
        });
        paginate(original, terms, source.id);
        const sources = emptyCopy(original, "sources");
        sources.classList.add("pdf-source-page");
        sources.querySelector("h2").textContent = language === "ru" ? "Источники и права" : "Sources and rights";
        sources.querySelector("h3")?.remove();
        sources.insertBefore(sourceNotes.cloneNode(true), sources.querySelector(".source-list"));
        sources.querySelectorAll("li").forEach((item) => {
          const text = item.textContent;
          if (!/^https:\/\//.test(text) && !text.startsWith("spec/")) return;
          const link = document.createElement("a");
          link.textContent = text;
          link.href = text.startsWith("spec/") ? `${data.meta.repoUrl}/blob/main/${text}` : text;
          item.replaceChildren(link);
        });
        mount(sources, `${source.id}-sources`);
        continue;
      }
      const sheet = original.cloneNode(true);
      const wrapper = mount(sheet, source.id);
      if (!fits(sheet)) {
        const groups = original.querySelectorAll(":scope > .notes");
        if (groups.length !== 1) throw new Error(`${language} ${source.id}: special layout does not fit: ${JSON.stringify([...sheet.children].map((node) => ({ class: node.className, height: node.getBoundingClientRect().height, bottom: node.getBoundingClientRect().bottom - sheet.getBoundingClientRect().top })))}`);
        wrapper.remove();
        paginate(original, [...groups[0].children], source.id);
      }
    }

    const wrappers = [...exportRoot.children];
    wrappers.forEach((wrapper, index) => {
      const sheet = wrapper.querySelector(".sheet");
      const heading = sheet.querySelector("h2");
      heading.id = `pdf-title-${index + 1}`;
      sheet.setAttribute("aria-labelledby", heading.id);
      const part = sheet.dataset.part ? ` (${sheet.dataset.part})` : "";
      sheet.querySelector(".sheet-id").textContent = `${wrapper.dataset.pageId}${part} · ${index + 1}/${wrappers.length}`;
      sheet.querySelectorAll("a[data-slug]").forEach((link) => {
        const target = wrappers.find((item) => item.querySelector(".sheet").dataset.slug === link.dataset.slug);
        if (target) link.setAttribute("href", `#${target.querySelector(".sheet").id}`);
      });
    });

    // Local font resolution can finish after a new size is first laid out.
    await document.fonts.ready;
    await new Promise(requestAnimationFrame);

    const issues = [];
    const tolerance = 2;
    const normalize = (text) => text.replace(/\s+/g, " ").trim();
    function problem(wrapper, kind, node) {
      issues.push({ page: wrapper.dataset.pageId, kind, text: normalize(node.textContent).slice(0, 110) });
    }
    for (const wrapper of wrappers) {
      const sheet = wrapper.querySelector(".sheet");
      if (!fits(sheet)) problem(wrapper, "page-overflow", sheet);
      for (const node of sheet.querySelectorAll("h2,h3,.lead,.note,.note-title,.canonical-label,.note p,.note li,.route-line span,.decision-strip span,.source-list")) {
        const rect = node.getBoundingClientRect();
        const parent = node.closest(".note") || sheet;
        const bounds = parent.getBoundingClientRect();
        if (rect.left < bounds.left - tolerance || rect.right > bounds.right + tolerance || rect.bottom > bounds.bottom + tolerance) {
          problem(wrapper, node.matches("h2,h3,.note-title") ? "title-overflow" : "card-overflow", node);
        }
        if (node.scrollWidth > node.clientWidth + tolerance && node.clientWidth > 0) problem(wrapper, "text-overflow", node);
        if (node.matches(".note,.note p,.note li,.source-list") && node.scrollHeight > node.clientHeight + tolerance && node.clientHeight > 0) problem(wrapper, "text-height-overflow", node);
        if (["hidden", "clip"].includes(getComputedStyle(node).overflow)) problem(wrapper, "clipping-style", node);
      }
      for (const group of sheet.querySelectorAll(".notes,.guardian-column")) {
        const cards = [...group.children];
        for (let i = 0; i < cards.length; i++) {
          const a = cards[i].getBoundingClientRect();
          for (let j = i + 1; j < cards.length; j++) {
            const b = cards[j].getBoundingClientRect();
            if (Math.min(a.right, b.right) - Math.max(a.left, b.left) > tolerance && Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > tolerance) problem(wrapper, "card-overlap", cards[j]);
          }
        }
      }
    }

    const glossaryCards = [...exportRoot.querySelectorAll("[data-term-id]")];
    const duplicateLabels = glossaryCards.filter((card) => normalize(card.querySelector(".note-title").textContent) === normalize(card.querySelector(".canonical-label")?.textContent || "")).length;
    const bilingualLabels = language !== "ru" || glossaryCards.every((card) => {
      const term = data.terms.find((item) => item.id === card.dataset.termId);
      return card.querySelector(".canonical-label")?.textContent === term.canonical && card.querySelector(".note-title").textContent === term.ru;
    });
    const content = normalize(exportRoot.textContent);
    const missingContent = [];
    for (const source of data.pages) {
      for (const note of source.notes || []) {
        for (const text of [note.title, note.body, ...(note.items || [])].filter(Boolean)) {
          // Numbered headings split their number into a separate visual badge.
          const expected = normalize(text.replace(/^(\d+)\s*[·.]\s*/, "$1"));
          if (!content.includes(expected) && !(source.layout === "cover" && note.items && text === note.title)) missingContent.push({ page: source.id, text });
        }
      }
    }
    for (const term of data.terms) if (!content.includes(normalize(term.definition))) missingContent.push({ term: term.id });
    return { locale: language, pageCount: wrappers.length, pages: wrappers.map((item) => item.dataset.pageId), issues, missingContent, glossaryCount: glossaryCards.length, duplicateLabels, bilingualLabels, glossaryTitle: glossary.title };
  }, locale);
}

async function main() {
  await fs.mkdir(output, { recursive: true });
  const { server, url } = await startServer();
  const browser = await chromium.launch({ headless: true });
  const reports = [];
  try {
    for (const locale of ["en", "ru"]) {
      const context = await browser.newContext({ viewport: { width: pageWidth, height: pageHeight }, reducedMotion: "reduce" });
      const page = await context.newPage();
      await page.addInitScript(() => localStorage.setItem("uais-view-mode", "scroll"));
      await page.goto(`${url}/${locale === "ru" ? "ru/" : ""}`, { waitUntil: "networkidle" });
      await page.waitForFunction(() => document.querySelectorAll("#book-stage > .sheet").length === 20);
      if (process.argv.includes("--capture-web") || process.argv.includes("--capture-web-only")) {
        const comparisonDir = path.join(root, "tmp", "task15-web-reference");
        await fs.mkdir(comparisonDir, { recursive: true });
        await page.addStyleTag({ content: ".site-header { visibility: hidden; }" });
        for (const index of [0, 4, 7, 8, 10, 12, 14, 16, 17, 18, 19]) {
          await page.locator("#book-stage > .sheet").nth(index).screenshot({ path: path.join(comparisonDir, `${locale}-P${String(index).padStart(2, "0")}.png`) });
        }
      }
      if (process.argv.includes("--capture-web-only")) {
        await context.close();
        continue;
      }
      await page.emulateMedia({ media: "print" });
      await page.addStyleTag({ path: path.join(__dirname, "visual_pdf.css") });
      await page.evaluate(() => document.fonts.ready);
      const report = await prepareExport(page, locale);
      reports.push(report);
      await fs.writeFile(path.join(output, "visual_pdf_layout_qa.json"), JSON.stringify(reports, null, 2));
      if (report.issues.length || report.missingContent.length || report.glossaryCount !== 41 || (locale === "en" && report.duplicateLabels) || !report.bilingualLabels) {
        throw new Error(`${locale}: export validation failed: ${JSON.stringify(report)}`);
      }
      if (!process.argv.includes("--check-only")) await page.pdf({ path: path.join(output, `UAIS_Visual_Edition_${locale.toUpperCase()}_Candidate3.pdf`), width: `${pageWidth}px`, height: `${pageHeight}px`, printBackground: true, preferCSSPageSize: true, displayHeaderFooter: false, tagged: true, outline: true });
      console.log(`${locale.toUpperCase()}: ${report.pageCount} pages, ${report.glossaryCount} terms, no layout or content issues`);
      await context.close();
    }
  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
}

module.exports = { prepareExport, startServer };
if (require.main === module) main().catch((error) => { console.error(error); process.exitCode = 1; });
