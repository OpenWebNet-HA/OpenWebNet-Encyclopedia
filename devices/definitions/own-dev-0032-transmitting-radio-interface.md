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

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

Firmware fields are A, PL, M and AID. Firmware 215 narrows M to modes 0/1, while the reusable Object 172 surface lists the wider generic mode family 0,1,6,7,8,CEN. Device programming must use the firmware-applicable subset.

## Object configuration surfaces

### Object `172` - Radio Interface Transmitter

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | Light point | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | Modality | Enum | range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`14` - CEN - range -..- - step `1`<br>`0` - None - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |

Object 172 provides A, PL and M for one transmitting interface endpoint. Generic Object capabilities are not evidence that every later radio-interface mode is enabled by firmware 215.

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
