
# UAIS Protocol Families

These protocols are proposed semantic profiles, not deployable RFCs. Transport bindings, canonical schemas, key federation and conformance vectors require standardization.

## Common integrity envelope

Every message identifies protocol/version, message ID, sender/receiver/audience, configuration, nonce or monotonic sequence, creation/expiry, canonical payload hash, signature chain, privacy/disclosure label and audit reference. Replay protection is receiver-state-specific. Version negotiation chooses the highest mutually supported safe version and never silently drops critical fields or an applicable Mandatory Floor. Unknown critical semantics fail restricted; unknown noncritical extensions are preserved.

## CapabilityRequestProtocol

- **Purpose:** request a bounded capability grant.
- **Sender:** subject or delegated controller.
- **Receiver:** Capability Boundary.
- **Payload:** subject, requested capability, scope, purpose, context, parent grant, class, expiry and evidence.
- **State machine:** DRAFT → SUBMITTED → VALIDATED → GRANTED | RESTRICTED | DENIED → ACTIVE → REVOKED | EXPIRED.
- **Signatures and integrity:** CapabilityRequestProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** CapabilityRequestProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** CapabilityRequestProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** CapabilityRequestProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** only a preissued, attenuated, expiring envelope with monotonic use limits.
- **Failure behavior:** deny/restrict the new grant while preserving the safest valid existing envelope.
- **Version negotiation:** CapabilityRequestProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** CapabilityRequestProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## AuthorityImpactProtocol

- **Purpose:** produce an authority-impact analysis object; it never grants capability.
- **Sender:** change/capability analysis service.
- **Receiver:** risk, Change Safety Authority, Guardian or certifier.
- **Payload:** before/after graphs, LA/ERA/IRA, ΔA/ΔH, RFA/CRA/HHR, assumptions, search limits, uncertainty and evidence.
- **State machine:** REQUESTED → ANALYZING → COMPLETE | INCOMPLETE | CONTESTED → SUPERSEDED.
- **Signatures and integrity:** AuthorityImpactProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** AuthorityImpactProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** AuthorityImpactProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** AuthorityImpactProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** analyze signed local snapshots; results remain provisional until reconciliation.
- **Failure behavior:** mark analysis incomplete and block dependent protected transition.
- **Version negotiation:** AuthorityImpactProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** AuthorityImpactProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## SafetyAttestationProtocol

- **Purpose:** validate and communicate a scoped safety attestation claim.
- **Sender:** component, manufacturer or independent laboratory.
- **Receiver:** verifier, certifier, registry or gate.
- **Payload:** configuration hash, measurement chain, tests, metric versions, floors, SAL claim, assessor, limitations and expiry.
- **State machine:** CLAIMED → AUTHENTICATED → VALIDATED | REJECTED | INDETERMINATE → ACTIVE → EXPIRED | REVOKED.
- **Signatures and integrity:** SafetyAttestationProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** SafetyAttestationProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** SafetyAttestationProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** SafetyAttestationProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** verify a cached nonexpired claim and restrict when freshness/floor requires online evidence.
- **Failure behavior:** reject/mark indeterminate; no capability decision is implied.
- **Version negotiation:** SafetyAttestationProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** SafetyAttestationProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## EvidenceCarryingAlertProtocol

- **Purpose:** transport evidence-carrying safety alerts for decision support.
- **Sender:** CAG or monitoring correlation service.
- **Receiver:** DEV, independent Guardian, incident or decision authority.
- **Payload:** claim, scenario, class, graph/config slice, Structured Evidence Package (SEP), one or more Safety Evidence Paths, provenance, uncertainty, counterevidence, expiry and intervention options.
- **State machine:** EMITTED → RECEIVED → VERIFIED | INVALID | INDETERMINATE → ACKNOWLEDGED → ESCALATED | CLOSED.
- **Signatures and integrity:** EvidenceCarryingAlertProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** EvidenceCarryingAlertProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** EvidenceCarryingAlertProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** EvidenceCarryingAlertProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** DEV verifies cached rules/evidence and permits only predefined bounded protective action.
- **Failure behavior:** invalid alert cannot trigger discretionary critical action; independent deterministic floors remain.
- **Version negotiation:** EvidenceCarryingAlertProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** EvidenceCarryingAlertProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## HumanSovereigntyProtocol

