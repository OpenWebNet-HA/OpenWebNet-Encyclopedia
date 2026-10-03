# Module contacts interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0071` | Project identity |
| Technical description | Module contacts interface | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `L/N/NT4688` | Canonical commercial records |
| Catalogue item | `80` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `150` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, Contact interface, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4688` | Established identity | canonical commercial record for item `80` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MH_Guide_Automatisme.pdf` | technical/system guide | historical publisher guide | `L/N/NT4688` contact-interface construction and traditional-device integration; printed p. 168 / PDF p. 170 | [Archived original](https://archive.openwebnet-ha.org/sha256/80/6a/806a55bffb924f5ef7b25398432c0a86ab210722adc30b81f33558c6ec36f561.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MH_Guide_Automatisme.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Form factor | `1` flush-mounted Living International / Light / Light Tech module | `MH_Guide_Automatisme.pdf`, printed p. 168 |
| Traditional inputs | `2` independent contact/control units | `MH_Guide_Automatisme.pdf`, printed p. 168 |
| Interface role | Dry-contact traditional controls to SCS BUS commands | `MH_Guide_Automatisme.pdf`, printed p. 168 |
| Declared module count | `1` | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `80` | Canonical catalogue |
| Technical item | Module contacts interface | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `150` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `202` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `202` | `1` | `33` Interface contacts automation | Fixed/designated metadata | `1507` | `33` | `755` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `202` | Physical configuration | supported configuration route for this Device family |
| `202` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `202` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `202` | `A` | `0..9` | `0` | A; Environment |
| `202` | `PL` | `0..9` | `0` | PL; Light Point |
| `202` | `M` | `0..9`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `15` = `PUL` | `0` | M; Mode physical configurator (0-9, `O/I`,`OFF`,`ON`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `33` - Interface contacts automation

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `202` | `33` | `1632` | `TYPE_CONTACT` | No legal values specified in source (entire reusable range retained) | `0` | Contact type; field definition belongs to a different Object scope; do not alias it to a similarly named field |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `80` / `modobj = 150` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`33`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Flush-mounted two-input interface translating traditional dry-contact controls into SCS BUS commands. The two logical units can operate independently or as a paired double command for a motorized load.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue identifies the combined `L/N/NT4688` reference and maps it to one technical item. The publisher automation guide directly describes the same combined reference and its one-module, two-input construction.

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
