# `WHAT` Reference

Published `WHO 24` `WHAT` forms are parameterized expressions rather than a flat scalar command table.

| `WHAT` form | Meaning | Parameter role |
| --- | --- | --- |
| `1#PROFILE_ID` | Profile frame | Selects the Lighting Management profile |
| `2#0` | Disable slave offset | Offset-enable state |
| `2#1` | Enable slave offset | Offset-enable state |

## Profile operations

In `1#PROFILE_ID`, the profile identifier is part of the `WHAT` field. It must remain attached to the operation when parsing, serializing, logging, or comparing frames. Treating `PROFILE_ID` as part of `WHERE` would change the grammar.

Profiles belong to Lighting Management rather than ordinary `WHO 1` Lighting scenes or levels. A profile identifier should therefore be represented as a `WHO 24` value even when applying the profile ultimately affects lighting output.

## Slave offset enable

`WHAT 2#0` and `2#1` control whether slave offset is disabled or enabled. The actual offset/GAP value is a separate property carried by `DIMENSION 12`. A complete configuration model must preserve both the Boolean enable state and the configured offset value.

## Namespace rule

These values are not aliases for `WHO 1` `WHAT` values. Their meaning follows the `WHO 24` management grammar and the structured sender/recipient address described in [`addressing.md`](addressing.md).