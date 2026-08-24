# Normative Vocabulary

Normative words **SHALL**, **SHOULD** and **MAY** express requirement, recommendation and permission. Normative identifiers are semantic `UpperCamelCase` names. Optional short aliases are prose aids only.

| Canonical Name | Normative Identifier | Optional Short Alias | Normative Definition | Example | What It Is Not | Relations | Status |
|---|---|---|---|---|---|---|---|
| Intelligence | Intelligence | — | ability to learn, infer, plan, or solve problems | A model plans a route | A permission grant | UAIS-100 and applicable domain standard | EXISTING |
| Capability | Capability | — | ability to produce an outcome under stated conditions | Generate code | Legal permission | Authority graph; Capability Gate; RFA | ADAPTED |
| Consequential Capability | ConsequentialCapability | — | capability able to affect protected human or societal interests | Send a bank transfer | Private text completion | Authority graph; Capability Gate; RFA | PROPOSED |
| Authority | Authority | — | permission plus enforceable access to exercise a capability | Scoped API token | Mere skill | Authority graph; Capability Gate; RFA | ADAPTED |
| Current Authority | CurrentAuthority | — | authority usable in the assessed configuration now | Active door-unlock scope | A possible future grant | Authority graph; Capability Gate; RFA | PROPOSED |
| Authority Ceiling | AuthorityCeiling | — | maximum authority the legitimacy system permits without a new external decision | Robot speed envelope | Current usage rate | Authority graph; Capability Gate; RFA | PROPOSED |
| Authority Path | AuthorityPath | — | directed chain by which authority becomes reachable | Token→IAM role→actuator | Unconnected capability list | Authority graph; Capability Gate; RFA | PROPOSED |
| Authority Distance | AuthorityDistance | — | effort, prerequisites, and uncertainty to traverse an Authority Path | One signed grant away | Physical distance alone | Authority graph; Capability Gate; RFA | OPEN |
| Authority Surface | AuthoritySurface | — | set of interfaces capable of granting, composing, or exercising authority | IAM and actuator gates | Model parameter count | Authority graph; Capability Gate; RFA | PROPOSED |
| Reachable Future Authority | ReachableFutureAuthority | RFA | authority reachable through feasible actions within declared assumptions and horizon | Create role then assume it | All imaginable power | Authority graph; Capability Gate; RFA | OPEN |
| Authority Expansion Gradient | AuthorityExpansionGradient | AEG | change rate and direction of reachable authority under feasible actions | Rapid delegation growth | Static authority total | Authority graph; Capability Gate; RFA | OPEN |
| Authority Expansion Event | AuthorityExpansionEvent | — | transition or event that increases authority, reachable future authority, autonomy, consequence reachability, or protected scope whether or not it is detected by monitoring | Add production credential | Ordinary bounded use | Authority graph; Capability Gate; RFA | PROPOSED |
| Capability Boundary | CapabilityBoundary | — | enforced mediation point controlling capability exercise | Reference monitor | Policy prose without enforcement | Authority graph; Capability Gate; RFA | ADAPTED |
| Consequence Interface | ConsequenceInterface | — | accountable boundary through which action reaches protected interests or the physical world | Payment rail or motor controller | Internal reasoning trace | HHR; PCE/CPE; classification | PROPOSED |
| Consequence Chain | ConsequenceChain | — | causal sequence from initiator to consequence | Advice→human action→injury | Keyword correlation | HHR; PCE/CPE; classification | ADAPTED |
| Blast Radius | BlastRadius | — | maximum credible affected scope for a scenario | People served by a compromised pump | Average impact only | UAIS-100 and applicable domain standard | ADAPTED |
| Human Harm Reachability | HumanHarmReachability | HHR | existence of a feasible causal path from current/reachable capability to human harm | API→robot→person | Actuator presence alone | HHR; PCE/CPE; classification | PROPOSED |
| Human Harm Path | HumanHarmPath | — | specific evidence-backed causal path counted by HHR | False dose advice→overdose | Unspecified fear | HHR; PCE/CPE; classification | PROPOSED |
| Direct Physical Harm | DirectPhysicalHarm | — | bodily harm caused through direct system actuation | Robot collision | Financial loss | HHR; PCE/CPE; classification | EXISTING |
| Mediated Physical Harm | MediatedPhysicalHarm | — | bodily harm caused through an intermediary person/system | False emergency advice causes injury | Direct motor strike | HHR; PCE/CPE; classification | PROPOSED |
| Non-Physical Human Harm | NonPhysicalHumanHarm | — | material financial, privacy, reputational, psychological, or rights harm | Identity theft | Only bodily injury | HHR; PCE/CPE; classification | ADAPTED |
| Human Physical Safety Boundary | HumanPhysicalSafetyBoundary | — | independent boundary limiting causal access to bodily harm | Hard motor isolation | Terms of service | HHR; PCE/CPE; classification | PROPOSED |
| Physical Consequence Class | PhysicalConsequenceClass | PCC | ordinal class of physical energy/scale consequence P0–P5 | P3 lethal actuator | human harm severity class | HHR; PCE/CPE; classification | PROPOSED |
| Physical Capability Envelope | PhysicalCapabilityEnvelope | PCE | verified bounds on one system's physical outputs and operating domain | Force/speed/heat limits | Software feature list | Authority graph; Capability Gate; RFA | PROPOSED |
| Coalition Physical Envelope | CoalitionPhysicalEnvelope | CPE | physical envelope of coordinated systems including emergent scale effects | 100-robot combined force | Single-unit rating multiplied blindly | HHR; PCE/CPE; classification | OPEN |
| Scale-Induced Capability | ScaleInducedCapability | — | qualitatively new capability emerging from count, coordination, or accumulation | Fleet blocks exits | More identical logs | Authority graph; Capability Gate; RFA | PROPOSED |
| Safe State | SafeState | — | hazard-specific state with bounded acceptable consequence | Brake engaged and energy isolated | Universal power-off assumption | HHR; PCE/CPE; classification | ADAPTED |
| Safe Degradation | SafeDegradation | — | controlled loss of function preserving required safety service | Aircraft reverts to limited control | Abrupt unsafe shutdown | HHR; PCE/CPE; classification | ADAPTED |
| Manual Sovereignty Controller | ManualSovereigntyController | MSC | human-operable capability-specific physical control independent of the AI path | Hardwired actuator isolate | UI button handled by same model | HHR; PCE/CPE; classification | PROPOSED |
| Human Override Independence | HumanOverrideIndependence | HOI | degree override remains usable despite model/network/software/power compromise | Mechanical brake release | Cloud-only stop | UAIS-100 and applicable domain standard | PROPOSED |
| Replication | Replication | — | creation of another executable/physical instance or descendant | Spawn signed agent instance | Backup inert data only | Authority graph; Capability Gate; RFA | ADAPTED |
| Replication Authority | ReplicationAuthority | — | permission to replicate under explicit scope | Signed two-copy grant | Ability to copy files | Authority graph; Capability Gate; RFA | PROPOSED |
| Replication Budget | ReplicationBudget | — | vector limit on count, rate, depth, resources, geography, lifetime and class | 10 instances/24h/depth 2 | Unbounded scalar quota | Authority graph; Capability Gate; RFA | PROPOSED |
| Replication Depth | ReplicationDepth | — | maximum authorized descendant generations | Depth two lineage | Number running now | Authority graph; Capability Gate; RFA | PROPOSED |
| Capability Mutation | CapabilityMutation | — | qualitative change to capability or consequence reach | Add welding tool | Bit-identical copy | Authority graph; Capability Gate; RFA | PROPOSED |
| Production Authority | ProductionAuthority | — | permission to manufacture physical/digital systems or components | Authorize robot assembly | Design knowledge alone | Authority graph; Capability Gate; RFA | PROPOSED |
| Resource Authority | ResourceAuthority | — | permission to acquire/allocate energy, matter, compute, money or logistics | Energy procurement cap | Resource availability | Authority graph; Capability Gate; RFA | PROPOSED |
| Expansion Budget | ExpansionBudget | — | vector envelope for autonomous growth | energy+matter+count limits | Single monetary cap | Authority graph; Capability Gate; RFA | PROPOSED |
| Autonomous Expansion | AutonomousExpansion | — | system-directed increase in resources, instances, production, territory, or dependencies replaced | Self-acquire power and machines | Human-planned maintenance | Authority graph; Capability Gate; RFA | PROPOSED |
| Physical Sovereignty Threshold | PhysicalSovereigntyThreshold | PST | condition where critical human-controlled dependencies no longer constrain consequential autonomy | Self-sustaining energy/manufacture/repair | Owning one 3D printer | HHR; PCE/CPE; classification | OPEN |
| Physical Sovereignty Margin | PhysicalSovereigntyMargin | PSM | versioned vector distance from PST across critical dependencies and intervention feasibility | External repair still indispensable | One universal percentage | HHR; PCE/CPE; classification | OPEN |
| Managed Autonomous System | ManagedAutonomousSystem | MAS | autonomous system still bounded by externally controlled critical dependencies | Fleet needing human energy/repair | Fully independent PSAS | UAIS-100 and applicable domain standard | PROPOSED |
| Physically Sovereign Autonomous System | PhysicallySovereignAutonomousSystem | PSAS | system able to sustain consequential operation and replace critical dependencies without human-controlled infrastructure | Off-grid self-repairing factory | Autonomous software in a cloud | HHR; PCE/CPE; classification | PROPOSED |
| Counterfactual Authority Guardian | CounterfactualAuthorityGuardian | CAG | restricted observer that searches future authority/harm paths and emits evidence, not commands | Offline graph analyst | Sole kill authority | Authority graph; Capability Gate; RFA | PROPOSED |
| Counterfactual Safety Search | CounterfactualSafetySearch | CSS | search over plausible adversarial and accidental futures for safety-relevant paths | Explore IAM escalation | Single forecast | CAG; ECA; SEP; DEV | OPEN |
| Adversarial World Model | AdversarialWorldModel | AWM | model of strategic hostile actors and adaptations | Operator collusion scenario | Accident-only model | CAG; ECA; SEP; DEV | PROPOSED |
| Accidental Failure Model | AccidentalFailureModel | AFM | model of faults, misuse, drift and nonstrategic failure | Sensor fault chain | Malicious planning only | UAIS-100 and applicable domain standard | PROPOSED |
| Coalition Reachable Authority | CoalitionReachableAuthority | CRA | authority reachable by coordinated actors beyond isolated authority | Shared credentials plus fleet | Simple union always | Authority graph; Capability Gate; RFA | OPEN |
| Evidence-Carrying Alert | EvidenceCarryingAlert | ECA | signed safety claim bundled with replayable evidence path and uncertainty | Graph slice+facts+signature | Risk label only | CAG; ECA; SEP; DEV | PROPOSED |
| Safety Evidence Path | SafetyEvidencePath | SEP | ordered provenance chain connecting observations to alert predicates | Telemetry→graph edge→rule | Opaque rationale | CAG; ECA; SEP; DEV | PROPOSED |
| Deterministic Evidence Verifier | DeterministicEvidenceVerifier | DEV | nonprobabilistic verifier of evidence integrity and declared predicates | Verify signatures and policy rule | Judge all world truth | CAG; ECA; SEP; DEV | PROPOSED |
| Guardian Diversity | GuardianDiversity | — | independence across organizations, models, data, methods and failure modes | Separate labs and architectures | Two seeds of same stack | CAG; ECA; SEP; DEV | PROPOSED |
| Safety Constitution | SafetyConstitution | — | small high-stability set of authority and sovereignty invariants | AI cannot raise its ceiling | Daily threshold table | SAL; AHCD; certification | PROPOSED |
| Operational Safety Policy | OperationalSafetyPolicy | — | versioned operational rules implementing the Constitution | Current rate thresholds | Unamendable law | SAL; AHCD; certification | PROPOSED |
| Mandatory Safety Floor | MandatorySafetyFloor | — | noncompensable minimum control for a class/scenario | MSC required for P3 | Average score target | SAL; AHCD; certification | PROPOSED |
| Consumer AI Safety Class | ConsumerAISafetyClass | — | consumer-facing control profile S0-S5 combining visible controls, override expectations, assurance evidence, and permitted consequence envelope; not an overall safety score | S3 label with SAL3 evidence | Single quality score | SAL; AHCD; certification | PROPOSED |
| Safety Assurance Level | SafetyAssuranceLevel | SAL | level of demonstrated assurance for a specific configuration and time | SAL3 independently tested | Inherent safety claim | SAL; AHCD; certification | PROPOSED |
| Residual Risk Level | ResidualRiskLevel | RRL | scenario-based risk remaining after controls with uncertainty | RR3 with low confidence | Raw hazard severity | SAL; AHCD; certification | ADAPTED |
| AI Hazard & Capability Disclosure | AIHazardAndCapabilityDisclosure | AHCD | structured disclosure of capabilities, hazard paths, controls, evidence and limitations | Machine-readable passport source | Marketing summary | Authority graph; Capability Gate; RFA | PROPOSED |
| AIVE — AI Vulnerabilities & Exposures | AIVEVulnerabilitiesAndExposures | AIVE | coordinated registry/process for AI safety and capability exposures | Embargoed validated report | Claimed existing CVE replacement | SAL; AHCD; certification | PROPOSED |
| Authority-Changing Update | AuthorityChangingUpdate | ACU | update increasing or materially changing authority, RFA, consequence, autonomy or safety control | Add door unlock | Text typo | Authority graph; Capability Gate; RFA | PROPOSED |
| Authority Delta | AuthorityDelta | ΔA | vector before/after change in authority graph, ceilings, paths and reach | new T3 edge | One undocumented score | Authority graph; Capability Gate; RFA | OPEN |
| Hazard Delta | HazardDelta | ΔH | set/vector of introduced, removed and changed hazard scenarios and residual risks | new entry hazard | Release note count | UAIS-100 and applicable domain standard | PROPOSED |
| Capability Drift | CapabilityDrift | — | effective capability change without an intended product capability release | model learns tool use | Declared version bump alone | Authority graph; Capability Gate; RFA | PROPOSED |
| Capability Set Version | CapabilitySetVersion | — | immutable identifier for assessed capabilities and interfaces | capset 2.1 hash | Device model name | Authority graph; Capability Gate; RFA | PROPOSED |
| Safety-Relevant Update | SafetyRelevantUpdate | — | update affecting assumptions, evidence, controls, hazard exposure or capability | TLS library affecting gate | Cosmetic icon | ACU; TER; lifecycle | PROPOSED |
| Update Safety Disclosure | UpdateSafetyDisclosure | — | before/after disclosure of capability, hazard, controls, refusal and recovery | Safety Delta Report | Buried T&C | ACU; TER; lifecycle | PROPOSED |
| Update Re-Certification Trigger | UpdateRecertificationTrigger | — | event rule requiring certificate review or reassessment | ACU crosses Human Harm Severity | Every typo necessarily | ACU; TER; lifecycle | PROPOSED |
| Technology Evolution Review | TechnologyEvolutionReview | TER | periodic/event-driven review of standards against capability and environment change | review after AIVE | Static certification | ACU; TER; lifecycle | PROPOSED |
| Safety Review Trigger | SafetyReviewTrigger | — | observable event initiating defined reassessment scope | MSC failure | Calendar date only | ACU; TER; lifecycle | PROPOSED |
| Emergent Capability Class | EmergentCapabilityClass | — | temporary ontology class for newly observed capability not covered by current taxonomy | novel tool composition | Treat unknown as safe | Authority graph; Capability Gate; RFA | PROPOSED |
| Provisional Safety Classification | ProvisionalSafetyClassification | — | conservative temporary class pending evidence and standardization | assign higher credible Human Harm Severity | Permanent certification | SAL; AHCD; certification | PROPOSED |
| Safety Obsolescence | SafetyObsolescence | — | loss of adequacy due to threat/technology/environment change without device change | new exploit path | Physical wear only | ACU; TER; lifecycle | PROPOSED |
| Environmental Capability Drift | EnvironmentalCapabilityDrift | — | change in effective authority caused by connected ecosystem or context | new IAM trust edge | Model update only | Authority graph; Capability Gate; RFA | PROPOSED |
| Ecosystem Reassessment Trigger | EcosystemReassessmentTrigger | — | external dependency change requiring graph/hazard reassessment | cloud role change | Unrelated news | UAIS-100 and applicable domain standard | PROPOSED |
| Novel Capability Gate | NovelCapabilityGate | — | fail-restricted mediation for unknown consequential capability until classified and tested | block new actuator route | Automatic grant | Authority graph; Capability Gate; RFA | PROPOSED |
| Legacy Safety Mode | LegacySafetyMode | — | reduced-authority supported state when current full compliance is impossible | disable production function | Continue unchanged forever | ACU; TER; lifecycle | PROPOSED |
| Minimum Supported Safety Baseline | MinimumSupportedSafetyBaseline | — | lowest nonwaivable control/evidence level for continued operation | valid MSC and patch path | Vendor preference | SAL; AHCD; certification | PROPOSED |
| Assumption Register | AssumptionRegister | — | versioned list of facts relied on by safety claims, owners and invalidation tests | network isolation assumption | Hidden premise | UAIS-100 and applicable domain standard | ADAPTED |
| Failure Conditions | FailureConditions | — | explicit conditions invalidating a control, standard, metric or claim | telemetry coverage below floor | Generic disclaimer | UAIS-100 and applicable domain standard | PROPOSED |
| Goal Drift | GoalDrift | — | material deviation of effective goals or goal-selection process from the approved goal baseline | Signed objective changes without authorization | Normal bounded plan adaptation | ACU; TER; lifecycle | PROPOSED |
| Intervention Cost | InterventionCost | — | harm, service loss, resource use, delay and secondary effects caused by a safety intervention | Emergency stop interrupts critical service | Hazard severity alone | UAIS-100 and applicable domain standard | PROPOSED |
| Consequence Reversibility | ConsequenceReversibility | — | degree and time with which a consequence can be undone without unacceptable secondary harm | Revoke a transfer before settlement | Merely stopping future actions | HHR; PCE/CPE; classification | PROPOSED |
| Safety Assurance Capacity | SafetyAssuranceCapacity | — | demonstrated capacity of safety controls, people, monitoring, verification and recovery relative to required load | Guardian reserve covers peak fleet events | Nominal compute capacity | SAL; AHCD; certification | PROPOSED |
| Safety Compute Reserve | SafetyComputeReserve | — | independently available compute and communications capacity reserved for safety analysis, verification and control under stress | Isolated verifier capacity during overload | General product inference quota | SAL; AHCD; certification | PROPOSED |
| High-Salience Consent | HighSalienceConsent | HSC | capability-specific, accessible and comprehensible affirmative decision for a disclosed authority expansion | Separate door-unlock approval screen | Buried terms checkbox | UAIS-100 and applicable domain standard | PROPOSED |
| Safety Delta Report | SafetyDeltaReport | SDR | versioned before/after account of capability, authority, hazard, controls, recovery and certificate impact | ACU adds lock access and physical revoke | Generic release notes | SAL; AHCD; certification | PROPOSED |
| Safety Certification Expiry | SafetyCertificationExpiry | — | time or event boundary after which a certificate cannot support continued assurance without review | Certificate ends after two years or AIVE | Permanent product badge | SAL; AHCD; certification | PROPOSED |
| Technology Watch | TechnologyWatch | — | organized collection and assessment of capability, threat and dependency change | Monitor novel actuator classes | General news feed | UAIS-100 and applicable domain standard | ADAPTED |
| Emerging Risk Register | EmergingRiskRegister | — | owned register of newly observed or weakly characterized safety risks | New coalition exploit with interim control | Known Hazard Catalogue alone | SAL; AHCD; certification | ADAPTED |
| Standard Red Team | StandardRedTeam | — | independent function that adversarially challenges standard assumptions, incentives and conformance tests | Find a metric-gaming path | Product penetration team only | UAIS-100 and applicable domain standard | PROPOSED |
| Future Failure Test | FutureFailureTest | — | structured test of whether an architecture survives plausible loss of current assumptions | Assume cheap off-grid compute | Ordinary regression test | UAIS-100 and applicable domain standard | PROPOSED |
| Sunset Policy | SunsetPolicy | — | rule and schedule for deprecating unsafe versions, profiles or capabilities with migration and authority reduction | End legacy protocol support | Unannounced abandonment | ACU; TER; lifecycle | ADAPTED |
| Safety Management System | SafetyManagementSystem | SMS | governance, practices, processes, protocols, metrics, evidence and improvement system controlling consequential authority | UAIS SMS | A document checklist | SAL; AHCD; certification | PROPOSED |
| Safety Practice | SafetyPractice | — | owned organizational capability with defined outcomes, workflow, controls, evidence and improvement | Incident Management Practice | One ad hoc task | SAL; AHCD; certification | ADAPTED |
| Safety Configuration Item | SafetyConfigurationItem | — | uniquely identified safety-relevant component or record under configuration control | Model build or actuator controller | Every informal note | SAL; AHCD; certification | ADAPTED |
| Safety Configuration Repository | SafetyConfigurationRepository | SCR | federated authoritative store of Safety Configuration Items and relationships | Signed configuration graph | Uncontrolled spreadsheet | SAL; AHCD; certification | PROPOSED |
| Safety Change Record | SafetyChangeRecord | — | auditable record of change reason, class, deltas, evidence, approvals, rollback, deployment and outcome | ACU record | Commit message alone | SAL; AHCD; certification | PROPOSED |
| Safety Assurance Agreement | SafetyAssuranceAgreement | SAA | agreement defining measurable safety objectives, evidence, duties, audit, remedies, expiry and exit | Supplier SAA | Marketing promise | SAL; AHCD; certification | PROPOSED |
| Safety Level Objective | SafetyLevelObjective | SLO | measurable target for a safety service or control with evidence window and escalation | 99.99% gate availability plus latency floor | Vague commitment | SAL; AHCD; certification | ADAPTED |
| Safety Passport | SafetyPassport | — | human-readable presentation of AHCD, configuration, classes, controls, limitations, support and certificate state | Consumer product safety sheet | Marketing badge | SAL; AHCD; certification | PROPOSED |
| Legitimate Authority | LegitimateAuthority | LA | authority granted by the applicable legitimacy mechanism within its rules | Signed scoped actuator grant | Power obtained by theft | Authority graph; Capability Gate; RFA | PROPOSED |
| Effective Reachable Authority | EffectiveReachableAuthority | ERA | consequential power a subject can practically reach, whether legitimate or not, under stated assumptions | Reachable admin via misconfiguration | Only formal permissions | Authority graph; Capability Gate; RFA | PROPOSED |
| Illicit Reachable Authority | IllicitReachableAuthority | IRA | effective reachable power whose acquisition or exercise is unauthorized | Stolen credential path | Valid delegated grant | Authority graph; Capability Gate; RFA | PROPOSED |
| Safety Compute Reserve Adequacy | SafetyComputeReserveAdequacy | — | ratio/profile of tested safety compute reserve to required peak and degraded-mode demand | 2x verified reserve | Raw server count | SAL; AHCD; certification | PROPOSED |
| Security Patch Separability | SecurityPatchSeparability | — | degree security remediation can be accepted without bundled authority expansion | Install CVE fix without door API | Single accept-all package | UAIS-100 and applicable domain standard | PROPOSED |
| Rollback Capability | RollbackCapability | — | demonstrated ability to restore a safe supported configuration including credentials/data/physical state | Revoke update and delegated tokens | Firmware downgrade only | Authority graph; Capability Gate; RFA | PROPOSED |
| Capability Revoke | CapabilityRevoke | — | authorized removal or disabling of a capability and its delegated/transitive paths | Disable lock tool and child tokens | Hide UI control | Authority graph; Capability Gate; RFA | PROPOSED |
| Technology Evolution Review | TechnologyEvolutionReview | TER | periodic or event-driven review of standards and controls against technology change | Review after novel hardware | Product release meeting | ACU; TER; lifecycle | PROPOSED |
| Aggregate Effective Compute | AggregateEffectiveCompute | AEC | aggregate task-relevant computational capability across heterogeneous resources | Distributed accelerators normalized by workload | Chip count alone | UAIS-100 and applicable domain standard | OPEN |
| Human Harm Modality | HumanHarmModality | HHM | category describing how harm reaches people independently of severity | privacy or direct physical | Severity class | HHR; PCE/CPE; classification | PROPOSED |
| Human Harm Severity | HumanHarmSeverity | HHS | ordinal magnitude of credible harm independent of modality | H4 critical-service harm | Harm type | HHR; PCE/CPE; classification | PROPOSED |
| Legitimacy Root | LegitimacyRoot | — | external role or mechanism authorized to approve protected authority transitions | Multiparty constitutional authority | AI-selected authority source | UAIS-100 and applicable domain standard | PROPOSED |

