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

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | 0..9 | 0 | area / environment configurator |
| `PL` | 0..9 | 0 | light-point configurator |
| `M` | 0 / O/I / OFF / ON / UP/DOWN / UP/DOWN monostable / CEN / PUL | 0 | operating / function mode |
| `LIV1` | 0..99 | 1 | first regulation level |
| `LIV2` | 0..99 | 1 | second regulation level |
| `SPE` | 0..9 | 0 | special-function selector |
| `I` | 0 / CEN | 0 | additional function selector |

LIV1/LIV2 are the two regulation-level fields. SPE and I are additional command selectors whose semantics depend on the selected operating mode.

## Object configuration surfaces

### Object `451` - Knob control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | 0..9 | 0 | Area |
| `PL` | 0..9 | 0 | Light point |
| `M` | O/I / OFF / ON / UP/DOWN / UP/DOWN monostable / CEN / PUL / None | 0 | Modality |
| `LIV1` | 0..99 | 1 | Configurator LIV1 |
| `LIV2` | 0..99 | 1 | Configurator LIV2 |
| `SPE` | 0..9 | 0 | Special function command control (0-9) |
| `I` | None / CEN | 0 | Configurator I |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

The tables above account for the reusable Object fields without reproducing database serialization metadata. Generic Object capability is kept distinct from the Device/firmware relationship and from physical configurator positions.

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
