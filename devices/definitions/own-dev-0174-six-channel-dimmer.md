# Six-channel dimmer

## Summary

The manufacturer catalogue identifies 002627 as a six-channel lighting dimmer. Its Firmware declares six Modules using dimmer Objects, with separate channel addressing and configuration surfaces. A product-specific original is still needed to establish its electrical ratings and local controls.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0174` | Project identity |
| Technical description | Six-channel dimmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `002627` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1493` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `142` | Main association; independent of project ID |
| Firmware definition | `219` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `6` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `002627` | Established catalogue identity | Manufacturer database commercial record `1493` explicitly links this SKU to item `1493` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `002627` | 6 channel dimmer | Canonical commercial record `1493` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1493`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue channel role | `6 declared Modules; reusable dimmer Object 8` | Canonical `MHCatalogue.db`, item `1493`, Firmware `219` |
| Electrical ratings / physical construction | `not established by a retained exact-product original` | Canonical `MHCatalogue.db`, item `1493`, Firmware `219` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1493` | Canonical catalogue |
| Technical item description | 6 channel dimmer | Canonical catalogue |
| Item family | Source placeholder description `0`; key `4` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `142` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `142` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `219` | `-1` | `-1` | `-1` | `6` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `219` | `1` | `8` Dimmer actuator | Fixed / designated metadata | `999` | `8` | `604` |
| `219` | `2` | `8` Dimmer actuator | Fixed / designated metadata | `1000` | `8` | `604` |
| `219` | `3` | `8` Dimmer actuator | Fixed / designated metadata | `1001` | `8` | `604` |
| `219` | `4` | `8` Dimmer actuator | Fixed / designated metadata | `1002` | `8` | `604` |
| `219` | `5` | `8` Dimmer actuator | Fixed / designated metadata | `1003` | `8` | `604` |
| `219` | `6` | `8` Dimmer actuator | Fixed / designated metadata | `1004` | `8` | `604` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `219` | Physical configuration | `0` | Canonical firmware/mode association |
| `219` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `219` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
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
| `219` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `219` | `A` | `0..9` | `0` | A; Enviroment |
| `219` | `G` | `0..9` | `0` | G (0-9) |
| `219` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M, S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `219` | `1` | `8` | `4956` | No textual predicate stored | `7206` |
| `219` | `2` | `8` | `4937` | No textual predicate stored | `7207` |
| `219` | `3` | `8` | `4938` | No textual predicate stored | `7208` |
| `219` | `4` | `8` | `4957` | No textual predicate stored | `7209` |
| `219` | `5` | `8` | `4958` | No textual predicate stored | `7210` |
| `219` | `6` | `8` | `4959` | No textual predicate stored | `7211` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `219` | `8` | `2063` | `LOCAL_BUTTON` | `15` = Pushbutton; `18` = Timed `ON`; `9` = `ON` - `OFF` | `0` | Local button modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `219` | `8` | `2064` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `219` | `8` | `2065` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `219` | `8` | `2066` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `219` | `8` | `2067` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `9` = DSI | `0` | Type of load |
| `219` | `8` | `2068` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `219` | `8` | `2069` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `219` | `8` | `2070` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `219` | `8` | `2190` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7206` | `A=0` | `PL` = `0` | `7206` |
| `7206` | `A=1` | `PL` = `1` | `7206` |
| `7206` | `A=2` | `PL` = `1` | `7206` |
| `7206` | `A=3` | `PL` = `1` | `7206` |
| `7206` | `A=4` | `PL` = `1` | `7206` |
| `7206` | `A=5` | `PL` = `1` | `7206` |
| `7206` | `A=6` | `PL` = `1` | `7206` |
| `7206` | `A=7` | `PL` = `1` | `7206` |
| `7206` | `A=8` | `PL` = `1` | `7206` |
| `7206` | `A=9` | `PL` = `1` | `7206` |
| `7207` | `A=0` | `PL` = `0` | `7207` |
| `7207` | `A=1` | `PL` = `2` | `7207` |
| `7207` | `A=2` | `PL` = `2` | `7207` |
| `7207` | `A=3` | `PL` = `2` | `7207` |
| `7207` | `A=4` | `PL` = `2` | `7207` |
| `7207` | `A=5` | `PL` = `2` | `7207` |
| `7207` | `A=6` | `PL` = `2` | `7207` |
| `7207` | `A=7` | `PL` = `2` | `7207` |
| `7207` | `A=8` | `PL` = `2` | `7207` |
| `7207` | `A=9` | `PL` = `2` | `7207` |
| `7208` | `A=0` | `PL` = `0` | `7208` |
| `7208` | `A=1` | `PL` = `3` | `7208` |
| `7208` | `A=2` | `PL` = `3` | `7208` |
| `7208` | `A=3` | `PL` = `3` | `7208` |
| `7208` | `A=4` | `PL` = `3` | `7208` |
| `7208` | `A=5` | `PL` = `3` | `7208` |
| `7208` | `A=6` | `PL` = `3` | `7208` |
| `7208` | `A=7` | `PL` = `3` | `7208` |
| `7208` | `A=8` | `PL` = `3` | `7208` |
| `7208` | `A=9` | `PL` = `3` | `7208` |
| `7209` | `A=0` | `PL` = `0` | `7209` |
| `7209` | `A=1` | `PL` = `4` | `7209` |
| `7209` | `A=2` | `PL` = `4` | `7209` |
| `7209` | `A=3` | `PL` = `4` | `7209` |
| `7209` | `A=4` | `PL` = `4` | `7209` |
| `7209` | `A=5` | `PL` = `4` | `7209` |
| `7209` | `A=6` | `PL` = `4` | `7209` |
| `7209` | `A=7` | `PL` = `4` | `7209` |
| `7209` | `A=8` | `PL` = `4` | `7209` |
| `7209` | `A=9` | `PL` = `4` | `7209` |
| `7210` | `A=0` | `PL` = `0` | `7210` |
| `7210` | `A=1` | `PL` = `5` | `7210` |
| `7210` | `A=2` | `PL` = `5` | `7210` |
| `7210` | `A=3` | `PL` = `5` | `7210` |
| `7210` | `A=4` | `PL` = `5` | `7210` |
| `7210` | `A=5` | `PL` = `5` | `7210` |
| `7210` | `A=6` | `PL` = `5` | `7210` |
| `7210` | `A=7` | `PL` = `5` | `7210` |
| `7210` | `A=8` | `PL` = `5` | `7210` |
| `7210` | `A=9` | `PL` = `5` | `7210` |
| `7211` | `A=0` | `PL` = `0` | `7211` |
| `7211` | `A=1` | `PL` = `6` | `7211` |
| `7211` | `A=2` | `PL` = `6` | `7211` |
| `7211` | `A=3` | `PL` = `6` | `7211` |
| `7211` | `A=4` | `PL` = `6` | `7211` |
| `7211` | `A=5` | `PL` = `6` | `7211` |
| `7211` | `A=6` | `PL` = `6` | `7211` |
| `7211` | `A=7` | `PL` = `6` | `7211` |
| `7211` | `A=8` | `PL` = `6` | `7211` |
| `7211` | `A=9` | `PL` = `6` | `7211` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `142` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `8` - Dimmer actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `8` - Dimmer actuator | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `8` | [Lighting](../../functional/who-1-lighting/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Resolve the six channel placements and their conditions using the Firmware-specific catalogue tables. The dimmer Object defines address, minimum-level and operating surfaces; reusable legal values do not establish a physical selector, supported load class or leading / trailing-edge hardware. A historical manufacturer-authored sheet appears in a discovery mirror under 02627, but its original could not be retained from the official routes attempted. Its electrical / procedural claims remain pending verification of the original.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

Firmware `219` has six fixed/designated placements for reusable Object `8`, with condition records `4956`, `4937`, `4938`, `4957`, `4958`, `4959`. Each stores no textual predicate, but references one of conversions `7206..7211`; the blank predicate is not an unconditional-activation claim. For item `A=0`, each conversion sets Object `PL=0`; for `A=1..9`, channel slots 1 through 6 yield `PL=1..6` respectively. These rows specify catalogue addressing, not six verified wired load outputs or a measured response.

Filter `2063` excludes reusable `LOCAL_BUTTON=0`; it admits `9`, `15`, `18` without storing a replacement default. Independently, `MIN_LEVEL_ADV` has reusable/default `0` outside its own `1..100` domain, and filter `2069` retains that full domain without repairing the default. Filter `2067` omits `TYPE_LOAD=8` (DALI) while retaining DSI and other reusable labels. Neither the retained labels nor `TYPE_STANDARD` establish hardware ballast outputs or load ratings. Item `M=0..4,11,15` differs from reusable Object `M=0,11,15,16`; no Object conversion for that mode field is referenced here.

002627 is explicitly linked to item 1493 in the manufacturer database, so its identity is established. Discovery found a mirrored 02627 technical-sheet transcript; attempted Legrand Australia locations returned 403 and no exact current product page was found. Related 002622/002671 dimmers have different outputs and are excluded. No electrical ratings are inferred from their similar references or from the six-Module count.

No exact-product document original is retained for this item. The canonical database is the source for the identity and configuration inventory; product-document discovery remains partial.

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

## Evidence limits and open work

Retain and inspect the original 02627/002627 sheet, including load classes, per-channel and aggregate ratings, local edge-mode programming, wiring and production applicability. EAN and observed diagnostics remain unavailable in retained evidence.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further product-source discovery and runtime corroboration remain open.

The 7 October retry of the [Legrand Australia technical-sheet route](https://www.legrand.com.au/sites/default/files/02627_SCS%206%20Channel%20Dimmer_Technical%20sheet.pdf) returned HTTP 403; the [discovery transcript](https://studyres.com/doc/7813220/02627_scs-6-channel-dimmer_technical-sheet) remains a lead rather than a retained exact-product original. Its claimed `300 VA` per-channel rating and edge-mode procedure are not adopted as verified Device facts. Searches for `002627`, `02627` and the six-channel SCS description found no usable official replacement original. The archival check covers the registered canonical database; no product PDF is represented as archived.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0171-0180-2026-10-07.md#own-dev-0174)