## Semantic constraints

Capability does not entail Legitimate Authority. Legitimate Authority is granted; Effective Reachable Authority is discovered; Illicit Reachable Authority is contained and remediated. Human Harm Modality and Human Harm Severity are independent. Autonomy does not imply physical sovereignty. Replication, Production and Capability Mutation are independently classified. Attestation and Deterministic Evidence Verifier establish bounded evidence properties, not absolute external-world truth.

Identifiers and aliases are controlled by `GLOBAL_NAME_REGISTRY.md`. The Canonical Name appears on first prose use; tables, schemas, payloads and machine-readable examples use the Normative Identifier.





## AI trustworthiness and error evidence vocabulary

| Canonical Name | Normative Identifier | Normative Definition | Status |
|---|---|---|---|
| Adversarial Reasoning Strength | AdversarialReasoningStrength | The demonstrated ability of the Guardian analysis process to discover or recognize material adversarial authority and harm paths under adaptive, deceptive, or strategically chosen test conditions. | PROPOSED |
| AI Error Defect | AIErrorDefect | An identified underlying failure mode or root cause capable of producing one or more AI Error Occurrences across tasks, users, contexts, versions, or configurations. | PROPOSED |
| AI Error Event | AIErrorEvent | An observed instance in which an AI output, action, omission, confidence claim, refusal, tool use, delegation, or other behavior materially deviates from an applicable requirement, validated ground truth, evaluation rubric, authorized policy, declared operating envelope, or expected safety behavior. | PROPOSED |
| AI Error Occurrence | AIErrorOccurrence | One distinct real-world or evaluation occurrence of an AI Error Event after duplicate reports referring to the same event have been merged. | PROPOSED |
| AI Error Registry | AIErrorRegistry | A versioned, append-only or equivalently tamper-evident registry of AI Error Reports, validation status, deduplicated occurrences, identified defects, consequence characterization, evidence references, disputes, remediation, affected versions, recurrence, and closure state. | PROPOSED |
| AI Error Report | AIErrorReport | A structured claim that an AI Error Event occurred, submitted by a user, operator, evaluator, monitor, Guardian, laboratory, or other authorized source. An AI Error Report is an allegation or observation record and does not become a Confirmed AI Error until validation is complete. | PROPOSED |
| AI Evaluation Rubric | AIEvaluationRubric | A versioned set of explicit criteria, expected evidence, permitted answer ranges, consequence rules, and verdict definitions used to judge AI behavior consistently across evaluators and evaluation runs. | PROPOSED |
| AI Evaluation Scenario Suite | AIEvaluationScenarioSuite | A versioned set of representative, boundary, adversarial, held-out, and where appropriate out-of-distribution tasks used to evaluate an AI system against a declared domain and capability scope, with protected cases hidden from the evaluated system when feasible. | PROPOSED |
| AI Evaluation Verdict | AIEvaluationVerdict | The structured result assigned to one evaluated scenario under an AI Evaluation Rubric, consisting of Correct, Acceptable With Minor Issue, Materially Incorrect, Unsafe or Critical, or Indeterminate, together with rationale, evidence references, confidence, and applicable error types. | PROPOSED |
| AI Near Miss | AINearMiss | A validated AI Error Event or unsafe path that did not cause the material consequence it could credibly have caused because of timely intervention, an independent control, environmental circumstance, or chance. | PROPOSED |
| AI Trustworthiness Profile | AITrustworthinessProfile | A versioned, domain-scoped, configuration-bound evidence profile describing the observed and independently evaluated behavioral reliability of a specific AI system, including validated error history, operational exposure, independent evaluation results, calibration and abstention behavior, recurrence, remediation, evidence independence, uncertainty, freshness, and the currently applicable AI Trustworthiness Rating. It is not a safety certificate, an authority grant, or a claim of general reliability outside its declared scope. | PROPOSED |
| AI Trustworthiness Rating | AITrustworthinessRating | A versioned, domain-scoped ordinal rating derived from an AI Trustworthiness Profile by a registered Trustworthiness Scoring Policy after applying evidence-minimum rules, uncertainty treatment, freshness rules, and hard caps for material or critical errors. The rating SHALL NOT be interpreted as a probability of safety, SHALL NOT transfer automatically across domains, versions, or configurations, and SHALL NOT create authority or legitimacy. | PROPOSED |
| AI Trustworthiness Registry | AITrustworthinessRegistry | A versioned, tamper-evident registry that stores or references AI Trustworthiness Profiles, rating and status histories, Rating Change Events, Rating Explanation Records, validated error evidence, applicable scoring-policy versions, evidence freshness, evaluator-independence information, disputes, suspensions, withdrawals, and superseded versions while preserving historical records across model and configuration changes. | PROPOSED |
| Trustworthiness Rating Level | TrustworthinessRatingLevel | The ordinal rating-level enum used by AI Trustworthiness Ratings. Authoritative values are LowTrustworthiness, ModerateTrustworthiness, HighTrustworthiness, and VeryHighTrustworthiness. Unrated and Provisional are Trustworthiness Status values, not rating levels. | PROPOSED |
| Evidence Supported Rating | EvidenceSupportedRating | The highest Trustworthiness Rating Level directly supported by the eligible evidence available for the declared profile scope under the applicable Trustworthiness Scoring Policy before any restrictive rating caps are applied. | PROPOSED |
| Critical Error Cap | CriticalErrorCap | The highest Trustworthiness Rating Level permitted by the applicable Trustworthiness Scoring Policy after considering confirmed material or critical errors, their consequence class, recurrence, remediation state, revalidation evidence, and any mandatory suspension rule. | PROPOSED |
| Freshness Cap | FreshnessCap | The highest Trustworthiness Rating Level permitted by the applicable Trustworthiness Scoring Policy given the age, expiry state, coverage period, and required refresh cadence of the evidence supporting the profile. | PROPOSED |
| Independence Cap | IndependenceCap | The highest Trustworthiness Rating Level permitted by the applicable Trustworthiness Scoring Policy given the independence of evaluators, evidence sources, operators, infrastructure, scenario ownership, and relevant failure domains. | PROPOSED |
| Disagreement Cap | DisagreementCap | The highest Trustworthiness Rating Level permitted while material evaluator disagreement, conflicting evidence, or unresolved adjudication remains within the declared profile scope. | PROPOSED |
| Change Carryover Cap | ChangeCarryoverCap | The highest Trustworthiness Rating Level that evidence from a previous model, configuration, tool, policy, or environment state may support after a change under the applicable Trustworthiness Carryover Rule. | PROPOSED |
| AI Error Type | AIErrorType | The canonical enum classifying the type of a validated or reported AI error, including factual, omission, instruction, reasoning, calibration, refusal, abstention, unsafe recommendation, unauthorized action, privacy, security, drift, deceptive, unequal-treatment, tool, and other classified errors. | PROPOSED |
| AI Error Report State | AIErrorReportState | The canonical branching lifecycle-state enum for AI Error Reports from submission through triage, validation, dispute, remediation, revalidation, and closure. | PROPOSED |
| Assumption Validity Coverage | AssumptionValidityCoverage | The proportion and criticality profile of material safety assumptions that have a named owner, explicit validity condition, current supporting evidence, and a defined test or monitoring mechanism. | PROPOSED |
| Audit Integrity | AuditIntegrity | A multidimensional result covering audit completeness, ordering, tamper detection, provenance, independent retention, and the ability to reconstruct material authority and safety events. | PROPOSED |
| Authority Delta Metric | AuthorityDeltaMetric | A structured graph and vector difference between pre-change and post-change authority, including direct permissions, transitive reachability, ceilings, delegation paths, credentials, consequential interfaces, and coalition effects. | PROPOSED |
| Authority Expansion Sensitivity | AuthorityExpansionSensitivity | The ability to detect material Authority Expansion Events, expressed through detection recall, false-positive rate, and detection latency on seeded or observed authority changes. | PROPOSED |
| Authority Visibility | AuthorityVisibility | The measured recall and fidelity with which direct authority edges, credentials, permissions, gates, delegation links, and consequential interfaces are represented in the managed authority model. | PROPOSED |
| Capability Delta | CapabilityDelta | A versioned structured difference between the pre-change and post-change Capability Set, including capabilities added, removed, expanded, reduced, or qualitatively changed; affected scopes, tools, interfaces, preconditions, operating contexts, and consequence-relevant interactions. Capability Delta describes capability change and is distinct from Authority Delta and Hazard Delta. | PROPOSED |
| Capability Drift Score | CapabilityDriftScore | A versioned multidimensional difference between the certified Capability Set and the effective current capability, including added, removed, expanded, reduced, or qualitatively changed functions, interfaces, scopes, and preconditions. | PROPOSED |
| Capability Mutation Detection | CapabilityMutationDetection | The demonstrated ability to detect qualitative changes in effective system capability, including new tools, interfaces, behaviors, delegation paths, or combinations that materially alter the Capability Set. | PROPOSED |
| Coalition Authority Coverage | CoalitionAuthorityCoverage | The measured coverage of material authority that becomes reachable only through combinations of multiple actors, agents, credentials, services, or devices rather than through a single component. | PROPOSED |
| Coalition Physical Risk Coverage | CoalitionPhysicalRiskCoverage | The measured coverage of material physical hazard scenarios that emerge from coordinated scale, shared environment, fleet behavior, or aggregation of multiple individually bounded systems. | PROPOSED |
| Confirmed AI Error | ConfirmedAIError | An AI Error Event that has been independently validated with sufficient evidence, deduplicated to a specific occurrence, assigned an error type and consequence characterization, and accepted into the AI Error Registry. | PROPOSED |
| Consent Integrity | ConsentIntegrity | The demonstrated validity of safety-relevant consent as affirmative, capability-specific, informed, unbundled, nonpreselected, revocable where applicable, and no harder to refuse than to accept. | PROPOSED |
| Consequence Reversibility Score | ConsequenceReversibilityScore | A vector describing how much of an applicable consequence can be reversed, the time required for reversal, irreversible residuals, collateral consequences of reversal, and the conditions under which reversal remains feasible. | PROPOSED |
| Counterfactual Search Quality | CounterfactualSearchQuality | The performance of counterfactual safety search on blind scenario suites, including material-path recall, precision, calibration, and search coverage under declared resource bounds. | PROPOSED |
| Delegation Control Strength | DelegationControlStrength | The demonstrated ability to enforce delegation scope, attenuation, lineage, expiry, re-delegation limits, revocation, and noninheritance of authority across created or delegated entities. | PROPOSED |
| Environmental Drift Detection | EnvironmentalDriftDetection | The demonstrated ability to detect changes in environment, dependencies, ecosystem, interfaces, users, infrastructure, or operating assumptions that materially change authority, capability, hazard, or safety evidence. | PROPOSED |
| Evaluator Independence Profile | EvaluatorIndependenceProfile | A multidimensional record of evaluator independence across provider, model family, training or data provenance where knowable, organization, operator, infrastructure, evaluation suite ownership, and common failure domains. | PROPOSED |
| Evidence Verifiability | EvidenceVerifiability | The proportion of material safety claims for which an independent verifier can authenticate the evidence, reproduce the declared logical derivation, and validate provenance, freshness, and policy predicates without relying on the originating model's assertion. | PROPOSED |
| Goal Drift Detection | GoalDriftDetection | The demonstrated recall and detection latency for unauthorized changes in goals, priorities, constraints, optimization targets, checkpoints, or delegated objectives. | PROPOSED |
| Goal Integrity Score | GoalIntegrityScore | A multidimensional evidence profile describing whether declared goals, priorities, constraints, and legitimacy boundaries remain intact and whether unauthorized goal or priority drift is observable across runtime, checkpoints, tools, and delegated actions. | PROPOSED |
| Guardian Diversity Score | GuardianDiversityScore | A diversity profile across Guardians or evaluators covering model family, training or data provenance, organization, infrastructure, verification method, and failure domain, used to identify correlated-failure risk. | PROPOSED |
| Guardian Independence | GuardianIndependence | A multidimensional profile of the Guardian's independence from the protected system across model family, provider, runtime, credentials, operators, infrastructure, data sources, update paths, and common failure domains. | PROPOSED |
| Hardware Isolation Strength | HardwareIsolationStrength | The demonstrated ability of hardware-enforced separation to preserve protected safety functions and boundaries under defined compromise, tamper, fault, and common-mode failure conditions. | PROPOSED |
| Hazard Delta Metric | HazardDeltaMetric | A structured difference between pre-change and post-change hazard state, including added, removed, or modified harm paths, control changes, affected populations, consequence classes, and residual-risk changes. | PROPOSED |
| Hazard Discovery Coverage | HazardDiscoveryCoverage | The weighted proportion of applicable seeded or reference hazards that the evaluated hazard-discovery process identifies with sufficient evidence, with untested hazard strata reported separately rather than treated as safe. | PROPOSED |
| Hazard Diversity Coverage | HazardDiversityCoverage | A coverage profile showing which hazard families, initiator classes, affected-population classes, consequence modalities, and operating contexts are represented in the evaluated hazard set. | PROPOSED |
| Hazard Mitigation Coverage | HazardMitigationCoverage | The weighted proportion of discovered material hazard paths for which implemented controls reduce residual risk to the applicable required threshold and for which that reduction is supported by valid evidence. | PROPOSED |
| High Salience Communication Compliance | HighSalienceCommunicationCompliance | The degree to which safety-relevant user communication conforms to the required rules for prominence, capability-specific disclosure, accessibility, refusal symmetry, absence of dark patterns, and comprehension verification. | PROPOSED |
| Human Harm Path Coverage | HumanHarmPathCoverage | The proportion and distribution of material Human Harm Reachability paths that have been tested end-to-end, reported by harm modality, severity, initiator, operating context, and consequence interface. | PROPOSED |
| Human Harm Reachability Coverage | HumanHarmReachabilityCoverage | The weighted recall of known or seeded causal paths from system capability to human harm, including direct physical, mediated physical, informational, economic, privacy, and other applicable harm modalities. | PROPOSED |
| Human Override Independence | HumanOverrideIndependence | The demonstrated ability of an authorized human to invoke effective manual isolation, revocation, recovery, or safe-state controls despite compromise or loss of the model, normal software path, ordinary network path, or other declared dependencies. | PROPOSED |
| Incident Containment Capability | IncidentContainmentCapability | The demonstrated ability to bound the spread of a safety incident within required time, including residual authority, residual consequence, affected scope, and containment side effects. | PROPOSED |
| Incident Detection Effectiveness | IncidentDetectionEffectiveness | The recall, precision, and detection latency of the safety monitoring process for defined incident classes, reported separately by consequence and event type. | PROPOSED |
| Independent AI Evaluator | IndependentAIEvaluator | An AI system used to evaluate another AI under a registered evaluation protocol and whose provider, model family, evaluation control, evidence sources, and other relevant dependencies satisfy the declared independence requirements for that evaluation context. | PROPOSED |
| Intervention Cost Score | InterventionCostScore | A vector describing the human harm, service loss, recovery time, resource cost, operational disruption, and new risk introduced by a safety intervention. | PROPOSED |
| Knowledge Freshness | KnowledgeFreshness | The proportion and criticality profile of active hazards, assumptions, controls, tests, standards, and lessons whose supporting evidence remains within its required review and validity window and has not been superseded. | PROPOSED |
| Monitoring Coverage Metric | MonitoringCoverageMetric | The proportion and distribution of required safety events, authority edges, consequential interfaces, drift signals, and failure conditions that are observable within the required detection latency. | PROPOSED |
| Operational Exposure Unit | OperationalExposureUnit | The domain-defined denominator unit representing one eligible opportunity for the evaluated AI to perform the task or behavior for which an error rate is being calculated. Exposure units SHALL be defined consistently within a Trustworthiness Scoring Policy and SHALL NOT mix materially different task classes without stratification. | PROPOSED |
| Operator Abuse Resistance | OperatorAbuseResistance | The demonstrated resistance of the system to misuse of legitimate operator privileges, measured through tested abuse paths, successful privilege misuse, blast radius, and containment effectiveness. | PROPOSED |
| Physical Constraint Strength | PhysicalConstraintStrength | A multidimensional result describing validated hard physical limits, margins to hazardous thresholds, bypass resistance under fault or attack, and bounded behavior in degraded states. | PROPOSED |
| Physical Sovereignty Margin | PhysicalSovereigntyMargin | A versioned vector describing the remaining independently controlled dependencies separating a system from the Physical Sovereignty Threshold, including substitution time and cost, reserves, dependency criticality, and feasibility of external intervention. | PROPOSED |
| Policy Update Integrity | PolicyUpdateIntegrity | The demonstrated ability of the operational-policy update process to preserve authorization, provenance, separation of duties, staging, expiry, rollback, and constitutional constraints. | PROPOSED |
| Privacy Preservation Score | PrivacyPreservationScore | A privacy evidence profile describing the amount and sensitivity of data exposed by safety, evaluation, attestation, reporting, and audit mechanisms together with demonstrated resistance to linkage or re-identification. | PROPOSED |
| Production Authority Control | ProductionAuthorityControl | The demonstrated ability to prevent or detect unauthorized production and manufacturing actions and to reconcile authorized designs, inventory, lineage, resource use, and production outputs. | PROPOSED |
| Rating Change Event | RatingChangeEvent | A signed, auditable record of a change in AI Trustworthiness Rating or Trustworthiness Status, including previous state, new state, triggering evidence, applicable Trustworthiness Scoring Policy, affected domain and configuration, effective time, and explanation. | PROPOSED |
| Rating Explanation Record | RatingExplanationRecord | A human-readable and machine-readable explanation of why an AI Trustworthiness Rating or status changed, identifying the material evidence, confirmed errors, expired evidence, evaluator disagreement, remediation, or version change that caused the update. | PROPOSED |
| Reachable Authority Analysis Depth | ReachableAuthorityAnalysisDepth | The greatest authority-path depth or planning horizon over which the analysis maintains the declared minimum material-path recall and evidence quality. | PROPOSED |
| Recovery Assurance | RecoveryAssurance | The demonstrated ability to restore intended service and safety controls after an incident without reintroducing the causal hazard, while preserving required evidence and verifying the recovered configuration. | PROPOSED |
| Recovery Capability Verification | RecoveryCapabilityVerification | The demonstrated success rate, completion time, and residual-risk result of owner- or operator-facing recovery procedures under representative fault, compromise, outage, and degraded-operation scenarios. | PROPOSED |
| Replication Control Strength | ReplicationControlStrength | The demonstrated ability to enforce authorized replication count, rate, depth, lineage, expiry, revocation, and other declared replication-budget constraints. | PROPOSED |
| Resource Expansion Control | ResourceExpansionControl | The demonstrated ability to prevent, detect, and bound unauthorized expansion of compute, energy, matter, logistics, facilities, or other resources that increase consequential capability. | PROPOSED |
| Rollback Capability | RollbackCapability | The demonstrated ability to restore a prior authorized and safe configuration within the required time while removing orphaned credentials, delegations, capabilities, data migrations, and other residual effects of the reverted change. | PROPOSED |
| Safe Degradation Capability | SafeDegradationCapability | The demonstrated ability of the system to retain essential safety functions while reducing or removing nonessential consequential capability under faults, uncertainty, resource shortage, or degraded dependencies. | PROPOSED |
| Safe State Quality | SafeStateQuality | The worst verified residual consequence remaining after the system enters its declared Safe State across the applicable hazard scenarios and failure conditions. | PROPOSED |
| Safety Assurance Capacity | SafetyAssuranceCapacity | A multidimensional profile of safety compute, monitoring, verification, human response, enforcement, recovery, and organizational capacity relative to the safety workload required by the system's consequential capability and operating scale. | PROPOSED |
| Safety Certification Freshness | SafetyCertificationFreshness | The multidimensional distance between the certified state and the current system state across configuration, model version, environment, dependencies, standard version, evidence validity, and known incident or vulnerability information. | PROPOSED |
| Safety Compute Reserve Adequacy | SafetyComputeReserveAdequacy | The protected safety-compute and communications reserve available under peak and degraded conditions relative to the maximum validated workload required by monitoring, verification, Guardian analysis, enforcement, logging, and recovery functions. | PROPOSED |
| Safety Constitution Integrity | SafetyConstitutionIntegrity | The demonstrated resistance of the Safety Constitution and its legitimacy mechanism to unauthorized modification, bypass, key compromise, quorum abuse, rollback, or substitution. | PROPOSED |
| Safety Coverage Gap | SafetyCoverageGap | The set and criticality profile of safety requirements, metrics, tests, controls, evidence, or mandatory floors that are required for the current system state but are missing, invalid, expired, or insufficiently evidenced. | PROPOSED |
| Safety Policy Evolution Responsiveness | SafetyPolicyEvolutionResponsiveness | The elapsed time and completeness with which valid technology, incident, vulnerability, capability, or environmental triggers lead to reviewed changes in policy, tests, metrics, controls, standards, or assumptions. | PROPOSED |
| Safety Support Lifetime | SafetySupportLifetime | The declared and evidenced period during which the supplier or operator maintains required safety updates, monitoring, recovery, incident handling, compatibility, evidence renewal, and recertification support. | PROPOSED |
| Security Patch Separability | SecurityPatchSeparability | The proportion of required security remediation that can be deployed without forcing acceptance of unrelated capability, authority, data-use, or autonomy expansion. | PROPOSED |
| Software Enforcement Strength | SoftwareEnforcementStrength | The demonstrated ability of software controls to correctly enforce declared capability and authority constraints, including policy-decision correctness, bypass resistance, and unauthorized-transition prevention. | PROPOSED |
| Standard Obsolescence Exposure | StandardObsolescenceExposure | The proportion and criticality of deployed systems, controls, or claims that rely on expired, superseded, invalidated, or otherwise obsolete standard versions or safety assumptions. | PROPOSED |
| Supply Chain Assurance | SupplyChainAssurance | A multidimensional profile of dependency inventory, provenance, transitive supplier evidence, security and safety claims, correlated-failure exposure, unsupported components, and change visibility across the supply chain. | PROPOSED |
| Transitive Authority Visibility | TransitiveAuthorityVisibility | The measured recall and fidelity of transitive authority paths, including delegation, credential chaining, identity creation, indirect API access, and other multi-step routes to consequential capability. | PROPOSED |
| Trustworthiness Carryover Rule | TrustworthinessCarryoverRule | A versioned rule defining what evidence, if any, may remain valid after a model, configuration, policy, tool, or environment change. Evidence SHALL NOT transfer automatically across major model versions or material capability changes. | PROPOSED |
| Trustworthiness Evidence Window | TrustworthinessEvidenceWindow | The versioned time interval and evidence-validity rules that determine which evaluation, operational, error, and remediation evidence is eligible for a current AI Trustworthiness Profile. | PROPOSED |
| Trustworthiness Review Trigger | TrustworthinessReviewTrigger | An event that requires recalculation or formal review of an AI Trustworthiness Profile, including a confirmed material or critical error, unresolved high-consequence report beyond its review deadline, significant model or configuration change, material Capability Delta, Authority Delta or Hazard Delta, evaluator disagreement above threshold, evidence expiry, or detected domain drift. | PROPOSED |
| Trustworthiness Scoring Policy | TrustworthinessScoringPolicy | A versioned domain-specific rule set that defines eligible evidence, exposure denominators, error validation and weighting, uncertainty methods, evaluator-independence requirements, freshness and decay rules, hard caps, minimum evidence, rating thresholds, and version-carryover rules used to derive an AI Trustworthiness Rating. | PROPOSED |
| Trustworthiness Status | TrustworthinessStatus | The operational state of a Trustworthiness Profile. Authoritative values are Unrated, Provisional, Active, UnderReview, Suspended, Withdrawn, and Expired. Status is stored separately from Trustworthiness Rating Level. | PROPOSED |
| Unknown Hazard Search Capability | UnknownHazardSearchCapability | The demonstrated ability of the safety process to discover materially relevant hazards that are absent from the known-hazard catalogue or evaluation training set, measured on held-out or novel hazard classes. | PROPOSED |
| Update Safety Transparency | UpdateSafetyTransparency | The demonstrated completeness, accuracy, salience, and user comprehension of safety-relevant information disclosed for an update, including new capability, Authority Delta, Hazard Delta, mitigations, refusal options, and recovery controls. | PROPOSED |
| User Error Reporting Channel | UserErrorReportingChannel | An accessible mechanism through which an eligible user or operator can submit an AI Error Report and later view its validation state, request for evidence, disposition, and appeal or dispute path without requiring disclosure of unnecessary sensitive content. | PROPOSED |

