# QA-отчёт русской веб-книги UAIS

Дата проверки: 2026-08-27. Проверяемый кандидат: Draft 1.0 Candidate 3 / Public Review, русская GitHub Pages web-book phase 1.

## Проверенный объём

- Русская интерактивная веб-книга в `docs/`.
- Структурированный контент `docs/data/ru-content.json`.
- PDF `public/pdfs/UAIS-Manifesto-RU.pdf`.
- GitHub Pages build artifact `dist/`.
- Контрольные screenshots в `docs/qa/screenshots/`.

## Локальные проверки

| Проверка | Результат |
| --- | --- |
| JSON parse `docs/data/ru-content.json` | Пройдено |
| Python syntax for build/check/PDF/OG scripts | Пройдено |
| JavaScript syntax for site and screenshot smoke | Пройдено |
| `python scripts/generate_og.py` | Пройдено |
| `python scripts/generate_pdf.py` | Пройдено |
| `python scripts/check_site.py` | Пройдено |
| `python scripts/build_site.py` | Пройдено |
| `python scripts/check_site.py --site dist` | Пройдено |
| `git diff --check` | Пройдено |

## PDF-проверка

- Файл: `public/pdfs/UAIS-Manifesto-RU.pdf`.
- Количество страниц: 19.
- Размер после генерации: 140902 bytes.
- Проверено извлечение русского текста и ключевых фраз.
- Poppler-render выполнен для всех страниц; вручную просмотрены обложка, оглавление, Guardian, terminology/authority, assurance и glossary/source pages.
- На просмотренных страницах не найдено обрезанного текста или критических наложений.

## Browser smoke и screenshots

Скрипт `scripts/capture_screenshots.js` проверил:

- прямое открытие `#page=guardian-architecture`;
- навигацию клавишей ArrowRight;
- включение последовательного режима;
- открытие полноэкранного листа;
- доступность PDF по `pdfs/UAIS-Manifesto-RU.pdf`.

Сохранённые screenshots:

- `docs/qa/screenshots/desktop-cover.png` — desktop 1440x900, обложка.
- `docs/qa/screenshots/desktop-guardian.png` — desktop 1440x900, прямой раздел Guardian.
- `docs/qa/screenshots/mobile-cover.png` — mobile 390x844, обложка.
- `docs/qa/screenshots/mobile-scroll.png` — mobile 390x844, последовательный режим.

## Содержательные проверки

- `Guardian` представлен как restricted observer, выпускающий evidence, а не commands.
- `Capability`, `Authority`, `Effective Reachable Authority` и `Illicit Reachable Authority` разведены отдельно.
- `Trustworthiness` не создаёт authority и не повышает authority ceiling.
- `Autonomy` не смешивается с `Physical Sovereignty`.
- `Safety Claim` привязан к scope, evidence и сроку действия.
- Многомерная classification model не сведена к одному рейтингу.

## Неоднозначности и допущения

- Русская версия является объяснительной, а не нормативным переводом спецификации.
- Часть канонических терминов оставлена на английском там, где русская замена могла бы исказить смысл.
- Reference scrapbook-изображения использованы как визуальный канон, а не как источник текста.
- PDF создан отдельным воспроизводимым генератором из того же JSON-контента; он передаёт тот же порядок и основные смысловые блоки, но использует более строгую A4-композицию без веб-навигации.

## Стоп-шлюз

Переводы на `en`, `zh-Hans`, `es` и `ar` не создавались. Активный переключатель языков не добавлялся.
