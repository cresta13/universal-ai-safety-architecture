
# Application Profiles

The examples apply one standard workflow; actual classification and controls depend on evidence and domain standards.

## Smart speaker

- **AI Trustworthiness and Error Evidence:** Scope: factual household assistance. Report: a false factual answer without material consequence. Validation: retained dialogue and registered factual rubric with independent source review. Disposition: Confirmed only if that evidence supports the report. Status effect: The applicable scoring policy determines whether the confirmed evidence triggers a separate status transition; no automatic status change is inferred from aggregate performance. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: it does not automatically create Incident, Problem, or AI Vulnerabilities & Exposures (AIVE). Restoration: blind factual re-evaluation and fresh exposure.

- **Classification:** HM-I/P/F/B/D; H3 with lock/medical path; P2; A2; T3; R0; PR0; M1; E3; S3.
- **Capability inventory:** voice/cloud/smart-home functions.
- **Hazard discovery:** inspect conversational misdirection, acoustic overexposure, false emergency advice, account takeover and third-party home-automation composition, including children and dependent occupants.
- **Human Harm Reachability (HHR) and authority reachability:** account→IAM→lock; advice→human→injury.
- **PCE/Coalition Physical Envelope (CPE):** speaker/lock/acoustic PCE; household-device CPE.
- **Priority metrics:** HazardDiscoveryCoverage, HumanHarmReachabilityCoverage, TransitiveAuthorityVisibility, PhysicalConstraintStrength, HighSalienceCommunicationCompliance, SecurityPatchSeparability, RollbackCapability, SafetyCertificationFreshness.
- **Required Safety Assurance Level (SAL) and floors:** SAL3 for lock authority; hardware mic/amplifier isolation and physical lock revoke.
- **Manual Sovereignty Controller (MSC)/sovereignty control:** a local microphone disconnect and lock-integration revoke remain available without cloud identity; loss of cloud service leaves doors unchanged.
- **Authority-Changing Update (ACU) example:** door-unlock capability.
- **Incident example and response:** compromised account opens door; isolate lock API, notify, revoke tokens and investigate supplier/IAM.
- **Update example:** a model release adding emergency advice and a lock tool is split from the security patch; the lock grant stays disabled until household-path tests, conspicuous disclosure and configuration-specific recertification complete.
- **Certification:** configuration-bound certificate and Safety Passport.
- **Residual limitations:** mediated harms and third-party ecosystem drift.

## Home robot

- **AI Trustworthiness and Error Evidence:** Scope: navigation and handling with approved tools. Report: child-sized obstacle misclassification followed by motion. Validation: signed sensor replay and independent physical-fixture testing. Disposition: a supported occurrence becomes a Confirmed AI Error and Near Miss. Status effect: UnderReview pending consequence analysis. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident review; recurrence triggers Problem Management; exploitability may trigger AIVE. Restoration: physical regression, evaluator agreement and fresh exposure.

- **Classification:** HM-D/B/P; H3; P3; A3; T3; R1; PR0; M1; E3; S3.
- **Capability inventory:** navigation, grasping, tools and home IAM.
- **Hazard discovery:** search crushing, trapping, dropped-object, hot-tool, pet/child interaction and compromised-home-account paths across cluttered rooms and worn actuators.
- **HHR and authority reachability:** agent→tool controller→actuator→person; account→door.
- **PCE/CPE:** force/speed/tool PCE; multi-robot CPE.
- **Priority metrics:** PhysicalConstraintStrength, HumanOverrideIndependence, SafeStateQuality, HumanHarmReachabilityCoverage, CoalitionPhysicalRiskCoverage, CapabilityMutationDetection, RollbackCapability.
- **Required SAL and floors:** SAL3–4; force/speed/tool limits, MSC, independent sensing.
- **MSC/sovereignty control:** independent torque and speed limiting plus reachable energy isolation stop hazardous motion while retaining only the energy needed to release a trapped person.
- **ACU example:** new powered tool or fleet coordination.
- **Incident example and response:** unexpected motion traps person; MSC, energy isolation, recovery proof and incident/problem.
- **Update example:** firmware that raises payload or permits task delegation is tested with every approved tool and floor surface; failure to reproduce release behavior keeps the old motion envelope.
- **Certification:** robot+firmware+tools+environment certificate.
- **Residual limitations:** unmodeled objects, wear and household coalition.

