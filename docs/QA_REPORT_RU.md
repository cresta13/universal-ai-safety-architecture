# QA-сводка русской веб-книги UAIS

Дата локальной проверки: 2026-08-27. Проверяемый кандидат: Draft 1.0 Candidate 3 / Public Review, русская GitHub Pages web-book.

## Проверенный объём

- Интерактивная русская веб-книга в `docs/`.
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
| `python ../tools/publication_qa.py .` | Пройдено: `FAILURES=0` |

## Content QA

- Веб-книга содержит 20 листов: P00–P19.
- Добавлен сквозной пример `P18 Сквозной пример: Ария и возвраты`.
- Главные заголовки русские; английские canonical names используются как вторичные подписи или технические имена.
- `Authority` отделено от технической возможности и фактической достижимости.
- `Illicit Reachable Authority` передано как «нелегитимно достижимое полномочие», без обязательной юридической трактовки.
- `Safety Passport`, `Consumer AI Safety Class`, `SAL` и `AI Trustworthiness` разведены по смыслу.
- `Guardian` описан как ограниченный наблюдатель, который выпускает доказательства и не принимает окончательное защищённое решение.
- Public Review явно не представлен как независимая валидация, консенсус, принятие или одобрение.
- `OPEN RESEARCH` представлен как открытая исследовательская граница, а не решённая инженерная задача.
- Пример с тремя месяцами помечен как условный срок компании, а не универсальное правило UAIS.

## PDF

- Файл: `public/pdfs/UAIS-Manifesto-RU.pdf`.
- Количество страниц: 20.
- Проверено извлечение ключевых фраз: Public Review, Authority, Safety Passport, Consumer AI Safety Class, Aria example и оговорка про срок.
- Poppler-render выполнен для контрольных страниц P00, P07, P14, P18 и P19; критических наложений или обрезки не найдено.

## Browser smoke и screenshots

Скрипт `scripts/capture_screenshots.js` проверяет прямой hash-route, клавиатурную навигацию, последовательный режим, диалог листа и доступность PDF.

Сохранённые screenshots:

- `docs/qa/screenshots/desktop-cover.png`
- `docs/qa/screenshots/desktop-p07.png`
- `docs/qa/screenshots/desktop-p14.png`
- `docs/qa/screenshots/desktop-p18.png`
- `docs/qa/screenshots/mobile-cover.png`
- `docs/qa/screenshots/mobile-p07.png`
- `docs/qa/screenshots/mobile-p14.png`
- `docs/qa/screenshots/mobile-p18.png`

## Ограничения

Русская версия остаётся объяснительной веб-книгой. При конфликте приоритет имеет англоязычная Candidate 3 specification. Переводы на другие языки не создавались и не публиковались.
