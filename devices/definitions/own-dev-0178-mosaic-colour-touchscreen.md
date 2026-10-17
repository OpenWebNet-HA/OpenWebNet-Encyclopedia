# Mosaic colour touchscreen

## Summary

`078474` is a Mosaic colour touchscreen for central lighting and blind control. Its historical Legrand catalogue describes local, zone and timed control, plus locking functions and lighting switching or dimming. It is completed with a separate white or aluminium Mosaic plate.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0178` | Project identity |
| Technical description | Mosaic colour touchscreen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `078474` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1515` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `47` | Main association; independent of project ID |
| Firmware definition | `86`, `87` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Mosaic | `078474` | Established catalogue identity | Manufacturer database commercial record `1515` explicitly links this SKU to item `1515` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `078474` | Colour Touch Screen | Canonical commercial record `1515` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `Mosaic-historical-catalogue-excerpt.pdf` | Manufacturer original | Historical English excerpt; publication date not established | Printed p. 801 / PDF p. 10: exact 78474 product, colour interface, lighting/blind control scopes and plates. Manufacturer-authored 22-page excerpt retained from distributor Chipdip; other entries are separate products. | [Archived original](https://archive.openwebnet-ha.org/sha256/43/f4/43f43160656eb3a6841197c032e3fb20c4acd4ca58f32a1e4001ca465afc09af.pdf) | [Distributor-hosted original](https://static.chipdip.ru/lib/818/DOC035818437.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1515`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | Colour touchscreen; diagonal and pixel resolution not specified in this entry | Mosaic catalogue printed p. 801 / PDF p. 10 |
| Finishing plates | White `78470` or aluminium `79174`; both are separate accessories | Mosaic catalogue printed p. 801 / PDF p. 10 |
| Electrical / enclosure ratings | Not established by the retained exact-product catalogue entry | Mosaic catalogue printed p. 801 / PDF p. 10 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1515` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `47` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `47` | Yes | Canonical item/system relationship |

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
| `86` | `6` | `0` | `1` | `1` | Catalogue default | Official |
| `87` | `5` | `0` | `9` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `86` | `122` | Legrand (key `2`) | `0` | external software | `ColorTouchConfigIP_0601` |
| `86` | `352` | Legrand (key `2`) | `3` | external software | `ColorTouchConfigIP_0601` |
| `87` | `123` | Legrand (key `2`) | `0` | external software | `ColorTouchConfigIP_0500` |
| `87` | `353` | Legrand (key `2`) | `3` | external software | `ColorTouchConfigIP_0500` |

All 4 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `86` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1325` | `32` | `685` |
| `87` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1326` | `32` | `686` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `86` | Product Programming | `3` | Canonical firmware/mode association |
| `87` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `86` | Ethernet | Canonical firmware/connection association |
| `86` | USB | Canonical firmware/connection association |
| `87` | Ethernet | Canonical firmware/connection association |
| `87` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

| Function | Published capability | Evidence |
| --- | --- | --- |
| Lighting / blinds | Local, zone and time-delayed control; locking functions | Mosaic catalogue printed p. 801 / PDF p. 10 |
| Lighting operation | ON/OFF and/or dimming through the system | Mosaic catalogue printed p. 801 / PDF p. 10 |
| Software / transfer | Catalogue-associated ColorTouchConfigIP, USB and Ethernet; exact product-entry procedure not given | Canonical Firmware `86`/87 associations |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `86` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `86` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `86` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `86` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `87` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `87` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `87` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `87` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |

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
| `DIMENSION 1` | Corroborate item model `47` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

The exact catalogue entry documents local, zone and time-delayed control of lighting and blinds, locking functions, and lighting ON/OFF or dimming. It describes a configurable colour interface but does not specify the PC software or a commissioning sequence (printed p. 801 / PDF p. 10). The canonical Firmware `86`/`87` tables independently register ColorTouchConfigIP parameter paths and Ethernet/USB routes; their payloads remain unexamined. Neighbouring scenario switches refer to `03551`, but that row is not an instruction to program 78474 without software. Remote control roles do not establish physical load-switching ratings or additional local actuator Objects.

## Source reconciliation

Reusable Object `32` stores `FW_VER=3.0.0` and the item-level field repeats it even where the firmware-definition table identifies a different release. This is a configuration-field default, not proof that any listed or installed firmware is version `3.0.0`. Its `LAN_IP_ADDRESS=192.168.1.35` is a public manufacturer-catalogue documentation default, not an observed installation address. `SYSADDRESS` is a separate device code (default `1`); the six-character mask does not establish its character set or an SCS physical configurator. One local UI Object does not instantiate the remote lighting, shutter, alarm, temperature or sound Objects it may control.

The explicit manufacturer database relation establishes 078474 without a device-specific PDF. A retained Legrand catalogue excerpt explicitly identifies `784 74` as the colour touchscreen, corresponding to database `078474`. Retailer EAN and specification claims are not promoted as retained manufacturer evidence. The differently referenced 078479 and finishing plates remain excluded technical identities.

The manufacturer-authored catalogue PDF is retained intact from distributor Chipdip. The distributor hosts the original PDF bytes; it is not a manufacturer-hosted response, and the original publication date and publisher download URL remain unestablished. The examined exact-product entry is printed p. 801 / PDF p. 10.

The exact entry separates touchscreen `78474` from white plate `78470` and aluminium plate `79174`. Its broad “all relays” wording concerns configurable system control, not load contacts inside the screen. The neighbouring telephone sockets’ `10/100 Mbps` and `35 mm` mounting depth are separate product facts and are excluded. No alarm, temperature, sound, diagonal or Ethernet-speed specification is inferred for 078474 from adjacent rows or Céliane/BTicino screens.

## Evidence limits and open work

The retained historical catalogue resolves the exact product role and finishing plates. A complete 078474/78474 technical sheet and user/software manual, electrical ratings, display diagonal/resolution, mounting dimensions and manufacturer EAN remain gaps. Installed configuration and diagnostics remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further product-source discovery and runtime corroboration remain open.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0171-0180-2026-10-07.md#own-dev-0178)
