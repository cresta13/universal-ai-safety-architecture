const http = require("http");
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const site = path.join(root, "dist");
const outDir = path.join(root, "docs", "qa", "screenshots");

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

function server() {
  return http.createServer((req, res) => {
    const url = new URL(req.url, "http://127.0.0.1");
    let filePath = path.join(site, decodeURIComponent(url.pathname));
    if (url.pathname === "/" || !path.extname(filePath)) filePath = path.join(site, "index.html");
    if (!filePath.startsWith(site)) {
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

async function main() {
  fs.mkdirSync(outDir, { recursive: true });
  const srv = server();
  await new Promise((resolve) => srv.listen(0, "127.0.0.1", resolve));
  const port = srv.address().port;
  const browser = await chromium.launch();
  try {
    const smoke = await browser.newPage({ viewport: { width: 1366, height: 768 } });
    await smoke.goto(`http://127.0.0.1:${port}/#page=guardian-architecture`, { waitUntil: "networkidle" });
    const statusText = await smoke.locator("#reader-status").innerText();
    if (!statusText.includes("Архитектура защитника полномочий")) throw new Error(`direct hash route failed: ${statusText}`);
    await smoke.keyboard.press("ArrowRight");
    const nextText = await smoke.locator("#reader-status").innerText();
    if (nextText === statusText) throw new Error("keyboard navigation did not advance");
    await smoke.click('[data-mode="scroll"]');
    if (!(await smoke.locator(".book-stage.scroll-track").count())) throw new Error("scroll mode did not activate");
    await smoke.click('[data-action="open"]');
    if (!(await smoke.locator("dialog[open]").count())) throw new Error("sheet dialog did not open");
    await smoke.keyboard.press("Escape");
    const pdfStatus = await smoke.evaluate(async () => {
      const response = await fetch("pdfs/UAIS-Manifesto-RU.pdf", { method: "HEAD" });
      return response.status;
    });
    if (pdfStatus !== 200) throw new Error(`PDF fetch failed: ${pdfStatus}`);
    await smoke.close();

    const shots = [
      ["desktop-cover.png", { width: 1440, height: 900 }, "#page=cover", "book"],
      ["desktop-p07.png", { width: 1440, height: 900 }, "#page=capability-authority-reachability", "book"],
      ["desktop-p14.png", { width: 1440, height: 900 }, "#page=hazard-disclosure-passport", "book"],
      ["desktop-p18.png", { width: 1440, height: 900 }, "#page=aria-refunds-example", "book"],
      ["mobile-cover.png", { width: 390, height: 844 }, "#page=cover", "book"],
      ["mobile-p07.png", { width: 390, height: 844 }, "#page=capability-authority-reachability", "book"],
      ["mobile-p14.png", { width: 390, height: 844 }, "#page=hazard-disclosure-passport", "book"],
      ["mobile-p18.png", { width: 390, height: 844 }, "#page=aria-refunds-example", "book"],
    ];
    for (const [name, viewport, hash, mode] of shots) {
      const page = await browser.newPage({ viewport });
      await page.goto(`http://127.0.0.1:${port}/${hash}`, { waitUntil: "networkidle" });
      await page.click(`[data-mode="${mode}"]`);
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
