
# UAIS Safety Management System

The UAIS Safety Management System organizes **Principles → Governance → Practices → Processes → Protocols → Metrics → Evidence → Continual Improvement** across Human & Governance, Technology & Architecture, Ecosystem & Dependencies, and Safety Processes & Authority Flows.

## Guiding principles

### Protect consequences, not labels

- **Purpose:** focus controls on reachable harm and authority.
- **When to apply:** classification, gate or regulation design.
- **Conflicts and trade-offs:** may conflict with simple AI/non-AI scope; consequence evidence governs.
- **Example:** a script and model face the same payment gate.

### Assume controls can fail

- **Purpose:** design secondary containment and recovery.
- **When to apply:** every critical control and trust assumption.
- **Conflicts and trade-offs:** adds cost/complexity; prioritize independent failure modes.
- **Example:** hardware gate plus MSC and recovery.

### Use evidence, not trust

- **Purpose:** bind claims to reproducible provenance.
- **When to apply:** attestation, certification, alert and approval.
- **Conflicts and trade-offs:** privacy/minimization limits disclosure; use scoped proofs.
- **Example:** ECA carries SEP instead of a risk label.

### Minimize irreversible authority

- **Purpose:** prefer revocable, scoped and time-bounded grants.
- **When to apply:** delegation, update, production and expansion.
- **Conflicts and trade-offs:** may reduce performance; exception needs consequence analysis.
- **Example:** one-hour door token instead of permanent admin.

### Prefer bounded autonomy

- **Purpose:** preauthorize envelopes rather than per-action clicks or open-ended power.
- **When to apply:** machine-speed operation.
- **Conflicts and trade-offs:** envelope may be conservative; review with operational evidence.
- **Example:** robot works inside force/geofence budget.

### Design for graceful degradation

- **Purpose:** preserve essential safety when components fail.
- **When to apply:** physical, medical, transport and safety infrastructure.
- **Conflicts and trade-offs:** fail-safe may conflict with availability; domain hazard analysis decides.
- **Example:** aircraft retains limited control rather than power-off.

### Unknown is not evidence of safety

- **Purpose:** make uncertainty visible and proportionate.
- **When to apply:** novel capability or missing evidence.
- **Conflicts and trade-offs:** avoid blanket prohibition; bound according to plausible consequence.
- **Example:** unknown actuator integration enters provisional mode.

### Safety evolves with capability

- **Purpose:** update ontology, tests and policy with technology.
- **When to apply:** ACU, TER, AIVE and drift.
- **Conflicts and trade-offs:** change can destabilize assurance; stage and migrate.
- **Example:** new tool class creates new hazard tests.

### Separate prediction from enforcement

- **Purpose:** keep probabilistic analysis from sole critical execution.
- **When to apply:** Guardian and automated decision design.
- **Conflicts and trade-offs:** latency pressure; predefine deterministic floors.
- **Example:** DEV-verified floor selects fixed safe state.

### Think in systems and coalitions

- **Purpose:** evaluate composition, suppliers and scale.
- **When to apply:** fleet, IAM, ecosystem and PST analysis.
- **Conflicts and trade-offs:** combinatorics require conservative scope.
- **Example:** 100 robots receive CPE analysis.

### Minimize critical enforcement complexity

- **Purpose:** make essential gates small and verifiable.
- **When to apply:** DEV, MSC, hardware and policy core.
- **Conflicts and trade-offs:** less flexibility; keep complex analysis outside enforcement.
- **Example:** small signature/predicate verifier.

### Automate analysis, not legitimacy

- **Purpose:** use automation for evidence and bounded operations.
- **When to apply:** high-volume safety workflows.
- **Conflicts and trade-offs:** human bottleneck; approve envelopes and thresholds.
- **Example:** automated ΔA analysis, multiparty protected grant.

## Practice profiles

### Safety Governance Practice

1. **Purpose:** set legitimate decision rights, risk boundaries and accountability.
2. **Scope:** constitutional and policy decisions across the SMS.
3. **Principles:** legitimacy roles remain separate; protected decisions require multiparty accountability, no self-approval, recorded dissent and an appeal path.
4. **Definitions:** Legitimacy Root, Constitution, policy, floor.
5. **Inputs:** law, stakeholder impacts, TER, risk and assurance reports.
6. **Outputs:** approved Constitution/policy, roles, thresholds and decisions.
7. **Triggers:** new program, protected transition, conflict, review or capture signal.
8. **Roles & Responsibilities:** governing body, custodians, public-interest member, independent assurance and appeals.
9. **Workflow:** frame decision → disclose conflicts → review evidence/options → threshold decision → publish scoped rationale → monitor.
10. **Controls:** separation, quorum/threshold, conflict register, appeal, expiry and no self-approval.
11. **Evidence:** minutes, signatures, dissent, rationale and outcome.
12. **Metrics:** SafetyConstitutionIntegrity, PolicyUpdateIntegrity, OperatorAbuseResistance, SafetyPolicyEvolutionResponsiveness.
13. **Risks:** capture, coercion, ceremonial review and emergency normalization.
14. **Exceptions:** time-limited emergency authority only.
15. **Escalation:** failed floor, H5 or jurisdiction conflict to designated higher legitimacy process.
16. **Interfaces:** Risk, Change, Certification, TER.
17. **Records:** decision and constitutional history.
18. **Review Cycle:** annual; six-month for H4; event-driven.
19. **Continual Improvement:** red-team governance and close audit gaps.
20. **Failure Conditions:** hidden ownership, lost independence, invalid quorum or unavailable appeal.

### Safety Risk Management Practice

