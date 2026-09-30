# Rotary regulation control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0028` | Project identity |
| Technical description | Flush-mounted rotary SCS control | Catalogue + implementation evidence |
| Catalogue item / model | `25` / `modobj 11` | Implementation evidence |
| Firmware applicability | firmware `213`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `HC/HS/HD4563`, `L/N/NT4563` | Catalogue |
| Categories | Control, Lighting/Automation command | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Axolute | `HC/HS/HD4563` | `25` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / L/N/NT | `L/N/NT4563` | `1838` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | 4563 control-family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `25` | Canonical catalogue |
| Technical item description | Regulation rotative control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `11` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `213` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `213` is wildcard `-1.-1.-1` with one Module.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `213` | `606` | `451` | `451` | Knob control |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1009` | `1` | `451` | fixed | Knob control |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The Module resolves to Object `451`, **Knob control**, a one-slot Object associated with Automation and the relevant command-control collections. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `213` | `1` | `1` | Virtual Configuration |
| `213` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `M` | M | Enum | range -..- - step `1`<br>`9` - O/I - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`12` - UP/DOWN - range -..- - step `1`<br>`13` - UP/DOWN monostable - range -..- - step `1`<br>`14` - CEN - range -..- - step `1`<br>`15` - PUL - range -..- - step `1`<br>`0` - 0 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `LIV1` | LIV1 | Range | range `0`..`99` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `LIV2` | LIV2 | Range | range `0`..`99` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `SPE` | SPE | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `I` | I | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`14` - CEN - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

The firmware exposes `A`, `PL`, `M`, `LIV1`, `LIV2`, `SPE`, `I` and `AID`. The catalogue describes `M` as command mode with `O/I`, `OFF`, `ON`, `PUL`, `SU_GIU` and `SU_GIU_M` alternatives. `LIV1` and `LIV2` are level configurators; `SPE` selects a special command function; `I` is an additional configurator.

## Object configuration surfaces

### Object `451` - Knob control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL` | Light point | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M` | Modality | Enum | range -..- - step `1`<br>`9` - O/I - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`12` - UP/DOWN - range -..- - step `1`<br>`13` - UP/DOWN monostable - range -..- - step `1`<br>`14` - CEN - range -..- - step `1`<br>`15` - PUL - range -..- - step `1`<br>`0` - None - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `LIV1` | Configurator LIV1 | Range | range `0`..`99` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `LIV2` | Configurator LIV2 | Range | range `0`..`99` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `SPE` | Special function command control (0-9) | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `I` | Configurator I | Enum | range -..- - step `1`<br>`0` - None - range -..- - step `1`<br>`14` - CEN - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

Object `451` mirrors the firmware's address, command-mode, level and special-function controls. These fields describe one rotary-control Module, not multiple independent channels.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `0` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | Identify the Device model/family and compare it with catalogue identity. | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Record installed firmware instead of treating wildcard catalogue applicability as an observed version. | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve Module/Object topology, especially when candidates share a slot. | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Inspect addressing for the resolved Module/Object when exposed. | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Corroborate firmware/Object configuration and physical/software relationships. | [Configuration](../../diagnostics/dim35-configuration.md) |

Catalogue applicability is not itself an observed runtime result.

## Functional applicability

The selected command mode determines the functional command emitted. The dossier therefore does not collapse the Device to a single lighting action without first resolving configuration.

## Observed behavior and corroboration

No sanitized hardware fingerprint or first-hand command trace is currently retained for this exact family.

## Programming

Preserve the complete `M/LIV1/LIV2/SPE/I` configuration rather than translating the rotary control to a simple on/off command.

## Source reconciliation

The database is internally consistent: both commercial identities share firmware `213`, one Knob control Object and the same eight configuration fields. Dedicated publisher documentation remains a discovery gap, so physical interaction details beyond the database model are not inferred.

## Evidence limits and open work

- Locate and archive a publisher-original 4563-family technical sheet.
- Add a sanitized hardware fingerprint and first-hand command traces.
- Establish human-readable semantics for each `LIV1/LIV2/SPE/I` combination.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
