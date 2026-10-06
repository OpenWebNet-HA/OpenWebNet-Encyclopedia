# Memory module

## Summary

This SCS memory module records lighting states and restores them after a power interruption. It excludes shutters and requires learning the loads to restore; systems joined by physical expansion can share one memory module.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0065` | Project identity |
| Technical description | Memory module | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F425`, `003552` | Canonical commercial records |
| Catalogue item | `60` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, State recovery, DIN accessory | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F425` | Established identity | canonical commercial record for item `60` |
| Legrand | `003552` | Established identity | canonical commercial record for item `60` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F425` | `8012199529646` | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/33/3f3380851ec72b06305ddb183b7efb83efd2abc35d381f37a0ae0f86c1bef8bc.pdf), `F425-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00281-b-UK` | technical sheet | MQ00281-b-UK; 2012-12-13 | Printed/PDF p. 1; complete `F425` memory, physical expansion, ratings, indicators and learning procedure | [Archived original](https://archive.openwebnet-ha.org/sha256/0f/28/0f28345d89b8ceccc8d7d91dba8eac68522e215c27b7ee82accb3d777a79233c.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00281-b-uk.pdf) |
| `F425-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1; exact-reference EAN and complete technical attributes examined; linked technical/DWG downloads and prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/33/3f3380851ec72b06305ddb183b7efb83efd2abc35d381f37a0ae0f86c1bef8bc.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F425) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Historical Spanish exact-product sheet within compilation | BT00281-a-ES; undated leaf | Printed p. 714 / PDF p. 145; complete `F425` ratings, placement, `LED`/learning procedure and physical-expansion exception | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current / dissipation | `27 Vdc` nominal; `18..27 Vdc` operating; `5 mA`; `0.1 W` | MQ00281-b-UK, printed/PDF p. 1 |
| Temperature / size | `0..40 °C`; two DIN modules | MQ00281-b-UK, printed/PDF p. 1 |
| Placement | No more than `10 m` from the power supply | MQ00281-b-UK, printed/PDF p. 1 |
| Restoration trigger / delay | Power interruption at least `400 ms`; lighting restoration about `10 s` after supply returns | MQ00281-b-UK, printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `60` | Canonical catalogue |
| Technical item | Memory module | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `54` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `60` | `F425` | `1` | `5` | `BTicino_Undefined_Black-out memory` |
| `1629` | `003552` | `2` | `5` | `Black-out memory` |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `187` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `187` | `1` | `30` Memory module | Fixed/designated metadata | `642` | `30` | `446` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `187` | Physical configuration | `0` | Canonical firmware/mode association |
| `187` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `187` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `187` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `187` | `A` | `0..9` | `0` | A; Environment |
| `187` | `PL` | `0..9` | `0` | `PL`; Light Point |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `30` - Memory module

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

### Device-specific interpretation

Firmware `187` designates Black-out memory Object `30` at slot `1`, without a Virgin, slot condition, relation filter or conversion. Firmware A/`PL=0..9` default 0 differs from reusable Object `A=0..10`/`PL=0..15`. The sheet recommends `A=0` and `PL=1..9` to avoid actuator address overlap; that recommendation is not a different stored default or proof of all wider Object addresses. Physical, virtual and advanced mode associations are software applicability, separate from the front-button learning sequence.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `60` / `modobj = 54` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`30`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Memory | Saves lighting actuator state on each bus command and restores it after qualifying interruption | MQ00281-b-UK, printed/PDF p. 1 |
| System boundary | Normally one module per installed system/power supply; one may cover multiple systems joined by F422 physical expansion | MQ00281-b-UK, printed/PDF p. 1 |
| Exceptions | Shutters are not managed; timed ON restores as simple ON | MQ00281-b-UK, printed/PDF p. 1 |
| `LED` states | Off: too far from supply; green fixed: normal; orange fixed: unacquired; red fixed: excluded; red flashing: learning; orange flashing: wrong/missing configuration | MQ00281-b-UK, printed/PDF p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Use a distinct address from actuators; the sheet recommends `A=0`, `PL=1..9`. For Lighting Management use Project&Download; MyHOME configuration is separately represented by the catalogue modes. Relearn after installation changes.

| Learning step | Manufacturer sequence |
| --- | --- |
| Prepare | All loads OFF, including powered dimmers |
| Enter / exclude | Hold front button 5 s until red; release; turn ON loads that must be excluded |
| Acquire | Within 30 min press button; red flashes quickly while learning; after about 30 s green indicates completion |
| Timeout | No confirmation within 30 min returns orange |
| Test | Perform a blackout of at least 15 s as instructed; this test is distinct from the `400 ms` minimum restoration trigger |

## Source reconciliation

The exact English sheet and Spanish BT00281-a-ES agree on power, timing, placement and physical-expansion scope. The current `F425` export confirms 27 V/5 mA/two DIN modules and its exact EAN. The previous logical-expansion wording was incorrect: `F425`’s exception is physical expansion, whereas `F420` has a separate logical-expansion limitation. Reusable addresses and catalogue defaults do not replace the recommended non-overlapping learning address.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Exact `003552` physical instructions and independent EAN remain unretained; catalogue identity is established.
- F422 topology/application instructions and Project&Download help are referenced but not independently examined.
- Restoration, excluded loads and address collision behavior remain unobserved.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F425-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F425` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3f/33/3f3380851ec72b06305ddb183b7efb83efd2abc35d381f37a0ae0f86c1bef8bc.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F425); SHA-256 `3f3380851ec72b06305ddb183b7efb83efd2abc35d381f37a0ae0f86c1bef8bc`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0065)
