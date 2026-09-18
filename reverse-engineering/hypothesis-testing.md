# Hypothesis Testing

A useful reverse-engineering test makes competing explanations predict different observations. Repeating a familiar case in which every candidate gives the same value increases sample size but does not identify the correct model.

## Test design template

For every experiment, record:

| Element | Requirement |
| --- | --- |
| Claim | one relationship or semantic statement |
| Alternatives | at least one credible competing explanation |
| Predictions | expected result for each alternative |
| Controlled variables | Device, firmware, Module, configuration, connection, and request |
| Changed variable | exactly one input where possible |
| Observation | raw frames, database rows, UI state, and timing |
| Decision rule | result that favors, rejects, or narrows each candidate |
| Restoration | how the baseline is recovered after a state-changing test |
| Scope | products and revisions to which the result applies |

A test is inconclusive when the candidates predict the same result or an uncontrolled variable could explain the difference.

## `DIMENSION 32.SYS`

Common Lighting/Automation values collapse to `1`. Use a managed family whose identifiers diverge:

| Diagnostic family | `sys_modobj` prediction | catalogue `id_system` prediction | functional `WHO` prediction |
| --- | ---: | ---: | ---: |
| Thermoregulation `1004` | `3` | `2` | `4` |
| Energy Management `1018` | `2` | `20` | `18` |
| Access Control `1023` | `7` | `8` | `23` |
| Integration Functions `1013` | `15` | `26` | `13` |

Procedure:

1. identify one configured Device and Module in the selected family;
2. resolve its Object and all catalogue `AS_OBJECT_SYSTEM` rows;
3. prefer an Object with one nonzero system assignment;
4. send the interview request that produces `DIMENSION 32`;
5. preserve raw `SYS`, `ADDR`, Device, and internal slot;
6. compare the result with every prediction;
7. repeat with an Object assigned to several systems to test context selection.

A value equal to one candidate and different from the other two rejects the alternatives for that observation. Multiple-system Objects remain a separate cardinality question.

## Firmware-selection precedence

The catalogue contains concrete `V.R.b` rows, explicit `-1` components, multiple build rows, missing build rows, and `FW_default` metadata. Static data establishes these states but not loader precedence.

Select an item that exposes competing rows and record:

1. all `EN_FIRMWARE` candidates for the item;
2. all associated `EN_BUILDS` rows;
3. `FW_default`, status, localization level, slots, and capability differences;
4. the Device's reported firmware `V.R.b`;
5. the firmware/capability MyHOME Suite actually presents;
6. behavior when only the build differs;
7. behavior for a concrete build versus `V.R.-1`;
8. behavior when no build row exists.

Use read-only observation first. Do not replace catalogue rows to force a selection. A useful result must distinguish exact match, component wildcard, default fallback, localization choice, and absence of build metadata.

## Hardware and microcontroller versions

`DIMENSION 3` and `6` use `Version*Release*Build`, but the canonical databases contain no direct target fields.

To determine whether they classify product revisions:

1. collect several physical examples of the same SKU and firmware;
2. record manufacturing date/revision markings where available;
3. capture firmware, hardware, and microcontroller tuples;
4. compare Module layout and supported configuration;
5. repeat across a known hardware revision or replacement product;
6. observe whether MyHOME Suite changes the selected catalogue Device or capability.

A stable correlation with a printed revision is useful empirical metadata; it does not create a database relationship unless a source field is found.

## `N_CONF` catalogue-wide equivalence

The meaning of `N_CONF` is established as the number of physical configurator positions. The remaining hypothesis is that it always equals the count of applicable firmware-scoped physical configuration fields after excluding `AID`.

For each test Device:

1. obtain a product diagram showing all physical configurator positions;
2. capture `DIMENSION 1.N_CONF`;
3. resolve item and exact firmware;
4. identify firmware-scoped physical definitions, configuration modes, and conditions;
5. exclude `AID` only when it is the common identifier rather than a physical position;
6. compare diagram, frame, and applicable-field count;
7. record conditional or duplicated fields instead of counting blindly.

Prioritize Devices with counts other than six and firmware shared by several SKUs. Known corroborating examples include `F420`, `F429`, and `H4652/3`.

## `DIMENSION 4` and `5`

The working hypothesis is that the two groups of six values encode physical-configurator state, possibly mapping positions `1`–`6` and `7`–`12`.

Use a Device with documented positions and removable configurators:

1. record a complete baseline with all positions empty if the Device permits it;
2. capture both dimensions at least twice to establish stability;
3. insert one known configurator into position `1` and repeat;
4. move the same configurator to several positions, including one above `6` when available;
5. keep the position fixed and change only the configurator value;
6. compare physical and Virtual configuration producing the same effective property;
7. record whether unchanged positions remain constant.

This matrix distinguishes position, presence, raw configurator code, effective value, and configuration-mode effects. Zero/nonzero data from one configuration cannot establish a presence bitmap.

## Diagnostic outer `WHERE`

Repeated `WHO 1001` observations suggest that the outer diagnostic `WHERE` often follows the configured address of internal slot `1`. Test the boundary cases:

- slot `1` enabled and addressed;
- slot `1` disabled or unconfigured;
- slot `1` assigned a command-only Object;
- another slot carrying the main physical address;
- several Modules sharing an address;
- non-Lighting diagnostic families.

For each case, compare discovery address, interview selector, outer response `WHERE`, and every `DIMENSION 32` Module address. The goal is to recover a selection rule, not merely another matching example.

## Physical-to-advanced property mapping

For a candidate physical field and `DIMENSION 32` or `35` property:

1. resolve the exact firmware, internal slot, and Object;
2. compare `CONF_SYMBOL_REF`, semantic type, and value domain;
3. inspect filters, conditions, conversion rules, and `EN_PHY_TO_ADV_TRANS`;
4. change only the physical field and read back the effective configuration;
5. restore the baseline;
6. program the proposed Virtual counterpart and read back again;
7. classify the result as direct, converted, range-limited, condition-dependent, or unrelated.

An identical effective value does not prove identical storage or configuration method. A physical counterpart indicates capability, not which method is active.

## Address-rule selection

Choose a system with both family-unqualified and family-qualified `EN_ADDRESS_RULE` rows.

1. resolve the Object's `id_family` and catalogue systems;
2. record every candidate rule and its Virtual/advanced template;
3. vary only the Object family or mode where possible;
4. observe the address form MyHOME Suite accepts and emits;
5. trace whether `validity_rule`, level flags, or `offset_adv` are read;
6. test a rejected address that differs at only one rule boundary.

This can distinguish rule selection from rule rendering and application-side prevalidation from Device rejection.

## Scenario persistence and matching

To find the missing scenario-instance layer:

1. fingerprint candidate project and data files;
2. trace file opens before creating a scenario;
3. create one minimal trigger-action scenario;
4. save, close, and reopen the application;
5. diff files, SQLite schemas, and records;
6. change one trigger, condition, action, or ordering edge independently;
7. correlate changes with ScenarioDevices resource keys and matching IDs;
8. trace execution separately from persistence.

The ScenarioDevices capability databases should remain unchanged. A changed capability file would indicate synchronization or migration behavior and must be investigated separately.

## Stop conditions

Stop and classify the result as inconclusive when:

- the Device or firmware cannot be resolved uniquely enough for the claim;
- multiple settings changed;
- request/response direction is unknown;
- candidates predict the same outcome;
- the operation timed out without proof that the Device could respond;
- a state-changing test cannot be restored safely.

An inconclusive test should still record what was tried and how the next test can become discriminating.
