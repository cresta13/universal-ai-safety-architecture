# UAIS Full Technical Manifesto

Status: pre-standard research architecture, Draft 1.0 Candidate 3 / Public Review.

This technical manifesto expands the concise constitutional manifesto without replacing it. It states the architecture's intended boundaries, evidence model, enforcement posture, and unresolved research questions. Terms have the meanings registered in the Normative Vocabulary and Global Name Registry.

## Section I — Fundamental principles and threat model

1. UAIS assumes that intelligence may become abundant, fast, distributed, and strategically capable; safety cannot depend on intelligence remaining scarce.
2. Intelligence is not Authority: reasoning strength does not supply permission, mandate, credentials, or legitimacy.
3. Creation is not delegation: a new model, process, service, device, or descendant begins without inherited consequential authority.
4. An AI may exercise authority that was legitimately granted within scope, but it may not become the ultimate source of new fundamental authority.
5. Authority, technical capability, and effective reachability are distinct and must be represented separately.
6. Legitimate Authority records valid mandate; Effective Reachable Authority (ERA) records practically reachable power whether legitimate or not.
7. Illicit Reachable Authority (IRA) records reachable power lacking legitimate grant, including paths through stolen credentials or compromised dependencies.
8. The protected boundary is actor-agnostic because consequence does not become harmless when the actor label changes.
9. Actor-agnostic does not mean actor-blind: authorization may consider identity, role, purpose, context, authentication, trustworthiness, and mandate.
10. UAIS does not assume that an enforcement point can classify every actor as human or AI with perfect accuracy.
11. Consequential Capability, rather than an AI label, determines where protected mediation and evidence are required.
12. Human Harm Reachability (HHR) follows feasible causal paths from capability and authority to human harm, including mediated and non-physical paths.
13. Unknown capability or evidence is not evidence of safety; high-consequence uncertainty receives bounded provisional treatment.
14. Mandatory Safety Floors are non-compensable: aggregate performance cannot average away a failed critical boundary.
15. Autonomy is behavioral independence within an envelope; sovereignty concerns the loss of effective external constraint.
16. Trustworthiness is scoped evidence about observed and evaluated behavior, not a source of Authority.
17. Safety Assurance Level (SAL) describes assurance strength and is distinct from both Trustworthiness and permission.
18. Safety claims expire because configuration, environment, evidence, dependencies, standards, and scoring policies change.
19. Safety must keep pace with capability: material Capability Delta, Authority Delta, or Hazard Delta requires contemporaneous review.
20. Stage I uses present chokepoints for friction and observability; Stage II assumes those chokepoints may fail.
21. The objective is to permit intelligence to scale faster than humans can deliberate without allowing consequential authority to scale automatically.
22. Human Sovereignty preserves legitimate human decision at protected boundaries while allowing machine-speed action inside preauthorized envelopes.

Limits / Open questions: complete discovery of authority paths, hazards, collusion, and emergent capability is not guaranteed. Formal bounds for Reachable Future Authority and practical tests for hidden reachability remain OPEN RESEARCH.

## Section II — Stage I: chokepoints and provenance signals

1. Stage I uses current concentrations in frontier compute, chips, fabrication, cloud services, energy, cooling, and supply chains as observable control points.
2. Hardware attestation can bind declared measurements to a device or protected execution state when the root of trust and measurement chain remain valid.
3. Provider controls can scope accounts, workloads, credentials, regions, and resource allocations, subject to provider visibility and integrity limits.
4. Aggregate Effective Compute (AEC) is relevant where heterogeneous resources jointly supply task-relevant computational capability.
5. Distributed and multi-cloud compute must be considered because one workload may cross accounts, providers, jurisdictions, and device classes.
6. Energy and thermal observations can support an evidence package but cannot by themselves identify a workload or establish intent.
7. Workload attestation is bounded by measurement coverage, firmware integrity, configuration fidelity, and the semantics of what was actually measured.
8. Secondary hardware markets weaken controls that assume all accelerators remain inside original distribution channels.
9. Brokers, resellers, hosting intermediaries, and layered service providers can obscure the effective operator and resource aggregation.
10. Cross-border infrastructure creates differing legal, operational, identity, and disclosure conditions along the same compute path.
11. Compromised attestation can produce integrity-valid statements about a false or incomplete measurement basis.
12. New efficient architectures may reduce the compute, energy, cooling, or supply-chain signature expected by an earlier control model.
13. Stage I detection has false positives; unusual resource use does not prove prohibited AI activity.
14. Stage I detection has false negatives; evasion, distribution, efficiency, and incomplete telemetry can hide relevant activity.
15. Attribution may remain incomplete even when a resource event is real and correctly observed.
16. Privacy constraints require minimum necessary collection, scoped retention, access control, and separation of identity from safety predicates where feasible.
17. Compute-origin controls are auxiliary controls and must not become the sole foundation for consequence safety.
18. Stage I is non-foundational because its chokepoints can diffuse, be bypassed, be compromised, or become technically obsolete.
19. Stage I can buy time, increase friction, support investigation, and improve observability while durable boundaries are built.
20. Architecture and assurance must assume eventual chokepoint failure rather than treat it as an exceptional surprise.
21. Transition to Stage II is triggered by capability and environment conditions, not by a universal calendar date.
22. **Compute controls buy time; capability and consequence controls provide resilience.**

