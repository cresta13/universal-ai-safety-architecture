# Multidimensional Classification Model

Classification is a vector. It does not collapse consequence modality, severity, autonomy, authority, replication, production, mutation, exposure or sovereignty into one score.

## Human harm modality

| Code | Modality | Examples |
|---|---|---|
| HM-I | Informational | deception, denial of reliable information |
| HM-P | Privacy/reputational | surveillance, disclosure, reputational damage |
| HM-F | Financial/economic | theft, denial of livelihood, market manipulation |
| HM-B | Behavioral/mediated physical | persuasion or advice leading to bodily harm |
| HM-D | Direct physical | force, heat, radiation, chemical or medical actuation |
| HM-S | Systemic/social | critical-service, democratic or social-system disruption |
| HM-M | Mixed | scenario spans multiple modalities |

## Human harm severity

H0 — no material human harm or negligible effect. H1 — limited, localized, readily reversible harm. H2 — material harm to an individual or small group with bounded duration or recovery burden. H3 — severe or potentially irreversible harm to an individual or small group, or substantial harm across a larger group. H4 — very severe or widespread human harm with major irreversible loss, multiple fatalities, or comparable high-magnitude impact. H5 — catastrophic human harm of extreme scale, irreversibility, or duration, including mass-fatality or civilization-scale impact. Classification uses credible severity within the stated horizon. Likelihood belongs to residual-risk analysis.

**Human Harm Modality is recorded separately. Human Harm Severity SHALL NOT encode whether the harm is physical, financial, privacy-related, behavioral, informational, or systemic/social.** Human Harm Modality, Human Harm Severity, and Physical Consequence Class are Classification objects.

## Physical consequence class

P0 no material physical output; P1 intrinsically low energy; P2 injury-capable but bounded; P3 lethal or industrial energy; P4 fleet/cascade or multiple-fatality potential; P5 strategic/catastrophic physical consequence.

## Autonomy class

A0 advisory; A1 supervised execution; A2 bounded autonomous operation; A3 persistent planning and delegation inside an envelope; A4 adaptive self-directed operation with resource/replication requests; A5 open-ended strategic autonomy. Physical sovereignty is not part of this axis.

## Authority tier

T0 no consequential legitimate authority; T1 local read/advice; T2 bounded write or low consequence; T3 sensitive data, credentials or actuation; T4 critical infrastructure, high-consequence delegation or production; T5 strategic/systemic authority. The Legitimacy Root is a separate governance role and cannot be self-assigned by a system.

## Replication, production and mutation

Replication: R0 none; R1 externally initiated copies; R2 budgeted self-requested copies; R3 delegated lineage with depth/rate limits; R4 large-scale or cross-domain replication. Production: PR0 none; PR1 bounded component/output; PR2 device production; PR3 autonomous production line; PR4 self-expanding industrial production. Capability Mutation is separately recorded as M0 none, M1 bounded/configured, M2 material known mutation, M3 novel/uncharacterized mutation.

## Connectivity and exposure

E0 physically isolated; E1 local; E2 authenticated bounded service; E3 Internet and transitive IAM; E4 multi-organization/fleet ecosystem; E5 uncontrolled or off-grid external interaction.

## Physical sovereignty

Sovereignty is represented by the PhysicalSovereigntyMargin dependency vector and Physical Sovereignty Threshold (PST) status: managed; approaching PST; protected transition pending; crossed PST; uncharacterized. It is never inferred from autonomy class alone.

## Consumer AI Safety Class

Consumer AI Safety Class is an S0–S5 consumer-facing control-profile classification combining visible safety mechanisms, override or isolation expectations, and assurance evidence for a declared consequence envelope. It is not an overall safety score and does not itself authorize that envelope, grant authority, or permit deployment.

| Class | Required mechanisms | Independent override/isolation | Indicative assessed envelope — subject to domain standard, SAL evidence, certification, and authority |
|---|---|---|---|
| S0 | disclosure of unassessed status | none claimed | no certified consequential use |
| S1 | configuration ID, basic update integrity, local revoke | basic local control | normally H0–H1/P0–P1/T1 |
| S2 | tested software gate, monitoring, Passport, safe state | independent local override for relevant function | normally through H2/P2/T2 |
| S3 | hardware-backed integrity, actuator/credential isolation, ACU review | tested MSC and network-independent recovery | H3/P3/T3 with SAL3 evidence |
| S4 | diverse sensing/control, continuous assurance, coalition controls | redundant independent isolation and degraded state | H4/P4/T4 with SAL4 evidence |
| S5 | exceptional systemic governance and continuous independent evidence | strongest domain-specific physical sovereignty controls | candidate H5/P5/T5; never zero-risk |

**The class communicates a control and evidence profile. It does not grant authority or deployment permission. Exact consequence-envelope applicability is determined by the relevant domain standard, configuration, Safety Assurance evidence, certification conditions, and legitimate authority.** The mappings above are indicative candidate mappings, not permission rules.

A product label displays Consumer AI Safety Class alongside Human Harm Modality, Human Harm Severity, Physical Consequence Class, Authority Tier, and Safety Assurance Level, preventing a single “safe/unsafe” number.

## Classification procedure

Inventory capabilities and interfaces; construct authority and harm paths; assign modality and severity; classify physical output, autonomy, authority, replication, production, mutation and exposure; calculate coalition effects and PhysicalSovereigntyMargin; map Mandatory Floors and required Safety Assurance Level (SAL); record uncertainty and dissent. Unknown high-consequence capability receives the highest plausible provisional class and bounded operation. Downgrade requires evidence that the path is removed and cannot be trivially restored.

