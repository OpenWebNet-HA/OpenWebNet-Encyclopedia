# Polyx Alarm

## Summary

The Polyx Alarm `3485B` is a four-zone alarm central unit in the canonical catalogue. It shares the TiSecurityBasic configuration-backup and firmware-update workflow with the flush-mounted 4601 family, while remaining a separate hardware identity.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0086` | Project identity |
| Technical description | Polyx Alarm | Canonical catalogue |
| Commercial identities | `3485B` | Canonical commercial records |
| Catalogue item | `140` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `199` | Canonical inventory |
| Firmware definition | `1.0.10` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3485B` | Established catalogue identity | canonical commercial record for item `140` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `U2864B_Software_IT.pdf` | TiSecurityBasic software manual | Version 1.0; 11/09-01-PC | Complete 16-page document: workflow pp. 3–7; firmware pp. 8–11; configuration acquisition/transfer pp. 12–14. Explicit `3485B` and HC/HS/HD/L/N/NT4601 targets | [Archived original](https://archive.openwebnet-ha.org/sha256/0b/ed/0bed021e002ce15f14ea5c7a5d576c323fa31acf791967bcf7c9285eb4a3cbcf.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2864B_Software_IT.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue role | Polyx Alarm; four-zone central unit | Commercial item 140 and Object `11` |
| PC interface | Six-pin programming connection; serial 335919 or USB 3559 | `U2864B`, PDF pp. 10, 12–14; exact target `3485B` |
| Hardware ratings | Enclosure dimensions, supply/current, battery and telephone hardware are not established here | Exact `3485B` hardware manual/technical sheet not retained |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `140` | Canonical catalogue |
| Technical item | Polyx Alarm | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `199` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Burglar alarm system | `199` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Burglar alarm | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `140` | `3485B` | `1` | `4` | `BTicino_L/N/NT_Polyx Alarm` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `140` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `1` | `0` | `10` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `18` | `61` | BTicino (key `1`) | `0` | external software | `TiSecurityBasic_0100` |

All 1 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `1` | `11` Burglar alarm 4 zones control unit | Fixed/designated metadata | `2273` | `11` | `951` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `18` | Product Programming | `3` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `18` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `11` - Burglar alarm 4 zones control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZONA1` | `1..4` | `1` | First zone AI |
| `ALLARME` | `0..9` | `0` | Allarm setting |

### Device-specific interpretation

Firmware `18`=1.0.10, Official/default, has one Module with four-zone Object `11` and AID only. Object `11` exposes only ZONA1ALLARME and ALLARME in this catalogue; the local menu and complete product capabilities cannot be inferred from those two fields. No Virgin, condition, filter or conversion is associated. Product Programming `3` and parameter record `61` (brand `1`, line `0`) are stored; no connection or package association is stored. Sharing this schema/parameter with the flush-mounted 4601 item `160` does not establish identical enclosures, battery ratings or telephone capability. TiSecurityBasic Version 1.0 is software-document scope, not the catalogue firmware `1`.0.10.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `140` / `modobj = 199` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`11`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `11` Burglar alarm 4 zones control unit | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Firmware update | Separate .fwz firmware transfer procedure with Maintenance and rear slide OFF | `U2864B`, PDF pp. 8–11 |
| Configuration backup / restoration | Acquire and save configuration; open and transfer to the selected panel | `U2864B`, PDF pp. 12–14 |
| Local menu scope | Four-zone Object catalogue; the 4601 hardware menu is not assumed identical | Canonical item 140; shared software target does not prove hardware equivalence |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

TiSecurityBasic explicitly selects the correct target, `3485B` or HC/HS/HD/L/N/NT4601. Its Version 1.0 is a software version (`U2864B`, PDF pp. 8–11), not installed panel firmware. For firmware update: enter Maintenance, move the rear slide to OFF, connect serial 335919 or USB 3559 at the six-pin connector, choose the COM port and .fwz file, follow the transfer, disconnect, move slide ON and press physical RESET. That post-update RESET is not documented as a factory erase.

For configuration acquisition/transfer, pp. 12–14 separately describe Maintenance, six-pin connection, COM selection and saving/opening a configuration file. Acquisition retains a backup; transfer restores a saved configuration or transfers it to another correctly selected target. Those pages do not prescribe the update-specific OFF/ON/RESET sequence. No edited parameter domain or transport mapping is inferred from the screenshots. The complete product’s local commissioning still requires its exact hardware manual.

## Source reconciliation

The catalogue establishes exact `3485B` identity independently of the missing hardware manual. TiSecurityBasic explicitly names `3485B` and 4601 as selectable targets. Its connection diagram carries ART.3485 although the accompanying target text says `3485B`; that legacy diagram label is recorded rather than treated as an alias to PSTN item 139. Commercial line key 4 is retained as catalogue metadata; no marketed L/N/NT enclosure is inferred from it. Hardware and local-menu details from `U2860B` are not transplanted to this separate item.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Obtain a dedicated `3485B` hardware/installation manual for supply/current, enclosure, zones, local controls, battery and any telephone capability.
- Resolve the ART.3485 illustration label against the explicitly named `3485B` target and corroborate installed firmware.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0086)
