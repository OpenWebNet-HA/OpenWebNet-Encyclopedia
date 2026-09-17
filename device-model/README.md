# Overview

The MyHOME device model describes how a physical product exposes configurable functions to MyHOME_Suite and to the diagnostic and programming protocols.

The canonical hierarchy used throughout this documentation is:

**Physical Device → Module → Object → Configuration**

Each level answers a different question:

| Level | Meaning | Reference |
| --- | --- | --- |
| Physical Device | The installed hardware identified as one product instance | [`physical-devices.md`](physical-devices.md) |
| Module | A firmware-exposed logical container within the Device | [`modules.md`](modules.md) |
| Object | The function assigned to or exposed by a Module | [`objects.md`](objects.md) |
| Virgin Object | A catalogue definition that constrains which Objects a Module may become | [`virgin-objects.md`](virgin-objects.md) |
| Configuration | The address, mode, parameters, and other values applied to an Object | [`configuration.md`](configuration.md) |

## Model boundary

A Physical Device is not equivalent to one OpenWebNet address or one functional `WHO`. A Device can expose several Modules, and its Modules can implement different Objects or participate in different functional systems.

A Module is the firmware-exposed logical object or container presented by the Device. The term **internal slot** is reserved for the numeric slot or index carried by diagnostic frames and represented by catalogue structures.

An Object describes an individual logical function. It is distinct from the Device itself and from the configuration currently applied to that function.

Configuration supplies the instance-specific values that make an Object operational, such as `A`/`PL`, groups, operating modes, and Object-specific parameters.

## Evidence domains

The model is reconstructed from complementary sources:

| Source | Contribution |
| --- | --- |
| MyHOME_Suite catalogue data | Device models, Modules, Objects, Virgin Objects, configuration definitions, and relationships |
| Diagnostic protocol | Device identity, Module/Object discovery, and readable configuration state |
| Programming protocol | Configuration writes and lifecycle operations |
| Functional protocol | Runtime commands, events, states, and measurements emitted or consumed by configured Objects |

Identifiers from different databases and protocol fields remain separate unless an explicit relationship or corroborated mapping establishes equivalence.

## Reference organization

The pages in this section define the conceptual model and its implementation vocabulary. Diagnostic frame sequences remain under `diagnostics/`; configuration-write workflows remain under `programming/`; functional traffic remains under the corresponding `WHO` in `functional/`.

Database table and column names are retained verbatim when referenced. User-facing descriptions follow MyHOME_Suite terminology: the Physical Device description comes from the Device catalogue entry, while an Object description identifies an individual logical function.
