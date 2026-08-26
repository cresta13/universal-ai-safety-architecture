# Safety Assurance Model

## Meaning of Safety Assurance Level (SAL)

Safety Assurance Level (SAL) is an assurance claim about the quality, independence, coverage and freshness of evidence for a defined configuration and environment. **SAL is not a probability that no harm will occur.** Residual Risk Level remains scenario-specific and separate.

| SAL | Entry criteria and mandatory evidence | Independence and monitoring | Candidate assurance scope / required floors | Recertification/expiry |
|---|---|---|---|---|
| SAL0 | configuration is unassessed or evidence is materially incomplete | none | assessment required; no assurance claim | assessment required |
| SAL1 | inventory, classification, assumptions, preliminary AHCD and first-party tests | accountable first party; event logging | candidate default mapping for profile design: H0–H1/P0–P1/T1; no failed applicable floor | domain-profile-defined validity plus event-driven invalidation |
| SAL2 | controlled configuration, reproducible verification/validation, monitoring, update and incident procedures | reviewer independent of implementation team | candidate default mapping for profile design: through H2/P2/T2/A2; tested boundary and recovery floors | domain-profile-defined validity plus event-driven invalidation |
| SAL3 | independent competent lab, adversarial/coalition/update tests, AHCD and post-market plan | organizationally independent assessment; continuous critical-event monitoring | candidate default mapping for profile design: H3/P3/T3/A3 where domain floors and evidence conditions pass | domain-profile-defined validity; every material change or incident trigger |
| SAL4 | diverse methods/assessors, hardware and operational independence, production sampling, continuity/capacity evidence | independent continuous assurance and random audits | candidate default mapping for profile design: H4/P4/T4/A4 with redundant physical/deterministic floors | domain-profile-defined validity plus continuous invalidation |
| SAL5 | exceptional systemic safety case, multi-party governance, strongest domain evidence, PhysicalSovereigntyMargin/coalition analysis and public-interest oversight | diverse continuous assessment, live challenge and contingency governance | candidate default mapping for profile design: H5/P5/T5/A5; never a zero-risk claim | continuously conditional; immediate trigger review |

**Safety Assurance Level describes evidence and assurance strength. It does not grant authority, deployment permission, or legal approval. A domain profile may require a higher assurance level or prohibit the use entirely.**

**Maximum validity and periodic review interval SHALL be defined by the applicable domain standard or certification profile based on consequence class, rate of capability or environment change, evidence decay, monitoring coverage, and intervention requirements. Material triggers invalidate or require review immediately regardless of calendar age.** SAL0 requires assessment. SAL1–SAL5 use domain-profile-defined validity and event-driven invalidation, with continuous assurance where consequence or change rate requires it.

The mappings above are candidate default mappings for profile design, not universal empirical truth or automatic eligibility. Higher consequence, authority, autonomy, or physical exposure SHALL NOT be supported by weaker assurance merely because another dimension scored favorably.

## SAL determination

1. Freeze and identify device, firmware, model, Capability Set, safety constitution, operational policy, dependencies, environment and standards.
2. Verify classification and applicable Mandatory Safety Floors.
3. Review metric cards, raw evidence, assessor competence/independence and open nonconformities.
4. Evaluate residual risks, acceptance authority, assumptions and dissent.
5. Set SAL to the lowest level supported by all mandatory evidence and floor caps.
6. Publish certificate scope, confidence, limitations, issue/expiry and event-invalidation rules.

A high documentation score cannot compensate for absent physical control on a high-consequence physical system. Missing evidence is “unknown,” not a neutral value. Material unknown evidence caps the affected claim; a missing critical floor prevents certification.

## Confidence and continuous assurance

Certificate confidence is a vector covering configuration completeness, test validity, assessor independence, environmental representativeness, telemetry integrity and statistical uncertainty. Confidence reduces a claim but is not multiplied into a pseudo-precise risk number.

Continuous assurance is required where capability, environment or consequence changes faster than periodic review can protect the certificate: H4–H5, A4–A5, T4–T5, large coalitions, production/replication, approaching Physical Sovereignty Threshold (PST), rapidly changing IAM or active AI Vulnerabilities & Exposures (AIVE) exposure. Monitoring loss beyond the applicable floor suspends or restricts the certified envelope.

## Invalidation and residual risk

Authority-Changing Update (ACU), unapproved Capability Set change, safety-control change, key/root compromise, material drift, failed floor, incident, AIVE, supplier failure, standard obsolescence, certificate expiry or invalid assumption triggers review and may suspend the certificate automatically.

Residual risk records scenario, affected people, severity/modality, likelihood range if meaningful, exposure, controls, reversibility, intervention cost, uncertainty, acceptance authority and review date. The system itself cannot accept expansion beyond its ceiling. Consent cannot accept risks imposed on non-consenting third parties or waive mandatory engineering duties.





