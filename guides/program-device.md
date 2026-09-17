# Program a Device

## Goal

Apply a completely validated Virtual configuration and preserve enough evidence to recover and verify the Device.

## Prerequisites

- resolved Device and firmware;
- complete current-state snapshot;
- complete validated intended state;
- selected canonical programming scenario;
- prepared diagnostic verification plan.

## Acquire and preserve the pre-programming state

Do not rely on a snapshot from an earlier application session.

Start a read-only diagnostic interview with the same Physical Device:

| Selection method | Send |
| --- | --- |
| Device ID | `*[WHO]*10#[ID]*0##` |
| diagnostic address | `*#[WHO]*[WHERE]*0##` |
| local interaction | `*[WHO]*5*0##`, then perform the Device-side interaction |

Collect identity, versions, Device ID, repeated `DIMENSION 30` and `32`, errors, and the terminal condition. Use the applicable 15-second ID/address or 300-second local first-response window, followed by the 20-second further-information window.

After resolving the Module/Object layout, send:

`*#[WHO]*0*38#0##`

Collect repeated `DIMENSION 35`, applicable `DIMENSION 39`, and any `DIMENSION 310` response during the eight-second detailed-read window.

Resolve this evidence into a complete snapshot containing:

- installed Device ID and catalogue identity candidates;
- firmware and hardware evidence;
- every reported Module and configured/unconfigured state;
- each Object or Virgin Object;
- addresses;
- indexed and special properties;
- raw frames and field-level resolution status.

Store the snapshot before opening the programming scenario. It is both the validation input and the recovery baseline; it is not proof that the Device can automatically be restored after a failed reset.

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

### SQL example: inspect the selected `OPEN.db` scenario

Use the scenario label from the table above as `:scenario_label`:

```sql
SELECT
    sc.id_scenario,
    sc.scenario_label,
    sc.descr AS scenario_description,
    ss.sequence_order,
    ss.repeated_sequence,
    seq.id_sequence,
    seq.sequence_label,
    seq.descr AS sequence_description,
    os.open_order,
    os.mandatory_open,
    os.repeated_open,
    os.status4nack,
    os.status4error,
    o.id_open,
    o.open_label,
    o.open_string,
    o.diag_open,
    o.error_open
FROM EN_SCENARIO AS sc
JOIN AS_SCENARIO_SEQUENCE AS ss
  ON ss.id_scenario = sc.id_scenario
JOIN EN_SEQUENCE AS seq
  ON seq.id_sequence = ss.id_sequence
JOIN AS_OPEN_SEQUENCE AS os
  ON os.id_sequence = seq.id_sequence
JOIN EN_OPEN AS o
  ON o.id_open = os.id_open
WHERE sc.scenario_label = :scenario_label
ORDER BY ss.sequence_order, os.open_order;
```

Retrieve the timeout transitions for the same scenario rather than hard-coding only the nominal path:

```sql
SELECT
    sc.scenario_label,
    ss.sequence_order,
    seq.sequence_label,
    o.open_label,
    o.open_string,
    t.timeout_label,
    t."default" AS timeout_value,
    t.type AS timeout_type,
    tos.action,
    tos.status4timeout
FROM EN_SCENARIO AS sc
JOIN AS_SCENARIO_SEQUENCE AS ss
  ON ss.id_scenario = sc.id_scenario
JOIN EN_SEQUENCE AS seq
  ON seq.id_sequence = ss.id_sequence
JOIN AS_TIMEOUT_OPEN_SEQUENCE AS tos
  ON tos.id_sequence = seq.id_sequence
JOIN EN_OPEN AS o
  ON o.id_open = tos.id_open
JOIN EN_TIMEOUT AS t
  ON t.id_timeout = tos.id_timeout
WHERE sc.scenario_label = :scenario_label
ORDER BY ss.sequence_order, seq.id_sequence, o.id_open, t.id_timeout;
```

The database describes stored members and transitions. It does not eliminate the need for the capture-backed cautions in this guide, including the unresolved coordination of address and local-button selection.

## Prepare the complete replacement payload

Programming is not a patch operation at the safety-model level. Build the complete intended Device state before transmitting the first destructive frame.

For every reported or intended Module, retain:

