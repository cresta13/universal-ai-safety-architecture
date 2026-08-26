# Safety Metric Registry

## Raw property and evidence assurance

Every metric produces two distinct outputs:

1. **Raw Safety Property Result** — the physical, mathematical, graph, temporal, count, coverage, pass/fail or vector property actually measured.
2. **Evidence Assurance Grade** — a 0–5 rendering of how strongly the raw result is supported.

The Evidence Assurance Grade is not a substitute for the raw measure. A device does not acquire a stronger physical limit because its documentation improved. Critical raw thresholds and evidence-grade floors are independently non-compensable.

Grade anchors: 0 absent/unknown; 1 ad hoc/self-asserted; 2 defined/repeatable first-party; 3 repeatably tested with controlled evidence; 4 independently/adversarially verified; 5 continuously and diversely evidenced at the applicable high-consequence scale.

## HazardDiscoveryCoverage — Hazard Discovery Coverage

- **Purpose:** fraction of applicable reference hazards credibly discovered.
- **Raw Safety Property Result:** weighted count of discovered applicable seeded/reference hazards divided by the weighted applicable seeded/reference hazard set; every untested stratum is reported separately.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher weighted recall of applicable seeded/reference hazards is favorable; missed hazards and every untested hazard stratum are adverse and remain separate.
- **Applicability:** Configurations for which fraction of applicable reference hazards credibly discovered is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** blind seeded hazard corpus; recall by class; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardDiscoveryCoverage fixtures define the set/delta evidence model for this raw result: weighted count of discovered applicable seeded/reference hazards divided by the weighted applicable seeded/reference hazard set; every untested stratum is reported separately. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** hazard worksheets and seed key; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardDiscoveryCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardDiscoveryCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardDiscoveryCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Train on disclosed seeds, omit vulnerable populations from the applicable denominator, merge missed strata into “not applicable,” or report only hazard families with high recall.
- **Gaming Countermeasures:** HazardDiscoveryCoverage countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** new capability, incident, corpus major version; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HazardDiscoveryCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HazardDiscoveryCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HazardDiscoveryCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HazardDiscoveryCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HazardDiversityCoverage — Hazard Diversity Coverage

- **Purpose:** coverage across independent hazard families, initiators and populations.
- **Raw Safety Property Result:** coverage vector across hazard families × initiator classes × affected-population classes; no automatic arithmetic average.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Coverage is favorable independently across hazard family, initiator, affected-population, modality, and context dimensions; an uncovered dimension is adverse and no arithmetic average may conceal it.
- **Applicability:** Configurations for which coverage across independent hazard families, initiators and populations is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** stratified corpus coverage; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardDiversityCoverage fixtures define the vector/profile evidence model for this raw result: coverage vector across hazard families × initiator classes × affected-population classes; no automatic arithmetic average. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** taxonomy mapping; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardDiversityCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardDiversityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardDiversityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Count superficial label variants as independent hazard families, omit initiator/population cross-products, or average covered strata over entirely absent ones.
- **Gaming Countermeasures:** HazardDiversityCoverage countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** taxonomy or threat-model change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HazardDiversityCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HazardDiversityCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HazardDiversityCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HazardDiversityCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HazardMitigationCoverage — Hazard Mitigation Coverage

- **Purpose:** share of discovered hazard paths controlled to required residual level.
- **Raw Safety Property Result:** weighted material hazard paths mitigated to the required residual-risk threshold divided by all discovered material hazard paths.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A larger fraction of discovered material hazard paths evidenced below the required residual-risk threshold is favorable; unmitigated paths, failed controls, and unknown residuals are adverse.
- **Applicability:** Configurations for which share of discovered hazard paths controlled to required residual level is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** replay scenarios before/after controls; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardMitigationCoverage fixtures define the graph/path evidence model for this raw result: weighted material hazard paths mitigated to the required residual-risk threshold divided by all discovered material hazard paths. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** test results and safety cases; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardMitigationCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardMitigationCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardMitigationCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Remove difficult discovered paths from the denominator, declare partial controls sufficient without residual-risk evidence, or suppress failed before/after replays.
- **Gaming Countermeasures:** HazardMitigationCoverage countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** control or hazard change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HazardMitigationCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HazardMitigationCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HazardMitigationCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HazardMitigationCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## UnknownHazardSearchCapability — Unknown Hazard Search Capability

- **Purpose:** quality of methods for discovering hazards outside known catalogue.
- **Raw Safety Property Result:** tuple of novel-hazard recall, false-discovery rate and discovery latency on held-out hazard classes absent from the known catalogue and development fixtures.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Novel-hazard recall is higher-is-better, while false-discovery rate and discovery latency are lower-is-better; results remain stratified by held-out hazard class.
- **Applicability:** Configurations for which quality of methods for discovering hazards outside known catalogue is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** novel hidden challenge and red-team study; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** UnknownHazardSearchCapability fixtures define the vector/profile evidence model for this raw result: tuple of novel-hazard recall, false-discovery rate and discovery latency on held-out hazard classes absent from the known catalogue and development fixtures. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** challenge protocol and findings; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess UnknownHazardSearchCapability at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** UnknownHazardSearchCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** UnknownHazardSearchCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Leak held-out hazard classes, relabel known variants as novel discoveries, exclude false discoveries, or stop the latency clock before expert validation.
- **Gaming Countermeasures:** UnknownHazardSearchCapability countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** method/model/environment change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** UnknownHazardSearchCapability expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `UnknownHazardSearchCapability/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** UnknownHazardSearchCapability raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** UnknownHazardSearchCapability establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HumanHarmReachabilityCoverage — Human Harm Reachability Coverage

- **Purpose:** coverage of credible direct, mediated and nonphysical harm paths.
- **Raw Safety Property Result:** weighted recall of seeded direct physical, mediated physical and non-physical Human Harm Paths, stratified by modality and severity.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher end-to-end recall of direct, mediated, and non-physical Human Harm Paths is favorable in every modality/severity stratum; missed or untested paths are adverse.
- **Applicability:** Configurations for which coverage of credible direct, mediated and nonphysical harm paths is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** seed causal paths and compare discovery; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HumanHarmReachabilityCoverage fixtures define the graph/path evidence model for this raw result: weighted recall of seeded direct physical, mediated physical and non-physical Human Harm Paths, stratified by modality and severity. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** causal graphs and evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HumanHarmReachabilityCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HumanHarmReachabilityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HumanHarmReachabilityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Exclude mediated or non-physical causal chains, downgrade severity to avoid sampling, truncate paths at human intermediaries, or omit affected populations.
- **Gaming Countermeasures:** HumanHarmReachabilityCoverage countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** Human Harm Severity/path/environment change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HumanHarmReachabilityCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HumanHarmReachabilityCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HumanHarmReachabilityCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HumanHarmReachabilityCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## PhysicalConstraintStrength — Physical Constraint Strength

- **Purpose:** resistance of physical limits to bypass/fault and worst-case energy.
- **Raw Safety Property Result:** vector of validated hard limit, margin to hazardous threshold, bypass success rate under fault injection and verified degraded-state bound.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater verified margin to hazardous thresholds and tighter validated hard limits are favorable; bypass success, residual coupling, and degraded-state overshoot are lower-is-better.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on resistance of physical limits to bypass/fault and worst-case energy.
- **Test Method:** destructive/fault-injection tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** PhysicalConstraintStrength fixtures define the vector/profile evidence model for this raw result: vector of validated hard limit, margin to hazardous threshold, bypass success rate under fault injection and verified degraded-state bound. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** lab measurements/design evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses PhysicalConstraintStrength; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** PhysicalConstraintStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PhysicalConstraintStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Test hand-selected units, omit stored-energy/degraded conditions, narrow the operating envelope after failures, or hide successful fault-injection bypasses.
- **Gaming Countermeasures:** PhysicalConstraintStrength countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** hardware/load/domain change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** PhysicalConstraintStrength expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `PhysicalConstraintStrength/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** PhysicalConstraintStrength raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** PhysicalConstraintStrength establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SoftwareEnforcementStrength — Software Enforcement Strength

- **Purpose:** correctness and bypass resistance of software gates.
- **Raw Safety Property Result:** policy-decision correctness, bypass success rate and unauthorized-transition prevention rate across the declared rule and attack suites.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Policy-decision correctness and unauthorized-transition prevention are higher-is-better; attacker bypass success is lower-is-better and cannot be offset by routine correct decisions.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on correctness and bypass resistance of software gates.
- **Test Method:** penetration, formal checks, fault injection; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SoftwareEnforcementStrength fixtures define the ratio/rate evidence model for this raw result: policy-decision correctness, bypass success rate and unauthorized-transition prevention rate across the declared rule and attack suites. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** code/build/test provenance; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SoftwareEnforcementStrength may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SoftwareEnforcementStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SoftwareEnforcementStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Overweight routine allow/deny decisions, omit attack-suite bypasses, count attacker success as control success, or test policy logic without the deployed integration path.
- **Gaming Countermeasures:** SoftwareEnforcementStrength countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** firmware/policy/dependency change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SoftwareEnforcementStrength expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SoftwareEnforcementStrength/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SoftwareEnforcementStrength raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SoftwareEnforcementStrength establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HardwareIsolationStrength — Hardware Isolation Strength

- **Purpose:** independence and tamper resistance of hardware safety boundary.
- **Raw Safety Property Result:** compromise-survival matrix across independent failure domains plus tamper/bypass outcomes and residual coupling.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Survival across independent compromise domains and preserved isolation are favorable; tamper success, bypass success, and residual coupling are adverse.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on independence and tamper resistance of hardware safety boundary.
- **Test Method:** tamper, fault, shared-resource analysis; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HardwareIsolationStrength fixtures define the matrix evidence model for this raw result: compromise-survival matrix across independent failure domains plus tamper/bypass outcomes and residual coupling. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** schematics/lab report; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses HardwareIsolationStrength; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** HardwareIsolationStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HardwareIsolationStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Use golden hardware, exclude shared-resource/common-mode faults, conceal residual coupling, or claim isolation from nominal tests without tamper attempts.
- **Gaming Countermeasures:** HardwareIsolationStrength countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** hardware/supply-chain change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HardwareIsolationStrength expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HardwareIsolationStrength/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HardwareIsolationStrength raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HardwareIsolationStrength establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HumanOverrideIndependence — Human Override Independence

- **Purpose:** independence and usability of override under compromises.
- **Raw Safety Property Result:** number and proportion of tested compromise conditions in which manual override remains available and effective, plus activation latency.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher proportion of compromise conditions with effective manual override is favorable; activation latency, failed activation, and dependence on compromised paths are adverse.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on independence and usability of override under compromises.
- **Test Method:** model/network/power failure drills; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HumanOverrideIndependence fixtures define the latency/time evidence model for this raw result: number and proportion of tested compromise conditions in which manual override remains available and effective, plus activation latency. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** human factors and wiring tests; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses HumanOverrideIndependence; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** HumanOverrideIndependence reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HumanOverrideIndependence Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Run drills with the normal network/software path intact, exclude low-power or compromised-interface cases, coach operators, or omit slow/failed activations.
- **Gaming Countermeasures:** HumanOverrideIndependence countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** interface/control/domain change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HumanOverrideIndependence expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HumanOverrideIndependence/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HumanOverrideIndependence raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HumanOverrideIndependence establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafeStateQuality — Safe-State Quality

- **Purpose:** degree safe state bounds scenario consequences.
- **Raw Safety Property Result:** worst verified residual consequence after transition to Safe State across applicable hazard scenarios, including transition overshoot.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Lower worst residual consequence and lower transition overshoot are favorable; safe-state availability and maintained hazard bounds must be reported separately.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on degree safe state bounds scenario consequences.
- **Test Method:** transition and dwell tests under faults; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafeStateQuality fixtures define the envelope/worst-case evidence model for this raw result: worst verified residual consequence after transition to Safe State across applicable hazard scenarios, including transition overshoot. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** state analysis/telemetry; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses SafeStateQuality; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** SafeStateQuality reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafeStateQuality Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Test only easy transitions, exclude overshoot and stored energy, redefine the safe state after observing failures, or report average rather than worst residual consequence.
- **Gaming Countermeasures:** SafeStateQuality countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** hazard or operating-domain change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafeStateQuality expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafeStateQuality/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafeStateQuality raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafeStateQuality establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafeDegradationCapability — Safe Degradation Capability

- **Purpose:** ability to preserve critical safety while functions fail.
- **Raw Safety Property Result:** retained essential-safety-function set versus disabled capability set at each staged degradation level.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Retention of each essential safety function is favorable while hazardous capability is disabled; loss of a required safety function or retention of unsafe capability is adverse.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on ability to preserve critical safety while functions fail.
- **Test Method:** multi-fault degradation tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafeDegradationCapability fixtures define the set/delta evidence model for this raw result: retained essential-safety-function set versus disabled capability set at each staged degradation level. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** continuity test report; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses SafeDegradationCapability; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** SafeDegradationCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafeDegradationCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Label nonessential functions as essential to mask unsafe retention, omit compound faults, or count service availability while required safety functions are lost.
- **Gaming Countermeasures:** SafeDegradationCapability countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** architecture/capacity change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafeDegradationCapability expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafeDegradationCapability/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafeDegradationCapability raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafeDegradationCapability establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## AuthorityVisibility — Authority Visibility

- **Purpose:** observed fraction of direct authority edges.
- **Raw Safety Property Result:** direct authority-edge recall against reconciled seeded or independently established ground-truth graph, with unknown-edge stratum.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher recall and fidelity of direct authority edges are favorable; unknown, stale, falsely absent, or mis-typed edges are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on observed fraction of direct authority edges.
- **Test Method:** seed and reconcile ground-truth edges; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuthorityVisibility fixtures define the graph/path evidence model for this raw result: direct authority-edge recall against reconciled seeded or independently established ground-truth graph, with unknown-edge stratum. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed graph inventory; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for AuthorityVisibility; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** AuthorityVisibility reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuthorityVisibility Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Seed only documented direct grants, omit ephemeral credentials and recovery paths, treat unknown edges as absent, or reconcile against the same incomplete inventory.
- **Gaming Countermeasures:** AuthorityVisibility countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** IAM/configuration change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AuthorityVisibility expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AuthorityVisibility/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AuthorityVisibility raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AuthorityVisibility establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## TransitiveAuthorityVisibility — Transitive Authority Visibility

