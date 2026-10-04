# Execution Model

The ScenarioDevices databases define editor capabilities, not a complete runtime state machine. This page separates the execution behavior that can be derived from stored templates from behavior that requires other evidence.

## Established pipeline

For an action with a literal OpenWebNet template, a safe application can:

1. resolve the selected Object System, Device Object, Command, and Parameters;
2. confirm the Command belongs to an action category;
3. resolve the target installed Device/Module using diagnostics and the Device Model;
4. validate the target functional address under the stored or parsed `WHO`;
5. validate and encode every Parameter;
6. render and reparse the complete frame;
7. send it through the appropriate command session, authenticated where the selected gateway requires it;
8. collect acknowledgement and functional state evidence where applicable;
9. record the action result independently from the scenario's future control flow.

Steps 1 through 6 are partly represented by ScenarioDevices. Transport/session behavior, acknowledgements, retries, scheduling, and state persistence are not defined by these tables.

## Trigger and condition model

Event and condition Commands commonly have `Frame=NULL`. Their resource keys, category, IDs, matching IDs, address metadata, and Parameters still describe editor concepts, but the database does not directly provide a complete incoming-frame matcher.

Possible runtime inputs include:

- an event decoded elsewhere and identified by `CommandId`;
- application code mapping functional frames to Commands;
- a separate persistence or capability layer;
- matching identifiers linking incoming concepts with actions;
- non-bus events such as time, delay, or Virtual Key Card activity.

The current evidence does not select one universal mechanism.

## Matching semantics

`ObjectMatchingId` and `CommandMatchingId` demonstrably group related lighting and hotel concepts across category rows. A runtime or editor can use this relationship to find semantic counterparts, but the database does not specify whether matching is used for:

- event subscription;
- condition evaluation;
- suggested action selection;
- display grouping;
- serialization compatibility.

Document the grouping; keep the runtime purpose provisional.

## Scenario graph boundary

The four ScenarioDevices tables contain no identified scenario-instance, node, edge, ordering, branch, schedule, or execution-history model. The inspected schemas and contents establish a capability catalogue, not a recovered persistence format for user-authored scenario graphs. This bounded finding does not prove where the application stores graphs or exclude an unexamined serialization mechanism.

A complete engine model still needs evidence for:

| Concern | Missing evidence |
| --- | --- |
| scenario identity | instance table or file format |
| graph structure | nodes, edges, branches, ordering |
| trigger bindings | mapping from runtime events to stored Commands |
| condition state | evaluation operands and persistence |
| action ordering | serial, parallel, delayed, or transactional behavior |
| error policy | retry, continue, abort, compensation |
| scheduling | clocks, recurrence, timezone, missed-event handling |
| runtime state | active executions and recovery after restart |

## Action execution algorithm

```text
function execute_literal_action(capability, target, inputs):
    require capability category is action
    require capability Frame is literal OpenWebNet syntax

    address = resolve target under functional WHO grammar
    parameters = validate and encode all capability Parameters
    frame = render placeholders atomically
    parsed = parse rendered frame

    require parsed WHO agrees with established capability context
    require parsed WHERE agrees with selected target
    require no placeholder remains

    send frame through the appropriate command transport
    collect ACK/NACK and applicable state feedback

    return transmitted frame, raw responses, and classified result
```

Do not generalize this action algorithm to triggers, conditions, symbolic frames, delay rows, or time-based rows.

## Result classification

| Result | Meaning |
| --- | --- |
| rendered | a complete frame was produced and validated, but not sent |
| transmitted | transport accepted the outgoing bytes; Device effect not yet proven |
| acknowledged | an applicable positive acknowledgement was received |
| rejected | `NACK` or another explicit rejection was received |
| observed effective | later functional state evidence matches the intended action |
| timeout | no terminal evidence arrived within the applicable window |
| indeterminate | transport loss or ambiguous feedback prevents a conclusion |
| unresolved capability | template, address, Parameter, or symbolic mapping was insufficient |

An acknowledgement and an observed state change answer different questions and should not be collapsed into one success flag.

## Historical touchscreen condition evaluation

The BTicino touchscreen `libqtcommon` condition evaluator provides a separate application model. Its tests establish that initial Lighting state initializes a condition without firing it, repeated satisfied states do not fire again, and a later unsatisfied-to-satisfied transition emits the condition event.

Saving an unchanged predicate neither re-requests state nor rearms it. For a changed predicate, the evaluator clears a previously satisfied state while preserving initialization; the next matching state can therefore fire. If the old predicate was unsatisfied, it clears initialization and suppresses the next managed state event. Unrelated values do not initialize a predicate.

