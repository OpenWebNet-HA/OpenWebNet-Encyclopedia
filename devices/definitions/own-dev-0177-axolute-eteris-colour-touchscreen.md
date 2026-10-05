# Axolute Etèris colour touchscreen

## Summary

HW4684 is the Axolute Etèris colour touchscreen for configured MyHOME controls. Its exact historical catalogue entry describes a single colour touch interface for lighting, automation, alarm, temperature, scenarios and energy management. Etèris-specific boxes, supports and finishing plates determine its installation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0177` | Project identity |
| Technical description | Axolute Etèris colour touchscreen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `HW4684` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1512` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `0` | Main association; independent of project ID |
| Firmware definition | `85` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute Etèris | `HW4684` | Established catalogue identity | Manufacturer database commercial record `1512` explicitly links this SKU to item `1512` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `eteris-historical-catalogue.pdf` | Historical exact-product manufacturer source | eteris-historical-catalogue; printed publication date not established | HW4684 printed pp.148, 151 / PDF pp.150, 153; touch-control HC/HS/HD4657M4 printed pp.77, 92, 124, 156 / PDF pp.79, 94, 126, 158, plus occupied box depth printed pp.163-165 / PDF pp.165-167. Separate plate, box, support and display dimensions are not interchangeable. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/07/a5076bf8fe317ce6516dbd3810af363add8eac63c8f783f47974991c6aaabb30.pdf) | [Publisher original](https://www.bticino.es/pdf/C_50_EditorialContent_145_Lib_Props_GLib_AList_GLib_AItem_0_GLib_ABin.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1512`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `monobloc colour touchscreen; exact retained entry does not specify diagonal` | `eteris-historical-catalogue` printed p. 148 / PDF p. 150 and printed p. 151 / PDF p. 153 |
| Installation | `528W masonry or PB528W plasterboard box; monobloc HW4684 shown separately from 8-module H4728W support` | `eteris-historical-catalogue` printed p. 148 / PDF p. 150 and printed p. 151 / PDF p. 153 |
| Box dimensions, 528W | `128.5 x 128.5 x 58 mm; box dimensions, not display enclosure` | `eteris-historical-catalogue` printed p. 148 / PDF p. 150 and printed p. 151 / PDF p. 153 |
| Box dimensions, PB528W | `116.5 x 116.5 x 58 mm; box dimensions, not display enclosure` | `eteris-historical-catalogue` printed p. 148 / PDF p. 150 and printed p. 151 / PDF p. 153 |
| Electrical ratings | `not established for HW4684 by the retained exact catalogue pages` | `eteris-historical-catalogue` printed p. 148 / PDF p. 150 and printed p. 151 / PDF p. 153 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1512` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `0` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `85` | `6` | `0` | `8` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `85` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1330` | `32` | `690` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `85` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `85` | Ethernet | `2` |
| `85` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `85` | `1` | `3` | `TiDisplayColorIP_0601` | Parameter type `7`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Catalogue programming routes` | Use each exact Firmware association and connection label above; no modality inferred from a bare mode ID | Exact source scope in Documentation; canonical catalogue tables below |
| `Physical selector map` | No complete exact-product physical selector map established by retained originals; reusable Object fields remain separate | Exact source scope in Documentation; canonical catalogue tables below |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `85` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `85` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `85` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `85` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `0` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Use the named Etèris mounting combination in the exact catalogue table. The colour-touchscreen Object and Firmware `85` provide the complete retained canonical configuration surface. The catalogue establishes system-control functions but does not supply HW4684’s full software transfer, user operation or electrical specification. Do not copy H4684 enclosure or module dimensions merely because the references and UI role are similar.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The historical catalogue establishes HW4684 as Axolute Etèris. The mounting table separates the 8-module H4728W support from the monobloc HW4684 touchscreen and its plates; that support is not assigned to HW4684. Its box dimensions are installation-accessory facts, not touchscreen body dimensions. The HW4684-specific entry does not state a 3.5-inch diagonal or sound-control function, so those are not imported from neighbouring touchscreens. The database’s explicit single-SKU item remains distinct from H4684/L4684 and AM5864. U1881 manufacturer retrieval attempts returned 403/404 and were not retained as original PDFs.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `eteris-historical-catalogue.pdf` | HW4684 printed pp.148, 151 / PDF pp.150, 153; touch-control HC/HS/HD4657M4 printed pp.77, 92, 124, 156 / PDF pp.79, 94, 126, 158, plus occupied box depth printed pp.163-165 / PDF pp.165-167. Separate plate, box, support and display dimensions are not interchangeable. |

## Evidence limits and open work

An exact electrical / installation / software manual, software applicability and EAN for HW4684 and installed diagnostics remain gaps; its identity is established.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
