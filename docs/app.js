(() => {
  const state = {
    data: null,
    pageIndex: 0,
    mode: localStorage.getItem("uais-view-mode") || "book",
    touchStartX: 0,
  };

  const stage = document.querySelector("#book-stage");
  const shell = document.querySelector(".book-shell");
  const status = document.querySelector("#reader-status");
  const dialog = document.querySelector("#sheet-dialog");
  const dialogContent = document.querySelector("#dialog-content");

  const accentClass = (accent) => `accent-${accent || "cream"}`;
  const slugHash = (slug) => `#page=${encodeURIComponent(slug)}`;
  const isWideSpread = () => window.matchMedia("(min-width: 1081px)").matches;

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }

  function canonicalLabel(text) {
    return text ? el("small", "canonical-label", text) : null;
  }

  function noteElement(note, index) {
    const box = el("section", `note ${accentClass(note.accent)}`);
    if (note.title) {
      const title = el("b", "note-title");
      if (/^\d+\s*[·.]/.test(note.title)) {
        const match = note.title.match(/^(\d+)\s*[·.]?\s*(.*)$/);
        const number = el("span", "principle-number", match?.[1] || String(index + 1));
        const text = el("span", "", match?.[2] || note.title);
        title.append(number, text);
      } else {
        title.textContent = note.title;
      }
      box.append(title);
      const canonical = canonicalLabel(note.canonical);
      if (canonical) box.append(canonical);
    }
    if (note.body) box.append(el("p", "", note.body));
    if (Array.isArray(note.items) && note.items.length) {
      const list = el("ul");
      note.items.forEach((item) => list.append(el("li", "", item)));
      box.append(list);
    }
    box.dataset.kind = note.kind || "note";
    return box;
  }

  function sourceLinks(page) {
    const wrap = el("div", "source-list");
    wrap.append(el("span", "", "Источники: "));
    (page.sourceSections || []).forEach((source, index) => {
      const file = source.split(":")[0].trim();
      const link = el("a", "", file);
      link.href = `https://github.com/cresta13/universal-ai-safety-architecture/blob/main/spec/${file}`;
      if (!file.endsWith(".md") || file === "NOTICE.md" || file === "CITATION.md") {
        link.href = `https://github.com/cresta13/universal-ai-safety-architecture/blob/main/${file}`;
      }
      link.target = "_blank";
      link.rel = "noreferrer";
      wrap.append(link);
      if (index < page.sourceSections.length - 1) wrap.append(document.createTextNode(" "));
    });
    return wrap;
  }

  function renderRouteLine(items) {
    const route = el("div", "route-line");
    items.forEach((item) => route.append(el("span", "", item)));
    return route;
  }

  function renderSpecial(page, sheet) {
    if (page.layout === "cover") {
      const mark = el("div", "cover-mark");
      const img = document.createElement("img");
      img.src = "assets/uais-favicon.svg";
      img.alt = "";
      const text = el("div", "cover-title");
      const heading = el("h2", "", page.title);
      heading.id = `${page.slug}-title`;
      text.append(heading, el("p", "lead", page.lead));
      mark.append(img, text);
      sheet.append(mark);
      const routeNote = page.notes.find((note) => note.items);
      if (routeNote) sheet.append(renderRouteLine(routeNote.items));
      return true;
    }

    if (page.layout === "toc") {
      const list = el("div", "toc-list");
      state.data.pages.forEach((item) => {
        const link = el("a");
        link.href = slugHash(item.slug);
        link.dataset.slug = item.slug;
        link.append(el("b", "", item.id), el("span", "", item.title));
        list.append(link);
      });
      sheet.append(el("p", "lead", page.lead), list);
      return true;
    }

    if (page.layout === "guardian") {
      sheet.append(el("p", "lead", page.lead));
      const board = el("div", "guardian-board");
      const left = el("div", "guardian-column");
      const right = el("div", "guardian-column");
      page.notes.slice(0, 4).forEach((note, index) => left.append(noteElement(note, index)));
      page.notes.slice(4).forEach((note, index) => right.append(noteElement(note, index + 4)));
      const boundary = el("div", "boundary-note");
      boundary.append(el("span", "", "ВИДЕТЬ ≠ ДЕЙСТВОВАТЬ"), el("small", "", "доказательство проходит, управляющий сигнал нет"));
      board.append(left, boundary, right);
      sheet.append(board, el("div", "blocked-signal", "×"));
      return true;
    }

    if (page.layout === "map") {
      sheet.append(el("p", "lead", page.lead));
      sheet.append(renderRouteLine(page.route || ["запрос на возможность", "граница возможностей", "разрешённый диапазон", "интерфейс последствий", "защищённое последствие"]));
      const notes = el("div", "notes");
      page.notes.forEach((note, index) => notes.append(noteElement(note, index)));
      sheet.append(notes);
      return true;
    }

    if (page.layout === "sovereignty" || page.layout === "authority") {
      sheet.append(el("p", "lead", page.lead));
      const strip = el("div", "decision-strip");
      strip.append(el("span", "", page.layout === "sovereignty" ? "человек сохраняет внешний путь" : "разрешённое"));
      strip.append(el("span", "", page.layout === "sovereignty" ? "ИИ-путь не отменяет физический контроль" : "достижимое"));
      sheet.append(strip);
      return false;
    }

    return false;
  }

  function renderSheet(page, index, options = {}) {
    const sheet = el("article", `sheet sheet-${page.layout || "standard"} ${accentClass(page.accent)}`);
    sheet.id = `page-${page.slug}`;
    sheet.tabIndex = -1;
    sheet.dataset.slug = page.slug;
    sheet.setAttribute("aria-labelledby", `${page.slug}-title`);

    const top = el("div", "sheet-top");
    top.append(el("p", "eyebrow", page.kicker || "UAIS"));
    top.append(el("span", "sheet-id", `${page.id} · ${index + 1}/${state.data.pages.length}`));
    sheet.append(top);

    if (page.layout !== "cover") {
      const title = el("h2", "", page.title);
      title.id = `${page.slug}-title`;
      sheet.append(title);
      if (page.subtitle) sheet.append(el("h3", "", page.subtitle));
      const canonical = canonicalLabel(page.canonical);
      if (canonical) sheet.append(canonical);
    }

    const handled = renderSpecial(page, sheet);
    if (!handled) {
      sheet.append(el("p", "lead", page.lead));
    }

    if (page.layout !== "toc" && page.layout !== "cover" && page.layout !== "guardian" && page.layout !== "map") {
      const notes = el("div", "notes");
      (page.notes || []).forEach((note, noteIndex) => notes.append(noteElement(note, noteIndex)));
      sheet.append(notes);
    } else if (page.layout === "cover") {
      const notes = el("div", "notes");
      page.notes.filter((note) => !note.items).forEach((note, noteIndex) => notes.append(noteElement(note, noteIndex)));
      sheet.append(notes);
    }

    if (page.layout === "glossary") {
      const terms = el("div", "notes");
      state.data.terms.forEach((term) => {
        terms.append(noteElement({
          accent: "cream",
          title: term.ru,
          canonical: term.canonical,
          body: term.definition,
        }, 0));
      });
      sheet.append(terms);
    }

    sheet.append(sourceLinks(page));
    if (options.clone) sheet.classList.add("sheet-dialog-copy");
    return sheet;
  }

  function indicesForBook() {
    if (state.mode === "scroll") return state.data.pages.map((_, index) => index);
    if (!isWideSpread() || state.pageIndex === 0) return [state.pageIndex];
    const left = state.pageIndex % 2 === 1 ? state.pageIndex : state.pageIndex - 1;
    return [left, left + 1].filter((index) => index < state.data.pages.length);
  }

  function render() {
    if (!state.data) return;
    stage.replaceChildren();
    shell.dataset.view = state.mode;
    stage.classList.toggle("scroll-track", state.mode === "scroll");
    const indices = indicesForBook();
    stage.classList.toggle("single", indices.length === 1 || state.mode === "scroll");
    indices.forEach((index) => stage.append(renderSheet(state.data.pages[index], index)));

    document.querySelectorAll("[data-mode]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.mode === state.mode));
    });
    document.querySelector('[data-action="prev"]').disabled = state.pageIndex <= 0;
    document.querySelector('[data-action="next"]').disabled = state.pageIndex >= state.data.pages.length - 1;
    const current = state.data.pages[state.pageIndex];
    status.textContent = `${state.data.ui.page} ${state.pageIndex + 1} ${state.data.ui.of} ${state.data.pages.length}: ${current.title}`;
    document.title = `${current.title} · UAIS`;
  }

  function setPage(index, push = true, focusBook = false) {
    state.pageIndex = Math.max(0, Math.min(index, state.data.pages.length - 1));
    const page = state.data.pages[state.pageIndex];
    if (push) history.replaceState(null, "", slugHash(page.slug));
    render();
    if (state.mode === "scroll") {
      document.querySelector(`#page-${CSS.escape(page.slug)}`)?.scrollIntoView({ block: "start", behavior: "smooth" });
    } else if (focusBook) {
      document.querySelector("#book")?.scrollIntoView({ block: "start", behavior: "smooth" });
    }
  }

  function setMode(mode) {
    state.mode = mode;
    localStorage.setItem("uais-view-mode", mode);
    render();
  }

  function pageIndexFromHash() {
    const match = location.hash.match(/page=([^&]+)/);
    if (!match || !state.data) return 0;
    const slug = decodeURIComponent(match[1]);
    const index = state.data.pages.findIndex((page) => page.slug === slug);
    return index >= 0 ? index : 0;
  }

  function nextStep(direction) {
    const step = state.mode === "book" && isWideSpread() && state.pageIndex > 0 ? 2 : 1;
    setPage(state.pageIndex + direction * step);
  }

  async function copyLink() {
    const url = `${location.origin}${location.pathname}${slugHash(state.data.pages[state.pageIndex].slug)}`;
    try {
      await navigator.clipboard.writeText(url);
      status.textContent = "Ссылка на текущий лист скопирована.";
    } catch {
      status.textContent = url;
    }
  }

  function openDialog() {
    dialogContent.replaceChildren(renderSheet(state.data.pages[state.pageIndex], state.pageIndex, { clone: true }));
    if (typeof dialog.showModal === "function") {
      dialog.showModal();
    }
  }

  function wireEvents() {
    document.addEventListener("click", (event) => {
      const link = event.target.closest("a[data-slug]");
      if (link) {
        event.preventDefault();
        const index = state.data.pages.findIndex((page) => page.slug === link.dataset.slug);
        if (index >= 0) setPage(index, true, true);
        return;
      }
      const button = event.target.closest("button");
      if (!button) return;
      const action = button.dataset.action;
      if (button.dataset.mode) setMode(button.dataset.mode);
      if (action === "prev") nextStep(-1);
      if (action === "next") nextStep(1);
      if (action === "toc") setPage(1, true, true);
      if (action === "copy") copyLink();
      if (action === "open") openDialog();
      if (action === "close") dialog.close();
    });

    window.addEventListener("hashchange", () => {
      if (/page=/.test(location.hash)) setPage(pageIndexFromHash(), false, true);
    });
    window.addEventListener("resize", render);
    document.addEventListener("keydown", (event) => {
      if (event.key === "ArrowLeft") nextStep(-1);
      if (event.key === "ArrowRight") nextStep(1);
      if (event.key === "Escape" && dialog.open) dialog.close();
    });
    stage.addEventListener("touchstart", (event) => {
      state.touchStartX = event.changedTouches[0].screenX;
    }, { passive: true });
    stage.addEventListener("touchend", (event) => {
      const delta = event.changedTouches[0].screenX - state.touchStartX;
      if (Math.abs(delta) > 45) nextStep(delta > 0 ? -1 : 1);
    }, { passive: true });
  }

  async function init() {
    wireEvents();
    const response = await fetch("data/ru-content.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`Content load failed: ${response.status}`);
    state.data = await response.json();
    document.documentElement.lang = state.data.locale;
    document.documentElement.dir = state.data.dir || "ltr";
    const hasPageHash = /page=/.test(location.hash);
    setPage(pageIndexFromHash(), false, hasPageHash);
  }

  init().catch((error) => {
    console.error(error);
    status.textContent = "Не удалось загрузить книгу. Откройте PDF или повторите позже.";
  });
})();