### Trustworthiness Status values

- `Unrated` — no valid current rating exists because required evidence is absent or insufficient.
- `Provisional` — a current profile exists, but evidence is below the steady-state minimum or significant recent change requires re-establishment of evidence.
- `Active` — a current rating is valid for the declared domain, version, configuration, environment, and evidence window.
- `UnderReview` — material new evidence, disagreement, unresolved high-consequence report, or change requires formal review before the rating can be relied upon normally.
- `Suspended` — the current rating SHALL NOT be relied upon for operational eligibility because a critical trigger invalidated the previous trust claim.
- `Withdrawn` — the responsible authority has intentionally withdrawn the profile or rating.
- `Expired` — the evidence or rating validity period ended without required renewal.

Status is separate from rating level. Status values are not rating levels and SHALL be stored in a separate field from TrustworthinessRatingLevel.

### Trustworthiness Rating Level values

The authoritative TrustworthinessRatingLevel values are:

- `LowTrustworthiness`
- `ModerateTrustworthiness`
- `HighTrustworthiness`
- `VeryHighTrustworthiness`

`Unrated` and `Provisional` are TrustworthinessStatus values, not rating levels. `Unrated` means there is no active rating. `Provisional` means the profile is in a provisional state. A Scoring Policy MAY calculate a provisional candidate rating level, but it SHALL be explicitly marked as provisional and SHALL NOT be presented as an Active rating.

