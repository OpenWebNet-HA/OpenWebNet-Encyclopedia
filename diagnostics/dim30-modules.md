# `DIMENSION 30`: Modules and Objects

`DIMENSION 30` reports the Object assigned to a firmware-exposed Module and whether that assignment is configured.

## Frame

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `SLOT` | `1`–`255` | numeric internal slot |
| `KEYO` | `1`–`65535` | Object number |
| `STATE` | `0`–`1` | unconfigured/configured state |

Use **Module** for the logical container and **internal slot** for `SLOT`. `OPEN.db` uses the legacy label “ko slot”; this documentation retains that wording only when quoting or naming source fields.

## Catalogue interpretation

| Diagnostic field | Catalogue concept | Status |
| --- | --- | --- |
| `SLOT` | `EN_SLOTS.first_slot` placement | structurally corroborated |
| `KEYO` | `EN_KEY_OBJECT.key_object` | structurally and behaviorally corroborated |
| `STATE` | installed runtime state | direct database label; no single catalogue column equivalent |

`KEYO` is not `EN_KEY_OBJECT.id_key_object`. The former is the exposed Object number; the latter is an internal catalogue row key.

Likewise, `SLOT` is not `EN_SLOTS.id_slot`. Diagnostic `SLOT` is a Device-local position correlated with catalogue placement such as `EN_SLOTS.first_slot`; `id_slot` identifies a database association row.

## Building the Module list

1. Group records by Physical Device interview.
2. Use `SLOT` as the Device-local internal-slot key.
3. Resolve `KEYO` against `EN_KEY_OBJECT.key_object`.
4. retain `STATE` even when the Object is known.
5. Attach `DIMENSION 32` address data using the same internal slot.
6. Attach `DIMENSION 35` configuration values only when both Device and internal slot match.

Do not renumber internal slots to match a UI’s visible Module numbering. MyHOME_Suite can hide or relabel slots, and observed scenario Devices show UI numbering that differs from the numeric diagnostic position.

## Configured and unconfigured Modules

`STATE 1` indicates configured and `STATE 0` indicates unconfigured according to `OPEN.db`. An unconfigured record is still meaningful: it can expose a Virgin-Object/template state or a supported Module position.

The diagnostic frame reports an Object number even when `STATE` is false. Whether that number represents a Virgin Object, default Object, placeholder, or Device-specific unconfigured state must be established for the particular firmware. Do not globally join it to `EN_VIRGIN_OBJECT.virgin_key_object` merely because the numbers match.

Catalogue capability and runtime state answer different questions:

| Evidence | Meaning |
| --- | --- |
| `EN_FIRMWARE.slots` | number of internal slots declared by a firmware definition |
| `EN_SLOTS` and `AS_OBJECT_FIRMWARE` | Objects permitted or designated at an internal slot |
| Virgin-Object associations | configurable template and allowed Object set |
| `DIMENSION 30` | Object and configured state currently reported by the installed Device |
| MyHOME_Suite UI | visible numbering, enabled state, and editability in that application context |

## Example interpretation

Observed Device `00C58E91`, correlated with item model `107` and firmware definition `157`, reported a four-slot runtime layout interpreted as:

| Internal slot | Object | Configured | Functional role |
| ---: | ---: | --- | --- |
| `1` | `6` | yes | Light actuator |
| `2` | `6` | yes | Light actuator |
| `3` | `400` | yes | Light control |
| `4` | `500` | no | unconfigured/virgin state |

This table is an interpretation of observed Device state, not a raw transcript or a universal four-slot schema.

The catalogue independently corroborates the four-slot capability: firmware `157` offers actuator Objects at internal slots `1` and `2`, command/scenario Objects at slots `3` and `4`, Automation relay Virgin Object `510` at slots `1` and `2`, and Automation double-command Virgin Object `500` at slots `3` and `4`.

## Observed Module-shape differences

- Device `007B269D` demonstrated that internal-slot numbering and UI-visible Module numbering can differ: internal slot `2` was absent from the UI while later slots were renumbered for display.
- Device `08CF44BF` demonstrated a large layout with internal slots through `17`, consistent with the maximum `EN_SLOTS.first_slot` observed in this catalogue revision.
- Light-control-only Device `00C44420` exposed command Modules as its actual hardware function; those Objects must not be interpreted as alternate actuator modes.

These observations constrain interpretation but do not prove that every Device returns `DIMENSION 30` or uses the same optional response set.

## Errors

`DIMENSION 31` reports Object-state results for an internal slot, including busy, already configured, insufficient capacity, and unsupported Object conditions. Preserve the accompanying configured state and do not substitute the error record for the last valid `DIMENSION 30` assignment.

See [Modules](../device-model/modules.md), [Objects](../device-model/objects.md), and [Virgin Objects](../device-model/virgin-objects.md) for the catalogue structures behind this runtime projection.
