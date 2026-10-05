# Vigik GPRS interface

## Summary

348330 is the GPRS communication interface for remote administration of a Vigik access-control installation through ACWEB. It links the site’s SCS equipment to the mobile service, allowing access records and compatible entrance-panel data to be updated remotely.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0188` | Project identity |
| Technical description | Vigik GPRS interface | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `348330` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1691` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `7` | Main association; independent of project ID |
| Firmware definition | `99`, `728`, `800` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Gateways and interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `348330` | Established catalogue identity | Manufacturer database commercial record `1755` explicitly links this SKU to item `1691` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `guide_controle_dacces_vigik.pdf` | Vigik access-control system guide | `Publication date not established` | Printed/PDF pp. 5, 7, 9, 12-19, 24-41: 348040 controller, 348405 programmer and 348330 GPRS specifications, administration modes and historical service workflow. | [Archived original](https://archive.openwebnet-ha.org/sha256/21/f1/21f15d54f5aabef655f35d8c64294b6288fdf5a6e1bfa98fc2d905d6e0f05563.pdf) | [Publisher original](https://assets.legrand.com/general/mediagrp/np-ft-gt/guide_controle_dacces_vigik.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1691`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `Two-wire SCS 18..27 Vdc or external 27 Vdc` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |
| Maximum consumption | `90 mA` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |
| Mounting | `6 DIN modules` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |
| Interfaces | `USB to PC; remote GSM antenna with RF connector; supplied dedicated SIM` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |
| Indicators | `Three operation/status LEDs` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |
| Historical service offer | `Five years prepaid communication from activation; renewal described in guide` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |
| Service scope | `One dedicated 348330 interface and one access-control installation per supplied SIM` | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1691` | Canonical catalogue |
| Technical item description | GPRS Interface | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `7` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `99` | `1` | `0` | `1` | `2` | Catalogue default | Official |
| `728` | `1` | `1` | `0` | `2` | Not catalogue default | Official |
| `800` | `3` | `0` | `0` | `2` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `99` | `1` | `227` Basic gateway GPRS | Fixed / designated metadata | `2367` | `552` | `1022` |
| `99` | `2` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2368` | `551` | `1023` |
| `728` | `1` | `227` Basic gateway GPRS | Fixed / designated metadata | `2659` | `552` | `1269` |
| `728` | `2` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2660` | `551` | `1270` |
| `800` | `1` | `227` Basic gateway GPRS | Fixed / designated metadata | `3288` | `552` | `1591` |
| `800` | `2` | `250` Gateway XOpen SCS | Fixed / designated metadata | `3289` | `551` | `1592` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `99` | Product Programming | `3` | Association key `4` |
| `728` | Product Programming | `3` | Association key `4` |
| `800` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `99` | USB | `3` |
| `728` | USB | `3` |
| `800` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `99` | `1` | `0` | `1691_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `99` | `1` | `0` | `1691_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `728` | `1` | `0` | `1691_1.1_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `728` | `1` | `0` | `1691_1.1_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `800` | `1` | `0` | `1691_3.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `800` | `1` | `0` | `1691_3.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Service association | Dedicated module/SIM for one access installation | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19, 24-41 |
| SIM activation | Install and power module; historical activation workflow | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19, 24-41 |
| Remote administration | Portal site data and badge / compatible entrance-panel updates | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19, 24-41 |
| Original service period | Five years prepaid; renewal described; present availability uncorroborated | `guide_controle_dacces_vigik.pdf` printed/PDF pp. 9, 18-19, 24-41 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `99` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `99` | `S/N` | `########` = S/N | `00000000` | Serial Number |
| `99` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `99` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `1` | Gateway |
| `728` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `728` | `S/N` | `########` = S/N | `00000000` | Serial Number |
| `728` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `728` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `1` | Gateway |
| `800` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `800` | `S/N` | `########` = S/N | `00000000` | Serial Number |
| `800` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `800` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `1` | Gateway |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `250` - Gateway XOpen SCS

Catalogue Object key `551` maps to external Object `250`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `227` - Basic gateway GPRS

Catalogue Object key `552` maps to external Object `227`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `S/N` | `########` = S/N | `00000000` | Serial Number |
| `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `1` | Gateway |

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
| `DIMENSION 1` | Corroborate item model `7` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `227` - Basic gateway GPRS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `250` - Gateway XOpen SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `227` - Basic gateway GPRS | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `250` - Gateway XOpen SCS | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The guide describes online administration with registration of the site and association of the module, followed by remote site updates (printed/PDF pp. 18-19, 24-41). The supplied SIM is activated when installed and powered; this is a historical manufacturer workflow, not verification that today’s network / service remains available. Follow exact Firmware configuration and gateway restrictions below; generic mobile-data capability is not inferred.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The manufacturer guide gives an exact 348330 reference, 27 Vdc external supply and 90 mA maximum. Secondary catalogues mentioning 12 Vac are not used to override that primary-source rating. The five-year service period is the original offer’s duration, not a current subscription guarantee. The two candidate gateway Objects are separate catalogue roles.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `guide_controle_dacces_vigik.pdf` | Printed/PDF pp. 5, 7, 9, 12-19, 24-41: 348040 controller, 348405 programmer and 348330 GPRS specifications, administration modes and historical service workflow. |

## Evidence limits and open work

A current exact installation instruction, modem bands, operating temperature, protection, source-specific provisioning details and current mobile-service availability remain unresolved documentation / operation evidence, not identity issues.

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
