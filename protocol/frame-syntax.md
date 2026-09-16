# Overview

OpenWebNet frames are ASCII messages delimited by `*` and terminated by `##`. The meaning and permitted structure of individual fields depend on the frame family and selected `WHO`.

## Common frame forms

| Frame class | Syntax | Purpose |
| --- | --- | --- |
| Command/status | `*WHO*WHAT*WHERE##` | Command, state, or asynchronous event |
| Status request | `*#WHO*WHERE##` | Requests current state |
| Dimension request | `*#WHO*WHERE*DIMENSION##` | Requests a Dimension value |
| Dimension response | `*#WHO*WHERE*DIMENSION*VALUE...##` | Reports a Dimension value |
| Dimension write | `*#WHO*WHERE*#DIMENSION*VALUE...##` | Writes a Dimension value |
| `ACK` | `*#*1##` | Positive acknowledgement |
| `NACK` | `*#*0##` | Negative acknowledgement |

The ellipsis in `VALUE...` denotes zero or more additional `*`-separated values defined by that Dimension. It is notation used by this reference and is not transmitted.

## Delimiters

| Token | Role |
| --- | --- |
| `*` | Separates major frame fields |
| `##` | Terminates a frame |
| `#` | Introduces frame variants, advanced addressing, or parameterized fields according to context |

`#` does not have one context-independent meaning. Its interpretation follows the grammar of the field in which it appears.

## Command and status frames

The normal form is `*WHO*WHAT*WHERE##`. Depending on direction and session context, the same structural form can represent a command, a reported state, or an event.

`WHAT` can itself be parameterized. The valid syntax is defined by the selected `WHO`; see [`what.md`](what.md).

## Dimension frames

Dimension operations use the `*#WHO...` family. A read request identifies `WHO`, `WHERE`, and `DIMENSION`. A response repeats those fields and appends the Dimension values. A write prefixes the Dimension field with `#`.

Dimension identifiers and value layouts are scoped to their `WHO`. See [`dimensions.md`](dimensions.md).

## Addressing

`WHERE` is interpreted using the address grammar of the selected system. It must not be parsed as a universal A/PL value. See [`addressing.md`](addressing.md).

## Acknowledgements

`ACK` and `NACK` are standalone frames rather than `WHO`-specific command frames. See [`acknowledgements.md`](acknowledgements.md).