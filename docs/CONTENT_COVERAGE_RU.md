# Покрытие манифеста русской веб-книгой UAIS

Статус: объяснительная русская веб-книга для содержательной и визуальной проверки владельцем проекта.

Источник истины: актуальные файлы `spec/*.md` из Draft 1.0 Candidate 3 / Public Review. Переданные scrapbook-изображения использованы как визуальный референс, не как нормативный источник текста.

| ID страницы | Название страницы | Разделы источника | Что объясняет страница | Статус |
| --- | --- | --- | --- | --- |
| P00 | UAIS | `spec/01_MANIFESTO.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md` | Главный тезис: возможность действия не создаёт права действия; Public Review не означает валидацию или одобрение. | Покрыто |
| P01 | Оглавление | `spec/00_MASTER_INDEX.md` | Навигация по 20 листам русской книги. | Покрыто |
| P02 | Что такое UAIS | `spec/01_MANIFESTO.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md` | Назначение архитектуры, actor-agnostic смысл и базовая цепочка через ограниченный разрешённый диапазон. | Покрыто |
| P03 | Почему нужна UAIS | `spec/01_MANIFESTO.md`, `spec/02_THREAT_MODEL.md` | Почему «может сделать» не равно «имеет право сделать». | Покрыто |
| P04 | Десять принципов · 1–5 | `spec/01_MANIFESTO.md` | Интеллект, создание, потолок полномочий, автономность и обновление доказательств. | Покрыто |
| P05 | Десять принципов · 6–10 | `spec/01_MANIFESTO.md` | Узкие места контроля, границы последствий, разделение ролей, неизвестное и срок действия заявлений. | Покрыто |
| P06 | Стадия I и Стадия II | `spec/01_MANIFESTO.md`, `spec/02_THREAT_MODEL.md`, `spec/12_STAGE_II_PHYSICAL_SOVEREIGNTY.md` | Почему контроль вычислений покупает время, а контроль возможностей и последствий создаёт устойчивость. | Покрыто |
| P07 | Возможность, полномочие и достижимость | `spec/03_NORMATIVE_VOCABULARY.md`, `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md` | Разводит возможность, легитимное полномочие, фактически достижимое полномочие и нелегитимно достижимое полномочие. | Покрыто |
| P08 | Архитектура защитника полномочий | `spec/09_GUARDIAN_ARCHITECTURE.md`, `spec/23_OPEN_RESEARCH_PROBLEMS.md` | Guardian наблюдает, моделирует сценарии и выпускает доказательства; он не принимает окончательное решение. | Покрыто |
| P09 | Потолок полномочий | `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md`, `spec/13_DEVICE_LIFECYCLE_AND_UPDATES.md` | Как фиксируется потолок и почему техническая архитектура не производит легитимность сама. | Покрыто |
| P10 | Три вида полномочий: LA, ERA и IRA | `spec/03_NORMATIVE_VOCABULARY.md`, `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md` | Сравнивает выданное, фактически достижимое и достижимое без легитимного мандата. | Покрыто |
| P11 | Многомерная классификация риска | `spec/04_CLASSIFICATION_MODEL.md`, `spec/05_SAFETY_METRICS.md` | Показывает H/P/A/T-оси как отдельные измерения, а не единый процент безопасности. | Покрыто |
| P12 | Суверенитет человека и физический суверенитет | `spec/10_PHYSICAL_SAFETY_AND_HUMAN_SOVEREIGNTY.md`, `spec/12_STAGE_II_PHYSICAL_SOVEREIGNTY.md` | Независимый ручной контроль, safe stop по опасности и различие автономности и физического суверенитета. | Покрыто |
| P13 | Метрики и подтверждённость безопасности | `spec/05_SAFETY_METRICS.md`, `spec/06_SAFETY_ASSURANCE_MODEL.md` | Различает результат свойства, силу доказательств, SAL и доказанную надёжность ИИ. | Покрыто |
| P14 | Раскрытие опасностей и паспорт безопасности | `spec/07_HAZARD_DISCLOSURE_AND_SAFETY_PASSPORT.md`, `spec/13_DEVICE_LIFECYCLE_AND_UPDATES.md` | Разводит Safety Passport, Consumer AI Safety Class, SAL и Trustworthiness на примере домашнего робота. | Покрыто |
| P15 | Копирование, производство и коалиции | `spec/11_REPLICATION_PRODUCTION_AND_EXPANSION.md`, `spec/12_STAGE_II_PHYSICAL_SOVEREIGNTY.md` | Почему копии, производство, ресурсы и коалиции меняют достижимые последствия. | Покрыто |
| P16 | Уязвимости, развитие и открытые исследования | `spec/19_AIVE.md`, `spec/20_EVOLUTION_AND_EXTENSIBILITY.md`, `spec/23_OPEN_RESEARCH_PROBLEMS.md` | AIVE, пересмотр при развитии технологий и границы `OPEN RESEARCH`. | Покрыто |
| P17 | Итоговая архитектурная карта | `spec/00_MASTER_INDEX.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md`, `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md` | Связывает запрос, полномочия, достижимость, вред, доказательства, границу возможностей и интерфейс последствий. | Покрыто |
| P18 | Сквозной пример: Ария и возвраты | `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md`, `spec/09_GUARDIAN_ARCHITECTURE.md`, `spec/13_DEVICE_LIFECYCLE_AND_UPDATES.md`, `spec/21_USE_CASES.md` | Человеческий end-to-end пример возвратов: $50, запрос на $2000, путь до $10 000, Guardian, ECA/SEP и ограниченный режим. | Покрыто |
| P19 | Глоссарий и источники | `spec/03_NORMATIVE_VOCABULARY.md`, `spec/GLOBAL_NAME_REGISTRY.md`, `NOTICE.md`, `CITATION.md` | Русские объяснительные термины, canonical English labels, даты и права использования. | Покрыто |

## Итоговое покрытие

Русская веб-книга покрывает основные смысловые блоки текущего публичного кандидата: manifesto, threat model, vocabulary, classification, metrics, assurance, hazard disclosure, authority architecture, Guardian, human/physical sovereignty, replication/production/coalitions, lifecycle, AIVE, evolution, open research, roadmap-level architecture and publication metadata.

Сознательное ограничение: это объяснительная русская версия, а не нормативный перевод спецификации. При конфликте приоритет остаётся у англоязычной Candidate 3 specification.
