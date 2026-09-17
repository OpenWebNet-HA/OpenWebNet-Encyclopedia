# Inspect Configuration State

## Goal

Determine which firmware-exposed Modules are configured and which remain in a Virgin Object state.

## Inputs

Use all `DIMENSION 30` responses from one completed Device interview:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

## Procedure

1. Group records by installed Device interview.
2. Key Modules by protocol `SLOT` without renumbering them to match the UI.
3. For `STATE = 1`, resolve `KEYO` through `EN_KEY_OBJECT.key_object`.
4. For `STATE = 0`, resolve `KEYO` through `EN_VIRGIN_OBJECT.virgin_key_object`.
5. For a Virgin Object, derive candidate configured Objects through `AS_OBJECT_VIRGIN_OBJECT`.
6. Intersect candidates with firmware and slot support.
7. Attach `DIMENSION 32` and `35` records only when Device and internal slot both match.
8. Preserve absent Modules, fixed Objects, and UI-hidden Modules as distinct cases.

## Result classification

| State | Interpretation |
| --- | --- |
| configured | `STATE = 1` and Object resolves |
| unconfigured | `STATE = 0` and Virgin Object resolves |
| inconsistent | state-specific namespace does not resolve |
| incomplete | the interview ended without enough Module evidence |
| error | `DIMENSION 31` reports a Module/Object condition |

An unconfigured Module is not semantically empty. Its Virgin Object describes the role and constrains what it can become.

## Expected result

A Module table containing internal slot, configured state, Object or Virgin Object, permitted target set, address availability, and parameter availability.

See [`DIMENSION 30`](../diagnostics/dim30-modules.md), [Modules](../device-model/modules.md), and [Virgin Objects](../device-model/virgin-objects.md).
