# Easy Kit Home + Security connected internal unit

## Summary

This cluster groups two white 7-inch Easy Kit Wi-Fi additional monitors, BTicino 335254 and Legrand 365225. They answer video-entry calls and control doors, gates, lighting and cameras, with Home + Security smartphone access. Their exact instructions name different compatible kit families, so their expansion requirements remain variant-specific.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0160` | Project identity |
| Technical description | Easy Kit Home + Security connected internal unit | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `335254`, `365225` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2301` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Video door entry system | Main system association |
| Item model / `modobj` | `101` | Main association; independent of project ID |
| Firmware definition | `860`, `916` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `335254` | Established catalogue identity | Manufacturer database commercial record `2655` explicitly links this SKU to item `2301` |
| Legrand | `365225` | Established catalogue identity | Manufacturer database commercial record `2656` explicitly links this SKU to item `2301` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `335254` | `8005543740835` | [335254-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/0c/42/0c42292e249e0d7909cf346c6271b4cc302ef389d6aefb62bc12a90881d061ca.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `335254` | Easy Kit Connnected with H+S | Canonical commercial record `2655` |
| `365225` | Easy Kit Connnected with H+S | Canonical commercial record `2656` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE14222AC.pdf` | Instruction Use `LE14222AC` | `LE14222AC`;05/24-01PC | English sections PDF pp. 1–6 examined: exact 335254 dimensions, keys, wiring, all three compatible-kit groups and technical data; p. 6 inspected visually; other translations unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/9c/6f/9c6fe4b25ed0773462e4f37b146db54f720c9bc84f4a7072c015ec64415359c7.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE14222AC.pdf) |
| `335254-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes | [Archived original](https://archive.openwebnet-ha.org/sha256/0c/42/0c42292e249e0d7909cf346c6271b4cc302ef389d6aefb62bc12a90881d061ca.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-335254&include_technical=1) |
| `LE14226AB.pdf` | Exact-product manufacturer variant/revision documentation | `LE14226AB; 09/23-01 PC` | English sections PDF pp. 1–7 examined: exact 365225 dimensions, controls, wiring, compatible kits, app and technical data; French/internal-unit wording conflict p. 6 retained; remaining translations unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/29/30/29306e6c22c7168c71b6dbc165975dc090ecb9680b194a54c1d0aed71d82e8f7.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE14226AB.pdf) |
| `EASYKIT_CONNECTED_README.pdf` | Software EASYKIT_CONNECTED_README | `30TH May, 2025; printed date` | PDF p. 1: entire30May 2025 Netatmo-family exact-reference list and software environment | [Archived original](https://archive.openwebnet-ha.org/sha256/d3/56/d3566257c4b717cdaed35b56ae4a7af8f28b182e0af37482c78c459bbe47c541.pdf) | [Publisher original](https://assets.legrand.com/pim/AUTRE/EASYKIT_CONNECTED_README.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2301`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| 335254 display | `7-inch, 16:9; touch control keys, not a touch-screen display` | `LE14222 AC` p. 3 |
| 335254 supply marking | `30 Vdc / 30 W in instruction; export nominal 30 V, current range 0..1 A` | `LE14222 AC` p. 6 |
| 335254 standby draw | `10 mA in publisher export` | `335254-publisher-product-sheet.pdf` pp. 2–3 |
| 335254 temperature | `operating 5..40 °C; storage -10..70 °C, export` | `LE14222 AC` p. 6; exact export p. 2 |
| 335254 dimensions | `215 x 142.5 x 22.3 mm in instruction; export height 140 mm` | `LE14222 AC` p. 1; exact export p. 2 |
| 335254 protection | `IP30 in publisher export` | `335254-publisher-product-sheet.pdf` pp. 2–3 |
| 335254 wireless | `IEEE 802.11 b/g/n; 2.4..2.4835 GHz; <20 dBm; WEP/WPA/WPA2` | `LE14222 AC` p. 6 |
| 335254 connectors | `D1/D2 upstream; R1/R2 additional monitor; mini-USB for firmware update` | `LE14222 AC` p. 4 |
| Role switches | `family 1/family 2; Master/Slave` | `LE14222 AC` p. 4 |
| 335254 export expansion | `maximum two additional screens; maximum internal/external distance 100 m, topology-specific` | `335254-publisher-product-sheet.pdf` pp. 2–3 |
| 365225 dimensions | `215 x 142.5 x 22.3 mm` | `LE14226AB` p. 1 |
| 365225 supply / temperature | `30 Vdc / 30 W marking; 5..40 °C` | `LE14226AB` p. 7 |
| 365225 wireless | `IEEE 802.11 b/g/n; 2.4..2.4835 GHz; <20 dBm; WEP/WPA/WPA2` | `LE14226AB` p. 7 |
| 365225 maximum terminal section | `2 x 1 mm²` | `LE14226AB` p. 7 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Classification frequency values of zero are separate from explicitly documented Wi-Fi carriers; a negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| With video | `Yes` | `LE14222 AC` p. 3 |
| Installation technique | `Bus system` | `LE14222 AC` p. 3 |
| Mounting method | `Surface mounted` | `LE14222 AC` p. 3 |
| Material | `Plastic` | `LE14222 AC` p. 3 |
| Picture system | `PAL` | `LE14222 AC` p. 3 |
| Property picture system | `Colour` | `335254-publisher-product-sheet.pdf` PDF p. 2 |
| With memory function | `No` | `LE14222 AC` p. 3 |
| Overhear protected | `No` | `LE14222 AC` p. 3 |
| Operation door lock | `Yes` | `LE14222 AC` p. 3 |
| Control extra function(s) | `Yes` | `LE14222 AC` p. 3 |
| Hands free | `Yes` | `LE14222 AC` p. 3 |
| Function lamps | `Yes` | `LE14222 AC` p. 3 |
| Can be connected to smartphone | `Yes` | `LE14222 AC` p. 3 |
| Zoom, pan/tilt function | `No` | `LE14222 AC` p. 3 |
| Screen diagonal | `177.8 mm` | `LE14222 AC` p. 3 |
| Screen diagonal (inch) | `7 inch` | `LE14222 AC` p. 3 |
| Hearing aid compatible | `No` | `LE14222 AC` p. 3 |
| With automatic door opener | `Yes` | `LE14222 AC` p. 3 |
| Colour | `White` | `LE14222 AC` p. 3 |
| Type of interface | `Wi-Fi` | `LE14222 AC` p. 3 |
| Mutable call tone | `Yes` | `LE14222 AC` p. 3 |
| Internal communication | `Yes` | `LE14222 AC` p. 3 |
| Specific call tone | `Yes` | `LE14222 AC` p. 3 |
| Additional device connectable | `Yes` | `LE14222 AC` p. 3 |
| Loudness setting | `Yes` | `LE14222 AC` p. 3 |
| With touch screen | `No` | `LE14222 AC` p. 3 |
| Width | `215 mm` | `LE14222 AC` p. 3 |
| Height | `140 mm` | `LE14222 AC` p. 3 |
| Depth | `22.3 mm` | `LE14222 AC` p. 3 |
| Compatible with Apple HomeKit | `No` | `LE14222 AC` p. 3 |
| Compatible with Google Assistant | `No` | `LE14222 AC` p. 3 |
| Compatible with Amazon Alexa | `No` | `LE14222 AC` p. 3 |
| IFTTT support available | `No` | `LE14222 AC` p. 3 |
| degree of impact strength (IK) | `Not applicable` | `LE14222 AC` p. 3 |
| Degree of protection (IP) | `IP30` | `335254-publisher-product-sheet.pdf` pp. 2–3 |
| Operating / setting temperature (Min-Max) | `5-40 °C` | `LE14222 AC` p. 6; exact export p. 2 |
| Storage temperature (Min-Max) | `-10-70 °C` | `LE14222 AC` p. 6; exact export p. 2 |
| Voltage type | `DC` | `LE14222 AC` p. 3 |
| Nominal voltage (Min-Max) | `30-30 V` | `LE14222 AC` p. 3 |
| Supply current (Min-Max) | `0-1 A` | `LE14222 AC` p. 3 |
| Frequency (Min-Max) | `0-0 Hz` | `LE14222 AC` p. 3 |
| Sound level | `82 dB` | `LE14222 AC` p. 3 |
| Standby consumption | `10 mA` | `LE14222 AC` p. 3 |
| Antimicrobial treatment | `No` | `LE14222 AC` p. 3 |
| Cable nature for connection | `Flexible or rigid` | `LE14222 AC` p. 3 |
| Cable section (Min-Max) | `0.1-2.5 mm²` | `LE14222 AC` p. 3 |
| Label space/information surface | `No` | `LE14222 AC` p. 3 |
| Fitted with USB plug | `Yes` | `LE14222 AC` p. 3 |
| Fitted with rainproof plate protection | `No` | `335254-publisher-product-sheet.pdf` pp. 2–3 |
| With complemantary luminous signal | `Yes` | `LE14222 AC` p. 3 |
| Vertical fixing center distance (Min-Max) | `25-85 mm` | `LE14222 AC` p. 3 |
| Horizontal fixing center distance (Min-Max) | `35-110 mm` | `LE14222 AC` p. 3 |
| Control mode | `Wireless` | `LE14222 AC` p. 3 |
| Contains Batteries | `No` | `LE14222 AC` p. 3 |
| Additional unit | `Yes` | `LE14222 AC` p. 3 |
| Maximum number of additional screens | `2` | `LE14222 AC` p. 3 |
| Addressable | `Yes` | `LE14222 AC` p. 3 |
| Door entry system with mobile application | `Yes` | `LE14222 AC` p. 3 |
| Number of ringtones | `20` | `LE14222 AC` p. 3 |
| Remote opening of gate / Electric door opener | `Yes` | `LE14222 AC` p. 3 |
| Screen resolution | `Other` | `LE14222 AC` p. 3 |
| Screen brightness setting | `Yes` | `LE14222 AC` p. 3 |
| Screen contrast setting | `Yes` | `LE14222 AC` p. 3 |
| Memory video function | `No` | `LE14222 AC` p. 3 |
| Max distance between internal and external unit | `100 m` | `LE14222 AC` p. 3 |
| Connected object | `Yes` | `LE14222 AC` p. 3 |
| Application store for download | `App Store, Google Play Store` | `LE14222 AC` p. 3 |
| Programming way | `Smartphone apps` | `LE14222 AC` p. 3 |
| With voice command | `No` | `LE14222 AC` p. 3 |
| Programmable | `No` | `LE14222 AC` p. 3 |
| Connectable by Internet box | `Yes` | `LE14222 AC` p. 3 |
| Product use function | `Door entry systems` | `LE14222 AC` p. 3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2301` | Canonical catalogue |
| Technical item description | Easy Kit Connnected with H+S | Canonical catalogue |
| Item family | 0; key `20` | Canonical catalogue |
| Main system | Video door entry system; key `4` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `101` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Video door entry system | `101` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Multimedia | private riser | Canonical item/bus relationship |
| Video door entry system 8 wires | private riser | Canonical item/bus relationship |
| Video door entry system 8 wires | public riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `860` | `1` | `0` | `0` | `1` | Not catalogue default | Official |
| `916` | `2` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `860` | `1123` | BTicino (key `1`) | `0` | Extra | `2301_1.0_BT\xml\Extra\extra.xml` |
| `860` | `1124` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2301_1.0_BT\xml\Protocol\protocol.xml` |
| `916` | `1147` | BTicino (key `1`) | `0` | Extra | `2301_2.0_BT\xml\Extra\extra.xml` |
| `916` | `1148` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2301_2.0_BT\xml\Protocol\protocol.xml` |

All 4 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `860` | `1` | `154` Internal Unit | Fixed/designated metadata | `3693` | `154` | `1768` |
| `916` | `1` | `154` Internal Unit | Fixed/designated metadata | `4917` | `154` | `2158` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `860` | Product Programming | `3` | Canonical firmware/mode association |
| `916` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `860` | Ethernet | Canonical firmware/connection association |
| `860` | Ethernet over USB | Canonical firmware/connection association |
| `916` | Ethernet | Canonical firmware/connection association |
| `916` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `F1 / F2; Master / Slave` | family and internal-unit role selection | `LE14222AC` printed/PDF pp. 1-7; `335254-publisher-product-sheet` PDF pp. 1-4 |
| `Idle / active-call commands` | main / communicating entrance panel | `LE14222AC` printed/PDF pp. 1-7; `335254-publisher-product-sheet` PDF pp. 1-4 |
| `335254 compatible-kit inventory` | BTicino references in `LE14222AC` p. 5 | `LE14222AC` printed/PDF pp. 1-7; `335254-publisher-product-sheet` PDF pp. 1-4 |
| `365225 compatible-kit inventory` | Legrand references in `LE14226AB` p. 6 | `LE14222AC` printed/PDF pp. 1-7; `335254-publisher-product-sheet` PDF pp. 1-4 |
| `365225 with 360910/360915/369420/369430` | one connected unit/family; each internal unit needs SP102 | `LE14222AC` printed/PDF pp. 1-7; `335254-publisher-product-sheet` PDF pp. 1-4 |
| `Update readme scope` | 335254 expressly listed; 365225 not added to that readme by inference | `LE14222AC` printed/PDF pp. 1-7; `335254-publisher-product-sheet` PDF pp. 1-4 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `860` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `916` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

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
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `101` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

For 335254, use the instruction’s explicit compatible-kit list and additional-monitor diagrams. The listed kits are 316913/317013/317014/317113/317213/316911/317011/317211 and 317913/317914/318913/318914; this is not authority to expand arbitrary SCS systems. Configure family/role switches, joystick settings and Home + Security association. At idle, door/gate/light commands target the main panel; during a call they target the communicating panel. Intercom needs an additional internal unit. The Wi-Fi LED distinguishes disconnected, disabled/working and active app-data exchange states. The diagrams use a <=10 A protective breaker and show optional separately purchased accessories; the 24 V external accessory power-supply drawings are not substituted for the monitor’s 30 V marking. The app’s Netatmo security controls are integration functions, not additional sensor hardware inside this monitor. `LE14226AB` directly documents 365225. Its compatible kits are 369110/369220/369230/369320/369330, 367910/367915/368910/368915, and the separately illustrated 360910/360915/369420/369430 group. For the last group, only one connected internal unit per family is allowed and each internal unit requires SP102. Its Home + Security application is explicitly named on p. 7. The Easy Kit Connected with Netatmo software readme dated 30 May 2025 explicitly lists 335254 and its software/update environment; it does not by itself add 365225 to that readme’s reference list.

Apply the firmware-specific restrictions above. The generic session/validation method remains in [Programming](../../programming/).

### Additional-monitor groups

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| 335254 third kit group | `LE14222AC` p. 6 also names 310913,310914,318011,318012,318013,318015. For this group only one connected IU per family is permitted and every IU needs SP102. This was missing from the earlier description. | `LE14222AC` p. 6, inspected visually |
| 365225 third kit group | `LE14226AB` p. 6 names 360910,360915,369420,369430. Only one connected IU per family and SP102 for each IU. French wording unexpectedly says each external unit while English and the other checked translations say internal unit; the diagram labels the internal monitors. | `LE14226AB` p. 6 |
| Setup evidence | Instructions point to separate downloadable configuration documentation. No full joystick/account-reset sequence is imported from the older Door Entry EASYKIT product. The Netatmo readme lists335254 and Windows10/11,64bit, .NET4+ software requirements; it does not name365225 or identify the installed release. | `LE14222AC` p. 6;`LE14226AB` p. 7; EASYKIT_CONNECTED_README p. 1 |

## Source reconciliation

335254 and 365225 are explicit catalogue commercial relationships. `LE14222AC` and the export directly cover 335254; `LE14226AB` directly covers 365225 and identifies the Legrand publisher. The two instructions agree on core monitor dimensions/supply/radio facts but list different compatible kit references. The database labels both commercial records BTicino; the marketed Legrand brand for 365225 is shown with that source distinction preserved. The export height 140 mm differs from the instruction’s 142.5 mm; both are preserved. Touch control commands coexist with the export’s “With touch screen: No”, because the display and dedicated controls are different surfaces. The instruction’s English rear legend accidentally lists Speaker twice and numbers power supply as 9 while other languages list it as 8; that numbering defect does not establish an extra interface. The 30 W supply marking is not asserted as measured monitor consumption.

### Reviewed source boundaries

Both commercial mappings are established and both exact instruction originals are retained. Their compatible-kit lists differ. The newly accounted third `335254` group requires one connected internal unit per family and SP102 for each internal unit; those restrictions apply to that group, not every diagram. The 2025 Netatmo readme names `335254` but not `365225`, so it does not establish interchangeable update applicability.

### Retained source accounting

| Original | Examined role / remaining scope |
| --- | --- |
| `LE14222AC.pdf` | English sections PDF pp. 1–6 examined: exact 335254 dimensions, keys, wiring, all three compatible-kit groups and technical data; p. 6 inspected visually; other translations unexamined |
| `335254-publisher-product-sheet.pdf` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes |
| `LE14226AB.pdf` | English sections PDF pp. 1–7 examined: exact 365225 dimensions, controls, wiring, compatible kits, app and technical data; French/internal-unit wording conflict p. 6 retained; remaining translations unexamined |
| `EASYKIT_CONNECTED_README.pdf` | PDF p. 1: entire30May 2025 Netatmo-family exact-reference list and software environment |

## Evidence limits and open work

A retained 365225 commercial export/EAN, dimensional tolerance explaining the 335254 export/instruction height difference, installed kit compatibility and app/firmware/diagnostic behavior remain uncorroborated. Exact instruction originals for both SKUs are retained.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete within the retained evidence scope. Unexamined documentation, source conflicts and runtime corroboration remain explicit limits of this review.

### Discovered sources outside this review

These publisher-linked sources were identified but were not retained or used as evidence. Their presence is not evidence of installed firmware, a certified test result or additional capability.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `DIYN_010011.fwz` | Firmware binary; payload/update applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/DIYN_010011.fwz) |
| `MyHome_Suite_README_v2.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/MyHome_Suite_README_v2.pdf) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0151-0160-2026-10-07.md#own-dev-0160)
