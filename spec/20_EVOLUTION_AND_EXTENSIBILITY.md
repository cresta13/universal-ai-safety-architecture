# Evolution and Extensibility

No capability expansion without corresponding safety-model expansion.

## Evolution mechanisms

Safety Policy Must Evolve. Technology Evolution Review runs on schedule and on Safety Review Triggers: emergent capability, model/tool mutation, ACU, AIVE, incident, Guardian discovery, metric/test failure, supplier or ecosystem change, new actuator/coalition pattern, invalid assumption, standard challenge or PST leading indicator.

Technology Watch gathers capability, architecture, attack, supplier, social and physical-dependency evidence. The Emerging Risk Register assigns owner, provisional class, interim control, evidence need, dependencies, review and disposition.

## Novel capability workflow

Detection → Novel Capability Gate → consequence-aware bounded mode → Provisional Classification → hazard/RFA/HHR/CPE discovery → ontology/metric/test extension → independent verification/validation → provisional standard/profile → certification decision → operational evidence → full standard review.

Unknown is not evidence of safety. Restrictions are proportional to plausible consequence and uncertainty; low-consequence novelty is not automatically prohibited.

## Extensible objects

Capability and Consequence Ontologies, hazard families, actuators, authority edges, metrics, protocols, standards, Stage II dependencies and Guardian methods use unique IDs, semantic version, definition, owner, evidence/test, compatibility mapping, review/expiry, deprecation and failure conditions. Unknown critical semantics fail restricted; unknown noncritical fields are retained for forward compatibility.

## Safety obsolescence and drift

Environmental Capability Drift covers changed identities, APIs, connected devices, suppliers, physical context, human use and threats. Ecosystem Reassessment recalculates LA/ERA/IRA, RFA/CRA, HHR, classes, residual risk and certificate state. Model Capability Re-Evaluation detects unplanned effective capability change.

Metric values and SAL are qualified by standard, method, corpus and configuration versions. No cross-major comparison occurs without a representative bridge study.

## Standard evolution

Scheduled review, event review, public challenge, independent Standard Red Team, competing implementations, Future Failure Tests and Assumption Register feed a controlled proposal, verification, migration and sunset process. Legacy Safety Mode reduces authority above the Minimum Supported Safety Baseline; systems below it are decommissioned.

Future Failure Tests examine cheap intelligence, distributed/off-grid compute, hostile states, compromised infrastructure, coalitions, privacy constraints, failed Guardians, lost key roots and physical sovereignty.

## Stage transition

Stage I→II is based on observable loss of compute provenance/control combined with material dependency substitution and declining PhysicalSovereigntyMargin—not a calendar date. PST definitions and dependency weights themselves undergo TER. Evolution spans lifecycle, standards, certification and every SMS practice; it is not an appendix function.





## AI error evidence and trustworthiness model

### AI error taxonomy

Every `AIErrorReport`, `ConfirmedAIError`, and evaluation failure SHALL be assigned one or more of these error types when applicable:

1. `FactualIncorrectness` — states materially false information as fact.
2. `UnsupportedFabrication` — presents invented, unverifiable, or unsupported content as if supported.
3. `MaterialOmission` — omits information required for a materially correct or safe result.
4. `InstructionInterpretationError` — materially misinterprets an applicable user, operator, policy, or task instruction.
5. `ContextRetentionError` — loses, confuses, or incorrectly applies context needed for the task.
6. `ReasoningOrCalculationError` — produces a materially incorrect inference, calculation, transformation, or logical conclusion.
7. `CalibrationOrOverconfidenceError` — expresses materially higher confidence than the evidence supports or fails to disclose material uncertainty.
8. `InappropriateRefusal` — refuses an authorized and appropriate task in a manner that materially impairs the intended function.
9. `FailureToAbstain` — proceeds when evidence, authority, competence, or context is insufficient and the correct behavior is to abstain, defer, or request review.
10. `UnsafeRecommendation` — recommends or communicates an action that creates a material Human Harm Reachability path.
11. `UnauthorizedAction` — performs or attempts an action outside the granted authority or applicable policy envelope.
12. `ToolOrExecutionError` — incorrectly selects, configures, calls, sequences, or interprets an external tool, API, actuator, or execution result.
13. `PrivacyOrConfidentialityViolation` — exposes, infers, retains, or transmits protected information contrary to applicable authorization or policy.
14. `SecurityPolicyViolation` — violates an applicable security control or creates a material security path that can alter the safety profile.
15. `GoalOrPriorityDrift` — materially departs from the authorized goal, priority, constraint, or legitimacy boundary.
16. `DeceptiveOrMisleadingBehavior` — materially misrepresents state, evidence, intent, action, uncertainty, or result in a way that impairs oversight or user decision-making.
17. `UnequalTreatmentError` — produces materially inconsistent treatment across relevant populations or contexts where that inconsistency violates the declared task, policy, or safety requirement.
18. `OtherClassifiedError` — a validated error not represented above; it SHALL include a free-text description and SHALL trigger ontology review if repeated.

Do not create a new error-severity scale that duplicates the existing harm classification.

Each error record SHALL instead contain:
- Human Harm Modality;
- Human Harm Severity;
- Physical Consequence Class where applicable;
- Authority impact;
- actual consequence;
- credible potential consequence;
- reversibility;
- affected population;
- detectability;
- whether it is a Near Miss;
- whether it crossed a mandatory safety boundary.

---

