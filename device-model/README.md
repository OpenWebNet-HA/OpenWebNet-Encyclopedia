# Overview

The MyHOME device model describes how one physical product exposes configurable functions to MyHOME_Suite and to the diagnostic, programming, and functional protocols.

The canonical hierarchy used throughout this documentation is:

**Physical Device → Firmware → Module → Object → Configuration**

Firmware is an implementation layer between the product model and its exposed Modules. In ordinary discussion the shorter **Physical Device → Module → Object → Configuration** form remains sufficient.

## Reference

| Subject | Page |
| --- | --- |
| Evidence roles, identifier boundaries, and source handling | [`sources-and-identifiers.md`](sources-and-identifiers.md) |
| Product identity, catalogue records, and Device composition | [`physical-devices.md`](physical-devices.md) |
| Firmware selection and capability projection | [`firmware.md`](firmware.md) |
| Firmware-exposed Modules and internal slots | [`modules.md`](modules.md) |
| Logical functions and Object identity | [`objects.md`](objects.md) |
| Configurable Module templates and permitted Objects | [`virgin-objects.md`](virgin-objects.md) |
| Configuration definitions, values, constraints, and protocol representation | [`configuration.md`](configuration.md) |

## Canonical model

| Level | Meaning | Primary catalogue representation |
| --- | --- | --- |
| Physical Device | An installed hardware product instance | `EN_DEVICE` → `EN_ITEM` |
| Firmware | A versioned capability definition for an item | `EN_FIRMWARE`, `EN_BUILDS` |
| Module | A firmware-exposed logical container at an internal slot | `EN_SLOTS`, `AS_OBJECT_FIRMWARE` |
| Object | The logical function assigned to or offered by a Module | `EN_KEY_OBJECT` |
| Virgin Object | A template constraining which Objects a configurable Module can become | `EN_VIRGIN_OBJECT` and association tables |
| Configuration | Object- or firmware-scoped properties and their allowed values | `EN_CONF`, ranges, filters, conditions, and conversion rules |

The [canonical `MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) contains 541 Device records, 210 item definitions, 311 firmware definitions, 158 Objects, 18 Virgin Objects, 1,725 slot/Object assignments, and 2,883 configuration definitions. These counts describe this source revision; they are not protocol limits.

## End-to-end catalogue path

For a catalogue Device, the principal capability path is:

1. `EN_DEVICE.id_item` selects the shared item definition in `EN_ITEM`.
2. `AS_ITEM_SYSTEM` associates the item with one or more catalogue systems and supplies the item-level `modobj`.
3. `EN_FIRMWARE.id_item` selects the firmware definitions available for that item.
4. `AS_OBJECT_FIRMWARE` associates each firmware with supported Objects.
5. `EN_SLOTS.id_object_firmware` places those Object options at internal slots.
6. Virgin-Object associations describe configurable Module templates and the Objects they permit.
7. `EN_CONF` defines Object-scoped or firmware-scoped configuration properties.
8. Ranges, filters, conditions, and rules constrain the values available in a particular context.

The original database declares few foreign keys. The relationships above are supported by complete key coverage in the canonical data and by the way the association tables are structured. They remain reconstructed relationships rather than modifications to the canonical source.

## Protocol projections

The [canonical `OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) projects parts of the model onto diagnostic and programming frames:

| Operation | Model level exposed |
| --- | --- |
| `DIMENSION 1` | item/model identity, a field labelled `N_CONF`, brand, and line |
| `DIMENSION 2` | firmware version |
| `DIMENSION 3` | hardware version |
| `DIMENSION 6` | microcontroller version |
| `DIMENSION 13` | 32-bit Device ID |
| `DIMENSION 30` | internal slot, Object identifier, and configured state |
| `DIMENSION 32` | internal slot, system, and configured address |
| `DIMENSION 35` | configuration index, internal slot, and parameter value |
| `DIMENSION 38` | request/reset operation selecting one or all internal slots |
| `DIMENSION 310` | special Object parameter response |

These frames expose a runtime projection of the catalogue model; they do not reproduce the catalogue schema directly.

## Model boundaries

A Physical Device is not equivalent to one OpenWebNet address, one Module, one Object, or one functional `WHO`.

- One product item can have several branded Device records.
- One item can have several firmware definitions.
- One firmware can expose several Modules.
- One Module can offer several Object choices.
- One Object can have several configuration properties.
- Different Modules of one Device can participate in different functional systems.
- The Device address used for discovery or interview can differ from the functional addresses configured on its Modules.

**Module** is the preferred term for a firmware-exposed logical container. **Internal slot** is reserved for the numeric slot or index used by diagnostic frames and catalogue structures.

The Device description and Object description are also distinct. `EN_DEVICE.name` is the preferred MyHOME_Suite-facing description for the physical model. `EN_KEY_OBJECT.descr` identifies an individual logical function.

## Evidence

The evidence sources and their identifier boundaries are defined in [`sources-and-identifiers.md`](sources-and-identifiers.md). In summary, `MHCatalogue.db` defines catalogue capability, `OPEN.db` defines diagnostic and programming structures, the ScenarioDevices databases describe scenario-engine capabilities, `rules.db3` adds selected configuration constraints, and the public OpenWebNet documents define published functional behavior.

Original evidence remains unchanged under [`sources/`](../sources/); derived relationships are documented outside the canonical corpus.

## Interpretation rules

Use each source only for the layer it establishes. Do not join independent identifier spaces because their numeric values happen to match, and do not promote implementation labels to protocol semantics without corroborating evidence.

Unknown fields remain unknown. The unresolved `N_CONF` value in diagnostic `DIMENSION 1` is documented with Physical Device identity in [`physical-devices.md`](physical-devices.md).
