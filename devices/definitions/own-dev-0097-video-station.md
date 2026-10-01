# Video Station

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0097` | Project identity |
| Technical description | Video Station | Canonical catalogue |
| Commercial identities | `349320`, `349321` | Canonical commercial records |
| Catalogue item | `1078` | Canonical catalogue |
| Main catalogue system | Video door entry system | Canonical catalogue |
| Item model / `modobj` | `161` | Canonical inventory |
| Firmware definition | `6.0.1`; `3.0.5`; `5.0.7` | Canonical firmware catalogue |
| Declared Modules | `4` | Canonical firmware catalogue |
| Categories | Video door entry system, Video door entry | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `349320` | Established catalogue identity | canonical commercial record for item `1078` |
| BTicino - Axolute | `349321` | Established catalogue identity | canonical commercial record for item `1078` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Video Station` | canonical item description |
| Commercial variants represented | `2` | canonical commercial records |
| Declared Module count | `4` | canonical firmware catalogue |
| Programming / connectivity surface | USB | canonical inventory |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1078` | Canonical catalogue |
| Technical item | Video Station | Canonical catalogue |
| Main system | Video door entry system | Canonical catalogue |
| Item model / `modobj` | `161` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `6` | `0` | `1` | `4` | catalogue default | concrete catalogue applicability |
| `32` | `3` | `0` | `5` | `4` | non-default | concrete catalogue applicability |
| `33` | `5` | `0` | `7` | `4` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `31` | `2279` | `154` Internal Unit | catalogue firmware/Object relation |
| `31` | `2280` | `418` Open lock control | catalogue firmware/Object relation |
| `31` | `2281` | `422` Addressed autoswitch control | catalogue firmware/Object relation |
| `31` | `2282` | `429` Paging button | catalogue firmware/Object relation |
| `32` | `2287` | `154` Internal Unit | catalogue firmware/Object relation |
| `32` | `2288` | `418` Open lock control | catalogue firmware/Object relation |
| `32` | `2289` | `422` Addressed autoswitch control | catalogue firmware/Object relation |
| `32` | `2290` | `429` Paging button | catalogue firmware/Object relation |
| `33` | `2283` | `154` Internal Unit | catalogue firmware/Object relation |
| `33` | `2284` | `418` Open lock control | catalogue firmware/Object relation |
| `33` | `2285` | `422` Addressed autoswitch control | catalogue firmware/Object relation |
| `33` | `2286` | `429` Paging button | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `31` | Product Programming | supported configuration route for this Device family |
| `32` | Product Programming | supported configuration route for this Device family |
| `33` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `31` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `31` | `N_1` | catalogue-defined domain | catalogue-scoped | N |
| `31` | `N_2` | catalogue-defined domain | catalogue-scoped | N |
| `31` | `P` | catalogue-defined domain | catalogue-scoped | P |
| `31` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `32` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `32` | `N_1` | catalogue-defined domain | catalogue-scoped | N |
| `32` | `N_2` | catalogue-defined domain | catalogue-scoped | N |
| `32` | `P` | catalogue-defined domain | catalogue-scoped | P |
| `32` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `33` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `33` | `N_1` | catalogue-defined domain | catalogue-scoped | N |
| `33` | `N_2` | catalogue-defined domain | catalogue-scoped | N |
| `33` | `P` | catalogue-defined domain | catalogue-scoped | P |
| `33` | `M` | catalogue-defined domain | catalogue-scoped | M |

## Object configuration surfaces

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

### Object `418` - Open lock control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | External unit address |
| `SEG_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Level |

### Object `422` - Addressed autoswitch control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | External unit address |
| `SEG_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Segment |

### Object `429` - Paging button

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `AMPL_AREA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Amplifier area |
| `AMPL_UNIT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Amplifier unit |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `2004`, `2005`, `2006` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1078` / `modobj = 161` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`154`, `418`, `422`, `429`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Video Station. Its firmware exposes `4` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `349320`, `349321` to technical item `1078`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

## Evidence limits and open work

- Locate and archive dedicated publisher documentation for the exact commercial references where available.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
