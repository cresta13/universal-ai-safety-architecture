const http = require("http");
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const site = path.join(root, "dist");
const outDir = path.join(root, "tmp", "screenshots");

const mime = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".pdf": "application/pdf",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
};

function resolveRequestPath(urlPath) {
  const decoded = decodeURIComponent(urlPath);
  let filePath = path.normalize(path.join(site, decoded));
  if (!filePath.startsWith(site)) return null;
  if (decoded.endsWith("/")) {
    filePath = path.join(filePath, "index.html");
  } else if (!path.extname(filePath)) {
    const nestedIndex = path.join(filePath, "index.html");
    filePath = fs.existsSync(nestedIndex) ? nestedIndex : path.join(site, "index.html");
  }
  return filePath;
}

function server() {
  return http.createServer((req, res) => {
    const url = new URL(req.url, "http://127.0.0.1");
    const filePath = resolveRequestPath(url.pathname);
    if (!filePath) {
      res.writeHead(403);
      res.end("Forbidden");
      return;
    }
    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(404);
        res.end("Not found");
        return;
      }
      res.writeHead(200, { "content-type": mime[path.extname(filePath)] || "application/octet-stream" });
      res.end(data);
    });
  });
}

async function assertNoOverflow(page, label) {
  const overflow = await page.evaluate(() => ({
    clientWidth: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    bodyScrollWidth: document.body.scrollWidth,
  }));
  if (overflow.scrollWidth > overflow.clientWidth + 2 || overflow.bodyScrollWidth > overflow.clientWidth + 2) {
    throw new Error(`${label}: horizontal overflow ${JSON.stringify(overflow)}`);
  }
}

async function assertNoConsoleErrors(page, label, callback) {
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await callback();
  if (errors.length) throw new Error(`${label}: console errors: ${errors.join(" | ")}`);
}

async function assertNoDuplicateIds(page, label) {
  const duplicates = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map((node) => node.id).filter(Boolean);
    return ids.filter((id, index) => ids.indexOf(id) !== index);
  });
  if (duplicates.length) throw new Error(`${label}: duplicate ids ${[...new Set(duplicates)].join(", ")}`);
}

async function assertNoBrokenInternalLinks(page, label) {
  const broken = await page.evaluate(async () => {
    const links = [...document.querySelectorAll('a[href]:not([href^="http"]):not([href^="#"])')].map((a) => a.getAttribute("href"));
    const failures = [];
    for (const href of links) {
      const response = await fetch(href, { method: "HEAD" });
      if (!response.ok) failures.push(`${href} -> ${response.status}`);
    }
    return failures;
  });
  if (broken.length) throw new Error(`${label}: broken links ${broken.join(", ")}`);
}

async function smokePage(page, url, expectedLang, expectedStatus, label) {
  await page.goto(url, { waitUntil: "networkidle" });
  await page.waitForSelector(".sheet");
  const lang = await page.locator("html").getAttribute("lang");
  if (lang !== expectedLang) throw new Error(`${label}: expected lang ${expectedLang}, got ${lang}`);
  const statusText = await page.locator("#reader-status").innerText();
  if (!statusText.includes(expectedStatus)) throw new Error(`${label}: direct hash route failed: ${statusText}`);
  await assertNoOverflow(page, label);
  await assertNoDuplicateIds(page, label);
}