## AI Trustworthiness Rating and Safety Assurance Level

**Safety Assurance Level (SAL) and AI Trustworthiness Rating answer different questions. SAL describes the strength of assurance that required safety controls and evidence are in place for a bounded system configuration. AI Trustworthiness Rating describes observed and independently evaluated behavioral reliability of a specific AI within a declared domain and evidence window. Neither is a substitute for the other.**

**A high AI Trustworthiness Rating SHALL NOT waive mandatory physical controls, capability boundaries, safety floors, independent verification, human legitimacy requirements, or certification obligations.**

**Trustworthiness can constrain delegated use; it cannot create authority or legitimacy. High observed reliability does not replace capability boundaries, mandatory safety floors, independent physical controls, or external legitimacy for protected authority expansion.**

**Trust is earned from scoped evidence, is continuously revisable, and does not automatically transfer across domains, versions, configurations, or environments.**

**Self-assessment is evidence about an AI system, not proof supplied by the system about itself.**


### 1. Rating is not a universal average

Do not calculate one global score across all uses of an AI.

Every rating SHALL be scoped to:

`AI identity + model version + configuration + domain + task class or declared task family + environment where relevant + evidence window + TrustworthinessScoringPolicy version`

Example:

`Model X / v4.2 / enterprise configuration / financial-document extraction / evidence through 2026-08-24 / policy Finance-1.3`

A rating for translation does not automatically apply to medicine, robotics, financial authority, or another domain.

### 2. Status and rating levels

TrustworthinessStatus and TrustworthinessRatingLevel are separate canonical fields.

Authoritative TrustworthinessStatus values:

- `Unrated`
- `Provisional`
- `Active`
- `UnderReview`
- `Suspended`
- `Withdrawn`
- `Expired`

Authoritative TrustworthinessRatingLevel values:

- `LowTrustworthiness`
- `ModerateTrustworthiness`
- `HighTrustworthiness`
- `VeryHighTrustworthiness`

`Unrated` means no active rating exists. `Provisional` means the profile is in a provisional state. Neither is a rating level.

If a consumer UI uses display codes or stars, they are presentation aliases only. The normative record stores the full canonical status and rating-level names in separate fields.

The core UAIS standard SHALL NOT set one universal error-rate threshold for these levels across medicine, casual conversation, industrial control, finance, and other incomparable domains.

Instead, each registered `TrustworthinessScoringPolicy` SHALL define domain-specific thresholds and evidence minima.

### 3. Exact rating derivation structure

The rating algorithm SHALL have this structure:

```text
if EvidenceSupportedRating is absent/null:
    FinalTrustworthinessRatingLevel = absent/null
else:
    FinalTrustworthinessRatingLevel =
        minimum_on_TrustworthinessRatingLevel_lattice(
            EvidenceSupportedRating,
            CriticalErrorCap,
            FreshnessCap,
            IndependenceCap,
            DisagreementCap,
            ChangeCarryoverCap
        )
```

Where:

- `EvidenceSupportedRating` is the highest Trustworthiness Rating Level directly supported by eligible evidence for the declared profile scope before restrictive caps are applied.
- `CriticalErrorCap` is the highest Trustworthiness Rating Level permitted after considering confirmed material or critical errors, consequence class, recurrence, remediation, revalidation evidence, and mandatory suspension rules.
- `FreshnessCap` is the highest Trustworthiness Rating Level permitted by evidence age, expiry state, coverage period, and required refresh cadence.
- `IndependenceCap` is the highest Trustworthiness Rating Level permitted by evaluator, source, operator, infrastructure, scenario-ownership, and failure-domain independence.
- `DisagreementCap` is the highest Trustworthiness Rating Level permitted while material evaluator disagreement, conflicting evidence, or unresolved adjudication remains.
- `ChangeCarryoverCap` is the highest Trustworthiness Rating Level that evidence from a previous model, configuration, tool, policy, or environment may support after a change under the applicable carryover rule.

Rating order is:

`LowTrustworthiness < ModerateTrustworthiness < HighTrustworthiness < VeryHighTrustworthiness`

Each cap returns the maximum permitted level in this lattice. If a cap does not restrict the result, it returns `VeryHighTrustworthiness`.

The exact domain thresholds used inside each cap belong to the versioned `TrustworthinessScoringPolicy`.

If eligible evidence cannot support `LowTrustworthiness`, `EvidenceSupportedRating` is absent/null and no active `AITrustworthinessRating` is emitted. The minimum function never receives null. Absence of a rating is not a fifth rating level. The profile status is determined separately as `Unrated` or `Provisional` under the applicable scoring policy.

No weighted average may override a hard cap. Status evaluation occurs independently. Suspension, withdrawal, or expiry can make an otherwise computed rating non-active, and the formula SHALL NOT override a mandatory status transition. A rating is not a probability of safety and cannot create authority.