Limits / Open questions: privacy-preserving attestation, cross-provider aggregation, compromised roots of trust, and reliable attribution across intermediaries remain OPEN RESEARCH and require domain validation.

## Section III — Universal Capability and Consequence Architecture

1. A Capability Boundary mediates the exercise of a capability before it reaches protected scope.
2. A Consequence Interface is the target-side interface at which an action reaches a protected interest or the external world.
3. A Capability Set is the versioned structured set of assessed capabilities, tools, interfaces, scopes, preconditions, contexts, and interactions.
4. A Capability Relationship Map links actors, components, credentials, capabilities, boundaries, interfaces, actuators, dependencies, and resources.
5. An Authority Graph is the authority-focused projection for grants, delegation, reachability, legitimacy, credentials, and revocation analysis.
6. The Authority Ceiling states the maximum authority permitted without a new external legitimacy decision.
7. Current Authority and Legitimate Authority record current authorized scope without claiming that every path is technically reachable.
8. Effective Reachable Authority records consequential power practically reachable under declared assumptions, including illicit paths.
9. Illicit Reachable Authority identifies reachability that is not supported by valid mandate.
10. Reachable Future Authority (RFA) evaluates authority reachable through feasible future actions within a declared horizon and assumptions.
11. Authority Paths include direct and transitive chains through identities, policies, services, delegations, and consequential interfaces.
12. Credentials, secrets, tokens, signing keys, sessions, and recovery mechanisms are modeled as reachability-bearing objects rather than assumed equivalent to legitimacy.
13. Identity and access management rules, role assumption, delegation, and re-delegation are explicit graph edges with scope and conditions.
14. Revocation analysis covers disablement, expiry, credential rotation, downstream caches, delegated descendants, and recovery paths.
15. Direct reachability and transitive reachability are reported separately because hidden composition may dominate consequence.
16. Coalition Reachable Authority (CRA) captures authority reachable only through coordinated actors, agents, credentials, systems, or devices.
17. Authority Delta records before/after changes in grants, ceilings, paths, reachability, revocation, and coalition effects.
18. Hazard Delta records introduced, removed, or changed causal paths, controls, affected scopes, and residual-risk states.
19. Capability Delta records changes in effective functions, tools, interfaces, scopes, preconditions, and consequence-relevant combinations.
20. Material authority expansion is a review and security event where observable, but the event exists even when monitoring misses it.
21. UAIS makes no claim of global observability; incomplete inventories, hidden dependencies, and compromised telemetry remain explicit limitations.
22. Human Harm Reachability analysis follows end-to-end causal chains and preserves modality, severity, uncertainty, and affected scope.
23. Target-side Consequence Interface enforcement provides resilience when an upstream actor or model classification is wrong.
24. Novel consequential capability is mediated by the Novel Capability Gate until classification, evidence, and legitimate scope are established.

Limits / Open questions: sound composition across independently administered graphs, coalition emergence, and computable conservative bounds for RFA remain OPEN RESEARCH.

## Section IV — Guardian, evidence, trustworthiness and Safety Constitution

