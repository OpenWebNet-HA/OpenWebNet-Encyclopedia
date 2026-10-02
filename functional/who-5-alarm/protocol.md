# Protocol

`WHO 5` uses ordinary OpenWebNet command/event frames together with status requests. The published interface is strongly status-oriented and often returns a sequence of state frames followed by `ACK`.

## Central-unit status request

A central-unit request uses `*#5##`. The response can contain multiple `WHO 5` frames before `*#*1##`. The published response set covers maintenance/active state, engaged/disengaged state, battery conditions, mains presence, zone engagement/division, zone alarm conditions, technical alarms and silent alarms.

A client must therefore collect the complete response sequence. Treating the first returned `WHO 5` frame as the complete central-unit state loses independent state axes.

## Zone status request

A zone request follows `*#5*#N##`, with published zones `N = 1..8`. The response identifies the zone as active/engaged with `WHAT 11` or non-active/divided with `WHAT 18`, followed by `ACK`.

The `#N` form is a zone selector, not a numeric point-to-point address. See [Addressing](addressing.md).

## Event connection

Alarm state changes are also emitted as events. Consumers should normalize events using the pair `(WHAT, WHERE)` because the same `WHAT` family can describe central-unit, zone, sensor, or auxiliary context depending on `WHERE`.

## Programming values

The published vocabulary includes `WHAT 26` and `27` for start/stop programming. These belong to the historical `WHO 5` functional protocol. They are not the same subsystem as the MyHOME_Suite Device/Object configuration protocol documented under [Programming](../../programming/).

## Historical password controls

The BTicino touchscreen implementation at `TS10_1_0_23` emits the following controls. These extend the published status-oriented surface; applicability to other alarm panels or gateway Firmware is not established.

| Operation | Implemented frame |
| --- | --- |
| Toggle armed/disarmed state using a password | `*5*36#PASSWORD*0##` |
| Set zone partialization | `*5*50#PASSWORD#MASK*0##` |
| Request central-unit state | `*#5*0##` |

`MASK` contains eight textual bits, left to right for zones `1..8`; `1` means partialized. For example, `11000001` selects zones 1, 2, and 8. The central target `0` is the library's form, distinct from the published request above. The password's format and acceptance rules are not established by the tests; do not log password-bearing frames unredacted.

When arming with changed partialization, the implementation sends `50`, waits 6 seconds, sends `36`, then waits another 5 seconds before requesting state. Other password controls are followed by a state request after 5 seconds. The application judges success from the resulting armed/zone state. These delays and the optimistic local state update are application choices, not protocol deadlines or proof that an ACK validates a password.

See [Alarm evidence](../../project/review/myopencommunity-integration.md#alarm-controls-and-events).

## Write support

Some published `WHAT` values describe system states rather than commands. Their presence in the vocabulary must not be interpreted as permission to transmit them as control operations. Where the corpus only establishes a value in responses/events, this reference treats it as report-only.

See [`WHAT` Reference](what.md) for values and [Addressing](addressing.md) for target syntax.