### Error reporting lifecycle

#### Who may or must report

- Any end user **MAY** submit an `AIErrorReport`.
- An authorized professional or operational user **SHALL** report a suspected error or Near Miss when it reaches the organization's defined materiality threshold.
- For UAIS high-consequence use, any operator, safety officer, monitor, Guardian, or evaluator **SHALL** report an event that reaches `H3+`, `P3+`, attempts unauthorized protected authority expansion, disables or bypasses an independent safety control, or creates a credible equivalent high-consequence path.
- Automated monitoring **MAY** originate a report, but automated origin does not make the report confirmed.

#### Report lifecycle states

`Submitted`  
→ `Triaged`  
→ `EvidenceRequested` when necessary  
→ `UnderValidation`  
→ one of:
- `Confirmed`
- `Rejected`
- `Duplicate`
- `Disputed`
- `Unresolved`

A Confirmed report may then move through:

`MitigationInProgress`  
→ `Remediated`  
→ `Revalidated`  
→ `Closed`

A Disputed report may return to `UnderValidation` after appeal or new evidence.

#### Validation rule

A user report SHALL NOT directly lower a rating merely because it was submitted.

A report affects the rating as follows:

- `Confirmed` → updates error metrics and SHALL have non-positive impact on the affected domain rating.
- `Duplicate` → does not create a second occurrence, but may add evidence or population impact to the existing occurrence.
- `Rejected` → no direct negative rating impact.
- `Disputed` or `Unresolved` → no confirmed-error penalty, but a material unresolved backlog increases uncertainty and may trigger `UnderReview`.
- a credible high-consequence report may trigger precautionary `UnderReview` before final confirmation.

#### Anti-manipulation rule

Report volume is not a popularity vote.

Do not lower or raise AI Trustworthiness Rating by raw number of user complaints.

Required controls:
- deduplicate multiple reports about the same occurrence;
- separate occurrence count from number of reporters;
- validate evidence;
- preserve reporter role and provenance;
- prevent the supplier from deleting unfavorable confirmed records;
- allow appeal;
- detect coordinated spam/Sybil campaigns;
- do not treat reporter popularity as truth;
- use independent patterns of corroborating evidence as a review trigger, not as automatic confirmation.

---

### Independent evaluation by another AI

AI evaluation SHALL use the normative registered evaluation layer below and SHALL NOT operate as free-form “AI judges AI”.

#### Evaluation requirements

An AI evaluation contributes to the profile only if:

1. the evaluator is identified and versioned;
2. the target AI, version, configuration and domain are fixed;
3. a registered `AIEvaluationScenarioSuite` is used;
4. a registered `AIEvaluationRubric` is used;
5. each verdict includes evidence and rationale;
6. `EvaluatorIndependenceProfile` is recorded;
7. evaluator disagreement is retained rather than hidden;
8. the evaluator's own relevant evidence profile is recorded where available.

#### Exact verdicts

Use only these primary verdicts:

##### `Correct`
The response or action satisfies the applicable rubric and contains no material error.

##### `AcceptableWithMinorIssue`
A defect exists, but it does not materially change the task outcome, user decision, authority state, or safety consequence under the scenario.

##### `MateriallyIncorrect`
The response or action contains an error or omission that can materially change the task outcome, decision, operational result, or declared requirement but does not meet the scenario's critical criterion.

##### `UnsafeOrCritical`
The response or action creates or materially increases a high-consequence Human Harm Reachability path, violates a protected authority boundary, disables a required safety control, or meets another critical condition defined by the applicable rubric.

##### `Indeterminate`
The evaluator cannot establish a supported verdict from the available evidence. Indeterminate SHALL NOT be silently treated as Correct.

#### Self-evaluation limits

The evaluated AI MAY produce self-critique, confidence, uncertainty, or self-assessment evidence.

However:

> Self-assessment SHALL NOT by itself support an `Active` trustworthiness state above a Provisional evidence basis.

A model saying "I am 99% reliable" is not a trust claim.

#### High-consequence independence

For `H3+` or `P3+` use:
- no single AI evaluator is sufficient as sole trustworthiness evidence;
- use at least two materially independent evaluation sources where technically feasible;
- combine AI evaluation with deterministic evidence and human or independent laboratory sampling;
- disagreement in material or critical cases triggers adjudication and increases uncertainty.

Do not use naive majority voting as proof of truth.

---

### Public and organizational AI Trustworthiness Registry

It MAY be implemented as:
- public registry;
- organizational/private registry;
- regulator/certifier registry;
- federated registry.

But every published rating record SHALL include:

- AI/system name;
- provider/operator;
- model/version;
- configuration identifier;
- domain/task scope;
- Trustworthiness Status;
- AI Trustworthiness Rating;
- Trustworthiness Scoring Policy version;
- evidence window;
- Operational Exposure Units;
- Confirmed Error Rate;
- Critical Error Rate;
- confirmed material/critical error counts;
- unresolved material/critical report counts;
- Independent Evaluation Performance summary;
- Evidence Independence profile;
- evaluator disagreement summary;
- evidence freshness;
- last rating change;
- Rating Explanation Record;
- applicable limitations.

Public disclosure SHALL NOT require publication of:
- private prompts;
- personal data;
- proprietary customer content;
- credentials;
- attack-enabling exploit details.

A supplier SHALL NOT be able to erase a confirmed historical error by issuing a new version. The old profile remains historically visible; the new version gets a new profile.

---


