# Practical Guides

Practical Guides start from an installer or application goal and raw OpenWebNet evidence, then follow the complete resolution path to structured, user-presentable data or a safely validated action. They combine the canonical protocol, Device Model, diagnostics, programming, and MyHOME_Suite implementation references.

Each guide must stand on its own as a complete end-to-end example rather than an alternative protocol specification. When an example and a canonical reference appear to differ, follow the canonical page and record the discrepancy.

## Guides

| Starting goal | Practical guide |
| --- | --- |
| Build an identified inventory of installed Devices | [Discover and Identify Devices](discover-devices.md) |
| Turn raw interview frames into a user-presentable Device configuration | [Read and Present a Device Configuration](read-device-configuration.md) |
| Decide whether a candidate value is allowed | [Validate a Configuration Value](validate-configuration-value.md) |
| Construct and execute a programming session | [Program a Device](program-device.md) |
| Prove the effective state after programming | [Verify Programming](verify-programming.md) |
| Explain incomplete scans and interviews | [Troubleshoot Diagnostics](troubleshoot-diagnostics.md) |

## Guide structure

Every guide should:

1. state the user or installer goal;
2. identify the required raw frames and other inputs;
3. resolve every protocol and database identifier in context;
4. transform raw values into user-presentable concepts;
5. apply validation and stop conditions;
6. define the final output or action;
7. preserve provenance, ambiguity, and unresolved semantics.

Concrete captures can be substituted into these workflows without changing their resolution rules. Examples must never invent missing frames, catalogue mappings, display labels, or Device behavior.

## Safety model

Read-only discovery should precede programming. Before any write:

1. identify the installed Device and firmware;
2. resolve every affected Module and Object;
3. validate the complete intended state;
4. preserve the previous state;
5. prepare diagnostic read-back;
6. stop on ambiguity.

Advanced Object programming begins by resetting all Objects. A partially validated payload is therefore unsafe.
