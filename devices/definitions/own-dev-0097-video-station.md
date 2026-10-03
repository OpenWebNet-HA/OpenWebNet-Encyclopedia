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
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `349320-publisher-product-sheet.pdf` | product sheet | Publisher export retained 2026-10-03 | Whole product document, PDF pp. 1-1; printed p. 1 for one-page catalogue exports | [Archived original](https://archive.openwebnet-ha.org/sha256/bf/6b/bf6b7ea64121d0ed81b8018492887103a77e2c17c0828138de2791e07f444cc8.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-349320) |
| `U2354B_U_UK.pdf` | technical / instruction manual | 09/09-01 PC | Whole product document, PDF pp. 1-38; printed p. 1 for one-page catalogue exports | [Archived original](https://archive.openwebnet-ha.org/sha256/8c/58/8c587b3f07620958efcca62e01a62f59c91d08484394754aae9f92d109658b62.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/U2354B_U_UK.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Programming / connectivity surface | USB | canonical inventory |
| Display / interface | `8 inch` colour display; backlit capacitive controls | 349320 publisher export; retained family user guide |
| Mounting | Wall bracket | 349320 publisher export |
| USB interface | Programming / firmware update | Same source |
| Local supply condition | Required when used with multimedia interface `3465` | Same source |
| Overall dimensions | `305 x 230 x 25 mm` | 349320 publisher export, PDF p. 1; height x width x depth |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1078` | Canonical catalogue |
| Technical item | Video Station | Canonical catalogue |
| Main system | Video door entry system | Canonical catalogue |
| Item model / `modobj` | `161` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `6` | `0` | `1` | `4` | Catalogue default | Official |
| `32` | `3` | `0` | `5` | `4` | Not catalogue default | Official |
| `33` | `5` | `0` | `7` | `4` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `1` | `154` Internal Unit | Fixed/designated metadata | `2279` | `154` | `957` |
| `31` | `2` | `418` Open lock control | Fixed/designated metadata | `2280` | `418` | `958` |
| `31` | `3` | `422` Addressed autoswitch control | Fixed/designated metadata | `2281` | `422` | `959` |
| `31` | `4` | `429` Paging button | Fixed/designated metadata | `2282` | `429` | `960` |
| `32` | `1` | `154` Internal Unit | Fixed/designated metadata | `2287` | `154` | `965` |
| `32` | `2` | `418` Open lock control | Fixed/designated metadata | `2288` | `418` | `966` |
| `32` | `3` | `422` Addressed autoswitch control | Fixed/designated metadata | `2289` | `422` | `967` |
| `32` | `4` | `429` Paging button | Fixed/designated metadata | `2290` | `429` | `968` |
| `33` | `1` | `154` Internal Unit | Fixed/designated metadata | `2283` | `154` | `961` |
| `33` | `2` | `418` Open lock control | Fixed/designated metadata | `2284` | `418` | `962` |
| `33` | `3` | `422` Addressed autoswitch control | Fixed/designated metadata | `2285` | `422` | `963` |
| `33` | `4` | `429` Paging button | Fixed/designated metadata | `2286` | `429` | `964` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `31` | Product Programming | supported configuration route for this Device family |
| `32` | Product Programming | supported configuration route for this Device family |
| `33` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `31` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `31` | `N_1` | `0..9` | `0` | N; Configurator N(0-9) |
| `31` | `N_2` | `0..9` | `0` | N; Device Number 0-9 |
| `31` | `P` | `0..9` | `0` | P; Configurator P |
| `31` | `M` | `0..6` | `0` | M; (0-6) |
| `32` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `32` | `N_1` | `0..9` | `0` | N; Configurator N(0-9) |
| `32` | `N_2` | `0..9` | `0` | N; Device Number 0-9 |
| `32` | `P` | `0..9` | `0` | P; Configurator P |
| `32` | `M` | `0..6` | `0` | M; (0-6) |
| `33` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `33` | `N_1` | `0..9` | `0` | N; Configurator N(0-9) |
| `33` | `N_2` | `0..9` | `0` | N; Device Number 0-9 |
| `33` | `P` | `0..9` | `0` | P; Configurator P |
| `33` | `M` | `0..6` | `0` | M; (0-6) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `154` - Internal Unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N` | `0..3999` | `0` | Address |
| `P` | `0..95` | `0` | Associated external unit |
| `HAND_FREE` | `0` = Disable; `1` = Enable | `0` | HAND_FREE |
| `PRO_STUDIO` | `0` = Disable; `1` = Enable | `0` | Professional Studio |
| `DOOR_STATE` | `0` = Disable; `1` = Enable | `0` | Door state display |
| `PEOPLE_S` | `0` = No; `1` = ?; `2` = ? | `0` | PeopleSearching |
| `MENU_PRE` | `0..99` | `0` | MenuPreset |
| `RING_T_OUT` | `1..30` | `10` | RingTimeOut |
| `CALL_T_OUT` | `10..180` | `30` | Call timeout |
| `PE_T_OUT` | `3..90` | `6` | EUConnectionTimeOut |
| `PI_T_OUT` | `3..90` | `18` | IUConnectionTimeOut |
| `TEL_T_OUT` | `3..180` | `90` | TelConnectionTimeout |
| `ASS_SWITCH` | `0..95` | `0` | AssociatedSwitchboard |
| `BEEP` | `0` = Disable; `1` = Enable | `0` | BEEP |
| `IS_SLAVE` | `0` = Not slave; `1` = Slave | Not specified in source | Slave |
| `DOSA_CALL` | `0` = Enable; `1` = Disable | `0` | Forward incoming call to ethernet |


### Object `418` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |


### Object `422` - Addressed autoswitch control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


### Object `429` - Paging button

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Base; `2` = Advanced | `2` | Modality; mode(Base,Advanced) |
| `AMPL_AREA` | `0..99` | `0` | Amplifier area |
| `AMPL_UNIT` | `0..39` | `0` | Amplifier unit |
| `ADDR_TYPE` | `0` = General; `1` = Ambient; `2` = Point to point | `0` | Addressing type |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `154` | `2004` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |
| `32` | `154` | `2006` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |
| `33` | `154` | `2005` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1078` / `modobj = 161` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`154`, `418`, `422`, `429`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `154` Internal Unit | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |
| `418` Open lock control | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `418` Open lock control | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `418` Open lock control | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |
| `418` Open lock control | Sound system | Firmware/Object capability association; resolve the slot and configuration first |
| `422` Addressed autoswitch control | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `422` Addressed autoswitch control | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |
| `422` Addressed autoswitch control | Sound system | Firmware/Object capability association; resolve the slot and configuration first |
| `429` Paging button | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `429` Paging button | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |
| `429` Paging button | Sound system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Product Programming for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has 4 declared Modules; retain the individual Module placements when preparing a project.

The retained sources establish only the Device-specific procedures described below; reset, transfer or update details not covered by those sources remain open work. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

The publisher sheet documents physical configurators or TiNighterandWhiceStation project programming, with USB used for programming and firmware update. Keep those product paths separate from runtime functional commands and retain the local-supply condition when the multimedia `3465` interface is used.

## Source reconciliation

The retained `U2354B_U_UK` user manual explicitly covers `349320` and `349321` as Nighter & Whice. The current `349320` publisher export instead calls its finish Whice, while the retained residential catalogue places `349320` under Nighter and `349321` under Whice. This naming conflict remains source-scoped; it does not justify swapping commercial references. The product sources support the display, controls, USB/project programming and multimedia-supply condition recorded above.

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