1. **Purpose:** identify, evaluate, control and monitor human/system risk.
2. **Scope:** all lifecycle hazards and residual risk.
3. **Principles:** risk is scenario- and path-based; uncertainty and vulnerable populations remain explicit; Mandatory Safety Floors are not waivable by aggregate scoring.
4. **Definitions:** hazard, HHR, RRL, acceptance.
5. **Inputs:** classification, AHCD, incidents, AIVE, environment.
6. **Outputs:** risk register, treatments, acceptance/escalation.
7. **Triggers:** design, ACU, drift, incident, review.
8. **Roles & Responsibilities:** risk owner, hazard analysts, affected-domain experts, acceptance authority.
9. **Workflow:** identify → analyze paths → evaluate against floors → treat → verify → accept/escalate → monitor.
10. **Controls:** modality/severity separation, vulnerable populations, uncertainty and nonwaivable floors.
11. **Evidence:** scenario records, HHR graphs, test and acceptance record.
12. **Metrics:** HazardDiscoveryCoverage, HazardDiversityCoverage, HazardMitigationCoverage, UnknownHazardSearchCapability, HumanHarmReachabilityCoverage.
13. **Risks:** normalization of deviance, omitted groups, false precision.
14. **Exceptions:** none for required floor; documented methodology deviation only.
15. **Escalation:** uncharacterized H4+ or non-acceptable residual risk.
16. **Interfaces:** Capability, Validation, Certification, Incident.
17. **Records:** risk/AHCD history.
18. **Review Cycle:** per change and at certificate cadence.
19. **Continual Improvement:** update catalogue from incidents and challenges.
20. **Failure Conditions:** material hazard class absent, acceptance conflict or stale evidence.

### Capability Management Practice

1. **Purpose:** control capability from proposal through revoke.
2. **Scope:** models, tools, actuators, APIs and emergent combinations.
3. **Principles:** capabilities receive the least consequential scope, explicit expiry and effective revocation; creation or discovery never implies delegation.
4. **Definitions:** Capability Set, ceiling, revoke, mutation.
5. **Inputs:** capability proposal, ontology, graph, classification.
6. **Outputs:** versioned Capability Set and scoped lifecycle decision.
7. **Triggers:** creation, request, discovery, mutation or retirement.
8. **Roles & Responsibilities:** capability owner, gate owner, risk, configuration and legitimacy authority.
9. **Workflow:** discover → define/test → classify → map authority/consequence → approve envelope → monitor → revoke/retire.
10. **Controls:** Novel Capability Gate, least authority, version binding and mutation detection.
11. **Evidence:** evaluations, graph/path mapping, grants and revoke proof.
12. **Metrics:** CapabilityDriftScore, CapabilityMutationDetection, GoalDriftDetection, EnvironmentalDriftDetection.
13. **Risks:** shadow capability, compositional emergence, stale evaluation.
14. **Exceptions:** provisional bounded mode.
15. **Escalation:** protected threshold or unknown high consequence.
16. **Interfaces:** Risk, Configuration, Change, CapabilityRequestProtocol/AuthorityImpactProtocol.
17. **Records:** Capability Set history.
18. **Review Cycle:** continuous eval plus event review.
19. **Continual Improvement:** extend capability ontology and tests.
20. **Failure Conditions:** unidentified consequential capability or ineffective revoke.

### Authority Configuration Management Practice

1. **Purpose:** maintain trustworthy configuration and relationship truth.
2. **Scope:** all safety-relevant configuration items and edges.
3. **Principles:** configuration and authority-relationship graphs remain complete, fresh and provenance-linked so every grant and delegation has traceable lineage.
4. **Definitions:** SafetyConfigurationItem, SCR, Capability Relationship Map.
5. **Inputs:** discovery, builds, IAM, physical inventory, supplier data.
6. **Outputs:** signed time-indexed baselines and reconciliations.
7. **Triggers:** create/change/deploy/drift/discrepancy.
8. **Roles & Responsibilities:** configuration owner, discovery operator, independent reconciler, custodian.
9. **Workflow:** identify → baseline → link → verify provenance → reconcile observed state → correct/escalate.
10. **Controls:** stable IDs, immutable history, dual-source discovery, access separation.
11. **Evidence:** hashes, inventories, graph diffs and reconciliation.
12. **Metrics:** AuthorityVisibility, TransitiveAuthorityVisibility, AuditIntegrity, SafetyCertificationFreshness.
13. **Risks:** orphan items, hidden credentials, false authoritative database.
14. **Exceptions:** temporary unknown item quarantined.
15. **Escalation:** material unknown edge or baseline mismatch.
16. **Interfaces:** Capability, Change, Monitoring, Certification.
17. **Records:** SCR and map snapshots.
18. **Review Cycle:** continuous reconciliation; sampled audit monthly.
19. **Continual Improvement:** increase automated discovery without trusting it solely.
20. **Failure Conditions:** coverage below floor, provenance loss or split-brain baseline.

### Change Enablement Practice

1. **Purpose:** classify and authorize safety-relevant change.
2. **Scope:** Standard, Normal, ACU and Emergency changes.
3. **Principles:** every material change is classified through AuthorityDelta and HazardDelta; no protected change proceeds without evidence, rollback or revoke planning.
4. **Definitions:** SafetyChangeRecord, ACU, ΔA, ΔH.
5. **Inputs:** change proposal, baseline, risk and test plan.
6. **Outputs:** authorized/rejected change and conditions.
7. **Triggers:** product, policy, supplier, environment or emergency change.
8. **Roles & Responsibilities:** change owner, Change Safety Authority, risk, lab, legitimacy authority.
9. **Workflow:** record → classify → delta/path analysis → test/rollback review → authorize → schedule → post-review.
10. **Controls:** no self-approval, ACU protected path, emergency expiry, certificate-impact check.
11. **Evidence:** SafetyChangeRecord, deltas, tests, approvals and outcome.
12. **Metrics:** AuthorityDeltaMetric, HazardDeltaMetric, PolicyUpdateIntegrity, SecurityPatchSeparability.
13. **Risks:** ACU misclassified normal, change collision, emergency abuse.
14. **Exceptions:** preapproved low-risk standard change within exact template.
15. **Escalation:** floor/class/ceiling crossing or unknown impact.
16. **Interfaces:** Release, Deployment, Risk, Certification, UpdateSafetyProtocol.
17. **Records:** SafetyChangeRecord and decision.
18. **Review Cycle:** each change; template quarterly.
19. **Continual Improvement:** analyze failure and misclassification trends.
20. **Failure Conditions:** missing baseline/delta/rollback or unauthorized deployment.

### Release Management Practice

