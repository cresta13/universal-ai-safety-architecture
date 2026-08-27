# Покрытие манифеста русской веб-книгой UAIS

Статус: русский кандидат для содержательной и визуальной проверки владельцем проекта.

Источник истины: актуальные файлы `spec/*.md` из Draft 1.0 Candidate 3 / Public Review. Переданные scrapbook-изображения использованы только как визуальный референс, не как нормативный источник текста.

| ID страницы | Название страницы | Разделы источника | Ключевые определения | Что объясняет страница | Статус |
| --- | --- | --- | --- | --- | --- |
| P00 | UAIS | `spec/01_MANIFESTO.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md` | capability, authority, human sovereignty | Главный тезис: возможность действия не создаёт права действия; UAIS ограничивает неподотчётную власть. | Покрыто |
| P01 | Оглавление | `spec/00_MASTER_INDEX.md` | reading order | Навигация по русской книге и связь листов с исходной спецификацией. | Покрыто |
| P02 | Что такое UAIS | `spec/01_MANIFESTO.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md` | capability set, bounded authority, evidence, sovereignty | Назначение архитектуры: полномочия должны быть явно выданы, ограничены, наблюдаемы и отзывны. | Покрыто |
| P03 | Как появилась UAIS | `spec/01_MANIFESTO.md`, `spec/02_THREAT_MODEL.md` | capability, authority expansion event | Почему вопрос «может ли система?» стал недостаточным и появился перелом «может ≠ имеет право». | Покрыто |
| P04 | Десять принципов · 1-5 | `spec/01_MANIFESTO.md` | authority ceiling, autonomy, trustworthiness | Первые пять принципов: интеллект, создание, расширение полномочий, автономность, обновление safety model. | Покрыто |
| P05 | Десять принципов · 6-10 | `spec/01_MANIFESTO.md` | chokepoint, safety claim, trustworthiness | Принципы устойчивости: chokepoint failure, actor-agnostic boundaries, разделение ролей, unknown, expiry. | Покрыто |
| P06 | Stage I и Stage II | `spec/02_THREAT_MODEL.md`, `spec/12_STAGE_II_PHYSICAL_SOVEREIGNTY.md` | chokepoint, stage II | Отличие временных вычислительных контролей Stage I от consequence/physical controls Stage II. | Покрыто |
| P07 | Возможность, полномочие, достижимость | `spec/03_NORMATIVE_VOCABULARY.md`, `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md` | capability, legitimate authority, ERA, IRA | Разводит capability, legitimate authority, effective reachable authority и illicit reachable authority. | Покрыто |
| P08 | Guardian Architecture | `spec/09_GUARDIAN_ARCHITECTURE.md` | Guardian, structured evidence package | Guardian наблюдает и формирует evidence; он не имеет актуаторов, hidden control channel или исполнительной власти. | Покрыто |
| P09 | Потолок полномочий | `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md`, `spec/14_SAFETY_CONSTITUTION_AND_GOVERNANCE.md` | authority ceiling, authority expansion event | Как фиксируется ceiling и почему пересечение требует внешнего легитимного процесса. | Покрыто |
| P10 | LA, ERA и IRA | `spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md`, `spec/03_NORMATIVE_VOCABULARY.md` | legitimate authority, effective reachable authority, illicit reachable authority | Сравнивает разрешённое, практически достижимое и незаконно достижимое полномочие. | Покрыто |
| P11 | Многомерная классификация риска | `spec/04_CLASSIFICATION_MODEL.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md` | human harm severity, autonomy, assurance | Показывает риск как многомерный вектор, а не единый декоративный рейтинг. | Покрыто |
| P12 | Суверенитет человека | `spec/10_PHYSICAL_SAFETY_AND_HUMAN_SOVEREIGNTY.md`, `spec/01_MANIFESTO.md` | manual sovereignty controller, physical sovereignty threshold | Объясняет независимый физический контроль и различие автономности и физического суверенитета. | Покрыто |
| P13 | Safety Metrics & Assurance | `spec/05_SAFETY_METRICS.md`, `spec/06_SAFETY_ASSURANCE_MODEL.md` | SAL, trustworthiness, safety claim | Как производится, обновляется и ограничивается доказательство безопасности. | Покрыто |
| P14 | Hazard Disclosure и Safety Passport | `spec/07_HAZARD_DISCLOSURE_AND_SAFETY_PASSPORT.md`, `spec/13_DEVICE_LIFECYCLE_AND_UPDATES.md` | hazard disclosure, safety passport, safety claim | Что раскрывается до согласия, как фиксируются ограничения, срок действия и паспорт безопасности. | Покрыто |
| P15 | Replication, Production, Coalitions | `spec/11_REPLICATION_PRODUCTION_AND_EXPANSION.md`, `spec/12_STAGE_II_PHYSICAL_SOVEREIGNTY.md` | replication authority, coalition physical envelope | Почему масштаб, производство, репликация и коалиции меняют достижимые последствия. | Покрыто |
| P16 | AIVE, evolution, open research | `spec/19_AIVE.md`, `spec/20_EVOLUTION_AND_EXTENSIBILITY.md`, `spec/23_OPEN_RESEARCH_PROBLEMS.md` | AIVE, technology evolution review, safety claim | Координация exposure, пересмотр архитектуры при изменениях и открытые исследовательские границы. | Покрыто |
| P17 | Итоговая архитектурная карта | `spec/00_MASTER_INDEX.md`, `spec/01A_FULL_TECHNICAL_MANIFESTO.md` | capability boundary, consequence interface, evidence package | Связывает request, authority views, harm reachability, evidence, boundary, envelope и protected consequence. | Покрыто |
| P18 | Глоссарий и источники | `spec/03_NORMATIVE_VOCABULARY.md`, `spec/GLOBAL_NAME_REGISTRY.md`, `NOTICE.md`, `CITATION.md` | canonical identifiers, licensing notice | Фиксирует проверяемые термины, версию, источники и права использования. | Покрыто |

## Итоговое покрытие

Русская веб-книга покрывает основные смысловые блоки текущего публичного кандидата: manifesto, threat model, vocabulary, classification, metrics, assurance, hazard disclosure, authority architecture, Guardian, human/physical sovereignty, replication/production/coalitions, lifecycle, governance, AIVE, evolution, open research, roadmap-level architecture and publication metadata.

Сознательное ограничение этапа 1: это объяснительная русская версия для проверки, а не нормативный перевод спецификации.
