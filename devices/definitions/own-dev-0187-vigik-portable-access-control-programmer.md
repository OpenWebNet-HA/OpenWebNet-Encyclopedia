# Vigik portable access-control programmer

## Summary

348405 is a portable programmer for Vigik access installations. Its display, keypad and badge-reading antennas let an installer manage sites and credentials, then transfer data to a 348040 controller or T25 reader; SD and smart-card slots support site storage and Vigik services.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0187` | Project identity |
| Technical description | Vigik portable access-control programmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `348405` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1690` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `5` | Main association; independent of project ID |
| Firmware definition | `102`, `587` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `348405` | Established catalogue identity | Manufacturer database commercial record `1754` explicitly links this SKU to item `1690` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `guide_controle_dacces_vigik.pdf` | Vigik access-control system guide | `Publication date not established` | Printed/PDF pp. 5, 7, 9, 12-19, 24-41: 348040 controller, 348405 programmer and 348330 GPRS specifications, administration modes and historical service workflow. | [Archived original](https://archive.openwebnet-ha.org/sha256/21/f1/21f15d54f5aabef655f35d8c64294b6288fdf5a6e1bfa98fc2d905d6e0f05563.pdf) | [Publisher original](https://assets.legrand.com/general/mediagrp/np-ft-gt/guide_controle_dacces_vigik.pdf) |
| `BT00756_b_IT.pdf` | 348405 programmer technical sheet | `BT00756-b-IT; 16/01/2014` | Printed/PDF p. 1: supply / batteries, display, dimensions, buttons, antennas, USB / micro-USB and storage interfaces. | [Archived original](https://archive.openwebnet-ha.org/sha256/4a/35/4a35bb890420c58e5a84c7af95932722786d828632aaa74ece0ac849bbbed67a.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00756_b_IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1690`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply alternatives | `Micro-USB; four AA alkaline or four rechargeable NiMH AA cells, not supplied` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |
| Display | `Backlit graphical LCD, 128 × 64 dots` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |
| Dimensions | `96 × 155 × 40 mm` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |
| Local interface | `Membrane alphanumeric keypad; F1/F2/F3; directional, OK, cancel and power keys` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |
| Connections | `USB to controller; micro-USB to PC/power/charging` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |
| Radio interfaces | `Front antenna for badge read/programming; rear antenna for T25 communication` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |
| Storage interfaces | `SD card for site database/data logging; smart-card slot for Vigik service cards` | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` printed/PDF p. 7 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1690` | Canonical catalogue |
| Technical item description | Local portable programmer | Canonical catalogue |
| Item family | Source placeholder description `0`; key `100` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `5` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `102` | `1` | `0` | `1` | `1` | Catalogue default | Official |
| `587` | `1` | `1` | `29` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `102` | `1` | `126` Local portable programmer | Fixed / designated metadata | `2405` | `622` | `1057` |
| `587` | `1` | `126` Local portable programmer | Fixed / designated metadata | `2404` | `622` | `1056` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `102` | Product Programming | `3` | Association key `4` |
| `587` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `102` | USB | `3` |
| `587` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `102` | `0` | `0` | `1690_1.0_undefined\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `102` | `0` | `0` | `1690_1.0_undefined\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `102` | `1` | `0` | `1690_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `102` | `1` | `0` | `1690_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `587` | `1` | `0` | `1690_1.1_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `587` | `1` | `0` | `1690_1.1_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| USB / micro-USB | Controller connection / PC, supply and NiMH charging | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` pp. 7, 13-18 |
| Front / rear antenna | Badge reading / programming / T25 communication | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` pp. 7, 13-18 |
| SD / smart card | Site database and logging / Vigik services | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` pp. 7, 13-18 |
| Local / local-plus | Local site / badge programming / portal database transfer via programmer | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` pp. 7, 13-18 |
| Battery scope | Four alkaline AA or four NiMH AA; recharge applies to NiMH | `BT00756_b_IT.pdf` printed/PDF p. 1; `guide_controle_dacces_vigik.pdf` pp. 7, 13-18 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `102` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `587` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `126` - Local portable programmer

Catalogue Object key `622` maps to external Object `126`.

| Surface | Evidence |
| --- | --- |
| Object configuration | No reusable fields stored for this Object in the canonical catalogue |

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

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `5` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `126` - Local portable programmer | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `126` - Local portable programmer | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The technical sheet describes local-menu programming or a site database downloaded from the dedicated web portal. Transfer to 348040 uses USB / micro-USB, or communication through the T25 reading head. The guide places this device in local and local-plus administration (printed/PDF pp. 13-18). The detailed installer manual, battery-selection procedure and exact transfer / error recovery sequence are not retained in this batch; configuration fields below are catalogue metadata.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact technical sheet and system guide agree on front badge and rear reader antennas, SD / smart-card slots and the separation of USB / controller and micro-USB/PC connections. Recharge applies to NiMH cells; alkaline cells are not represented as rechargeable. Catalogue gateway-related identity tokens do not prove that this portable accessory answers installed-device diagnostics.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `guide_controle_dacces_vigik.pdf` | Printed/PDF pp. 5, 7, 9, 12-19, 24-41: 348040 controller, 348405 programmer and 348330 GPRS specifications, administration modes and historical service workflow. |
| `BT00756_b_IT.pdf` | Printed/PDF p. 1: supply / batteries, display, dimensions, buttons, antennas, USB / micro-USB and storage interfaces. |

## Evidence limits and open work

Operating temperature, protection, charger electrical rating, radio frequencies, detailed administrator workflow and installed firmware behavior remain unestablished.

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
| `guide_controle_dacces_vigik.pdf` | `21f15d54f5aabef655f35d8c64294b6288fdf5a6e1bfa98fc2d905d6e0f05563` | 14121445 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/21/f1/21f15d54f5aabef655f35d8c64294b6288fdf5a6e1bfa98fc2d905d6e0f05563.pdf) |
| `BT00756_b_IT.pdf` | `4a35bb890420c58e5a84c7af95932722786d828632aaa74ece0ac849bbbed67a` | 641417 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/4a/35/4a35bb890420c58e5a84c7af95932722786d828632aaa74ece0ac849bbbed67a.pdf) |
