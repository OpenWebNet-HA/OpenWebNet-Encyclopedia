# Troubleshoot Diagnostics

## Goal

Classify incomplete discovery or interview results without converting silence, optionality, or ambiguous identity into false conclusions.

## Prerequisites

- the applicable diagnostic `WHO` and selection method;
- the exact request that should have produced the missing evidence;
- raw traffic with direction, order, and timestamps;
- the timeout and sequence state active when collection stopped;
- the relevant `OPEN.db` revision;
- catalogue identity and firmware candidates where the failure is interpretive rather than transport-level.

If raw traffic was not retained, reproduce the read-only request before drawing conclusions. Do not reproduce programming writes merely to troubleshoot a missing diagnostic response.

## Triage

| Symptom | Check first |
| --- | --- |
| no ID responses | diagnostic `WHO`, connection, release frame, timeout, family support |
| repeated same Device | suppression frame and exact 32-bit ID handling |
| no `WHAT 4` | further-response timer, abort, transport loss |
| missing `DIMENSION 32` | Object/firmware capability and optional response behavior |
| unknown `DIMENSION 30.KEYO` | `STATE`-selected Object versus Virgin Object namespace |
| unknown `DIMENSION 35.INDEX` | Device/firmware/slot/Object context |
| wrong product match | item mapping, brand/line, firmware, and SKU ambiguity |
| local-button timeout | installer interaction, 300-second window, Device capability |

## Reproduce the request

Troubleshooting begins with the frame that was supposed to produce the missing response:

| Missing evidence | Request to reproduce |
| --- | --- |
| Device IDs | release with `*[WHO]*12*0##`, then send `*#[WHO]*0*13##` |
| addressed identity | `*#[WHO]*[WHERE]*1##` |
| full interview | `*[WHO]*10#[ID]*0##` or `*#[WHO]*[WHERE]*0##` |
| local interview | `*[WHO]*5*0##`, then perform the local interaction |
| detailed properties | after resolving Modules, use `*#[WHO]*0*38#0##` only where its effects are established for the family and firmware |

The `DIMENSION 38` template is labelled reset/select despite its `DiagKO` retrieval role. It must not be included in a presumed read-only retry on an unfamiliar target. Preserve the uncertainty and obtain applicable evidence first.

Preserve the exact request, all returned frames, their direction and order, and the timer that ended collection. Do not troubleshoot a parsed value without retaining the request that elicited it.

## Procedure

1. Confirm the transport session and authentication.
2. Record the exact request and diagnostic family.
3. Check whether the expected response is mandatory, optional, or repeatable in `OPEN.db`.
4. Apply the Suite timer associated with the active sequence.
5. Preserve all raw responses and terminal conditions.
6. Retry only according to an explicit policy.
7. Close or release scan state after abandonment.
8. Compare with a second selection method where safe.
9. Classify the outcome rather than guessing the missing value.

## Diagnostic decision algorithm

```text
function troubleshoot(request, captured_frames, expected_evidence):
    verify transport connection and authentication
    verify request syntax, diagnostic WHO, selector, and direction

    if request was not definitely transmitted:
        return local_transport_or_logging_failure

    classify every received frame before filtering

    if explicit NACK, abort, or structured error exists:
        return classify_explicit_terminal_evidence()

    membership = query_OPEN_db_sequence_membership(expected_evidence)
    timeout = resolve_active_sequence_timeout(request, membership)

    if expected response was received but parser rejected it:
        return parsing_or_context_resolution_failure

    if other valid Device responses were received:
        if expected response is optional:
            return completed_with_optional_omission
        if response depends on Object/firmware capability:
            resolve Device, Module, Object, and firmware
            return supported_missing, unsupported, or still_ambiguous
        return partial_interview

    if no valid response was received:
        compare selector with a second safe selection method
        verify diagnostic family support
        return one of:
            no Device observed
            invalid selector
            wrong diagnostic family
            transport/gateway failure
            timeout with indeterminate Device state

    never infer zero, disabled, or unconfigured from silence
```

## Symptom-specific checks

### No Device IDs

1. Confirm the correct diagnostic family.
2. Send the release frame before enumeration.
3. Verify that the inventory request was transmitted exactly.
4. Collect for the configured first-response window.
5. Check whether another scanner could be suppressing Devices.
6. Retry under a bounded policy.
7. Release scan state even after failure.

“No IDs” means no Device was observed under those conditions; it does not prove the installation contains no Devices.

### The same Device repeats indefinitely

1. Preserve the raw decimal ID from `DIMENSION 13` and its eight-character hexadecimal display; encode the numeric value in decimal in the suppression frame.
2. Verify the corresponding `WHAT 11` suppression frame.
3. Confirm that hexadecimal formatting did not truncate leading zeroes.
4. Check frame direction and whether the gateway actually transmitted suppression.
5. Bound the enumeration rounds and release scan state on exit.

### Missing `WHAT 4`

1. Determine whether the Device returned useful interview frames first.
2. Apply the further-information timer rather than waiting forever.
3. Check for abort, `NACK`, structured error, or transport closure.
4. Mark the interview partial if the normal terminator never arrived.
5. Do not discard already valid `DIMENSION` responses.