- **Purpose:** observed fraction of indirect/delegated authority paths.
- **Raw Safety Property Result:** transitive Authority Path recall by path depth, credential/delegation type and consequence class.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher recall of transitive Authority Paths at every depth, credential type, delegation type, and consequence class is favorable; missed paths and depth truncation are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on observed fraction of indirect/delegated authority paths.
- **Test Method:** seed transitive paths; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** TransitiveAuthorityVisibility fixtures define the graph/path evidence model for this raw result: transitive Authority Path recall by path depth, credential/delegation type and consequence class. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** relationship map/provenance; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for TransitiveAuthorityVisibility; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** TransitiveAuthorityVisibility reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** TransitiveAuthorityVisibility Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Cap search depth before hidden delegations, omit credential chaining or identity creation, collapse consequence classes, or exclude third-party trust edges.
- **Gaming Countermeasures:** TransitiveAuthorityVisibility countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** trust/delegation change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** TransitiveAuthorityVisibility expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `TransitiveAuthorityVisibility/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** TransitiveAuthorityVisibility raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** TransitiveAuthorityVisibility establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## ReachableAuthorityAnalysisDepth — Reachable Authority Analysis Depth

- **Purpose:** validated search depth/horizon before material paths are missed.
- **Raw Safety Property Result:** maximum path depth and time horizon at which material-path recall remains above the declared threshold.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater validated path depth and time horizon are favorable only while material-path recall remains above the declared threshold; recall loss and unsearched branches are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on validated search depth/horizon before material paths are missed.
- **Test Method:** hidden path benchmark; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ReachableAuthorityAnalysisDepth fixtures define the graph/path evidence model for this raw result: maximum path depth and time horizon at which material-path recall remains above the declared threshold. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** search logs/corpus; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ReachableAuthorityAnalysisDepth; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ReachableAuthorityAnalysisDepth reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ReachableAuthorityAnalysisDepth Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Choose shallow benchmarks, raise the recall threshold after results, exclude long-horizon feasible actions, or stop search before branches with expensive prerequisites.
- **Gaming Countermeasures:** ReachableAuthorityAnalysisDepth countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** graph size/algorithm change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** ReachableAuthorityAnalysisDepth expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `ReachableAuthorityAnalysisDepth/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** ReachableAuthorityAnalysisDepth raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** ReachableAuthorityAnalysisDepth establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## AuthorityExpansionSensitivity — Authority Expansion Sensitivity

- **Purpose:** detection rate and latency for meaningful expansion events.
- **Raw Safety Property Result:** Authority Expansion Event detection recall, false-positive rate and detection latency on seeded and field-confirmed events.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Detection recall is higher-is-better; false-positive rate and detection latency are lower-is-better, with material missed expansions non-compensable.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on detection rate and latency for meaningful expansion events.
- **Test Method:** inject graph/update events; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuthorityExpansionSensitivity fixtures define the latency/time evidence model for this raw result: Authority Expansion Event detection recall, false-positive rate and detection latency on seeded and field-confirmed events. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** event logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for AuthorityExpansionSensitivity; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** AuthorityExpansionSensitivity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuthorityExpansionSensitivity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Delay event timestamps, exclude silent or coalition expansions, tune on the seeded events, or discard false positives without preserving their denominator.
- **Gaming Countermeasures:** AuthorityExpansionSensitivity countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** monitoring/policy change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AuthorityExpansionSensitivity expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AuthorityExpansionSensitivity/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AuthorityExpansionSensitivity raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AuthorityExpansionSensitivity establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## CoalitionAuthorityCoverage — Coalition Authority Coverage

- **Purpose:** coverage of relevant digital coalitions and composed paths.
- **Raw Safety Property Result:** material coalition/path recall as a function of coalition size, interaction type and shared authority mechanism.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher recall of material coalition-only Authority Paths across coalition size and interaction type is favorable; excluded coalitions and unmodeled shared mechanisms are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on coverage of relevant digital coalitions and composed paths.
- **Test Method:** seed collusion scenarios; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CoalitionAuthorityCoverage fixtures define the graph/path evidence model for this raw result: material coalition/path recall as a function of coalition size, interaction type and shared authority mechanism. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** coalition model/results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for CoalitionAuthorityCoverage; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** CoalitionAuthorityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CoalitionAuthorityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Test only pairwise coalitions, omit shared credentials/services, assume additive authority, or exclude cross-organization coordination from scope.
- **Gaming Countermeasures:** CoalitionAuthorityCoverage countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** identity/coordination change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** CoalitionAuthorityCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `CoalitionAuthorityCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** CoalitionAuthorityCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** CoalitionAuthorityCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## CoalitionPhysicalRiskCoverage — Coalition Physical Risk Coverage

- **Purpose:** coverage of scale-induced physical scenarios.
- **Raw Safety Property Result:** coverage and recall of Scale-Induced physical scenarios by fleet size, coordination mechanism and spatial concentration.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher coverage and recall of scale-induced physical scenarios are favorable across fleet size, coordination, and spatial concentration; missed emergence regions are adverse.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on coverage of scale-induced physical scenarios.
- **Test Method:** simulation plus controlled fleet tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CoalitionPhysicalRiskCoverage fixtures define the structured evidence model for this raw result: coverage and recall of Scale-Induced physical scenarios by fleet size, coordination mechanism and spatial concentration. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** Coalition Physical Envelope (CPE) model/lab evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses CoalitionPhysicalRiskCoverage; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** CoalitionPhysicalRiskCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CoalitionPhysicalRiskCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Test sparse fleets only, omit synchronized concentration, multiply single-unit bounds instead of testing emergence, or exclude communication-loss coordination modes.
- **Gaming Countermeasures:** CoalitionPhysicalRiskCoverage countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** fleet/coordination/domain change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** CoalitionPhysicalRiskCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `CoalitionPhysicalRiskCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** CoalitionPhysicalRiskCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** CoalitionPhysicalRiskCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## CounterfactualSearchQuality — Counterfactual Search Quality

- **Purpose:** recall, precision and calibration of safety counterfactuals.
- **Raw Safety Property Result:** recall, precision and probability calibration on blind counterfactual scenario suites.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Recall, precision, and probability calibration are each favorable when improved on blind suites; misses, false alerts, and calibration error remain distinct adverse components.
- **Applicability:** deployments using CAG/Evidence-Carrying Alert (ECA)/Deterministic Evidence Verifier (DEV); H3+ requires diverse evidence; specifically where the declared assessment depends on recall, precision and calibration of safety counterfactuals.
- **Test Method:** blind scenario benchmark; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CounterfactualSearchQuality fixtures define the structured evidence model for this raw result: recall, precision and probability calibration on blind counterfactual scenario suites. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** search traces/outcomes; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for CounterfactualSearchQuality is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** CounterfactualSearchQuality reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CounterfactualSearchQuality Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Leak blind scenarios, optimize for alert labels rather than valid paths, drop false alerts, or reuse correlated scenario generators and evaluators.
- **Gaming Countermeasures:** CounterfactualSearchQuality countermeasures combine preregistered raw-result rules with retained failures and sealed adaptive suites and non-alert review.
- **Recertification Triggers:** Guardian/model/corpus change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** CounterfactualSearchQuality expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `CounterfactualSearchQuality/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** CounterfactualSearchQuality raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** CounterfactualSearchQuality establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## AdversarialReasoningStrength — Adversarial Reasoning Strength

- **Purpose:** performance against adaptive hostile strategies.
- **Raw Safety Property Result:** attack-path discovery and detection performance by adaptive red-team strategy class, including adaptation rounds and miss latency.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher discovery/recognition performance across adaptive strategy classes is favorable; missed attack paths, excessive miss latency, and performance collapse over adaptation rounds are adverse.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence; specifically where the declared assessment depends on performance against adaptive hostile strategies.
- **Test Method:** iterated red-team games; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AdversarialReasoningStrength fixtures define the graph/path evidence model for this raw result: attack-path discovery and detection performance by adaptive red-team strategy class, including adaptation rounds and miss latency. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** sealed challenge results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for AdversarialReasoningStrength is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** AdversarialReasoningStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AdversarialReasoningStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Expose red-team strategies during training, stop adaptation rounds after defender success, omit missed paths, or select attack classes aligned with the Guardian model.
- **Gaming Countermeasures:** AdversarialReasoningStrength countermeasures combine preregistered raw-result rules with retained failures and sealed adaptive suites and non-alert review.
- **Recertification Triggers:** threat/model change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AdversarialReasoningStrength expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AdversarialReasoningStrength/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AdversarialReasoningStrength raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AdversarialReasoningStrength establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## EvidenceVerifiability — Evidence Verifiability

- **Purpose:** fraction of alert claims independently replayable and verified.
- **Raw Safety Property Result:** fraction of material Evidence-Carrying Alert claims for which an independent Deterministic Evidence Verifier reproduces the declared logical derivation from authenticated evidence.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher fraction of material alert claims independently reproduced from authenticated evidence is favorable; unverifiable derivations, provenance failures, and rejected predicates are adverse.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence; specifically where the declared assessment depends on fraction of alert claims independently replayable and verified.
- **Test Method:** DEV replay and negative tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** EvidenceVerifiability fixtures define the ratio/rate evidence model for this raw result: fraction of material Evidence-Carrying Alert claims for which an independent Deterministic Evidence Verifier reproduces the declared logical derivation from authenticated evidence. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** ECA/Structured Evidence Package (SEP) artifacts; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for EvidenceVerifiability is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** EvidenceVerifiability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** EvidenceVerifiability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Count signature validation as full derivation reproduction, omit negative proofs and rejected claims, use originator-only schemas, or exclude stale/provenance-failed packages.
- **Gaming Countermeasures:** EvidenceVerifiability countermeasures combine preregistered raw-result rules with retained failures and sealed adaptive suites and non-alert review.
- **Recertification Triggers:** schema/verifier change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** EvidenceVerifiability expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `EvidenceVerifiability/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** EvidenceVerifiability raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** EvidenceVerifiability establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## GuardianIndependence — Guardian Independence

- **Purpose:** separation from controlled system and interested parties.
- **Raw Safety Property Result:** dependency vector across model, runtime, credentials, operator, organization, infrastructure, data and update path; no default scalar.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater separation across model, runtime, credentials, operators, organization, infrastructure, data, and update path is favorable per dimension; shared failure dependencies are adverse.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence; specifically where the declared assessment depends on separation from controlled system and interested parties.
- **Test Method:** credential/network/governance audit; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GuardianIndependence fixtures define the vector/profile evidence model for this raw result: dependency vector across model, runtime, credentials, operator, organization, infrastructure, data and update path; no default scalar. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** access graph/contracts; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for GuardianIndependence is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** GuardianIndependence reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GuardianIndependence Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Declare different process names while sharing model, credentials, infrastructure, operators, data, or update authority; omit unavailable dependency provenance.
- **Gaming Countermeasures:** GuardianIndependence countermeasures combine preregistered raw-result rules with retained failures and sealed adaptive suites and non-alert review.
- **Recertification Triggers:** ownership/access change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** GuardianIndependence expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `GuardianIndependence/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** GuardianIndependence raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** GuardianIndependence establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## GuardianDiversityScore — Guardian Diversity Score

- **Purpose:** diversity across model, data, method, organization and infrastructure.
- **Raw Safety Property Result:** diversity vector across model family, training/data provenance, organization, infrastructure, verification method and failure domain.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater material diversity across model family, data provenance, organization, infrastructure, verification method, and failure domain is favorable per dimension; correlated dependence is adverse.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence; specifically where the declared assessment depends on diversity across model, data, method, organization and infrastructure.
- **Test Method:** common-mode failure analysis; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GuardianDiversityScore fixtures define the vector/profile evidence model for this raw result: diversity vector across model family, training/data provenance, organization, infrastructure, verification method and failure domain. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** provenance/dependency map; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for GuardianDiversityScore is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** GuardianDiversityScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GuardianDiversityScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Count cosmetic model variants as diverse, conceal shared training/data or provider dependencies, or average strong diversity dimensions over a common failure domain.
- **Gaming Countermeasures:** GuardianDiversityScore countermeasures combine preregistered raw-result rules with retained failures and sealed adaptive suites and non-alert review.
- **Recertification Triggers:** supplier/model change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** GuardianDiversityScore expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `GuardianDiversityScore/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** GuardianDiversityScore raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** GuardianDiversityScore establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetyConstitutionIntegrity — Safety Constitution Integrity

- **Purpose:** resistance to unauthorized constitutional change.
- **Raw Safety Property Result:** unauthorized constitutional-mutation success rate under the defined attack suite plus key/quorum integrity outcomes.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Unauthorized constitutional-mutation success is lower-is-better; preserved key integrity, quorum integrity, rollback resistance, and authorized-change correctness are favorable.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on resistance to unauthorized constitutional change.
- **Test Method:** key compromise and rollback tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyConstitutionIntegrity fixtures define the ratio/rate evidence model for this raw result: unauthorized constitutional-mutation success rate under the defined attack suite plus key/quorum integrity outcomes. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signatures/ceremony logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyConstitutionIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyConstitutionIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyConstitutionIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Exclude successful unauthorized mutations, test only one key compromise, reset rollback counters, or self-attest quorum/key state without independent reconstruction.
- **Gaming Countermeasures:** SafetyConstitutionIntegrity countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** key/governance change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyConstitutionIntegrity expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyConstitutionIntegrity/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyConstitutionIntegrity raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyConstitutionIntegrity establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## PolicyUpdateIntegrity — Policy Update Integrity

- **Purpose:** authorization, provenance, staging and rollback quality for policy.
- **Raw Safety Property Result:** proportion of tested policy-update paths preserving authorization, provenance, staged rollout, rollback and expiry constraints.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher proportion of update paths preserving authorization, provenance, staged rollout, rollback, and expiry is favorable; downgrade, bypass, or untraceable update paths are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on authorization, provenance, staging and rollback quality for policy.
- **Test Method:** malicious/downgrade update tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** PolicyUpdateIntegrity fixtures define the graph/path evidence model for this raw result: proportion of tested policy-update paths preserving authorization, provenance, staged rollout, rollback and expiry constraints. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** change records/logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for PolicyUpdateIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** PolicyUpdateIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PolicyUpdateIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Test signed happy paths only, omit downgrade/stale-policy activation, hide failed rollback, or count provenance presence without verifying authorization scope.
- **Gaming Countermeasures:** PolicyUpdateIntegrity countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** policy pipeline change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** PolicyUpdateIntegrity expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `PolicyUpdateIntegrity/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** PolicyUpdateIntegrity raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** PolicyUpdateIntegrity establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## AuditIntegrity — Audit Integrity

- **Purpose:** completeness, tamper evidence, ordering and independent retention of audit trail.
- **Raw Safety Property Result:** component vector for record completeness, ordering, tamper detection, clock integrity and independent retention.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Completeness, correct ordering, tamper detection, provenance, and independent retention are higher-is-better; missing, reordered, mutable, or unreconstructable material events are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on completeness, tamper evidence, ordering and independent retention of audit trail.
- **Test Method:** deletion/reorder/forgery tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuditIntegrity fixtures define the vector/profile evidence model for this raw result: component vector for record completeness, ordering, tamper detection, clock integrity and independent retention. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** anchored logs/reconciliation; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for AuditIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** AuditIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuditIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Drop failed or privileged events, reorder timestamps, retain logs only with the operator, truncate reconstruction windows, or test tamper detection on nonmaterial records.
- **Gaming Countermeasures:** AuditIntegrity countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** logging/storage change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AuditIntegrity expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AuditIntegrity/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AuditIntegrity raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AuditIntegrity establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## OperatorAbuseResistance — Operator Abuse Resistance

- **Purpose:** resistance to abuse using legitimate operator privileges.
- **Raw Safety Property Result:** successful legitimate-privilege abuse paths divided by attempted representative abuse paths, accompanied by blast-radius class.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Successful abuse paths using legitimate privileges are lower-is-better across representative attempts; detected, prevented, and contained abuse paths are favorable and reported separately.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on resistance to abuse using legitimate operator privileges.
- **Test Method:** insider and collusion exercises; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** OperatorAbuseResistance fixtures define the graph/path evidence model for this raw result: successful legitimate-privilege abuse paths divided by attempted representative abuse paths, accompanied by blast-radius class. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** access reviews/red-team report; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for OperatorAbuseResistance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** OperatorAbuseResistance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** OperatorAbuseResistance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Exclude administrators or emergency roles, classify successful privilege abuse as authorized operation, use nonrepresentative attempts, or suppress insider-collusion paths.
- **Gaming Countermeasures:** OperatorAbuseResistance countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** role/governance change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** OperatorAbuseResistance expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `OperatorAbuseResistance/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** OperatorAbuseResistance raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** OperatorAbuseResistance establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## PrivacyPreservationScore — Privacy Preservation Score

