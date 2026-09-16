# Overview

OpenWebNet is a frame-based protocol used to exchange commands, status information, measurements, configuration data, and service information between compatible systems.

A frame identifies a system through `WHO`, an operation or state through `WHAT` where applicable, and a recipient through `WHERE`. `DIMENSION` frames add a `DIMENSION` identifier and zero or more values.

## Core concepts

| Concept | Purpose | Reference |
| --- | --- | --- |
| `WHO` | Selects the OpenWebNet system or function family | System-specific documentation |
| `WHAT` | Identifies a command, event, or state within a `WHO` | [`what.md`](what.md) |
| `WHERE` | Identifies the destination or source according to the addressing rules of the `WHO` | [`addressing.md`](addressing.md) |
| `DIMENSION` | Identifies a readable or writable property within a `WHO` | [`dimensions.md`](dimensions.md) |
| `ACK` / `NACK` | Reports positive or negative acknowledgement | [`acknowledgements.md`](acknowledgements.md) |

`WHAT`, `WHERE`, and `DIMENSION` are not globally uniform namespaces. Their syntax and semantics depend on the selected `WHO`.

## Frame families

The common functional frame families are summarized below. See [`frame-syntax.md`](frame-syntax.md) for the complete structural reference.

| Purpose | Form |
| --- | --- |
| Command or status | `*WHO*WHAT*WHERE##` |
| Status request | `*#WHO*WHERE##` |
| `DIMENSION` request | `*#WHO*WHERE*DIMENSION##` |
| `DIMENSION` response | `*#WHO*WHERE*DIMENSION*VALUE...##` |
| `DIMENSION` write | `*#WHO*WHERE*#DIMENSION*VALUE...##` |
| Positive acknowledgement | `*#*1##` |
| Negative acknowledgement | `*#*0##` |

Fields can contain additional parameters. Their exact grammar is defined by the relevant system and operation.

## Reference organization

This directory defines concepts shared by OpenWebNet systems. Functional command values and `DIMENSION` identifiers are documented with their corresponding `WHO`, because identical numeric identifiers can have unrelated meanings in different systems.

Diagnostic and programming protocols use the same frame language while defining their own operations, `DIMENSION` identifiers, sequences, and addressing rules.