# Transmitting radio interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0032` | Project identity |
| Technical description | SCS-powered radio transmitting interface | Catalogue + official documentation |
| Catalogue item / model | `34` / `modobj 21` | Implementation evidence |
| Firmware applicability | 215, wildcard -1.-1.-1, one slot | Implementation evidence |
| Commercial identities | HC/HS4576; HD4576; L/N/NT4576 | Catalogue |
| Categories | Radio interface, Control bridge, Lighting / Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Axolute | `HC/HS4576` | `34` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `L/N/NT4576` | `1828` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `HD4576` | `1829` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | 4576 radio-transmitter sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

Publisher documentation identifies the interface as a 27 Vdc BUS-powered, two-module radio transmitter. Exact suffix/aesthetic variants differ by product line.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `34` | Canonical catalogue |
| Technical item description | Transmitting radio interface | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `21` | AS_ITEM_SYSTEM |
| Commercial records | `3` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `215` | `-1` | `-1` | `1` | `1` | `0` |

Firmware 215 has wildcard version/revision/build applicability and one Module slot.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `215` | `754` | `172` | `172` | Radio Interface Transmitter |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1506` | `1` | `172` | fixed | Radio Interface Transmitter |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

Slot 1 is fixed Object 172, Radio Interface Transmitter.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `215` | `1` | `1` | Virtual Configuration |
| `215` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | 0..9 | 0 | area / environment configurator |
| `PL` | 0..9 | 0 | light-point configurator |
| `M` | 0 / 1 | 0 | operating / function mode |

Firmware 215 narrows M to 0/1. The reusable transmitter Object has a wider generic mode family, which must not be projected back onto this Device.

## Object configuration surfaces

### Object `172` - Radio Interface Transmitter

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | 0..9 | 0 | Area |
| `PL` | 0..9 | 0 | Light point |
| `M` | 1 / 6 / 7 / 8 / CEN / None | 0 | Modality |

**Firmware relationship.** catalogue irregularity: `TYPE_CONTACT` (filter `1631`) is not present in this reusable Object schema.

The tables above account for the reusable Object fields without reproducing database serialization metadata. Generic Object capability is kept distinct from the Device/firmware relationship and from physical configurator positions.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `1` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `172` | `1631` | `TYPE_CONTACT` | Contact type | `1` | - |

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

The interface bridges configured SCS control semantics to the supported radio side. Functional meaning depends on the configured command role; it should not be hard-coded as a single lighting action.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Treat firmware 215's `M` values 0/1 domain as authoritative for this Device unless direct revision-specific evidence establishes additional modes.

## Source reconciliation

The canonical catalogue establishes the one-slot Radio Interface Transmitter model and the three grouped commercial records. Official historical documentation corroborates the family role and physical format, but suffix naming differs between the implementation catalogue and printed guide; that mismatch remains explicit.

## Evidence limits and open work

- Recover a dedicated publisher technical sheet for the exact database-listed 4576 variants if one exists.
- Hardware-corroborate firmware identity and transmitted command behavior.
- Resolve the Contact type filter into a human-readable Device-specific rule.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
