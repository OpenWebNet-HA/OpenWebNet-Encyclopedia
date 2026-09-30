# DIN dimmer 1000 W

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0025` | Project identity |
| Technical description | One-channel DIN SCS dimmer for resistive and ferromagnetic-transformer loads | Catalogue + official technical sheet |
| Catalogue item / model | `17` / `modobj 133` | Implementation evidence |
| Firmware applicability | firmware `176`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `F414`, `003652` | Catalogue |
| Categories | Actuator, Dimmer, Lighting | Capability model |

## Commercial identities

BTicino `F414` and Legrand `003652` share catalogue item `17`.

## Documentation

Dedicated technical sheet `MQ00278_e_EN` and the official SCS guide are archived under [Device Sources](../../sources/devices/). MyHOME Suite documents dimmer modes, while current F460/F461 documentation supplies production-batch compatibility boundaries.

## Physical and electrical characteristics

The official sheet establishes a one-output, 4-DIN dimmer for resistive loads and ferromagnetic transformers. Short control presses switch the load; long presses adjust brightness. The actuator can report load faults such as lamp failure and has a replaceable fuse. SCS nominal supply is `27 Vdc`, operating supply `18..27 Vdc`, current draw `9 mA`, and published F414 load range `0.25..4.3 A`, `60..1000 VA`.

## Identity

Catalogue item `17` maps to Automation `modobj = 133`.

## Firmware and hardware

Firmware `176` is wildcard `-1.-1.-1` and declares one Module. Current F460/F461 compatibility documentation maps Legrand `003652` from production batch `09W50` and BTicino `F414` from `09W29`; MyHOME_Up documentation independently gives F414 `09W29`.

## Module, Object, and Virgin Object model

One fixed Object `8`, Dimmer actuator, occupies slot `1`. There is no Virgin Object.

## Configuration modes

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

`A`, `PL`, and `G1` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `AID` is the identity field. MyHOME Suite identifies F414 as an inductive/halogen-capable dimmer with Master, delayed Slave, Master PUL and Slave PUL modes.

## Object configuration surfaces

Object `8` supplies the reusable Dimmer-actuator model. Device-specific applicability is restricted by the documented load technology; F414 is not a generic modern multi-load dimmer.

## Conditions, filters, and conversions

One slot condition and one conversion rule are recorded. Generic resolution belongs in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

`DIMENSION 1`, `2`, `30`, `32`, and `35` apply. WHO 1 dimmer runtime `DIMENSION 4` is relevant but F414/MH200 support remains unresolved: tester reports describe timeout followed by `NACK`, while the raw exchange has not been preserved.

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/) as a dimmer actuator.

## Observed behavior and corroboration

No raw F414/MH200 DIM4 trace is retained; the tester report remains unresolved evidence.

## Programming

Preserve inductive/resistive load constraints and distinguish F414 from capacitive/electronic-transformer variants such as F415.

## Source reconciliation

The dedicated sheet establishes load type, electrical range, local button behavior, dimming interaction, fault indication and fuse behavior. The SCS guide corroborates `60..1000 VA`. MyHOME Suite confirms mode/load applicability. F460/F461 and MyHOME_Up documentation add production-batch boundaries. The remaining issue is runtime DIM4 behavior through MH200, not basic Device definition.

## Evidence limits and open work

- Preserve a raw F414/MH200 DIM4 request/timeout/`NACK` exchange.
- Hardware-corroborate `modobj`, firmware, address and configurator count.
- Archive historical sheet revisions when they materially change load/fuse data.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [Reverse Engineering Open Questions](../../reverse-engineering/open-questions.md)
- [MyHOME Suite dimmer functions](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_attuatore_dimmer.html)
