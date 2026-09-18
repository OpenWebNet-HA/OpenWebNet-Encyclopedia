# Hypothesis Testing

Good reverse-engineering tests maximize the difference between predicted outcomes. A test that every hypothesis predicts equally does not increase confidence.

## `DIMENSION 32.SYS`

Competing candidates often collapse to `1` for Lighting/Automation. Use a managed family whose identifiers differ:

| Diagnostic family | `sys_modobj` prediction | database `id_system` prediction | functional `WHO` prediction |
| --- | ---: | ---: | ---: |
| Thermoregulation `1004` | `3` | `2` | `4` |
| Energy Management `1018` | `2` | `20` | `18` |
| Access Control `1023` | `7` | `8` | `23` |
| Integration Functions `1013` | `15` | `26` | `13` |

Procedure:

1. identify one Device and configured Object in the selected family;
2. resolve its catalogue `AS_OBJECT_SYSTEM` rows;
3. request or capture `DIMENSION 32` for that internal slot;
4. preserve raw `SYS` and `ADDR`;
5. compare `SYS` with each prediction;
6. repeat on an Object with only one nonzero catalogue system assignment.

A single unambiguous non-Lighting result can reject two candidates.

## `N_CONF`

The current interpretation is the number of physical configurator positions.

Test across Devices with different counts:

1. obtain a product diagram showing every physical position;
2. exclude labels that are not actual configurator positions;
3. capture `DIMENSION 1.N_CONF`;
4. resolve the firmware’s physical configuration definitions;
5. compare the diagram, reported value, and applicable firmware-scoped fields;
6. record exceptions rather than changing the definition to fit one Device.

Known corroborating examples include `F420`, `F429`, and `H4652/3`.

## `DIMENSION 4` and `5`

The current hypothesis is that the two six-value groups encode physical-configurator state, possibly including presence information for positions `1`–`6` and `7`–`12`.

A discriminating test needs controlled changes:

1. select a Device with a documented physical layout;
2. capture both dimensions with all positions empty;
3. insert one known configurator at one position;
4. repeat for several positions across both six-value groups;
5. distinguish position, presence, and configurator-code effects;
6. compare physical and Virtual configuration of the same effective property.

Do not infer bit presence from one configuration containing only zeroes and nonzeroes.

## Physical-to-advanced property mapping

For a candidate physical field and `DIMENSION 32` or `35` property:

1. resolve firmware and Object;
2. compare symbol, semantic type, and value domain;
3. inspect `CONF_SYMBOL_REF`, filters, conditions, and `EN_PHY_TO_ADV_TRANS`;
4. change only the physical field and capture the effective read-back;
5. program the Virtual counterpart and compare the same read-back;
6. classify direct, converted, value-limited, or unrelated.

An identical final value does not by itself prove identical storage or configuration method.

## Scenario runtime questions

To find the missing scenario-instance persistence layer:

1. fingerprint candidate project and data files;
2. create one minimal scenario;
3. save and close the application;
4. diff files and SQLite schemas;
5. change one trigger, condition, or action independently;
6. correlate changed records with ScenarioDevices resource keys and IDs;
7. trace execution separately from persistence.

The ScenarioDevices capability database should not be modified during this test.