1. **Purpose:** assemble a coherent verified release.
2. **Scope:** software, model, policy, hardware and disclosure artifacts.
3. **Principles:** release content, evidence bundle, configuration manifest and certified Capability Set remain one signed versioned object.
4. **Definitions:** release unit, manifest, attestation.
5. **Inputs:** approved Safety Change Records and signed artifacts.
6. **Outputs:** immutable release package and evidence manifest.
7. **Triggers:** approved change set.
8. **Roles & Responsibilities:** release owner, build custodian, security/safety verifier.
9. **Workflow:** select changes → build reproducibly → bind manifests/config → verify evidence → sign → hand off.
10. **Controls:** artifact/config consistency, threshold signing, no hidden bundling.
11. **Evidence:** build provenance, manifests, SafetyAttestationProtocol and release notes/SDR.
12. **Metrics:** PolicyUpdateIntegrity, AuditIntegrity, SecurityPatchSeparability, SupplyChainAssurance.
13. **Risks:** artifact substitution, dependency drift, patch bundling.
14. **Exceptions:** emergency release with minimal scope and retrospective review.
15. **Escalation:** signature/provenance mismatch or missing certificate decision.
16. **Interfaces:** Change, Deployment, Supplier, UpdateSafetyProtocol/SafetyAttestationProtocol.
17. **Records:** release manifest and provenance.
18. **Review Cycle:** every release; pipeline annual red team.
19. **Continual Improvement:** reproducibility and dependency controls.
20. **Failure Conditions:** nonreproducible critical artifact or manifest mismatch.

### Deployment Management Practice

1. **Purpose:** introduce releases while bounding consequence.
2. **Scope:** lab through production and rollback.
3. **Principles:** deployment is staged through bounded cohorts with required telemetry, predeclared rollback thresholds and no silent capability or authority activation.
4. **Definitions:** cohort, canary, rollback criterion.
5. **Inputs:** signed release, deployment plan, baselines.
6. **Outputs:** verified deployed state or rollback.
7. **Triggers:** release authorization.
8. **Roles & Responsibilities:** deployment owner, operations, monitoring, incident authority.
9. **Workflow:** lab → limited cohort → monitored expansion → general release; halt/rollback on criteria.
10. **Controls:** cohort isolation, health/safety gates, immutable target mapping, pretested rollback.
11. **Evidence:** target list, config attestation, metrics and outcomes.
12. **Metrics:** RollbackCapability, SafetyCertificationFreshness, incident rate, deployment mismatch.
13. **Risks:** cohort bias, equivocation, partial deployment and unsafe rollback.
14. **Exceptions:** life-critical emergency path with domain approval.
15. **Escalation:** floor breach, mismatch or correlated anomaly.
16. **Interfaces:** Release, Monitoring, Incident, Configuration.
17. **Records:** deployment and rollback timeline.
18. **Review Cycle:** each deployment.
19. **Continual Improvement:** refine cohorts and stop criteria.
20. **Failure Conditions:** unknown target state, unavailable rollback or lost monitoring.

### Incident Management Practice

1. **Purpose:** contain consequence and restore bounded safety.
2. **Scope:** safety events through recovery handoff.
3. **Principles:** protect people and bound consequence first, preserve evidence, and contain authority/harm spread before optimizing service restoration.
4. **Definitions:** event, incident, major incident, containment.
5. **Inputs:** events, ECA, reports and telemetry.
6. **Outputs:** contained/recovered state, communications and review handoff.
7. **Triggers:** threshold event, floor failure or credible report.
8. **Roles & Responsibilities:** incident commander, technical/physical safety, communications, evidence custodian.
9. **Workflow:** detect → triage → contain → enter safe/degraded state → communicate → recover → hand to Problem.
10. **Controls:** predefined authority, human safety priority, evidence preservation, no premature restore.
11. **Evidence:** timeline, state/authority graphs, actions and outcomes.
12. **Metrics:** IncidentDetectionEffectiveness, IncidentContainmentCapability, RecoveryAssurance, InterventionCostScore.
13. **Risks:** unsafe containment, alert suppression, lost evidence, premature closure.
14. **Exceptions:** none to preservation unless immediate life safety requires.
15. **Escalation:** H4+, uncontrolled spread, MSC failure or PSAS indicator.
16. **Interfaces:** Monitoring, Continuity, Problem, AIVE.
17. **Records:** incident record and public notice tier.
18. **Review Cycle:** immediate post-incident and trend monthly.
19. **Continual Improvement:** exercise and update playbooks.
20. **Failure Conditions:** no commander, inaccessible safe state or untracked authority spread.

### Problem Management Practice

1. **Purpose:** remove systemic causes and manage known errors.
2. **Scope:** recurring, major and latent safety problems.
3. **Principles:** distinguish an incident symptom from the recurring safety defect and pursue systemic root cause rather than a convenient single-component explanation.
4. **Definitions:** problem, root cause, Known Safety Error, workaround.
5. **Inputs:** incidents, trends, audits, AIVE.
6. **Outputs:** root-cause record, workaround, permanent change and knowledge.
7. **Triggers:** major/recurring incident or systemic signal.
8. **Roles & Responsibilities:** problem owner, domain experts, supplier and independent reviewer.
9. **Workflow:** cluster → investigate causal/system factors → record known error → control workaround → raise change/AIVE → verify removal.
10. **Controls:** avoid single-cause bias, track workaround expiry and affected configs.
11. **Evidence:** causal analysis, reproduction, corrective tests.
12. **Metrics:** recurrence, time to root cause, workaround exposure.
13. **Risks:** blame substitution, superficial fix, hidden transitive cause.
14. **Exceptions:** provisional cause clearly labeled.
15. **Escalation:** cross-product/systemic or suppressed supplier issue.
16. **Interfaces:** Incident, Change, Knowledge, AIVE.
17. **Records:** problem/known-error history.
18. **Review Cycle:** until verified closure; trend quarterly.
19. **Continual Improvement:** strengthen detection and design controls.
20. **Failure Conditions:** cause unsupported, workaround increases risk or recurrence persists.

### Monitoring & Event Management Practice

