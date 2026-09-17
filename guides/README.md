# Practical Guides

Practical Guides transform an installer or application goal and raw OpenWebNet evidence into structured, user-presentable data or a safely validated action. They combine the canonical protocol, Device Model, diagnostics, programming, and MyHOME_Suite implementation references.

These pages are procedures, not alternative protocol specifications. When a guide and a canonical reference appear to differ, follow the canonical page and record the discrepancy.

## Guides

| Goal | Guide |
| --- | --- |
| Build an identified inventory of installed Devices | [Discover and Identify Devices](discover-devices.md) |
| Turn raw interview frames into a user-presentable Device configuration | [Read and Present a Device Configuration](read-device-configuration.md) |
| Decide whether a candidate value is allowed | [Validate a Configuration Value](validate-configuration-value.md) |
| Construct and execute a programming session | [Program a Device](program-device.md) |
| Prove the effective state after programming | [Verify Programming](verify-programming.md) |
| Compare physical and Virtual configuration | [Physical and Virtual Configuration](physical-and-virtual-configuration.md) |
| Diagnose incomplete scans and interviews | [Troubleshoot Diagnostics](troubleshoot-diagnostics.md) |
| Follow complete examples | [Worked Examples](worked-examples/) |

## Guide structure

Each guide begins with a high-level goal, identifies its raw inputs, traces every protocol and database resolution step, and ends with a defined user-presentable result or validated action. Examples preserve raw frames and distinguish established behavior, inference, ambiguity, and unresolved semantics.

## Safety model

Read-only discovery should precede programming. Before any write:

1. identify the installed Device and firmware;
2. resolve every affected Module and Object;
3. validate the complete intended state;
4. preserve the previous state;
5. prepare diagnostic read-back;
6. stop on ambiguity.

Advanced Object programming begins by resetting all Objects. A partially validated payload is therefore unsafe.
