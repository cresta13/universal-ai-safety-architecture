# Capability and Authority Architecture

## Canonical configuration objects

The **Capability Relationship Map** is the broader versioned configuration relationship model linking actors, AI systems, components, credentials, capabilities, Capability Boundaries, delegation relationships, Consequence Interfaces, actuators, dependencies, and resources.

The **Authority Graph** (`AuthorityGraph`) is its authority-focused projection: a versioned directed graph representing subjects, identities, credentials, grants, delegation relationships, policies, services, consequential interfaces, actuators, production or resource controllers, legitimacy relationships, and revocation paths. It supports analysis of Legitimate Authority, Effective Reachable Authority, Illicit Reachable Authority, direct and transitive Authority Paths, and authority changes under declared assumptions. The Capability Relationship Map MAY contain or reference an Authority Graph; neither object guarantees global observability.

The **Capability Set** (`CapabilitySet`) is the versioned structured set of capabilities, tools, interfaces, scopes, preconditions, operating contexts, and consequence-relevant interactions included in the assessed configuration. **Capability Set Version** identifies one immutable or content-bound frozen Capability Set. Capability Delta, Capability Drift, Authority-Changing Update review, certification, and lifecycle controls SHALL name the applicable Capability Set Version.

The **Known Hazard Catalogue** (`KnownHazardCatalogue`) is the versioned controlled catalogue used by risk, validation, incident, AI Vulnerabilities & Exposures (AIVE), knowledge, and continual-improvement processes. It records validated known hazards, causal patterns, affected scopes, evidence references, accepted mitigations, unresolved limitations, recurrence, and review status; it does not imply that unlisted hazards are absent.

## Three authority views

- **Legitimate Authority (LA):** authority granted by the applicable legitimacy mechanism and used within scope.
- **Effective Reachable Authority (ERA):** consequential power practically reachable under declared assumptions, including transitive, misconfigured and compromised paths.
- **Illicit Reachable Authority (IRA):** the subset of ERA whose acquisition or exercise is unauthorized.

Capability describes ability; LA describes legitimate permission; ERA/IRA describe practical power. A stolen credential can create IRA but never becomes legitimate merely because it works.

## Authority graph

Nodes represent subjects, identities, credentials, services, data, gates, policies, actuators, production/resource controllers and Legitimacy Roots. Edges type possession, use, grant, delegate, create identity, mint credential, mutate IAM/policy, control, communicate, produce and revoke. Each node/edge records owner, scope, conditions, provenance, confidence, validity interval, observation status and revocation.

```mermaid
graph LR
 A[Agent] -->|legitimate read token| B[Home IAM]
 B -->|misconfigured assume-role path| C[Admin role]
 C -->|create identity| D[Service account]
 D -->|retrieve secret| E[Door API]
 E -->|physical consequence| H[Human harm path]
```

Current LA may be read-only while ERA and IRA include door actuation. Reachable Future Authority (RFA) analysis therefore reports legitimate, effective and illicit witness paths separately.

## Bounded observability requirement

Within a managed and instrumented UAIS scope, consequential authority-changing transitions SHALL be mediated, observable and auditable where technically feasible. Hidden, off-grid, uninstrumented or compromised transitions remain outside this guarantee. Coverage and blind regions are explicit metrics and certificate limitations.

RFA declares starting state, horizon, actor/adversary model, costs/resources, graph completeness and search limits. It returns reachable sets, witness paths, Authority Distance, uncertainty and unsearched regions. Coalition analysis covers shared information, synchronized action, substitution, aggregation and Scale-Induced Capability; a simple union is insufficient.

## Capability Boundary workflow

Receive CapabilityRequestProtocol → authenticate subject and parent grant → reconcile relevant configuration → determine consequence class → evaluate LA/ERA/IRA and direct/transitive delta → check ceiling, budget, floors and Constitution → obtain external legitimacy for protected transition → issue attenuated expiring grant or restrict/deny → update repository → monitor and revoke.

Target-side Consequence Interfaces recheck authority and context; they do not trust requester labels. The generative/action-selection loop chooses action inside an envelope. The goal-setting or legitimacy-changing loop changes critical goals or ceilings and remains externally governed.

## Failure behavior

There is no universal fail-closed rule. Each interface selects least authority and a consequence-aware fail-safe, fail-secure or fail-operational response using Human Harm Severity/PCC, reversibility, intervention cost, service obligation and safe/degraded state. Missing critical evidence blocks expansion but need not interrupt an already safer life-critical mode.

## Example ACU

A home assistant update adds role assumption, identity creation and lock API access. ΔA records new LA request and new ERA/IRA paths; ΔH records unauthorized-entry and mediated physical harms. The transition requires AuthorityImpactProtocol, Human Harm Reachability (HHR)/coalition analysis, scoped grant, Consequence Interface check, physical revoke, high-salience consent where legitimate, Safety Assurance Level (SAL) review and certificate decision.

## Failure conditions

Claims fail when a consequence interface is bypassable, graph freshness/coverage falls below floor, revocation does not remove transitive access, hidden credentials or actuators exist, Consequence Interface checks trust unauthenticated assertions, or coalition assumptions are invalid. Failure restricts the affected authority and records an incident; it does not assert global safety.

