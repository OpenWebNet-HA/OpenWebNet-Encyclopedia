# Overview

`WHAT` identifies a command, state, or event within an OpenWebNet `WHO`.

A `WHAT` value is meaningful only in the context of its `WHO`. The semantic identity of an operation is therefore `(WHO, WHAT)`, not `WHAT` alone.

## Frame position

The normal command/status form is `*WHO*WHAT*WHERE##`.

`WHAT` can include parameters introduced with `#` when defined by the selected system. Parameter structure is part of the `WHAT` grammar for that `WHO` and must not be interpreted globally.

## Scope

A numeric `WHAT` value can have unrelated meanings in different systems. Implementations should therefore resolve `WHO` before interpreting `WHAT`.

System-specific `WHAT` reference tables belong with the corresponding functional or diagnostic system documentation rather than in a global value table.

## Relationship to `DIMENSION`

`WHAT` represents commands, states, and events expressed through the normal frame family. Properties read or written through `*#WHO...` frames are identified by `DIMENSION` instead. See [`dimensions.md`](dimensions.md).

The distinction is structural rather than purely semantic: the same real-world function can expose command behavior through `WHAT` and state or configuration data through one or more `DIMENSION` identifiers.

See [`frame-syntax.md`](frame-syntax.md) for the common frame forms and [`addressing.md`](addressing.md) for `WHERE` interpretation.