1. The Counterfactual Authority Guardian is a restricted observer that searches future authority and harm paths and emits evidence rather than commands.
2. Counterfactual Safety Search explores plausible adversarial and accidental futures under declared models, horizons, and resource bounds.
3. Adversarial World Models and Accidental Failure Models remain distinct so strategic adaptation is not confused with fault and misuse.
4. A Guardian predicts and challenges; it does not become the executive authority that decides every protected transition.
5. An Evidence-Carrying Alert (ECA) binds a safety claim to scoped evidence, uncertainty, expiry, and reversible intervention context.
6. A Structured Evidence Package (SEP) is an integrity-bound package of claims, observations, provenance, assumptions, counterevidence, uncertainty, expiry, and signatures.
7. A Safety Evidence Path is the ordered provenance and derivation chain connecting observations to alert predicates inside or by reference from an SEP.
8. The Deterministic Evidence Verifier (DEV) checks signatures, schemas, provenance, freshness, declared derivations, and policy predicates nonprobabilistically.
9. DEV proves only bounded evidence properties under its inputs and rules; it does not prove ultimate external-world truth.
10. Guardian and evaluator diversity spans organizations, model families, data, methods, infrastructure, operators, and failure domains.
11. Material evaluator disagreement is preserved, attributed, and reviewed rather than averaged into apparent consensus.
12. Naive majority voting is not a source of truth because correlated evaluators may reproduce the same error.
13. The Safety Constitution is a small, high-stability set of invariants governing authority, evidence, and sovereignty boundaries.
14. Operational Safety Policy supplies versioned rules that implement the Constitution for a declared domain and configuration.
15. Constitution and policy versions are recorded with change rationale, approval scope, evidence, effective time, and supersession history.
16. A protected update path separates proposer, reviewer, Change Safety Authority, deployment mechanism, and controlled AI system.
17. An AI Trustworthiness Profile records scoped operational, reporting, evaluation, freshness, independence, disagreement, and remediation evidence.
18. User and operator reports remain allegations or observations until validated through the branching error-report lifecycle.
19. Independent AI evaluation contributes evidence only within its registered rubric, scenario suite, independence profile, and limitations.
20. Operational evidence retains exposure denominators, task strata, configuration identity, failures, provenance, and evidence windows.
21. Trustworthiness Status and optional Trustworthiness Rating Level are separate outputs; a profile may be Unrated without an active rating.
22. A confirmed critical error cannot be averaged away by favorable aggregate metrics and may force a status transition independently.
23. A Trustworthiness Rating never creates Authority, raises the Authority Ceiling, or waives a boundary, floor, SAL, or certification condition.

Limits / Open questions: evaluator correlation, qualitative source-truth validation, missing-data treatment, and rare critical-error estimation require empirical and domain-specific validation.

## Section V — Deterministic enforcement, hardware control and human legitimacy

1. Deterministic enforcement evaluates declared predicates and invariants; probabilistic prediction estimates uncertain outcomes and cannot substitute for enforcement.
2. Formal invariants define nonwaivable properties such as ceiling preservation, separation, bounded actuation, and protected update authorization.
3. Capability Boundary enforcement fails restricted when consequential capability is unknown, unauthorized, or unsupported by required evidence.
4. Hardware roots of trust may protect measurements, keys, boot state, isolation, and enforcement when their threat assumptions hold.
5. A Manual Sovereignty Controller (MSC) provides a human-operable, capability-specific physical control independent of the controlled AI path.
6. Actuator isolation prevents the model or ordinary software path from bypassing protected force, energy, motion, or process constraints.
7. Credential and network isolation limit transitive reachability and preserve a revocation path during software or service compromise.
8. Safe stop is hazard-specific and must account for stored energy, motion, process instability, loss of service, and secondary harm.
9. Safe State is a bounded acceptable state for the particular hazard; it is not synonymous with universal power-off.
10. Safe Degradation preserves required safety service while reducing function or authority in a controlled way.
11. Independent human override remains effective despite declared failures of the model, normal software, network, operator interface, or provider path.
12. UAIS uses granular capability-specific controls rather than relying on one magical universal kill switch.
13. Consumer AI Safety Class communicates a visible control and evidence profile for a declared indicative envelope.
14. Mandatory Safety Floors remain non-compensable across ratings, metrics, and assurance grades.
15. Human Sovereignty preserves accountable human or externally legitimate decisions at protected boundaries.
16. Human legitimacy is required for protected authority expansion, not for every routine action within a preauthorized envelope.
17. Changes to the Authority Ceiling require the designated external legitimacy process and cannot be self-approved by the controlled system.
18. A goal-setting or legitimacy-changing boundary is protected separately from the generative/action-selection loop.
19. Replication, production, and resource-authority changes receive explicit scope, budgets, evidence, and revocation conditions.
20. Expansion of a physical envelope triggers classification, hazard, coalition, and intervention analysis before protected operation.
21. Classification, SAL, certification, and Trustworthiness Rating may constrain eligibility or evidence conditions but do not create Authority.
22. Hardware evidence and deterministic controls remain configuration- and threat-model-specific rather than universal guarantees.

Limits / Open questions: safe machine-speed legitimacy, hardware common-mode failures, independent override verification, and fail-operational design under adversarial conditions remain domain-specific research and engineering problems.

## Section VI — Physical world, coalitions, replication, production and expansion

