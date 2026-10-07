# Matix colour touchscreen

## Summary

AM5864 is a Matix colour touchscreen for central control of configured MyHOME functions. Its backlit icon interface operates lighting, shutters, scenarios, temperature, sound and other supported system functions. TiDisplay Color defines the pages and associates icons with the installed system.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0175` | Project identity |
| Technical description | Matix colour touchscreen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `AM5864` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1510` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `36` | Main association; independent of project ID |
| Firmware definition | `80`, `81`, `82`, `83` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Matix | `AM5864` | Established catalogue identity | Manufacturer database commercial record `1510` explicitly links this SKU to item `1510` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `AM5864` | Colour Touch Screen | Canonical commercial record `1510` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00287-a-EN.pdf` | Exact manufacturer documentation | Printed BT00287-a-UK; filename BT00287-a-EN; date not established | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/20/31/20315182f949ce1ad7be68bbe4955e4189b26161fe881fab599d2cae15959f0a.pdf) | [Publisher original](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileId=58107.23188.48069.54823&fileName=BT00287-a-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1510`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |
| Current draw | `80 mA` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |
| Temperature | `0..40 °C` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |
| Mounting | `3+3 flush-mounted wiring-device modules; box 506E` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |
| Display | `backlit colour touchscreen` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |
| PC interfaces | `335919 RS232, 3559 USB, Ethernet` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |
| Software | `TiDisplay Color` | `BT00287-a-EN` printed code BT00287-a-UK, printed/PDF pp. 1-2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1510` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `36` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `36` | Yes | Canonical item/system relationship |

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
| `80` | `6` | `0` | `8` | `1` | Catalogue default | Official |
| `81` | `5` | `0` | `0` | `1` | Not catalogue default | Official |
| `82` | `4` | `1` | `19` | `1` | Not catalogue default | Official |
| `83` | `1` | `0` | `0` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `80` | `56` | BTicino (key `1`) | `2` | external software | `TiDisplayColorIP_0601` |
| `81` | `98` | BTicino (key `1`) | `2` | external software | `TiDisplayColorIP_0500` |
| `82` | `99` | BTicino (key `1`) | `2` | external software | `TiDisplayColorIP_0400` |
| `83` | `101` | BTicino (key `1`) | `2` | external software | `TiDisplayColorIP_0101` |

All 4 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `80` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1315` | `32` | `675` |
| `81` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1316` | `32` | `676` |
| `82` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1317` | `32` | `677` |
| `83` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1318` | `32` | `678` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `80` | Product Programming | `3` | Canonical firmware/mode association |
| `81` | Product Programming | `3` | Canonical firmware/mode association |
| `82` | Product Programming | `3` | Canonical firmware/mode association |
| `83` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `80` | Ethernet | Canonical firmware/connection association |
| `80` | USB | Canonical firmware/connection association |
| `81` | Ethernet | Canonical firmware/connection association |
| `81` | USB | Canonical firmware/connection association |
| `82` | Ethernet | Canonical firmware/connection association |
| `82` | USB | Canonical firmware/connection association |
| `83` | Ethernet | Canonical firmware/connection association |
| `83` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Catalogue programming routes` | Use each exact Firmware association and connection label above; no modality inferred from a bare mode ID | Exact source scope in Documentation; canonical catalogue tables below |
| `Physical selector map` | No complete exact-product physical selector map established by retained originals; reusable Object fields remain separate | Exact source scope in Documentation; canonical catalogue tables below |
| `TiDisplay Color project` | Configure icons, system-function references, logic / time scenarios, activations, clock and access protection | `BT00287-a-EN` printed/PDF pp. 1-2 |
| `Transfer / update` | RS232335919, USB3559 or Ethernet; software configuration and updating documented for namedAM5864 | `BT00287-a-EN` printed/PDF pp. 1-2 |

The exact AM5864 sheet names a historical RS232 interface `335919` in addition to USB `3559` and Ethernet (printed/PDF p. 2). The canonical firmware/connection associations contain only USB and Ethernet. Preserve RS232 as the sheet’s interface-cable workflow; do not add an unsupported direct catalogue connection association.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `80` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `80` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `80` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `80` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `81` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `81` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `81` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `81` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `82` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `82` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `82` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `82` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `83` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `83` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `83` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `83` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `36` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Create or modify the project in TiDisplay Color, assigning available icons to configured automation, energy, sound, alarm and temperature functions. Transfer uses the stated interface cable or Ethernet. The software can define logic / time scenarios, activations, time / date, access protection and firmware updates. These UI functions control remote system devices; one local UI Object is not a local actuator / thermostat for each icon. Apply the four exact Firmware definitions and their field / filter applicability separately.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

Reusable Object `32` stores `FW_VER=3.0.0` and the item-level field repeats it even where the firmware-definition table identifies a different release. This is a configuration-field default, not proof that any listed or installed firmware is version `3.0.0`. Its `LAN_IP_ADDRESS=192.168.1.35` is a public manufacturer-catalogue documentation default, not an observed installation address. `SYSADDRESS` is a separate device code (default `1`); the six-character mask does not establish its character set or an SCS physical configurator. One local UI Object does not instantiate the remote lighting, shutter, alarm, temperature or sound Objects it may control.

The archived English sheet explicitly co-lists AM5864 with H4684 and L4684, making it exact evidence for this Matix item. Its filename ends EN while its printed identifier ends UK; both are preserved. The explicit database commercial relationship establishes AM5864 independently of related touchscreens. The current product lookup and export attempts did not return an exact current page; that is a documentation gap, not a weakened identity.


## Evidence limits and open work

An exact user / software manual for the retained AM5864 generation, current EAN, multimedia accessory compatibility and measured runtime support remain gaps.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further product-source discovery and runtime corroboration remain open.

`U1881D` (printed 11/08-01 PC in a discovery mirror) names H/L4684 and AM5864, but fresh `dar.bticino.com` and `dar.bticino.it` original retrieval attempts returned HTTP 403 on 7 October. Its unretained text is not used to extend this sheet’s functions or establish per-release menu applicability. AM5890 successor instructions and EANs are not assigned to AM5864.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0171-0180-2026-10-07.md#own-dev-0175)