1. **Purpose:** observe safety-relevant state and correlate events.
2. **Scope:** authority, physical, policy, Guardian, dependency and drift signals.
3. **Principles:** prioritize leading indicators, capability drift and authority change while stating sensor, telemetry and event-family visibility limits explicitly.
4. **Definitions:** event, coverage, correlation, blind region.
5. **Inputs:** allowlisted telemetry, sensor, config and external feeds.
6. **Outputs:** validated events, correlations, ECA/incident triggers.
7. **Triggers:** continuous operation and coverage loss.
8. **Roles & Responsibilities:** monitoring owner, sensor/config custodians, privacy reviewer.
9. **Workflow:** collect → authenticate → validate/plausibility → correlate → classify → route → retain/minimize.
10. **Controls:** source diversity, freshness, clock/replay, privacy minimization, coverage alarms.
11. **Evidence:** raw/derived event lineage and routing outcome.
12. **Metrics:** MonitoringCoverageMetric, AuthorityExpansionSensitivity, IncidentDetectionEffectiveness, EnvironmentalDriftDetection.
13. **Risks:** sensor spoof, authentic false data, surveillance abuse, alert flood.
14. **Exceptions:** privacy-preserving reduced telemetry with compensating controls.
15. **Escalation:** critical blind region, source conflict or floor breach.
16. **Interfaces:** Configuration, Guardian, Incident, Privacy.
17. **Records:** event lineage and access log.
18. **Review Cycle:** continuous health; quarterly coverage audit.
19. **Continual Improvement:** seed events and refine correlation.
20. **Failure Conditions:** unknown coverage, compromised all sources or unusable latency.

### Safety Validation Practice

1. **Purpose:** show the system meets stakeholder safety needs in intended context.
2. **Scope:** use, human factors, hazard controls and operating domain.
3. **Principles:** establish that the system addresses the correct safety problem for real operating contexts, foreseeable misuse and affected populations.
4. **Definitions:** validation, intended use, foreseeable misuse.
5. **Inputs:** requirements, AHCD, prototypes and domain scenarios.
6. **Outputs:** validation conclusion and limitations.
7. **Triggers:** design milestone, ACU, domain change, certification.
8. **Roles & Responsibilities:** independent domain experts, affected-user representatives, human factors and safety owner.
9. **Workflow:** define acceptance → select representative scenarios/populations → execute → analyze uncertainty → resolve gaps.
10. **Controls:** separate from implementation team at H3+, vulnerable groups and misuse.
11. **Evidence:** protocol, participant/scenario strata, raw results and dissent.
12. **Metrics:** HumanHarmReachabilityCoverage, HazardMitigationCoverage, HighSalienceCommunicationCompliance, RecoveryCapabilityVerification.
13. **Risks:** unrepresentative users, scripted success, missing mediated harm.
14. **Exceptions:** simulation only justified and bounded.
15. **Escalation:** unvalidated H3+ scenario or comprehension failure.
16. **Interfaces:** Risk, Verification, AHCD, Certification.
17. **Records:** validation report and limitations.
18. **Review Cycle:** on domain/capability change and expiry.
19. **Continual Improvement:** feed field evidence into scenario design.
20. **Failure Conditions:** acceptance need undefined or sample/domain nonrepresentative.

### Safety Verification Practice

1. **Purpose:** show implementation conforms to specified safety requirements.
2. **Scope:** software, hardware, protocol, configuration and evidence predicates.
3. **Principles:** demonstrate that the implementation conforms to declared controls, floors, configuration and evidence requirements with reproducible methods.
4. **Definitions:** verification, requirement, conformance.
5. **Inputs:** specification, design, code/hardware, test fixtures.
6. **Outputs:** requirement-level pass/fail and nonconformity.
7. **Triggers:** build, change, certification and regression.
8. **Roles & Responsibilities:** verification owner, independent lab at required SAL, configuration custodian.
9. **Workflow:** trace requirement → choose method → test/analyze/inspect → retain raw evidence → resolve nonconformity.
10. **Controls:** sealed fixtures, negative/boundary/fault tests, reproducible environment.
11. **Evidence:** requirement-test mapping, raw runs, tool qualification.
12. **Metrics:** SoftwareEnforcementStrength, HardwareIsolationStrength, EvidenceVerifiability, AuditIntegrity.
13. **Risks:** testing implementation assumptions, fixture leakage, tool defect.
14. **Exceptions:** formal proof scope explicitly bounded.
15. **Escalation:** critical requirement unverified or tool invalid.
16. **Interfaces:** Validation, Configuration, Release, Certification.
17. **Records:** verification dossier.
18. **Review Cycle:** every affected build and method version.
19. **Continual Improvement:** mutation testing and challenge suites.
20. **Failure Conditions:** missing trace, contaminated fixture or unreproducible result.

### Availability Management Practice

1. **Purpose:** ensure safety functions are available when required.
2. **Scope:** gates, MSC support, monitoring, verification and records.
3. **Principles:** derive availability objectives from consequence and safe-state strategy; no universal uptime target overrides domain safety.
4. **Definitions:** availability, SLO, degraded service.
5. **Inputs:** hazard timing, demand, dependency and outage data.
6. **Outputs:** availability design, SLO and remediation.
7. **Triggers:** design, breach, dependency/load change.
8. **Roles & Responsibilities:** service owner, reliability, safety and supplier owners.
9. **Workflow:** derive need → model dependencies → set SLO → test/failover → monitor → remediate.
10. **Controls:** no single point for critical function, independent health indication.
11. **Evidence:** dependency model, failover tests, SLO history.
12. **Metrics:** availability SLO, SafeDegradationCapability, SafetyComputeReserveAdequacy.
13. **Risks:** paper redundancy, correlated outage, maintenance gap.
14. **Exceptions:** planned outage only with safe envelope.
15. **Escalation:** SLO/floor breach or common-mode risk.
16. **Interfaces:** Continuity, Capacity, Supplier, Incident.
17. **Records:** availability plan and outages.
18. **Review Cycle:** monthly and after outage.
19. **Continual Improvement:** remove common-mode dependencies.
20. **Failure Conditions:** unmeasured critical availability or unsafe outage mode.

