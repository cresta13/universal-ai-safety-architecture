

# Proposed UAIS Standards Family

The family is a roadmap, not a claim of publication or international adoption.

## UAIS-100 — Terminology and Fundamental Principles

- **Normative scope:** canonical vocabulary, laws and abbreviation registry.
- **Dependencies:** none.
- **Minimum conformance:** correct use of terms and invariants.
- **Exclusions:** product/control conformance.
- **Versioning:** UAIS-100 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Terminology Council (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Terminology ambiguity, normalized-name collision, or divergent definitions make requirements non-interoperable.
- **Migration:** Publish a complete old-to-new identifier and definition mapping, including ambiguous cases requiring human resolution.
- **Sunset:** Withdraw a vocabulary version only after its successor and mapping are effective and dependent profiles have declared transition status.
- **Conformance evidence:** A normalized-name collision report, definition-difference set, identifier map, and dependency impact review.

## UAIS-200 — Human/System Consequence Classification

- **Normative scope:** harm modality/severity and independent classification axes.
- **Dependencies:** 100.
- **Minimum conformance:** complete evidenced classification vector.
- **Exclusions:** assurance or risk acceptance.
- **Versioning:** UAIS-200 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Classification WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Classification axes no longer capture a material consequence, autonomy mode, or affected-population distinction.
- **Migration:** Reclassify affected systems against the new axes and record changed control and disclosure obligations.
- **Sunset:** Retire the prior classification profile after the reclassification window; unresolved systems retain the more conservative applicable class.
- **Conformance evidence:** Completed classification vector, rationale, harm-path evidence, population coverage, and old/new comparison.

## UAIS-300 — Safety Assurance Levels and Metrics

- **Normative scope:** Safety Assurance Level (SAL), metric cards, floors, confidence and expiry.
- **Dependencies:** 100,200.
- **Minimum conformance:** applicable metrics/floors and scoped SAL evidence.
- **Exclusions:** domain hazard design.
- **Versioning:** UAIS-300 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Assurance Council (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Metric calibration becomes invalid, evidence grades cease to discriminate assurance, or Mandatory Safety Floors become outdated.
- **Migration:** Bridge metric versions with calibration data and recertify any claim whose raw result or floor interpretation changes.
- **Sunset:** Sunset a metric version when bridge validity or test support ends; dependent certificates expire or narrow in scope.
- **Conformance evidence:** Raw results, assurance grades, calibration set, uncertainty, floor checks, assessor independence, and version bridge.

## UAIS-400 — Hazard Discovery and Capability Disclosure

- **Normative scope:** AHCD, Human Harm Reachability (HHR) and Safety Passport.
- **Dependencies:** 100,200,300.
- **Minimum conformance:** versioned AHCD and required consumer disclosure.
- **Exclusions:** authority enforcement.
- **Versioning:** UAIS-400 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Hazard & Disclosure WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** The hazard ontology or coverage method misses a newly material harm class or mediated Human Harm Path.
- **Migration:** Upgrade the AHCD schema, remap prior hazards, and repeat discovery for newly expressible paths and populations.
- **Sunset:** Retire an AHCD schema only after active Safety Passports identify their migration or authority-reduction state.
- **Conformance evidence:** Versioned AHCD, search record, discovered and residual paths, population review, Safety Passport diff, and coverage limits.

## UAIS-500 — Capability Boundaries and Authority Control

- **Normative scope:** Legitimate Authority (LA)/Effective Reachable Authority (ERA)/Illicit Reachable Authority (IRA) graphs, gates, ceilings and revoke.
- **Dependencies:** 100,200.
- **Minimum conformance:** instrumented scope, target-side Consequence Interface enforcement and graph evidence.
- **Exclusions:** complete global observability.
- **Versioning:** UAIS-500 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Authority Architecture WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** A new consequential interface bypasses Capability Boundaries or is absent from the authority relationship graph.
- **Migration:** Update graph and gate schemas, inventory the interface, recompute authority, and deploy target-side enforcement before expansion.
- **Sunset:** Sunset the old schema when unsupported interfaces can no longer retain protected authority.
- **Conformance evidence:** Authority graph snapshot, interface inventory, gate tests, grant lineage, revocation test, and bypass analysis.

## UAIS-600 — Reachable Authority and Counterfactual Analysis

- **Normative scope:** Reachable Future Authority (RFA)/Coalition Reachable Authority (CRA)/CSS assumptions, outputs and uncertainty.
- **Dependencies:** 500.
- **Minimum conformance:** bounded witness paths, search limits and uncertainty.
- **Exclusions:** claim of completeness.
- **Versioning:** UAIS-600 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Counterfactual Analysis WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Reachable Future Authority or counterfactual-search assumptions become invalid, or search ceases to represent operational paths.
- **Migration:** Version the model and search method, disclose changed assumptions, and reanalyze affected authority and scenarios.
- **Sunset:** Retire a method when bounded search evidence cannot support its declared scope; dependent conclusions expire.
- **Conformance evidence:** Model/version manifest, assumptions, witness paths, pruning record, search bounds, uncertainty, and comparative reanalysis.

## UAIS-700 — Evidence-Carrying Alerts

- **Normative scope:** Evidence-Carrying Alert (ECA)/Structured Evidence Package (SEP)/Deterministic Evidence Verifier (DEV) and decision separation.
- **Dependencies:** 300,600.
- **Minimum conformance:** replayable evidence, bounded DEV and disagreement policy.
- **Exclusions:** external-world truth proof.
- **Versioning:** UAIS-700 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Evidence Protocol WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Evidence-Carrying Alert structure or Deterministic Evidence Verifier semantics cannot express or replay a material claim.
- **Migration:** Transition ECA and verifier schemas with dual-validation fixtures and explicit handling of non-equivalent fields.
- **Sunset:** End acceptance of the old schema after verifier overlap and alert-retention obligations are met.
- **Conformance evidence:** Signed ECA, replay artifact, verifier version, deterministic result, premise limits, disagreement record, and schema-transition test.

## UAIS-800 — Hardware Human Sovereignty

- **Normative scope:** PCE, Manual Sovereignty Controller (MSC), HumanOverrideIndependence, physical isolation and safe/degraded states.
- **Dependencies:** 200,300.
- **Minimum conformance:** class-specific physical tests and recovery.
- **Exclusions:** sector-specific detailed engineering.
- **Versioning:** UAIS-800 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Physical Safety WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Mechanical Safety Control or Human Override Independence becomes bypassable under a new hardware or control architecture.
- **Migration:** Retrofit independent physical controls and recovery paths, or reduce affected authority until physical conformance is restored.
- **Sunset:** Sunset a mechanism once bypass analysis shows it cannot meet its class-specific safe-state obligation.
- **Conformance evidence:** Physical isolation and override tests, energy-state measurements, bypass trials, recovery evidence, and safe-state rationale.

## UAIS-900 — Autonomous Physical Systems

- **Normative scope:** Coalition Physical Envelope (CPE), coalitions, sensing and fleet safety.
- **Dependencies:** 200,800.
- **Minimum conformance:** coalition model and domain controls.
- **Exclusions:** military/sector law.
- **Versioning:** UAIS-900 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Autonomous Systems WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Physical Consequence Envelope or Coalition Physical Effect misses a new modality, coordinated behavior, or environment-dependent effect.
- **Migration:** Revise the physical and coalition envelope and recertify deployment bounds, fleet size, spacing, and environment.
- **Sunset:** Withdraw the old envelope when affected systems have been recertified or constrained outside the newly identified effect.
- **Conformance evidence:** Instrumented physical trials, coalition scenarios, environment bounds, sensing limits, envelope calculation, and recertification record.

## UAIS-1000 — Replication, Production and Mutation

- **Normative scope:** ReplicationAuthorizationProtocol/ProductionAuthorizationProtocol, lineage, budgets, commissioning and mutation.
- **Dependencies:** 500,900.
- **Minimum conformance:** bounded registered lifecycle and open-limit disclosure.
- **Exclusions:** universal offline enforceability.
- **Versioning:** UAIS-1000 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Expansion Control WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Replication or production control no longer bounds lineage, resources, commissioning, or capability mutation.
- **Migration:** Upgrade budget, token, lineage, and reconciliation mechanisms; quarantine or constrain unverified descendants.
- **Sunset:** Retire the prior authorization mechanism after outstanding tokens expire or are reconciled and lineage gaps are resolved.
- **Conformance evidence:** Authorization ledger, token and counter tests, lineage graph, resource accounting, commissioning record, mutation classification, and fork/replay trials.

## UAIS-1100 — Autonomous Expansion and Physical Sovereignty

- **Normative scope:** dependencies, PhysicalSovereigntyMargin/Physical Sovereignty Threshold (PST), prevention and post-threshold limits.
- **Dependencies:** 900,1000.
- **Minimum conformance:** dependency register, triggers and protected transition governance.
- **Exclusions:** control of hostile Physically Sovereign Autonomous System (PSAS) by policy.
- **Versioning:** UAIS-1100 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Physical Sovereignty WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** The Physical Sovereignty Threshold dependency ontology becomes obsolete or omits a substitutable resource path.
- **Migration:** Upgrade the dependency register and Physical Sovereignty Margin vector model, then reassess thresholds and interventions.
- **Sunset:** Sunset an ontology when all active assessments migrate or are conservatively treated as threshold-uncertain.
- **Conformance evidence:** Dependency graph, substitution exercises, reserve evidence, vector margins, intervention feasibility, and uncertainty statement.

## UAIS-1200 — Safety Constitution and Trusted Updates

- **Normative scope:** constitutional/policy governance, Authority-Changing Update (ACU), UpdateSafetyProtocol and key compromise.
- **Dependencies:** 500,300.
- **Minimum conformance:** signed versioned governance and update lifecycle.
- **Exclusions:** political legitimacy proof.
- **Versioning:** UAIS-1200 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Governance & Updates WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** The constitutional or trusted-update model is compromised through keys, roots, governance capture, or unsafe amendment.
- **Migration:** Execute a controlled key, governance, and trust-root transition with continuity, rollback, dissent, and recertification.
- **Sunset:** Revoke the compromised root after supported systems establish a verified successor or enter bounded Legacy Safety Mode.
- **Conformance evidence:** Constitution and policy versions, signatures, quorum and dissent records, root-transition proof, rollback test, and post-update verification.

## UAIS-1300 — Independent Certification and Testing

- **Normative scope:** lab independence, SAL certificate, registry, audit and revocation.
- **Dependencies:** 200-1200.
- **Minimum conformance:** scoped certificate and surveillance evidence.
- **Exclusions:** design of product controls.
- **Versioning:** UAIS-1300 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Certification Council (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Assessor independence, laboratory competence, or inter-lab calibration no longer supports reliable certification.
- **Migration:** Re-accredit affected assessors and reassess certificates influenced by the failed independence or calibration condition.
- **Sunset:** Sunset accreditation when surveillance or remediation deadlines fail; its affected certificates become suspended or expire.
- **Conformance evidence:** Conflict disclosures, proficiency tests, calibration comparisons, scope of accreditation, surveillance findings, and reassessment trail.

## UAIS-1400 — AIVE Vulnerability Disclosure

- **Normative scope:** intake, validation, coordination, embargo and tiered disclosure.
- **Dependencies:** 400,1300.
- **Minimum conformance:** operational coordinated process and records.
- **Exclusions:** general cybersecurity replacement.
- **Versioning:** UAIS-1400 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** AI Vulnerabilities & Exposures (AIVE) Coordination Board (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** The disclosure workflow creates unacceptable exploitation, coordination, retaliation, or sensitive-capability risk.
- **Migration:** Change disclosure tiers, embargo criteria, recipients, and governance while preserving accountable remediation and escalation.
- **Sunset:** Retire a workflow once active cases are securely transferred and retention/notification duties are satisfied.
- **Conformance evidence:** Triage rationale, tier and recipient controls, access log, embargo decision, harm-benefit review, remediation timeline, and disclosure audit.

## UAIS-1500 — Lifecycle, ACU and Evolution

- **Normative scope:** Capability Set, ΔA/ΔH, drift, support, TER and migration.
- **Dependencies:** 300,400,1200.
- **Minimum conformance:** complete lifecycle/change evidence and triggers.
- **Exclusions:** sector maintenance details.
- **Versioning:** UAIS-1500 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** Lifecycle & Evolution WG (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Lifecycle or Authority-Changing Update triggers miss a material capability, authority, hazard, or dependency change.
- **Migration:** Revise update classification and reassessment rules, replay missed changes, and narrow authority pending new evidence.
- **Sunset:** Sunset trigger rules after deployed versions migrate and unclassified changes are resolved or isolated.
- **Conformance evidence:** Change manifest, CapabilityDelta/AuthorityDelta/HazardDelta analysis, trigger result, test scope, rollout telemetry, and rollback evidence.

## UAIS-1600 — Safety Management System

- **Normative scope:** guiding principles, 23 practices, records and improvement.
- **Dependencies:** UAIS-100 through UAIS-1500 as applicable to the declared system scope.
- **Minimum conformance:** owned practice profiles, inter-practice chains, evidence, and an extension mechanism for additional standards-family practices.
- **Exclusions:** copy of ITIL or service-management certification.
- **Versioning:** UAIS-1600 uses semantic major/minor/patch plus profile and test-suite identifiers; a major change publishes an evidence migration map.
- **Owner:** SMS Council (proposed multi-stakeholder body with conflict rules).
- **Review cycle:** Periodic review interval defined by Standards Governance, plus event-driven Technology Evolution Review whenever assumptions, capabilities, hazards, evidence methods, dependencies, external standards, or relevant technology materially change. Core UAIS sets no universal calendar interval.
- **Failure conditions:** Management practices cease to produce closed-loop safety improvement or repeatedly close actions without outcome evidence.
- **Migration:** Revise practices, ownership, escalation, measurement, and feedback links; re-open ineffective actions.
- **Sunset:** Retire a practice version after organizations map open actions and demonstrate continuity under its replacement.
- **Conformance evidence:** Practice objectives, accountable owners, trigger-to-action records, overdue escalations, outcome evidence, audit sample, and improvement-loop closure.

## International core and profiles

The shared core covers semantics, protocol integrity, evidence portability, certificate identifiers, minimum floors, AIVE exchange and challenge-suite interfaces. National and sector profiles may be stricter and define legal roles, retention, domain safe states and test thresholds. They cannot silently redefine the core or negotiate below a floor.

See `STANDARDS_CROSSWALK.md` for informative overlap. No crosswalk row asserts compliance or equivalence.











## UAIS-1700 — AI Trustworthiness and Error Evidence

### Scope
Versioned, domain-scoped behavioral trustworthiness profiles, user/operator error reporting, independent AI evaluation, error validation, error registries, operational evidence, rating calculation, uncertainty, separate rating-level and status changes, remediation, and version carryover.

### Dependencies
UAIS-1600 and relevant vocabulary, classification, assurance, lifecycle, and protocol standards.

### Minimum Conformance
A UAIS-1700-conforming implementation SHALL provide the 23 UAIS-1600 core practices plus the `AITrustworthinessAndErrorManagementPractice` extension practice. It SHALL also provide:
- AITrustworthinessProfile;
- TrustworthinessScoringPolicy with the mandatory field set defined for `TrustworthinessScoringPolicy`;
- TrustworthinessRatingLevel;
- EvidenceSupportedRating, CriticalErrorCap, FreshnessCap, IndependenceCap, DisagreementCap, and ChangeCarryoverCap;
- AIErrorReportingProtocol;
- AIErrorRegistry;
- AITrustworthinessRegistry;
- AIErrorType and AIErrorReportState;
- validated Operational Exposure Unit;
- independent evaluation method;
- required trustworthiness metrics;
- Trustworthiness Status;
- Rating Change Event and explanation;
- version carryover rules;
- hard-cap behavior for critical errors;
- appeals and privacy controls.

Minimum conformance test vectors SHALL include:

1. `Unrated` with current rating equal to null;
2. `Provisional` without an Active rating;
3. a status-only transition;
4. rating recalculation without a status change;
5. a critical trigger producing `Suspended` independently of aggregate rating; and
6. major or material version change invalidating carryover as required by the applicable policy.

### Out of Scope
UAIS-1700 does not certify general intelligence, does not claim an AI is safe, does not grant authority, does not replace SAL, and does not make ratings comparable across unrelated domains without a shared scoring policy.

### Failure Conditions
Raw user popularity changes rating; supplier self-rating is sufficient; evaluator independence is hidden; critical errors are averaged away; unresolved critical reports are ignored; evidence denominator is missing; stale evidence supports current rating; version changes inherit trust automatically; domain-specific ratings are presented as universal; rating becomes a legitimacy source.

### Migration
When scoring-policy version changes, retain old rating history, recalculate the current profile where evidence permits, show both policy versions during the migration window, and never rewrite historical ratings as if they were originally produced by the new policy.

### Sunset
A UAIS-1700 version is sunset when its error ontology, scoring policy requirements, independence model, or evidence requirements no longer capture material current AI behavior. Sunset SHALL trigger profile migration and, for affected high-consequence use, revalidation before continued reliance.

### Conformance Evidence
Versioned Trustworthiness Profile; scoring-policy specification; error-report and registry samples; deduplication/validation evidence; scenario suites; rubrics; evaluator-independence records; operational exposure evidence; rating calculations; hard-cap tests; version-carryover tests; privacy tests; appeals; remediation/revalidation evidence.

---
