# LivingLight Air colour touchscreen

## Summary

LN4684A is the LivingLight Air colour touchscreen variant for central MyHOME control. Its historical manufacturer catalogue describes lighting, shutters, alarm, temperature, sound, scenarios and energy management through the touch interface. The Air variant fits the corresponding LivingLight Air plates.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0176` | Project identity |
| Technical description | LivingLight Air colour touchscreen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `LN4684A` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1511` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `50` | Main association; independent of project ID |
| Firmware definition | `84` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight Air | `LN4684A` | Established catalogue identity | Manufacturer database commercial record `1511` explicitly links this SKU to item `1511` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `LN4684A` | Colour Touch Screen | Canonical commercial record `1511` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `livinglight-historical-catalogue.pdf` | Historical exact-product manufacturer source | Page 66 footer 12/01/12 13:28; catalogue-wide publication date not established | LN4684A: printed p. 66 / PDF p. 68; exact commercial and functional description. Other products and successor sheets do not establish its ratings. | [Archived original](https://archive.openwebnet-ha.org/sha256/db/75/db75d0071e27ea0904973b8ebaa936334347e3646135884b7b7081e110a3f414.pdf) | [Publisher original](https://www.bticino.es/pdf/livinglight.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1511`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `3.5-inch colour touchscreen, historical product inventory` | `livinglight-historical-catalogue` printed p. 66 / PDF p. 68 |
| Installation line | `LivingLight Air plates; catalogue explicitly identifies LN4684A` | `livinglight-historical-catalogue` printed p. 66 / PDF p. 68 |
| Electrical ratings | `not stated for LN4684A in the retained exact-reference catalogue entry` | `livinglight-historical-catalogue` printed p. 66 / PDF p. 68 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1511` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `50` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `50` | Yes | Canonical item/system relationship |

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
| `84` | `6` | `0` | `8` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `84` | `56` | BTicino (key `1`) | `0` | external software | `TiDisplayColorIP_0601` |
| `84` | `359` | BTicino (key `1`) | `1` | external software | `TiDisplayColorIP_0601` |

All 2 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `84` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1314` | `32` | `674` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `84` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `84` | Ethernet | Canonical firmware/connection association |
| `84` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

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
| `84` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `84` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `84` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `84` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `50` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Use the exact catalogue Firmware `84` and colour-touchscreen Object configuration inventory below. The historical catalogue identifies LN4684A as the Air version of the listed touch interface; this establishes a documented role but does not reproduce its standalone commissioning manual. Newer LN4890A is explicitly marketed as a replacement, which does not establish identical firmware, wiring, consumption or every feature for LN4684A.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact `LN4684A` entry says “touchscreen as above”, referring to `L4684`’s `3.5-inch` colour display and enumerated system-control roles on the same printed p. 66 / PDF p. 68. That explicit cross-reference supports the stated display/roles; it does not import the separately retained AM5864 sheet’s `80 mA`, box `506E` or RS232 cable. Page 66’s dated production footer is source metadata, rather than a proven release date for the entire catalogue. The catalogue’s “L/N/NT” line grouping is not a marketed variant name; Air is established by the exact entry.

Reusable Object `32` stores `FW_VER=3.0.0` and the item-level field repeats it even where the firmware-definition table identifies a different release. This is a configuration-field default, not proof that any listed or installed firmware is version `3.0.0`. Its `LAN_IP_ADDRESS=192.168.1.35` is a public manufacturer-catalogue documentation default, not an observed installation address. `SYSADDRESS` is a separate device code (default `1`); the six-character mask does not establish its character set or an SCS physical configurator. One local UI Object does not instantiate the remote lighting, shutter, alarm, temperature or sound Objects it may control.

The database’s L/N/NT grouping is presented as marketed LivingLight Air using the exact historical entry. The Spanish catalogue names LN4684A and the applicable system functions. Its neighbouring L4684 and 3496 entries are separate references; the shared listing does not directly rate LN4684A or guarantee multimedia accessory compatibility for its production revision. No replacement-product EAN or rating is imported.


## Evidence limits and open work

A retained exact LN4684A technical / installation / software manual, electrical and dimensional specifications, EAN and hardware diagnostics remain documentation / corroboration gaps; identity is established.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further product-source discovery and runtime corroboration remain open.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0171-0180-2026-10-07.md#own-dev-0176)