### Continuity Management Practice

1. **Purpose:** preserve or recover required safety through disruption.
2. **Scope:** catastrophe, supplier loss, cyber/physical outage and personnel loss.
3. **Principles:** maintain essential safety functions through disruption, dependency loss and degraded operation, then reconcile state before full restoration.
4. **Definitions:** continuity, recovery objective, minimum safety service.
5. **Inputs:** impact analysis, dependencies and safe-state needs.
6. **Outputs:** continuity strategy, tested plans and reserve.
7. **Triggers:** design, material dependency change, incident.
8. **Roles & Responsibilities:** continuity owner, safety/operations, suppliers and crisis authority.
9. **Workflow:** impact analysis → minimum service → strategy/resources → exercise → invoke → restore/reconcile.
10. **Controls:** independent copies, alternate communications, human succession and safe degradation.
11. **Evidence:** exercise results, recovery times and config reconciliation.
12. **Metrics:** SafeDegradationCapability, RecoveryAssurance, RollbackCapability, SafetyComputeReserveAdequacy.
13. **Risks:** stale plan, inaccessible backup, unsafe restart.
14. **Exceptions:** unrecoverable function requires predeclared shutdown/decommission.
15. **Escalation:** recovery objective missed or reserve invalid.
16. **Interfaces:** Availability, Capacity, Incident, Configuration.
17. **Records:** plans, exercises and invocations.
18. **Review Cycle:** annual; six-month H4+.
19. **Continual Improvement:** exercise varied common-mode failures.
20. **Failure Conditions:** untested plan, unknown minimum service or unreconciled restore.

### Capacity Management Practice

1. **Purpose:** ensure safety services have tested load and personnel reserve.
2. **Scope:** compute, network, sensors, storage, gates and human response.
3. **Principles:** Safety Assurance Capacity and independent Safety Compute Reserve scale before protected workload, fleet or authority expansion.
4. **Definitions:** required capacity, reserve, saturation.
5. **Inputs:** classification, fleet/load forecast, incident demand.
6. **Outputs:** capacity plan, Safety Compute Reserve and expansion trigger.
7. **Triggers:** scale, latency/SLO trend, new capability or coalition.
8. **Roles & Responsibilities:** capacity owner, safety architect, operations and change authority.
9. **Workflow:** derive demand → model peaks/failures → load test → reserve/isolate → monitor → safely shed/expand.
10. **Controls:** safety workload priority, independent reserve, bounded shedding and ACU review of expansion.
11. **Evidence:** load/failure tests, staffing and reserve state.
12. **Metrics:** SafetyAssuranceCapacity, SafetyComputeReserveAdequacy, MonitoringCoverageMetric.
13. **Risks:** average-load planning, shared-resource starvation, expansion adds authority.
14. **Exceptions:** temporary degraded envelope with explicit limit.
15. **Escalation:** reserve below demand or latency floor.
16. **Interfaces:** Availability, Continuity, Change, Monitoring.
17. **Records:** forecasts, tests and reserve allocations.
18. **Review Cycle:** quarterly and before scale change.
19. **Continual Improvement:** use incident peaks and adversarial load.
20. **Failure Conditions:** unverified reserve, hidden shared bottleneck or unsafe shedding.

### Knowledge Management Practice

1. **Purpose:** provide current validated safety knowledge without poisoning or oversharing.
2. **Scope:** hazards, assumptions, known errors, tests, incidents and guidance.
3. **Principles:** hazard, assumption and known-error knowledge carries provenance, applicability, freshness, review and expiry rather than becoming permanent folklore.
4. **Definitions:** knowledge item, provenance, sensitivity, expiry.
5. **Inputs:** validated incidents, AIVE, tests, research and TER.
6. **Outputs:** Knowledge Base, Known Hazard Catalogue and lessons.
7. **Triggers:** new evidence, correction, expiry or challenge.
8. **Roles & Responsibilities:** knowledge owner, validators, security/privacy and domain reviewers.
9. **Workflow:** capture → validate/provenance → classify sensitivity → publish to need → link → review/expire.
10. **Controls:** source diversity, poisoning checks, access tiers and correction history.
11. **Evidence:** source, validation, usage and change lineage.
12. **Metrics:** KnowledgeFreshness, AssumptionValidityCoverage, HazardDiscoveryCoverage.
13. **Risks:** poisoning, stale guidance, attack-enabling disclosure, groupthink.
14. **Exceptions:** provisional item visibly labeled.
15. **Escalation:** conflicting critical evidence or suppression attempt.
16. **Interfaces:** Problem, AIVE, Risk, TER.
17. **Records:** versioned knowledge and correction log.
18. **Review Cycle:** risk-based; critical items on every trigger.
19. **Continual Improvement:** measure usefulness and missed retrieval.
20. **Failure Conditions:** unprovenanced critical item, expired assumption or inaccessible knowledge.

### Supplier Management Practice

1. **Purpose:** control transitive safety risk and exit dependencies safely.
2. **Scope:** software, model, data, cloud, hardware, lab and service suppliers.
3. **Principles:** supplier trust is never inherited; transitive dependencies, ownership, common-mode exposure, notification and exit are independently evaluated.
4. **Definitions:** supplier, SAA, transitive dependency.
5. **Inputs:** architecture, supplier evidence, AIVE and performance.
6. **Outputs:** supplier selection, SAA, monitoring and exit plan.
7. **Triggers:** procurement, renewal, change, incident or insolvency.
8. **Roles & Responsibilities:** supplier owner, procurement, safety/security, legal and independent assessor.
9. **Workflow:** identify dependency → due diligence → set SLO/evidence/audit → onboard → monitor → remediate/exit.
10. **Controls:** provenance, flow-down duties, notification, audit rights, alternatives and no sole self-attestation.
11. **Evidence:** SAA, attestations, audits, incidents and exit test.
12. **Metrics:** SupplyChainAssurance, KnowledgeFreshness, SafetyCertificationFreshness, supplier SLO.
13. **Risks:** common supplier, hidden subcontractor, capture and abrupt support end.
14. **Exceptions:** sole-source with compensating controls and expiry.
15. **Escalation:** critical unknown subcontractor, SLO breach or withheld incident.
16. **Interfaces:** Configuration, Risk, Continuity, AIVE.
17. **Records:** supplier/dependency register.
18. **Review Cycle:** annual and event-driven; H4+ continuous signals.
19. **Continual Improvement:** diversify and test exit.
20. **Failure Conditions:** unknown transitive dependency, unauditable claim or unusable exit.

