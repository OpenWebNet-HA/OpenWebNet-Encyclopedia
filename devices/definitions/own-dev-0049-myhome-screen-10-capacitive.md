# MyHOME_Screen 10 Capacitive

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0049` | Project identity |
| Technical description | MyHOME_Screen 10 Capacitive | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH4892C`, `MH4893C`, `067228`, `067219` | Canonical commercial records |
| Catalogue item | `1898` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Firmware definition | `2.0.0`; `2.1.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Integration, Touchscreen, Video door entry, Multimedia | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino MyHOME | `MH4892C` | established catalogue identity for item `1898` | canonical commercial record |
| BTicino MyHOME | `MH4893C` | established catalogue identity for item `1898` | canonical commercial record |
| Legrand MyHOME | `067228` | established catalogue identity for item `1898` | canonical commercial record |
| Legrand MyHOME | `067219` | established catalogue identity for item `1898` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| RA00079AC_S_EN | software manual | publisher copy | MyHOME_Screen10 and MyHOME_Screen10 C configuration, system functions and programming workflow | - | https://dar.bticino.com/asset/Documents/RA00079AC_S_EN.pdf |
| BTicino MH4892C catalogue page | product page | current catalogue | MH4892C product characteristics and capacitive-screen variant | - | https://catalogue.bticino.com/product/smart-home-solutions/my-home---home-automation-system/integration-and-control/BTI-MH4892C-EN |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | 10 inch 16:9 capacitive touchscreen | Current MH4892C catalogue |
| Supply | 27 Vdc | Current BTicino catalogue |
| Dimensions | 315 x 200 x 24 mm | Current BTicino catalogue |
| Mounting | Wall mounted with 506E flush-mounted box | Current BTicino catalogue |
| Managed functions | MyHOME, video door entry and multimedia functions with room navigation and profile customization | Current catalogue / RA00079AC_S_EN |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1898` | Canonical catalogue |
| Technical item | MyHOME_Screen 10 Capacitive | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `558` | `2` | `0` | `0` | `1` | non-default | concrete catalogue applicability |
| `697` | `2` | `1` | `0` | `1` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `558` | `2431` | `32` Colors Touch Screen | catalogue firmware/Object relation |
| `697` | `2583` | `32` Colors Touch Screen | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `558` | Product Programming | supported configuration route for this Device family |
| `697` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `558` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `558` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `558` | `FW_VER` | catalogue-defined domain | catalogue-scoped | Firmware version |
| `558` | `SYSADDRESS` | catalogue-defined domain | catalogue-scoped | Univocal code |
| `697` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `697` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `697` | `FW_VER` | catalogue-defined domain | catalogue-scoped | Firmware version |
| `697` | `SYSADDRESS` | catalogue-defined domain | catalogue-scoped | Univocal code |

## Object configuration surfaces

### Object `32` - Colors Touch Screen

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP address |
| `FW_VER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Firmware version |
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
| `DIMENSION 1` | corroborate technical identity for catalogue item `1898` / `modobj = 55` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Capacitive MyHOME touchscreen for integrated automation, video door entry and multimedia functions, programmed through MyHOME Suite/product programming.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The shared software manual intentionally covers both resistive and capacitive MyHOME_Screen10 families. The catalogue distinguishes this capacitive family as item 1898 with firmware 2.0.0 and 2.1.0.

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
