const http = require("http");
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const site = path.join(root, "dist");
const results = [];

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

async function installMutationCounter(page) {
  await page.evaluate(() => {
    window.__uaisStageMutations = 0;
    window.__uaisObservedScroll = [];
    window.__uaisObserver?.disconnect();
    window.__uaisObserver = new MutationObserver((mutations) => {
      window.__uaisStageMutations += mutations.filter((mutation) => mutation.type === "childList").length;
    });
    window.__uaisObserver.observe(document.querySelector("#book-stage"), { childList: true });
  });
}

async function resetMutationCounter(page) {
  await page.evaluate(() => {
    window.__uaisStageMutations = 0;
  });
}

async function stageMutations(page) {
  return page.evaluate(() => window.__uaisStageMutations || 0);
}

async function assertNoHeightResizeRerender(page, viewport, label) {
  await resetMutationCounter(page);
  const before = await page.evaluate(() => window.scrollY);
  await page.setViewportSize({ width: viewport.width, height: Math.max(620, viewport.height - 96) });
  await page.waitForTimeout(150);
  await page.setViewportSize(viewport);
  await page.waitForTimeout(150);
  const after = await page.evaluate(() => window.scrollY);
  const mutations = await stageMutations(page);
  if (mutations !== 0) {
    throw new Error(`${label}: height-only resize rerendered the book stage ${mutations} time(s)`);
  }
  if (Math.abs(after - before) > 2) {
    throw new Error(`${label}: height-only resize moved scrollY from ${before} to ${after}`);
  }
}

async function dispatchTouchSwipe(page, from, to) {
  const client = await page.context().newCDPSession(page);
  await client.send("Input.dispatchTouchEvent", {
    type: "touchStart",
    touchPoints: [{ x: from.x, y: from.y }],
  });
  for (let step = 1; step <= 8; step++) {
    await client.send("Input.dispatchTouchEvent", {
      type: "touchMove",
      touchPoints: [{ x: from.x + (to.x - from.x) * step / 8, y: from.y + (to.y - from.y) * step / 8 }],
    });
    await page.waitForTimeout(25);
  }
  await client.send("Input.dispatchTouchEvent", {
    type: "touchEnd",
    touchPoints: [],
  });
  await client.detach();
  await waitForScrollSettled(page);
}

async function waitForScrollSettled(page) {
  let previous = -1;
  let stable = 0;
  for (let attempt = 0; attempt < 50; attempt++) {
    await page.waitForTimeout(80);
    const current = await page.evaluate(() => window.scrollY);
    stable = Math.abs(current - previous) < 1 ? stable + 1 : 0;
    if (stable >= 3) return;
    previous = current;
  }
  throw new Error("Scrolling did not settle");
}

async function readerStatus(page) {
  return page.locator("#reader-status").innerText();
}

async function assertDiagonalScrollDoesNotTurn(page, label) {
  const before = await readerStatus(page);
  await dispatchTouchSwipe(page, { x: 190, y: 690 }, { x: 252, y: 210 });
  const after = await readerStatus(page);
  if (after !== before) {
    throw new Error(`${label}: diagonal vertical gesture changed page from "${before}" to "${after}"`);
  }
}

async function assertHorizontalSwipeTurns(page, label) {
  const before = await readerStatus(page);
  await dispatchTouchSwipe(page, { x: 310, y: 530 }, { x: 120, y: 520 });
  const after = await readerStatus(page);
  if (after === before) {
    const target = await page.evaluate(() => ({ scrollY, target: document.elementFromPoint(310, 530)?.outerHTML.slice(0, 200) }));
    throw new Error(`${label}: clear horizontal swipe did not turn page: ${JSON.stringify(target)}`);
  }
}

async function openIsolatedPage(browser, baseUrl, route, viewport, mode) {
  const context = await browser.newContext({
    viewport,
    isMobile: true,
    hasTouch: true,
  });
  const page = await context.newPage();
  await page.addInitScript((initialMode) => localStorage.setItem("uais-view-mode", initialMode), mode);
  await page.goto(`${baseUrl}${route}`, { waitUntil: "networkidle" });
  await page.waitForSelector(".sheet");
  if (!route.includes("#")) await page.locator("#book").evaluate((node) => node.scrollIntoView());
  await waitForScrollSettled(page);
  await installMutationCounter(page);
  return { context, page };
}

