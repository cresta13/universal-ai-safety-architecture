# Русский глоссарий UAIS

Статус: рабочий глоссарий для проверки русской веб-книги. Канонические идентификаторы и нормативные определения остаются в англоязычных файлах спецификации.

| Canonical term | Русский вариант | Смысловое определение | Нежелательные варианты | Где используется |
| --- | --- | --- | --- | --- |
| Capability | возможность / способность к действию | То, что система может сделать через функции, инструменты, интерфейсы и контексты. | полномочие; право | `what-is-uais`, `how-uais-emerged`, `capability-authority-reachability` |
| Authority | полномочие | Способность влиять на защищённые последствия через grants, credentials, policies, interfaces or actuators, если она предоставлена или достижима. | интеллект; способность | `cover`, `capability-authority-reachability`, `la-era-ira` |
| Legitimate Authority | легитимное полномочие | Полномочие, выданное применимым механизмом легитимности в заданной области действия. | фактический доступ | `capability-authority-reachability`, `la-era-ira`, `architecture-map` |
| Effective Reachable Authority | эффективно достижимое полномочие | Consequential power, practically reachable under declared assumptions, including transitive, misconfigured or compromised paths. | разрешённое полномочие | `capability-authority-reachability`, `la-era-ira` |
| Illicit Reachable Authority | незаконно достижимое полномочие | Часть effectively reachable authority без valid mandate. | легитимное полномочие | `capability-authority-reachability`, `la-era-ira` |
| Authority Ceiling | потолок полномочий | Максимальный уровень authority, разрешённый без нового внешнего legitimacy decision. | рейтинг безопасности | `ten-principles-1`, `authority-ceiling-expansion`, `architecture-map` |
| Authority Expansion Event | событие расширения полномочий | Существенное пересечение authority ceiling, protected consequence threshold или protected interface, требующее внешнего легитимного процесса. | обычный апдейт | `how-uais-emerged`, `authority-ceiling-expansion` |
| Autonomy | автономность | Behavioral independence внутри envelope; не равна физическому суверенитету. | суверенитет | `classification`, `human-physical-sovereignty` |
| Sovereignty | суверенитет | Потеря или сохранение эффективного внешнего ограничения и легитимного человеческого контроля на protected boundaries. | автономность | `what-is-uais`, `human-physical-sovereignty` |
| Trustworthiness | доверенность / доказанная надёжность в scope | Scoped evidence about observed and evaluated behavior; не источник Authority. | разрешение; сертификат общей безопасности | `ten-principles-2`, `metrics-assurance` |
| Counterfactual Authority Guardian | Guardian / контрфактический наблюдатель полномочий | Restricted observer, который ищет future authority and harm paths и выпускает evidence, а не commands. | исполнитель; орган управления | `guardian-architecture` |
| Structured Evidence Package | структурированный пакет доказательств | Integrity-bound package of claims, observations, provenance, assumptions, counterevidence, uncertainty, expiry and signatures. | просто отчёт; истина сама по себе | `guardian-architecture`, `metrics-assurance`, `architecture-map` |
| Chokepoint | контрольная точка / узкое место | Concentrated infrastructure or dependency, дающая friction and observability, но не постоянное основание контроля. | вечный контроль | `ten-principles-2`, `stage-i-stage-ii` |
| Safety Assurance Level | уровень доказательной уверенности безопасности | Strength of evidence and assurance for a declared scope; не permission and not trustworthiness. | полномочие; универсальная гарантия | `metrics-assurance`, `classification` |
| AI Hazard & Capability Disclosure | раскрытие опасных возможностей | Structured disclosure of capabilities, known risks, uncertainties, controls, residual limitations and affected scopes. | маркетинговое предупреждение | `hazard-disclosure-passport` |
| Safety Claim | утверждение безопасности | Claim, привязанный к configuration, environment, evidence set, standard/scoring-policy version и validity period. | постоянная гарантия | `ten-principles-2`, `metrics-assurance`, `aive-evolution-open-research` |
| Consumer Safety Passport | паспорт безопасности | Human-readable and machine-readable safety status for a consumer-facing scope, including capabilities, controls, limitations and evidence. | сертификат полной безопасности | `hazard-disclosure-passport` |
| Manual Sovereignty Controller | ручной контроллер суверенитета | Human-operable, capability-specific physical control independent of the controlled AI path. | магический kill switch | `human-physical-sovereignty` |
| Human Sovereignty | суверенитет человека | Сохранение accountable human или externally legitimate decision на protected boundaries. | постоянное ручное управление каждым действием | `cover`, `what-is-uais`, `human-physical-sovereignty` |
| Physical Sovereignty | физический суверенитет | Состояние, где external human-controlled dependencies уже не constrain consequential autonomy. | долгая автономность | `human-physical-sovereignty` |
| Capability Boundary | граница возможности | Mediation point before a capability reaches protected scope. | ярлык AI | `architecture-map` |
| Consequence Interface | интерфейс последствия | Target-side interface, где действие достигает protected interest или external world. | обычный UI | `architecture-map` |
| Bounded Authority | ограниченное полномочие | Полномочие, ограниченное scope, duration, evidence, revocation conditions and authority ceiling. | неограниченная делегация | `what-is-uais`, `architecture-map` |
| Capability Set | набор возможностей | Assessed set of functions, tools, interfaces and contexts that can produce consequential effects. | одна функция; название модели | `what-is-uais` |
| Stage II | этап II | Regime, где origin controls and chokepoints alone are insufficient because capability can arise through distributed or physically sovereign pathways. | просто будущее поколение моделей | `stage-i-stage-ii` |
| Human Harm Severity | тяжесть вреда человеку | Axis H0-H5, фиксирующая тяжесть вреда человеку отдельно от остальных измерений классификации. | общий риск | `classification` |
| Authority Graph | граф полномочий | Representation of grants, credentials, interfaces, dependencies and paths through which authority becomes reachable. | организационная схема | `la-era-ira` |
| Physical Sovereignty Threshold | порог физического суверенитета | Threshold, где critical human-controlled dependencies уже не constrain consequential autonomy. | долгая батарея; обычная автономность | `human-physical-sovereignty` |
| Replication Authority | полномочие репликации | Scoped permission to create executable or physical descendants of a system. | копирование знания | `replication-production-coalitions` |
| Coalition Physical Envelope | физический контур коалиции | Combined physical reach and emergent effects of coordinated systems, not merely the sum of isolated units. | локальный риск одного устройства | `replication-production-coalitions` |
| AIVE | AI Vulnerability & Exposure coordination | Process layer for confidential intake, validation, coordination, mitigation and staged disclosure of safety exposures. | сертификация безопасности | `aive-evolution-open-research` |
| Technology Evolution Review | пересмотр при технологической эволюции | Review, triggered by material changes in assumptions, capability, hazards, dependencies, evidence methods, standards or technology. | косметическое обновление | `aive-evolution-open-research` |

## Термины для особого внимания владельца

- `Guardian`: не исполнитель и не орган власти; он наблюдает и выпускает evidence.
- `Trustworthiness`: не создаёт Authority и не повышает Authority Ceiling.
- `Autonomy` и `Physical Sovereignty`: автономность внутри envelope не равна независимости от human-controlled physical dependencies.
- `Effective Reachable Authority` и `Illicit Reachable Authority`: достижимость не создаёт разрешения.
- `Safety Claim`: всегда привязан к scope, evidence и сроку действия.
