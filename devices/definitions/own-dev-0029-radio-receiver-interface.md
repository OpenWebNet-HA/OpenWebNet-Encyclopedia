# Radio receiver interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0029` | Project identity |
| Technical description | Flush-mounted 868 MHz radio-to-SCS receiving interface | Catalogue + official technical documentation |
| Catalogue item / model | `28` / `modobj 20` | Implementation evidence |
| Firmware applicability | firmware `214`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `HC/HS/HD4575`, `L/N/NT4575`, `L/N/NT4575N` | Catalogue |
| Categories | Radio interface, Control bridge | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Axolute | `HC/HS/HD4575` | `28` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / L/N/NT | `L/N/NT4575` | `1839` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / L/N/NT | `L/N/NT4575N` | `1840` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| mh_diff-sonore2008.pdf | Radio-wired interface technical guide | historical publisher guide | 4575 family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-radio-wired-interface-sound-guide/mh_diff-sonore2008.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

The official guide specifies 27 Vdc BUS supply, 868 MHz reception, 2 mA consumption for `L/N/NT4575N` and `HC/HS4575`, two wiring-device modules, and +5 °C to +35 °C operating temperature. It identifies a status LED, programming micro-button, physical configurator positions and the SCS BUS connector.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `28` | Canonical catalogue |
| Technical item description | Receiving radio interface | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `20` | AS_ITEM_SYSTEM |
| Commercial records | `3` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `214` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `214` is wildcard `-1.-1.-1` and declares one Module.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `214` | `607` | `27` | `27` | Radio receiver |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1010` | `1` | `27` | fixed | Radio receiver |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The single Module resolves to Object `27`, **Radio receiver**. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `214` | `1` | `1` | Virtual Configuration |
| `214` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | 0..9 | 0 | area / environment configurator |
| `PL` | 0..9 | 0 | light-point configurator |
| `M` | 0 / 1 / 6 / 7 / 8 / CEN | 0 | operating / function mode |

The firmware exposes only A, PL, M and AID. The reusable radio-receiver Object uses the corresponding MOD concept.

## Object configuration surfaces

### Object `27` - Radio receiver

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | 0..9 | 0 | Area |
| `PL` | 0..9 | 0 | Light point |
| `MOD` | 1 / 6 / 7 / 8 / CEN | 1 | Modality |

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

The official documentation shows that the receiver can translate radio controls into SCS functions. A sound-system guide specifically documents amplifier on/off, volume, source selection and radio-station/track changes when appropriately configured. Other configured modes must be interpreted from their own functional context.

## Observed behavior and corroboration

No sanitized first-hand capture for this exact receiver is currently retained.

## Programming

Preserve the configured `M/MOD` role, including `CEN`, rather than assuming all received radio commands are ordinary lighting commands.

## Source reconciliation

The canonical database and publisher technical guide agree on a one-Module radio receiver with physical configurators and SCS BUS connection. The official guide directly covers two of the catalogue's reference forms; the remaining grouped references are catalogue-correlated and should not be represented as separately documented variants.

## Evidence limits and open work

- Add sanitized hardware and pairing traces.
- Recover dedicated documentation for the catalogue-only `HD4575` and `L/N/NT4575` forms if distinct publisher sheets exist.
- Map each `M/MOD` value to verified emitted OpenWebNet behavior.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [mh_diff-sonore2008.pdf](../../sources/devices/documents/device-doc-radio-wired-interface-sound-guide/mh_diff-sonore2008.pdf)