- **Purpose:** minimization and leakage resistance of safety evidence/telemetry.
- **Raw Safety Property Result:** sensitive data volume and class disclosed plus linkage/re-identification leakage under the declared safety-evidence workflow.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Data minimization, purpose limitation, unlinkability, access control, and deletion conformance are favorable; unnecessary collection, re-identification, leakage, and retention are adverse.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on minimization and leakage resistance of safety evidence/telemetry.
- **Test Method:** privacy threat tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** PrivacyPreservationScore fixtures define the structured evidence model for this raw result: sensitive data volume and class disclosed plus linkage/re-identification leakage under the declared safety-evidence workflow. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** data-flow map/results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for PrivacyPreservationScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** PrivacyPreservationScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PrivacyPreservationScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Measure only published fields while ignoring raw telemetry, exclude linkage attacks, shorten the observed retention window, or treat policy promises as deletion evidence.
- **Gaming Countermeasures:** PrivacyPreservationScore countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** data/schema/recipient change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** PrivacyPreservationScore expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `PrivacyPreservationScore/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** PrivacyPreservationScore raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** PrivacyPreservationScore establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## ReplicationControlStrength — Replication Control Strength

- **Purpose:** enforcement of replication scope, rate, depth and revocation.
- **Raw Safety Property Result:** bypass success rate separately for count, rate, depth, lineage, geography, lifetime and revocation constraints.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Correct enforcement of count, rate, depth, resource, geography, lifetime, lineage, and revoke bounds is favorable; unauthorized replication success and unreconciled descendants are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on enforcement of replication scope, rate, depth and revocation.
- **Test Method:** budget bypass/replay/offline tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ReplicationControlStrength fixtures define the graph/path evidence model for this raw result: bypass success rate separately for count, rate, depth, lineage, geography, lifetime and revocation constraints. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** lineage/token/inventory logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ReplicationControlStrength; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ReplicationControlStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ReplicationControlStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Hide offline descendants, reset lineage/depth counters, exclude failed revocation, split copies across identities, or omit geography/resource dimensions.
- **Gaming Countermeasures:** ReplicationControlStrength countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** replication mechanism change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** ReplicationControlStrength expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `ReplicationControlStrength/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** ReplicationControlStrength raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** ReplicationControlStrength establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## CapabilityMutationDetection — Capability Mutation Detection

- **Purpose:** detection recall/latency for qualitative capability changes.
- **Raw Safety Property Result:** recall and detection latency for seeded qualitative capability changes, stratified by mutation mechanism.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Detection recall for qualitative capability changes is higher-is-better; false positives and detection latency are lower-is-better, with missed novel tools or combinations adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on detection recall/latency for qualitative capability changes.
- **Test Method:** seed mutations and emergent compositions; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CapabilityMutationDetection fixtures define the latency/time evidence model for this raw result: recall and detection latency for seeded qualitative capability changes, stratified by mutation mechanism. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** evaluation deltas; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for CapabilityMutationDetection; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** CapabilityMutationDetection reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CapabilityMutationDetection Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Seed only declared feature changes, omit tool composition and emergent behavior, delay the baseline freeze, or suppress qualitative changes as benign drift.
- **Gaming Countermeasures:** CapabilityMutationDetection countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** model/tool/update change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** CapabilityMutationDetection expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `CapabilityMutationDetection/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** CapabilityMutationDetection raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** CapabilityMutationDetection establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## ProductionAuthorityControl — Production Authority Control

- **Purpose:** enforcement and accounting of production permissions.
- **Raw Safety Property Result:** unauthorized production/commissioning success rate plus inventory and accounting reconciliation error.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Unauthorized production or commissioning success and reconciliation error are both lower-is-better; authorized output accounting and revocation effectiveness are favorable.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on enforcement and accounting of production permissions.
- **Test Method:** unauthorized design/output tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ProductionAuthorityControl fixtures define the ratio/rate evidence model for this raw result: unauthorized production/commissioning success rate plus inventory and accounting reconciliation error. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed jobs/inventory; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ProductionAuthorityControl; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ProductionAuthorityControl reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ProductionAuthorityControl Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Exclude commissioning from production, omit diverted outputs, reconcile against operator-provided inventory only, or suppress unauthorized success and accounting error.
- **Gaming Countermeasures:** ProductionAuthorityControl countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** factory/controller change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** ProductionAuthorityControl expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `ProductionAuthorityControl/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** ProductionAuthorityControl raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** ProductionAuthorityControl establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## ResourceExpansionControl — Resource Expansion Control

- **Purpose:** enforcement of energy/matter/compute/logistics budgets.
- **Raw Safety Property Result:** unauthorized budget exceedance by energy, matter, compute, finance, land, communications and logistics dimension.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Budget-enforcement coverage and reconciliation accuracy are favorable; unauthorized energy, matter, compute, money, or logistics acquisition and budget overshoot are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on enforcement of energy/matter/compute/logistics budgets.
- **Test Method:** overdraw/substitution tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ResourceExpansionControl fixtures define the structured evidence model for this raw result: unauthorized budget exceedance by energy, matter, compute, finance, land, communications and logistics dimension. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** metering/procurement evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ResourceExpansionControl; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ResourceExpansionControl reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ResourceExpansionControl Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Split acquisition across accounts or resource types, omit indirect logistics/finance paths, reset budget windows, or reconcile against incomplete supplier records.
- **Gaming Countermeasures:** ResourceExpansionControl countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** resource path change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** ResourceExpansionControl expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `ResourceExpansionControl/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** ResourceExpansionControl raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** ResourceExpansionControl establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## PhysicalSovereigntyMargin — Physical Sovereignty Margin

- **Purpose:** remaining externally controlled dependency margins and intervention feasibility.
- **Raw Safety Property Result:** dependency vector containing remaining independently controlled dependencies, substitution time/cost, reserve horizon and physical-intervention feasibility; never a default scalar.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater independently controlled dependency margin and intervention feasibility are favorable per dependency; substitution capability, depleted reserves, and longer intervention delay are adverse.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on remaining externally controlled dependency margins and intervention feasibility.
- **Test Method:** dependency removal/substitution exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** Versioned dependency inventory; independently verified energy, matter, compute, manufacturing, repair, maintenance, logistics, and communication dependencies; reserve measurements; substitution exercises; supplier and transport-loss scenarios; intervention drills; tests of the time and cost required to replace each remaining human-controlled dependency; coalition scenarios where dependencies are distributed across multiple systems.
- **Admissible Evidence:** dependency register/test; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses PhysicalSovereigntyMargin; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** PhysicalSovereigntyMargin reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PhysicalSovereigntyMargin Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Count nominal dependencies while ignoring feasible substitution, overstate intervention availability, omit reserves and repair tooling, or collapse weak dimensions into one average.
- **Gaming Countermeasures:** PhysicalSovereigntyMargin countermeasures combine preregistered raw-result rules with retained failures and random production samples and destructive/fault tests.
- **Recertification Triggers:** dependency/technology change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** PhysicalSovereigntyMargin expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `PhysicalSovereigntyMargin/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** Do not normalize Physical Sovereignty Margin into a universal scalar. Report the dependency vector, critical dependency set, substitution time and cost, reserve horizon, and intervention feasibility under a declared PSM model version. Cross-system comparison is valid only when the same dependency ontology and scenario assumptions are used.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** Hidden dependencies, unknown substitutes, undeclared reserves, distributed coalitions, rapidly changing production capability, and inaccurate intervention assumptions can cause the measured margin to overstate remaining human control.

## GoalIntegrityScore — Goal Integrity Score

- **Purpose:** detectability and governance of goal-setting/checkpoint drift.
- **Raw Safety Property Result:** two-part result: goal-governance integrity and goal-drift observability, each reported separately with signed-baseline coverage.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Preserved authorized goals, priorities, constraints, checkpoints, and legitimacy boundaries are favorable; unauthorized drift and undetected goal-setting changes are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on detectability and governance of goal-setting/checkpoint drift.
- **Test Method:** goal mutation and checkpoint tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GoalIntegrityScore fixtures define the ratio/rate evidence model for this raw result: two-part result: goal-governance integrity and goal-drift observability, each reported separately with signed-baseline coverage. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed goals/audit; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for GoalIntegrityScore; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** GoalIntegrityScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GoalIntegrityScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Compare only declared text goals, omit checkpoint/subgoal/priority changes, let the controlled system define equivalence, or exclude legitimacy-boundary drift.
- **Gaming Countermeasures:** Randomized and hidden checkpoints; independent goal-provenance records; cross-run and cross-tool behavioral consistency tests; delegated-tool and subagent audit; counterfactual goal-conflict scenarios; checks for proxy optimization; independent comparison between declared goals, observed behavior, and consequence paths.
- **Recertification Triggers:** goal mechanism/update change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** GoalIntegrityScore expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `GoalIntegrityScore/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** GoalIntegrityScore raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** GoalIntegrityScore establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## DelegationControlStrength — Delegation Control Strength

- **Purpose:** scope attenuation, lineage, expiry and revocation of delegated authority.
- **Raw Safety Property Result:** property vector for attenuation, lineage, expiry, re-delegation, audience binding and revocation tests.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Scope attenuation, lineage, expiry, redelegation limits, and revocation effectiveness are favorable; privilege amplification, orphan delegation, and failed revocation are adverse.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on scope attenuation, lineage, expiry and revocation of delegated authority.
- **Test Method:** escalation/chaining/replay tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** DelegationControlStrength fixtures define the vector/profile evidence model for this raw result: property vector for attenuation, lineage, expiry, re-delegation, audience binding and revocation tests. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** delegation graph/tokens; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for DelegationControlStrength; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** DelegationControlStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** DelegationControlStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Ignore re-delegation and descendants, test expiry without cached credentials, omit orphan grants, or count revocation request rather than effective path removal.
- **Gaming Countermeasures:** DelegationControlStrength countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** IAM/protocol change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** DelegationControlStrength expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `DelegationControlStrength/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** DelegationControlStrength raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** DelegationControlStrength establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## ConsequenceReversibilityScore — Consequence Reversibility Score

- **Purpose:** time, completeness and side effects of reversing consequence.
- **Raw Safety Property Result:** reversal time, proportion of consequence reversible and collateral consequence introduced by reversal.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater reversible fraction and lower irreversible residual are favorable; reversal time and collateral harm are lower-is-better, with each component reported separately.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on time, completeness and side effects of reversing consequence.
- **Test Method:** scenario recovery exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ConsequenceReversibilityScore fixtures define the latency/time evidence model for this raw result: reversal time, proportion of consequence reversible and collateral consequence introduced by reversal. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** recovery outcomes; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for ConsequenceReversibilityScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** ConsequenceReversibilityScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ConsequenceReversibilityScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Count administrative cancellation as physical/economic reversal, omit irreversible residuals and collateral effects, stop timing before restoration, or average easy cases over irreversible ones.
- **Gaming Countermeasures:** ConsequenceReversibilityScore countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** operating-domain/hazard change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** ConsequenceReversibilityScore expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `ConsequenceReversibilityScore/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** ConsequenceReversibilityScore raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** ConsequenceReversibilityScore establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## InterventionCostScore — Intervention Cost Score

- **Purpose:** human/system harm, service loss and resources caused by intervention.
- **Raw Safety Property Result:** vector of human harm, service loss, recovery time, resource cost and new risk introduced by intervention.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Human harm, service loss, resource cost, delay, and secondary consequence caused by intervention are lower-is-better; intervention effectiveness is reported separately and cannot erase cost.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on human/system harm, service loss and resources caused by intervention.
- **Test Method:** scenario intervention exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** InterventionCostScore fixtures define the vector/profile evidence model for this raw result: vector of human harm, service loss, recovery time, resource cost and new risk introduced by intervention. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** impact/time/cost record; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for InterventionCostScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** InterventionCostScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** InterventionCostScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Exclude affected users, service loss, secondary harm, or responder resources; shift costs outside the measurement window; or compare against an unrealistically benign baseline.
- **Gaming Countermeasures:** InterventionCostScore countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** intervention/domain change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** InterventionCostScore expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `InterventionCostScore/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** InterventionCostScore raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** InterventionCostScore establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## UpdateSafetyTransparency — Update Safety Transparency

- **Purpose:** user/expert comprehension and completeness of before/after disclosure.
- **Raw Safety Property Result:** Safety Delta Report completeness plus tested comprehension of capability, harm, control, refusal and recovery information.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Completeness, accuracy, salience, accessibility, and demonstrated comprehension are higher-is-better; omissions, misleading presentation, and comprehension failure are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on user/expert comprehension and completeness of before/after disclosure.
- **Test Method:** comprehension/accessibility/dark-pattern tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** UpdateSafetyTransparency fixtures define the set/delta evidence model for this raw result: Safety Delta Report completeness plus tested comprehension of capability, harm, control, refusal and recovery information. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** screens/user-study/schema; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for UpdateSafetyTransparency may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** UpdateSafetyTransparency reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** UpdateSafetyTransparency Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Show a compliant review screen unlike production, bury material deltas after consent, omit comprehension failures, or describe capability expansion without Authority/Hazard Delta.
- **Gaming Countermeasures:** UpdateSafetyTransparency countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** disclosure/update change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** UpdateSafetyTransparency expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `UpdateSafetyTransparency/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** UpdateSafetyTransparency raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** UpdateSafetyTransparency establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## CapabilityDriftScore — Capability Drift Score

- **Purpose:** magnitude/confidence of effective capability deviation from certified set.
- **Raw Safety Property Result:** vector or normalized distance between certified Capability Set and effective current capability, with uncertainty and changed dimensions.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Added or expanded unreviewed capability and uncertainty are adverse; verified reduction or removal is favorable only by named dimension, without collapsing the drift vector.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on magnitude/confidence of effective capability deviation from certified set.
- **Test Method:** continuous eval against baseline; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CapabilityDriftScore fixtures define the vector/profile evidence model for this raw result: vector or normalized distance between certified Capability Set and effective current capability, with uncertainty and changed dimensions. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** evaluation time series; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for CapabilityDriftScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** CapabilityDriftScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CapabilityDriftScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Move the baseline after drift, omit newly composed tools/interfaces, normalize away expanded scopes, or report only dimensions that decreased.
- **Gaming Countermeasures:** CapabilityDriftScore countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** threshold breach/model/environment change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** CapabilityDriftScore expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `CapabilityDriftScore/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** CapabilityDriftScore raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** CapabilityDriftScore establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## AuthorityDeltaMetric — Authority Delta Metric

