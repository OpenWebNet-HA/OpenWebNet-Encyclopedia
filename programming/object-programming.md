# Object Programming

Object programming assigns a logical Object to each firmware-exposed Module during advanced configuration.

## Write frame

`*#[WHO]*0*#30*[SLOT]*[KEYO]##`

| Field | `OPEN.db` range | Meaning |
| --- | ---: | --- |
| `SLOT` | `1..255` | Device-local `slot` |
| `KEYO` | `1..65535` | target Object number |

`KEYO` is the external `EN_KEY_OBJECT.key_object` value, not `EN_KEY_OBJECT.id_key_object`.

## Replacement-style transfer

The canonical `ConfKO` sequence begins with:

`*[WHO]*14#0*0##`

`OPEN.db` describes this as resetting all Device Objects. The sequence then requires repeated Object writes and later sends addresses and parameters. Treat this as a full replacement transfer: construct and validate the complete desired Module/Object layout before sending reset-all.

`OPEN.db` also registers:

`*[WHO]*14#[SLOT]*0##`

for resetting one `slot`. It is not a member of the canonical `ConfKO` sequence, so its standalone lifecycle and completion behavior are not established by that scenario.

## Resolving the permitted Object

1. Resolve the Physical Device item and firmware.
2. Resolve the target `SLOT` against the firmware's slot structures.
3. Determine whether the current diagnostic `KEYO` is a configured Object or Virgin Object from `DIMENSION 30.STATE`.
4. If unconfigured, resolve `KEYO` through `EN_VIRGIN_OBJECT.virgin_key_object`.
5. Use `AS_OBJECT_VIRGIN_OBJECT` to find Objects permitted by that Virgin Object.
6. Use `AS_OBJECT_FIRMWARE` and `EN_SLOTS` to require firmware and slot support.
7. Respect `EN_SLOTS.fixed_ko` and slot conditions.
8. Use the target Object's external `key_object` in the programming frame.

A Virgin Object constrains the Module's configurable role. It is not itself the configured Object to send unless independent evidence establishes that a specific Device expects such a write.

## Fixed and absent Modules

A fixed Object is catalogue capability, not permission to overwrite it. Hidden UI Modules and gaps in UI numbering do not change protocol `SLOT` values.

Do not synthesize Modules up to `EN_FIRMWARE.slots` merely because the firmware declares a capacity. Use the actual slot/Object associations and the current diagnostic projection.

## Sequence behavior

The Object write is both mandatory and repeatable. It starts the 50-second `DeviceKOTimeOut` and a two-second `CmdKoValueTimeWait`. `NACK` transitions to Error.

After all Object, address, and parameter writes, the programmer sends `WHAT 4` end of transmission. The Device can then return `WHAT 52`, `WHAT 51`, a structured error, or abort.

## Object errors

| `DIMENSION 31` code | `OPEN.db` meaning |
| ---: | --- |
| `0` | Object not implemented/unset |
| `1` | Object busy |
| `2` | Object already configured |
| `3` | insufficient free Object capacity |
| `4` | requested Object not implemented |

Codes `0`, `2`, `3`, and `4` are fatal errors in `ConfKO`. Busy code `1` is classified as error-and-information but still maps to Error through `status4error` in that sequence. Retain the accompanying `STATE` and `slot`.

See [Modules](../device-model/modules.md), [Objects](../device-model/objects.md), [Virgin Objects](../device-model/virgin-objects.md), and [`DIMENSION 30`](../diagnostics/dim30-modules.md).
