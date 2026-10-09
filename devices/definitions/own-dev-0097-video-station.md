# Video Station

## Summary

Video Station 349320 / 349321 is an 8-inch colour indoor video-entry unit with capacitive controls and stereo speakers. Its configurable menu can bring entry, scenarios, sound, temperature and alarm information together; physical menu presets and USB project programming have distinct limits.

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
| `349320-publisher-product-sheet.pdf` | product sheet | Publisher export retained 2026-10-03 | Whole exact 349320 export, PDF/printed p. 1; finish/series wording conflict retained | [Archived original](https://archive.openwebnet-ha.org/sha256/bf/6b/bf6b7ea64121d0ed81b8018492887103a77e2c17c0828138de2791e07f444cc8.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-349320) |
| `U2354B_U_UK.pdf` | technical / instruction manual | 09/09-01 PC | Entire substantive user guide, printed/PDF pp. 6–37; 349320–349321; front/closing leaves outside operating claims | [Archived original](https://archive.openwebnet-ha.org/sha256/8c/58/8c587b3f07620958efcca62e01a62f59c91d08484394754aae9f92d109658b62.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/U2354B_U_UK.pdf) |
| `U2354B_I_UK.pdf` | Installer manual · EN | 09/09-01PC | Entire substantive chapters, printed/PDF pp. 4–24; cover identifies 349320–349321; contents/front and closing leaves provide no additional operating claims | [Archived original](https://archive.openwebnet-ha.org/sha256/eb/4c/eb4c7fcd572d3fed2478cdaabf67beb79fe0ef4b300e7148c3bc8ecbb3417e37.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2354B_I_UK.pdf) |
| `U2354B_S_UK.pdf` | Software manual · EN | 09/09-01PC | Entire substantive chapters, printed/PDF pp. 4–28; connection, .jtv projects, import losses, menus, .fwz update and 10-second .jtr sounds | [Archived original](https://archive.openwebnet-ha.org/sha256/9c/65/9c659e49fa522eb13a0bfefae73f7d35577a9e212f1999c2068ef401dc2a4a65.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2354B_S_UK.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display / controls | `8 inch` colour LCD, blue-lit capacitive navigation and six entry/control keys; stereo speakers | U2354B_I_UK, printed/PDF pp. 6–8; exact family guide |
| Supply / consumption / temperature | SCS `18..28 V`; maximum `600 mA` when no audio signal; `0..40 °C` | Installer appendix, p. 24; stated maximum condition retained |
| Mounting / dimensions | Metal wall base and supplied bracket; export H×W×D `305×230×25 mm` | Installer pp. 8–9; 349320 export p. 1; export axis labels preserved |
| Rear connectors / controls | Configurator socket, miniUSB, extra-supply connector, 2-wire BUS and line-termination ON/OFF microswitch | Installer p. 8; no Ethernet connector documented |
| Multimedia supply | Local supply required with multimedia interface 3465; local amplifier also requires local supply | Exact export; user manual audio chapters |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1078` | Canonical catalogue |
| Technical item | Video Station | Canonical catalogue |
| Main system | Video door entry system | Canonical catalogue |
| Item model / `modobj` | `161` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Video door entry system | `161` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `1078` | `349320` | `1` | `2` | `Nighter` |
| `1965` | `349321` | `1` | `2` | `Whice` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `1078` | `1` | `0` | `0` | Empty in source |
| `1965` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `6` | `0` | `1` | `4` | Catalogue default | Official |
| `32` | `3` | `0` | `5` | `4` | Not catalogue default | Official |
| `33` | `5` | `0` | `7` | `4` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `31` | `65` | BTicino (key `1`) | `3` | external software | `TiAxoluteNighterAndWhiceStation_0600` |
| `32` | `117` | BTicino (key `1`) | `3` | external software | `TiAxoluteNighterAndWhiceStation_0300` |
| `33` | `118` | BTicino (key `1`) | `3` | external software | `TiAxoluteNighterAndWhiceStation_0500` |

All 3 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

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

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `31` | Product Programming | `3` | Canonical firmware/mode association |
| `32` | Product Programming | `3` | Canonical firmware/mode association |
| `33` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `31` | USB | Canonical firmware/connection association |
| `32` | USB | Canonical firmware/connection association |
| `33` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

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

### Device-specific interpretation

Official firmware `31`=6.0.1 (default), 32=3.0.5 and 33=5.0.7 each declare four logical Modules: 154 Internal Unit, 418 Open lock, 422 Addressed autoswitch and 429 Paging. There are no Virgin, slot-condition or conversion rows. Each build has Product Programming mode 3, USB connection 3 and a distinct parameter association 65/117/118 (brand 1, line 3). Firmware N_1/N_2/P=`0..9` and M=`0..6`, default 0, are narrower than reusable N=`0..3999` and `P=0..95`. Internal-unit HAND_FREE/PRO_STUDIO/DOOR_STATE are booleans default 0; PEOPLE_S retains its literal unknown/question-mark labels. RING/CALL/PE/PI/TEL timeouts have their distinct stored ranges/defaults, not inferred call durations. IS_SLAVE has no stored default. DOSA_CALL is 0 Enable / 1 Disable, default 0; filters 2004/2006/2005 retain the full boolean range and do not prove an Ethernet port. Paging `M=1` Base/2 Advanced default 2, AMPL_AREA=`0..99`, AMPL_UNIT=`0..39` and `ADDR_TYPE=0` General/1 Ambient/2 Point default 0 remain separate from physical M=`0..6` menu layouts. SEG_LEV=`0..3` applies to reusable open-lock and autoswitch surfaces. The broader manufacturer menu capabilities do not create additional catalogue Modules.

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

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Entry controls | Door release, stairs, auto-switch/camera, connection/paging, mute and call exclusion; hold Push-to-Talk at least 2 s to talk, release to hear | Installer pp. 6–7; user pp. 7–11 |
| Menu / capacity | Five customizable first-page functions plus fixed Settings; two levels; at least one function. Up to 30 total scenario/communication entries; six subpage entries | Installer pp. 10–15; software pp. 18–21 |
| Camera cycle | 10 seconds per camera, then off after one cycle; call interrupts and occupied channel rejects switching | User p. 18; not a protocol timeout inferred from schema |
| Sound / temperature | Four audio sources and six room/amplifier entries; single/multichannel source selection, volume; thermostat central/zone manual, automatic/program, protection and OFF | Software pp. 21–23; user pp. 29–34; PC/system and local-power conditions apply |
| Alarms / messages | Last three alarms; displayed zones `1..8`, zone 0 not displayed; alarm memory clears on arming; switchboard messages depend on system | User pp. 27–28, 37; UI scope, not every central unit’s zone capacity |
| Technical alarm channels | 1 gas, 2 freezer, 3 flood, 4 emergency, 5/6/7 generic, 8 fire, 9 remote assistance | User p. 28 |
| Automatic answering / lock | Handsfree automatically answers; Professional Studio automatically releases the lock on a call and is mutually exclusive with Door State; Door State requires supporting system | User pp. 35–36 |
| Cleaning / ringing | Cleaning mode suppresses key commands for 20 seconds; 16 preset melodies and PC-created custom ringtone transfer | User pp. 13–15; software pp. 24–28 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

### Physical menu presets

U2354B_I_UK, printed/PDF pp. 10–12, uses N/P/M configurators. Physically configured menus cannot be edited; systems with 346850 require advanced configuration. M=`0..6` defines the following five functions plus Settings (matrix visually checked). Camera/activation examples use P plus icon index; intercom numbers use the displayed N index.

| M | Documented preset functions |
| --- | --- |
| 0 | Intercom 1, 2, 3, 4, 5 |
| 1 | Camera 1, 2, 3, 4; camera cycle |
| 2 | Activation 1; intercom 1, 2; camera 1; camera cycle |
| 3 | Camera 1; intercom 1, 2; activation 1; camera cycle |
| 4 | Camera 1, 2; intercom 1; activation 1, 2 |
| 5 | Activation 1, 2, 3; camera 1; intercom 1 |
| 6 | Intercom 1, 2, 3; activation 1; camera 1 |

### USB projects, updates and sound files

Installer pp. 13–16 and U2354B_S_UK pp. 4–28 describe TiAxoluteNighterAndWhiceStation: create/open/edit/save a .jtv project, receive a backup from the Device, then send a project through USB-miniUSB. The Device must be BUS-powered; the installer also requires it not be physically configured. The software connection chapter omits that second condition, so the stricter installer scope is retained. Importing a TiAxoluteDisplay project removes unsupported fields and highlights them: inspect those losses before transfer. Connection/port selection and successful transfer confirmation are distinct from observed installed behavior.

Firmware updates select .fwz files, show version differences with Info and transfer to the connected Device; no package contents or applicability to each recorded build was examined. Custom ringtones use a selected 10-second audio segment, saved as .jtr or sent to the Device. These are file/workflow descriptions, not firmware version guarantees.

### Local settings and recovery

Installer pp. 17–21 covers language/first-start confirmation, N/P changes and services. SLAVE allows at most three units with the same N (one master plus two slaves); MASTER_CLOCK supplies periodic time synchronization; PAGING enables paging. The source factory defaults are No for these services. Its Reset menu cancels all data and returns factory settings after confirmation; this is more than setting those three service options to No. User pp. 13–15 covers volume/display/melody adjustment; user p. 20 adds room-specific amplifier configuration constraints.

## Source reconciliation

The three U2354B manuals explicitly cover both 349320 and 349321 and share 09/09-01PC. The retained 349320 export describes Whice finish but identifies its series as Axolute Nighter. This is a source wording conflict, not grounds to swap SKUs. The software contents page has inconsistent chapter locators; actual printed/PDF chapters are used. User p. 35 repeats a door-lock-LED description for Handsfree; that ambiguous indicator wording is not generalized. Catalogue DOSA_CALL and telephone fields do not prove Ethernet/telephone hardware ports.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- Exact finish wording, firmware-specific feature applicability and ambiguous Handsfree indicator wording remain source-scoped.
- Parameter payloads 65/117/118, .fwz files, linked technical-sheet revisions and installed behavior remain unexamined. The full substantive installer/user/software chapters were inspected; unrelated services outside the configured system are not promised.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0097)
