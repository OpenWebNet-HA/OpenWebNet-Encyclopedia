# SCS/SCS interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0078` | Project identity |
| Technical description | SCS/SCS interface | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F422`, `003562` | Canonical commercial records |
| Catalogue item | `90` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `251` | Canonical inventory |
| Firmware definition | `-1.-1.-1`; `6.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Integration, SCS gateway, Bus separation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F422` | Established identity | canonical commercial record for item `90` |
| Legrand | `003562` | Established identity | canonical commercial record for item `90` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00280-f-EN` | technical sheet | publisher technical sheet | `F422` SCS/SCS interface electrical data and six operating modes | [Archived original](../../sources/devices/documents/device-doc-f422-mq00280-f-en/MQ00280_f_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00280_f_EN.pdf) |
| MyHOME Server compatibility table | compatibility documentation | current publisher support | Corroborates `F422` / `003562` pairing; PDF p. 7 | [Archived original](../../sources/devices/documents/device-doc-f460-f461-ra00224aa-en/RA00224AA_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00224AA_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `MQ00280-f-EN` |
| Current draw - IN side | `25 mA` | `MQ00280-f-EN` |
| Current draw - OUT side | `5 mA` | `MQ00280-f-EN` |
| Maximum dissipated power | `1 W` | `MQ00280-f-EN` |
| Width | `2 DIN modules` | `MQ00280-f-EN` |
| Interfaces | two SCS BUS domains | `MQ00280-f-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `90` | Canonical catalogue |
| Technical item | SCS/SCS interface | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `251` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `143` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |
| `722` | `6` | `0` | `0` | `1` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `143` | `508` | `74` Interface SCS / SCS Logic | catalogue firmware/Object relation |
| `143` | `509` | `75` Interface SCS / SCS physical | catalogue firmware/Object relation |
| `143` | `510` | `76` Interface SCS / SCS galvanic | catalogue firmware/Object relation |
| `143` | `511` | `77` Interface SCS / SCS burglar alarm | catalogue firmware/Object relation |
| `143` | `512` | `78` Interface SCS / SCS public riser | catalogue firmware/Object relation |
| `143` | `513` | `79` Interface SCS / SCS access control | catalogue firmware/Object relation |
| `143` | `514` | `496` Interface SCS / SCS physical separation | catalogue firmware/Object relation |
| `722` | `2637` | `74` Interface SCS / SCS Logic | catalogue firmware/Object relation |
| `722` | `2638` | `75` Interface SCS / SCS physical | catalogue firmware/Object relation |
| `722` | `2639` | `76` Interface SCS / SCS galvanic | catalogue firmware/Object relation |
| `722` | `2640` | `77` Interface SCS / SCS burglar alarm | catalogue firmware/Object relation |
| `722` | `2641` | `78` Interface SCS / SCS public riser | catalogue firmware/Object relation |
| `722` | `2643` | `496` Interface SCS / SCS physical separation | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `143` | `524` | catalogue candidate/template association |
| `722` | `524` | catalogue candidate/template association |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `143` | Advanced Configuration | supported configuration route for this Device family |
| `143` | Physical configuration | supported configuration route for this Device family |
| `143` | Virtual Configuration | supported configuration route for this Device family |
| `722` | Advanced Configuration | supported configuration route for this Device family |
| `722` | Physical configuration | supported configuration route for this Device family |
| `722` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `143` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `143` | `I1` | catalogue-defined domain | catalogue-scoped | I1 |
| `143` | `I2` | catalogue-defined domain | catalogue-scoped | I2 |
| `143` | `I3` | catalogue-defined domain | catalogue-scoped | I3 |
| `143` | `I4` | catalogue-defined domain | catalogue-scoped | I4 |
| `143` | `MOD` | catalogue-defined domain | catalogue-scoped | MOD |
| `722` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `722` | `I1` | catalogue-defined domain | catalogue-scoped | I1 |
| `722` | `I2` | catalogue-defined domain | catalogue-scoped | I2 |
| `722` | `I3` | catalogue-defined domain | catalogue-scoped | I3 |
| `722` | `I4` | catalogue-defined domain | catalogue-scoped | I4 |
| `722` | `MOD` | catalogue-defined domain | catalogue-scoped | MOD |

## Object configuration surfaces

### Object `74` - Interface SCS / SCS Logic

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 3 |
| `I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 4 |

### Object `75` - Interface SCS / SCS physical

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 3 |
| `I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 4 |

### Object `76` - Interface SCS / SCS galvanic

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address |

### Object `77` - Interface SCS / SCS burglar alarm

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address |

### Object `78` - Interface SCS / SCS public riser

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I1I2I3I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Internal unit address |

### Object `79` - Interface SCS / SCS access control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 1 |
| `I2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 2 |
| `I3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 3 |
| `I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automation interface address 4 |

### Object `496` - Interface SCS / SCS physical separation

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `I4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address |
| `ADDRESSES_MANAGED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 1 |
| `ADDRESSES_MANAGED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 2 |
| `ADDRESSES_MANAGED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 3 |
| `ADDRESSES_MANAGED_4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 4 |
| `ADDRESSES_MANAGED_5` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 5 |
| `ADDRESSES_MANAGED_6` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 6 |
| `ADDRESSES_MANAGED_7` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 7 |
| `ADDRESSES_MANAGED_8` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 8 |
| `ADDRESSES_MANAGED_9` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 9 |
| `ADDRESSES_MANAGED_10` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 10 |
| `ADDRESSES_MANAGED_11` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 11 |
| `ADDRESSES_MANAGED_12` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 12 |
| `ADDRESSES_MANAGED_13` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 13 |
| `ADDRESSES_MANAGED_14` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 14 |
| `ADDRESSES_MANAGED_15` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 15 |
| `ADDRESSES_MANAGED_16` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 17 |
| `ADDRESSES_MANAGED_17` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 17 |
| `ADDRESSES_MANAGED_18` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 18 |
| `ADDRESSES_MANAGED_19` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 19 |
| `ADDRESSES_MANAGED_20` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 20 |
| `ADDRESSES_MANAGED_22` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address managed 22 |
| `CENTRAL_AUTOMATION_MANAGED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Control unit automation managed |
| `CENTRAL_ANTINTRUSION_MANAGED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Control unit burglar alarm managed |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `2965`, `2968`, `2970`, `2972`, `2974`, `2976`, `2980` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4697`, `4698`, `4699`, `4700`, `4895`, `4896` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `90` / `modobj = 251` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`74`, `75`, `76`, `77`, `78`, `79`, `496`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

SCS/SCS interface used for physical or logical expansion, system-to-system interfacing, riser separation, galvanic separation and physical separation. The catalogue retains both wildcard firmware applicability and a concrete `6.0.0` firmware surface, with one Object difference between them.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The dedicated technical sheet documents `F422`, while current publisher compatibility documentation explicitly pairs Legrand `003562` with BTicino `F422`; commercial reconciliation is therefore established across both references.

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