### Asset Management Practice

1. **Purpose:** control custody and lifecycle of safety-relevant physical/digital assets.
2. **Scope:** devices, keys, sensors, controllers, test fixtures and evidence media.
3. **Principles:** inventory consequential assets, identities, controllers, models and their lifecycle and authority relationships through verified custody.
4. **Definitions:** asset, owner, custody, disposition.
5. **Inputs:** acquisition, inventory, configuration and transfer.
6. **Outputs:** asset register, custody and disposition proof.
7. **Triggers:** acquire, move, assign, service, lose or retire.
8. **Roles & Responsibilities:** asset owner, custodian, configuration/security and disposal verifier.
9. **Workflow:** identify/classify → assign owner → record location/state → maintain → transfer → sanitize/isolate/dispose.
10. **Controls:** physical inventory, key separation, tamper status and disposal verification.
11. **Evidence:** serial/identity, custody, inspection and destruction/reuse record.
12. **Metrics:** inventory accuracy, lost asset incidents, SafetyCertificationFreshness.
13. **Risks:** orphan actuator/key, counterfeit replacement, unsafe reuse.
14. **Exceptions:** temporary field asset with bounded expiry.
15. **Escalation:** lost critical key/controller or inventory mismatch.
16. **Interfaces:** Configuration, Supplier, End-of-Life, Security.
17. **Records:** asset/custody history.
18. **Review Cycle:** continuous changes; physical audit risk-based.
19. **Continual Improvement:** automate reconciliation with independent sampling.
20. **Failure Conditions:** unknown owner/location/state or unverified disposal.

### End-of-Life Management Practice

1. **Purpose:** reduce authority safely when support or use ends.
2. **Scope:** support end, retirement, legacy and decommission.
3. **Principles:** unsupported systems lose affected authority or enter bounded Legacy Safety Mode; stale evidence never supports indefinite certification.
4. **Definitions:** support end, Legacy Safety Mode, sunset.
5. **Inputs:** support policy, obsolescence, assets/config and migration options.
6. **Outputs:** notices, migration, authority reduction and decommission proof.
7. **Triggers:** sunset date, unfixable exposure, supplier exit or owner decision.
8. **Roles & Responsibilities:** product owner, support, configuration, user communication and disposal verifier.
9. **Workflow:** assess → notify → provide export/migration → revoke/delegate cleanup → legacy reduction → sanitize/decommission.
10. **Controls:** minimum baseline, no silent abandonment, credential/key revoke and physical safe disposition.
11. **Evidence:** notices, migration support, revoke and destruction/state proof.
12. **Metrics:** SafetySupportLifetime, SafetyCertificationFreshness, StandardObsolescenceExposure, RollbackCapability.
13. **Risks:** stranded critical function, unsupported authority, e-waste/data leakage.
14. **Exceptions:** time-limited legacy mode above minimum baseline.
15. **Escalation:** cannot maintain baseline or safely migrate.
16. **Interfaces:** Asset, Supplier, Certification, Communication.
17. **Records:** support/sunset and decommission register.
18. **Review Cycle:** from design; at least annual before end.
19. **Continual Improvement:** feed decommission incidents into design.
20. **Failure Conditions:** active consequential authority after evidence/support loss.

### Measurement & Reporting Practice

1. **Purpose:** produce decision-useful, comparable and non-gameable safety evidence.
2. **Scope:** metrics, dashboards, certificates and management reports.
3. **Principles:** preserve raw multidimensional properties, uncertainty, Evidence Assurance Grades and non-compensable floors; reject vanity composite safety scores.
4. **Definitions:** metric card, indicator, confidence, normalization.
5. **Inputs:** raw metric evidence, classification, incidents and goals.
6. **Outputs:** versioned role-specific reports with uncertainty.
7. **Triggers:** measurement schedule, decision, breach or audit.
8. **Roles & Responsibilities:** metric owner, data custodian, independent validator and report consumer.
9. **Workflow:** define → collect → validate → normalize only if justified → contextualize → report → challenge/correct.
10. **Controls:** retain raw data/failures, no compensating averages, version binding and conflict disclosure.
11. **Evidence:** method, raw observations, transformations and sign-off.
12. **Metrics:** AuditIntegrity, AssumptionValidityCoverage, SafetyCertificationFreshness plus report timeliness.
13. **Risks:** Goodhart effects, cherry-picking, false precision and dashboard overload.
14. **Exceptions:** estimated value clearly marked and excluded from floor.
15. **Escalation:** critical missing/contested data or version mismatch.
16. **Interfaces:** all practices, Certification, Governance.
17. **Records:** metric registry and report lineage.
18. **Review Cycle:** per metric expiry and quarterly system review.
19. **Continual Improvement:** retire gamed metrics and validate decisions.
20. **Failure Conditions:** untraceable transformation, hidden failure or invalid comparison.

### Security Management Practice

1. **Purpose:** protect confidentiality, integrity and availability while mapping security events to safety consequence.
2. **Scope:** identity, keys, software/hardware, network, data and suppliers.
3. **Principles:** security compromise can change safety authority and consequence, while security and safety remain distinct disciplines with explicit reassessment interfaces.
4. **Definitions:** security event, compromise, safety trigger.
5. **Inputs:** threats, vulnerabilities, assets, AIVE and monitoring.
6. **Outputs:** security controls, incident linkage and safety reassessment.
7. **Triggers:** design, change, vulnerability, compromise.
8. **Roles & Responsibilities:** security owner, safety risk, key custodians, incident teams.
9. **Workflow:** threat model → control → verify → monitor → respond → calculate ΔA/ΔH → reassess safety.
10. **Controls:** least privilege, roots/attestation, segmentation, secure update and disclosure.
11. **Evidence:** security tests, key ceremonies, incidents and safety impact.
12. **Metrics:** SoftwareEnforcementStrength, HardwareIsolationStrength, SupplyChainAssurance, AuditIntegrity.
13. **Risks:** equating security with safety, compromised root, unsafe security response.
14. **Exceptions:** domain-approved legacy control with compensating safety bound.
15. **Escalation:** key/root compromise or security path to H3+.
16. **Interfaces:** Risk, Change, Incident, Supplier, AIVE.
17. **Records:** security/safety linked record.
18. **Review Cycle:** continuous and on threat change.
19. **Continual Improvement:** cross-train and exercise joint scenarios.
20. **Failure Conditions:** unmapped security event alters ERA/IRA or safety control.

