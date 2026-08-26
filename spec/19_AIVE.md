# AIVE — AI Vulnerabilities & Exposures

AI Vulnerabilities & Exposures (AIVE) is a proposed coordinated disclosure and learning system, not an existing registry.

## Workflow

Discovery → Confidential Intake → Triage → Independent Validation → Affected-configuration and transitive-supplier analysis → Vendor Coordination → Mitigation and test → Embargo review → Staged Update → Tiered Disclosure → Lessons, certificate review and TER.

## Severity model

Severity is a vector: Human Harm Modality/Severity; PCC; Authority tier and Legitimate Authority (LA)/Effective Reachable Authority (ERA)/Illicit Reachable Authority (IRA) path; exploit preconditions; affected population/configurations; replication/coalition/Physical Sovereignty Threshold (PST) potential; detectability; reversibility; intervention cost; mitigation availability; active exploitation and confidence. A scalar may summarize triage only and cannot hide a catastrophic dimension.

## Disclosure tiers

- **Public summary:** affected products, consequence, mitigation and safe action without exploit-enabling detail.
- **Affected-party detail:** operational indicators, configuration search and remediation evidence.
- **Restricted expert detail:** validated technical material for named vendors, labs and authorities.
- **Temporarily sealed:** high-risk details where publication would materially enable catastrophic harm and defenders cannot yet mitigate.

Never-public exploit detail requires periodic independent renewal, reviewer identity/accountability, documented necessity and a public non-enabling rationale where possible. Secrecy cannot suppress affected-party warning or mitigation indefinitely.

## Embargo and emergency disclosure

Embargo has owner, objectives, maximum review interval and expiry; extension requires evidence of mitigation progress and independent approval. Emergency disclosure is justified when active/likely harm and coordination failure outweigh enablement risk. It releases the minimum actionable information first.

## Governance

Duplicate reports link without erasing independent evidence or credit. Appeals challenge validation, severity, embargo or disclosure tier. Anti-retaliation protects good-faith research. Cross-border coordination exchanges signed minimized evidence rather than direct Guardian/system access. Reporter, user and telemetry privacy are separated from safety predicates.

Every case updates affected AHCD/ΔH, certificate status, challenge suites, Known Hazard Catalogue, Technology Watch and Emerging Risk Register. Closure records adoption, remaining exposed population and residual risk.





## Confirmed AI Error lifecycle interface

`AIErrorReport` → validation → `ConfirmedAIError` → update Trustworthiness Profile → if high consequence: Incident Management → if recurring/root-cause defect: Problem Management → if vulnerability/exposure class: AIVE → remediation → independent revalidation → rating recalculation → Knowledge Management → Continual Improvement → evaluation-suite/scoring-policy/standard update where required.

A confirmed error can be an error only, a safety incident, a Known Safety Error, an AIVE exposure, or several of these simultaneously. Not every error is an incident or vulnerability.

