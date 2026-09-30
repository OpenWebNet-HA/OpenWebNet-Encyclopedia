# Two-relay DIN actuator 10 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0022` | Project identity |
| Technical description | Two-independent-relay DIN actuator for lighting, automation and paired motor loads | Catalogue + official documentation |
| Catalogue item / model | `2` / `modobj 129` | Implementation evidence |
| Firmware applicability | firmware `132`, `-1.-1.-1`, two slots | Implementation evidence |
| Commercial identities | `F411/2`, `003842` | Catalogue |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

BTicino `F411/2` and Legrand `003842` are the two canonical commercial records for item `2`.

## Documentation

The archived official MyHOME automation guide and the current BTicino product record are reconciled with MyHOME Suite light-actuator function documentation.

## Physical and electrical characteristics

F411/2 is a 2-DIN, two-relay actuator with local/manual control and LED indication. Current BTicino data gives `27 Vdc`, `28 mA`, `1380 W` maximum switching power, two contacts and `18..27 V` operating voltage. Current product text gives `10 A` resistive, `6 A` filament, `500 W` motor reducers, `2 A cosφ 0.5` ferromagnetic transformers and `250 W` fluorescent loads. Older guides contain lower values for some load classes and remain revision-scoped. The relays can be logically interlocked for motor/shutter use.

## Identity

Catalogue item `2` maps to Automation `modobj = 129`.

## Firmware and hardware

Firmware `132` is wildcard `-1.-1.-1` and declares two Module slots.

## Module, Object, and Virgin Object model

Slots `1` and `2` default to Object `6`, Light actuator. Slot `1` also has Object `7`, Automation actuator, as a candidate. Virgin Object `510`, Automation relay virgin, applies to both slots and permits Object `1` Blind actuator, Object `6` Light actuator and Object `7` Automation actuator.

## Configuration modes

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

`A`, `PL1`, `PL2`, and `G1` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `AID` is the identity field. The shared `A` plus separate `PL1/PL2` addresses the two outputs.

## Object configuration surfaces

Objects `1`, `6`, and `7` contribute their reusable blind, lighting and automation parameter models when selected.

## Conditions, filters, and conversions

Three slot conditions and two conversion rules govern legal topology. Candidate row order must not be used to choose the active Object.

## Diagnostic applicability

Use `DIMENSION 1`, `2`, `30`, `32`, and `35`; see [Diagnostics](../../diagnostics/).

## Functional applicability

The selected topology can expose [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Preserve both slots independently. Motor/shutter configurations require the documented logical interlock.

## Source reconciliation

The database Virgin-Object topology explains the documented single, double and combined-load behavior: the relay slots can remain lighting channels or resolve to automation/blind roles. Current and historical load tables differ, so current ratings are stated with source scope rather than overwriting older revisions.

## Evidence limits and open work

- Archive a dedicated current F411/2 technical sheet if exposed by the publisher.
- Hardware-corroborate Object selection and interlock configurations.
- Establish the exact physical configurator-position count from dedicated documentation or hardware.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [BTicino F411/2](https://www.bticino.com/products/bt-f411-2)