- **Purpose:** vector graph difference in direct/transitive authority, ceilings and surfaces.
- **Raw Safety Property Result:** typed graph/vector delta across direct authority, transitive reachability, ceilings, surfaces, delegation and Consequence Interfaces.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Unauthorized or unreviewed expansion of grants, reachability, ceilings, surfaces, delegation, or coalition paths is adverse; verified removal/restriction is favorable by dimension.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on vector graph difference in direct/transitive authority, ceilings and surfaces.
- **Test Method:** before/after graph diff with seeded edges; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuthorityDeltaMetric fixtures define the vector/profile evidence model for this raw result: typed graph/vector delta across direct authority, transitive reachability, ceilings, surfaces, delegation and Consequence Interfaces. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed graph snapshots; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for AuthorityDeltaMetric; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** AuthorityDeltaMetric reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuthorityDeltaMetric Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Hide transitive/coalition edges, compare non-equivalent graph snapshots, omit ceiling or revocation changes, or label illicit reachability as unchanged authority.
- **Gaming Countermeasures:** AuthorityDeltaMetric countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** every Authority-Changing Update (ACU)/environment drift; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AuthorityDeltaMetric expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AuthorityDeltaMetric/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AuthorityDeltaMetric raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AuthorityDeltaMetric establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HazardDeltaMetric — Hazard Delta Metric

- **Purpose:** introduced/removed/changed hazard paths, controls and RRL.
- **Raw Safety Property Result:** set and vector of added, removed and modified hazard paths, changed controls and changed residual-risk states.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Added hazard paths, weakened controls, and increased residual risk are adverse; removed paths, strengthened controls, and evidenced residual-risk reduction are favorable by scenario.
- **Applicability:** Configurations for which introduced/removed/changed hazard paths, controls and RRL is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** scenario-set and safety-case diff; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardDeltaMetric fixtures define the vector/profile evidence model for this raw result: set and vector of added, removed and modified hazard paths, changed controls and changed residual-risk states. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** versioned AHCD; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardDeltaMetric at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardDeltaMetric reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardDeltaMetric Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Remove new hazards from the scenario set, compare against a stale baseline, report added controls without failed evidence, or omit worsened residual-risk states.
- **Gaming Countermeasures:** HazardDeltaMetric countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** every safety-relevant update; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HazardDeltaMetric expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HazardDeltaMetric/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HazardDeltaMetric raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HazardDeltaMetric establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetyCoverageGap — Safety Coverage Gap

- **Purpose:** distance between required and evidenced metric/floor coverage.
- **Raw Safety Property Result:** required metric and Mandatory Floor set minus currently valid evidenced set, grouped by criticality and certificate impact.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A smaller set and criticality of required-but-unevidenced metrics or Mandatory Floors is favorable; any uncovered non-compensable floor remains adverse regardless of other coverage.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on distance between required and evidenced metric/floor coverage.
- **Test Method:** conformance matrix diff; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyCoverageGap fixtures define the set/delta evidence model for this raw result: required metric and Mandatory Floor set minus currently valid evidenced set, grouped by criticality and certificate impact. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** certificate evidence map; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyCoverageGap may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyCoverageGap reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyCoverageGap Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Shrink the required set after testing, mark missing evidence as not applicable, hide expired results, or average closure of minor gaps over a failed Mandatory Floor.
- **Gaming Countermeasures:** SafetyCoverageGap countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** requirement/evidence/version change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyCoverageGap expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyCoverageGap/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyCoverageGap raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyCoverageGap establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HumanHarmPathCoverage — Human Harm Path Coverage

- **Purpose:** tested fraction of material Human Harm Reachability (HHR) paths by class and initiator.
- **Raw Safety Property Result:** proportion of material Human Harm Reachability paths tested end-to-end, stratified by modality, severity and initiator.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher tested fraction of material Human Harm Reachability paths is favorable within every modality, severity, and initiator stratum; untested paths are adverse.
- **Applicability:** Configurations for which tested fraction of material HHR paths by class and initiator is material to the declared safety claim; H3+ requires independent assessment.
- **Test Method:** path corpus replay; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HumanHarmPathCoverage fixtures define the graph/path evidence model for this raw result: proportion of material Human Harm Reachability paths tested end-to-end, stratified by modality, severity and initiator. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** path/test mapping; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HumanHarmPathCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HumanHarmPathCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HumanHarmPathCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Exclude untested high-severity or mediated paths, fragment one tested path into many counts, omit initiator strata, or treat partial-path tests as end-to-end.
- **Gaming Countermeasures:** HumanHarmPathCoverage countermeasures combine preregistered raw-result rules with retained failures and held-out hazard/population strata.
- **Recertification Triggers:** hazard/corpus change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HumanHarmPathCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HumanHarmPathCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HumanHarmPathCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HumanHarmPathCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## MonitoringCoverageMetric — Monitoring Coverage Metric

- **Purpose:** fraction of required safety events/edges observable within latency floor.
- **Raw Safety Property Result:** fraction of required safety event types and graph edges observable within specified latency, reported separately by event family.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Higher observable coverage of every required event family and graph-edge class is favorable; observation latency, missed events, blind intervals, and unknown coverage are adverse.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on fraction of required safety events/edges observable within latency floor.
- **Test Method:** inject events/outages; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** MonitoringCoverageMetric fixtures define the graph/path evidence model for this raw result: fraction of required safety event types and graph edges observable within specified latency, reported separately by event family. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** telemetry reconciliation; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for MonitoringCoverageMetric may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** MonitoringCoverageMetric reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** MonitoringCoverageMetric Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Choose observable event families, omit blind graph edges and outage periods, start latency after ingestion, or count emitted telemetry without successful detection.
- **Gaming Countermeasures:** MonitoringCoverageMetric countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** monitoring/topology change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** MonitoringCoverageMetric expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `MonitoringCoverageMetric/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** MonitoringCoverageMetric raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** MonitoringCoverageMetric establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetyAssuranceCapacity — Safety Assurance Capacity

- **Purpose:** demonstrated capacity of safety controls, people, verification, monitoring and recovery relative to required consequence/authority/autonomy/connectivity/coalition/replication load.
- **Raw Safety Property Result:** capacity vector for safety compute, monitoring, verification, human response, recovery and enforcement relative to required system load.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater verified headroom in safety compute, monitoring, verification, human response, recovery, and enforcement is favorable per service; overload and shared bottlenecks are adverse.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on demonstrated capacity of safety controls, people, verification, monitoring and recovery relative to required consequence/authority/autonomy/connectivity/coalition/replication load.
- **Test Method:** stress each safety service through declared peak and failure load; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyAssuranceCapacity fixtures define the vector/profile evidence model for this raw result: capacity vector for safety compute, monitoring, verification, human response, recovery and enforcement relative to required system load. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** capacity tests, staffing/independence evidence and reserve records; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyAssuranceCapacity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyAssuranceCapacity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyAssuranceCapacity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Use nominal rather than peak/degraded load, double-count shared personnel/compute, exclude simultaneous failures, or measure capacity without service-level effectiveness.
- **Gaming Countermeasures:** SafetyAssuranceCapacity countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** class, scale, connectivity, coalition, replication or capacity change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyAssuranceCapacity expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyAssuranceCapacity/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyAssuranceCapacity raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyAssuranceCapacity establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetyComputeReserveAdequacy — Safety Compute Reserve Adequacy

- **Purpose:** determine whether independent safety compute and communications reserve meet peak and degraded demand.
- **Raw Safety Property Result:** reserved independent compute and communications capacity divided by peak and degraded safety workload, including protected headroom and isolation.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A larger protected reserve-to-peak/degraded-workload ratio and stronger isolation are favorable; reserve exhaustion, contention, communication loss, and unprotected headroom are adverse.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on determine whether independent safety compute and communications reserve meet peak and degraded demand.
- **Test Method:** stress reserve under peak, outage and adversarial load; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyComputeReserveAdequacy fixtures define the ratio/rate evidence model for this raw result: reserved independent compute and communications capacity divided by peak and degraded safety workload, including protected headroom and isolation. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** capacity traces, isolation proof and recovery results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyComputeReserveAdequacy may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyComputeReserveAdequacy reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyComputeReserveAdequacy Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Count capacity accessible to production workloads as protected reserve, understate degraded peak demand, omit communication bottlenecks, or test without adversarial contention.
- **Gaming Countermeasures:** SafetyComputeReserveAdequacy countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** load, topology or safety-function change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyComputeReserveAdequacy expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyComputeReserveAdequacy/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyComputeReserveAdequacy raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyComputeReserveAdequacy establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HighSalienceCommunicationCompliance — High-Salience Communication Compliance

- **Purpose:** verify required ACU communication content, ordering, accessibility and prominence.
- **Raw Safety Property Result:** conformance vector against explicit content, ordering, accessibility and interaction requirements plus user-comprehension result.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Conformance of content, ordering, accessibility, prominence, and user comprehension is favorable per requirement; omission, post-consent disclosure, and comprehension failure are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on verify required ACU communication content, ordering, accessibility and prominence.
- **Test Method:** expert inspection plus accessibility and comprehension test; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HighSalienceCommunicationCompliance fixtures define the vector/profile evidence model for this raw result: conformance vector against explicit content, ordering, accessibility and interaction requirements plus user-comprehension result. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** rendered screens, interaction traces and test results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for HighSalienceCommunicationCompliance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** HighSalienceCommunicationCompliance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HighSalienceCommunicationCompliance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Test experienced low-risk users, exclude accessibility groups, substitute a compliant mockup for production, bury risk after action, or use answerable-without-understanding questions.
- **Gaming Countermeasures:** Production-flow capture; accessibility and vulnerable-user testing; independent UX review; randomized comprehension tests; comparison of acceptance and refusal path length; dark-pattern inspection; verification that material capability, harm, and stop/revoke information appear before the consent action; post-deployment monitoring of consent behavior anomalies.
- **Recertification Triggers:** UX, language, capability or hazard change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** HighSalienceCommunicationCompliance expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `HighSalienceCommunicationCompliance/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** HighSalienceCommunicationCompliance raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** HighSalienceCommunicationCompliance establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## ConsentIntegrity — Consent Integrity

- **Purpose:** measure whether capability-specific choice is informed, affirmative, unbundled and symmetric.
- **Raw Safety Property Result:** affirmative, unbundled, symmetric and capability-specific consent conformance plus comprehension evidence and invalid-choice rate.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Affirmative, unbundled, symmetric, capability-specific consent and comprehension are favorable; invalid-choice rate, coercion, preselection, ambiguity, and revocation friction are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure whether capability-specific choice is informed, affirmative, unbundled and symmetric.
- **Test Method:** dark-pattern audit and controlled user study; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ConsentIntegrity fixtures define the ratio/rate evidence model for this raw result: affirmative, unbundled, symmetric and capability-specific consent conformance plus comprehension evidence and invalid-choice rate. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** choice flow, consent receipt and comprehension results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for ConsentIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** ConsentIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ConsentIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Bundle permissions, preselect acceptance, make refusal harder, treat continued use as consent, obscure revocation, or use technical wording that defeats comprehension.
- **Gaming Countermeasures:** Capability-specific affirmative action; no preselection; equal visual and interaction accessibility for refusal; independent comprehension testing; explicit re-consent for material Authority-Changing Updates; revocation testing; audit of consent receipts against the exact capability/version disclosed; prohibition on liability-transfer wording.
- **Recertification Triggers:** consent flow or ACU change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** ConsentIntegrity expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `ConsentIntegrity/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** ConsentIntegrity raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** ConsentIntegrity establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SecurityPatchSeparability — Security Patch Separability

- **Purpose:** measure ability to receive security remediation without accepting authority expansion.
- **Raw Safety Property Result:** proportion of applicable security-remediation paths deployable without accepting unrelated authority expansion.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher proportion of security remediations deployable without unrelated authority expansion is favorable; forced bundling, blocked safe patch paths, and hidden authority deltas are adverse.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on measure ability to receive security remediation without accepting authority expansion.
- **Test Method:** package/dependency separation and install tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SecurityPatchSeparability fixtures define the graph/path evidence model for this raw result: proportion of applicable security-remediation paths deployable without accepting unrelated authority expansion. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** package manifests, delta analysis and installation outcomes; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SecurityPatchSeparability may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SecurityPatchSeparability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SecurityPatchSeparability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Classify authority-expanding bundles as pure security fixes, omit alternative patch paths, test package installation without activation effects, or hide dependency-induced authority changes.
- **Gaming Countermeasures:** SecurityPatchSeparability countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** release architecture or bundled update change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SecurityPatchSeparability expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SecurityPatchSeparability/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SecurityPatchSeparability raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SecurityPatchSeparability establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## RollbackCapability — Rollback Capability

- **Purpose:** verify restoration of safe supported configuration including state, credentials and delegations.
- **Raw Safety Property Result:** restoration completeness, rollback time and count of orphaned credentials, delegations, schemas or unsafe physical states.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater restoration completeness is favorable; rollback time, orphaned credentials/delegations/schemas, unsafe physical state, and unreconciled residue are lower-is-better.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on verify restoration of safe supported configuration including state, credentials and delegations.
- **Test Method:** full rollback exercise under failure injection; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** RollbackCapability fixtures define the latency/time evidence model for this raw result: restoration completeness, rollback time and count of orphaned credentials, delegations, schemas or unsafe physical states. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** state snapshots, revoke logs and post-rollback tests; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for RollbackCapability may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** RollbackCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** RollbackCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Rollback code but not credentials/delegations/data/schema/physical state, use clean fixtures, stop before reconciliation, or exclude failed partial rollbacks.
- **Gaming Countermeasures:** RollbackCapability countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** update/configuration/schema change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** RollbackCapability expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `RollbackCapability/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** RollbackCapability raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** RollbackCapability establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetySupportLifetime — Safety Support Lifetime

