# Memory module

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0065` | Project identity |
| Technical description | Memory module | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F425`, `003552` | Canonical commercial records |
| Catalogue item | `60` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, State recovery, DIN accessory | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F425` | Established identity | canonical commercial record for item `60` |
| Legrand | `003552` | Established identity | canonical commercial record for item `60` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00281-b-UK` | technical sheet | 2012-12-13 | `F425` blackout-memory behavior, electrical characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/0f/28/0f28345d89b8ceccc8d7d91dba8eac68522e215c27b7ee82accb3d777a79233c.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00281-b-uk.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `MQ00281-b-UK` |
| Consumption | `5 mA` | `MQ00281-b-UK` |
| Operating temperature | `0..40 °C` | `MQ00281-b-UK` |
| Dissipated power | `0.1 W` maximum | `MQ00281-b-UK` |
| Width | `2 DIN modules` | `MQ00281-b-UK` |
| Recommended distance from power supply | not more than `10 m` | `MQ00281-b-UK` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `60` | Canonical catalogue |
| Technical item | Memory module | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `187` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `187` | `642` | `30` Memory module | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `187` | Advanced Configuration | supported configuration route for this Device family |
| `187` | Physical configuration | supported configuration route for this Device family |
| `187` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `187` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `187` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `187` | `PL` | catalogue-defined domain | catalogue-scoped | PL |

## Object configuration surfaces

### Object `30` - Memory module

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `60` / `modobj = 54` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`30`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

SCS blackout-memory module that records actuator states and restores managed lighting states after power returns. One module is normally used per system/power-supply domain, with documented behavior for logically expanded systems.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue maps `F425` and `003552` to one technical item. The publisher sheet directly documents `F425`; the old Legrand number `003552` is corroborated by the archived MyHOME catalogue cross-reference.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