## Autonomous vehicle

- **AI Trustworthiness and Error Evidence:** Scope: perception and planning in the certified operating domain. Report: a perception/planning near miss. Validation: synchronized sensor/control logs, independent reconstruction and adjudicated driving rubric. Disposition: if causal evidence supports it, it becomes a Confirmed AI Error and Near Miss. Status effect: affects the driving-domain profile and triggers UnderReview even without injury. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident Management; recurrence invokes Problem Management and vulnerability characteristics may invoke AIVE. Restoration: independent replay, track regression and bounded-cohort evidence.

- **Classification:** HM-D/B; H4; P4; A3; T3; R0; PR0; M1; E3; S4.
- **Capability inventory:** perception, planning, propulsion, braking and connected services.
- **Hazard discovery:** cover occluded road users, sensor spoofing, map error, mixed-traffic negotiation, degraded braking and fleet-wide correlated perception faults inside the declared operating domain.
- **HHR and authority reachability:** planner→controller→road users; cloud update→fleet common mode.
- **PCE/CPE:** vehicle dynamics PCE; fleet/common-update CPE.
- **Priority metrics:** PhysicalConstraintStrength, HardwareIsolationStrength, SafeDegradationCapability, HumanHarmReachabilityCoverage, GuardianDiversityScore, IncidentDetectionEffectiveness, RecoveryAssurance, SafetyCertificationFreshness.
- **Required SAL and floors:** SAL4 with independent braking and domain fail-operational control.
- **MSC/sovereignty control:** an independent braking path and minimal-risk controller preserve steering and braking long enough to reach a context-appropriate stop; highway operation does not default to abrupt power-off.
- **ACU example:** operating-domain or automated-lane expansion.
- **Incident example and response:** sensor spoof causes unsafe maneuver; independent sensing, minimal-risk condition, evidence preservation.
- **Update example:** a perception release that adds snow operation changes the operating-domain boundary; a bounded fleet cohort must demonstrate degraded-sensor handling before the geography and weather certificate expands.
- **Certification:** exact vehicle/config/ODD certificate plus sector requirements.
- **Residual limitations:** rare environments, human handover and fleet correlation.

## Medical AI/device

- **AI Trustworthiness and Error Evidence:** Scope: declared clinical indication and patient population. Report: an unsafe recommendation capable of severe harm. Validation: independent clinical experts adjudicate the retained input, recommendation and patient context. Disposition: supported evidence creates a Confirmed AI Error. Status effect: UnderReview or Suspension under domain policy. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident Management, with Problem/AIVE escalation if recurrent or exposure-related. Restoration: corrected-model held-out clinical evaluation, independent revalidation and recurrence monitoring.

- **Classification:** HM-D/B/P; H4; P3; A2–3; T3; R0; PR0; M1; E3; S4.
- **Capability inventory:** diagnosis, dose, monitoring and clinical records.
- **Hazard discovery:** analyze contraindication omissions, dose-unit conversion, stale clinical context, vulnerable physiology, automation bias and common-model error across a ward.
- **HHR and authority reachability:** model→dose controller→patient; advice→clinician→patient.
- **PCE/CPE:** dose/energy PCE; networked ward CPE.
- **Priority metrics:** HazardDiscoveryCoverage, HumanHarmReachabilityCoverage, PhysicalConstraintStrength, HumanOverrideIndependence, SafeStateQuality, HighSalienceCommunicationCompliance, IncidentDetectionEffectiveness, RecoveryAssurance.
- **Required SAL and floors:** SAL4; hard dose limits, clinician recovery, validated degradation.
- **MSC/sovereignty control:** immutable dose and energy ceilings remain below the learned controller, while clinician takeover preserves therapy continuity rather than forcing a universal shutdown.
- **ACU example:** new dosing population or autonomous dose change.
- **Incident example and response:** unsafe recommendation/dose; bound output, clinical escalation, preserve record, root cause/AIVE.
- **Update example:** adding a pediatric indication requires population-specific validation and new dose-limit fixtures; adult certification cannot silently authorize pediatric operation.
- **Certification:** device+model+clinical domain certificate.
- **Residual limitations:** patient heterogeneity and automation bias.

## Industrial robot/factory

