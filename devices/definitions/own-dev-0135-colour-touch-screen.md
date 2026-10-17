# Colour Touch Screen

## Summary

This flush-mounted colour touchscreen brings configured lighting, automation, scenarios, temperature, sound and other MyHOME functions into one interface. Its backlit screen uses programmable icons, with TiDisplay Color software defining the controls and graphical layout.

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

### Catalogue labels and classifications

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `H4684` | Colour Touch Screen | Canonical commercial record `924` |
| `L4684` | Colour Touch Screen | Canonical commercial record `1509` |

Both commercial records are enabled for catalogue display, have no visibility-type value, and are not marked dependent or gateway in this historical commercial table. These classifications do not establish market availability, installed state or functional gateway capability. Empty or truncated internal description labels are not used to infer additional product features.

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

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `29` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `76` | `6` | `0` | `8` | `1` | Catalogue default | Official |
| `77` | `5` | `0` | `9` | `1` | Not catalogue default | Official |
| `78` | `4` | `1` | `19` | `1` | Not catalogue default | Official |
| `79` | `3` | `0` | `9` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `76` | `56` | BTicino (key `1`) | `1` | external software | `TiDisplayColorIP_0601` |
| `76` | `56` | BTicino (key `1`) | `3` | external software | `TiDisplayColorIP_0601` |
| `77` | `98` | BTicino (key `1`) | `1` | external software | `TiDisplayColorIP_0500` |
| `77` | `98` | BTicino (key `1`) | `3` | external software | `TiDisplayColorIP_0500` |
| `78` | `99` | BTicino (key `1`) | `1` | external software | `TiDisplayColorIP_0400` |
| `78` | `99` | BTicino (key `1`) | `3` | external software | `TiDisplayColorIP_0400` |
| `79` | `101` | BTicino (key `1`) | `1` | external software | `TiDisplayColorIP_0101` |
| `79` | `101` | BTicino (key `1`) | `3` | external software | `TiDisplayColorIP_0101` |

All 8 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

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
| `76` | Product Programming | `3` | Canonical firmware/mode association |
| `77` | Product Programming | `3` | Canonical firmware/mode association |
| `78` | Product Programming | `3` | Canonical firmware/mode association |
| `79` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `76` | Ethernet | Canonical firmware/connection association |
| `76` | USB | Canonical firmware/connection association |
| `77` | Ethernet | Canonical firmware/connection association |
| `77` | USB | Canonical firmware/connection association |
| `78` | Ethernet | Canonical firmware/connection association |
| `78` | USB | Canonical firmware/connection association |
| `79` | Ethernet | Canonical firmware/connection association |
| `79` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `76` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `76` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `76` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `76` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `77` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `77` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `77` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `77` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `78` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `78` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `78` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `78` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `79` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `79` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `79` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `79` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
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

### Semantic review findings

All four official firmware definitions (`6.0.8`, default; `5.0.9`; `4.1.19`; `3.0.9`) place one Object `32`, with no Virgin, conditions, filters or conversions. The common reusable/firmware `FW_VER=3.0.0` is a historical schema default, not evidence of the installed tuple. Eight USB/Ethernet connection associations and eight TiDisplayColorIP parameter associations are separate from the technical sheets' TiDisplay Color, RS232/USB-adapter and LAN examples. The English sheet also names `AM5864`; that reference is not added to this catalogue item. Spanish imposition timestamps `01/04/11` are document-production metadata rather than a hardware release mapping. Exact legacy software discovery distinguishes TiDisplayColor and TiDisplayColorIP editions but the linked edition-specific manuals were not examined. Their missing retention is an evidence limit, not unresolved H4684/L4684 identity.

## Evidence limits and open work

Full TiDisplay Color software manual, exact reset procedure, hardware/microcontroller identities and installed per-firmware diagnostic/function behavior remain missing.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

A historical Legrand Netherlands legacy-software page was discovered listing TiDisplayColor and TiDisplayColorIP editions, but its linked edition-specific user/software manuals were not retained or examined. Hardware/software edition matching, detailed menu procedures and transfer compatibility across the four catalogue firmware tuples remain limited to the exact sheets and canonical associations. The sheets' RS232/USB adapter wording and LAN/USB-miniUSB diagrams do not prove identical ports on every production unit.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0131-0140-2026-10-06.md#own-dev-0135)
