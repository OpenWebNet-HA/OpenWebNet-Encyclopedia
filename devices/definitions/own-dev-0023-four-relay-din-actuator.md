# Four-relay DIN actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0023` | Project identity |
| Technical description | Four-independent-relay 2-DIN actuator for lighting and paired automation/motor loads | Catalogue + official documentation |
| Catalogue item / model | `3` / `modobj 130` | Implementation evidence |
| Firmware applicability | firmware `142`, `-1.-1.-1`, four slots | Implementation evidence |
| Commercial identities | `F411/4`, `003844` | Catalogue |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

BTicino `F411/4` and Legrand `003844` share item `3`.

## Documentation

The archived MyHOME automation guide is reconciled with current BTicino product data and technical sheet `ST_00000896_IT`.

## Physical and electrical characteristics

Current product data describes four independent relays in two DIN modules, local/manual operation, LED indication, `27 Vdc` nominal supply, `40 mA` input current and `18..27 V` operation. Current load data includes `2 A` rated switching, `500 W` motor reducers, `2 A cosφ 0.5` ferromagnetic transformers and `70 W` fluorescent loads. The technical sheet shows a `10 A` protective breaker for its lighting example and paired motor/shutter wiring. Relays can be logically interlocked.

## Identity

Catalogue item `3` maps to Automation `modobj = 130`.

## Firmware and hardware

Firmware `142` is wildcard `-1.-1.-1` and declares four Modules.

## Module, Object, and Virgin Object model

All four slots can be Object `6`, Light actuator. Object `7`, Automation actuator, is a candidate on slots `1..3`; Object `1`, Blind actuator, is a candidate beginning at slot `1`. Virgin Object `510`, Automation relay virgin, applies across slots `1..4` and permits Objects `1`, `6`, and `7`.

## Configuration modes

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

`A` and `PL1..PL4` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `AID` is the identity field.

## Object configuration surfaces

Selected slots reuse the Light, Automation, or Blind actuator configuration models. Pairing/interlocking must remain consistent with resolved topology.

## Conditions, filters, and conversions

Eight slot conditions and three conversion rules constrain the four slots. Do not flatten the candidate set into four unconditional Objects.

## Diagnostic applicability

`DIMENSION 30` is especially important because physical relay channels can resolve to different Object roles. `DIMENSION 1`, `2`, `32`, and `35` provide the remaining identity/configuration evidence.

## Functional applicability

The Device can expose [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Resolve slot conditions before assigning relay roles. Motor/shutter arrangements require logical interlocking; a four-light arrangement keeps four independent lighting Modules.

## Source reconciliation

Official documentation corroborates four physical outputs, local control and paired motor use. The Virgin-Object topology explains the shared lighting/automation/blind capability. Older catalogues publish different lamp-load figures; this dossier keeps current values source-scoped.

## Evidence limits and open work

- Archive `ST_00000896` byte-for-byte in the Device source manifest.
- Hardware-corroborate representative four-light and paired-motor configurations.
- Publish an exact `M` to slot-condition topology table after conversion-rule review.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [BTicino F411/4](https://www.bticino.com/products/bt-f411-4)