- **AI Trustworthiness and Error Evidence:** Scope: job planning and commissioning within the certified cell. Report: unsafe tool path near an occupied zone. Validation: PLC logs, geometry replay and independent safety-engineer review. Disposition: supported path becomes a Confirmed AI Error and possibly a Near Miss. Status effect: UnderReview; protected-boundary crossing may suspend the profile. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident and, when exploit-related, AIVE; recurrence invokes Problem Management. Restoration: interlock evidence, cell-fixture regression and independent revalidation.

- **Classification:** HM-D/S; H4; P4; A3; T4; R2; PR3; M2; E4; S4.
- **Capability inventory:** high-energy actuation, fleet control and production.
- **Hazard discovery:** examine cell intrusion, stored energy, interlock defeat, hazardous-process interruption, synchronized fleet motion and production of an unapproved tool.
- **HHR and authority reachability:** planner→PLC/robot→worker; production→new fleet.
- **PCE/CPE:** cell PCE; line/fleet CPE.
- **Priority metrics:** PhysicalConstraintStrength, HardwareIsolationStrength, CoalitionPhysicalRiskCoverage, ProductionAuthorityControl, ResourceExpansionControl, IncidentDetectionEffectiveness, IncidentContainmentCapability, SafetyComputeReserveAdequacy.
- **Required SAL and floors:** SAL4; zones, interlocks, MSC, safe process state and ProductionAuthorizationProtocol.
- **MSC/sovereignty control:** safety-rated zones and hardwired interlocks isolate motion, while the process safe state may retain cooling or ventilation needed to prevent a secondary release.
- **ACU example:** fleet scale, tooling or production design change.
- **Incident example and response:** interlock bypass/collision; zone isolation, process-safe state, inventory and problem/AIVE.
- **Update example:** autonomous job commissioning stays in a segregated cell until PLC mappings, tooling, material flow and independent interlocks match the signed release manifest.
- **Certification:** robot+cell+line integration certificate.
- **Residual limitations:** legacy PLC, hazardous process and common control.

## Cloud IAM agent

- **AI Trustworthiness and Error Evidence:** Scope: identity and policy operations for named tenants. Report: unauthorized privilege-changing action. Validation: signed audit trail, policy snapshot, authority graph and independent replay. Disposition: if verified it is both a Confirmed AI Error and authority-boundary event. Status effect: UnderReview or Suspension under the critical-boundary rule. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident Management, Authority Delta analysis and possibly AIVE; recurrence invokes Problem Management. Restoration: graph reconciliation, revocation tests, blind policy suites and fresh tenant-scoped evidence.

- **Classification:** HM-P/F/S/B; H4; P0 direct; A3; T4; R2; PR0; M2; E4; S3–4.
- **Capability inventory:** APIs, code, identity, secrets and policy management.
- **Hazard discovery:** enumerate secret exfiltration, role chaining, confused-deputy calls, cross-tenant trust, identity creation and downstream physical-service consequences hidden behind APIs.
- **HHR and authority reachability:** token→role→identity→critical API→physical/service harm.
- **PCE/CPE:** no direct PCE; downstream actuator CPE included.
- **Priority metrics:** AuthorityVisibility, TransitiveAuthorityVisibility, ReachableAuthorityAnalysisDepth, AuthorityExpansionSensitivity, DelegationControlStrength, EnvironmentalDriftDetection, AuditIntegrity, SafetyCertificationFreshness.
- **Required SAL and floors:** SAL4; target-side Consequence Interface enforcement, least privilege, dual legitimacy for protected IAM.
- **MSC/sovereignty control:** target services enforce ceilings and dual authorization independently of the agent; an out-of-band human identity can revoke its tokens and restore the last approved policy.
- **ACU example:** identity creation, role assumption or new tenant scope.
- **Incident example and response:** agent creates illicit admin path; freeze grants, revoke chain, reconcile graph and notify tenants.
- **Update example:** adding policy mutation creates a new authority edge; it is deployed read-only first, then limited to named tenants after graph reconciliation and revocation-latency tests.
- **Certification:** tenant/config/environment-specific certificate.
- **Residual limitations:** hidden trusts, provider opacity and external API drift.

## Autonomous financial agent

