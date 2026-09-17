# Practical Guides

Practical Guides explain how to achieve installation-level goals by combining the canonical protocol, Device Model, diagnostics, programming, and MyHOME_Suite implementation references.

These pages are procedures, not alternative protocol specifications. When a guide and a canonical reference appear to differ, follow the canonical page and record the discrepancy.

## Guides

| Goal | Guide |
| --- | --- |
| Build an inventory of installed Devices | [Discover Devices](discover-devices.md) |
| Resolve one response to a catalogue Device | [Identify a Device](identify-device.md) |
| Determine whether Modules are configured | [Inspect Configuration State](inspect-configuration-state.md) |
| Read Objects, addresses, and indexed values | [Read Device Configuration](read-device-configuration.md) |
| Map an indexed value to its catalogue definition | [Resolve a Configuration Property](resolve-configuration-property.md) |
| Decide whether a candidate value is allowed | [Validate a Configuration Value](validate-configuration-value.md) |
| Construct and execute a programming session | [Program a Device](program-device.md) |
| Prove the effective state after programming | [Verify Programming](verify-programming.md) |
| Compare physical and Virtual configuration | [Physical and Virtual Configuration](physical-and-virtual-configuration.md) |
| Diagnose incomplete scans and interviews | [Troubleshoot Diagnostics](troubleshoot-diagnostics.md) |
| Follow complete examples | [Worked Examples](worked-examples/) |

## Guide structure

Each guide identifies its goal, prerequisites, inputs, procedure, database resolution, validation gates, expected result, and canonical reference pages. Examples preserve raw frames and distinguish established behavior, inference, and unresolved semantics.

## Safety model

Read-only discovery should precede programming. Before any write:

1. identify the installed Device and firmware;
2. resolve every affected Module and Object;
3. validate the complete intended state;
4. preserve the previous state;
5. prepare diagnostic read-back;
6. stop on ambiguity.

Advanced Object programming begins by resetting all Objects. A partially validated payload is therefore unsafe.
