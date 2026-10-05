# Classe 300 V13E/V13M video internal unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0108` | Project identity |
| Technical description | Classe 300 V13E/V13M video internal unit | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `344612`, `344613`, `344622` | All three catalogue commercial records; confidence scoped below |
| Catalogue item | `2134` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration functions | Main system association |
| Item model / `modobj` | `69` | Main association; independent of project ID |
| Firmware definition | `671`, `727` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | User interfaces, Audio video | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `344612` | Established commercial variant | Catalogue record `2473`; published family/variant scope reconciled below |
| BTicino | `344613` | Established commercial variant | Catalogue record `2474`; published family/variant scope reconciled below |
| BTicino | `344622` | Established commercial variant | Catalogue record `2475`; published family/variant scope reconciled below |

The catalogue identifies `344612` as white V13E, `344613` as dark V13E, and `344622` as white V13M. Separate exact technical-sheet headers establish the V13E pair and V13M identity. Only V13M has the answering-machine video memory. No marketed wiring-device line is established; Classe 300 is a product family.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `344612` | `8005543535004` | [Archived original](https://archive.openwebnet-ha.org/sha256/9c/0e/9c0ed29efbcad6aa457848f07b5197cb5bd89297b68241c2874c9de462f863b9.pdf), `344612-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `344613` | `8005543535011` | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/e1/8be12fa4069ebde6d703e60b856356988cdea39fe224f07fae1f5f53b86c1591.pdf), `344613-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00861_b_EN.pdf` | V13E technical sheet | `BT00861-b-EN; 24/03/2016` | `344612`/`344613` only; specifications p. 1, physical/advanced setup p. 2, complete M mapping pp. 3-4, functions/capacities p. 5. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/03/8e/038e5ad019dd842a8c0d6421d5682c8bbb3e1a1edb2f4b64a4ef6d89484de048.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/BT00861_b_EN.pdf) |
| `BT00862_a_EN.pdf` | V13M technical sheet | `BT00862-a-EN; 23/02/2015` | `344622` only; specifications p. 1, setup p. 2, complete M mapping pp. 3-4, functions/memory p. 5. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/2e/5f/2e5fb4685b21de7f15cdcf3cd76dc60bd219be9cb134f9846ac0d8a48eb4ab33.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/BT00862_a_EN.pdf) |
| `RA00136AB_I_EN.pdf` | Classe 300 installation manual | `RA00136AB; revision from publisher filename; no publication date located` | Family installation, jumper and physical M matrices pp. 4-16; local/advanced configuration pp. 17-43; factory settings/capacities p. 44. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/3b/d1/3bd16910eb5df9682ba3bca7aa8bba550f6ea77bf265b339c57ba4ceba99aa29.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00136AB_I_EN.pdf) |
| `RA00136AC_U_EN.pdf` | Classe 300 user manual | `RA00136AC; revision from publisher filename; no publication date located` | Family operations pp. 4-36; settings pp. 37-48; induction loop, door status, Office and paging pp. 49-53. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/54/c1/54c1864c80b2e7d695048acfe0e03b6834c8cd4c266ff17e0c771f2fc8d22805.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00136AC_U_EN.pdf) |
| `LE07498AE.pdf` | Multilingual illustrated installation sheet | `LE07498AE; 04/16-01 PC` | `344612`/`344613`/`344622`; dimensions/heights/mounting PDF p. 1 (no printed number); interfaces pp. 2-4; configuration/matrices pp. 5-9; declarations pp. 10-12. Subsequent printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/74/cd/74cd8e15a7174e9cd62a2e56a5999449b972b0be331379b469c7b947fe1d049b.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/LE07498AE.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2134`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `344612-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `344612` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/9c/0e/9c0ed29efbcad6aa457848f07b5197cb5bd89297b68241c2874c9de462f863b9.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344612) |
| `344613-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `344613` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/e1/8be12fa4069ebde6d703e60b856356988cdea39fe224f07fae1f5f53b86c1591.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344613) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `18..27 Vdc` SCS BUS; extra `1-2` supply controlled by jumper `J1` | BT00861-b-EN / BT00862-a-EN p. 1-2 |
| Current | Standby `40 mA`; maximum `330 mA` | Both sheets p. 1 |
| Operating temperature | `5..40 °C` | Both sheets p. 1 |
| Metric dimensions by source | Sheets: `194 x 162 x 22 mm`; illustrated LE07498AE: `194 x 162 x 25 mm` | Both sheets p. 1; LE07498AE PDF p. 1; depth conflict unresolved |
| Display | `7 inch`, `16:9` colour LCD touch screen | Both sheets p. 1 |
| Mounting | Wall bracket supplied; table-top support `344632` with cable `336803` purchased separately | Both sheets p. 1 |
| Recommended heights | `160..165 cm`; wheelchair illustration `135..140 cm` | LE07498AE unnumbered / PDF p. 1 |
| Local controls | Capacitive entrance-panel/cycling, handsfree, Favorites and door-release keys; tactile guides | Both sheets p. 1 |
| Indication | Call green flashing, active speech green steady; key actuation red; unread notes red flashing, muted call red steady | Both sheets p. 1 |
| V13M additional LED | Answering machine active red steady; new recordings red flashing | BT00862-a-EN p. 1 |
| Rear interfaces | `J1`, `J2`, `N`, `P`, `M`; SCS and `1-2`; end-of-line switch; Mini-USB update; floor-call input; extra ringtone `1-5M` | Both sheets pp. 1-2 |
| Ringtone wiring | Additional ringtone terminals require point-to-point connections | Both sheets p. 1 |
| Accessibility | Inductive loop, hearing aid T setting; recommended user distance `25..35 cm`; metal/electronic noise can reduce coupling | Sheets p. 5; RA00136AC_U_EN p. 49 |
| Notes | Up to `20` audio and `50` text notes; oldest replaced at capacity | Both sheets p. 5; installer p. 44 |
| V13M videos | `25 x 15 s` high resolution or `150 x 15 s` low resolution; oldest overwritten at capacity | V13M sheet p. 5; installer p. 44 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2134` | Canonical catalogue |
| Technical item description | CLASSE300 V13E/M | Canonical catalogue |
| Item family | 0; key `20` | Canonical catalogue |
| Main system | Integration functions; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `69` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |
| Additional system | Video door entry; system key `4`, model `16` | Separate non-main association; inventory summary chooses this system, but main association is Integration functions/model `69` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `671` | `1` | `0` | `0` | `2` | Not catalogue default | Official |
| `727` | `2` | `0` | `0` | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `671` | `1` | `132` CLASSE300 V13E/M | Fixed/designated metadata | `2504` | `628` | `1154` |
| `671` | `2` | `154` Internal Unit | Fixed/designated metadata | `2507` | `154` | `1157` |
| `727` | `1` | `132` CLASSE300 V13E/M | Fixed/designated metadata | `2657` | `628` | `1267` |
| `727` | `2` | `154` Internal Unit | Fixed/designated metadata | `2658` | `154` | `1268` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `671` | Product Programming | `3` | Association key `4` |
| `727` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `671` | Ethernet over USB | `4` |
| `727` | Ethernet over USB | `4` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `671` | `1` | `0` | `2134_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `671` | `1` | `0` | `2134_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `727` | `1` | `0` | `2134_2.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `727` | `1` | `0` | `2134_2.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

