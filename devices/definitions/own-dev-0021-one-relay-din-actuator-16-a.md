# One-relay DIN actuator 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0021` | Project identity |
| Technical description | DIN-rail one-relay lighting actuator with local load control | Catalogue + official automation documentation |
| Catalogue item / model | `1` / `modobj 137` | Implementation evidence |
| Firmware applicability | firmware `166`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `F411/1N`, `003841` | Catalogue |
| Categories | Actuator, Lighting | Capability model |

The shared technical item covers BTicino `F411/1N` and Legrand `003841`.

## Commercial identities

| Brand | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F411/1N` | Established identity | Catalogue + official automation guide |
| Legrand | `003841` | Shared technical item | Canonical catalogue |

## Documentation

The official MyHOME automation guide covers F411/1N product data, load limits, installation and configuration. MyHOME Suite separately documents the light-actuator mode matrix. The publisher guide is archived under [Device Sources](../../sources/devices/).

## Physical and electrical characteristics

The official guide describes a 2-DIN actuator with one changeover relay and local load-control pushbutton. Its later load table gives `10 A` resistive / `2300 W` at 230 Vac, `500 W` LED, `4 A` linear-fluorescent/electronic-transformer and `4 A cosφ 0.5` ferromagnetic-transformer capability. Older catalogues use the family label 16 A and contain revision-dependent load figures, so load-specific limits are retained instead of treating 16 A as universal. Fluorescent-load guidance requires at least `3 m` between actuator and load.

## Identity

Catalogue item `1` maps to Automation `modobj = 137`.

## Firmware and hardware

Firmware `166` has wildcard applicability `-1.-1.-1` and declares one Module. Installed firmware/hardware remains to be corroborated.

## Module, Object, and Virgin Object model

The single fixed Module is Object `6`, Light actuator, on slot `1`. Firmware `166` has no Virgin Object.

## Configuration modes

Physical configuration, Virtual Configuration and Advanced Configuration are declared.

## Firmware-scoped configuration

`A` and `PL` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `G1`, `G2`, `G3` are `0..9`; `AID` is the implementation identity field. MyHOME Suite documents Master, delayed Slave, Master PUL and Slave PUL behavior.

## Object configuration surfaces

Object `6` supplies the reusable Light-actuator configuration surface. Device programming must preserve all three physical group positions.

## Conditions, filters, and conversions

The technical inventory records one condition and one conversion rule. Generic evaluation belongs in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

`DIMENSION 1`, `2`, `30`, `32` and `35` apply for identity, firmware, Object, address and configuration. See [Diagnostics](../../diagnostics/).

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact item is currently retained.

## Programming

Treat the product as one independently addressed Light actuator and preserve delayed-Slave/PUL and `G1..G3` semantics.

## Source reconciliation

The database, official automation guide and MyHOME Suite actuator documentation are reconciled. The material source tension is rating nomenclature: the item is named 16 A while published load-specific limits vary by load and revision. This dossier therefore does not infer a universal 16 A load capability.

## Evidence limits and open work

- Archive a dedicated F411/1N technical-sheet revision if a current publisher endpoint is recovered.
- Add a sanitized hardware fingerprint.
- Preserve historical load-table revisions explicitly.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MyHOME Suite lighting actuator functions](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_attuatore_luci.html)
