# Classe100 X12B energy-display video handset

## Summary

Classe100 X12B (344602) is a hands-free two-wire colour video handset with an induction loop and energy-consumption display. It provides door-release and video-entry controls, concierge messages and configurable ringing; its separate energy BUS connection adds MyHOME consumption visualisation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0196` | Project identity |
| Technical description | Classe100 X12B energy-display video handset | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `344602` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1872` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Video door entry system | Main system association |
| Item model / `modobj` | `172` | Main association; independent of project ID |
| Firmware definition | `546` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `344602` | Established catalogue identity | Manufacturer database commercial record `2165` explicitly links this SKU to item `1872` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` | Dutch video-entry design / installation guide | `Guide publication date unestablished; exact sheet BT00860-a-FR dated 01/12/2014` | Printed pp. 188-190 / PDF pp. 190-192: exact 344602 specifications, dual-BUS supply / draw, controls, physical modes, wiring and unresolved J1/J2 label. | [Archived original](https://archive.openwebnet-ha.org/sha256/09/83/0983cf9d7719af23c4cbe4c37e963337064c5e00dfe9752415c51d51f21636fe.pdf) | [Publisher original](https://assets.legrand.com/webf/nl/Document/nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1872`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Video-only SCS supply / draw | `18..27 Vdc; 14.5 mA standby / 260 mA maximum` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Video-plus-energy, MyHOME side draw | `18..27 Vdc; 3 mA standby / 18 mA maximum` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Video-plus-energy, video-entry side draw | `18..27 Vdc; 27 mA standby / 275 mA maximum` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Operating temperature | `5..40 °C` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Dimensions | `171 × 171 × 27 mm` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Display / ringing | `4.3-inch colour LCD, 16:9; 16 ringtones` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Mounting | `Wall bracket supplied; recessed/desk/handset/tilting accessories separately referenced` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Connections | `Video SCS; BUS ENERGY; floor-call input; extra bell 1-5M; handset connector; mini-USB for update` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Controls / indicators | `Audio, lock, entrance/camera, stair light and menu keys; call-exclusion, concierge-message, door and communication LEDs` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |
| Compatibility exclusion | `3522 pulse-counting interface` | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed p. 188 / PDF p. 190 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1872` | Canonical catalogue |
| Technical item description | CLASSE100 X12B | Canonical catalogue |
| Item family | No resolved family mapping; `EN_ITEM.id_family` is empty | Canonical catalogue |
| Main system | Video door entry system; key `4` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `172` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `546` | `1` | `0` | `1` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `546` | `1` | `154` Internal Unit | Fixed / designated metadata | `2508` | `154` | `1158` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `546` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `546` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `546` | `1` | `0` | `1872_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `546` | `1` | `0` | `1872_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| N | Internal-unit identity; parallel units share N; max 3 without 346850 in stated topology | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| P | Associated entrance panel for idle camera / lock operation | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| M units / tens | Video-entry key mode / MyHOME energy integration | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| M absent | Entrance / camera cycling, audio, associated lock, stair light | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| `M=1` | Fourth key activates P+1 lock or compatible actuator, source scope | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| `M=2` | Same-address internal call; audio, lock and stair light | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| `M=3` | Basic video / lock keys plus same-address intercom | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| `M=4` | Basic video / lock keys plus general intercom | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| Master / slave jumper | Text identifies J1 but explanatory fitted / removed lines name J2; unresolved label conflict | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |
| Termination / USB | `ON`/`OFF` end-of-line switch / firmware update; physical configuration only | `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` printed pp. 188-190 / PDF pp. 190-192 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `546` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `546` | `N` | `0..99` | `0` | Internal Unit address - units |
| `546` | `P` | `00..95` | `0` | Associated external unit |
| `546` | `M1` | `0..7` | `0` | Energy display basic mode for installation in France |
| `546` | `M2` | `0..4` | `0` | Video Door Entry Mode for 100X12B |

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

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `546` | `154` | `2031` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `172` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `154` - Internal Unit | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `154` - Internal Unit | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The exact historical handset sheet says physical configuration only (printed pp. 189-190 / PDF pp. 191-192). N identifies the internal unit; parallel handsets share N (maximum 3 without 346850 in the stated topology). P associates an entrance panel. M units choose video-key behavior, while M tens select MyHOME energy integration. Physical M absent/1/2/3/4 covers basic door / video, additional P+1 release, same-address intercom, combined basic / intercom and general intercom respectively. The jumper controls master / slave and the termination switch matches position on the line; mini-USB is documented for firmware updates.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact 344602 pages establish dual-BUS current figures and energy-display behavior, without substituting later connected Classe100 products. The sheet names the jumper J1 but its explanatory lines say J2 fitted / removed; this internal label conflict is preserved. No complete M-tens energy-mode matrix is present in the retained three-page sheet, so the catalogue’s software fields are not represented as a published physical map.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` | Printed pp. 188-190 / PDF pp. 190-192: exact 344602 specifications, dual-BUS supply / draw, controls, physical modes, wiring and unresolved J1/J2 label. |

## Evidence limits and open work

Applicable mounting accessory, full energy-mode configuration, jumper labelling on actual hardware, exact firmware update workflow and installed behavior remain to be corroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

### Retained original fingerprints

All incorporated originals were checked against the public archive by SHA-256 and byte length. Their manifest registrations were pushed on main before incorporation; previously registered originals were reused by fingerprint.

| Original | SHA-256 | Retention / size |
| --- | --- | --- |
| `nl_nl_deurcommunicatie_ontwerp_en_installatie_gids.pdf` | `0983cf9d7719af23c4cbe4c37e963337064c5e00dfe9752415c51d51f21636fe` | 52382107 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/09/83/0983cf9d7719af23c4cbe4c37e963337064c5e00dfe9752415c51d51f21636fe.pdf) |