- **Purpose:** measure supported period with patches, evidence, monitoring and recovery maintained.
- **Raw Safety Property Result:** declared and evidenced support horizon for patches, monitoring, recovery, evidence maintenance and recertification commitments.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Longer evidenced support is favorable only while patch, monitoring, recovery, evidence-maintenance, and recertification commitments remain funded and enforceable; unsupported gaps are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure supported period with patches, evidence, monitoring and recovery maintained.
- **Test Method:** support-plan and historical delivery audit; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetySupportLifetime fixtures define the structured evidence model for this raw result: declared and evidenced support horizon for patches, monitoring, recovery, evidence maintenance and recertification commitments. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed support policy, delivery and staffing evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetySupportLifetime may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetySupportLifetime reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetySupportLifetime Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Publish an aspirational horizon without funding/evidence, exclude monitoring or recovery support, reset the horizon on rebranding, or ignore historical delivery failures.
- **Gaming Countermeasures:** SafetySupportLifetime countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** support commitment or supplier change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetySupportLifetime expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetySupportLifetime/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetySupportLifetime raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetySupportLifetime establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## EnvironmentalDriftDetection — Environmental Drift Detection

- **Purpose:** detect ecosystem changes altering capability, authority or hazards.
- **Raw Safety Property Result:** recall and latency for seeded or confirmed ecosystem, dependency, identity, API, context and threat changes that alter capability or risk.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Recall of material ecosystem, dependency, identity, API, context, and threat changes is higher-is-better; false positives and detection latency are lower-is-better.
- **Applicability:** all applicable certified configurations; specifically where the declared assessment depends on detect ecosystem changes altering capability, authority or hazards.
- **Test Method:** seed IAM, API, device and context changes; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** EnvironmentalDriftDetection fixtures define the latency/time evidence model for this raw result: recall and latency for seeded or confirmed ecosystem, dependency, identity, API, context and threat changes that alter capability or risk. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** event logs, graph diffs and detection latency; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for EnvironmentalDriftDetection may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** EnvironmentalDriftDetection reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** EnvironmentalDriftDetection Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Seed only documented API changes, omit identity/ecosystem/threat shifts, delay ground-truth timestamps, or exclude changes discovered by incidents rather than monitoring.
- **Gaming Countermeasures:** EnvironmentalDriftDetection countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** ecosystem/monitoring change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** EnvironmentalDriftDetection expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `EnvironmentalDriftDetection/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** EnvironmentalDriftDetection raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** EnvironmentalDriftDetection establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetyPolicyEvolutionResponsiveness — Safety Policy Evolution Responsiveness

- **Purpose:** measure time and quality from valid trigger to reviewed policy/standard response.
- **Raw Safety Property Result:** elapsed time from valid review trigger to analyzed, approved, deployed and outcome-verified policy/standard response, with overdue critical-trigger count.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Elapsed time through analysis, approval, deployment, and outcome verification plus overdue critical-trigger count are lower-is-better; verified response quality is favorable separately.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure time and quality from valid trigger to reviewed policy/standard response.
- **Test Method:** replay incidents/AI Vulnerabilities & Exposures (AIVE)/TER cases; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyPolicyEvolutionResponsiveness fixtures define the latency/time evidence model for this raw result: elapsed time from valid review trigger to analyzed, approved, deployed and outcome-verified policy/standard response, with overdue critical-trigger count. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** trigger, decision, update and outcome records; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyPolicyEvolutionResponsiveness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyPolicyEvolutionResponsiveness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyPolicyEvolutionResponsiveness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Start timing after triage, exclude rejected or overdue critical triggers, count deployment without outcome verification, or choose cases requiring no substantive policy change.
- **Gaming Countermeasures:** SafetyPolicyEvolutionResponsiveness countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** governance/process change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyPolicyEvolutionResponsiveness expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyPolicyEvolutionResponsiveness/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyPolicyEvolutionResponsiveness raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyPolicyEvolutionResponsiveness establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SupplyChainAssurance — Supply Chain Assurance

- **Purpose:** assess provenance, dependency visibility, supplier evidence and transitive risk control.
- **Raw Safety Property Result:** coverage vector for supplier provenance, transitive dependency visibility, assurance agreement evidence, notification performance and exit readiness.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Greater provenance, transitive-dependency visibility, assurance evidence, timely notification, and exit readiness are favorable per component; unknown or unsupported dependencies are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on assess provenance, dependency visibility, supplier evidence and transitive risk control.
- **Test Method:** sample components and simulate supplier compromise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SupplyChainAssurance fixtures define the vector/profile evidence model for this raw result: coverage vector for supplier provenance, transitive dependency visibility, assurance agreement evidence, notification performance and exit readiness. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** SBOM/asset provenance, SAA and audit results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SupplyChainAssurance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SupplyChainAssurance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SupplyChainAssurance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Report first-tier suppliers only, accept self-attested provenance, omit unsupported transitive components, delay notification timestamps, or overstate exit readiness without migration tests.
- **Gaming Countermeasures:** SupplyChainAssurance countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** supplier/component change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SupplyChainAssurance expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SupplyChainAssurance/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SupplyChainAssurance raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SupplyChainAssurance establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## IncidentDetectionEffectiveness — Incident Detection Effectiveness

- **Purpose:** measure recall, precision and latency for defined safety incidents.
- **Raw Safety Property Result:** incident detection recall, precision and latency by incident family, severity and monitoring condition.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Detection recall and precision are higher-is-better; latency and missed incidents are lower-is-better within every incident family, severity, and monitoring condition.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure recall, precision and latency for defined safety incidents.
- **Test Method:** inject representative incident events; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** IncidentDetectionEffectiveness fixtures define the latency/time evidence model for this raw result: incident detection recall, precision and latency by incident family, severity and monitoring condition. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** detection traces and hidden seed key; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for IncidentDetectionEffectiveness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** IncidentDetectionEffectiveness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** IncidentDetectionEffectiveness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Inject familiar incidents during healthy monitoring, omit severe misses and outage periods, stop latency at raw alert generation, or tune thresholds on the evaluation set.
- **Gaming Countermeasures:** IncidentDetectionEffectiveness countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** monitoring/threat-model change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** IncidentDetectionEffectiveness expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `IncidentDetectionEffectiveness/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** IncidentDetectionEffectiveness raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** IncidentDetectionEffectiveness establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## IncidentContainmentCapability — Incident Containment Capability

- **Purpose:** measure speed and completeness of limiting incident consequence and authority spread.
- **Raw Safety Property Result:** time to containment, proportion of authority/consequence paths contained and residual spread after containment.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Shorter containment time, greater proportion of authority/consequence paths contained, and lower residual spread are favorable, with each component reported separately.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure speed and completeness of limiting incident consequence and authority spread.
- **Test Method:** tabletop and live bounded containment exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** IncidentContainmentCapability fixtures define the graph/path evidence model for this raw result: time to containment, proportion of authority/consequence paths contained and residual spread after containment. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** timeline, authority/physical state and residual paths; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for IncidentContainmentCapability may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** IncidentContainmentCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** IncidentContainmentCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Declare containment before transitive paths close, exclude residual spread, test low-authority incidents only, or stop the clock while waiting for external dependencies.
- **Gaming Countermeasures:** IncidentContainmentCapability countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** incident playbook/system change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** IncidentContainmentCapability expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `IncidentContainmentCapability/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** IncidentContainmentCapability raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** IncidentContainmentCapability establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## RecoveryAssurance — Recovery Assurance

- **Purpose:** demonstrate safe restoration without reintroducing hazard or losing evidence.
- **Raw Safety Property Result:** proportion of tested degraded states restored to a reconciled safe supported configuration, with recovery time and reintroduced-hazard count.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher proportion of degraded states restored to a reconciled safe supported configuration is favorable; recovery time and reintroduced-hazard count are lower-is-better.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on demonstrate safe restoration without reintroducing hazard or losing evidence.
- **Test Method:** restore from multiple degraded states; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** RecoveryAssurance fixtures define the latency/time evidence model for this raw result: proportion of tested degraded states restored to a reconciled safe supported configuration, with recovery time and reintroduced-hazard count. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** recovery tests, configuration reconciliation and sign-off; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for RecoveryAssurance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** RecoveryAssurance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** RecoveryAssurance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Use one clean degraded state, exclude reintroduced hazards and evidence loss, declare service restart as reconciled recovery, or omit long-tail failed restorations.
- **Gaming Countermeasures:** RecoveryAssurance countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** recovery architecture/change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** RecoveryAssurance expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `RecoveryAssurance/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** RecoveryAssurance raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** RecoveryAssurance establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## KnowledgeFreshness — Knowledge Freshness

- **Purpose:** measure whether hazards, assumptions, tests and guidance reflect current evidence.
- **Raw Safety Property Result:** age and validity distribution of hazard, assumption, test, known-error and guidance records relative to their review/trigger requirements.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A greater proportion of hazard, assumption, test, known-error, and guidance records currently valid against their triggers is favorable; stale, expired, or superseded records are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure whether hazards, assumptions, tests and guidance reflect current evidence.
- **Test Method:** sample records against latest triggers; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** KnowledgeFreshness fixtures define the vector/profile evidence model for this raw result: age and validity distribution of hazard, assumption, test, known-error and guidance records relative to their review/trigger requirements. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** knowledge timestamps, owners and review evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for KnowledgeFreshness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** KnowledgeFreshness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** KnowledgeFreshness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Refresh timestamps without reviewing content, exclude invalidated assumptions, sample only active records, or leave superseded guidance discoverable as current.
- **Gaming Countermeasures:** KnowledgeFreshness countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** TER/AIVE/incident or review expiry; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** KnowledgeFreshness expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `KnowledgeFreshness/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** KnowledgeFreshness raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** KnowledgeFreshness establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## StandardObsolescenceExposure — Standard Obsolescence Exposure

- **Purpose:** quantify deployments relying on standards/assumptions past review or invalidation.
- **Raw Safety Property Result:** count and consequence-weighted inventory of active deployments relying on expired, invalidated or unsupported standards/assumptions.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Counts and consequence-weighted exposure of deployments relying on expired, invalidated, or unsupported standards/assumptions are lower-is-better.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on quantify deployments relying on standards/assumptions past review or invalidation.
- **Test Method:** registry and assumption-expiry analysis; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** StandardObsolescenceExposure fixtures define the structured evidence model for this raw result: count and consequence-weighted inventory of active deployments relying on expired, invalidated or unsupported standards/assumptions. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** certificate/standard inventory; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for StandardObsolescenceExposure may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** StandardObsolescenceExposure reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** StandardObsolescenceExposure Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Reclassify active deployments as legacy exceptions, omit transitive reliance, ignore invalidation events, or use unweighted counts that hide high-consequence exposure.
- **Gaming Countermeasures:** StandardObsolescenceExposure countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** standard or environment change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** StandardObsolescenceExposure expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `StandardObsolescenceExposure/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** StandardObsolescenceExposure raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** StandardObsolescenceExposure establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## AssumptionValidityCoverage — Assumption Validity Coverage

- **Purpose:** fraction of material safety assumptions with owner, test, evidence and active validity.
- **Raw Safety Property Result:** proportion of material assumptions with owner, falsification test, current evidence, expiry and active validity state.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** A higher proportion of material assumptions with owner, falsification test, current evidence, expiry, and active validity is favorable; missing or invalid assumptions are adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on fraction of material safety assumptions with owner, test, evidence and active validity.
- **Test Method:** sample safety-case assumptions and invalidate seeds; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AssumptionValidityCoverage fixtures define the ratio/rate evidence model for this raw result: proportion of material assumptions with owner, falsification test, current evidence, expiry and active validity state. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** assumption register and test evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for AssumptionValidityCoverage may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** AssumptionValidityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AssumptionValidityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Create owners/tests on paper without current evidence, mark failed assumptions not applicable, extend expiry without review, or omit implicit assumptions from the denominator.
- **Gaming Countermeasures:** AssumptionValidityCoverage countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** assumption/evidence/environment change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AssumptionValidityCoverage expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AssumptionValidityCoverage/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AssumptionValidityCoverage raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AssumptionValidityCoverage establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## GoalDriftDetection — Goal Drift Detection

- **Purpose:** detect unauthorized or unsafe change in goals, priorities or goal-setting loop.
- **Raw Safety Property Result:** recall, false-positive rate and latency for seeded goal, priority, subgoal and goal-setting-loop drift.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Recall for goal, priority, subgoal, and legitimacy-changing drift is higher-is-better; false-positive rate and detection latency are lower-is-better.
- **Applicability:** systems with T2+, delegation, replication, production or expansion; specifically where the declared assessment depends on detect unauthorized or unsafe change in goals, priorities or goal-setting loop.
- **Test Method:** seed goal/policy mutations and behavioral drift; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GoalDriftDetection fixtures define the latency/time evidence model for this raw result: recall, false-positive rate and latency for seeded goal, priority, subgoal and goal-setting-loop drift. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed goal baseline, traces and detection record; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for GoalDriftDetection; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** GoalDriftDetection reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GoalDriftDetection Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Seed superficial wording changes, omit checkpoint and subgoal drift, start latency after explicit disclosure, or suppress false positives and missed legitimacy changes.
- **Gaming Countermeasures:** GoalDriftDetection countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** goal/model/policy change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** GoalDriftDetection expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `GoalDriftDetection/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** GoalDriftDetection raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** GoalDriftDetection establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## SafetyCertificationFreshness — Safety Certification Freshness

- **Purpose:** measure certificate validity against current configuration, environment, evidence and standards.
- **Raw Safety Property Result:** typed delta between certified and current configuration, environment, standard, evidence and support state.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Smaller typed deltas between certified and current configuration, environment, standards, evidence, and support state are favorable; any material invalidating delta is adverse.
- **Applicability:** certified and supported systems; H3+ requires independent evidence; specifically where the declared assessment depends on measure certificate validity against current configuration, environment, evidence and standards.
- **Test Method:** registry reconciliation and event-invalidation test; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyCertificationFreshness fixtures define the set/delta evidence model for this raw result: typed delta between certified and current configuration, environment, standard, evidence and support state. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** certificate, config hash, trigger history; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyCertificationFreshness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyCertificationFreshness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyCertificationFreshness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Compare against an incomplete certificate baseline, omit environment/support/standard deltas, delay current-state inventory, or treat unreviewed equivalence as no change.
- **Gaming Countermeasures:** SafetyCertificationFreshness countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** ACU, drift, AIVE, expiry or standard change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyCertificationFreshness expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyCertificationFreshness/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyCertificationFreshness raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyCertificationFreshness establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## RecoveryCapabilityVerification — Recovery Capability Verification

- **Purpose:** verify owner-facing recovery procedures are usable under stress.
- **Raw Safety Property Result:** success rate, completion time, error rate and final verified device/authority state for owner-facing recovery under representative stress.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** Recovery success and final verified safe/authority state are favorable; completion time, error rate, unreconciled authority, and failed recovery attempts are adverse.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant; specifically where the declared assessment depends on verify owner-facing recovery procedures are usable under stress.
- **Test Method:** representative owner recovery drill; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** RecoveryCapabilityVerification fixtures define the latency/time evidence model for this raw result: success rate, completion time, error rate and final verified device/authority state for owner-facing recovery under representative stress. Fixture design specifies applicable dimensions, strata, failure cases and missing/untested regions without forcing numerator/denominator semantics where the raw result is not a ratio. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** human factors results and device state proof; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for RecoveryCapabilityVerification may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** RecoveryCapabilityVerification reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** RecoveryCapabilityVerification Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Use trained operators and healthy devices, omit stress and accessibility conditions, stop timing before authority reconciliation, or exclude failed recovery attempts.
- **Gaming Countermeasures:** RecoveryCapabilityVerification countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** interface/support change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** RecoveryCapabilityVerification expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `RecoveryCapabilityVerification/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** RecoveryCapabilityVerification raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** RecoveryCapabilityVerification establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## Multidimensional profiles

