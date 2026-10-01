# Classe 300X

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0050` | Project identity |
| Technical description | Classe 300X | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `344742`, `344743`, `344745`, `344746` | Canonical commercial records |
| Catalogue item | `2321` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `140` | Canonical inventory |
| Firmware definition | `1.0.1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Video door entry, Wi-Fi, Indoor unit, Integration | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `344742` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344743` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344745` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344746` | established catalogue identity for item `2321` | canonical commercial record |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino `344742` product page | product page | current product family | Current Classe 300X connected indoor-unit functions and documentation links | Not applicable - web page | [Official product page](https://www.bticino.com/products/bt-344742) |
| `FIS_C300X_1` | technical data sheet | current publisher copy | `344742` / `344743` / `344745` / `344746` supply, Wi-Fi and teleloop electrical data | [Archived original](../../sources/devices/documents/device-doc-classe300x-fis-c300x-1/FIS_C300X_1.pdf) | [Official source](https://dar.bticino.it/asset/Documents/FIS_C300X_1.pdf) |
| `ST-00002362-EN` | technical sheet | current publisher copy | `344745` / `344746` connected video internal units with inductive loop | [Archived original](../../sources/devices/documents/device-doc-classe300x-st00002362-en/ST-00002362-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00002362-EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `7 inch` horizontal LCD touchscreen, `1024 x 600` | Current BTicino Classe 300X product documentation |
| SCS supply | `20..27 Vdc`; `22..27 Vdc` with active inductive loop | `FIS_C300X_1` |
| Wi-Fi | `2.4 GHz` and `5 GHz`; `802.11 b/g/n/ac/ax` in current product documentation | `FIS_C300X_1` |
| Variants | `344742` light, `344743` dark, `344745` light with teleloop, `344746` dark with teleloop | Current BTicino/Legrand product documentation |
| System role | Connected 2-wire hands-free video internal unit with remote/app functions | Current BTicino product page |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2321` | Canonical catalogue |
| Technical item | Classe 300X | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `140` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `892` | `1` | `0` | `1` | `2` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `892` | `4506` | `32` Colors Touch Screen | catalogue firmware/Object relation |
| `892` | `4507` | `154` Internal Unit | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `892` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `892` | `AID` | catalogue-defined domain | catalogue-scoped | ID |

## Object configuration surfaces

### Object `32` - Colors Touch Screen

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP address |
| `FW_VER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Firmware version |
| `SYSADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Univocal code |

### Object `154` - Internal Unit

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `N` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address |
| `P` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Associated external unit |
| `HAND_FREE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | HAND_FREE |
| `PRO_STUDIO` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Professional Studio |
| `DOOR_STATE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Door state display |
| `PEOPLE_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | PeopleSearching |
| `MENU_PRE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | MenuPreset |
| `RING_T_OUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | RingTimeOut |
| `CALL_T_OUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Call timeout |
| `PE_T_OUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | EUConnectionTimeOut |
| `PI_T_OUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | IUConnectionTimeOut |
| `TEL_T_OUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | TelConnectionTimeout |
| `ASS_SWITCH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | AssociatedSwitchboard |
| `BEEP` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | BEEP |
| `IS_SLAVE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Slave |
| `DOSA_CALL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Forward incoming call to ethernet |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `2321` / `modobj = 140` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`, `154`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Connected video-door-entry indoor unit with SCS/2-wire and network-facing functions. Canonical firmware/Object applicability on this page remains tied to the catalogue snapshot, not inferred from newer current-product firmware.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

Current publisher material confirms the four commercial references and differentiates the teleloop variants. Because current Classe 300X documentation postdates the canonical MyHOME Suite catalogue snapshot, current electrical/product facts are kept separate from the catalogue's firmware 1.0.1 and Object model.

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