async function scenarioScrollMode(browser, baseUrl, route, viewport, label) {
  const { context, page } = await openIsolatedPage(browser, baseUrl, route, viewport, "scroll");
  try {
    const initialStatus = await readerStatus(page);
    const initialHash = await page.evaluate(() => location.hash);
    await page.evaluate(() => window.scrollBy(0, 300));
    await waitForScrollSettled(page);
    await assertNoHeightResizeRerender(page, viewport, `${label} scroll mid-sheet`);
    for (let step = 0; step < 3; step++) {
      const before = await page.evaluate(() => scrollY);
      await assertDiagonalScrollDoesNotTurn(page, `${label} scroll`);
      const after = await page.evaluate(() => scrollY);
      if (after < before - 2) throw new Error(`${label}: downward reading jumped upward`);
      await assertNoHeightResizeRerender(page, viewport, `${label} scroll lower ${step}`);
    }
    const beforeSwipe = await readerStatus(page);
    await dispatchTouchSwipe(page, { x: 310, y: 530 }, { x: 120, y: 520 });
    if (await readerStatus(page) !== beforeSwipe) throw new Error(`${label}: scroll mode horizontal gesture turned a page`);
    if (await readerStatus(page) !== initialStatus || await page.evaluate(() => location.hash) !== initialHash) {
      throw new Error(`${label}: ordinary scrolling changed navigation state`);
    }
    if (route.includes("p14")) {
      fs.mkdirSync(path.join(root, "tmp", "task15-mobile"), { recursive: true });
      await page.screenshot({ path: path.join(root, "tmp", "task15-mobile", `${label.replace(/[^a-z0-9]+/gi, "-")}.png`) });
    }
    results.push({ route, viewport, mode: "scroll", heightOnlyRerenders: 0, unexpectedJumps: 0, accidentalPageTurns: 0 });
  } finally {
    await context.close();
  }
}

async function scenarioBookMode(browser, baseUrl, route, viewport, label) {
  const { context, page } = await openIsolatedPage(browser, baseUrl, route, viewport, "book");
  try {
    await assertNoHeightResizeRerender(page, viewport, `${label} book`);
    await assertDiagonalScrollDoesNotTurn(page, `${label} book`);
    await assertHorizontalSwipeTurns(page, `${label} book`);
    results.push({ route, viewport, mode: "book", heightOnlyRerenders: 0, unexpectedJumps: 0, accidentalPageTurns: 0 });
  } finally {
    await context.close();
  }
}

async function main() {
  const srv = server();
  await new Promise((resolve) => srv.listen(0, "127.0.0.1", resolve));
  const port = srv.address().port;
  const baseUrl = `http://127.0.0.1:${port}`;
  const browser = await chromium.launch();
  try {
    for (const viewport of [{ width: 390, height: 844 }, { width: 430, height: 932 }]) {
      for (const route of ["/ru/", "/ru/#p07", "/ru/#p14", "/ru/#p18"]) {
        const label = `ru ${route.split("#")[1] || "p00"} ${viewport.width}x${viewport.height}`;
        await scenarioScrollMode(browser, baseUrl, route, viewport, label);
        await scenarioBookMode(browser, baseUrl, route, viewport, label);
      }
      await scenarioScrollMode(browser, baseUrl, "/#p14", viewport, `en p14 ${viewport.width}x${viewport.height}`);
      await scenarioBookMode(browser, baseUrl, "/#p07", viewport, `en p07 ${viewport.width}x${viewport.height}`);
    }
    const { context, page } = await openIsolatedPage(browser, baseUrl, "/#p07", { width: 1000, height: 900 }, "book");
    await page.setViewportSize({ width: 1200, height: 900 });
    await page.waitForFunction(() => document.querySelectorAll("#book-stage > .sheet").length === 2);
    await page.setViewportSize({ width: 1000, height: 900 });
    await page.waitForFunction(() => document.querySelectorAll("#book-stage > .sheet").length === 1);
    await context.close();
  } finally {
    await browser.close();
    srv.close();
  }
  fs.mkdirSync(path.join(root, "output", "pdf"), { recursive: true });
  fs.writeFileSync(path.join(root, "output", "pdf", "mobile_scroll_qa.json"), JSON.stringify({ scenarios: results, breakpointChange: "passed" }, null, 2));
  console.log(`Mobile scroll QA passed: ${results.length} scenarios and spread breakpoint changes`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