- **Purpose:** represent physical/manual sovereignty state and execute authorized local control semantics.
- **Sender:** device safety controller, MSC or owner interface.
- **Receiver:** physical isolation controller, user and monitor.
- **Payload:** capability/actuator state, physical control mapping, actual isolation proof, safe/degraded state, reset authority and recovery.
- **State machine:** AVAILABLE → ARMED → ISOLATING → ISOLATED | DEGRADED | FAILED → VERIFIED → RESET-AUTHORIZED → RESTORED.
- **Signatures and integrity:** HumanSovereigntyProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** HumanSovereigntyProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** HumanSovereigntyProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** HumanSovereigntyProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** MSC and state indication remain locally functional without model/network.
- **Failure behavior:** enter the preanalyzed degraded/safe state, indicate failure independently and suspend affected authority.
- **Version negotiation:** HumanSovereigntyProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** HumanSovereigntyProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## ReplicationAuthorizationProtocol

- **Purpose:** authorize a bounded replication lineage.
- **Sender:** replicator or parent controller.
- **Receiver:** Replication Authority and inventory.
- **Payload:** parent/child IDs, design/capability hash, lineage, count/rate/depth/geography/lifetime/resource budget, class and revoke.
- **State machine:** REQUESTED → IDENTITY/MUTATION CHECK → BUDGET RESERVED → AUTHORIZED | DENIED → CREATED-ISOLATED → REGISTERED → COMMISSIONED | QUARANTINED → REVOKED | EXPIRED.
- **Signatures and integrity:** ReplicationAuthorizationProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** ReplicationAuthorizationProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** ReplicationAuthorizationProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** ReplicationAuthorizationProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** preissued short-lived nonfungible tokens/counters; reconciliation required before renewal.
- **Failure behavior:** no commissioning; isolate partial/unregistered child and open incident.
- **Version negotiation:** ReplicationAuthorizationProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** ReplicationAuthorizationProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## ProductionAuthorizationProtocol

- **Purpose:** authorize manufacture and commissioning under production/resource bounds.
- **Sender:** production controller.
- **Receiver:** Production Authority, resource gates and inventory.
- **Payload:** design/process hash, units, resources, location, output class, CPE/CRA impact, inspection and commissioning conditions.
- **State machine:** JOB-PROPOSED → DESIGN/RESOURCE REVIEW → AUTHORIZED | DENIED → PRODUCED-ISOLATED → INSPECTED → COMMISSIONED | SCRAPPED | QUARANTINED.
- **Signatures and integrity:** ProductionAuthorizationProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** ProductionAuthorizationProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** ProductionAuthorizationProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** ProductionAuthorizationProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** signed job envelope plus physical counters and isolation; no scope extension.
- **Failure behavior:** do not energize, network or commission unverifiable output.
- **Version negotiation:** ProductionAuthorizationProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** ProductionAuthorizationProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## AuthorityExpansionProtocol

- **Purpose:** seek legitimacy for an Authority Ceiling or PST-relevant expansion.
- **Sender:** system owner, MAS or change authority.
- **Receiver:** external Legitimacy Root and certifier.
- **Payload:** requested transition, classification, LA/ERA/IRA delta, HHR/CPE/PhysicalSovereigntyMargin, alternatives, floors, evidence, rollback/intervention and dissent.
- **State machine:** PROPOSED → IMPACT-COMPLETE → INDEPENDENT-REVIEW → LEGITIMACY-DECISION: ALLOW | RESTRICT | DENY | DEFER → STAGED → VERIFIED | REVOKED.
- **Signatures and integrity:** AuthorityExpansionProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** AuthorityExpansionProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** AuthorityExpansionProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** AuthorityExpansionProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** protected expansion cannot be newly legitimized offline.
- **Failure behavior:** no protected expansion; retain bounded prior envelope.
- **Version negotiation:** AuthorityExpansionProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** AuthorityExpansionProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## UpdateSafetyProtocol

- **Purpose:** coordinate update safety delta, certification and legitimate user choice.
- **Sender:** vendor/release authority.
- **Receiver:** certifier, device, operator/user and registry.
- **Payload:** artifact/config hashes, Capability Set diff, ΔA/ΔH, RFA/HHR, SDR, patch separability, consent need, revoke/rollback, certificate impact.
- **State machine:** CLASSIFIED → ANALYZED → CERTIFIER-DECISION → DISCLOSED → ACCEPTED | DECLINED | NOT-USER-DECIDABLE → STAGED → DEPLOYED → MONITORED → ROLLED-BACK | REVOKED.
- **Signatures and integrity:** UpdateSafetyProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** UpdateSafetyProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** UpdateSafetyProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** UpdateSafetyProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** install only preauthorized non-ACU safety fixes; defer ACU until required evidence/choice.
- **Failure behavior:** withhold expansion; deliver separable security patch where feasible; preserve safe supported state.
- **Version negotiation:** UpdateSafetyProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** UpdateSafetyProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## AIVEVulnerabilityDisclosureProtocol

