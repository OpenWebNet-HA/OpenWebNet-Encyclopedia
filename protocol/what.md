# Overview

`WHAT` identifies a command, state, or event within the system selected by `WHO`.

A `WHAT` value has meaning only in the context of its `WHO`. It must therefore be represented semantically as the pair `(WHO, WHAT)`, not as a globally unique command identifier.

## Syntax

The common command/status frame places `WHAT` between `WHO` and `WHERE`: `*WHO*WHAT*WHERE##`.

Some operations extend `WHAT` with one or more `#`-introduced parameters. The number, order, range, and meaning of those parameters are defined by the corresponding system.

## Scope

The same numeric `WHAT` can identify unrelated operations in different systems. For example, a value defined by Lighting must not be interpreted using the Automation or scenario-management command table.

For this reason, this page defines the common concept only. Complete `WHAT` tables belong in the reference for the corresponding functional, diagnostic, or programming system.

## Implementation model

A protocol implementation should retain at least:

| Field | Purpose |
| --- | --- |
| `WHO` | Selects the command namespace |
| `WHAT` | Selects the operation or state within that namespace |
| Parameters | Carries any `WHAT`-specific arguments |
| Direction/session | Distinguishes command, state, and event use where required |

See [`frame-syntax.md`](frame-syntax.md) for frame structure and [`addressing.md`](addressing.md) for `WHERE` parsing.