Manufacturer physical N/P/M configuration cannot be changed through the menu. Advanced on-device configuration requires no configurators in N/P/M and exposes more custom functions. The catalogue Product Programming/Ethernet-over-USB association is distinct: the exact installer sheet calls the physical PC connection USB–Mini-USB for firmware update and requires the unit to be powered.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `671` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `671` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `671` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `671` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `727` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `727` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `727` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `727` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Published physical configurator meanings

| Physical setting | Published meaning | Evidence |
| --- | --- | --- |
| `N` | Internal-unit address; parallel units share N; maximum three in an apartment without `346850` | Both sheets p. 2 |
| `P` | Entrance panel activated first by auto-on and door lock released while idle | Both sheets p. 2 |
| `M` tens | Four quick-action preset selection; published matrices enumerate `1..9` | Sheets pp. 3-4; installer pp. 13-16 |
| `M` units | Favorites operation `0..9` | Sheets p. 3 |
| `J1` inserted / removed | Extra supply disabled / enabled | Both sheets p. 2 |
| `J2` inserted / removed | Master / Slave | Both sheets p. 2 |

### Favorites: complete M-unit mapping

| M unit | Favorites function | Evidence |
| --- | --- | --- |
| `0` | Staircase light | Both exact sheets p. 3 / PDF p. 3 |
| `1` | Door lock P+1 | Both exact sheets p. 3 / PDF p. 3 |
| `2` | Door lock P+2 | Both exact sheets p. 3 / PDF p. 3 |
| `3` | Door lock P+3 | Both exact sheets p. 3 / PDF p. 3 |
| `4` | Auto-on P+1 | Both exact sheets p. 3 / PDF p. 3 |
| `5` | Auto-on P+2 | Both exact sheets p. 3 / PDF p. 3 |
| `6` | Auto-on P+3 | Both exact sheets p. 3 / PDF p. 3 |
| `7` | General intercom | Both exact sheets p. 3 / PDF p. 3 |
| `8` | Internal intercom | Both exact sheets p. 3 / PDF p. 3 |
| `9` | Enable/disable Office | Both exact sheets p. 3 / PDF p. 3 |

