# Scenario programmer

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0080` | Project identity |
| Technical description | Scenario programmer | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH200` | Canonical commercial records |
| Catalogue item | `98` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `4` | Canonical inventory |
| Firmware definition | `2.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Scenarios, Integration, Ethernet programmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH200` | Established identity | canonical commercial record for item `98` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `TiMH200_FR` | software/configuration manual | version 2.03; 06/07-01 PC | Configuration, Ethernet transfer, scenario editing and firmware update for `MH200` | [Archived original](https://archive.openwebnet-ha.org/sha256/00/64/00649f4d577863eab8a6366529468044a7fdce4d2b868cdcd09b8f4f634a01ea.pdf) | [Official source](https://www.bticino.be/sites/default/files/Service-en-support/software-en-schemas2/Audio-Video/MH200/Version%202_1_00/TiMH200_FR.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Network interface | Ethernet LAN | `TiMH200_FR`, printed p. 8 / PDF p. 8 |
| Project transfer | Ethernet crossover/direct LAN or remote IP connection | `TiMH200_FR`, printed p. 8 / PDF p. 8 |
| Automation connection context | MyHOME Automation BUS | `TiMH200_FR`, printed pp. 16-18 / PDF pp. 16-18 |
| Declared module count | `1` | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `98` | Canonical catalogue |
| Technical item | Scenario programmer | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `4` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `210` | `2` | `0` | `0` | `1` | catalogue default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `210` | `1188` | `61` Scenario scheduler | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `210` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `210` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `210` | `SYSADDRESS` | catalogue-defined domain | catalogue-scoped | Univocal code |
| `210` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `210` | `LAN_IP_ADDR_TYPE` | catalogue-defined domain | catalogue-scoped | Local IP dynamicity |
| `210` | `CMD_PORT` | catalogue-defined domain | catalogue-scoped | Commands port |
| `210` | `IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Public IP address |
| `210` | `CONNECTION_METHOD` | catalogue-defined domain | catalogue-scoped | Public IP dynamicity |

## Object configuration surfaces

### Object `61` - Scenario scheduler

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP address |
| `LAN_IP_ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP dynamicity |
| `CONNECTION_METHOD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Public IP dynamicity |
| `IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Public IP address |
| `CMD_PORT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Commands port |
| `IS_GATEWAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Gateway |
| `SYSADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Univocal code |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `98` / `modobj = 4` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`61`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Programmable scenario controller configured with TiMH200. Projects define time- or event-driven scenarios, are transferred over Ethernet, and can coordinate MyHOME Automation devices and F422-separated installations.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue identifies a single `MH200` commercial identity with firmware `2.0.0`. The retained official TiMH200 manual directly targets the MH200 Scenario Programmer and documents Ethernet programming, project transfer and firmware update without importing MH200N-specific electrical characteristics.

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
