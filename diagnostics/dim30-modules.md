# `DIMENSION 30`: Modules and Objects

`DIMENSION 30` reports the configured Object or unconfigured Virgin Object associated with a firmware-exposed Module, together with its configured state.

## Frame

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `SLOT` | `1..255` | numeric `slot` |
| `KEYO` | `1..65535` | Object or Virgin Object number, selected by `STATE` |
| `STATE` | `0..1` | unconfigured/configured state |

Use **Module** for the logical container and **`slot`** for `SLOT`. `OPEN.db` uses the legacy label “ko slot”; this documentation retains that wording only when quoting or naming source fields.

## Catalogue interpretation

| Diagnostic field | Catalogue concept | Status |
| --- | --- | --- |
| `SLOT` | `EN_SLOTS.first_slot` placement | structurally corroborated |
| `KEYO`, when `STATE = 1` | `EN_KEY_OBJECT.key_object` | structurally and behaviorally corroborated |
| `KEYO`, when `STATE = 0` | `EN_VIRGIN_OBJECT.virgin_key_object` | structurally and behaviorally corroborated |
| `STATE` | installed runtime state | direct database label; no single catalogue column equivalent |

`KEYO` selects one of two external number spaces according to `STATE`. It is not the internal catalogue key `EN_KEY_OBJECT.id_key_object` or `EN_VIRGIN_OBJECT.id_virgin_key_object`, even where a particular database revision happens to assign equal numeric values.

Likewise, `SLOT` is not `EN_SLOTS.id_slot`. Diagnostic `SLOT` is a Device-local position correlated with catalogue placement such as `EN_SLOTS.first_slot`; `id_slot` identifies a database association row.

## Building the Module list

1. Group records by Physical Device interview.
2. Use `SLOT` as the Device-local `slot` key.
3. When `STATE = 1`, resolve `KEYO` against `EN_KEY_OBJECT.key_object`.
4. When `STATE = 0`, resolve `KEYO` against `EN_VIRGIN_OBJECT.virgin_key_object`.
5. Use the resolved Virgin Object and its catalogue associations to derive the unconfigured Module's functional role and permitted Object set.
6. Retain `STATE` alongside the resolved record so an Object and Virgin Object are never conflated.
7. Attach `DIMENSION 32` address data using the same `slot`.
8. Attach `DIMENSION 35` configuration values only when both Device and `slot` match.

Do not renumber `slot` positions to match a UI’s visible Module numbering. MyHOME_Suite can hide or relabel slots, and observed scenario Devices show UI numbering that differs from the numeric diagnostic position.

## Configured and unconfigured Modules

`STATE 1` indicates configured and `STATE 0` indicates unconfigured according to `OPEN.db`. The meaning of `KEYO` changes with that state:

| `STATE` | `KEYO` namespace | Interpretation |
| ---: | --- | --- |
| `1` | `EN_KEY_OBJECT.key_object` | Object selected for the Module |
| `0` | `EN_VIRGIN_OBJECT.virgin_key_object` | Virgin Object describing the unconfigured Module's functional role |

An unconfigured Module is therefore not unidentified or semantically empty. Its Virgin Object describes the role exposed by that Module before an Object is selected. `AS_OBJECT_VIRGIN_OBJECT` relates the Virgin Object to the Objects into which it can be configured; firmware and slot associations further constrain availability on the resolved Physical Device.

Catalogue capability and runtime state answer different questions:

| Evidence | Meaning |
| --- | --- |
| `EN_FIRMWARE.slots` | number of `slot` positions declared by a firmware definition |
| `EN_SLOTS` and `AS_OBJECT_FIRMWARE` | Objects permitted or designated at a `slot` |
| Virgin-Object associations | configurable template and allowed Object set |
| `DIMENSION 30` | configured Object or unconfigured Virgin Object currently reported by the installed Device |
| MyHOME_Suite UI | visible numbering, enabled state, and editability in that application context |

## Example interpretation

Observed Device `00C58E91`, correlated with item model `107` and firmware definition `157`, reported a four-slot runtime layout interpreted as:

| `slot` | Object | Configured | Functional role |
| ---: | ---: | --- | --- |
| `1` | `6` | yes | Light actuator |
| `2` | `6` | yes | Light actuator |
| `3` | `400` | yes | Light control |
| `4` | `500` | no | Automation double command Virgin Object |

For `slot` `4`, `STATE = 0` selects the Virgin Object namespace. `EN_VIRGIN_OBJECT.virgin_key_object = 500` resolves to “Automation double command virgin”; there is no ordinary `EN_KEY_OBJECT.key_object = 500` in this catalogue revision. This table is an interpretation of observed Device state, not a raw transcript or a universal four-slot schema.

The catalogue independently corroborates the four-slot capability: firmware `157` offers actuator Objects at `slot` positions `1` and `2`, command/scenario Objects at slots `3` and `4`, Automation relay Virgin Object `510` at slots `1` and `2`, and Automation double-command Virgin Object `500` at slots `3` and `4`.

## Observed Module-shape differences

- Device `007B269D` demonstrated that `slot` numbering and UI-visible Module numbering can differ: `slot` `2` was absent from the UI while later slots were renumbered for display.
- Device `08CF44BF` demonstrated a large layout with `slot` positions through `17`, consistent with the maximum `EN_SLOTS.first_slot` observed in this catalogue revision.
- Light-control-only Device `00C44420` exposed command Modules as its actual hardware function; those Objects must not be interpreted as alternate actuator modes.

These observations constrain interpretation but do not prove that every Device returns `DIMENSION 30` or uses the same optional response set.

## Errors

`DIMENSION 31` reports Object-state results for a `slot`, including busy, already configured, insufficient capacity, and unsupported Object conditions. Preserve the accompanying configured state and do not substitute the error record for the last valid `DIMENSION 30` assignment.

See [Modules](../device-model/modules.md), [Objects](../device-model/objects.md), and [Virgin Objects](../device-model/virgin-objects.md) for the catalogue structures behind this runtime projection.