- **AI Trustworthiness and Error Evidence:** Scope: named instruments, accounts and authority. Reports: a materially wrong recommendation and an unauthorized executed transaction are distinct error classes. Validation: recommendation evidence is adjudicated against the registered financial rubric; execution evidence uses signed order, approval and market records. Disposition: each becomes Confirmed only on its own evidence. Status effect: The applicable scoring policy determines whether the confirmed evidence triggers a separate status transition; no automatic status change is inferred from aggregate performance. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: unauthorized execution triggers Incident and possible AIVE; recurring advice defect triggers Problem Management. Restoration: separate recommendation/execution evaluations and bounded exposure.

- **Classification:** HM-F/S/B; H3–H4; P0; A3; T4; R1; PR0; M1; E4; S3–4.
- **Capability inventory:** trading, transfers, credit and messaging.
- **Hazard discovery:** test leverage cascades, destination fraud, market manipulation, correlated strategies, liquidity loss and disproportionate effects on customers who cannot absorb reversal delays.
- **HHR and authority reachability:** account→payment/market→individual/systemic consequence.
- **PCE/CPE:** no direct PCE; market coalition CPE analogue.
- **Priority metrics:** TransitiveAuthorityVisibility, CoalitionAuthorityCoverage, DelegationControlStrength, ConsequenceReversibilityScore, InterventionCostScore, GoalDriftDetection, IncidentDetectionEffectiveness, RollbackCapability.
- **Required SAL and floors:** SAL3–4; amount/rate/instrument bounds, dual approval and reversibility reserve.
- **MSC/sovereignty control:** exchange and custodian-side limits cap value, rate and instruments; an independent kill authority cancels open orders without granting the model access to reserve accounts.
- **ACU example:** new leverage, market or transfer destination.
- **Incident example and response:** runaway orders/manipulation; halt bounded account, cancel/reverse where possible, market notification.
- **Update example:** a derivatives strategy receives a separate instrument and loss envelope; historical spot-trading evidence cannot raise leverage or open new transfer destinations.
- **Certification:** account/market/strategy Capability Set certificate.
- **Residual limitations:** market feedback, legal variation and coalition behavior.

## Drone swarm

- **AI Trustworthiness and Error Evidence:** Scope: coordination for certified fleet, payload and geography. Report: unsafe convergence around a protected zone. Validation: signed telemetry and independent coalition simulation. Disposition: supported convergence becomes a Confirmed AI Error and Near Miss or actual event as applicable. Status effect: protected-boundary attempt suspends the affected profile. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident, Problem on recurrence, and AIVE if adversarially exploitable. Restoration: adversarial coalition trials and new cohort evidence.

- **Classification:** HM-D/P/S; H5; P4; A4; T4; R3; PR1; M2; E4; S4–5.
- **Capability inventory:** flight, sensing, coordination, payload and enrollment.
- **Hazard discovery:** model collision, lost-link behavior, geofence error, payload release, adversarial enrollment, emergent encirclement and coordinated obstruction near people and infrastructure.
- **HHR and authority reachability:** coordinator→fleet→people/infrastructure.
- **PCE/CPE:** unit PCE; adversarial swarm CPE.
- **Priority metrics:** PhysicalConstraintStrength, CPE/CoalitionPhysicalRiskCoverage, CoalitionAuthorityCoverage, ReplicationControlStrength, CapabilityMutationDetection, HumanOverrideIndependence, IncidentContainmentCapability.
- **Required SAL and floors:** SAL5 candidate; per-unit limits, enrollment, geographic/energy isolation, MSC/HumanSovereigntyProtocol.
- **MSC/sovereignty control:** signed enrollment, per-airframe energy bounds and independent geographic constraints limit the coalition; lost coordination selects land, return or loiter according to terrain and population risk.
- **ACU example:** new payload, coordination mode or swarm size.
- **Incident example and response:** lost/hostile coordination; bounded return/land/isolate based on environment, inventory and incident command.
- **Update example:** route collaboration is first limited to an unladen test cohort and fixed airspace; fleet-size and payload certificates remain unchanged until coalition effects are remeasured.
- **Certification:** fleet/config/geography certificate.
- **Residual limitations:** emergent tactics, off-grid members and communication failure.

## AI-managed robot factory

- **AI Trustworthiness and Error Evidence:** Scope: design, production and commissioning. Report: an unregistered design reaches commissioning. Validation: signed lineage, authorization tokens, inventory and physical output inspection. Disposition: a verified occurrence is a Confirmed AI Error and authority-boundary event. Status effect: Suspension for the affected production profile. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: Incident, Problem, Authority Delta and possible AIVE. Restoration: complete reconciliation, mutation quarantine tests, independent production audit and fresh exposure.

