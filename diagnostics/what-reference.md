# Diagnostic `WHAT` Reference

Diagnostic `WHAT` values control discovery and interview sessions. Their meaning is scoped to a diagnostic `WHO`; matching numeric values in a functional `WHO` are unrelated unless independently documented.

## Values

| `WHAT` | Direction | Frame | Meaning in `OPEN.db` |
| ---: | --- | --- | --- |
| `4` | Device → programmer | `*[WHO]*4*[WHERE_FAKE]##` | Device end of transmission |
| `4` | Device → programmer | `*[WHO]*4*0##` | end-of-transmission variant |
| `5` | Programmer → Device | `*[WHO]*5*0##` | start diagnosis through local-button/general mode |
| `6` | Either diagnostic participant in source labels | `*[WHO]*6*0##` | abort/close diagnosis |
| `10` | Programmer → Device | `*[WHO]*10#[ID]*0##` | start diagnosis by Device ID |
| `11` | Programmer → Device | `*[WHO]*11#[ID]*0##` | mark/suppress an ID already found during enumeration |
| `12` | Programmer → Device | `*[WHO]*12*0##` | release/reset Device-ID enumeration state |

These values are management operations inside the selected diagnostic family. The same numeric `WHAT` under another `WHO`, or in a programming lifecycle, can have different semantics.

## `WHAT 4`: end of transmission

`WHAT 4` is the positive terminal marker for a Device interview. The main diagnostic sequences place it after identity, version, health, Module, address, and applicable error responses.

The `[WHERE_FAKE]` label is an implementation label, not a general OpenWebNet field type. Preserve the received value but do not treat it as a newly discovered functional address. `OPEN.db` also contains the `*[WHO]*4*0##` form.

The sequence metadata does not mark the end frame mandatory, even though observed interviews use it as the normal completion marker. A collector must retain timeout and abort completion states separately.

## `WHAT 5`: local/general start

`WHAT 5` begins the `DiagLocalButton` sequence. The database name implies a local-button workflow, while the wire frame itself carries neither Device ID nor address. Device selection therefore depends on external/local state not represented in the frame.

Do not use this mode when several Devices could respond unless the installation procedure provides a reliable physical selection step.

## `WHAT 6`: abort or close

`OPEN.db` contains programmer-abort and Device-abort entries with the same frame. Treat it as a session-closing signal whose origin must be derived from transport direction and active state.

An abort does not certify that a full response set was received. Keep partial data marked incomplete.

## `WHAT 10`: interview by ID

`WHAT 10` selects one installed Device by its 32-bit ID and begins a full interview. It is distinct from the `DIMENSION 13` request used to enumerate IDs.

## `WHAT 11`: suppress a discovered ID

During ID enumeration, the programmer sends `WHAT 11` for each returned ID. The `ScanAID` sequence repeats this operation before requesting IDs again. Observed traffic supports interpreting it as suppressing or acknowledging an already enumerated Device for the current scan state.

This is scan control, not a permanent Device configuration change.

## `WHAT 12`: release enumeration state

`WHAT 12` brackets ID enumeration. Send it before a new scan and after the final empty pass so Device-side scan state does not leak into the next operation.

The frame carries no Device ID and applies to the selected diagnostic `WHO` scope.

## Related programming values

The same `OPEN.db` registry also contains programming operations such as `WHAT 9` for configuration by Device ID and programming-specific `WHAT 1`, `2`, `3`, `7`, `14`, `51`, and `52`. They are outside this diagnostic reference and belong under [`programming/`](../programming/). Their presence is one reason the `diag_open` database flag must not be treated as a diagnostics-only classification.
