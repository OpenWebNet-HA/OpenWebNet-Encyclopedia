# Identify a Device

## Goal

Resolve one installed Device to its MyHOME_Suite catalogue context and preferred Device description.

## Prerequisites

A completed Device interview containing at least `DIMENSION 1`. Firmware, hardware, and `DIMENSION 13` improve resolution.

## Procedure

1. Start an interview by Device ID with `*[WHO]*10#[ID]*0##` where available.
2. Collect `DIMENSION 1`, firmware, hardware, Device ID, Module records, and the `WHAT 4` terminal marker.
3. Resolve the `DIMENSION 1` model value through the item/system path in `MHCatalogue.db`.
4. Resolve candidate `EN_DEVICE` records through their shared item.
5. Use `EN_DEVICE.name` as the preferred MyHOME_Suite-facing description.
6. Narrow firmware capability using the reported version and item/firmware associations.
7. Retain every compatible SKU when the protocol evidence does not identify one uniquely.
8. Keep the installed Device ID separate from all catalogue IDs.

## Identifier boundaries

| Runtime value | Must not be treated as |
| --- | --- |
| Device ID | `EN_DEVICE.id_device`, item ID, SKU, or Object |
| `OBJECT_MODEL`/`modobj` | Device primary key |
| `DIMENSION 1` VALUE 2 | Object, Virgin Object, form factor, or firmware class |
| `WHERE` | globally unique Device identity |

`DIMENSION 1` VALUE 2 remains unknown and must not be used to disambiguate candidates.

## Validation gates

A unique Device claim requires one surviving catalogue record. If several branded SKUs share the same item and capability, report the common Device description and the candidate SKU set.

## Expected result

An identity record containing the installed ID, diagnostic family, raw `DIMENSION 1`, item, candidate Devices/SKUs, preferred `EN_DEVICE.name` description, resolved firmware evidence, and remaining ambiguity.

See [Device Identity](../diagnostics/dim1-device-identity.md), [Physical Devices](../device-model/physical-devices.md), and [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).
