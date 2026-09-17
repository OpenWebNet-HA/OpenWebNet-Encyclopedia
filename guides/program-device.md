# Program a Device

## Goal

Apply a completely validated Virtual configuration and preserve enough evidence to recover and verify the Device.

## Prerequisites

- resolved Device and firmware;
- complete current-state snapshot;
- complete validated intended state;
- selected canonical programming scenario;
- prepared diagnostic verification plan.

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
3. Send reset-all only after the entire replacement payload has passed validation.
4. Send every required `DIMENSION 30` Object assignment.
5. Send applicable `DIMENSION 32` addresses after their Object assignments.
6. Send applicable `DIMENSION 35` properties.
7. Send programmer `*[WHO]*4*0##` to end the transfer payload.
8. Classify `WHAT 52`, `WHAT 51`, structured errors, warnings, abort, or timeout.
9. Close the outer session with `*[WHO]*2*0##` when the workflow reaches close.
10. Start a new diagnostic session for verification.

## Safety gates

Do not send reset-all if any Module, Object, address, property, filter, dependency, or encoded value remains ambiguous. Do not resume an interrupted replacement payload at an arbitrary later frame.

## Expected result

A programming record containing the scenario, selected Device, ordered transmitted frames, every response and timer transition, terminal classification, and verification request.

See [Programming Session Lifecycle](../programming/session-lifecycle.md), [Programming Error Handling](../programming/error-handling.md), and [Programming Validation](../programming/validation.md).