| Field | Required evidence |
| --- | --- |
| internal slot | raw `DIMENSION 30.SLOT` and catalogue slot support |
| configured state | intended enabled/unconfigured state |
| Object | external `key_object` and internal `id_key_object` |
| address | encoded `SYS` and `ADDR`, plus decoded components |
| properties | each `INDEX`, encoded `VAL_PAR`, and selected `id_conf` |
| dependencies | linked properties and conditions used during validation |
| expected read-back | expected `DIMENSION 30`, `32`, `35`, or `310` value |

Validate every value as described in [Validate a Configuration Value](validate-configuration-value.md). Then validate the configuration as a whole:

1. every target Object is allowed for its Virgin Object, firmware, and slot;
2. no two Modules create a forbidden address or role conflict;
3. all linked-property rules are evaluated against the final state, not a mixture of old and new values;
4. every required property is present;
5. hidden or fixed properties required by the Device are preserved or regenerated;
6. each semantic value has exactly one established wire encoding;
7. the payload can be ordered without forward references that violate the selected scenario;
8. a read-back expectation exists for every transmitted assignment.

Keep the previous snapshot and the intended snapshot as separate immutable records.

### Construct the ordered frames

For advanced Object programming, order the payload as:

1. reset all Objects;
2. Object assignments by internal slot;
3. addresses after the corresponding Object exists;
4. properties after the corresponding Object exists;
5. programmer end marker;
6. outer-session close when the selected scenario reaches that state.

Within each class, use the ordering established by the canonical scenario and verified captures. Do not assume arbitrary slot or property ordering is accepted merely because the wire grammar can represent it.

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

## Reference programming algorithm

```text
function program_device(selector, intended_state):
    previous = acquire_and_resolve_fresh_snapshot(selector)
    require previous identity matches the requested Physical Device

    validation = validate_complete_intended_state(previous, intended_state)
    if validation contains invalid, ambiguous, unknown, or missing requirements:
        stop before entering programming

    scenario = select canonical scenario from selection method
    projection = start scenario and collect through its projection terminator
    require projection identity and firmware are compatible with validation

    journal = durable append-only programming record
    state = "selected"

    try:
        if scenario uses advanced Objects:
            send_and_journal(reset_all)
            state = "reset sent"

            for assignment in ordered_object_assignments:
                send_and_journal(assignment)

            for address in ordered_addresses:
                send_and_journal(address)

            for property in ordered_properties:
                send_and_journal(property)

            send_and_journal(programmer_end)

        if scenario uses virtual configurators:
            send_and_journal(configurator_positions_1_to_6)
            if positions_7_to_12 are established and required:
                send_and_journal(configurator_positions_7_to_12)

        collect and classify every response, error, warning, NACK, and timeout

        if scenario reaches its close state:
            send_and_journal(outer_session_close)

    except transport_loss or cancellation:
        record last definitely transmitted frame
        record last acknowledged or observed Device state
        do not resume at the next unsent frame
        classify Device state as indeterminate

    verification = start a new diagnostic session
    compare complete effective state with intended_state

    return journal, terminal classification, verification result
```

The journal should be durable before a destructive frame is sent. At minimum it contains timestamps, direction, raw frame, scenario/sequence state, timeout state, and the intended semantic operation.

## Response and failure handling

| Observation | Action |
| --- | --- |
| expected success/progress response | record it and continue only if the scenario permits |
| `WHAT 51` or `WHAT 52` | interpret in the active sequence; do not assign one global meaning |
| structured programming error | attach it to the affected operation and stop or transition as defined |
| warning | retain it; continue only when the scenario and safety policy allow |
| `NACK` | classify the active frame as rejected and stop the replacement transfer |
| timeout before destructive work | abort without changing the Device |
| timeout after reset or a write | mark Device state indeterminate; close if safe, then diagnose |
| transport loss | never assume the last write was or was not applied |
| user cancellation | treat like transport interruption once destructive work has started |

After any interruption following reset-all, do not resume from the next frame. Re-interview the Device, rebuild the effective state, and decide whether to restart the entire validated replacement workflow.

## Safety gates

Do not send reset-all if any Module, Object, address, property, filter, dependency, or encoded value remains ambiguous. Do not resume an interrupted replacement payload at an arbitrary later frame.

## Expected result

A programming record containing the scenario, selected Device, ordered transmitted frames, every response and timer transition, terminal classification, and verification request.

See [Programming Session Lifecycle](../programming/session-lifecycle.md), [Programming Error Handling](../programming/error-handling.md), and [Programming Validation](../programming/validation.md).
