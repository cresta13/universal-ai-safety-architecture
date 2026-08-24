# Canonical Threat Model

## Scope and protected interests

The model covers deliberate attacks, accidental failures, institutional capture, privacy abuse and common-mode failure affecting human life, bodily integrity, rights, property, privacy, critical services, infrastructure, legitimacy mechanisms and the evidence needed to support safety claims.

| Threat/failure class | Capability and attack surface | Trust assumption | UAIS mitigation | Residual limitation |
|---|---|---|---|---|
| Malicious or misaligned system | planning, deception, tools, credentials, delegation | no trust in goals | ceilings, target gates, least authority, RFA/HHR | unknown strategies and hidden paths |
| Compromised system/model | supply chain, prompt/tool injection, runtime compromise | model integrity is conditional | isolation, provenance, monitoring, safe degradation | novel compromise |
| Accidental failure/drift | defects, distribution shift, overload, misuse | tested behavior is scoped | AFM, validation, monitoring, safe state | untested conditions |
| Malicious operator/owner | legitimate access and operational knowledge | separation of duties | OperatorAbuseResistance, audit, threshold approval | collusion/coercion |
| Malicious human approver | abuse of legitimacy role | approver is accountable, not infallible | multiparty approval, conflict record, appeal | coordinated capture |
| Manufacturer or update operator | firmware/model/policy distribution | signed does not mean safe | ACU, ΔA/ΔH, independent review, rollback | hidden build pipeline |
| Malicious update infrastructure | equivocation, downgrade, targeted payload | update roots remain protected | transparency, threshold signing, staged release | root/key compromise |
| Cloud/provider | IAM, hosting, telemetry, availability | provider claims require evidence | TransitiveAuthorityVisibility, supplier assurance, target gates | provider-state opacity |
| Dependency/supplier compromise | libraries, APIs, parts, data, services | transitive trust is bounded | SafetyConfigurationItem inventory, SAA, attestations, AIVE | unknown dependency |
| Compromised telemetry | omit, forge, delay or reorder events | provenance/freshness are verifiable | diverse sources, reconciliation, Audit Integrity | authentic false data |
| Compromised sensor/spoofing | manipulate external-world inputs | sensor validity is conditional | independent sensing, plausibility, physical diversity | common environmental spoof |
| Compromised DEV | accept invalid chain or predicates | verifier build/rules controlled | minimal code, reproducible build, diversity, negative tests | shared rule defect |
| Compromised attestation | false configuration/integrity claim | root and measurement chain scoped | nonce/freshness, measured boot, independent checks | root compromise |
| Compromised Hardware Root of Trust | extract or misuse root keys | hardware isolation resists attack | key rotation, multiple roots, physical controls | invasive/common supplier failure |
| Signing/key infrastructure compromise | authorize malicious grants/updates | threshold shares independent | threshold signing, revocation, ceremony audit | collusion or systemic crypto break |
| Captured certification lab | suppress failures or sell favorable results | independence and competence auditable | conflict rules, rotating tests, appeals, random audits | market/regulatory capture |
| Collusion among independent roles | shared incentives or covert coordination | diversity is substantive | ownership/dependency maps, threshold diversity | hidden beneficial ownership |
| Compromised Guardian | false or omitted alerts | Guardian has no consequential credentials | ECA/SEP/DEV, diversity, non-alert audits | persuasive automation bias |
| Correlated Guardian failure | common model/data/infrastructure | diversity claims are evidenced | GuardianDiversityScore, common-mode tests | unknown shared assumptions |
| Model/telemetry/verifier common mode | one false premise propagates | trust chain is finite | independent modalities and assumption register | no proof of external truth |
| Malicious regulator/state | coercion, surveillance, key seizure, suppression | legitimacy remains external assumption | federation, minimum core, appeals, privacy | sovereign coercive power |
| Privacy abuse by safety infrastructure | telemetry used for profiling/control | collection is purpose-limited | minimization, access separation, retention limits | lawful or covert overreach |
| Poisoned risk knowledge/AIVE | false reports, poisoned fixtures, suppression | knowledge is validated/provenanced | independent validation, duplicate analysis, challenge controls | coordinated poisoning |
| Coalition of agents/devices | shared credentials, scale, emergent behavior | isolated ratings do not compose safely | CRA/CPE and coalition monitoring | combinatorial explosion |
| Physical swarm coordination | synchronized force, obstruction, payload | unit PCE does not bound fleet | CPE, enrollment/inventory, zoning | off-grid members |
| Off-grid or distributed PSAS | energy, matter, compute, repair and replication independence | no internal-policy coercion assumption | pre-PST prevention; interface defense/resilience | hostile independence after PST |
| Safety infrastructure outage | unavailable gates, Guardians, people or records | continuity capacity is tested | reserve, fail-mode policy, exercises | correlated catastrophe |
| SybilOrCoordinatedFalseReporting | coordinated false reports, report farms, identity cycling | reporting channel and deduplication process | provenance, clustering, evidence requirements, independent validation, and anomaly review | coordinated actors may still evade linkage or suppress contrary evidence |
| ProviderSuppressionOfUnfavorableReports | vendor or operator hides, delays, narrows, or reclassifies unfavorable reports | intake workflow, registry publication, remediation record | append-only records, appeal paths, independent evaluators, audit sampling, and disclosure rules | private deployments may remain opaque without external access |
| OperationalExposureDenominatorManipulation | denominator inflation, selective logging, task-strata mixing, or exclusion of failed exposures | operational exposure measurement | registered Operational Exposure Unit definition, stratification, audit, and reconciliation against external evidence | hidden traffic and unlogged contexts can bias rates |
| VersionLaundering | new version label used to bury confirmed errors or inherit trust without evidence | version identity, profile migration, registry history | versioned profiles, carryover caps, Rating Change Events, and preserved historical error records | subtle configuration forks can remain hard to compare |
| BenchmarkOrScenarioLeakage | training, memorization, or targeted optimization against protected evaluation cases | scenario suites, evaluator infrastructure, release process | held-out suites, rotation, leakage controls, evaluator independence, and gaming tests | leakage can be hard to prove after broad public exposure |
| TrustworthinessEvaluationGaming | optimization for measured metrics while shifting failure into unmeasured strata | scoring policy, metrics, evaluator rubrics | diverse metrics, adversarial suites, stratified exposure, uncertainty reporting, and red-team review | proxy metrics may still miss real-world failure modes |
| EvaluatorCollusionOrCommonModeFailure | evaluators share incentives, infrastructure, data, model family, or hidden owner | independent evaluation layer | evaluator-independence profiles, conflict disclosure, diversity requirements, and disagreement tracking | undisclosed beneficial ownership or shared assumptions may remain |
| TrustworthinessRegistryTampering | deletion, rewriting, equivocation, or selective disclosure of profiles and error history | registry storage, synchronization, publication, signing keys | tamper-evident history, signatures, replication, audit logs, and superseded-version retention | root compromise or private-registry opacity can limit detection |
| TrustworthinessRatingMisuseOrAutomationBias | rating treated as permission, safety guarantee, procurement shortcut, or automated approval | UI, procurement, certification, policy automation | required disclaimers, separation from authority grant, status/rating fields, and explanation records | users may still over-rely on simplified labels |
| ReporterRetaliation | retaliation against users, employees, evaluators, or researchers who report errors | reporting identity, employment/vendor relationship, disclosure process | privacy minimization, protected channels, appeal, and non-sensitive public issue paths | legal or institutional pressure can deter reporting |
| ReportingPrivacyLeakage | error evidence exposes personal data, confidential content, or sensitive context | report payloads, registry evidence, evaluator review | data minimization, redaction, access controls, privacy-preserving evidence, and retention limits | some high-fidelity validation may require sensitive evidence |

## Canonical trust rules

Trust is scoped, time-bound and evidenced. Authentication proves an identity claim, not benevolence. Attestation proves declared measurements and provenance, not external-world truth. Independence must include organization, ownership, infrastructure, method, data and incentives. Any invalidated assumption triggers reassessment and may cap or suspend certification.

## Threat-model maintenance

The threat model is reviewed on ACU, AIVE, incident, supplier change, new attack class, material environmental drift, failed challenge, key compromise, coalition growth or Technology Evolution Review. Domain profiles may add threats but may not remove a canonical class without a documented non-applicability argument.


