# Easy Kit Connected video-entry kit

## Summary

This catalogue cluster groups the Easy Kit Connected references 318011 and 369420. The retained 369420 kit manual describes a 7-inch connected handsfree monitor with door, gate, light and intercom controls. Wi-Fi supports the published Door Entry EASYKIT service; variant-specific documentation is needed before assigning every 369420 kit detail to 318011.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0158` | Project identity |
| Technical description | Easy Kit Connected video-entry kit | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `318011`, `369420` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2279` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Video door entry system | Main system association |
| Item model / `modobj` | `100` | Main association; independent of project ID |
| Firmware definition | `809` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `318011` | Established catalogue identity | Manufacturer database commercial record `2640` explicitly links this SKU to item `2279` |
| Legrand | `369420` | Established catalogue identity | Manufacturer database commercial record `2642` explicitly links this SKU to item `2279` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE11336AC.pdf` | Exact-product manufacturer original | `LE11336AC01PC-21W38; printed revision label` | Retained 56-page original; exact-product technical, configuration and operating sections reviewed where applicable. Source-specific facts and remaining limits are scoped in the dossier; this does not claim a line-by-line review of every manual page. | [Archived original](https://archive.openwebnet-ha.org/sha256/19/b8/19b830b183591f73371d050eed408836579cad37a1d815fbfca968f3026b8709.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE11336AC.pdf) |
| `EASYKIT_CONNECTED_D_E_READMEv1.pdf` | Exact catalogue-reference compatibility/readme | `EASYKIT_CONNECTED_D_E_READMEv1; 04/08/2025` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/b5/d3/b5d30fbae1c4ac0b1ea6cede9cf5cce7ceb968b39875beb523741559793d42b0.pdf) | [Publisher original](https://assets.legrand.com/pim/AUTRE/EASYKIT_CONNECTED_D_E_READMEv1.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2279`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| 369420 monitor display | `7-inch, 16:9; dedicated touch control keys and joystick` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| 369420 power-source marking | `DC 30 V / 30 W; supply marking, not measured monitor consumption` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| Wireless, 369420 | `IEEE 802.11 b/g/n; 2.4..2.4835 GHz; <20 dBm; WEP/WPA/WPA2` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| 369420 connectors | `D1/D2 previous panel or monitor; R1/R2 next monitor; mini-USB service` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| Family / role selection | `family 1/family 2 and Master/Slave switches` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| 369420 cable limits | `80 m for 2 x 0.28 mm² twisted pair / 100 m for 2 x 0.5 mm² 573999 cable` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| CCTV secondary-panel connection | `100 m coaxial in specified diagram` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| Published app limit | `one connected indoor unit per family linked to home Wi-Fi/app` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| Software readme references | `318011 explicitly listed in BTicino family; 369420 in Legrand family` | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2279` | Canonical catalogue |
| Technical item description | Easy Kit Connnected | Canonical catalogue |
| Item family | 0; key `20` | Canonical catalogue |
| Main system | Video door entry system; key `4` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `100` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `809` | `1` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `809` | `1` | `154` Internal Unit | Fixed/designated metadata | `3391` | `154` | `1645` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `809` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `809` | Ethernet | `2` |
| `809` | Ethernet over USB | `4` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `809` | `1` | `0` | `2279_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `809` | `1` | `0` | `2279_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `369420 F1 / F2` | single/two-family addressing; entrance button adapts | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| `369420 Master / Slave` | monitor role selection | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| `Idle / active-call door,gate,light` | main panel / communicating panel | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| `App connection` | one connected monitor per family | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |
| `318011` | exact software readme identity; full exact kit instruction still absent | `LE11336AC` printed/PDF pp. 3-6,14,18-20,21-40; `EASYKIT_CONNECTED_D_E_READMEv1` PDF pp. 1-2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `809` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

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
| `DIMENSION 1` | Corroborate item model `100` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

For 369420, use the exact single-family/two-family wiring and family/role switches. The entrance-panel call adapts to F1/F2 settings. At idle, door/gate/light keys act on the main entrance panel; during a call they act on the communicating panel. Intercom requires an additional monitor. Configure ringing, video/audio and Wi-Fi through the joystick; the installation manual separately covers app association and Wi-Fi reset. Red bell LED flashing means ringtone excluded; red Wi-Fi flashing means enabled but disconnected; off means disabled or working; steady red means app data exchange. The software readme lists the supported Easy Kit families and device/software update context; it does not prove that a 318011 package has the same contents or every electrical value as 369420.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The manufacturer database explicitly links both SKUs to item 2279, and the software readme names both. LE11336AC names 369420/369430, not 318011: its kit counts, cable/electrical details and commissioning instructions are therefore scoped to 369420. Publisher exports for 318011 were not found at the attempted endpoints; the Legrand 369420 export returned 403. These are documentation gaps, not unresolved identities. The single catalogue indoor-unit Object `154` describes the configured device role, not the entire kit’s component count. This older app generation must not be replaced silently with the newer Home + Security generation. The database labels 369420 as BTicino, while its exact manufacturer manual identifies Legrand; the commercial identity uses the marketed Legrand brand without changing the explicit database relationship.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE11336AC.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `EASYKIT_CONNECTED_D_E_READMEv1.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |

## Evidence limits and open work

An exact 318011 installation/contents sheet, a retained commercial export/EAN for each kit, and current app/update compatibility remain documentation gaps. Hardware fingerprint and observed operation remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