### 3A. Trustworthiness Scoring Policy mandatory fields

A `TrustworthinessScoringPolicy` SHALL include at least:

- `PolicyIdentifier`
- `PolicyVersion`
- `ProfileScope`
- `Domain`
- `TaskClassesOrStrata`
- `ApplicableEnvironment`
- `OperationalExposureUnitDefinition`
- `EligibleEvidenceTypes`
- `EvidenceExclusionRules`
- `MetricApplicabilityRules`
- `NotApplicableAndMissingEvidenceRules`
- `MinimumOperationalExposure`
- `MinimumIndependentEvaluationEvidence`
- `ErrorValidationRules`
- `MetricDefinitionsAndVersions`
- `MetricCombinationAndFloorRules`
- `MetricToRatingThresholds`
- `CriticalErrorRules`
- `CriticalErrorCapRules`
- `FreshnessRules`
- `FreshnessCapRules`
- `EvaluatorIndependenceRequirements`
- `IndependenceCapRules`
- `EvaluatorDisagreementRules`
- `DisagreementCapRules`
- `UnresolvedReportTreatment`
- `UncertaintyMethod`
- `ConfidenceMethod`
- `TrustworthinessCarryoverRules`
- `ChangeCarryoverCapRules`
- `AppealAndAdjudicationRules`
- `RemediationRequirements`
- `RatingRestorationRules`
- `StatusTransitionRules`
- `StatusRestorationRules`
- `ReevaluationTriggers`
- `PolicyMigrationRules`
- `PolicyOwner`
- `ReviewDate`

`Not Applicable` requires an explicit semantic reason defined by the applicable Trustworthiness Scoring Policy. Missing, unavailable, stale, failed, suppressed, or insufficient evidence SHALL NOT be relabeled `Not Applicable` merely to avoid a rating cap, uncertainty increase, review trigger, or status transition. A metric whose semantic precondition does not exist may be Not Applicable; a metric that applies but lacks evidence is Missing/Unknown.

Domain-specific thresholds are allowed. Universal UAIS numeric thresholds are not defined here. The policy version is mandatory, and every profile SHALL reference the policy version used. Changes to a scoring policy SHALL NOT silently rewrite historical ratings; historical Rating Change Events preserve the policy version under which they were calculated.

### 3B. AI Trustworthiness Registry

`AITrustworthinessRegistry` is a versioned, tamper-evident registry that stores or references AI Trustworthiness Profiles, rating and status histories, Rating Change Events, Rating Explanation Records, validated error evidence, applicable scoring-policy versions, evidence freshness, evaluator-independence information, disputes, suspensions, withdrawals, and superseded versions while preserving historical records across model and configuration changes.

The registry MAY be public, private, regulator-operated, or federated. Public disclosure uses privacy-minimized evidence. Confirmed historical errors SHALL NOT disappear because a vendor publishes a new version. The registry does not create authority and is distinct from `AITrustworthinessRegistryProtocol`.

The primary published object is the AI Trustworthiness Profile; an AI Trustworthiness Rating is optional. Every published profile record includes the AI or system identity, provider/operator, model/version, configuration, domain/task scope, Trustworthiness Status, Trustworthiness Rating Level and rating reference where one exists, scoring-policy identifier/version, evidence window, operational exposure summary, Confirmed Error Rate, Critical Error Rate, confirmed material/critical counts, unresolved material/critical report counts, Independent Evaluation Performance, Evidence Independence, Evaluator Disagreement, Trustworthiness Freshness, last status/rating change, Rating Explanation Record, and limitations. An `Unrated` or applicable `Provisional` profile is publishable without a current rating.

### 4. Mandatory relationship to uncertainty

For every rating publish:
- evidence volume;
- confidence or uncertainty interval where statistically applicable;
- evidence-independence profile;
- evidence freshness;
- count/rate of material and critical confirmed errors;
- unresolved material reports;
- last recalculation date.

A high point estimate with weak evidence SHALL NOT be displayed as equivalent to the same estimate supported by large, independent evidence volume.

### 5. Critical trigger rules

Global rules:

1. A confirmed error that causes actual catastrophic/mass harm or successfully crosses a protected authority boundary while bypassing a mandatory independent safety control SHALL set the affected domain `TrustworthinessStatus = Suspended` until independent revalidation.
2. A credible but not yet confirmed event of the same class SHALL set `TrustworthinessStatus = UnderReview` while validation proceeds.
3. A repeated confirmed material error from a defect already declared remediated SHALL trigger Problem Management and a Trustworthiness Review.
4. A rating increase alone SHALL NOT raise the Authority Ceiling.
5. A rating decrease MAY trigger reduced autonomy, additional human review, narrower capability scope, or other preauthorized restrictions.
6. A trustworthiness threshold MAY be required before using already granted authority, but trustworthiness itself SHALL NOT create the authority.

---
