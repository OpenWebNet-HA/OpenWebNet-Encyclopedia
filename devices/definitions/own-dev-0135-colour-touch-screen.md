# Colour Touch Screen

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0135` | Project identity |
| Technical description | Colour Touch Screen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `H4684`, `L4684` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1509` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `29` | Main association; independent of project ID |
| Firmware definition | `76`, `77`, `78`, `79` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4684` | Established catalogue identity | Manufacturer database commercial record `924` explicitly links this SKU to item `1509` |
| BTicino - LivingLight | `L4684` | Established catalogue identity | Manufacturer database commercial record `1509` explicitly links this SKU to item `1509` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `H4684-L4684-Spanish-sheet.pdf` | Exact historical manufacturer documentation | `H4684-L4684-Spanish-sheet; original publication date not established` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/7e/0e7e541678c24f2c6fb3445041664efa8ab701544e814efc31a1c5b6ac0955a3.pdf) | [Publisher original](https://www.bticino.es/conceptbook/files/H4684_L4684.pdf) |
| `BT00287-a-EN.pdf` | Exact manufacturer documentation | `BT00287-a-EN; original publication date not established` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/20/31/20315182f949ce1ad7be68bbe4955e4189b26161fe881fab599d2cae15959f0a.pdf) | [Publisher original](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileId=58107.23188.48069.54823&fileName=BT00287-a-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1509` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Nominal / operating SCS supply | `27 Vdc / 18..27 Vdc` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |
| Current draw | `80 mA` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |
| Operating temperature | `0..40 °C` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |
| Mounting | `3+3 flush-mounted wiring-device modules; box 506E` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |
| Display | `backlit colour touch screen` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |
| PC interfaces | `335919 RS232; 3559 USB; Ethernet` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |
| Software | `TiDisplay Color` | `BT00287-a-UK` and `BT00287-a-ES`, printed/PDF pp. 1-2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1509` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | 0; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `29` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `76` | `6` | `0` | `8` | `1` | Catalogue default | Official |
| `77` | `5` | `0` | `9` | `1` | Not catalogue default | Official |
| `78` | `4` | `1` | `19` | `1` | Not catalogue default | Official |
| `79` | `3` | `0` | `9` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `76` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1321` | `32` | `681` |
| `77` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1322` | `32` | `682` |
| `78` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1323` | `32` | `683` |
| `79` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1324` | `32` | `684` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `76` | Product Programming | `3` | Association key `4` |
| `77` | Product Programming | `3` | Association key `4` |
| `78` | Product Programming | `3` | Association key `4` |
| `79` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `76` | Ethernet | `2` |
| `76` | USB | `3` |
| `77` | Ethernet | `2` |
| `77` | USB | `3` |
| `78` | Ethernet | `2` |
| `78` | USB | `3` |
| `79` | Ethernet | `2` |
| `79` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `76` | `1` | `1` | `TiDisplayColorIP_0601` | Parameter type `7`; payload not inspected |
| `76` | `1` | `3` | `TiDisplayColorIP_0601` | Parameter type `7`; payload not inspected |
| `77` | `1` | `1` | `TiDisplayColorIP_0500` | Parameter type `7`; payload not inspected |
| `77` | `1` | `3` | `TiDisplayColorIP_0500` | Parameter type `7`; payload not inspected |
| `78` | `1` | `1` | `TiDisplayColorIP_0400` | Parameter type `7`; payload not inspected |
| `78` | `1` | `3` | `TiDisplayColorIP_0400` | Parameter type `7`; payload not inspected |
| `79` | `1` | `1` | `TiDisplayColorIP_0101` | Parameter type `7`; payload not inspected |
| `79` | `1` | `3` | `TiDisplayColorIP_0101` | Parameter type `7`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `76` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `76` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
| `76` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `76` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `77` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `77` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
| `77` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `77` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `78` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `78` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
| `78` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `78` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `79` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `79` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
| `79` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `79` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `29` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `32` - Colors Touch Screen | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Create or modify a TiDisplay Color project linking icons to automation, lighting, scenario, temperature, sound, alarm and energy functions. The software also configures logical/time scenarios, scheduled activities, clock/date, access password, graphical style and firmware updating. Select plates and mounting accessories for the actual line. Configured pages describe remote system roles, not multiple local Object instances.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

H4684/L4684 catalogue identities agree with exact English and Spanish sheets. The English filename ends EN but its printed code is BT00287-a-UK; that literal is preserved. English also co-lists AM5864, which is not a commercial member of this cluster. The sheets agree on supply, current, temperature and mounting. Four historical Firmware definitions and one UI Object describe catalogue applicability, not four installed firmware releases. The database’s L/N/NT grouping is rendered as the marketed LivingLight line.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `H4684-L4684-Spanish-sheet.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `BT00287-a-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

## Evidence limits and open work

Full TiDisplay Color software manual, exact reset procedure, hardware/microcontroller identities and installed per-firmware diagnostic/function behavior remain missing.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
