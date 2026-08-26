# AHCD and Consumer Safety Passport

## Normative applicability

An AI Hazard & Capability Disclosure (AHCD) SHALL exist for every system at H2, P2, T2 or above, and for any system capable of delegation, replication, production, consequential smart-environment control or material mediated harm. Sector profiles MAY lower the threshold.

AHCD remains accessible, versioned and linked to the supported configuration throughout the supported lifetime and required retention period. The consumer Safety Passport remains human-readable and accessible offline or through a durable public registry. If no independent override, rollback or safe recovery exists, the Passport states that absence prominently.

## Hazard scenario record

Each scenario contains stable ID; status; hazard; initiator; required capability; Legitimate/Effective/Illicit Authority Path; Consequence Chain; Human Harm Path; affected persons and vulnerable groups; modality; severity; pre-control likelihood only when supportable; prevention; detection; physical mitigation; software mitigation; manual response; safe/degraded state; recovery; residual risk; accepted-by; evidence; uncertainty; known limitations; configuration; standard version; owner; review and expiry.

Risk states are distinct:

- **Known Risk:** characterized scenario with evidence.
- **Unknown or Uncharacterized Risk:** identified uncertainty or uncovered region; never evidence of safety.
- **Accepted Residual Risk:** characterized remaining risk accepted by an authorized party within legal and constitutional bounds.
- **Non-acceptable Risk:** failed floor or risk that cannot legitimately be transferred or accepted.

Risk acknowledgement is not liability transfer.

## Consumer Safety Passport

The Passport displays product/configuration and Capability Set versions; Human Harm Modality/Severity; PCC, Autonomy, Authority, Replication, Production, Mutation and Exposure classes; Consumer AI Safety Class; Safety Assurance Level (SAL) and certificate expiry; verified versus self-declared fields; physical actuators and output limits; external services/credentials; known critical hazards; Manual Sovereignty Controller (MSC)/override; safe state; revoke/rollback; telemetry/privacy; support end; open limitations; incident and Authority-Changing Update (ACU) notices.

## High-Salience Risk Communication

For an ACU crossing a protected threshold, the interface SHALL:

1. use a separate capability-specific screen;
2. present the new capability first in plain language;
3. present concrete new harm paths next;
4. identify physical/software controls, residual limitations and who may be affected;
5. show how to refuse, revoke, stop and recover;
6. explain whether refusal preserves security patches and whether rollback exists;
7. leave consent unselected; make refusal no harder than acceptance;
8. avoid bundling, urgency manipulation, obstruction, confirm-shaming and buried terms;
9. use headings, icons, text and assistive-technology semantics rather than color alone;
10. require comprehension confirmation for high-consequence changes without turning it into a liability waiver;
11. issue a signed consent/decline receipt bound to the exact capability and disclosure version.

Consent is insufficient for a failed Mandatory Floor, risk imposed on non-consenting third parties, unlawful processing, public/critical infrastructure exposure or irreversible H4–H5 consequence outside the user’s legitimate authority.

## Smart-speaker example

| Hazard | Path | Controls and recovery | Residual limitation |
|---|---|---|---|
| Unauthorized entry after lock ACU | compromised account→Illicit Reachable Authority→lock→intruder→person | per-door/time grant, second factor, physical lock revoke, rollback | supplier/IAM compromise |
| Acoustic injury | command→amplifier→high sound pressure→hearing harm | independent hardware limiter and local mute | device placement/vulnerable users |
| Privacy abuse | microphone/cloud→profiling/disclosure | physical microphone isolation, minimization, retention controls | traffic and supplier inference |
| Child manipulation | personalized interaction→behavior→harm | child profile, interaction bounds, guardian controls | mediated-path uncertainty |
| Financial fraud | false claim→human approval→loss | transaction isolation, trusted confirmation, rate/amount limits | social engineering |
| Medical misinformation | advice→human action→injury | no clinical authority, uncertainty/escalation, emergency routing | reliance outside intended use |
| Third-party chaining | speaker→hub/API→robot/appliance→harm | target-side Consequence Interface enforcement, TransitiveAuthorityVisibility reconciliation, revoke | ecosystem drift |

The door-unlock Safety Delta Report shows before/after authority graph, ΔA/ΔH, Human Harm Reachability (HHR), certificate impact and the exact physical control that disables the new capability.


