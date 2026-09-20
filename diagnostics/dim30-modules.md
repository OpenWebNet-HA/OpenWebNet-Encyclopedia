# `DIMENSION 30`: Modules and Objects

`DIMENSION 30` reports whether a firmware-exposed Module is enabled or disabled and, accordingly, the regular configured Object or Virgin Object that identifies it.

## Frame

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `SLOT` | `1..255` | numeric `slot` |
| `KEYO` | `1..65535` | Object or Virgin Object number, selected by `STATE` |
| `STATE` | `0..1` | Module enabled/disabled state |

Use **Module** for the logical container and **`slot`** for `SLOT`. `OPEN.db` uses the legacy label “ko slot”; this documentation retains that wording only when quoting or naming source fields.

## Catalogue interpretation

| Diagnostic field | Catalogue concept | Status |
| --- | --- | --- |
| `SLOT` | `EN_SLOTS.first_slot` placement | structurally corroborated |
| `KEYO`, when `STATE = 0` | `EN_KEY_OBJECT.key_object` | regular configured Object; experimentally and behaviorally corroborated |
| `KEYO`, when `STATE = 1` | `EN_VIRGIN_OBJECT.virgin_key_object` | Virgin Object for a disabled Module; experimentally and behaviorally corroborated |
| `STATE` | installed Module enabled/disabled state | `OPEN.db` supplies the binary field and generic label; polarity is established by controlled diagnostic/programming evidence correlated with MyHOME_Suite UI behavior |

`KEYO` selects one of two external number spaces according to `STATE`. It is not the internal catalogue key `EN_KEY_OBJECT.id_key_object` or `EN_VIRGIN_OBJECT.id_virgin_key_object`, even where a particular database revision happens to assign equal numeric values.

Likewise, `SLOT` is not `EN_SLOTS.id_slot`. Diagnostic `SLOT` is a Device-local position correlated with catalogue placement such as `EN_SLOTS.first_slot`; `id_slot` identifies a database association row.

## Building the Module list

1. Group records by Physical Device interview.
2. Use `SLOT` as the Device-local `slot` key.
3. When `STATE = 0`, resolve `KEYO` against `EN_KEY_OBJECT.key_object`; the Module is enabled.
4. When `STATE = 1`, resolve `KEYO` against `EN_VIRGIN_OBJECT.virgin_key_object`; the Module is disabled.
5. Use the resolved Virgin Object and its catalogue associations to derive the disabled Module's functional role and permitted Object set.
6. Retain `STATE` alongside the resolved record so an Object and Virgin Object are never conflated.
7. Attach `DIMENSION 32` address data using the same `slot`.
8. Attach `DIMENSION 35` configuration values only when both Device and `slot` match.

Do not renumber `slot` positions to match a UI’s visible Module numbering. MyHOME_Suite can hide or relabel slots, and observed scenario Devices show UI numbering that differs from the numeric diagnostic position.

## Enabled and disabled Modules

Controlled diagnostic/programming experiments correlated with direct MyHOME_Suite UI observations establish the `DIMENSION 30` polarity. `OPEN.db` describes `STATE` generically as “configured or not configured”, but that label does not establish the numeric polarity by itself:

| `STATE` | Module state | `KEYO` namespace | Interpretation |
| ---: | --- | --- | --- |
| `0` | enabled | `EN_KEY_OBJECT.key_object` | regular configured Object currently applying to the Module |
| `1` | disabled | `EN_VIRGIN_OBJECT.virgin_key_object` | Virgin Object representing the disabled Module's configurable role |

A disabled Module is therefore not unidentified or semantically empty. Its Virgin Object describes the configurable role retained while the regular Object is not active. `AS_OBJECT_VIRGIN_OBJECT` relates that Virgin Object to permitted regular Objects; firmware and `slot` associations further constrain availability on the resolved Physical Device.

This polarity is specific to the `STATE` field of diagnostic/programming `DIMENSION 30`. Do not transfer it to `DIMENSION 31` or to unrelated fields named `STATE` without independent evidence.

Catalogue capability and runtime state answer different questions:

| Evidence | Meaning |
| --- | --- |
| `EN_FIRMWARE.slots` | number of `slot` positions declared by a firmware definition |
| `EN_SLOTS` and `AS_OBJECT_FIRMWARE` | Objects permitted or designated at a `slot` |
| Virgin-Object associations | configurable template and allowed Object set |
| `DIMENSION 30` | enabled regular Object or disabled Virgin Object currently reported by the installed Device |
| MyHOME_Suite UI | visible numbering, enabled state, and editability in that application context |

## Evidence and interpretation

The corrected polarity comes from controlled changes of Module enablement during diagnostic/programming work, with the resulting `DIMENSION 30.STATE` and `KEYO` values correlated directly with MyHOME_Suite's enabled/disabled presentation. Catalogue lookups then corroborate which external namespace the reported `KEYO` belongs to. The catalogue alone does not define the numeric polarity.

Earlier documentation used a Device-specific example to argue the opposite mapping from a catalogue lookup. That conclusion was circular: it selected the namespace using the assumed polarity and then treated the lookup as confirmation. The corrected interpretation therefore keeps catalogue capability evidence separate from the experimentally established `STATE` polarity.

## Observed Module-shape differences

- Device `007B269D` demonstrated that `slot` numbering and UI-visible Module numbering can differ: `slot` `2` was absent from the UI while later slots were renumbered for display.
- Device `08CF44BF` demonstrated a large layout with `slot` positions through `17`, consistent with the maximum `EN_SLOTS.first_slot` observed in this catalogue revision.
- Light-control-only Device `00C44420` exposed command Modules as its actual hardware function; those Objects must not be interpreted as alternate actuator modes.

These observations constrain interpretation but do not prove that every Device returns `DIMENSION 30` or uses the same optional response set.

## Errors

`DIMENSION 31` reports Object-state results for a `slot`, including busy, already configured, insufficient capacity, and unsupported Object conditions. Preserve its accompanying `STATE` value as a distinct field and do not apply the `DIMENSION 30` polarity to it without independent evidence. Do not substitute an error record for the last valid `DIMENSION 30` assignment.

See [Modules](../device-model/modules.md), [Objects](../device-model/objects.md), and [Virgin Objects](../device-model/virgin-objects.md) for the catalogue structures behind this runtime projection.
