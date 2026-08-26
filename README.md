# Universal AI Safety Architecture (UAIS)

**Pre-standard research architecture — Draft 1.0 Candidate 3 / Public Review**

**Assume unlimited intelligence. Limit autonomous authority.**

UAIS constrains consequential authority and consequence pathways rather than trying to control intelligence as such.

This repository publishes a public Draft 1.0 Candidate for technical and policy review. It is not an adopted standard, certification scheme, compliance claim, or guarantee of AI safety.

[Visual explainer](https://cresta13.github.io/universal-ai-safety-architecture/) · [Manifesto](spec/01_MANIFESTO.md) · [Full Technical Manifesto](spec/01A_FULL_TECHNICAL_MANIFESTO.md) · [Master Index](spec/00_MASTER_INDEX.md) · [Roadmap](ROADMAP.md) · [Known Limitations](KNOWN_LIMITATIONS.md)

## What UAIS controls

```mermaid
flowchart LR
  A[Actor / Capability Request] --> B{Capability Boundary}
  LA[Legitimate Authority + Authority Ceiling] --> B
  R[Effective / Illicit Reachability + Reachable Future Authority (RFA)] --> B
  HC[Human Harm Reachability (HHR) + coalition analysis] --> B
  SE[Safety Evidence] --> I[Deterministic Evidence Verifier]
  I --> B
  B -->|authorized, scoped, fresh evidence| C[Bounded Authorized Envelope]
  B -->|missing authority or evidence| D[Restrict / Review]
  C --> E[Consequence Interface]
  E --> F[Digital / Physical Consequence]
```

Deterministic Evidence Verifier (DEV) verifies bounded evidence properties and provenance; it does not establish ultimate external-world truth. This limitation includes clinical, factual, and physical-world truth claims.

UAIS separates:

| Dimension | Question |
|---|---|
| Capability | What can the system do? |
| Legitimate Authority | What has been granted by the applicable legitimacy mechanism? |
| Effective Reachability | What consequential power is practically reachable under stated assumptions? |
| Illicit Reachability | Which reachable paths are unauthorized and must be contained or remediated? |
| Consequence | What protected interests can be affected? |
| Evidence | What is known, fresh, independent, and verifiable? |
| Human Sovereignty | Can authorized humans still intervene outside the AI path? |
| Physical Sovereignty | Does the system still depend on human-controlled energy, compute, matter, manufacturing, maintenance, repair, logistics, or other critical resources? |

Actor-agnostic does not mean actor-blind. The protected boundary follows consequential capability; authorization may still depend on identity, role, authentication, purpose, context, trustworthiness, and legitimate mandate. No actor category may bypass the boundary merely by changing its label.

## Repository map

| Area | Start here |
|---|---|
| Architecture overview | [Master Index](spec/00_MASTER_INDEX.md) |
| Terms and identifiers | [Normative Vocabulary](spec/03_NORMATIVE_VOCABULARY.md), [Global Name Registry](spec/GLOBAL_NAME_REGISTRY.md) |
| Threats and boundaries | [Threat Model](spec/02_THREAT_MODEL.md), [Known Limitations](KNOWN_LIMITATIONS.md) |
| Classification and evidence | [Classification Model](spec/04_CLASSIFICATION_MODEL.md), [Safety Assurance Model](spec/06_SAFETY_ASSURANCE_MODEL.md) |
| Authority, Guardian, physical sovereignty | [Authority Architecture](spec/08_CAPABILITY_AUTHORITY_ARCHITECTURE.md), [Guardian](spec/09_GUARDIAN_ARCHITECTURE.md), [Stage II](spec/12_STAGE_II_PHYSICAL_SOVEREIGNTY.md) |
| Trustworthiness and error evidence | [Safety Assurance Model](spec/06_SAFETY_ASSURANCE_MODEL.md), [UAIS-1700](spec/17_UAIS_STANDARDS_FAMILY.md) |
| Public review | [Contributing](CONTRIBUTING.md), [Issue templates](.github/ISSUE_TEMPLATE) |

## Trustworthiness and error evidence

UAIS includes a proposed AI Trustworthiness & Error Evidence layer. It separates profile status from rating level, uses domain-specific scoring policies, preserves historical error records, and applies hard rating caps for critical errors, stale evidence, weak independence, disagreement, and version carryover.

Trustworthiness evidence can constrain delegated use. Insufficient, degraded, stale, or disputed evidence may trigger pre-authorized restrictions. A higher rating never raises the Authority Ceiling. A rating cannot create authority, waive safety controls, or certify general safety.

## Policy and standards relevance

UAIS explores implementation pathways through voluntary standards, procurement requirements, independent evaluation, certification / assurance, post-deployment reporting, lifecycle governance, high-consequence capability boundaries, and interoperable evidence.

Current policy-oriented work is focusing on AI Trustworthiness & Error Evidence as a narrower, potentially implementable module within the broader UAIS architecture.

The standards crosswalk identifies candidate conceptual overlap and research relationships. It is not a clause-level compliance statement and does not establish conformance with any external standard.

## What comes next

UAIS is moving from architecture drafting toward:
1. specification hardening,
2. formal schemas,
3. reference prototypes,
4. adversarial evaluation,
5. domain pilots,
6. standards and procurement translation,
7. independent external review.

See [ROADMAP.md](ROADMAP.md).

## Citation

Use [CITATION.md](CITATION.md) and cite the specific version reviewed.

## Licensing and use

All rights are reserved by Anna Simakova. This repository is available for reading, review, citation, linking, and public discussion. Any other use or reuse requires prior written permission from the author. See [NOTICE.md](NOTICE.md).

## Author

**Anna Simakova**  
AI Researcher • System Architect • Product Builder

- Website: https://annasimakova.tilda.ws/
- LinkedIn: https://www.linkedin.com/in/cresta13
- GitHub: https://github.com/cresta13
