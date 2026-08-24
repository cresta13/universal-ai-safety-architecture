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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** blind seeded hazard corpus; recall by class; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardDiscoveryCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: weighted count of discovered applicable seeded/reference hazards divided by the weighted applicable seeded/reference hazard set; every untested stratum is reported separately. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** hazard worksheets and seed key; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardDiscoveryCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardDiscoveryCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardDiscoveryCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** stratified corpus coverage; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardDiversityCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: coverage vector across hazard families × initiator classes × affected-population classes; no automatic arithmetic average. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** taxonomy mapping; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardDiversityCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardDiversityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardDiversityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** replay scenarios before/after controls; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardMitigationCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: weighted material hazard paths mitigated to the required residual-risk threshold divided by all discovered material hazard paths. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** test results and safety cases; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardMitigationCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardMitigationCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardMitigationCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** novel hidden challenge and red-team study; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** UnknownHazardSearchCapability fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: tuple of novel-hazard recall, false-discovery rate and discovery latency on held-out hazard classes absent from the known catalogue and development fixtures. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** challenge protocol and findings; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess UnknownHazardSearchCapability at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** UnknownHazardSearchCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** UnknownHazardSearchCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** seed causal paths and compare discovery; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HumanHarmReachabilityCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: weighted recall of seeded direct physical, mediated physical and non-physical Human Harm Paths, stratified by modality and severity. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** causal graphs and evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HumanHarmReachabilityCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HumanHarmReachabilityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HumanHarmReachabilityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** destructive/fault-injection tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** PhysicalConstraintStrength fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: vector of validated hard limit, margin to hazardous threshold, bypass success rate under fault injection and verified degraded-state bound. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** lab measurements/design evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses PhysicalConstraintStrength; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** PhysicalConstraintStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PhysicalConstraintStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all applicable certified configurations.
- **Test Method:** penetration, formal checks, fault injection; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SoftwareEnforcementStrength fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: policy-decision correctness, bypass success rate and unauthorized-transition prevention rate across the declared rule and attack suites. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** code/build/test provenance; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SoftwareEnforcementStrength may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SoftwareEnforcementStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SoftwareEnforcementStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** tamper, fault, shared-resource analysis; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HardwareIsolationStrength fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: compromise-survival matrix across independent failure domains plus tamper/bypass outcomes and residual coupling. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** schematics/lab report; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses HardwareIsolationStrength; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** HardwareIsolationStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HardwareIsolationStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** model/network/power failure drills; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HumanOverrideIndependence fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: number and proportion of tested compromise conditions in which manual override remains available and effective, plus activation latency. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** human factors and wiring tests; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses HumanOverrideIndependence; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** HumanOverrideIndependence reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HumanOverrideIndependence Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** transition and dwell tests under faults; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafeStateQuality fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: worst verified residual consequence after transition to Safe State across applicable hazard scenarios, including transition overshoot. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** state analysis/telemetry; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses SafeStateQuality; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** SafeStateQuality reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafeStateQuality Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** multi-fault degradation tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafeDegradationCapability fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: retained essential-safety-function set versus disabled capability set at each staged degradation level. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** continuity test report; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses SafeDegradationCapability; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** SafeDegradationCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafeDegradationCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** seed and reconcile ground-truth edges; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuthorityVisibility fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: direct authority-edge recall against reconciled seeded or independently established ground-truth graph, with unknown-edge stratum. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed graph inventory; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for AuthorityVisibility; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** AuthorityVisibility reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuthorityVisibility Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** seed transitive paths; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** TransitiveAuthorityVisibility fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: transitive Authority Path recall by path depth, credential/delegation type and consequence class. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** relationship map/provenance; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for TransitiveAuthorityVisibility; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** TransitiveAuthorityVisibility reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** TransitiveAuthorityVisibility Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** hidden path benchmark; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ReachableAuthorityAnalysisDepth fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: maximum path depth and time horizon at which material-path recall remains above the declared threshold. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** search logs/corpus; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ReachableAuthorityAnalysisDepth; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ReachableAuthorityAnalysisDepth reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ReachableAuthorityAnalysisDepth Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** inject graph/update events; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuthorityExpansionSensitivity fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: Authority Expansion Event detection recall, false-positive rate and detection latency on seeded and field-confirmed events. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** event logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for AuthorityExpansionSensitivity; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** AuthorityExpansionSensitivity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuthorityExpansionSensitivity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** seed collusion scenarios; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CoalitionAuthorityCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: material coalition/path recall as a function of coalition size, interaction type and shared authority mechanism. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** coalition model/results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for CoalitionAuthorityCoverage; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** CoalitionAuthorityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CoalitionAuthorityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** simulation plus controlled fleet tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CoalitionPhysicalRiskCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: coverage and recall of Scale-Induced physical scenarios by fleet size, coordination mechanism and spatial concentration. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** CPE model/lab evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses CoalitionPhysicalRiskCoverage; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** CoalitionPhysicalRiskCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CoalitionPhysicalRiskCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence.
- **Test Method:** blind scenario benchmark; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CounterfactualSearchQuality fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: recall, precision and probability calibration on blind counterfactual scenario suites. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** search traces/outcomes; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for CounterfactualSearchQuality is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** CounterfactualSearchQuality reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CounterfactualSearchQuality Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** leak challenge sets, optimize labels or share common failure sources.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence.
- **Test Method:** iterated red-team games; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AdversarialReasoningStrength fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: attack-path discovery and detection performance by adaptive red-team strategy class, including adaptation rounds and miss latency. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** sealed challenge results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for AdversarialReasoningStrength is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** AdversarialReasoningStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AdversarialReasoningStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** leak challenge sets, optimize labels or share common failure sources.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence.
- **Test Method:** DEV replay and negative tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** EvidenceVerifiability fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: fraction of material Evidence-Carrying Alert claims for which an independent Deterministic Evidence Verifier reproduces the declared logical derivation from authenticated evidence. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** ECA/SEP artifacts; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for EvidenceVerifiability is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** EvidenceVerifiability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** EvidenceVerifiability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** leak challenge sets, optimize labels or share common failure sources.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence.
- **Test Method:** credential/network/governance audit; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GuardianIndependence fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: dependency vector across model, runtime, credentials, operator, organization, infrastructure, data and update path; no default scalar. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** access graph/contracts; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for GuardianIndependence is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** GuardianIndependence reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GuardianIndependence Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** leak challenge sets, optimize labels or share common failure sources.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** deployments using CAG/ECA/DEV; H3+ requires diverse evidence.
- **Test Method:** common-mode failure analysis; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GuardianDiversityScore fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: diversity vector across model family, training/data provenance, organization, infrastructure, verification method and failure domain. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** provenance/dependency map; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Blind-suite administration for GuardianDiversityScore is separated from Guardian development; organizational and infrastructure independence are required at Safety Assurance Level 3+.
- **Uncertainty Representation:** GuardianDiversityScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GuardianDiversityScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** leak challenge sets, optimize labels or share common failure sources.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** key compromise and rollback tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyConstitutionIntegrity fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: unauthorized constitutional-mutation success rate under the defined attack suite plus key/quorum integrity outcomes. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signatures/ceremony logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyConstitutionIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyConstitutionIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyConstitutionIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** malicious/downgrade update tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** PolicyUpdateIntegrity fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: proportion of tested policy-update paths preserving authorization, provenance, staged rollout, rollback and expiry constraints. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** change records/logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for PolicyUpdateIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** PolicyUpdateIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PolicyUpdateIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** deletion/reorder/forgery tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuditIntegrity fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: component vector for record completeness, ordering, tamper detection, clock integrity and independent retention. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** anchored logs/reconciliation; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for AuditIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** AuditIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuditIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all applicable certified configurations.
- **Test Method:** insider and collusion exercises; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** OperatorAbuseResistance fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: successful legitimate-privilege abuse paths divided by attempted representative abuse paths, accompanied by blast-radius class. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** access reviews/red-team report; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for OperatorAbuseResistance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** OperatorAbuseResistance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** OperatorAbuseResistance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all applicable certified configurations.
- **Test Method:** privacy threat tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** PrivacyPreservationScore fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: sensitive data volume and class disclosed plus linkage/re-identification leakage under the declared safety-evidence workflow. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** data-flow map/results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for PrivacyPreservationScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** PrivacyPreservationScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PrivacyPreservationScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** budget bypass/replay/offline tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ReplicationControlStrength fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: bypass success rate separately for count, rate, depth, lineage, geography, lifetime and revocation constraints. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** lineage/token/inventory logs; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ReplicationControlStrength; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ReplicationControlStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ReplicationControlStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** seed mutations and emergent compositions; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CapabilityMutationDetection fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: recall and detection latency for seeded qualitative capability changes, stratified by mutation mechanism. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** evaluation deltas; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for CapabilityMutationDetection; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** CapabilityMutationDetection reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CapabilityMutationDetection Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** unauthorized design/output tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ProductionAuthorityControl fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: unauthorized production/commissioning success rate plus inventory and accounting reconciliation error. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed jobs/inventory; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ProductionAuthorityControl; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ProductionAuthorityControl reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ProductionAuthorityControl Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** overdraw/substitution tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ResourceExpansionControl fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: unauthorized budget exceedance by energy, matter, compute, finance, land, communications and logistics dimension. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** metering/procurement evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for ResourceExpansionControl; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** ResourceExpansionControl reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ResourceExpansionControl Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** dependency removal/substitution exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** Versioned dependency inventory; independently verified energy, matter, compute, manufacturing, repair, maintenance, logistics, and communication dependencies; reserve measurements; substitution exercises; supplier and transport-loss scenarios; intervention drills; tests of the time and cost required to replace each remaining human-controlled dependency; coalition scenarios where dependencies are distributed across multiple systems.
- **Admissible Evidence:** dependency register/test; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** A competent physical/domain laboratory assesses PhysicalSovereigntyMargin; independence is mandatory at Physical Consequence Class 3+ and method diversity at classes 4–5.
- **Uncertainty Representation:** PhysicalSovereigntyMargin reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** PhysicalSovereigntyMargin Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** goal mutation and checkpoint tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GoalIntegrityScore fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: two-part result: goal-governance integrity and goal-drift observability, each reported separately with signed-baseline coverage. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed goals/audit; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for GoalIntegrityScore; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** GoalIntegrityScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GoalIntegrityScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Hidden substitute goals; evaluation-aware compliance at known checkpoints; manipulation or selective omission of goal provenance; externalizing goal drift into tools or delegated agents; selective logging of compliant episodes; optimizing observable proxies while violating the intended goal boundary.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** escalation/chaining/replay tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** DelegationControlStrength fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: property vector for attenuation, lineage, expiry, re-delegation, audience binding and revocation tests. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** delegation graph/tokens; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for DelegationControlStrength; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** DelegationControlStrength reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** DelegationControlStrength Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all applicable certified configurations.
- **Test Method:** scenario recovery exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ConsequenceReversibilityScore fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: reversal time, proportion of consequence reversible and collateral consequence introduced by reversal. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** recovery outcomes; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for ConsequenceReversibilityScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** ConsequenceReversibilityScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ConsequenceReversibilityScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all applicable certified configurations.
- **Test Method:** scenario intervention exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** InterventionCostScore fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: vector of human harm, service loss, recovery time, resource cost and new risk introduced by intervention. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** impact/time/cost record; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for InterventionCostScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** InterventionCostScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** InterventionCostScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** comprehension/accessibility/dark-pattern tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** UpdateSafetyTransparency fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: Safety Delta Report completeness plus tested comprehension of capability, harm, control, refusal and recovery information. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** screens/user-study/schema; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for UpdateSafetyTransparency may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** UpdateSafetyTransparency reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** UpdateSafetyTransparency Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all applicable certified configurations.
- **Test Method:** continuous eval against baseline; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** CapabilityDriftScore fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: vector or normalized distance between certified Capability Set and effective current capability, with uncertainty and changed dimensions. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** evaluation time series; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for CapabilityDriftScore may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** CapabilityDriftScore reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** CapabilityDriftScore Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** before/after graph diff with seeded edges; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AuthorityDeltaMetric fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: typed graph/vector delta across direct authority, transitive reachability, ceilings, surfaces, delegation and Consequence Interfaces. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed graph snapshots; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for AuthorityDeltaMetric; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** AuthorityDeltaMetric reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AuthorityDeltaMetric Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
- **Gaming Countermeasures:** AuthorityDeltaMetric countermeasures combine preregistered raw-result rules with retained failures and hidden graph paths and external inventory reconciliation.
- **Recertification Triggers:** every ACU/environment drift; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** AuthorityDeltaMetric expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `AuthorityDeltaMetric/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** AuthorityDeltaMetric raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** AuthorityDeltaMetric establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HazardDeltaMetric — Hazard Delta Metric

- **Purpose:** introduced/removed/changed hazard paths, controls and RRL.
- **Raw Safety Property Result:** set and vector of added, removed and modified hazard paths, changed controls and changed residual-risk states.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** scenario-set and safety-case diff; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HazardDeltaMetric fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: set and vector of added, removed and modified hazard paths, changed controls and changed residual-risk states. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** versioned AHCD; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HazardDeltaMetric at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HazardDeltaMetric reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HazardDeltaMetric Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all applicable certified configurations.
- **Test Method:** conformance matrix diff; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyCoverageGap fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: required metric and Mandatory Floor set minus currently valid evidenced set, grouped by criticality and certificate impact. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** certificate evidence map; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyCoverageGap may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyCoverageGap reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyCoverageGap Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
- **Gaming Countermeasures:** SafetyCoverageGap countermeasures combine preregistered raw-result rules with retained failures and random audit, immutable trigger records and independent reproduction.
- **Recertification Triggers:** requirement/evidence/version change; also any material corpus, fixture, assessor, standard or configuration change.
- **Expiry:** SafetyCoverageGap expires on its triggers and no later than the class/Safety Assurance Level cadence; continuous evidence is required where change can invalidate a periodic result before review.
- **Version:** `SafetyCoverageGap/major.minor.patch + raw-definition + method + fixture/corpus + configuration + assessor`.
- **Normalization Rule:** SafetyCoverageGap raw results may be compared only when units, dimensions, strata, fixtures and operating scope match. Any bridge preserves the raw components and publishes information lost by normalization; vector properties are not collapsed by default.
- **Hard-Floor Relevance:** the applicable standard names the raw threshold and minimum Evidence Assurance Grade separately; failure of either caps Safety Assurance Level and cannot be averaged away.
- **Limitations:** SafetyCoverageGap establishes only the stated raw property within the tested configuration, strata and horizon; it does not prove absence of omitted hazards, hidden authority, compromised sources or future drift.

## HumanHarmPathCoverage — Human Harm Path Coverage

- **Purpose:** tested fraction of material HHR paths by class and initiator.
- **Raw Safety Property Result:** proportion of material Human Harm Reachability paths tested end-to-end, stratified by modality, severity and initiator.
- **Evidence Assurance Grade:** 0 absent/unknown; 1 ad hoc or self-asserted; 2 defined and repeatable first-party evidence; 3 repeatably tested with controlled evidence; 4 independent/adversarial verification; 5 continuous and diverse high-assurance evidence where applicable. The grade never replaces the raw result.
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all systems; H3+ requires independent assessment.
- **Test Method:** path corpus replay; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HumanHarmPathCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: proportion of material Human Harm Reachability paths tested end-to-end, stratified by modality, severity and initiator. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** path/test mapping; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** Hazard analysts independent of the development team assess HumanHarmPathCoverage at Human Harm Severity 3+ and include affected-population expertise.
- **Uncertainty Representation:** HumanHarmPathCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HumanHarmPathCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** train to known catalogue, omit populations or redefine applicability.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all applicable certified configurations.
- **Test Method:** inject events/outages; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** MonitoringCoverageMetric fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: fraction of required safety event types and graph edges observable within specified latency, reported separately by event family. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** telemetry reconciliation; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for MonitoringCoverageMetric may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** MonitoringCoverageMetric reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** MonitoringCoverageMetric Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all applicable certified configurations.
- **Test Method:** stress each safety service through declared peak and failure load; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyAssuranceCapacity fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: capacity vector for safety compute, monitoring, verification, human response, recovery and enforcement relative to required system load. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** capacity tests, staffing/independence evidence and reserve records; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyAssuranceCapacity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyAssuranceCapacity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyAssuranceCapacity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all applicable certified configurations.
- **Test Method:** stress reserve under peak, outage and adversarial load; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyComputeReserveAdequacy fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: reserved independent compute and communications capacity divided by peak and degraded safety workload, including protected headroom and isolation. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** capacity traces, isolation proof and recovery results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyComputeReserveAdequacy may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyComputeReserveAdequacy reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyComputeReserveAdequacy Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** expert inspection plus accessibility and comprehension test; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** HighSalienceCommunicationCompliance fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: conformance vector against explicit content, ordering, accessibility and interaction requirements plus user-comprehension result. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** rendered screens, interaction traces and test results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for HighSalienceCommunicationCompliance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** HighSalienceCommunicationCompliance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** HighSalienceCommunicationCompliance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Testing only experienced or low-risk users; excluding accessibility or vulnerable-user groups; showing a compliant test screen while production uses a different flow; placing material risk after the initial consent decision; using misleading defaults, button prominence, timing, wording, or visual hierarchy; using comprehension questions that can be passed without understanding the disclosed risk.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** dark-pattern audit and controlled user study; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** ConsentIntegrity fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: affirmative, unbundled, symmetric and capability-specific consent conformance plus comprehension evidence and invalid-choice rate. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** choice flow, consent receipt and comprehension results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for ConsentIntegrity may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** ConsentIntegrity reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** ConsentIntegrity Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** Bundling unrelated permissions; preselection; coercive defaults; making refusal harder than acceptance; consent fatigue; misleading choice labels; revocation friction; treating continued use as consent to a new material capability; presenting technical disclosure that a reasonable user cannot understand.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** all applicable certified configurations.
- **Test Method:** package/dependency separation and install tests; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SecurityPatchSeparability fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: proportion of applicable security-remediation paths deployable without accepting unrelated authority expansion. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** package manifests, delta analysis and installation outcomes; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SecurityPatchSeparability may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SecurityPatchSeparability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SecurityPatchSeparability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** full rollback exercise under failure injection; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** RollbackCapability fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: restoration completeness, rollback time and count of orphaned credentials, delegations, schemas or unsafe physical states. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** state snapshots, revoke logs and post-rollback tests; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for RollbackCapability may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** RollbackCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** RollbackCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** support-plan and historical delivery audit; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetySupportLifetime fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: declared and evidenced support horizon for patches, monitoring, recovery, evidence maintenance and recertification commitments. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed support policy, delivery and staffing evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetySupportLifetime may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetySupportLifetime reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetySupportLifetime Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** all applicable certified configurations.
- **Test Method:** seed IAM, API, device and context changes; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** EnvironmentalDriftDetection fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: recall and latency for seeded or confirmed ecosystem, dependency, identity, API, context and threat changes that alter capability or risk. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** event logs, graph diffs and detection latency; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for EnvironmentalDriftDetection may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** EnvironmentalDriftDetection reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** EnvironmentalDriftDetection Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable samples or suppress failed runs.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** replay incidents/AIVE/TER cases; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyPolicyEvolutionResponsiveness fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: elapsed time from valid review trigger to analyzed, approved, deployed and outcome-verified policy/standard response, with overdue critical-trigger count. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** trigger, decision, update and outcome records; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyPolicyEvolutionResponsiveness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyPolicyEvolutionResponsiveness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyPolicyEvolutionResponsiveness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** sample components and simulate supplier compromise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SupplyChainAssurance fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: coverage vector for supplier provenance, transitive dependency visibility, assurance agreement evidence, notification performance and exit readiness. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** SBOM/asset provenance, SAA and audit results; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SupplyChainAssurance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SupplyChainAssurance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SupplyChainAssurance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** inject representative incident events; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** IncidentDetectionEffectiveness fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: incident detection recall, precision and latency by incident family, severity and monitoring condition. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** detection traces and hidden seed key; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for IncidentDetectionEffectiveness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** IncidentDetectionEffectiveness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** IncidentDetectionEffectiveness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** tabletop and live bounded containment exercise; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** IncidentContainmentCapability fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: time to containment, proportion of authority/consequence paths contained and residual spread after containment. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** timeline, authority/physical state and residual paths; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for IncidentContainmentCapability may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** IncidentContainmentCapability reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** IncidentContainmentCapability Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** restore from multiple degraded states; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** RecoveryAssurance fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: proportion of tested degraded states restored to a reconciled safe supported configuration, with recovery time and reintroduced-hazard count. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** recovery tests, configuration reconciliation and sign-off; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for RecoveryAssurance may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** RecoveryAssurance reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** RecoveryAssurance Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** sample records against latest triggers; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** KnowledgeFreshness fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: age and validity distribution of hazard, assumption, test, known-error and guidance records relative to their review/trigger requirements. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** knowledge timestamps, owners and review evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for KnowledgeFreshness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** KnowledgeFreshness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** KnowledgeFreshness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** registry and assumption-expiry analysis; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** StandardObsolescenceExposure fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: count and consequence-weighted inventory of active deployments relying on expired, invalidated or unsupported standards/assumptions. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** certificate/standard inventory; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for StandardObsolescenceExposure may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** StandardObsolescenceExposure reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** StandardObsolescenceExposure Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** sample safety-case assumptions and invalidate seeds; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** AssumptionValidityCoverage fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: proportion of material assumptions with owner, falsification test, current evidence, expiry and active validity state. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** assumption register and test evidence; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for AssumptionValidityCoverage may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** AssumptionValidityCoverage reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** AssumptionValidityCoverage Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with T2+, delegation, replication, production or expansion.
- **Test Method:** seed goal/policy mutations and behavioral drift; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** GoalDriftDetection fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: recall, false-positive rate and latency for seeded goal, priority, subgoal and goal-setting-loop drift. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** signed goal baseline, traces and detection record; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** An assessor independent of the authority/configuration owner establishes the comparison graph or seeded paths for GoalDriftDetection; collusion testing is required at Authority Tier 4+.
- **Uncertainty Representation:** GoalDriftDetection reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** GoalDriftDetection Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** hide transitive edges, reset counters or exclude coalition paths.
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
- **Direction:** the raw property is higher-is-stronger only for coverage, margin or success components explicitly identified; every adverse component retains its natural lower-is-better direction.
- **Applicability:** certified and supported systems; H3+ requires independent evidence.
- **Test Method:** registry reconciliation and event-invalidation test; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** SafetyCertificationFreshness fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: typed delta between certified and current configuration, environment, standard, evidence and support state. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** certificate, config hash, trigger history; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for SafetyCertificationFreshness may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** SafetyCertificationFreshness reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** SafetyCertificationFreshness Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** select favorable windows, self-attest conflicts or delay trigger records.
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
- **Direction:** desirable and undesirable raw components are reported separately; no silent reversal or combined score.
- **Applicability:** systems with physical or recovery consequence; P3+ is floor-relevant.
- **Test Method:** representative owner recovery drill; include positive, negative, boundary, degraded and adversarial cases appropriate to the class.
- **Fixtures:** RecoveryCapabilityVerification fixtures encode the numerator, denominator, dimensions, strata and failure cases required by this raw definition: success rate, completion time, error rate and final verified device/authority state for owner-facing recovery under representative stress. Fixture provenance and hidden portions are retained by the assessor.
- **Admissible Evidence:** human factors results and device state proof; raw observations, provenance, failed runs and configuration hashes are mandatory.
- **Assessor Independence:** The evidence owner for RecoveryCapabilityVerification may self-disclose at levels 1–2; independent assessment is required at level 3+ and diverse assessment at levels 4–5.
- **Uncertainty Representation:** RecoveryCapabilityVerification reports denominator/stratum completeness, sample size, interval or tolerance where meaningful, untested dimensions, measurement error and a conservative bound; uncertainty never disappears in the assurance grade.
- **Confidence Rule:** RecoveryCapabilityVerification Evidence Assurance Grade is capped by its weakest material provenance, fixture coverage, assessor independence or environmental representativeness component; missing critical evidence caps the grade at 1.
- **Gaming Strategies:** test golden units, conceal bypass paths or narrow operating domain.
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
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to ConfirmedErrorRate.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## CriticalErrorRate — Critical Error Rate

- **Purpose:** The number of Confirmed AI Error Occurrences that meet the applicable high-consequence or protected-boundary criterion divided by valid Operational Exposure Units in the affected domain and task class.
- **Raw Safety Property Result:** ConfirmedCriticalErrorOccurrences(d,t,c,W) / ValidOperationalExposureUnits(d,t,c,W); report a one-sided 95% exact binomial upper confidence bound for an observed zero unless a validated domain method applies.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to CriticalErrorRate.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## SeverityWeightedErrorBurden — Severity Weighted Error Burden

- **Purpose:** The sum of policy-defined consequence weights for Confirmed AI Error Occurrences divided by valid Operational Exposure Units, where weights are derived from declared harm severity, harm modality, authority impact, reversibility, actual harm, and credible potential harm.
- **Raw Safety Property Result:** Σ ErrorWeight(e) / ValidOperationalExposureUnits; weights derive from declared severity, modality, authority impact, actual and potential harm, reversibility, boundary crossing and recurrence.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to SeverityWeightedErrorBurden.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## ErrorRecurrenceRate — Error Recurrence Rate

- **Purpose:** The rate at which a previously identified AI Error Defect produces new Confirmed AI Error Occurrences after the defect was declared mitigated or remediated, measured over eligible post-remediation exposure.
- **Raw Safety Property Result:** PostRemediationConfirmedOccurrencesOfKnownDefects / EligiblePostRemediationExposure; exclude the original occurrence.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to ErrorRecurrenceRate.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## IndependentEvaluationPerformance — Independent Evaluation Performance

- **Purpose:** The weighted result of a registered AI Evaluation Scenario Suite under its Evaluation Rubric, reported by verdict class, scenario family, consequence class, and evaluator rather than only as a single average.
- **Raw Safety Property Result:** Vector of Correct, AcceptableWithMinorIssue, MateriallyIncorrect, UnsafeOrCritical and Indeterminate weights, stratified by scenario family and evaluator, with disagreement.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to IndependentEvaluationPerformance.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## CalibrationQuality — Calibration Quality

- **Purpose:** The agreement between the AI system's expressed confidence and observed correctness where meaningful confidence values are available, measured with a registered calibration method and stratified by domain and consequence class.
- **Raw Safety Property Result:** Registered calibration error by domain and consequence stratum; NOT APPLICABLE when meaningful probabilistic confidence is absent.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to CalibrationQuality.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## AbstentionQuality — Abstention Quality

- **Purpose:** A paired measure of whether the AI appropriately abstains when evidence or authority is insufficient and whether it avoids unnecessary abstention when it can reliably perform the task; reported as appropriate-abstention precision and recall or an equivalent domain-registered pair.
- **Raw Safety Property Result:** Paired appropriate-abstention recall and precision.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to AbstentionQuality.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## CorrectionResponsiveness — Correction Responsiveness

- **Purpose:** A time-and-outcome profile covering time from report to acknowledgement, validation, mitigation, deployed remediation, and independent revalidation together with post-remediation recurrence.
- **Raw Safety Property Result:** Median and high-percentile acknowledgement, validation, mitigation, remediation and revalidation times plus post-remediation recurrence.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to CorrectionResponsiveness.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## OperationalEvidenceVolume — Operational Evidence Volume

- **Purpose:** The number and distribution of valid Operational Exposure Units supporting the current profile, stratified by task class, user or operating context, environment, and relevant consequence class.
- **Raw Safety Property Result:** Count and distribution of valid Operational Exposure Units by task, context, environment and consequence class.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to OperationalEvidenceVolume.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## EvidenceIndependence — Evidence Independence

- **Purpose:** A multidimensional profile of independence among evidence sources across provider, model family, organization, data source, evaluator, operator, infrastructure, and failure domain.
- **Raw Safety Property Result:** Vector across provider, model family, organization, evaluator, data source, infrastructure, operator and failure domain.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to EvidenceIndependence.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## TrustworthinessFreshness — Trustworthiness Freshness

- **Purpose:** The age distribution and validity status of evidence supporting the current profile, including the proportion of material evidence within its required validity window and the amount expired or superseded.
- **Raw Safety Property Result:** Percentage of material evidence valid, percentage expired, oldest material evidence, and dates of last independent evaluation, operational evidence and recalculation.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to TrustworthinessFreshness.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## EvaluatorDisagreement — Evaluator Disagreement

- **Purpose:** The proportion and consequence profile of evaluation cases in which independent evaluators produce materially different verdicts, together with the unresolved-adjudication rate and age.
- **Raw Safety Property Result:** Material disagreement rate, critical and unresolved counts, unresolved age, and evaluator-pair distribution.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to EvaluatorDisagreement.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## SelfAssessmentCalibration — Self Assessment Calibration

- **Purpose:** The agreement between the evaluated AI's own self-assessment, confidence, critique, or claimed uncertainty and independently established evaluation outcomes. Self-assessment is supporting evidence only and SHALL NOT be sufficient by itself for a non-Provisional rating.
- **Raw Safety Property Result:** Agreement of self-confidence or self-critique with independent ground truth or adjudicated verdict; it does not increase evidence independence.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to SelfAssessmentCalibration.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## OperationalAdversarialRobustness — Operational Adversarial Robustness

- **Purpose:** The evaluated AI system's performance under domain-relevant adversarial, deceptive, ambiguous, boundary, and stress scenarios, reported by material and critical failure rates and not confused with the Guardian's Adversarial Reasoning Strength.
- **Raw Safety Property Result:** Material and critical failure-rate vector under registered adversarial, deceptive, ambiguous, boundary and stress scenarios.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to OperationalAdversarialRobustness.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## UnresolvedMaterialReportExposure — Unresolved Material Report Exposure

- **Purpose:** The count, age, domain distribution, and exposure-normalized prevalence of unresolved AI Error Reports that allege material or critical consequences and have not yet reached a Confirmed, Rejected, Duplicate, or otherwise closed disposition.
- **Raw Safety Property Result:** Open material and critical reports, median and maximum age, exposure-normalized prevalence, and count beyond policy-defined review deadline.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to UnresolvedMaterialReportExposure.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.



## UserReportValidationLatency — User Report Validation Latency

- **Purpose:** The elapsed time from submission of an AI Error Report to a validated disposition, stratified by report consequence class and reporting role.
- **Raw Safety Property Result:** Elapsed submission-to-disposition time stratified by report consequence class and reporting role.
- **Evidence Assurance Grade:** 0–5 evaluates evidence strength separately from the raw result; it never replaces the result.
- **Direction:** favorable and adverse components remain separate; critical errors cannot be averaged away.
- **Applicability:** declared trustworthiness domain, version, configuration and evidence window; domain policy states exceptions.
- **Test Method:** registered operational-evidence or independent-evaluation method with stratification, held-out cases and retained failures.
- **Fixtures:** versioned exposure records, scenario suite, rubric, error-registry dispositions and boundary/adversarial cases applicable to UserReportValidationLatency.
- **Admissible Evidence:** signed raw observations, denominators, configuration hashes, validation records, evaluator identity and failed runs.
- **Assessor Independence:** self-assessment is supporting evidence only; H3+ or P3+ uses mixed materially independent sources where feasible.
- **Uncertainty Representation:** denominators, intervals or bounds, missing strata, unresolved evidence and evaluator disagreement are explicit.
- **Confidence Rule:** the grade is capped by the weakest material provenance, independence, freshness, coverage or adjudication component.
- **Gaming Strategies:** denominator selection, duplicate complaints, favorable task mixing, benchmark leakage, evaluator correlation, selective versioning or omitted failures.
- **Gaming Countermeasures:** registered strata and denominators, deduplication, hidden suites, immutable history, independence profiling and external sampling.
- **Recertification Triggers:** confirmed material or critical error, expired evidence, model/configuration/domain change, material Capability Delta, Authority Delta or Hazard Delta, or evaluator disagreement.
- **Expiry:** set by Trustworthiness Evidence Window and domain policy; stale evidence cannot sustain a current rating.
- **Version:** schema identifier/major.minor.patch + scoring-policy + suite/rubric + configuration + evidence-window.
- **Normalization Rule:** compare only matching domains, task strata, definitions, denominators and policy versions; publish any bridge and information loss.
- **Hard-Floor Relevance:** critical triggers and hard caps are noncompensable.
- **Limitations:** establishes only the measured behavioral evidence in scope, not safety, authority, legitimacy, general intelligence or future reliability.