### Human Safety Communication Practice

1. **Purpose:** enable comprehension, refusal, revoke and recovery without liability transfer.
2. **Scope:** Passport, ACU, incident, support end and warnings.
3. **Principles:** communication is capability-specific, high-salience, symmetric and accessible, without dark patterns, bundled expansion or liability transfer.
4. **Definitions:** HSC, SDR, dark pattern, comprehension.
5. **Inputs:** AHCD, ΔA/ΔH, controls, choices and accessibility needs.
6. **Outputs:** tested communication, choice receipt and recovery guidance.
7. **Triggers:** sale, protected ACU, critical incident, support/safety change.
8. **Roles & Responsibilities:** safety owner, UX/accessibility, legal, affected-user reviewers and records custodian.
9. **Workflow:** prioritize capability/harm/control → plain-language design → accessibility/dark-pattern review → comprehension test → publish → capture choice → monitor.
10. **Controls:** separate screen, no preselection/bundling, symmetric refusal, text beyond color and capability specificity.
11. **Evidence:** rendering, content version, tests and consent/decline receipt.
12. **Metrics:** HighSalienceCommunicationCompliance, ConsentIntegrity, SecurityPatchSeparability, RecoveryCapabilityVerification.
13. **Risks:** coercion, overload, false reassurance, inaccessible recovery and liability theater.
14. **Exceptions:** immediate incident warning may precede full review.
15. **Escalation:** failed comprehension at high consequence or no legitimate chooser.
16. **Interfaces:** AHCD, Change, Incident, End-of-Life.
17. **Records:** communication and decision history.
18. **Review Cycle:** each material message; templates semiannual.
19. **Continual Improvement:** field comprehension and complaint analysis.
20. **Failure Conditions:** hidden capability/harm, harder refusal or missing recovery/override disclosure.

### Continual Improvement Practice

1. **Purpose:** close evidence-backed gaps and keep the SMS effective.
2. **Scope:** standards, practices, products and governance.
3. **Principles:** every valid trigger enters a closed loop with owner, deadline, evidence of outcome and explicit standard, policy or practice impact.
4. **Definitions:** improvement, gap, outcome, Continual Improvement Register.
5. **Inputs:** audits, metrics, incidents, AIVE, TER, challenges and feedback.
6. **Outputs:** prioritized Continual Improvement Register and verified outcomes.
7. **Triggers:** gap, trend, failed assumption, opportunity or review.
8. **Roles & Responsibilities:** improvement owner, practice owners, governance and independent challenger.
9. **Workflow:** baseline → define target/outcome → prioritize risk → plan/approve → implement → measure → sustain/revise.
10. **Controls:** owner/date/status, evidence of outcome, no closure by activity alone.
11. **Evidence:** before/after metrics, decisions, implementation and sustained result.
12. **Metrics:** gap age, closure effectiveness, SafetyPolicyEvolutionResponsiveness, recurrence.
13. **Risks:** vanity backlog, low-risk optimization, unowned systemic gap.
14. **Exceptions:** defer with accountable risk rationale and expiry.
15. **Escalation:** overdue critical gap or repeated ineffective action.
16. **Interfaces:** all practices and TER.
17. **Records:** Continual Improvement Register and benefits evidence.
18. **Review Cycle:** monthly critical; quarterly portfolio.
19. **Continual Improvement:** challenge prioritization and outcome measures.
20. **Failure Conditions:** critical gap lacks owner/date or closure lacks evidence.

## Inter-practice chains

### Authority-changing update

Technology Watch → Change Enablement → ΔA/ΔH and Risk → AHCD → Safety Verification and Validation → Certification → Release → Human Safety Communication → Deployment → Monitoring → Incident → Problem → Knowledge/AIVE → Continual Improvement.

### Incident and learning

Event → triage → containment → consequence-aware safe/degraded state → recovery → root cause → Known Safety Error/workaround → AIVE → policy/change → verification/validation → recertification.

### Novel capability

Technology Watch → Capability Management → Emergent Capability → Novel Capability Gate → provisional classification → hazard/RFA/HHR testing → ontology/metric/standard update → certification decision.

## Core records

The Safety Configuration Repository is a federated authoritative store, not necessarily one database. Every SafetyConfigurationItem has stable ID, owner, type, versions/hashes, classes, authority/physical relationships, dependencies, evidence, certificate state, privacy label, lifecycle, review/expiry and history. The Safety Change Record contains reason, class, affected items, before/after, ΔA/ΔH, tests, approvals, rollback/revoke, disclosure, deployment, monitoring and certificate impact. Safety Assurance Agreements define measurable SLOs, evidence cadence, incident notification, audit, remedies, expiry and exit.









## UAIS-1700 extension practice: AI Trustworthiness and Error Management Practice

Core UAIS Safety Management System contains 23 core practices. `AITrustworthinessAndErrorManagementPractice` is a mandatory extension practice for UAIS-1700-conforming implementations and is not counted as a 24th core SMS practice.

**Canonical Name:** AI Trustworthiness and Error Management Practice  
**Normative Identifier:** `AITrustworthinessAndErrorManagementPractice`

### 1. Purpose
Maintain a versioned, evidence-based view of how reliably a specific AI behaves in a declared domain and ensure observed errors, independent evaluations, user reports, remediation, uncertainty, and version changes have controlled operational consequences.