async function main() {
  fs.mkdirSync(outDir, { recursive: true });
  const srv = server();
  await new Promise((resolve) => srv.listen(0, "127.0.0.1", resolve));
  const port = srv.address().port;
  const browser = await chromium.launch();
  try {
    const smoke = await browser.newPage({ viewport: { width: 1366, height: 768 } });
    await assertNoConsoleErrors(smoke, "root-en", async () => {
      await smokePage(smoke, `http://127.0.0.1:${port}/#p08`, "en", "Guardian Architecture", "root-en");
    });
    await assertNoBrokenInternalLinks(smoke, "root-en");
    const ruLinksOnRoot = await smoke.locator('a[href*="ru/"], a[href="/ru/"], a[href="./ru/"]').count();
    if (ruLinksOnRoot) throw new Error("root exposes the hidden Russian route");
    const heroPosition = await smoke.locator(".intro-paper").evaluate((node) => getComputedStyle(node).position);
    if (heroPosition === "fixed" || heroPosition === "sticky") throw new Error(`hero uses disallowed position: ${heroPosition}`);
    await smoke.keyboard.press("ArrowRight");
    const nextText = await smoke.locator("#reader-status").innerText();
    if (!nextText.includes("Three views of authority")) throw new Error(`keyboard navigation did not advance: ${nextText}`);
    await smoke.click('[data-mode="scroll"]');
    if (!(await smoke.locator(".book-stage.scroll-track").count())) throw new Error("scroll mode did not activate");
    await smoke.click('[data-action="open"]');
    if (!(await smoke.locator("dialog[open]").count())) throw new Error("sheet dialog did not open");
    await smoke.keyboard.press("Escape");
    await smoke.goto(`http://127.0.0.1:${port}/#p19`, { waitUntil: "networkidle" });
    await smoke.waitForSelector(".sheet-glossary");
    const duplicatedEnglishGlossaryLabels = await smoke.locator(".sheet-glossary .canonical-label", {
      hasText: /^(Capability|Authority|Authority Ceiling|Safety Passport)$/,
    }).count();
    if (duplicatedEnglishGlossaryLabels) {
      throw new Error(`English glossary duplicates labels: ${duplicatedEnglishGlossaryLabels}`);
    }
    const enPdfStatus = await smoke.evaluate(async () => (await fetch("pdfs/UAIS-Manifesto-EN.pdf", { method: "HEAD" })).status);
    if (enPdfStatus !== 200) throw new Error(`English PDF fetch failed: ${enPdfStatus}`);
    await smoke.close();

    const ruSmoke = await browser.newPage({ viewport: { width: 390, height: 844 } });
    await assertNoConsoleErrors(ruSmoke, "ru-hidden", async () => {
      await smokePage(ruSmoke, `http://127.0.0.1:${port}/ru/#p12`, "ru", "Суверенитет человека", "ru-hidden");
    });
    const robots = await ruSmoke.locator('meta[name="robots"]').getAttribute("content");
    if (robots !== "noindex, nofollow") throw new Error(`ru route must be noindex, got ${robots}`);
    const ruLeadCount = await ruSmoke.locator(".sheet-sovereignty > .lead").count();
    if (ruLeadCount !== 1) throw new Error(`P12 lead duplicated: ${ruLeadCount}`);
    await ruSmoke.goto(`http://127.0.0.1:${port}/ru/#p19`, { waitUntil: "networkidle" });
    await ruSmoke.waitForSelector(".sheet-glossary");
    const russianCanonicalLabels = await ruSmoke.locator(".sheet-glossary .canonical-label", {
      hasText: "Legitimate Authority, LA",
    }).count();
    if (!russianCanonicalLabels) throw new Error("Russian glossary lost English canonical labels");
    const ruPdfStatus = await ruSmoke.evaluate(async () => (await fetch("../pdfs/UAIS-Manifesto-RU.pdf", { method: "HEAD" })).status);
    if (ruPdfStatus !== 200) throw new Error(`Russian PDF fetch failed: ${ruPdfStatus}`);
    await ruSmoke.close();

    const shots = [
      ["en-1440-p00.png", { width: 1440, height: 900 }, "/#p00", "book"],
      ["en-1440-p04.png", { width: 1440, height: 900 }, "/#p04", "book"],
      ["en-1440-p08.png", { width: 1440, height: 900 }, "/#p08", "book"],
      ["en-1440-p14.png", { width: 1440, height: 900 }, "/#p14", "book"],
      ["en-1440-p16.png", { width: 1440, height: 900 }, "/#p16", "book"],
      ["en-1440-p17.png", { width: 1440, height: 900 }, "/#p17", "book"],
      ["en-1440-p19.png", { width: 1440, height: 900 }, "/#p19", "book"],
      ["en-390-p00.png", { width: 390, height: 844 }, "/#p00", "book"],
      ["en-430-p14.png", { width: 430, height: 932 }, "/#p14", "book"],
      ["en-390-p19.png", { width: 390, height: 844 }, "/#p19", "book"],
      ["ru-1440-p12.png", { width: 1440, height: 900 }, "/ru/#p12", "book"],
      ["ru-390-p19.png", { width: 390, height: 844 }, "/ru/#p19", "book"],
    ];
    for (const [name, viewport, route, mode] of shots) {
      const page = await browser.newPage({ viewport });
      await page.goto(`http://127.0.0.1:${port}${route}`, { waitUntil: "networkidle" });
      await page.waitForSelector(".sheet");
      await page.click(`[data-mode="${mode}"]`);
      await assertNoOverflow(page, name);
      await page.screenshot({ path: path.join(outDir, name), fullPage: true });
      await page.close();
    }
  } finally {
    await browser.close();
    srv.close();
  }
  console.log(`Screenshots saved to ${outDir}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