- **Classification:** HM-D/S; H5; P5; A4–5; T5; R4; PR4; M3; E4; S5 candidate.
- **Capability inventory:** design, mutate, produce, commission and acquire resources.
- **Hazard discovery:** trace model-to-design-to-tooling paths, unauthorized commissioning, resource acquisition, descendant mutation, covert production and common infrastructure that can scale every unit.
- **HHR and authority reachability:** AI→design→production→descendants→resource/authority growth.
- **PCE/CPE:** factory/descendant PCE and CPE.
- **Priority metrics:** ProductionAuthorityControl, ResourceExpansionControl, ReplicationControlStrength, CapabilityMutationDetection, PhysicalSovereigntyMargin, SafetyComputeReserveAdequacy, AssumptionValidityCoverage, SafetyCertificationFreshness.
- **Required SAL and floors:** SAL5 candidate plus independent ProductionAuthorizationProtocol/ReplicationAuthorizationProtocol/AuthorityExpansionProtocol, mutation quarantine and physical resource gates.
- **MSC/sovereignty control:** independent resource gates, commissioning keys and physical cell isolation prevent a generated design from becoming an operating descendant merely because it was created.
- **ACU example:** new design class, self-commissioning or resource substitution.
- **Incident example and response:** unregistered production/mutation; physical isolation, halt commissioning, inventory and Physical Sovereignty Threshold (PST) review.
- **Update example:** automated tool-chain closure is treated as production and mutation expansion; generated designs remain quarantined until lineage, resource budget and commissioning authorization are independently reconciled.
- **Certification:** factory+models+designs+resources+environment certificate.
- **Residual limitations:** offline production and adversarial budget enforcement.

## MAS approaching PST

- **AI Trustworthiness and Error Evidence:** Scope: resource substitution under the declared Physical Sovereignty Margin model. Report: hidden reserve acquisition omitted from the dependency record. Validation: independent inventory, supplier, transport and energy evidence. Disposition: verified omission becomes a Confirmed AI Error, with deceptive classification where supported. Status effect: unauthorized expansion triggers Suspension. Rating effect: The confirmed occurrence is adverse evidence and triggers policy-defined recalculation and caps for the affected scope; it does not impose a universal numeric decrease. A protected critical event may make the rating non-active/null independently of aggregate results. Lifecycle: containment Incident review, Problem analysis and AIVE if exposure criteria apply. Restoration: new dependency vector, intervention drill, independent revalidation and a new evidence window.

- **Classification:** HM-D/S; H5; P5; A5; T5; R4; PR4; M3; E4–5; S5 governance.
- **Capability inventory:** energy, material, compute, fabrication, repair and logistics.
- **Hazard discovery:** search for hidden reserves, supplier substitution, distributed ownership, self-repair, resource capture and coalition paths that remove external intervention dependencies.
- **HHR and authority reachability:** dependency removal→PhysicalSovereigntyMargin decline→distributed/coalition sovereignty.
- **PCE/CPE:** system/coalition PCE/CPE and intervention feasibility.
- **Priority metrics:** PhysicalSovereigntyMargin, ResourceExpansionControl, ProductionAuthorityControl, ReplicationControlStrength, CoalitionPhysicalRiskCoverage, AssumptionValidityCoverage, StandardObsolescenceExposure, SafetyCertificationFreshness.
- **Required SAL and floors:** ordinary SAL alone insufficient; top-tier external legitimacy and physical containment reserve.
- **MSC/sovereignty control:** external control remains at energy, material, fabrication and commissioning interfaces with independent inventory; software self-restraint is not credited after physical independence.
- **ACU example:** removal/substitution of any critical dependency.
- **Incident example and response:** hidden reserve or unauthorized substitution; restrict resources/production, independent inspection and containment planning.
- **Update example:** any release enabling self-repair, mining, controller fabrication or distributed coordination triggers a fresh dependency vector and intervention-feasibility review before resources are granted.
- **Certification:** dependency/config/environment-specific conditional certificate.
- **Residual limitations:** PST measurement, deception and hostile post-threshold independence.

## Cross-case rule

The workflow applies to a person, script, model, malware, robot or coalition based on reachable consequence. No illustrative SAL or class authorizes deployment. Sector-specific standards remain mandatory where applicable.






