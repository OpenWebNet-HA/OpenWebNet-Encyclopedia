# Arteor 573960 colour touchscreen

## Summary

Arteor 573960 is a Legrand colour touchscreen for controlling a MyHOME installation. Its catalogue Object exposes configurable lighting, automation and scenario functions, with different firmware definitions that must be matched to the installed unit.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0193` | Project identity |
| Technical description | Arteor 573960 colour touchscreen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `573960` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1814` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `39` | Main association; independent of project ID |
| Firmware definition | `91`, `92`, `93` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Arteor | `573960` | Established catalogue identity | Manufacturer database commercial record `1957` explicitly links this SKU to item `1814` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ex212001_657.pdf` | Historical lighting catalogue page | `Catalogue 2012–2013; extract ex212001_657` | Printed p. 657 / PDF p. 1: 002645 and 573960 exact-reference mentions; 573958 paragraph excluded from 573960 specifications. | [Archived original](https://archive.openwebnet-ha.org/sha256/40/0d/400d2496efd6d5d7d7ecb32711f9014db2d885f83849c64d8bbb5b262144f662.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/cexp2012-13/ex212001_657.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1814`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Exact reference in historical catalogue | `573960 pictured and named in scenario-module compatibility text` | `ex212001_657.pdf` printed p. 657 / PDF p. 1; canonical catalogue item `1814` |
| Catalogue user-interface role | `Colour touchscreen; three distinct Firmware definitions` | `ex212001_657.pdf` printed p. 657 / PDF p. 1; canonical catalogue item `1814` |
| Exact electrical / mechanical ratings | `Not established by retained exact-product technical sheet` | `ex212001_657.pdf` printed p. 657 / PDF p. 1; canonical catalogue item `1814` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1814` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `39` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `91` | `6` | `0` | `1` | `1` | Catalogue default | Official |
| `92` | `5` | `0` | `9` | `1` | Not catalogue default | Official |
| `93` | `4` | `1` | `19` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `91` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1327` | `32` | `687` |
| `92` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1328` | `32` | `688` |
| `93` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1329` | `32` | `689` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `91` | Product Programming | `3` | Association key `4` |
| `92` | Product Programming | `3` | Association key `4` |
| `93` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `91` | Ethernet | `2` |
| `91` | USB | `3` |
| `92` | Ethernet | `2` |
| `92` | USB | `3` |
| `93` | Ethernet | `2` |
| `93` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `91` | `2` | `0` | `ColorTouchConfigIP_0601` | Parameter type `7`; payload not inspected |
| `91` | `2` | `2` | `ColorTouchConfigIP_0601` | Parameter type `7`; payload not inspected |
| `92` | `2` | `0` | `ColorTouchConfigIP_0500` | Parameter type `7`; payload not inspected |
| `92` | `2` | `2` | `ColorTouchConfigIP_0500` | Parameter type `7`; payload not inspected |
| `93` | `2` | `0` | `ColorTouchConfigIP_0400` | Parameter type `7`; payload not inspected |
| `93` | `2` | `2` | `ColorTouchConfigIP_0400` | Parameter type `7`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Firmware selection | Match the exact revision, Object association, restrictions and connection label below | Canonical `MHCatalogue.db`; exact-product documentation limits below |
| Physical selector / transfer sequence | Not established by an exact retained technical / installation manual | Canonical `MHCatalogue.db`; exact-product documentation limits below |
| Remote functions | Configure the actual remote-system references; a UI control field does not instantiate the target actuator locally | Canonical `MHCatalogue.db`; exact-product documentation limits below |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `91` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `91` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `91` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `91` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `92` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `92` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `92` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `92` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `93` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `93` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `93` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `93` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `39` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `32` - Colors Touch Screen | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `32` - Colors Touch Screen | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The historical catalogue names 573960 as a control associated with scenario module 003551/F420, without software tools for that scenario-module use. This does not replace the exact touchscreen’s configuration software / manual. Match its three canonical Firmware definitions, Object fields, connections and parameters below; software masks and reusable domains are not a physical selector map.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The same historical catalogue page pictures 573960 and names it in the F420 compatibility text, but its touch-screen commercial paragraph lists 573958. Paragraph-level mounting / finish details are therefore not assigned to 573960. The explicit catalogue record establishes the Arteor identity; neither 573958 nor newer touchscreen ratings are substituted.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `ex212001_657.pdf` | Printed p. 657 / PDF p. 1: 002645 and 573960 exact-reference mentions; 573958 paragraph excluded from 573960 specifications. |

## Evidence limits and open work

An exact 573960 technical / install / user manual, EAN, display size, supply / draw, mounting and revision-scoped operation remain documentation gaps.

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
| `ex212001_657.pdf` | `400d2496efd6d5d7d7ecb32711f9014db2d885f83849c64d8bbb5b262144f662` | 265011 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/40/0d/400d2496efd6d5d7d7ecb32711f9014db2d885f83849c64d8bbb5b262144f662.pdf) |
