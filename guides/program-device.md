# Program a Device

## Goal

Apply a completely validated Virtual configuration and preserve enough evidence to recover and verify the Device.

## Prerequisites

- resolved Device and firmware;
- complete current-state snapshot;
- complete validated intended state;
- selected canonical programming scenario;
- prepared diagnostic verification plan.

## Start the programming scenario and acquire its projection

Select the Device and start the applicable scenario:

| Selection | Send | First-response window |
| --- | --- | ---: |
| diagnostic address | `*[WHO]*1*[WHERE]##` | 15 s |
| Device ID | `*[WHO]*9#[ID]*0##` | 15 s |
| local interaction | `*[WHO]*1*[WHERE]##`, then perform the Device-side interaction | 300 s |

The address and local-interaction entries use the same stored frame template. Their operational distinction is the installer interaction and timeout; `OPEN.db` does not fully explain how the frame `WHERE` and physical selection are coordinated.

Collect the initial Device projection through Device `WHAT 4` or an explicit abort/timeout. Confirm its identity, firmware, Module/Object state, and Device ID against the validated target before sending any configuration write.

## Choose the scenario

| Selection | Canonical scenario | Transfer |
| --- | --- | --- |
| diagnostic address | `ConfPoint2PointByAddress` | virtual-configurator transfer |
| Device ID | `ConfPoint2PointWithID` | repeated advanced Object transfer |
| local interaction | `ConfLocalButton` | advanced Object and virtual-configurator transfer |

Virtual configuration is the umbrella for configuration performed through MyHOME_Suite. Advanced Object programming and virtual-configurator transfer are mechanisms within it.

## Advanced Object procedure

1. Start the ID or local-interaction scenario.
2. Confirm the returned identity projection matches the intended Device.
3. Send reset-all `*[WHO]*14#0*0##` only after the entire replacement payload has passed validation.
4. Send every required Object assignment as `*#[WHO]*0*#30*[SLOT]*[KEYO]##`.
5. Send applicable addresses after their Object assignments as `*#[WHO]*0*#32#[SLOT]*[SYS]*[ADDR]##`.
6. Send applicable properties as `*#[WHO]*0*#35#[INDEX]#[SLOT]*[VAL_PAR]##`.
7. Send programmer `*[WHO]*4*0##` to end the transfer payload.
8. Classify `WHAT 52`, `WHAT 51`, structured errors, warnings, abort, or timeout.
9. Close the outer session with `*[WHO]*2*0##` when the workflow reaches close.
10. Start a new diagnostic session for verification.

## Virtual-configurator procedure

For a scenario containing `ConfConfigurators`:

1. send positions 1–6 as `*#[WHO]*0*#4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##`;
2. where applicable, send positions 7–12 as `*#[WHO]*0*#5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##`;
3. collect Device configurator reports, `WHAT 51`, abort, `NACK`, timeout, and Device `WHAT 4`;
4. do not wait for `WHAT 52`, which is not a canonical member of `ConfConfigurators`.

The precise field-level meaning of `C1`–`C12` remains unresolved. Send only values derived from an established MyHOME_Suite configuration workflow.

## Safety gates

Do not send reset-all if any Module, Object, address, property, filter, dependency, or encoded value remains ambiguous. Do not resume an interrupted replacement payload at an arbitrary later frame.

## Expected result

A programming record containing the scenario, selected Device, ordered transmitted frames, every response and timer transition, terminal classification, and verification request.

See [Programming Session Lifecycle](../programming/session-lifecycle.md), [Programming Error Handling](../programming/error-handling.md), and [Programming Validation](../programming/validation.md).