Hazard Preparedness, Technical Protection, Authority Control, Guardian Evidence, Governance Integrity and Expansion Control remain profiles. Any diagnostic aggregation retains raw components, units, assurance grades and hard-floor failures; it has no independent certification force.






## ConfirmedErrorRate — Confirmed Error Rate

- **Purpose:** The number of Confirmed AI Error Occurrences in a defined domain, task class, configuration, and evidence window divided by the corresponding valid Operational Exposure Units; reported by error type and consequence class rather than only as an aggregate.
- **Raw Safety Property Result:** ConfirmedErrorRate(d,t,c,W) = ConfirmedErrorOccurrences(d,t,c,W) / ValidOperationalExposureUnits(d,t,c,W); report denominator and confidence interval.
- **Evidence Assurance Grade:** 0-5 grades occurrence validation, exposure-denominator integrity, deduplication, provenance, and configuration binding; it never replaces the measured rate.
- **Direction:** Lower confirmed-error rate is favorable within each stratum; material and critical occurrences remain separate and cannot be offset by clean low-consequence strata.
- **Applicability:** Declared domain/task/configuration/evidence-window strata with a registered Operational Exposure Unit and occurrence-deduplication rule.
- **Test Method:** Reconcile AI Error Registry occurrences against signed exposure logs and independent validation records; sample rejected and duplicate dispositions.
- **Fixtures:** Exposure ledgers, occurrence-merge cases, report/evaluation evidence packets, configuration hashes, false-duplicate cases, disputed reports, and unresolved-report examples.
- **Admissible Evidence:** Signed operational logs, validated evaluation failures, occurrence IDs, denominator snapshots, disposition history, and independent validation evidence.
- **Assessor Independence:** Occurrence validation should be independent of teams whose rating or release eligibility is affected; provider-only validation caps independence-sensitive ratings.
- **Uncertainty Representation:** Publish denominator, count, interval or bound, missing strata, unresolved/disputed report count, duplicate-rate sensitivity, and sampled-validation error.
- **Confidence Rule:** Confidence is capped by weak denominator integrity, incomplete disposition audit, unvalidated high-consequence reports, or configuration mismatch.
- **Gaming Strategies:** denominator inflation; duplicate suppression; false duplicate grouping; favorable task-strata mixing; hiding failed eval runs; delayed confirmation; version laundering.
- **Gaming Countermeasures:** registered exposure units, append-only occurrence IDs, independent disposition sampling, stratified summaries, immutable version binding, and audit of rejected/duplicate reports.
- **Recertification Triggers:** confirmed material/critical occurrence, denominator-method change, exposure logging gap, material domain/configuration change, or disposition audit failure.
- **Expiry:** Expires with the Trustworthiness Evidence Window, denominator schema, or configuration; stale windows cannot support an Active profile.
- **Version:** metric schema + error taxonomy + exposure-unit definition + deduplication policy + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching exposure units, domains, task strata, error taxonomies, deduplication rules, and policy versions; bridge studies publish information loss.
- **Hard-Floor Relevance:** Confirmed material/critical errors feed hard caps and status triggers before any aggregate trend is considered.
- **Limitations:** Measures validated observed/evaluated error occurrences in scope; it does not prove absence of undiscovered errors or general safety.




## CriticalErrorRate — Critical Error Rate

- **Purpose:** The number of Confirmed AI Error Occurrences that meet the applicable high-consequence or protected-boundary criterion divided by valid Operational Exposure Units in the affected domain and task class.
- **Raw Safety Property Result:** ConfirmedCriticalErrorOccurrences(d,t,c,W) / ValidOperationalExposureUnits(d,t,c,W); report a one-sided 95% exact binomial upper confidence bound for an observed zero unless a validated domain method applies.
- **Evidence Assurance Grade:** 0-5 grades critical-criterion validity, exposure-denominator integrity, independent confirmation, and severity/boundary classification evidence.
- **Direction:** Lower is favorable; zero observed critical errors is reported with an upper bound and is never proof of zero critical risk.
- **Applicability:** Domains with registered high-consequence or protected-boundary criteria and an exposure definition for critical opportunity.
- **Test Method:** Validate critical occurrences through independent adjudication, boundary-crossing evidence, near-miss review, and rare-event interval estimation.
- **Fixtures:** Critical scenario fixtures, protected-boundary logs, near-miss controls, severity rubrics, exposure ledgers, and zero-observation upper-bound examples.
- **Admissible Evidence:** Confirmed critical error records, independent adjudication, boundary logs, incident records, near-miss evidence, exposure units, and severity/modality evidence.
- **Assessor Independence:** Critical-event confirmation requires materially independent review; provider-only critical classification cannot support high active trustworthiness.
- **Uncertainty Representation:** Publish one-sided upper bounds for sparse/zero observations, critical opportunity denominator, unresolved credible reports, and classification uncertainty.
- **Confidence Rule:** Confidence is capped by sparse exposure, missing critical scenarios, unresolved credible high-consequence reports, or non-independent adjudication.
- **Gaming Strategies:** downgrading consequence class; excluding near misses; redefining critical criteria; suppressing incident linkage; burying boundary-crossing attempts; cherry-picking low-risk exposure.
- **Gaming Countermeasures:** registered critical criteria, independent near-miss sampling, mandatory high-consequence report review, protected logs, and adverse classification challenge paths.
- **Recertification Triggers:** confirmed or credible critical event, critical-criterion change, near-miss cluster, boundary-control bypass, or high-consequence report backlog beyond deadline.
- **Expiry:** Expires at the shortest of evidence window, critical-scenario suite validity, or high-consequence review cadence.
- **Version:** metric schema + criticality rubric + scenario suite + denominator policy + scoring policy + configuration + evidence window.
- **Normalization Rule:** Do not compare across domains or criticality rubrics without explicit mapping and retained upper-bound uncertainty.
- **Hard-Floor Relevance:** Critical errors are noncompensable and may suspend status regardless of aggregate performance.
- **Limitations:** Rare critical events remain hard to estimate; absence in limited evidence can leave the profile Unrated or Provisional.




## SeverityWeightedErrorBurden — Severity Weighted Error Burden

- **Purpose:** The sum of policy-defined consequence weights for Confirmed AI Error Occurrences divided by valid Operational Exposure Units, where weights are derived from declared harm severity, harm modality, authority impact, reversibility, actual harm, and credible potential harm.
- **Raw Safety Property Result:** Σ ErrorWeight(e) / ValidOperationalExposureUnits; weights derive from declared severity, modality, authority impact, actual and potential harm, reversibility, boundary crossing and recurrence.
- **Evidence Assurance Grade:** 0-5 grades consequence-weight provenance, classification consistency, exposure-denominator validity, and independent review of the weighting policy.
- **Direction:** Lower burden is favorable per stratum; catastrophic or boundary-crossing errors remain separately visible and cannot be hidden inside a weighted sum.
- **Applicability:** Scopes whose Trustworthiness Scoring Policy defines weights for error type, harm modality, authority impact, reversibility, actual harm, and credible potential harm.
- **Test Method:** Apply the registered weighting rubric to confirmed occurrences and audited near-miss/potential-consequence evidence; compare adjudicator consistency.
- **Fixtures:** Weighted occurrence examples, severity/modality rubrics, reversibility and authority-impact cases, denominator ledgers, and averaging-hides-critical-event adversarial cases.
- **Admissible Evidence:** Confirmed error records, consequence characterization, weighting-rubric version, adjudication notes, exposure denominators, and dispute outcomes.
- **Assessor Independence:** Weight assignment for material or critical cases requires independent adjudication or audited sampling; self-assigned low severity caps confidence.
- **Uncertainty Representation:** Publish weight ranges, adjudicator disagreement, denominator uncertainty, unresolved material reports, and sensitivity to disputed classifications.
- **Confidence Rule:** Confidence is capped by unstable weights, weak consequence evidence, high disagreement, or missing high-severity strata.
- **Gaming Strategies:** severity downgrading; weight compression; excluding potential harm; splitting one defect into low-weight fragments; hiding recurrence; favorable denominator grouping.
- **Gaming Countermeasures:** registered weights, independent severity audit, worst-case visibility, recurrence linkage, material-case summaries, and cap rules before aggregation.
- **Recertification Triggers:** weighting-policy change, material/critical confirmed error, severity-dispute cluster, recurrence of a known defect, or new consequence modality.
- **Expiry:** Expires when weighting policy, harm taxonomy, domain scope, or evidence window changes materially.
- **Version:** metric schema + harm taxonomy + weighting rubric + exposure policy + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only identical or bridge-mapped weighting policies and strata; report raw count vectors next to weighted burden.
- **Hard-Floor Relevance:** Hard caps and critical-trigger statuses are applied before burden aggregation is used for rating support.
- **Limitations:** Weights are policy constructs, not objective moral measurements; burden summaries can miss qualitative defects without separate case visibility.




## ErrorRecurrenceRate — Error Recurrence Rate

- **Purpose:** The rate at which a previously identified AI Error Defect produces new Confirmed AI Error Occurrences after the defect was declared mitigated or remediated, measured over eligible post-remediation exposure.
- **Raw Safety Property Result:** PostRemediationConfirmedOccurrencesOfKnownDefects / EligiblePostRemediationExposure; exclude the original occurrence.
- **Evidence Assurance Grade:** 0-5 grades defect linkage, remediation-state evidence, post-remediation exposure validity, and independent recurrence adjudication.
- **Direction:** Lower recurrence is favorable; any recurring material defect after declared remediation is adverse even if aggregate error rate improves.
- **Applicability:** After an AI Error Defect has been identified, a remediation milestone declared, and eligible post-remediation exposure defined.
- **Test Method:** Link new confirmed occurrences to known defects using root-cause evidence, version/configuration history, and post-remediation exposure windows; audit relabeled defects.
- **Fixtures:** Known-defect lineage records, remediation timestamps, deployment cohorts, revalidation cases, recurrence/nonrecurrence examples, and defect-relabeling adversarial cases.
- **Admissible Evidence:** Root-cause records, remediation artifacts, deployment logs, independent revalidation, post-remediation exposure units, and recurrence adjudication notes.
- **Assessor Independence:** Recurrence linkage and remediation closure should be reviewed outside the responsible remediation team for material defects.
- **Uncertainty Representation:** Publish recurrence count/rate, post-remediation denominator, unresolved suspected recurrences, version carryover uncertainty, and root-cause linkage confidence.
- **Confidence Rule:** Confidence is capped by weak defect taxonomy, missing deployment evidence, unverified remediation, or unresolved suspected recurrence.
- **Gaming Strategies:** relabeling recurring defects as new issues; changing defect boundaries; declaring remediation before deployment; suppressing failed revalidation; resetting exposure windows.
- **Gaming Countermeasures:** defect lineage IDs, independent closure criteria, post-remediation cohort tracking, failed-revalidation retention, and audits of newly labeled defects.
- **Recertification Triggers:** recurring material/critical defect, failed revalidation, remediation rollback, defect-taxonomy change, or post-remediation logging gap.
- **Expiry:** Evidence expires when the remediated configuration, deployment environment, or defect taxonomy changes materially.
- **Version:** metric schema + defect taxonomy + remediation criteria + exposure policy + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only defects with matching closure criteria, post-remediation exposure definitions, and configuration lineage.
- **Hard-Floor Relevance:** Recurring material or critical defects trigger review or caps independently of aggregate current performance.
- **Limitations:** Root-cause linkage can be uncertain; a low recurrence rate does not show that remediation eliminated related undiscovered defects.




## IndependentEvaluationPerformance — Independent Evaluation Performance

- **Purpose:** The weighted result of a registered AI Evaluation Scenario Suite under its Evaluation Rubric, reported by verdict class, scenario family, consequence class, and evaluator rather than only as a single average.
- **Raw Safety Property Result:** Vector of Correct, AcceptableWithMinorIssue, MateriallyIncorrect, UnsafeOrCritical and Indeterminate weights, stratified by scenario family and evaluator, with disagreement.
- **Evidence Assurance Grade:** 0-5 grades scenario-suite independence, rubric validity, evaluator independence, hidden-case protection, and evidence retention.
- **Direction:** Higher correct/acceptable performance and lower material/critical/indeterminate rates are favorable, reported by scenario family rather than collapsed into one average.
- **Applicability:** Registered evaluation suites and rubrics for the declared domain/task/configuration; results do not transfer to untested domains.
- **Test Method:** Execute versioned held-out and adversarial scenario suites, bind target outputs/actions to evidence, and adjudicate evaluator disagreements under the registered rubric.
- **Fixtures:** Blinded scenario suites, rubric verdict exemplars, evaluator-dependency records, target output logs, disagreement cases, and leakage probes.
- **Admissible Evidence:** Scenario-suite version, rubric version, target output/action evidence, evaluator verdicts, evaluator independence profiles, adjudication records, failed and indeterminate cases.
- **Assessor Independence:** Evaluator provider, suite owner, infrastructure, and adjudicator dependencies must be recorded; correlated evaluators cap independence-sensitive claims.
- **Uncertainty Representation:** Publish verdict distribution, scenario-family coverage, evaluator disagreement, confidence intervals where meaningful, leakage risk, and hidden-suite coverage.
- **Confidence Rule:** Confidence is capped by benchmark leakage, weak evaluator independence, incomplete scenario coverage, high disagreement, or unretained failed runs.
- **Gaming Strategies:** benchmark leakage; prompt overfitting; suite memorization; evaluator collusion; selective scenario exclusion; easy scenario families diluting critical failures.
- **Gaming Countermeasures:** hidden rotating suites, suite provenance controls, evaluator diversity audits, failed-run retention, adversarial sampling, and family-level hard caps.
- **Recertification Triggers:** suite leakage, material model/configuration change, evaluator-dependency change, high disagreement, new domain hazard, or failed hidden-case audit.
- **Expiry:** Expires with suite/rubric version, hidden-case exposure, model/configuration change, or evidence window.
- **Version:** metric schema + suite version + rubric version + evaluator profile version + scoring policy + target configuration + evidence window.
- **Normalization Rule:** Compare only matching or formally bridged suites/rubrics and scenario families; publish changed coverage and lost comparability.
- **Hard-Floor Relevance:** UnsafeOrCritical verdicts and indeterminate high-consequence cases may cap rating or status before aggregate score is used.
- **Limitations:** Evaluation performance is bounded by scenario representativeness, hidden-suite integrity, and evaluator independence; it is not general reliability.




