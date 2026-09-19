# `WHO 25` - Transversal Functions

`WHO 25` contains multiple transversal OpenWebNet functions whose grammars are selected by their `WHAT` family. The namespace includes CEN+ virtual-command events and dry-contact/IR state reporting. Sharing `WHO 25` does not make these functions one address or parameter model.

## Reference

| Function | Reference | Established vocabulary |
| --- | --- | --- |
| CEN+ | [CEN+](cen-plus.md) | `WHAT 21..28`; pushbutton `0..31`; virtual Object `0..2047` |
| Dry contact / IR | [Dry Contact and IR](dry-contact-ir.md) | `WHAT 31..32`; state/event parameter `0`/`1` |

## Function selection

A parser should resolve `WHO 25` and then the `WHAT` family before decoding the remaining fields. CEN+ interprets the `WHAT` parameter as a virtual pushbutton and uses a `2`-prefixed virtual Object `WHERE`. Dry-contact/IR operations instead use the parameter to distinguish requested state from event/action context and use device-family-specific `WHERE` ranges.

## CEN+ relationship

CEN+ complements Basic/Evolved CEN under [`WHO 15`](../who-15-cen/). In CEN+, the interaction phase moves into `WHAT 21..24`, the pushbutton becomes a `WHAT` parameter, and the source is represented by a virtual Object. Rotary-selector operations `25..28` extend that model further.

## Dry-contact and IR relationship

The dry-contact/IR family uses `WHAT 31` for ON/detection and `WHAT 32` for OFF/no detection. It remains under the canonical `WHO 25` namespace even though its address grammar is unrelated to CEN+ virtual Objects.

The [functional overview](../) provides alternate navigation by function while these pages remain organized under their canonical protocol namespace.