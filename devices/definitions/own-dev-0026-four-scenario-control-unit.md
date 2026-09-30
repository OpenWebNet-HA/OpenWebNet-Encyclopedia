# Four-scenario control unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0026` | Project identity |
| Technical description | Flush-mounted four-scenario control and storage unit | Catalogue + official automation guide |
| Catalogue item / model | `20` / `modobj 4` | Implementation evidence |
| Firmware applicability | firmware `223`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `N4681` | Catalogue |
| Categories | Scenario control, Automation | Capability model |

## Commercial identities

The canonical catalogue maps BTicino `N4681` to technical item `20`.

## Documentation

The archived official MyHOME automation guide documents the N4681 scenario unit, its four scenario keys, addressing and both physical operating modes.

## Physical and functional characteristics

N4681 exposes four scenario keys with indicator LEDs. The official guide states that previously stored command sequences are activated from those keys and may address actuators outside the unit's own room. Stored scenarios can be modified or deleted.

## Identity

Catalogue item `20` maps to Automation `modobj = 4`.

## Firmware and hardware

Firmware `223` has wildcard applicability `-1.-1.-1` and one Module slot. A sanitized hardware fingerprint remains pending.

## Module, Object, and Virgin Object model

The firmware resolves to Object `2`, **4 scenarios control unit**, with one slot. No Virgin Object is declared for this firmware.

## Configuration modes

The catalogue declares Physical Configuration and Virtual Configuration.

## Firmware-scoped configuration

The firmware exposes `A`, `PL` and `AID`. The Object surface adds `SCE1` through `SCE4` for the four scenario definitions.

The official guide documents two physical addressing modes. With only `PL = 1..9`, the number identifies the scenario unit and activation does not first send OFF commands. With `A` and `PL` populated, they form the unit address; scenario activation first resets actuators in the configured room before applying the scenario.

## Object configuration surfaces

Object `2` owns the four scenario fields. The scenario payload semantics belong to the reusable scenario-control Object rather than four independent Modules.

## Conditions, filters, and conversions

The technical inventory records no Device-specific conditions, filters or conversions for this item.

## Diagnostic applicability

Identity, firmware, Object, address and configuration should be interpreted through the standard Device diagnostics described in [Diagnostics](../../diagnostics/).

## Functional applicability

The Device is a scenario-control endpoint. Scenario actions can target multiple functional domains; they must not be reduced to the Device's own `A/PL` address.

## Observed behavior and corroboration

No sanitized hardware capture for this exact Device is currently retained.

## Programming

Preserve the distinction between the `PL`-only mode and the `A + PL` room-reset mode. The official guide explicitly notes that the latter cannot manage scenarios by activating L4674 dimmer actuators.

## Source reconciliation

The canonical database and archived official automation guide agree on the one-slot four-scenario topology and physical addressing. The guide supplies the behavior that the database alone cannot express: four stored scenarios and the two activation/reset modes.

## Evidence limits and open work

- Add a sanitized N4681 hardware fingerprint.
- Corroborate scenario programming frames from first-hand traffic.
- Preserve the documented L4674 limitation as revision-scoped behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