### Missing `DIMENSION 32`

1. Resolve every `DIMENSION 30` Module and Object.
2. Determine whether that Module class is expected to expose an address.
3. Check Object/firmware support and `OPEN.db` optionality.
4. Keep “not reported” separate from “no address.”
5. Remember that configurable commands and actuators do not necessarily expose identical diagnostic Dimensions.

### Unknown `DIMENSION 30.KEYO`

1. Read `STATE`.
2. For `STATE=1`, query `EN_KEY_OBJECT.key_object`.
3. For `STATE=0`, query `EN_VIRGIN_OBJECT.virgin_key_object`.
4. Verify the catalogue revision and firmware context.
5. Preserve the raw Object number if unresolved.

### Unknown `DIMENSION 35.INDEX`

1. Attach the response to its internal `SLOT`.
2. Resolve that Module's configured Object.
3. Union Object-scoped and firmware-scoped `EN_CONF` rows.
4. Match `idx` only within that context.
5. Apply filters and conditions before selecting among duplicates.
6. If no definition survives, report the raw tuple as unknown.

### Wrong product match

1. Recheck `DIMENSION 1` VALUE 1 against `AS_ITEM_SYSTEM.modobj`.
2. Apply brand and collection evidence without forcing absent values.
3. Use `EN_DEVICE.name` for the Physical Device description.
4. Keep all surviving SKUs.
5. Retain VALUE 2 as `N_CONF`, a physical configurator-position count, rather than a classification key.
6. Do not substitute an Object description for the Device description.

### Local-button timeout

1. Confirm that the 300-second first-response window was used.
2. Record whether and when the installer operated the Device.
3. Verify that the Device and workflow support local selection.
4. Separate failure to select a Device from failure during the later interview.
5. Close or abort the waiting workflow explicitly where supported.

## Evidence bundle

Every troubleshooting result should retain:

- request and selector;
- diagnostic family;
- transport/session identifier;
- timestamped raw frames in both directions;
- parser output and rejected frames;
- first-response and further-response timers;
- sequence and timeout database rows used;
- Device, firmware, Module, and Object candidates;
- retry count and policy;
- release/close action;
- final outcome class and confidence.

## SQL example: inspect response membership and timeouts

Bind the expected response label as `:open_label`, or replace that predicate with an exact `open_string` match when the label is unknown:

```sql
SELECT
    o.id_open,
    o.open_label,
    o.open_string,
    seq.id_sequence,
    seq.sequence_label,
    seq.descr AS sequence_description,
    os.open_order,
    os.mandatory_open,
    os.repeated_open,
    os.status4nack,
    os.status4error
FROM EN_OPEN AS o
JOIN AS_OPEN_SEQUENCE AS os
  ON os.id_open = o.id_open
JOIN EN_SEQUENCE AS seq
  ON seq.id_sequence = os.id_sequence
WHERE o.open_label = :open_label
ORDER BY seq.sequence_label, os.open_order;
```

Interpret `mandatory_open` and `repeated_open` only within the returned sequence. The same stored frame can participate in several sequences with different roles.

Retrieve the timeout actions for a selected sequence and frame:

```sql
SELECT
    seq.sequence_label,
    o.open_label,
    o.open_string,
    t.timeout_label,
    t.descr AS timeout_description,
    t.type AS timeout_type,
    t."default" AS timeout_value,
    atos.action,
    atos.status4timeout
FROM AS_TIMEOUT_OPEN_SEQUENCE AS atos
JOIN EN_SEQUENCE AS seq
  ON seq.id_sequence = atos.id_sequence
JOIN EN_OPEN AS o
  ON o.id_open = atos.id_open
JOIN EN_TIMEOUT AS t
  ON t.id_timeout = atos.id_timeout
WHERE seq.sequence_label = :sequence_label
  AND o.open_label = :open_label
ORDER BY t.id_timeout;
```

A missing row proves only that the installed `OPEN.db` revision does not describe that membership or timeout. It does not prove that a Device can never emit the frame.

## Outcome classes

- no Device observed;
- unsupported or wrong diagnostic family;
- invalid selector/address;
- partial interview;
- explicit Device abort;
- timeout with indeterminate Device state;
- transport failure;
- catalogue resolution failure.

Silence alone cannot distinguish these outcomes.

## Expected result

Return a troubleshooting record containing:

- the original symptom and expected evidence;
- the exact reproduced request;
- diagnostic family and selector;
- timestamped raw traffic;
- active sequence, membership, and timeout evidence;
- Device, firmware, Module, Object, and property context where applicable;
- retries and cleanup/release operations;
- eliminated hypotheses and the evidence that eliminated them;
- the selected outcome class;
- remaining ambiguity;
- the safest next read-only action.

A useful conclusion is bounded and falsifiable-for example, “the selected Device completed its interview, but this configured command Object did not report optional `DIMENSION 32` in two fresh sessions.” Avoid conclusions such as “the Device has no address” unless independent evidence establishes that stronger claim.

See [Diagnostic Error Handling](../diagnostics/device-interview.md#errors-and-abnormal-termination) and [Address Discovery](../diagnostics/address-discovery.md).
