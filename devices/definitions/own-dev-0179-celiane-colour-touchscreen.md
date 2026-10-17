# Céliane colour touchscreen

## Summary

067283 is a Céliane 3.5-inch colour touchscreen for central MyHOME control. Its icon interface operates lighting, shutters, scenarios, temperature, alarm and sound, including documented network multimedia functions. The exact sheet identifies a network connector and ColorTouchConfigIP commissioning.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0179` | Project identity |
| Technical description | Céliane colour touchscreen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `067283` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1516` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `46` | Main association; independent of project ID |
| Firmware definition | `88`, `89` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Céliane | `067283` | Established catalogue identity | Manufacturer database commercial record `1516` explicitly links this SKU to item `1516` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `067283` | Colour Touch Screen | Canonical commercial record `1516` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `celiane-pilotage-historical-guide.pdf` | Historical exact-product manufacturer source | celiane-pilotage-historical-guide; printed publication date not established | 067283: exact wiring examples printed pp. 364, 366 / PDF pp. 28, 30; general integration pp. 338-349 / PDF pp. 2-13. Broader system examples do not establish unsupported firmware features. | [Archived original](https://archive.openwebnet-ha.org/sha256/7a/aa/7aaa46e456b413201dfe6f5115df3e14069ac05de1cfca4e59bc66eeba057f4c.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-fr/pfat/ca/principe_de_mise_en_oeuvre_pilotage.pdf) |
| `celiane-067283-historical-sheet.pdf` | Historical exact manufacturer documentation | celiane-067283-historical-sheet; printed publication date not established | 067283 / 672 83: printed pp. 605-606 / PDF pp. 1-2; exact supply, draw, mounting, interfaces and configuration. French text prints LG00160-a-UK. | [Archived original](https://archive.openwebnet-ha.org/sha256/21/ef/21ef653b8d09964881e88aafc4295c8443b7b35da73591f71321a7b55ed390f5.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-fr/pfat/gm/fiche%20technique%20067283.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1516`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |
| Current draw | `80 mA` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |
| Temperature | `0..40 °C` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |
| Display | `3.5-inch backlit colour; LED technology in legend` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |
| Mounting | `2+3 flush-mounted modules, exact sheet wording` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |
| Interfaces | `RJ45 network; SCS BUS; mini-USB` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |
| PC connection / software | `49234 USB interface; ColorTouchConfigIP` | `celiane-067283-historical-sheet` printed pp. 605-606 / PDF pp. 1-2; `celiane-pilotage-historical-guide` printed pp. 364, 366 / PDF pp. 28, 30 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1516` | Canonical catalogue |
| Technical item description | Colour Touch Screen | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `46` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `46` | Yes | Canonical item/system relationship |

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
| `88` | `6` | `0` | `1` | `1` | Catalogue default | Official |
| `89` | `5` | `0` | `9` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `88` | `122` | Legrand (key `2`) | `0` | external software | `ColorTouchConfigIP_0601` |
| `88` | `354` | Legrand (key `2`) | `4` | external software | `ColorTouchConfigIP_0601` |
| `89` | `123` | Legrand (key `2`) | `0` | external software | `ColorTouchConfigIP_0500` |
| `89` | `355` | Legrand (key `2`) | `4` | external software | `ColorTouchConfigIP_0500` |

All 4 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `88` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1319` | `32` | `679` |
| `89` | `1` | `32` Colors Touch Screen | Fixed / designated metadata | `1320` | `32` | `680` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `88` | Product Programming | `3` | Canonical firmware/mode association |
| `89` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `88` | Ethernet | Canonical firmware/connection association |
| `88` | USB | Canonical firmware/connection association |
| `89` | Ethernet | Canonical firmware/connection association |
| `89` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Catalogue programming routes` | Use each exact Firmware association and connection label above; no modality inferred from a bare mode ID | Exact source scope in Documentation; canonical catalogue tables below |
| `Physical selector map` | No complete exact-product physical selector map established by retained originals; reusable Object fields remain separate | Exact source scope in Documentation; canonical catalogue tables below |
| `ColorTouchConfigIP` | Assign icons, logic / time conditions, timed activations, date / time and password protection; software update | `celiane-067283-historical-sheet` printed pp. 605-606 /PDF pp. 1-2 |
| `49234 / RJ45` | Published USB configuration interface / network connector; not inferred from BTicino sibling software | `celiane-067283-historical-sheet` printed pp. 605-606 /PDF pp. 1-2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `88` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `88` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `88` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `88` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `89` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `89` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `89` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `89` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `46` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

ColorTouchConfigIP associates icons with configured automation, sound, alarm and temperature functions, allows logic / time conditions and timed activations, sets time / date / protection and updates software. Use the 49234 PC interface shown in the exact sheet. Network multimedia content depends on the appropriate installed network / sound topology; the retained guide’s exact `67283` examples show automation/temperature integration and automation/temperature/alarm integration, without establishing a particular multimedia adapter. Catalogue Firmware `88`/89 and UI restrictions remain independent of the nominal display-control functions.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

Reusable Object `32` stores `FW_VER=3.0.0` and the item-level field repeats it even where the firmware-definition table identifies a different release. This is a configuration-field default, not proof that any listed or installed firmware is version `3.0.0`. Its `LAN_IP_ADDRESS=192.168.1.35` is a public manufacturer-catalogue documentation default, not an observed installation address. `SYSADDRESS` is a separate device code (default `1`); the six-character mask does not establish its character set or an SCS physical configurator. One local UI Object does not instantiate the remote lighting, shutter, alarm, temperature or sound Objects it may control.

The exact French sheet names 672 83, corresponding to database 067283, and prints LG00160-a-UK despite its French text. Its 2+3-module mounting label is preserved rather than replaced by the BTicino 3+3-module label from a different reference. ColorTouchConfigIP is the stated Legrand software, not inferred to be TiDisplay Color. Shared integration-guide diagrams establish a configured system example but do not guarantee all related firmware / media-server combinations. Newer 067292 and the larger 067285 are different references.


The retained guide’s printed p. 364 / PDF p. 28 names `67283` in an automation/temperature example; printed p. 366 / PDF p. 30 adds alarm activation, deactivation and partitioning with the configured alarm central and BUS/BUS gateway. Those are installation examples, not a capture of this screen’s diagnostic or media-server support. The previous reference to adapter `574044` is removed because it is not established by the cited exact-product sheet or retained guide. The sheet itself establishes access to network multimedia content but does not specify the corresponding adapter, protocols or media formats. Its “LED technology” legend is preserved as publisher terminology, rather than recast as an independently proven OLED/LCD panel type.

## Evidence limits and open work

An exact user manual, software executable / version applicability, supported network / media server formats and retained EAN remain gaps. Display / network and diagnostic runtime behavior remains uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further product-source discovery and runtime corroboration remain open.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0171-0180-2026-10-07.md#own-dev-0179)
