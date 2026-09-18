# Addressing

`WHO 18` encodes the Energy Management device family in `WHERE`. Address parsing must therefore preserve the complete syntactic form rather than treating `WHERE` as an untyped device number.

## Published `WHERE` forms

| `WHERE` | Device family | Index |
| --- | --- | --- |
| `1N` | Stop&Go | `N = 1–127` |
| `5N` | Energy Management central unit, pulse counter, power meter | `N = 1–255` |
| `7N#0` | Energy Management actuator | `N = 1–255` |

The published examples associate the `5N` family with devices including BTicino F520/F523/3522 and the `7N#0` family with Energy Management actuators including F522/F523.

## Family-specific operations

The address prefix is not merely routing metadata. It constrains the operation set:

- Stop&Go addresses use automatic-reset commands and `DIMENSION 250`–`263` status functions.
- `5N` measurement addresses expose power, accumulated energy and historical-series operations where supported by the target.
- `7N#0` actuator addresses expose actuator commands and `DIMENSION 71`–`73` state/information where supported.

A decoder should therefore resolve the `WHERE` family before interpreting the complete operation.

## Actuator suffix

The actuator form includes the literal `#0` suffix: `7N#0`. The suffix is part of the published address grammar and must not be discarded by integer conversion or generic normalization.

## Discovery

The published `WHO 18` functional specification defines direct device addressing but does not define a general broadcast inventory request equivalent to the Lighting general-status query. Device discovery should not be invented from the existence of the `N` ranges.

The published ranges describe valid address spaces, not proof that every index is populated. Software that needs to probe functional Energy Management addresses must distinguish “address can exist” from “device is present.”

See [`WHAT` Reference](what.md) for command applicability and [`DIMENSION` Reference](dimensions.md) for family-specific data operations.