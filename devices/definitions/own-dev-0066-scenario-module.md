# Scenario module

## Summary

This two-module DIN SCS unit stores and recalls up to sixteen scenarios, each containing up to one hundred controls. It supports several MyHOME systems, with a narrower automation scope across logical expansion and front-panel protection against unintended programming.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0066` | Project identity |
| Technical description | Scenario module | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F420`, `003551` | Canonical commercial records |
| Catalogue item | `61` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, Scenarios, DIN accessory | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F420` | Established identity | canonical commercial record for item `61` |
| Legrand | `003551` | Established identity | canonical commercial record for item `61` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F420` | `8012199738741` | [Archived original](https://archive.openwebnet-ha.org/sha256/8e/0d/8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a.pdf), `F420-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00067-d-EN` | technical sheet | MQ00067-d-EN; 2014-06-05 | Printed/PDF pp. 1–2; complete `F420` ratings, scenario capacity, address and learning/programming limits | [Archived original](https://archive.openwebnet-ha.org/sha256/a9/3b/a93b06343116dda6e4db771a72ab51ac2822748f79ba8eababe1b2a3f453a007.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00067_d_EN.pdf) |
| `F420-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1; exact-reference EAN and complete technical attributes examined; linked technical/DWG downloads and prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/8e/0d/8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F420) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Historical Spanish exact-product sheet within compilation | BT00067-b-ES; undated leaf | Printed p. 703 / PDF p. 134; complete `F420` capacity, 20 mA rating, learning and conflicting 30 s timeout | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / consumption | `27 Vdc` nominal; `18..27 Vdc` operating; `20 mA` | MQ00067-d-EN, printed/PDF pp. 1–2 |
| Temperature / size | `0..40 °C`; two DIN modules | MQ00067-d-EN, printed/PDF pp. 1–2 |
| Scenario capacity | 16 scenarios, up to 100 controls each | MQ00067-d-EN, printed/PDF pp. 1–2 |
| Export consumption discrepancy | `25 mA` at `27 Vdc`, versus exact sheet `20 mA` | `F420`-ean-product-sheet.pdf, printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `61` | Canonical catalogue |
| Technical item | Scenario module | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `55` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `61` | `F420` | `1` | `5` | `BTicino_Undefined_Scenario module` |
| `1710` | `003551` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `196` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `196` | `1` | `3` Scenario module | Fixed/designated metadata | `700` | `3` | `485` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `196` | Physical configuration | `0` | Canonical firmware/mode association |
| `196` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `196` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `196` | `A` | `0..9` | `0` | A; Environment |
| `196` | `PL` | `0..9` | `0` | `PL`; Light Point |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `3` - Scenario module

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

### Device-specific interpretation

Firmware `196` designates Scenario module Object `3` at slot `1` without a Virgin, slot condition, filter or conversion. Firmware A/`PL=0..9` default 0 differs from the published physical `PL=1..9` and reusable Object `A=0..10`/`PL=0..15`. The source associates Physical and Virtual Configuration only; no Advanced Configuration association is stored. Sixteen scenario slots and 100 commands per scenario are publisher limits, not additional physical Modules or a generic reusable Object limit.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `61` / `modobj = 55` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`3`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Functions | Stores automation, sound, temperature and one-family door-entry actions, including stair lighting and lock | MQ00067-d-EN, printed/PDF pp. 1–2 |
| Expansion limit | With F422 logical expansion, only automation commands in the local system containing the scenario module | MQ00067-d-EN, printed/PDF pp. 1–2 |
| Programming indication | Green: available; red: blocked; amber: temporarily blocked while another scenario module is being programmed | MQ00067-d-EN, printed/PDF pp. 1–2 |
| Learning constraints | Only state changes are learned; timed/group commands introduce a 20 s period with no event learning | MQ00067-d-EN, printed/PDF pp. 1–2 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Give each scenario module a unique address and keep it distinct from actuator addresses; its control uses the same scenario-module address. The sheet gives both physical and MyHOME_Suite virtual address ranges as `A=0..9`, `PL=1..9`; these remain distinct from the wider reusable Object domains.

| Operation | English d-revision procedure |
| --- | --- |
| Unlock / lock | Hold lock key at least 0.5 s; green unlocks, red locks |
| Learn / save | Hold relevant control button 3 s until flashing; perform actions; confirm briefly |
| Recall | Brief press on the relevant scenario control |
| Delete one / all | Hold individual control about 10 s; global `DEL` about 10 s until fast yellow indication |
| Abort / bad configuration | Inactivity 30 min aborts in English sheet; orange flashing physical / red flashing virtual indicates configuration error |

Historical Spanish BT00067-b-ES instead specifies 30 seconds of inactivity before abort. Do not assume those timings interchangeable or map them to an installed revision without further evidence.

## Source reconciliation

The English d sheet and historical Spanish b leaf agree on scenario capacity and 20 mA consumption, but their inactivity abort timings differ: 30 minutes versus 30 seconds. The current Italian export lists 25 mA. No change log establishes a production revision or correction for either discrepancy. Catalogue modes establish physical and virtual configuration only; the software compatibility record does not establish installed behavior.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Learning timeout and 20/25 mA consumption differences remain unresolved by a hardware/release mapping.
- Independent exact-`003551` instructions/EAN and the referenced software/F422 commissioning guides are not examined.
- Actual learned command order, capacity and expansion behavior are unobserved.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F420-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F420` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/8e/0d/8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F420); SHA-256 `8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0066)
