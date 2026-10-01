# MyHOME_Screen 10

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0047` | Project identity |
| Technical description | MyHOME_Screen 10 | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH4892`, `MH4893`, `067267`, `067268` | Canonical commercial records |
| Catalogue item | `1768` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Firmware definition | `1.0.7`; `2.0.0`; `2.1.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Integration, Touchscreen, Video door entry, Multimedia | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH4892` | established catalogue identity for item `1768` | canonical commercial record |
| BTicino | `MH4893` | established catalogue identity for item `1768` | canonical commercial record |
| Legrand | `067267` | established catalogue identity for item `1768` | canonical commercial record |
| Legrand | `067268` | established catalogue identity for item `1768` | canonical commercial record |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00079AC_S_EN` | software manual | publisher copy | MyHOME_Screen10 and MyHOME_Screen10 C configuration, system functions and programming workflow | [Archived original](https://archive.openwebnet-ha.org/sha256/b9/ba/b9baa0fea2deb196253f415c47e6fd83f52d1a9728b5bfe99f69a20e0bc47340.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00079AC_S_EN.pdf) |
| BTicino `MH4892` catalogue page | product page | current catalogue | `MH4892` product characteristics and integration role | Not applicable - web page | [Official product page](https://catalogo.bticino.it/prodotto/soluzioni-per-la-smart-home/my-home---sistema-domotico/integrazione-e-controllo/BTI-MH4892-IT) |
| `MH4892` version history | firmware history | through 2015-03-26 in identified copy | Historical `MH4892` / `MH4893` / `067267` / `067268` firmware lineage | [Archived original](https://archive.openwebnet-ha.org/sha256/ea/4c/ea4c1d9873c01cb2868edc3930f6608a5821c00d6986025a74a5f220d09042ea.pdf) | [Official source](https://myhomeswupdate.bticino.com/VersionHistory/Version_History_MH4892_20150326.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `10 inch` 16:9 LCD touchscreen | Current `MH4892` / `MH4893` catalogue |
| Supply | `27 Vdc` | Current BTicino catalogue |
| Dimensions | `315 x 200 x 24 mm` | Current BTicino catalogue |
| Mounting | Wall mounted with `506E` flush-mounted box | Current BTicino catalogue |
| Managed functions | MyHOME, video door entry and multimedia functions with Ethernet/USB/SD/IP content support | Current catalogue and `RA00079AC_S_EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1768` | Canonical catalogue |
| Technical item | MyHOME_Screen 10 | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `109` | `1` | `0` | `7` | `1` | catalogue default | concrete catalogue applicability |
| `560` | `2` | `0` | `0` | `1` | non-default | concrete catalogue applicability |
| `696` | `2` | `1` | `0` | `1` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `109` | `1385` | `32` Colors Touch Screen | catalogue firmware/Object relation |
| `560` | `2345` | `32` Colors Touch Screen | catalogue firmware/Object relation |
| `696` | `2582` | `32` Colors Touch Screen | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `109` | Product Programming | supported configuration route for this Device family |
| `560` | Product Programming | supported configuration route for this Device family |
| `696` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `109` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `109` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `109` | `FW_VER` | catalogue-defined domain | catalogue-scoped | Firmware version |
| `109` | `SYSADDRESS` | catalogue-defined domain | catalogue-scoped | Univocal code |
| `560` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `560` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `560` | `FW_VER` | catalogue-defined domain | catalogue-scoped | Firmware version |
| `560` | `SYSADDRESS` | catalogue-defined domain | catalogue-scoped | Univocal code |
| `696` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `696` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `696` | `FW_VER` | catalogue-defined domain | catalogue-scoped | Firmware version |
| `696` | `SYSADDRESS` | catalogue-defined domain | catalogue-scoped | Univocal code |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `1768` / `modobj = 54` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Integrated MyHOME touchscreen for automation, lighting, temperature control, scenarios, energy, video door entry, sound and multimedia functions, configured through the product-programming workflow.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The software manual covers the MyHOME_Screen10 and capacitive successor together, while the canonical catalogue keeps item 1768 and item 1898 as distinct technical items. This page retains only item 1768 firmware and Object applicability.

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