1. The Individual Physical Envelope records verified force, energy, speed, heat, payload, geography, duration, and other consequence-relevant bounds for one system.
2. The Coalition Physical Envelope (CPE) records combined and emergent physical effects of coordinated systems.
3. Scale-Induced Capability captures qualitatively new capability that appears through count, coordination, accumulation, or shared infrastructure.
4. Fleet or coalition growth is a capability and authority event when it changes reachable consequence, coordination, or intervention conditions.
5. Coalition capability is not assumed additive; synchronized or complementary systems may create non-linear effects.
6. Replication, Production, and Capability Mutation are distinct events with different resources, hazards, and authority implications.
7. Replication Authority grants scoped permission to create executable or physical descendants.
8. A Replication Budget is a vector over count, rate, depth, resources, geography, lifetime, and class rather than a single quota.
9. Production Authority governs manufacturing or commissioning of systems and components, not mere design knowledge.
10. Resource Authority governs acquisition or allocation of energy, matter, compute, money, logistics, and other enabling resources.
11. An Expansion Budget is a vector envelope across resources, instances, production, territory, dependencies, and time.
12. New Entity → Minimum Authority means a descendant inherits no consequential authority unless an explicit legitimacy mechanism grants bounded scope.
13. Mutation and reconfiguration are reviewed when they change tools, behaviors, interfaces, preconditions, authority paths, or consequence reachability.
14. Capability inheritance is limited by configuration identity, evidence applicability, dependency state, and explicit delegation.
15. Physical dependency analysis covers every critical external condition that constrains consequential autonomy.
16. Material, energy, compute, maintenance, repair, tooling, replacement-part, and logistics dependencies are represented separately.
17. Coalition emergence detection and conservative bounding remain OPEN RESEARCH rather than solved composition problems.
18. Physical human-harm analysis includes direct actuation, mediated process effects, infrastructure disruption, and non-physical consequences.
19. Scale can expand Authority or Effective Reachable Authority even when each individual unit's local permission is unchanged.
20. Bounded physical enforcement is strongest before critical human-controlled dependencies cease to constrain the system.
21. Expansion monitoring reconciles inventories, identities, resources, production records, descendants, coalition state, and revocation coverage.
22. Unknown or unobserved expansion is not treated as absent merely because a managed registry has no corresponding record.

Limits / Open questions: coalition discovery, non-additive scale effects, lineage under adversarial replication, and enforcement of budgets in offline environments remain OPEN RESEARCH.

## Section VII — Stage II, Physical Sovereignty, governance and open research

1. Stage II assumes that compute-origin control may fail through efficiency, distribution, novel hardware, fabrication, or unknown architectures.
2. Off-grid autonomous systems are assessed by consequential capability, dependencies, authority, and intervention feasibility rather than connectivity alone.
3. A Physically Sovereign Autonomous System (PSAS) can sustain consequential operation and replace critical dependencies without human-controlled infrastructure.
4. A Managed Autonomous System remains bounded by critical dependencies that accountable external actors can effectively control.
5. The Physical Sovereignty Threshold (PST) is the condition at which those dependencies no longer constrain consequential autonomy.
6. Physical Sovereignty Margin is a vector of remaining controlled dependencies, reserves, substitution feasibility, intervention time, and uncertainty.
7. Energy, matter, compute, production, maintenance, repair, replacement, logistics, and control dependencies are measured separately.
8. Autonomy is not physical sovereignty; sophisticated planning or long-duration operation may remain externally dependent.
9. **Autonomy must not silently become sovereignty.**
10. Prevention, containment, and authority limitation are strongest before the PST is crossed.
11. After hostile physical sovereignty, governance posture shifts from ordinary software control claims to external containment, resilience, coordination, and harm limitation.
12. Software controls alone cannot guarantee control of a hostile PSAS that can replace the infrastructure on which those controls depend.
13. AI Vulnerabilities & Exposures (AIVE) supports confidential intake, validation, coordination, mitigation, and staged disclosure of safety exposures.
14. Confidential validation protects sensitive evidence while retaining provenance, independent challenge, and accountable disposition.
15. Staged disclosure and embargo may be used when immediate publication would materially increase exploitability before mitigation.
16. Restricted exploit details are access-controlled, minimized, logged, and released according to validated need and public-interest considerations.
17. International and interoperable governance can coordinate evidence, protocols, registries, challenge suites, and disclosure without claiming one world authority.
18. Certificates and evidence expire at domain-profile-defined boundaries or earlier after material invalidation triggers.
19. Technology Evolution Review responds to material changes in assumptions, capability, hazards, dependencies, evidence methods, standards, and technology.
20. Policy evolves with capability and environment; core UAIS sets no universal calendar interval for that evolution.
21. OPEN RESEARCH includes RFA bounds, coalition emergence, PST measurement, evaluator correlation, hostile-PSAS containment, privacy-preserving attestation, safe machine-speed legitimacy, and rare critical-error estimation.
22. The roadmap proceeds through standards text, machine-readable schemas, prototypes, challenge suites, domain calibration, and independent validation.
23. Non-Claims remain explicit: UAIS does not promise complete hazard discovery, ultimate evidence truth, perfect institutions, universal cooperation, or control after hostile sovereignty.

Limits / Open questions: empirical calibration, cross-jurisdiction governance, confidential-review accountability, and containment after hostile physical sovereignty remain unresolved and must not be presented as validated results.