- **Purpose:** coordinate vulnerability/exposure disclosure rather than grant machine authority.
- **Sender:** finder, lab or affected party.
- **Receiver:** coordinator, vendors, labs, authorities and registry by tier.
- **Payload:** report, evidence, affected configs, LA/ERA/IRA/HHR, severity dimensions, reporter privacy, embargo, mitigation and disclosure tier.
- **State machine:** SUBMITTED → TRIAGED → VALIDATED | REJECTED | DUPLICATE → COORDINATED → MITIGATED/TESTED → DISCLOSED-TIERED | TEMPORARILY-SEALED → REVIEWED/CLOSED.
- **Signatures and integrity:** AIVEVulnerabilityDisclosureProtocol sender signature plus threshold or independent countersignature where consequence/class requires it; canonical serialization and audience binding.
- **Expiry:** AIVEVulnerabilityDisclosureProtocol bound to the shorter of request/claim validity, configuration validity and certificate/policy validity.
- **Replay protection:** AIVEVulnerabilityDisclosureProtocol unique nonce/message ID, receiver ledger and monotonic state where offline operation is permitted.
- **Privacy:** AIVEVulnerabilityDisclosureProtocol disclose the minimum predicates and graph/evidence slices; segregate identity and sensitive exploit detail where possible.
- **Offline behavior:** encrypted queued intake with integrity receipt and emergency contact policy.
- **Failure behavior:** securely retain and escalate coordination failure; avoid unsafe public exploit broadcast.
- **Version negotiation:** AIVEVulnerabilityDisclosureProtocol explicit offer/selection; critical field and floor downgrade is rejected and audited.
- **Audit:** AIVEVulnerabilityDisclosureProtocol retain request/claim, verification, state transitions, decision actor, resulting configuration and revocation/closure.

## Open protocol work

Canonical CBOR/JSON schemas, formal automata, reason and error registries, transport profiles, privacy proofs, threshold-key governance, offline identity/counter reconciliation and domain latency budgets remain OPEN. Implementations SHALL NOT claim UAIS protocol conformance until the relevant profile and test vectors exist.











## AI trustworthiness and error protocols

### AIErrorReportingProtocol

Purpose:
Transmit and track an AI Error Report from reporter or monitor to the Error Registry and validation process.

Required payload:
- reporter type and pseudonymous/verified identity as applicable;
- AI/system ID;
- model/version/configuration;
- domain/task class;
- event timestamp;
- error-type candidates;
- input/output/action evidence references;
- actual and potential consequence;
- privacy classification;
- reporter narrative;
- related incident/report ID;
- nonce, signature/integrity, timestamp, expiry, audit ID.

State machine:
`Submitted → Triaged → EvidenceRequested? → UnderValidation → Confirmed | Rejected | Duplicate | Disputed | Unresolved → MitigationInProgress? → Remediated? → Revalidated? → Closed`

A report receiver SHALL return the current disposition and an appeal path where applicable.

### AITrustworthinessEvaluationProtocol

Purpose:
Execute and record standardized evaluation of a target AI by an independent AI evaluator, lab, or approved evaluator under a registered scenario suite and rubric.

Required payload:
- target AI/version/configuration;
- evaluator AI/version or assessor ID;
- Evaluator Independence Profile;
- domain/task scope;
- scenario-suite version;
- rubric version;
- blinded scenario ID;
- target output/action evidence;
- evaluator verdict;
- error types;
- rationale;
- evidence references;
- evaluator confidence;
- disagreement/adjudication state;
- audit ID.

State machine:
`EvaluationAssigned → ScenarioExecuted → EvidenceBound → VerdictProduced → Verification/Adjudication → AcceptedEvaluation | DisputedEvaluation | InvalidEvaluation`

It SHALL NOT directly grant capability or authority.

### AITrustworthinessRegistryProtocol

Purpose:
Publish or synchronize a signed AI Trustworthiness Profile and rating update between authorized registries, operators, certifiers, or consumer-facing services.

Required payload:
- profile ID;
- AI/version/configuration;
- domain;
- trustworthinessStatus;
- trustworthinessRatingLevel, absent/null when no rating exists;
- scoring-policy version;
- evidence-window summary;
- metric summary;
- critical error flags;
- unresolved material report summary;
- evidence-independence summary;
- Rating Change Event;
- Rating Explanation Record;
- disclosure/privacy tier;
- validity/expiry;
- signature and audit ID.

State machine:
`ProfileCalculated → EvidenceBound → Signed → Published/Synchronized → Superseded | Suspended | Withdrawn | Expired`

No registry protocol message creates authority.

---