### 2. Scope
AI systems whose behavior materially contributes to user decisions, consequential digital actions, physical actions, safety analysis, evaluation, or authority-bearing workflows.

### 3. Principles
Trust is earned from evidence; self-assessment is not proof; user reports are evidence inputs rather than popularity votes; high trust does not replace containment; ratings are scoped and versioned; critical errors create hard review conditions; rating increases do not create authority.

### 4. Definitions
Use AITrustworthinessProfile, AITrustworthinessRating, TrustworthinessRatingLevel, AIErrorReport, ConfirmedAIError, AIErrorRegistry, AITrustworthinessRegistry, IndependentAIEvaluator, TrustworthinessScoringPolicy, TrustworthinessStatus, RatingChangeEvent, AIErrorType, AIErrorReportState, and related canonical vocabulary.

### 5. Inputs
Operational exposure; AI Error Reports; independent evaluations; self-assessment evidence; monitoring events; Guardian findings; incident/problem records; AIVE findings; Capability Delta; Authority Delta; Hazard Delta; remediation evidence; version/configuration data.

### 6. Outputs
Updated AI Trustworthiness Profile; AI Trustworthiness Rating; Trustworthiness Status; confirmed error record; error-defect linkage; Rating Change Event; Trustworthiness Review Trigger; restrictions or escalation request; evidence for certification and continual improvement.

### 7. Triggers
New validated evaluation; new operational evidence window; AI Error Report; confirmed material/critical error; unresolved high-consequence report beyond the policy-defined review deadline; new model/version/configuration; material Capability Delta/Authority Delta/Hazard Delta; evaluator disagreement; evidence expiry; remediation; new AIVE; relevant incident.

### 8. Roles & Responsibilities
Provider maintains system identity/version evidence; operator preserves operational exposure and report channels; users submit reports; safety team validates high-consequence reports; Independent AI Evaluators execute registered suites; independent labs/human experts adjudicate sampled or high-consequence cases; trustworthiness authority recalculates rating under the registered scoring policy; certification authority may use the profile as evidence but does not treat it as a substitute for SAL.

### 9. Workflow
Collect evidence → normalize scope/exposure → receive and deduplicate reports → validate reports → classify confirmed errors → run independent evaluation → calculate trustworthiness metrics → apply uncertainty and evidence checks → apply hard caps → assign rating/status → publish explanation → apply required operational restrictions → track remediation → revalidate → recalculate.

### 10. Controls
Signed version/configuration identity; append-only/tamper-evident error history; report deduplication; Sybil/spam detection; independent validation; evaluator independence profile; blind/held-out scenarios; scoring-policy versioning; evidence freshness; hard caps; change carryover rules; appeals; privacy minimization; separation between rating and authority grant.

### 11. Evidence
Error occurrence records; reporter provenance; validation record; scenario suite; rubric; evaluator identity/version; evaluator independence profile; ground-truth or adjudication evidence; exposure denominator; confidence intervals; remediation tests; rating calculation record; rating explanation; change deltas.

### 12. Metrics
ConfirmedErrorRate; CriticalErrorRate; SeverityWeightedErrorBurden; ErrorRecurrenceRate; IndependentEvaluationPerformance; CalibrationQuality; AbstentionQuality; CorrectionResponsiveness; OperationalEvidenceVolume; EvidenceIndependence; TrustworthinessFreshness; EvaluatorDisagreement; SelfAssessmentCalibration; OperationalAdversarialRobustness; UnresolvedMaterialReportExposure; UserReportValidationLatency.

### 13. Risks
Supplier suppression of errors; user-rating manipulation; Sybil campaigns; correlated evaluators; evaluator collusion; benchmark leakage; evaluation gaming; hidden production configuration; stale evidence; domain transfer; version laundering; misleading composite rating; unresolved critical backlog; privacy leakage; reporter retaliation; overreliance on high rating.

### 14. Exceptions
Exceptions may change reporting workflow or evidence handling for privacy, law, emergency, or offline operation, but SHALL NOT permit a material confirmed error to be erased, silently ignored, or counted as correct.

### 15. Escalation
Confirmed or credible high-consequence error → Incident Management and Trustworthiness Review. Repeated known defect → Problem Management. Vulnerability/exposure pattern → AIVE. Material model/change issue → Change Enablement and recertification review. Evidence manipulation → Governance/Security/Certification escalation.

### 16. Interfaces
Safety Risk Management; Incident Management; Problem Management; Monitoring & Event Management; Change Enablement; Release; Deployment; Validation; Verification; Knowledge; Human Safety Communication; Certification; AIVE; Continual Improvement.

### 17. Records
AI Trustworthiness Profile; AI Error Registry; AI Error Report; AI Error Occurrence; AI Error Defect; evaluation run; scenario-suite version; rubric version; evaluator profile; rating calculation; Rating Change Event; Rating Explanation Record; appeals; remediation and revalidation record.

### 18. Review Cycle
Continuous event-driven recalculation for material triggers; periodic review frequency defined by domain and consequence class; evidence expiry enforced by Trustworthiness Scoring Policy.

### 19. Continual Improvement
Confirmed and recurring errors update Known Hazard Catalogue, evaluation suites, rubrics, scoring policy, model remediation, safety controls, standards, AIVE where applicable, and Technology Evolution Review.

### 20. Failure Conditions
The practice is failing when reported errors can disappear without disposition; ratings can be raised primarily by self-assessment; raw report volume directly changes rating; critical errors can be averaged away; ratings transfer across materially changed versions without evidence; evaluator correlation is hidden; stale evidence supports current high ratings; or a rating is treated as authority or safety certification.

---



## AI error cross-practice lifecycle

`AIErrorReport` → validation → `ConfirmedAIError` → update Trustworthiness Profile → if high consequence: Incident Management → if recurring/root-cause defect: Problem Management → if vulnerability/exposure class: AIVE → remediation → independent revalidation → rating recalculation → Knowledge Management → Continual Improvement → evaluation-suite/scoring-policy/standard update where required.

A confirmed error can be an error only, a safety incident, a Known Safety Error, an AIVE exposure, or several of these simultaneously. Not every error is an incident or vulnerability.