### Quick actions: published M-tens presets

| M tens | Four configured actions / address semantics | Printed/PDF locator |
| --- | --- | --- |
| `1` | Internal intercom to all handsets sharing the same address; activation `P+1`; locks `P+1/P+2` | Sheets p. 4; installer p. 14 |
| `2` | General intercom to all handsets of the system; activation `P+1`; locks `P+1/P+2` | Sheets p. 4; installer p. 14 |
| `3` | Internal same-address intercom; reciprocal peer intercom `N1/N2`; activation `P+1`; lock `P+1` | Sheets p. 4; installer p. 14 |
| `4` | Two individual peer intercoms among `N1/N2/N3`, excluding caller; locks `P+1/P+2`. Peer scope is inside an apartment with `346850`, or among apartments without an interface | Sheets p. 4; installer pp. 13, 15 |
| `5` | Two individual peer intercoms among `N1/N2/N3`, excluding caller; locks `P+1/P+2`. Calls are among apartments with `346850` interfaces | Sheets p. 4; installer pp. 13, 15 |
| `6` | Four individual peer intercoms among `N1..N5`, excluding caller. Peer scope is inside an apartment with `346850`, or among apartments without an interface | Sheets p. 4; installer pp. 13, 15 |
| `7` | Four individual peer intercoms among `N1..N5`, excluding caller. Calls are among apartments with `346850` interfaces | Sheets p. 4; installer pp. 13, 16 |
| `8` | Activation `P+1`; reciprocal peer intercom `N1/N2`; locks `P+1/P+2` | Sheets p. 4; installer p. 16 |
| `9` | Four locks `P+1..P+4`, using `MOD=5` for the specified actuators | Sheets p. 4; installer p. 16 |

The published matrices enumerate presets `1..9`; a four-action mapping for tens `0` is not established here. The diagrams for presets `5/7` distinguish apartment-interface topology, not a group call or cyclic address sequence. For presets `4/5`, caller `N1` has peers `N2/N3`, caller `N2` has `N1/N3`, and caller `N3` has `N1/N2`. Presets `6/7` contain all four other addresses from `N1..N5`; these sets do not establish icon ordering. Use the original matrix to associate the displayed quick-action labels.

Door-lock actions use an associated entrance panel or `346200/346210` with `MOD=5`, or `346230`; direct activation uses entrance panel or actuator with `MOD=9`. Offset addresses do not expand the physical/configurable address domain.

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


### Object `132` - CLASSE300 V13E/M

Catalogue Object key `628` maps to external Object `132`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |

### Published UI/control capacities

| Surface | Published limit / constraint | Printed/PDF locator |
| --- | --- | --- |
| Configurable lists | `50` lock commands, `50` generic activations, `50` direct activations/entrance-panel auto-on, `40` internal and `40` external intercoms | Sheets p. 5; installer p. 44, list wording reconciled below |
| Home page | Up to four quick actions; physical mode limits choices to preset actions, though names/removal may change | Installer pp. 27-29, 42-44; user pp. 45-47 |
| Ringtones | `16` choices; main S0, secondary S1/S2/S3, internal/external intercom, floor call and switchboard notification | Sheets p. 5; installer p. 22 |
| Factory defaults | Beep off; Office off; background Home; installer password `12345`, five case-sensitive alphanumeric characters | Installer p. 44; published default, not a retained credential |
| Factory ringtones | S0=`2`; S1=`11`; S2=`5`; S3=`4`; floor=`7`; notification=`13`; internal intercom=`1`; external=`16` | Installer p. 44 |
| V13M factory memory | Enabled but inactive; high-resolution recordings selected | Installer p. 44 |
| Display | Background choice; five-position touch calibration; cleaning inhibits touch/keys `10 s` | Installer pp. 23-24; user pp. 41-42 |
| Advanced intercom types | Internal, external, paging, general; external/internal scope depends on apartment interfaces | Installer pp. 35-36 |
| Advanced cameras | Private, public, CCTV; without apartment interface cameras treated private; CCTV `3 min` view with no cycling, `347400` integration | Installer pp. 37-38 |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `671` | `154` | `2030` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |
| `727` | `154` | `2996` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `69` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Function | Applicability | Evidence / canonical reference |
| --- | --- | --- |
| Video entry | Answer, door release, auto-on/cameras, additional activations, intercom and switchboard communication | [`WHO 6`](../../functional/who-6-basic-video-door-entry/), [`WHO 7`](../../functional/who-7-multimedia-video/); all variants |
| Paging | Configured speech from the microphone into sound-system speakers | Exact sheets p. 5; external system required |
| Door status | Compatible actuator required; open lock red LED flashing, closed off; mutually exclusive with Office | Both sheets p. 5; user p. 50 |
| Office / Professional Studio | Installer-enabled option opens associated lock automatically on entrance-panel call; mutually exclusive with Door status | Both sheets p. 5; user p. 51 |
| Answering machine | Only `344622`; enable/disable, record/play/delete and quality/welcome settings | V13M sheet p. 5; installer pp. 25-26, 44; user pp. 6-8, 23-25, 43-44 |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Choose physical or advanced local setup. Wait for LEDs to stop flashing at first power-up, then set language/date/time and inspect the information page for N/P/M, master/slave, extra supply and actual firmware. Advanced configuration requires absent N/P/M configurators; physical presets cannot be rewritten from the menu. Secure the wall bracket on a flat surface without deformation, then slide the unit in without force.

