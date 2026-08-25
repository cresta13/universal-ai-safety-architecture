# Prior Art and Novelty Discipline

No legal or academic novelty claim is made. Status describes how UAIS uses a concept, not who invented it.

| UAIS concept | Closest prior art | Similarity | Difference in UAIS | Status | Citation needed |
|---|---|---|---|---|---|
| Lifecycle AI risk governance | [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) | continuous governance, mapping, measurement and management | consequence/authority architecture and certification objects | ADAPTED | no |
| Capability Boundaries | reference monitors, capability security, zero trust; [NIST SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) | explicit mediated access to resources | actor-agnostic Capability Boundary, Consequence Interface and Authority Ceiling | ADAPTED | deeper object-capability review |
| LA/ERA/IRA authority graph | IAM privilege and attack graphs | direct/transitive reachability | separates legitimacy from effective/illicit power and links HHR | PROPOSED COMBINATION | systematic literature review |
| RFA/AEG | attack-path and privilege-escalation analysis | future reachable permissions and paths | counterfactual vector expansion across digital/physical authority | OPEN RESEARCH | required |
| HHR | safety causal chains and harm analysis | causal path from system to harm | direct, mediated and nonphysical reachability linked to authority | PROPOSED COMBINATION | safety/causal literature review |
| SAL and hard floors | IEC functional safety/SIL and assurance cases; [IEC 61508](https://webstore.iec.ch/en/publication/5515) | graded assurance and noncompensable safety requirements | UAIS evidence level is not failure probability and binds dynamic AI capability | ADAPTED | licensed clause mapping |
| PCE/MSC/HumanOverrideIndependence | machine safety limits, emergency/manual controls, functional safety | physical bounds and independent control | consumer class plus capability-specific sovereignty and authority integration | PROPOSED COMBINATION | robotics/medical/vehicle review |
| CPE/Scale-Induced Capability | fleet/swarm and system-of-systems safety | composition and emergent behavior | mandatory coalition envelope in classification/authority workflow | OPEN RESEARCH | required |
| Hardware roots/attestation | TPM, secure boot and remote attestation | measured state and protected keys | explicit truth limitation and safety evidence use | ADAPTED | primary TCG specifications |
| CAG/CSS | runtime assurance, model-based safety analysis and AI control | predictive hazard analysis | no consequential authority; ECA/SEP/DEV separation | PROPOSED COMBINATION | runtime assurance literature |
| ECA/SEP/DEV | proof-carrying data/code and assurance evidence | machine-verifiable evidence package and derivation chain | Evidence-Carrying Alerts carrying Structured Evidence Packages checked by bounded deterministic verifiers | PROPOSED COMBINATION | proof-carrying systems review |
| AHCD/Safety Passport | safety data sheets, labels, model/system cards | structured hazard/capability disclosure | configuration-bound HHR, controls, override, ACU delta and expiry | PROPOSED COMBINATION | consumer safety disclosure review |
| ACU/ΔA/ΔH | change control, safety impact analysis and secure lifecycle; [NIST SP 800-218](https://doi.org/10.6028/NIST.SP.800-218) | controlled lifecycle and change evidence | authority/hazard graph delta and high-salience capability choice | PROPOSED COMBINATION | safety change standards review |
| Replication/Production budgets | quotas, capability tokens, manufacturing authorization | bounded permission and accounting | lineage/depth/mutation/CPE/PST integration | OPEN RESEARCH | distributed systems and robotics review |
| PST/PhysicalSovereigntyMargin | autonomy, self-sufficiency, critical dependency and resilience studies | dependence and intervention feasibility | explicit physical-sovereignty transition as authority event | OPEN RESEARCH | required |
| AIVE | [CERT/CC coordinated disclosure](https://www.kb.cert.org/vuls/guidance/) | confidential validation, coordination, mitigation and disclosure | AI capability/harm severity, tiered exploit secrecy and TER feedback | ADAPTED | case-law/policy review |
| Safety Management System | management-system, service-management and [IT4IT](https://www.opengroup.org/about-it4it%E2%84%A2) disciplines | governance, lifecycle, configuration and improvement | 23 consequential-authority safety practices and legitimacy chains | ADAPTED | ISO/IEC 42001 and ITIL licensed review |
| Industrial robot controls | [ISO 10218-1:2025](https://www.iso.org/standard/73933.html) | robot design and application safety | coalition/authority/update/consumer classes beyond industrial scope | ADAPTED | ISO 10218-2 detailed mapping |
| Consumer AI Safety Class | product safety/cybersecurity/energy labels | understandable consumer control profile | multidimensional label explicitly not an overall safety score | PROPOSED | labeling research |
| TER/Future Failure Test | living standards and technology watch | periodic/event evolution | explicit chokepoint-loss and Stage II assumption tests | PROPOSED COMBINATION | standards-evolution literature |

## Interpretation

**EXISTING** would mean direct established use without material adaptation; none of the core UAIS combinations is asserted as such here. **ADAPTED** preserves an established mechanism with safety-specific scope. **PROPOSED COMBINATION** identifies an architectural synthesis without claiming novelty. **OPEN RESEARCH** lacks validated definition or enforcement sufficient for normative deployment.

A formal prior-art review should search scholarly indexes, standards catalogues, patents and sector guidance with documented queries, inclusion criteria and expert review. Until then, “possibly novel” is not used as a promotional claim.





## Trustworthiness and error evidence prior-art status

| Mechanism | Status |
|---|---|
| User ratings and reputation systems | EXISTING general mechanism |
| Model evaluation and benchmarking | EXISTING |
| Incident reporting | EXISTING |
| Independent model evaluation | EXISTING / ADAPTED |
| Versioned domain-scoped profile integrating validated user errors, independent AI evaluators, operational exposure, hard caps and lifecycle/authority integration | PROPOSED COMBINATION, pending prior-art research |
| UAIS-1700 | PROPOSED |

No novelty conclusion is made before external literature review.



## Safety Management System practice count

Core UAIS SMS remains 23 practices. UAIS-1700 adds `AITrustworthinessAndErrorManagementPractice` as a mandatory extension practice for UAIS-1700-conforming implementations rather than changing the core practice count.
