# Burglar alarm central unit with communicator

## Summary

This alarm central unit combines burglar-alarm control with a PSTN telephone communicator. Manufacturer catalogue text describes alarm calls, telephone status checks and remote home-system functions, with Ademco Contact ID integration; the retained evidence does not establish a complete local-menu specification for this exact 3485 reference.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0085` | Project identity |
| Technical description | Burglar alarm central unit with communicator | Canonical catalogue |
| Commercial identities | `3485` | Canonical commercial records |
| Catalogue item | `139` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `198` | Canonical inventory |
| Firmware definition | `8.0.0`; `6.0.0`; `7.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Pivot | `3485` | Established catalogue identity | canonical commercial record for item `139` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| BTicino/Legrand residential catalogue | product catalogue | historical publisher catalogue | 3485 phone/Contact ID role: printed p. 187 / PDF p. 189; battery 3506 compatibility printed p. 195 / PDF p. 197; do not alias `3485STD` | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | [Official source](https://assets.legrand.com/webf/ch/ch_de_katalog_wohnbau.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Physical role | PSTN alarm control unit; enclosure/electrical ratings not established by retained exact-reference evidence | Canonical item 139 / Object `13`; Swiss guide printed p. 187 / PDF p. 189 |
| Backup battery compatibility | 3506, 7.2 V; source names 3485 and `3485STD` | Swiss guide printed p. 195 / PDF p. 197; capacity/chemistry not specified |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `139` | Canonical catalogue |
| Technical item | Burglar alarm central unit with communicator | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `198` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Burglar alarm system | `198` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Burglar alarm | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `139` | `3485` | `1` | `9` | `BTicino_Pivot_Burglar alarm central unit with` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `139` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `8` | `0` | `0` | `1` | Catalogue default | Official |
| `16` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `17` | `7` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `15` | `59` | BTicino (key `1`) | `6` | external software | `TiSecurityPolyx_0300` |
| `16` | `106` | BTicino (key `1`) | `6` | external software | `TiSecurityPolyx_0100` |
| `17` | `105` | BTicino (key `1`) | `6` | external software | `TiSecurityPolyx_0200` |

All 3 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2272` | `13` | `950` |
| `16` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2275` | `13` | `953` |
| `17` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2274` | `13` | `952` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `15` | Product Programming | `3` | Canonical firmware/mode association |
| `16` | Product Programming | `3` | Canonical firmware/mode association |
| `17` | Product Programming | `3` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `15` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `16` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `17` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `13` - AI Control Unit With Communicator Pstn

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `FW_VER` | No legal values specified in source | Not specified in source | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |

### Device-specific interpretation

Three Official catalogue firmware definitions apply: `15`=8.0.0 (default), `16`=6.0.0, `17`=7.0.0, each one Module with PSTN Object `13`. Only AID is firmware-scoped. Reusable `FW_VER` and NUM_PSTN have no catalogue domain/default; `IS_GATEWAY` is a separate boolean default `0`, not evidence of an Ethernet gateway. No Virgin, condition, filter or conversion is associated. Product Programming `3` is stored for each firmware; no connection row is stored. Parameter records `59/106/105` have brand `1`, line `6`, independently of commercial line `9`. No payload or installed firmware is inferred from their paths.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `139` / `modobj = 198` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`13`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `13` AI Control Unit With Communicator Pstn | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `13` AI Control Unit With Communicator Pstn | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Telephone integration | Bidirectional alarm notification, system-state checking and remote functions | Swiss guide printed p. 187 / PDF p. 189; prose names 3485 and 3486 |
| Monitoring centre | Ademco Contact ID communication | Same exact-reference prose |
| Catalogue capability | PSTN Object `13`, one Module, three firmware definitions | Canonical source; not a complete physical menu specification |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Product Programming `3` is associated with each of the three catalogue firmware records. The retained manufacturer guide establishes telephone integration and battery compatibility, but does not provide a complete 3485 commissioning, transfer, reset or update sequence. No 3486 or `3485B` procedure is prescribed for this item. The parameter-file association paths below are catalogue data; their payloads have not been examined.

## Source reconciliation

The Swiss prose explicitly names 3485 for telephone/Contact ID functions and its battery table explicitly names 3485 with 3506. The facing selection table instead names `3485STD` for eight zones/72 detectors. That does not independently establish the same numeric limits for catalogue 3485. `3485B` is a separate four-zone technical item; the shared software-manual diagram label ART.3485 does not merge those identities. Attempts to obtain a dedicated primary 3485 installation manual from candidate manufacturer endpoints did not return a usable original. Generic product-page navigation and third-party manual discovery are not retained product specifications.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Obtain a directly applicable 3485 manual/technical sheet for enclosure, supply/current, zone limits, menus and programming.
- Examine referenced parameter payloads and firmware-specific revision changes if originals become available.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0085)
