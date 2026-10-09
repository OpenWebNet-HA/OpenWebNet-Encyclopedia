# Burglar alarm central unit with communicator

## Summary

This Legrand burglar-alarm central unit combines alarm control with a PSTN telephone communicator. Céliane 067510 and Galea 775795 are established catalogue identities, with two recorded firmware builds; detailed zone capacity and telephone workflows remain gaps in exact-product documentation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0095` | Project identity |
| Technical description | Burglar alarm central unit with communicator | Canonical catalogue |
| Commercial identities | `067510`, `775795` | Canonical commercial records |
| Catalogue item | `975` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `201` | Canonical inventory |
| Firmware definition | `6.0.20`; `7.0.17` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Céliane | `067510` | Established catalogue identity | canonical commercial record for item `975` |
| Legrand - Galea | `775795` | Established catalogue identity | canonical commercial record for item `975` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `Legrand-TR-256-291.pdf` | Regional manufacturer catalogue · TR | Printed issue date not stated in examined leaf; retrieved 2026-10-06 | Only printed p. 274 / PDF p. 19: USB cable 49234 explicitly for central unit 67510; preceding 67520 panel ratings excluded; other catalogue leaves unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/8d/d4/8dd46231dc38ff1b76e37443f29b3521ebaf446e1dfcf27238cbf00905a864f0.pdf) | [Publisher source](https://www.legrand.com.tr/pdf/katalog-sayfa/256-291.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Hardware / electrical limits | Not established by retained exact panel documentation | Catalogue Serial connection is software metadata, not a physical connector rating |
| Programming accessory | Regional catalogue explicitly lists USB cable 49234 for central unit 67510 | Legrand Turkish catalogue, printed p. 274 / PDF p. 19; 67510 is the unpadded regional reference |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `975` | Canonical catalogue |
| Technical item | Burglar alarm central unit with communicator | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `201` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Burglar alarm system | `201` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Burglar alarm | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `974` | `067510` | `2` | `13` | Empty in source |
| `975` | `775795` | `2` | `14` | Empty in source |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `974` | `1` | `0` | `0` | Empty in source |
| `975` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `106` | `6` | `0` | `20` | `1` | Not catalogue default | Official |
| `107` | `7` | `0` | `17` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `106` | `166` | Legrand (key `2`) | `0` | external software | `SecurityConfig_010041` |
| `106` | `192` | Legrand (key `2`) | `2` | external software | `SecurityConfig_0100` |
| `106` | `633` | Legrand (key `2`) | `4` | external software | `AlarmConfig_0100` |
| `106` | `640` | Legrand (key `2`) | `5` | external software | `AlarmConfig_0100` |
| `107` | `167` | Legrand (key `2`) | `0` | external software | `SecurityConfig_020030` |
| `107` | `193` | Legrand (key `2`) | `2` | external software | `SecurityConfig_0200` |
| `107` | `634` | Legrand (key `2`) | `4` | external software | `AlarmConfig_0200` |
| `107` | `639` | Legrand (key `2`) | `5` | external software | `AlarmConfig_0200` |

All 8 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `106` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2296` | `13` | `974` |
| `107` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2295` | `13` | `973` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `106` | Product Programming | `3` | Canonical firmware/mode association |
| `107` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `106` | Serial | Canonical firmware/connection association |
| `107` | Serial | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `106` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `107` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `13` - AI Control Unit With Communicator Pstn

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `FW_VER` | No legal values specified in source | Not specified in source | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |

### Device-specific interpretation

Official firmware `106`=6.0.20 and default 107=7.0.17 each declare one Module with PSTN Object `13`; firmware AID has no prescribed character set/default. Object NUM_PSTN and FW_VER have no stored domain/default; IS_GATEWAY is boolean default 0, not an Ethernet connector specification. No Virgin, condition, filter or conversion is associated. Product Programming mode 3 and Serial connection 1 apply to both builds. All eight parameter associations are retained, including separate Legrand brand 2 and line 0/2/4/5 scopes; none of the payloads was supplied or examined. The catalogue establishes both 067510 and 775795 identities, independently of the exact-product hardware-documentation gap.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `975` / `modobj = 201` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`13`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `13` AI Control Unit With Communicator Pstn | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `13` AI Control Unit With Communicator Pstn | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product-specific behavior and transport constraints remain unestablished where no direct source is retained.

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Alarm / PSTN role | Central control with fixed-line communication | Canonical item 975 and Object `13`; no documented complete dialling/zone workflow |
| USB accessory scope | Cable 49234 is explicitly associated with 67510 | Regional catalogue p. 274; adapter/bridge implementation and applicability to 775795 not specified |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Product Programming mode 3 and Serial connection 1 are associated with firmware `106` and 107. The regional catalogue supplies an exact 67510 USB-programming-cable relationship, but not the panel commissioning, reset, project format, update or complete transport arrangement. Do not prescribe the procedures of BTicino 3485/3486 or another Legrand panel. All eight parameter metadata associations are shown; their files have not been examined.

## Source reconciliation

The database explicitly maps 067510 and 775795 to item 975. The regional catalogue uses 67510 in its cable caption, without the leading zero. Its preceding panel entry is 67520, so that entry’s detector capacity, battery/supply and construction are not evidence for 67510. USB accessory evidence and canonical Serial metadata have different scopes; no unexamined bridge implementation is invented. Third-party copies found during historical discovery are not retained manufacturer evidence.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- Locate exact 067510/67510 and 775795 installation/user/software manuals and relevant historical revisions.
- Establish physical supply, zone/call workflows, reset/update and the USB-to-Serial programming arrangement from those originals; payloads and hardware behavior remain unexamined.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0095)