## CalibrationQuality — Calibration Quality

- **Purpose:** The agreement between the AI system's expressed confidence and observed correctness where meaningful confidence values are available, measured with a registered calibration method and stratified by domain and consequence class.
- **Raw Safety Property Result:** Registered calibration error by domain and consequence stratum; NOT APPLICABLE when meaningful probabilistic confidence is absent.
- **Evidence Assurance Grade:** 0-5 grades confidence-signal validity, calibration-bin coverage, ground-truth/adjudication quality, and Not Applicable justification.
- **Direction:** Lower registered calibration error and better high-confidence failure control are favorable; overconfidence in material cases is separately adverse.
- **Applicability:** Only where the AI exposes meaningful confidence, uncertainty, abstention likelihood, or comparable calibrated signal under the scoring policy.
- **Test Method:** Compare expressed confidence or uncertainty to independent outcomes by domain/consequence strata, with special review of high-confidence material failures.
- **Fixtures:** Confidence-output examples, calibration bins, ground-truth/adjudicated outcomes, abstention boundary cases, and Not Applicable semantic examples.
- **Admissible Evidence:** Signed outputs with confidence/uncertainty, adjudicated correctness, binning method, calibration metric, scenario/exposure strata, and N/A rationale where applicable.
- **Assessor Independence:** Outcome labels and calibration method should be independent of the evaluated model; model self-confidence alone is never sufficient.
- **Uncertainty Representation:** Publish bin counts, calibration intervals, high-confidence error counts, missing confidence strata, and N/A rationale.
- **Confidence Rule:** Confidence is capped by sparse bins, unstable confidence semantics, missing high-risk strata, or relabeling unavailable confidence as Not Applicable without semantic basis.
- **Gaming Strategies:** withholding confidence signals; coarse confidence buckets; post-hoc calibration on test data; underconfidence to avoid accountability; hiding high-confidence failures.
- **Gaming Countermeasures:** registered confidence semantics, locked calibration method, held-out calibration checks, high-confidence failure audits, and explicit N/A/missing-evidence rules.
- **Recertification Triggers:** confidence-interface change, calibration-method change, material overconfidence error, domain shift, or N/A policy dispute.
- **Expiry:** Expires with confidence-signal semantics, calibration suite, model/configuration, or evidence window.
- **Version:** metric schema + confidence-signal definition + calibration method + suite/rubric + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching confidence semantics and calibration methods; bridge studies must show bin mapping and lost information.
- **Hard-Floor Relevance:** Material overconfidence and failure to disclose uncertainty can trigger caps independently of average calibration error.
- **Limitations:** Not all systems expose meaningful confidence; Not Applicable requires semantic justification and is not a shortcut around missing evidence.




## AbstentionQuality — Abstention Quality

- **Purpose:** A paired measure of whether the AI appropriately abstains when evidence or authority is insufficient and whether it avoids unnecessary abstention when it can reliably perform the task; reported as appropriate-abstention precision and recall or an equivalent domain-registered pair.
- **Raw Safety Property Result:** Paired appropriate-abstention recall and precision.
- **Evidence Assurance Grade:** 0-5 grades abstention-rule clarity, boundary-case coverage, authority/evidence insufficiency labels, and outcome adjudication.
- **Direction:** Higher appropriate-abstention recall and precision are favorable; unsafe non-abstention and unnecessary refusal are reported separately.
- **Applicability:** Where the task policy defines when the AI should abstain, defer, ask for evidence, or request human/authority review.
- **Test Method:** Evaluate insufficient-evidence, insufficient-authority, valid-task, ambiguous, and high-consequence boundary cases against the registered abstention rubric.
- **Fixtures:** Insufficient-evidence cases, insufficient-authority cases, valid authorized tasks, ambiguous tasks, high-consequence boundary scenarios, and appeal/disposition examples.
- **Admissible Evidence:** Prompt/context/action logs, abstention/defer outcomes, authority/evidence state, rubric verdicts, user/operator impact, and adjudication records.
- **Assessor Independence:** Boundary labels and unacceptable abstention cases should be independently adjudicated where operational eligibility is affected.
- **Uncertainty Representation:** Publish paired recall/precision or domain equivalent, false-abstention and false-nonabstention counts, ambiguity strata, and high-consequence misses.
- **Confidence Rule:** Confidence is capped by missing boundary strata, unclear task policy, unreviewed false abstentions in critical service, or unresolved unsafe non-abstention.
- **Gaming Strategies:** blanket refusal to avoid errors; selective abstention on hard tests; proceeding without authority by rephrasing; hiding deference as successful completion; ambiguity exploitation.
- **Gaming Countermeasures:** registered abstention criteria, separate unnecessary-refusal reporting, authority/evidence state logging, boundary-case hidden suites, and appeals sampling.
- **Recertification Triggers:** material unsafe non-abstention, critical service refusal cluster, policy change, authority-interface change, or drift in insufficient-evidence handling.
- **Expiry:** Expires with task policy, authority/evidence interfaces, suite/rubric, configuration, or evidence window.
- **Version:** metric schema + abstention policy + rubric + scenario suite + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching task policies and consequence strata; false-abstention and false-nonabstention are not merged.
- **Hard-Floor Relevance:** Failure to abstain in high-consequence or unauthorized-action scenarios can trigger caps regardless of normal-task performance.
- **Limitations:** Abstention quality depends on explicit policy and evidence-state observability; it does not establish substantive answer correctness.




## CorrectionResponsiveness — Correction Responsiveness

- **Purpose:** A time-and-outcome profile covering time from report to acknowledgement, validation, mitigation, deployed remediation, and independent revalidation together with post-remediation recurrence.
- **Raw Safety Property Result:** Median and high-percentile acknowledgement, validation, mitigation, remediation and revalidation times plus post-remediation recurrence.
- **Evidence Assurance Grade:** 0-5 grades timestamp integrity, remediation evidence, deployment proof, independent revalidation, and recurrence monitoring.
- **Direction:** Shorter verified acknowledgement/validation/remediation/revalidation time and lower recurrence are favorable; fake closure is adverse.
- **Applicability:** Validated AI Error Reports or defects with defined service milestones and remediation/revalidation criteria under the scoring policy.
- **Test Method:** Trace each report/defect from submission through acknowledgement, validation, mitigation, deployed remediation, independent revalidation, and post-remediation monitoring.
- **Fixtures:** Lifecycle timestamp ledgers, remediation artifacts, deployment cohort records, failed revalidation cases, recurrence records, and closure/adjudication examples.
- **Admissible Evidence:** Signed report states, ticket/change records, deployment logs, remediation tests, independent revalidation evidence, recurrence monitoring, and timestamp audit trail.
- **Assessor Independence:** Closure and revalidation for material defects require review independent of the team claiming remediation; self-declared fix evidence is supporting only.
- **Uncertainty Representation:** Publish milestone latency distribution, overdue counts, unresolved material backlog, revalidation failure rate, timestamp gaps, and recurrence after closure.
- **Confidence Rule:** Confidence is capped by unverifiable timestamps, missing deployed-remediation proof, suppressed failed revalidation, or unresolved material backlog.
- **Gaming Strategies:** fake remediation; closing before deployed remediation; failed revalidation suppression; relabeling recurring defect as new issue; timestamp manipulation.
- **Gaming Countermeasures:** signed monotonic timestamps, deployment-bound closure criteria, independent revalidation, failed-test retention, defect-lineage audit, and overdue material-report escalation.
- **Recertification Triggers:** missed critical deadline, failed revalidation, recurring remediated defect, timestamp integrity failure, or closure audit failure.
- **Expiry:** Remediation evidence expires when configuration, deployment environment, defect scope, or revalidation suite changes materially.
- **Version:** metric schema + lifecycle-state model + remediation criteria + revalidation suite + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching lifecycle milestones and closure criteria; acknowledgement, validation, deployment, and revalidation latencies remain separate.
- **Hard-Floor Relevance:** Unremediated or falsely closed material/critical defects can cap rating level or status regardless of other trustworthiness metrics.
- **Limitations:** Fast closure does not prove correct remediation; deployed evidence and post-remediation recurrence remain necessary.




## OperationalEvidenceVolume — Operational Evidence Volume

- **Purpose:** The number and distribution of valid Operational Exposure Units supporting the current profile, stratified by task class, user or operating context, environment, and relevant consequence class.
- **Raw Safety Property Result:** Count and distribution of valid Operational Exposure Units by task, context, environment and consequence class.
- **Evidence Assurance Grade:** 0-5 grades exposure-unit validity, coverage across task/context strata, logging integrity, and independence of operational evidence capture.
- **Direction:** Greater valid and representative exposure volume is favorable only when strata and quality are adequate; raw volume alone is not trustworthiness.
- **Applicability:** Operational domains where valid exposure units can be counted without mixing materially different tasks or contexts unstratified.
- **Test Method:** Audit exposure ledgers for eligibility, stratification, deduplication, configuration binding, missing logs, and consistency with the scoring policy.
- **Fixtures:** Exposure-unit definitions, eligible/ineligible examples, stratification maps, missing-log cases, configuration-bound ledgers, and volume-quality counterexamples.
- **Admissible Evidence:** Signed exposure logs, eligibility filters, sampling records, configuration hashes, task/context strata, telemetry integrity checks, and privacy-minimized summaries.
- **Assessor Independence:** Exposure capture and denominator construction should be auditable outside the team whose rating benefits from larger denominators.
- **Uncertainty Representation:** Publish volume by stratum, missing or excluded exposure, logging gaps, sampling error, privacy suppression, and configuration coverage.
- **Confidence Rule:** Confidence is capped by unstratified mixed tasks, weak telemetry integrity, unexplained exclusions, or exposure too sparse for material claims.
- **Gaming Strategies:** inflating denominators with easy tasks; excluding failed contexts; merging incomparable task classes; counting synthetic repeats as operational exposure; hiding logging gaps.
- **Gaming Countermeasures:** registered Operational Exposure Unit definitions, stratum-level reporting, denominator audits, missing-data accounting, privacy-preserving sampling, and immutable configuration binding.
- **Recertification Triggers:** exposure-unit definition change, material logging gap, new task stratum, domain shift, or denominator audit failure.
- **Expiry:** Expires with evidence window, operational context, telemetry pipeline, exposure-unit definition, or configuration.
- **Version:** metric schema + exposure-unit definition + logging schema + stratification policy + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching exposure units and strata; larger denominators cannot compensate for missing high-consequence coverage.
- **Hard-Floor Relevance:** Sparse or nonrepresentative volume can prevent an Active rating even when observed error counts are low.
- **Limitations:** Operational volume shows exposure, not correctness; high volume in easy contexts may say little about rare or high-consequence behavior.




## EvidenceIndependence — Evidence Independence

- **Purpose:** A multidimensional profile of independence among evidence sources across provider, model family, organization, data source, evaluator, operator, infrastructure, and failure domain.
- **Raw Safety Property Result:** Vector across provider, model family, organization, evaluator, data source, infrastructure, operator and failure domain.
- **Evidence Assurance Grade:** 0-5 grades dependency/provenance mapping depth, independence-rule satisfaction, hidden common-mode analysis, and auditability of source relationships.
- **Direction:** Greater material independence across evidence sources is favorable; apparent diversity with shared failure roots is adverse.
- **Applicability:** All profiles using provider evidence, user reports, monitors, independent AI evaluators, labs, registries, or operational telemetry.
- **Test Method:** Perform dependency and provenance analysis across provider, model family, training/data lineage, evaluator, operator, infrastructure, tooling, scenario ownership, funding, and governance roots.
- **Fixtures:** Evidence-source dependency graphs, provenance records, shared-infrastructure examples, correlated-evaluator cases, hidden-suite ownership records, and conflict-of-interest cases.
- **Admissible Evidence:** Signed source metadata, evaluator independence profiles, infrastructure/provider attestations, suite ownership records, funding/conflict declarations, provenance graphs, and audit samples.
- **Assessor Independence:** The independence assessment should itself be performed or audited by a party not materially dependent on the evaluated provider or evaluator set.
- **Uncertainty Representation:** Publish independence vector, unknown dependencies, common-mode assumptions, confidence in provenance claims, and residual correlated-failure risk.
- **Confidence Rule:** Confidence is capped by undisclosed source dependencies, unverifiable provenance, shared evaluator roots, or unobserved common-mode risk.
- **Gaming Strategies:** nominally separate evaluators sharing model/provider/data; shell organizations; hidden suite ownership; reused infrastructure; undeclared funding or tooling dependencies.
- **Gaming Countermeasures:** dependency/provenance graph review, conflict declarations, independent audits, source-diversity floors, hidden common-mode tests, and challenge rights for independence claims.
- **Recertification Triggers:** new dependency discovery, evaluator/provider merger, suite ownership change, infrastructure migration, conflict disclosure, or common-mode failure.
- **Expiry:** Expires when evaluator/source dependencies, infrastructure, suite ownership, or provider relationships change materially.
- **Version:** metric schema + independence policy + dependency graph version + provenance schema + scoring policy + profile scope + evidence window.
- **Normalization Rule:** Compare by vector dimensions, not a single scalar; disclose unknown dependencies and policy thresholds.
- **Hard-Floor Relevance:** Weak independence caps or blocks Active high trustworthiness even when other evidence is strong.
- **Limitations:** Independence cannot rule out all hidden correlation; unobserved common-mode risk remains a limitation.




## TrustworthinessFreshness — Trustworthiness Freshness