Initialization is condition-specific: the Auxiliary test permits the first matching `WHO 9` state to fire, then suppresses repeats. Other tested predicates include inclusive dimmer/volume ranges and a temperature band of ±10 tenths of the selected scale around the threshold, giving ±1.0 °C or ±1.0 °F. These are application operands, not Device thresholds. A bare dimmer ON value without a level substitutes local value `1`; it does not establish a measured output level. Volume evaluation uses the cached amplifier ON state; ON alone does not supply a volume operand.

The product's advanced-scenario tests also establish enable and weekday gating. With both time and Device conditions, a Device transition alone does not start the action: the time event checks the current Device condition. Without a time condition, the Device event can start the action. The action sends its configured literal frame through the command writer.

| Advanced-scenario control | Touchscreen behavior |
| --- | --- |
| Automatic trigger | Requires enabled state and the current weekday; time and Device gates apply as above |
| Manual Start | Sends the action directly, bypassing enabled, weekday, time and Device gates |
| Enable / disable | Changes and persists a local flag; does not send a `WHO 17` command or itself trigger the action |
| Weekday selection | Bit `0` is Monday, bit `6` Sunday; editable weekday values also govern automatic execution before Save |

Time conditions use the touchscreen's local clock and a single-shot timer, rearmed after timeout. Date/time notifications recalculate the interval from that local clock; their payload is not used as the trigger time. The implementation wraps the interval within 24 hours, without establishing calendar recurrence, daylight-saving handling or recovery of missed events. Resetting editable time values does not immediately rearm the timer.

Advanced-scenario Configuration selects active time and Device conditions and a literal action frame. Action type and Command IDs supply descriptions; they do not render or select the frame's namespace. A scheduled-scenario control instead sends separately configured Start, Stop, Enable and Disable frames when present. Its label does not establish a touchscreen scheduler or execution-state feedback. Use the literal frame to distinguish [`WHO 17`](../functional/who-17-scenario-management/), [`WHO 15` CEN](../functional/who-15-cen/), and [`WHO 25` CEN+ or Scenario Plus](../functional/who-25-transversal/).

Local “started” notifications follow action dispatch and do not establish acknowledgement or Device execution. See [Scenario and condition history evidence](../project/review/myopencommunity-scenario-history-review.md#conditions-and-automatic-execution) for assertion scope and historical corrections.

This is implementation evidence for the touchscreen engine at `TS10_1_0_23`. It does not resolve MyHOME Suite ScenarioDevices matching IDs, graph persistence, or a universal OpenWebNet trigger policy. See [Application condition evidence](../project/review/myopencommunity-integration.md#application-condition-evaluation) and [Additional predicate and scheduling evidence](../project/review/myopencommunity-reassessment.md#condition-and-scenario-behavior).

## Historical touchscreen alarm-clock scheduling

BtExperience's alarm clocks at `TS10_1_0_23` use a separate local scheduler and ordinary [sound controls](../functional/who-22-sound-diffusion/#historical-alarm-clock-control).

| Setting / event | Application behavior |
| --- | --- |
| Weekdays | Bit `6` is Monday, bit `0` Sunday, reversing the advanced-scenario order above |
| No selected weekdays | One-shot alarm; triggering disables subsequent automatic scheduling |
| Enabled state | Arms the automatic timer; disabling stops it. Direct calls to the trigger method do not themselves check enabled state |
| Next trigger | Uses the local date and selected hour/minute; a time already reached schedules the following day. Selected weekdays are checked at timeout, then the timer is rearmed |
| Editable time / weekdays | Changed values recalculate the timer before Save; Reset emits changes and recalculates it too |
| Date/time report | Recalculates from the touchscreen clock, without using the report payload as the alarm time |
| Snooze restart | Resets the tick counter within a nominal 30-minute window from the original start; its time-of-day comparison does not establish correct behavior across midnight or clock changes |

Configuration stores volume in tens of percentage points, resolves the amplifier by an application Object reference, and selects the first configured source of the requested type. These fields are not bus addresses or a general OpenWebNet alarm schema. The scheduler does not establish missed-event recovery or duplicate-trigger suppression. Earlier implementations and corrections are scoped in [Alarm-clock history evidence](../project/review/myopencommunity-alarm-clock-history-review.md).

## Relationship to `OPEN.db`

`OPEN.db` describes MyHOME_Suite communication scenarios for diagnostics and Device programming. It does not define the Scenario Engine graph or replace the functional meanings of ScenarioDevices action frames.

Use the common OpenWebNet session documentation for transport behavior and the functional `WHO` pages for command semantics. Do not search for ScenarioDevices row IDs in `OPEN.db` unless a separate mapping is established.