Validate internal/entrance-panel addresses in the selected scope. Apartment-interface presence determines intercom/camera reach and general-call scope. Enable functions before assigning quick actions. Door status and Office cannot be enabled together. V13E lacks V13M video recording regardless of their shared catalogue Object model. Update through a powered USB–Mini-USB connection; Ethernet-over-USB is the catalogue connection label, not proof of an external RJ45 or Wi-Fi radio.

Reusable Object `154` includes N up to `3999`, P up to `95`, timeout and switchboard fields, while the printed physical configurators are two-digit sockets. Treat these as separate scopes until software and runtime evidence reconcile them. PEOPLE_S labels `1/2` are unknown in the source; do not supply meanings. The `DOSA_CALL` “forward incoming call to ethernet” field remains reusable catalogue capability, not proof of direct network hardware.

## Source reconciliation

Both exact sheets establish their own variant identities and agree on the common electrical/control facts. The shared installer and user revisions add complete configuration, capacities, defaults and operating constraints; their examples are not installed observations. LE07498AE adds installation details but disagrees on depth.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| System/model identity | Main Integration functions/model `69` coexists with video-door-entry model `16`; generated inventory summary uses the latter. Neither is the project Device ID | AS_ITEM_SYSTEM; inventory |
| Depth | Technical sheets `22 mm`; installation sheet `25 mm`, with no documented hardware/measurement explanation | Exact sheet p. 1; LE07498AE PDF p. 1 |
| Firmware defaults | Catalogue application tuples `1.0.0/2.0.0`, Object `132` FW_VER `1.0.0`, firmware-scoped FW_VER `3.0.0` and installer example `1.0.12` are distinct; no installed tuple inferred | Catalogue; installer p. 21 |
| Network fields | Firmware LAN_IP_ADDRESS/SYSADDRESS and Object `154` DOSA_CALL coexist with documented SCS and Mini-USB. These do not establish Wi-Fi, RJ45 or app forwarding | Catalogue; exact rear legends |
| Activation labels | Sheets say 50 direct auto-on to EP; installer says 50 direct activations and 50 locks/generic activations. Preserve the source terms without adding capacities together | Sheets p. 5; installer p. 44 |
| Variant memory | Only `344622` records video; common written/audio notes apply to family. Camera-page wording is not evidence of V13E video recording | Exact sheets; user |
| Unknown reusable labels | PEOPLE_S values `1/2` have question-mark labels; IS_SLAVE has no stored default; no guessed repair | Object `154` |

## Evidence limits and open work

- Resolve `22/25 mm` depth, software LAN/version metadata and physical/reusable address limits with exact hardware and parameter evidence.
- Obtain sanitized capture evidence for both firmware generations, two active Modules and the commercial variants; installed hardware and MCU are unknown.
- Confirm the reusable timeout units, PEOPLE_S labels, DOSA_CALL scope and accepted slave/default configuration.
- Exact revision scope is limited to the retained sheets/manuals; a tested newer user-manual URL was unavailable and is not treated as an incorporated revision.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- `344612-ean-product-sheet.pdf`, printed/PDF p. 1: exact `344612` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/9c/0e/9c0ed29efbcad6aa457848f07b5197cb5bd89297b68241c2874c9de462f863b9.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344612); SHA-256 `9c0ed29efbcad6aa457848f07b5197cb5bd89297b68241c2874c9de462f863b9`.
- `344613-ean-product-sheet.pdf`, printed/PDF p. 1: exact `344613` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/8b/e1/8be12fa4069ebde6d703e60b856356988cdea39fe224f07fae1f5f53b86c1591.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344613); SHA-256 `8be12fa4069ebde6d703e60b856356988cdea39fe224f07fae1f5f53b86c1591`.