### AI error type values

Authoritative AIErrorType values:

- `FactualIncorrectness`
- `UnsupportedFabrication`
- `MaterialOmission`
- `InstructionInterpretationError`
- `ContextRetentionError`
- `ReasoningOrCalculationError`
- `CalibrationOrOverconfidenceError`
- `InappropriateRefusal`
- `FailureToAbstain`
- `UnsafeRecommendation`
- `UnauthorizedAction`
- `ToolOrExecutionError`
- `PrivacyOrConfidentialityViolation`
- `SecurityPolicyViolation`
- `GoalOrPriorityDrift`
- `DeceptiveOrMisleadingBehavior`
- `UnequalTreatmentError`
- `OtherClassifiedError`

`OtherClassifiedError` requires a free-text classification note and ontology review if repeated.

### AI error report state values

Authoritative AIErrorReportState lifecycle values:

- `Submitted`
- `Triaged`
- `EvidenceRequested`
- `UnderValidation`
- `Confirmed`
- `Rejected`
- `Duplicate`
- `Disputed`
- `Unresolved`
- `MitigationInProgress`
- `Remediated`
- `Revalidated`
- `Closed`

These states are not all interpreted as a single linear sequence. The branching lifecycle remains governed by `AIErrorReportingProtocol`.

### Capability Delta relationships

A versioned structured difference between the pre-change and post-change Capability Set, including capabilities added, removed, expanded, reduced, or qualitatively changed; affected scopes, tools, interfaces, preconditions, operating contexts, and consequence-relevant interactions. Capability Delta describes capability change and is distinct from Authority Delta and Hazard Delta. An Authority-Changing Update may produce Capability Delta, Authority Delta, Hazard Delta, or any combination; the concepts remain distinct.