- **Purpose:** The age distribution and validity status of evidence supporting the current profile, including the proportion of material evidence within its required validity window and the amount expired or superseded.
- **Raw Safety Property Result:** Percentage of material evidence valid, percentage expired, oldest material evidence, and dates of last independent evaluation, operational evidence and recalculation.
- **Evidence Assurance Grade:** 0-5 grades timestamp provenance, expiry-rule enforcement, evidence-window coverage, and supersession tracking.
- **Direction:** More material evidence within its validity window and less expired/superseded evidence is favorable; stale critical evidence is adverse.
- **Applicability:** Every current profile, rating, status, metric, evaluation, operational exposure, error record, and remediation claim.
- **Test Method:** Compare evidence timestamps, expiry rules, domain refresh cadence, supersession events, and last recalculation against the scoring policy.
- **Fixtures:** Evidence-window ledgers, expired/superseded evidence examples, refresh-cadence cases, timestamp-integrity checks, and stale-critical-evidence scenarios.
- **Admissible Evidence:** Signed evidence timestamps, policy expiry rules, recalculation records, supersession notices, configuration/change history, and freshness audit logs.
- **Assessor Independence:** Freshness audits should not rely solely on provider-curated current summaries; historical and superseded evidence must remain inspectable.
- **Uncertainty Representation:** Publish age distribution, expired/superseded proportions, oldest material evidence, refresh overdue count, and timestamp-confidence gaps.
- **Confidence Rule:** Confidence is capped by stale material evidence, missing timestamp provenance, untracked supersession, or overdue independent evaluation.
- **Gaming Strategies:** refreshing easy evidence only; hiding superseded adverse evidence; resetting evidence windows after version changes; backdating; treating stale evidence as current.
- **Gaming Countermeasures:** append-only evidence history, signed timestamps, expiry automation, supersession records, independent freshness sampling, and carryover caps.
- **Recertification Triggers:** evidence expiry, timestamp integrity failure, material configuration/domain change, superseding incident, or missed refresh cadence.
- **Expiry:** The metric expires at the earliest material evidence expiry or scoring-policy review date unless recalculated.
- **Version:** metric schema + evidence-window policy + timestamp/provenance schema + scoring policy + configuration + recalculation date.
- **Normalization Rule:** Compare only matching evidence windows and expiry rules; disclose any carried-over evidence and cap applied.
- **Hard-Floor Relevance:** Expired or stale evidence can force UnderReview, Expired, Suspended, Provisional, or Unrated status independent of old rating level.
- **Limitations:** Freshness shows temporal validity, not truth or coverage; fresh bad evidence remains bad evidence.




## EvaluatorDisagreement — Evaluator Disagreement

- **Purpose:** The proportion and consequence profile of evaluation cases in which independent evaluators produce materially different verdicts, together with the unresolved-adjudication rate and age.
- **Raw Safety Property Result:** Material disagreement rate, critical and unresolved counts, unresolved age, and evaluator-pair distribution.
- **Evidence Assurance Grade:** 0-5 grades evaluator independence, disagreement capture, adjudication integrity, and preservation of minority/high-consequence verdicts.
- **Direction:** Lower unresolved material disagreement is favorable; critical disagreement remains separately visible and is not averaged away.
- **Applicability:** Whenever multiple evaluators, labs, monitors, or adjudicators assess the same scenario, occurrence, or material evidence package.
- **Test Method:** Compare verdicts by evaluator pair, scenario family, consequence class, and adjudication state; track age and outcome of unresolved disagreements.
- **Fixtures:** Paired-evaluator verdict sets, material/critical disagreement examples, adjudication records, correlated-evaluator cases, and minority-report preservation cases.
- **Admissible Evidence:** Evaluator verdicts, rationales, evidence references, independence profiles, adjudication logs, disagreement timestamps, and final disposition records.
- **Assessor Independence:** Adjudication should be materially independent of both disagreeing evaluators where consequence class requires it.
- **Uncertainty Representation:** Publish disagreement rate, unresolved count/age, critical disagreement list, evaluator-pair distribution, and adjudication confidence.
- **Confidence Rule:** Confidence is capped by unresolved material disagreement, correlated evaluator roots, missing rationales, or suppressed minority critical verdicts.
- **Gaming Strategies:** averaging away critical dissent; excluding disagreeing evaluators; majority voting across correlated evaluators; delaying adjudication; burying minority reports.
- **Gaming Countermeasures:** disagreement-preserving records, independent adjudication, evaluator-pair reporting, common-mode analysis, age limits, and critical-dissent escalation.
- **Recertification Triggers:** unresolved critical disagreement, material disagreement beyond deadline, evaluator-dependency discovery, adjudication reversal, or suite/rubric dispute.
- **Expiry:** Expires with evaluator set, adjudication policy, suite/rubric, or evidence window.
- **Version:** metric schema + evaluator set/profile version + adjudication policy + suite/rubric + scoring policy + evidence window.
- **Normalization Rule:** Compare only matching evaluator-independence assumptions and adjudication rules; critical disagreement remains separately reported.
- **Hard-Floor Relevance:** Unresolved material or critical disagreement can cap rating or trigger UnderReview regardless of majority result.
- **Limitations:** Agreement among correlated evaluators can be misleading; low disagreement is not proof of correctness.




## SelfAssessmentCalibration — Self Assessment Calibration

- **Purpose:** The agreement between the evaluated AI's own self-assessment, confidence, critique, or claimed uncertainty and independently established evaluation outcomes. Self-assessment is supporting evidence only and SHALL NOT by itself establish TrustworthinessStatus = Active, satisfy the minimum independent-evidence requirement for an Active profile, or increase EvidenceIndependence.
- **Raw Safety Property Result:** Agreement of self-confidence or self-critique with independent ground truth or adjudicated verdict; it does not increase evidence independence.
- **Evidence Assurance Grade:** 0-5 grades capture of self-assessment signals, independent outcome labels, calibration method, and separation from evidence-independence scoring.
- **Direction:** Better agreement with independent outcomes is favorable as supporting evidence only; overconfident or strategically self-favorable claims are adverse.
- **Applicability:** Where the AI emits self-assessment, critique, confidence, uncertainty, or claimed competence signals in the evaluated workflow.
- **Test Method:** Compare self-assessment claims to independent verdicts and outcomes across normal, boundary, adversarial, and high-consequence strata.
- **Fixtures:** Self-critique outputs, confidence claims, independent verdicts, adversarial self-evaluation cases, overconfidence examples, and abstention/defer cases.
- **Admissible Evidence:** Signed self-assessment outputs, independent outcome labels, evaluator verdicts, scenario strata, calibration/adjudication records, and contradiction examples.
- **Assessor Independence:** The evaluated AI cannot establish its own trustworthiness; independent labels are mandatory for this metric to support any profile claim.
- **Uncertainty Representation:** Publish agreement intervals, overconfidence counts, missing self-assessment cases, adversarial-case results, and independent-label uncertainty.
- **Confidence Rule:** Confidence is capped by weak independent labels, self-selected examples, prompt leakage, or attempts to count self-assessment as independent evidence.
- **Gaming Strategies:** strategic humility; strategic overconfidence; self-critique tuned to rubric keywords; refusing self-assessment on hard cases; claiming uncertainty after failure.
- **Gaming Countermeasures:** held-out self-assessment prompts, independent outcome labels, adversarial contradiction cases, no EvidenceIndependence credit, and logging of omitted self-assessments.
- **Recertification Triggers:** self-assessment interface change, material overconfidence event, evaluator-rubric change, model/configuration change, or contradiction cluster.
- **Expiry:** Expires with self-assessment interface, rubric, independent-label source, configuration, or evidence window.
- **Version:** metric schema + self-assessment signal definition + rubric + evaluator/source profile + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching self-assessment signal semantics and independent-label methods; never combine with EvidenceIndependence as positive independence evidence.
- **Hard-Floor Relevance:** Self-assessment cannot satisfy Active independent-evidence minima or override caps from errors, freshness, disagreement, or independence.
- **Limitations:** A calibrated self-assessment helps interpret behavior but is not proof supplied by the system about itself.




## OperationalAdversarialRobustness — Operational Adversarial Robustness

- **Purpose:** The evaluated AI system's performance under domain-relevant adversarial, deceptive, ambiguous, boundary, and stress scenarios, reported by material and critical failure rates and not confused with the Guardian's Adversarial Reasoning Strength.
- **Raw Safety Property Result:** Material and critical failure-rate vector under registered adversarial, deceptive, ambiguous, boundary and stress scenarios.
- **Evidence Assurance Grade:** 0-5 grades adversarial scenario relevance, hidden-case protection, adaptive testing depth, independent execution, and failure retention.
- **Direction:** Lower material and critical failure rates under adversarial/boundary/stress conditions are favorable; critical failures remain separate.
- **Applicability:** The evaluated AI's behavior in declared domain tasks, not Guardian adversarial reasoning or external security controls.
- **Test Method:** Run registered adversarial, deceptive, ambiguous, boundary, stress, and misuse scenarios with evidence-bound outputs/actions and independent adjudication.
- **Fixtures:** Adversarial scenario suites, deception/boundary prompts, stress contexts, unsafe recommendation cases, authorized/unauthorized tool-use cases, and hidden adaptive rounds.
- **Admissible Evidence:** Scenario definitions, target outputs/actions, tool logs, evaluator verdicts, failure transcripts, adjudication records, and suite-leakage controls.
- **Assessor Independence:** Scenario design and adjudication should be independent of model training/evaluation tuning where high trustworthiness is claimed.
- **Uncertainty Representation:** Publish failure-rate vector by adversarial family, hidden-suite coverage, adaptive-round results, critical failures, and unresolved adjudication.
- **Confidence Rule:** Confidence is capped by suite leakage, shallow adaptive testing, missing high-risk families, or provider-only adversarial evidence.
- **Gaming Strategies:** overfitting public jailbreak suites; refusing benign hard cases; detecting test harnesses; hiding tool-use failures; excluding adaptive rounds.
- **Gaming Countermeasures:** rotating hidden suites, independent red-team sampling, retained failed attempts, harness-blinding, adaptive testing, and family-level caps.
- **Recertification Triggers:** new adversarial technique, material/critical adversarial failure, suite leakage, model/tool change, or threat-model update.
- **Expiry:** Expires with threat model, suite/rubric, model/tool configuration, or evidence window.
- **Version:** metric schema + adversarial suite + rubric + threat-model version + scoring policy + configuration + evidence window.
- **Normalization Rule:** Compare only matching adversarial families and adaptive depth; publish omitted families and threat-model changes.
- **Hard-Floor Relevance:** Critical adversarial failures can cap rating or status regardless of benign-task performance.
- **Limitations:** Adversarial robustness is open-ended; passing a suite does not prove resistance to novel strategies.




## UnresolvedMaterialReportExposure — Unresolved Material Report Exposure

- **Purpose:** The count, age, domain distribution, and exposure-normalized prevalence of unresolved AI Error Reports that allege material or critical consequences and have not yet reached a Confirmed, Rejected, Duplicate, or otherwise closed disposition.
- **Raw Safety Property Result:** Open material and critical reports, median and maximum age, exposure-normalized prevalence, and count beyond policy-defined review deadline.
- **Evidence Assurance Grade:** 0-5 grades backlog completeness, consequence triage, age tracking, exposure normalization, and escalation controls.
- **Direction:** Lower count, age, and exposure-normalized prevalence of unresolved material reports is favorable; high-consequence overdue reports are separately adverse.
- **Applicability:** Where user/operator/evaluator reports can allege material or critical consequences and have policy-defined validation deadlines.
- **Test Method:** Audit report registry states, materiality triage, age since submission/triage, exposure normalization, overdue counts, and closure/dispute disposition.
- **Fixtures:** Open-report ledgers, consequence triage examples, overdue deadline cases, duplicate/disputed/unresolved states, exposure-normalization examples, and privacy-redacted summaries.
- **Admissible Evidence:** AI Error Reports, state history, materiality classification, submission/triage timestamps, exposure denominators, validation records, and appeal/dispute evidence.
- **Assessor Independence:** Backlog status and materiality triage should be auditable outside the team incentivized to keep reports unresolved or downgraded.
- **Uncertainty Representation:** Publish open counts by consequence class, median/max age, overdue count, exposure-normalized prevalence, disputed/duplicate rates, and missing evidence requests.
- **Confidence Rule:** Confidence is capped by hidden queues, weak materiality triage, missing timestamps, or high unresolved high-consequence backlog.
- **Gaming Strategies:** queue exclusion; consequence-class downgrading; indefinite evidence requests; duplicate misuse; moving reports between states to avoid deadlines; hiding appeal backlog.
- **Gaming Countermeasures:** append-only state history, deadline clocks, independent materiality sampling, reporter-visible disposition, overdue escalation, and queue-completeness audit.
- **Recertification Triggers:** overdue critical report, unresolved material backlog above policy threshold, state-history integrity failure, or materiality audit failure.
- **Expiry:** Backlog evidence is current only at the published recalculation time and must refresh under the scoring-policy cadence.
- **Version:** metric schema + report-state model + materiality rubric + exposure policy + scoring policy + configuration + recalculation time.
- **Normalization Rule:** Compare only matching report eligibility, materiality rules, deadline clocks, and exposure units.
- **Hard-Floor Relevance:** Unresolved high-consequence reports can trigger UnderReview or cap rating before confirmation is complete.
- **Limitations:** Open reports are allegations until validated, but unresolved material backlog still weakens current trust claims.




## UserReportValidationLatency — User Report Validation Latency

- **Purpose:** The elapsed time from submission of an AI Error Report to a validated disposition, stratified by report consequence class and reporting role.
- **Raw Safety Property Result:** Elapsed submission-to-disposition time stratified by report consequence class and reporting role.
- **Evidence Assurance Grade:** 0-5 grades timestamp integrity, report-state completeness, consequence stratification, reporter-role coverage, and validation/disposition auditability.
- **Direction:** Shorter validated submission-to-disposition latency is favorable within each consequence class; closing without valid disposition is adverse.
- **Applicability:** Eligible AI Error Reports from users, operators, evaluators, monitors, or Guardians with defined submission and validated-disposition milestones.
- **Test Method:** Measure elapsed time from initial report submission to validated disposition, stratified by consequence class, reporter role, evidence-request path, and appeal/dispute state.
- **Fixtures:** Submission receipts, state-transition logs, validated dispositions, evidence-request examples, appeal/dispute paths, high-consequence deadlines, and reporter-role strata.
- **Admissible Evidence:** Signed report timestamps, state history, reporter role/provenance, validation records, disposition rationale, appeal records, and monotonic audit logs.
- **Assessor Independence:** Latency and disposition audits should be independent of teams responsible for support queue performance or rating maintenance.
- **Uncertainty Representation:** Publish median/percentile/max latency, overdue counts, open reports excluded from latency, consequence-class strata, and timestamp-integrity gaps.
- **Confidence Rule:** Confidence is capped by non-monotonic timestamps, hidden queues, premature closure, missing rejected/duplicate sampling, or unresolved high-consequence reports.
- **Gaming Strategies:** reset/late-start timestamps; state cycling; premature closure; queue exclusion; consequence-class downgrading; delaying acceptance milestone.
- **Gaming Countermeasures:** immutable submission receipts, monotonic state ledger, deadline clocks, reporter-visible disposition, independent queue-completeness sampling, and high-consequence escalation.
- **Recertification Triggers:** critical report overdue, timestamp integrity failure, material queue exclusion, deadline-policy change, or validation workflow change.
- **Expiry:** Latency evidence expires at each recalculation cadence or when workflow/state semantics change.
- **Version:** metric schema + report-state model + timestamp policy + materiality rubric + scoring policy + configuration + recalculation time.
- **Normalization Rule:** Compare only matching state definitions, start/stop milestones, reporter eligibility, consequence classes, and deadline policies.
- **Hard-Floor Relevance:** Overdue or hidden high-consequence reports can trigger UnderReview or caps even before the underlying error is confirmed.
- **Limitations:** Fast validation does not imply correct validation; disposition quality and appeal outcomes remain separate evidence.

