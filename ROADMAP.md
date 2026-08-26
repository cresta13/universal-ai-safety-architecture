# Roadmap

UAIS is moving from architecture drafting toward specification hardening, formal schemas, reference prototypes, adversarial evaluation, domain pilots, standards translation, and external review.

## Phase 1 — Specification hardening

Planned work:
- resolve remaining term collisions and undefined aliases;
- complete canonical object definitions;
- sharpen SHALL / SHOULD / MAY boundaries;
- add traceable requirement families without changing the Draft Candidate framing;
- keep open research problems visibly separated from implementable requirements.

## Phase 2 — Formal schemas and conformance artifacts

Planned work:
- Authority Graph schema;
- Capability Relationship Map schema;
- Human Harm Reachability representation;
- Coalition Reachable Authority composition model;
- Coalition Physical Envelope research model;
- Capability Delta schema;
- Authority Delta schema;
- Hazard Delta schema;
- protocol message schemas;
- machine-readable schemas for Safety Passport, AHCD, Safety Delta Report, Trustworthiness Profile, Rating Change Event, and AI Vulnerabilities & Exposures (AIVE) records;
- conformance vectors and negative tests;
- policy-version migration examples;
- evidence-freshness and evaluator-independence examples.

## Phase 3 — Reference prototypes

Planned reference prototypes:
- authority graph and Reachable Future Authority analyzer;
- Capability Boundary / Consequence Interface demonstrator;
- Authority-Changing Update (ACU) delta pipeline;
- Manual Sovereignty Controller demonstrator;
- Safety Passport generator;
- Evidence-Carrying Alert verifier;
- Trustworthiness Profile and rating-cap calculator;
- AI Error Report workflow;
- AIVE intake/disclosure prototype;
- registry proof-of-concept.

All prototypes should be clearly labeled: **REFERENCE / RESEARCH PROTOTYPE — NOT SAFETY CERTIFIED**.

## Phase 4 — Evaluation and adversarial testing

Planned work:
- hidden scenario suites;
- metric gaming tests;
- evaluator-correlation tests;
- Sybil/report manipulation tests;
- version-laundering tests;
- benchmark-leakage tests;
- coalition/emergent capability tests;
- failure injection;
- privacy leakage tests;
- independent red-team review;
- post-incident learning loops.

## Phase 5 — Domain application profiles

Planned pilots or case studies:
- low-consequence conversational assistant;
- smart speaker / connected consumer device;
- cloud IAM agent;
- medical recommendation AI;
- autonomous physical system / near miss;
- high-consequence industrial or critical-infrastructure workflow.

These are planned profiles, not claims that UAIS is already validated for those domains.

## Phase 6 — Standards and policy translation

Planned work:
- deeper NIST / ISO / IEC / IEEE / sector standards crosswalk;
- identify genuine overlap versus UAIS-specific proposals;
- voluntary-standard profile for AI Trustworthiness & Error Evidence;
- procurement-ready evidence requirements;
- sample procurement clauses;
- independent-evaluation requirements;
- post-deployment error-reporting model;
- certification / assurance research;
- stakeholder workshops;
- policy memo;
- regulatory and procurement adoption-path analysis.

Current policy-oriented work is focusing on AI Trustworthiness & Error Evidence as a narrower, potentially implementable module within the broader UAIS architecture.

## Phase 7 — External review and publication

Planned work:
- named external reviewers where permission is given;
- public issue-based technical review;
- versioned changelog;
- stable citation package;
- archival publication / DOI where appropriate;
- expanded visual website and public architecture diagrams;
- research papers / technical notes for individual open problems;
- Draft 1.0 release only after acceptance criteria are met.
