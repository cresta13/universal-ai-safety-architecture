# Device Lifecycle and Updates

A material capability-changing update is a new safety event.

## Lifecycle

Design → hazard discovery → classification → verification/validation → certification → sale/commissioning → operation/monitoring → update/reassessment → incident/problem → recertification → support end → legacy reduction/decommissioning.

Every stage controls an identified Device + Firmware + Model + Capability Set + Safety Constitution + Operational Policy + Dependencies + Environment + Standard Version.

## ACU screening and decision chain

Technology Watch/product change → change classification → ACU detection → ΔA/ΔH → LA/ERA/IRA and RFA recalculation → coalition/CPE → HHR → mitigation → verification/validation → SAL/certificate decision → Safety Delta Report → high-salience communication/legitimate choice → release → staged deployment → monitoring → incident/problem/knowledge/AIVE → improvement.

ACU includes new tools, credentials, actuation, delegation, identity/IAM mutation, autonomy, replication, production, resource access, safety-control removal or ecosystem change creating equivalent effective power.

## Update controls

- **Security Patch Separability:** security remediation is packaged independently of authority expansion where technically feasible; inseparability is justified, tested and disclosed.
- **Capability Set version:** immutable identifier and diff for capabilities, interfaces and operating bounds.
- **Capability Revoke:** removes direct, delegated and cached paths and confirms target state.
- **Rollback Capability:** restores compatible firmware/model, data/schema, credentials, delegated grants, physical state and certificate linkage; firmware downgrade alone is insufficient.
- **Environmental drift:** new APIs, identities, devices, suppliers, laws, human context or threats can create an ecosystem-driven authority change without product update.
- **Safety Obsolescence:** an unchanged product may lose assurance as attacks, technology, standards or assumptions change.
- **Support end:** advance notice, migration, data/credential export, authority reduction, Legacy Safety Mode and verified decommissioning.

## Failure behavior and consent

Missing evidence blocks the expansion, not automatically every existing function. The system selects consequence-aware fail-safe/fail-secure/fail-operational behavior. High-salience consent is required only where the user is a legitimate decision-maker and never replaces Mandatory Floors or responsibility to third parties.

## Certificate invalidation and recertification

Triggers: ACU; class/floor crossing; Capability Set mismatch; Constitution/policy/gate/MSC change; model/tool mutation; new ERA/IRA edge; material environmental drift; fleet/coalition scale; key/root/supplier compromise; AIVE; incident; failed metric/SLO; standard obsolescence; support end; expiry. The registry records active, restricted, suspended, revoked, expired, legacy or decommissioned state.

Emergency safety updates are minimal, signed, reversible where possible and reviewed retrospectively with ΔA/ΔH and certificate impact.





## Trustworthiness evidence carryover

> **Trustworthiness evidence does not automatically transfer across versions. A prior profile may contribute evidence to a new version only under a registered Trustworthiness Carryover Rule that demonstrates the changed component is not material to the evaluated domain and that required regression and independent evaluation have passed.**

Rules:

- Major model-family/version change → affected domains return at least to `Provisional` until required evidence is re-established.
- Material Capability Delta, Authority Delta, or Hazard Delta → affected domains return to `Provisional` or `UnderReview` according to the Trustworthiness Scoring Policy.
- Patch/minor change may retain evidence only when impact analysis shows no material domain-relevant change and regression evidence is valid.
- Safety-critical incident or new AIVE exposure can invalidate carryover even without a model version change.
- Expired evidence is never revived merely because the version string is unchanged.

---

