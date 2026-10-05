# Scenario module

## Summary

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
| `MQ00067-d-EN` | technical sheet | 2014-06-05 | `F420` scenario capacity, electrical data and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/a9/3b/a93b06343116dda6e4db771a72ab51ac2822748f79ba8eababe1b2a3f453a007.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00067_d_EN.pdf) |
| `F420-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `F420` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/8e/0d/8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F420) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `MQ00067-d-EN` |
| Current draw | `20 mA` | `MQ00067-d-EN` |
| Operating temperature | `0..40 °C` | `MQ00067-d-EN` |
| Width | `2 DIN modules` | `MQ00067-d-EN` |
| Scenario capacity | up to `16` scenarios | `MQ00067-d-EN` |
| Controls per scenario | up to `100` | `MQ00067-d-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `61` | Canonical catalogue |
| Technical item | Scenario module | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `196` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `196` | Physical configuration | supported configuration route for this Device family |
| `196` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `196` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `196` | `A` | `0..9` | `0` | A; Environment |
| `196` | `PL` | `0..9` | `0` | PL; Light Point |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `3` - Scenario module

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

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

DIN scenario-memory module storing up to 16 scenarios with up to 100 controls each. Scenarios are associated with controls through the module address, with dedicated front-panel programming lock and erase functions.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue maps `F420` and `003551`. The dedicated publisher technical sheet documents `F420`, while the archived MyHOME catalogue provides the old/new commercial cross-reference.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F420-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F420` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/8e/0d/8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F420); SHA-256 `8e0dd94d2d2f31f024cc9684241de9c9c9a1cd8adb602cae12ea7c6c28fca99a`.
