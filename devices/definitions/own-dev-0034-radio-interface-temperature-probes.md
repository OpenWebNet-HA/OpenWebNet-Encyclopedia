# Radio interface for temperature probes

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0034` | Project identity |
| Technical description | Two-channel radio receiving interface for wireless temperature probes | Catalogue + official documentation |
| Catalogue item / model | `39` / `modobj 23` | Implementation evidence |
| Firmware applicability | 239, wildcard -1.-1.-1, two slots | Implementation evidence |
| Commercial identities | HC/HS/HD4577; L/N/NT4577 | Catalogue |
| Categories | Radio interface, Temperature control, Sensor bridge | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / L/N/NT | `L/N/NT4577` | `39` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `HC/HS/HD4577` | `1966` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| MQ00183-c-EN | Technical sheet | publisher revision as archived | Whole document | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-4577-mq00183-c-en/MQ00183-c-EN.pdf) |
| U1870C | Instruction sheet | publisher revision as archived | Whole document | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-4577-u1870c/U1870C.pdf) |
| BTicino L4577 | Current product record | current | Whole product page | External official source | [Official source](https://www.bticino.com/products/bt-l4577) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

Current publisher data for the Livinglight form gives 27 Vdc supply, 33 mA input current, 868 MHz radio and a two-module flush-mounted enclosure.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `39` | Canonical catalogue |
| Technical item description | Radio interface for temperature probes | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Additional system | `1` - lighting_automation; `modobj` `23` | AS_ITEM_SYSTEM |
| Main system | `2` - thermoregulation; `modobj` `23` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `239` | `-1` | `-1` | `2` | `1` | `0` |

Firmware 239 has wildcard version/revision/build applicability and two Module slots.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `239` | `693` | `124` | `124` | Radio interface for sensors (measurer T) |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1333` | `1` | `124` | fixed | Radio interface for sensors (measurer T) |
| `1334` | `2` | `124` | fixed | Radio interface for sensors (measurer T) |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

Slots 1 and 2 are both fixed Object 124, Radio interface for sensors (measurer T). This is a two-slot instance of the same temperature-sensor-interface Object.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `239` | `1` | `1` | Virtual Configuration |
| `239` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL1/N1` | PL1/N1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M1` | M1 | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `A2/-` | A2/- | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL2/N2` | PL2/N2 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M2` | M2 | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

Firmware fields are A, PL1/N1, M1, A2/-, PL2/N2, M2 and AID. For each channel, `M` value 0 means not configured, `M` value 1 temperature sensor and `M` value 6 lighting sensor. The reusable Object 124 exposes A, PL_N and M.

## Object configuration surfaces

### Object `124` - Radio interface for sensors (measurer T)

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL_N` | Light point N | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M` | Modality | Boolean | range -..- - step `1` - default marker `1`<br>`0` - None - range -..- - step `1`<br>`1` - 1 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

Each fixed slot uses the temperature-sensor radio-interface Object. The firmware's paired PL/N and M fields distinguish the two configured channels; they must not be flattened into a single probe address.

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

Thermoregulation is the main catalogue system for the Device; the item is also associated with lighting/automation. The configured channel mode determines whether a slot represents temperature or lighting-sensor use.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Program and validate both channel positions independently. Preserve `M` values 0/1/6 semantics and the dual-system applicability.

## Source reconciliation

Official product documentation corroborates the 4577/3455 radio-temperature role, 27 Vdc BUS supply and two-module form. The database adds two fixed Object slots and explicitly permits `M` value 6 lighting-sensor mode, which broadens the implementation model beyond the product headline.

## Evidence limits and open work

- Hardware-corroborate both slot identities and `M` value 6 behavior.
- Capture representative radio-probe traffic without retaining private installation identifiers.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MQ00183-c-EN](../../sources/devices/documents/device-doc-4577-mq00183-c-en/MQ00183-c-EN.pdf)
- [U1870C](../../sources/devices/documents/device-doc-4577-u1870c/U1870C.pdf)
- [BTicino L4577](https://www.bticino.com/products/bt-l4577)
