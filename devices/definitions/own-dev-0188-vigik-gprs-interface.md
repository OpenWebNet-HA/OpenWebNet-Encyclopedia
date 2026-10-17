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

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `348330` | GPRS Interface | Canonical commercial record `1755` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `guide_controle_dacces_vigik.pdf` | Vigik access-control system guide | `Publication date not established` | Printed/PDF pp. 5, 7, 9, 12-19: 348040 controller, 348405 programmer and 348330 GPRS specifications, administration modes and historical service workflow. | [Archived original](https://archive.openwebnet-ha.org/sha256/21/f1/21f15d54f5aabef655f35d8c64294b6288fdf5a6e1bfa98fc2d905d6e0f05563.pdf) | [Publisher original](https://assets.legrand.com/general/mediagrp/np-ft-gt/guide_controle_dacces_vigik.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1691`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `RA00082AA_S_FR.pdf` | ACWEB installer portal manual | RA00082AA_S_FR; publication date unestablished | Printed/PDF pp. 14–41: local-plus/online configuration, validation, transfers, site/family/service limits and synchronisation; portal concepts are not local Objects | [Archived original](https://archive.openwebnet-ha.org/sha256/80/05/80052edcb622123171d31b6797b3ee0efb70125f285e3c30f6ce4a9afc789bd9.pdf) | [Publisher source](https://www.acweb.bticino.com/fr_FR/browser/attachments/bin/help/RA00082AA_S_FR.pdf) |
| `BT-controle-acces.pdf` | Manufacturer access-control brochure | Publication date unestablished | Printed pp. 12–13 / PDF pp. 14–15: exact controller, programmer and GPRS descriptions; supply and USB wording conflicts scoped | [Archived original](https://archive.openwebnet-ha.org/sha256/f9/bd/f9bdca3299f987ae1207b5fdeb9b4be5173038d9f448734597d819c9eeb58d3f.pdf) | [Publisher source](https://assets.legrand.com/pim/DOCUMENT/BT_controle_acces.pdf) |

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

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Access control | `7` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `99` | `1` | `0` | `1` | `2` | Catalogue default | Official |
| `728` | `1` | `1` | `0` | `2` | Not catalogue default | Official |
| `800` | `3` | `0` | `0` | `2` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `99` | `163` | BTicino (key `1`) | `0` | Extra | `1691_1.0_BT\xml\Extra\extra.xml` |
| `99` | `165` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1691_1.0_BT\xml\Protocol\protocol.xml` |
| `728` | `1022` | BTicino (key `1`) | `0` | Extra | `1691_1.1_BT\xml\Extra\extra.xml` |
| `728` | `1023` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1691_1.1_BT\xml\Protocol\protocol.xml` |
| `800` | `1042` | BTicino (key `1`) | `0` | Extra | `1691_3.0_BT\xml\Extra\extra.xml` |
| `800` | `1043` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1691_3.0_BT\xml\Protocol\protocol.xml` |

All 6 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

The Vigik integration compatibility table requires 348330 GPRS interface 1.00.43 (guide printed/PDF p. 19). This is a minimum for the named intercom/access integration, not proof that every older catalogue release supports it. Companion requirements include 348040/T25 1.02.06/2.01.00, 348405 1.01.26 and 348330 1.00.43; exact connected-product applicability must be checked.

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
| `99` | Product Programming | `3` | Canonical firmware/mode association |
| `728` | Product Programming | `3` | Canonical firmware/mode association |
| `800` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `99` | USB | Canonical firmware/connection association |
| `728` | USB | Canonical firmware/connection association |
| `800` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

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

The two slots are Basic GPRS external Object `227` and XOpen SCS external Object `250`; they are not two cellular interfaces or two door outputs. Item-side `FW_VER` default `1.0.0` is not the installed firmware of all three releases. The serial template `00000000` and documented LAN defaults are public catalogue values. A reusable XOpen `LAN_IP` field does not establish a physical Ethernet port on this GPRS/USB device. Gateway flags differ between the two roles and do not replace the product’s documented remote-management function.

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

### ACWEB configuration and transfer scope

The retained AA installer manual separates Local Plus (transfer through 348405) from On-line (through 348330); site and management types cannot be changed after setup (p. 14). Controllers must be associated with at least one entrance, with one Vigik reader per controller (p. 19). Validate addresses before activation; Local Plus requires confirming settings, exporting the site and transferring it through the portable programmer (pp. 21–23). On-line requires the site password and interface serial, installation diagnostics and correction of errors before management is enabled (pp. 24–28). These are setup requirements; no installation-specific credentials or serial are retained here.

Even an On-line site must add new Vigik services through 348405: export to the programmer, add the service, transfer to the controller and import the changed site back to ACWEB (p. 31). The Local Plus sequence imports the changed site before the controller transfer. AA portal notifications distinguish pending, sent/acknowledged and executed commands; GPRS connects hourly, with an immediate synchronisation option (p. 41). Portal or mobile-service availability today is unestablished.

## Source reconciliation

The manufacturer guide gives an exact 348330 reference, 27 Vdc external supply and 90 mA maximum. Secondary catalogues mentioning 12 Vac are not used to override that primary-source rating. The five-year service period is the original offer’s duration, not a current subscription guarantee. The two candidate gateway Objects are separate catalogue roles.

The guide p. 9 and brochure printed p. 13 / PDF p. 15 agree on SCS `18..27` Vdc or a separate 27 Vdc supply with SCS connection. The five years of included communication describe a historical commercial offer; they do not establish a presently active SIM or service. A discovered [2016 distributor catalogue](https://res.cloudinary.com/sonepar-fr/raw/upload/s--hZlaS8si--/v1/documents/38/348405.pdf) is an unretained revision lead, outside examined evidence; no auxiliary-voltage statement from it is adopted.

## Evidence limits and open work

A current exact installation instruction, modem bands, operating temperature, protection, source-specific provisioning details and current mobile-service availability remain unresolved documentation / operation evidence, not identity issues.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

The official ACWEB AD HTML overview was found at [RA00082AD_S_FR-3.html](https://www.acweb.bticino.com/fr_FR/browser/attachments/bin/help/PortailACWEB-FR/RA00082AD_S_FR-3.html). Only its Local Plus / On-line overview was inspected; the complete AD revision is outside this review. The corresponding attempted PDF retrieval returned 404. AA procedures must not be represented as a complete reconciliation of AD. The older Vigik guide’s customer-screen walkthrough beyond p. 19 was not re-audited; the AA installer manual supplies the reviewed portal workflow.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0181-0190-2026-10-07.md#own-dev-0188)
