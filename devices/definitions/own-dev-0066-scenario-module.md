# Scenario module

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0066` | Project identity |
| Technical description | Scenario module | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F420`, `003551` | Canonical commercial records |
| Catalogue item | `61` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, Scenarios, DIN accessory | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F420` | Established identity | canonical commercial record for item `61` |
| Legrand | `003551` | Established identity | canonical commercial record for item `61` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00067-d-EN` | technical sheet | 2014-06-05 | `F420` scenario capacity, electrical data and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/a9/3b/a93b06343116dda6e4db771a72ab51ac2822748f79ba8eababe1b2a3f453a007.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00067_d_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `MQ00067-d-EN` |
| Current draw | `20 mA` | `MQ00067-d-EN` |
| Operating temperature | `0..40 °C` | `MQ00067-d-EN` |
| Width | `2 DIN modules` | `MQ00067-d-EN` |
| Scenario capacity | up to `16` scenarios | `MQ00067-d-EN` |
| Controls per scenario | up to `100` | `MQ00067-d-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `61` | Canonical catalogue |
| Technical item | Scenario module | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `196` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `196` | `700` | `3` Scenario module | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `196` | Physical configuration | supported configuration route for this Device family |
| `196` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `196` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `196` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `196` | `PL` | catalogue-defined domain | catalogue-scoped | PL |

## Object configuration surfaces

### Object `3` - Scenario module

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `61` / `modobj = 55` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`3`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

DIN scenario-memory module storing up to 16 scenarios with up to 100 controls each. Scenarios are associated with controls through the module address, with dedicated front-panel programming lock and erase functions.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue maps `F420` and `003551`. The dedicated publisher technical sheet documents `F420`, while the archived MyHOME catalogue provides the old/new commercial cross-reference.

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
