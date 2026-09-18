# Verify Programming

## Goal

Prove what configuration is effective after a programming attempt.

A programming success response is not sufficient evidence. Verification starts a new diagnostic session, rebuilds the Device model from fresh responses, and compares the observed effective state with the intended state property by property.

## Prerequisites

- the applicable diagnostic `WHO`;
- the programmed Device's exact eight-character hexadecimal ID, or another unambiguous selector;
- the immutable intended configuration used to construct the programming payload;
- the programming journal, including every transmitted frame and terminal observation;
- access to `MHCatalogue.db`, `OPEN.db`, and applicable `rules.db3`;
- the ability to start a new session and send and receive frames as MyHOME_Suite does.

If the intended state or target identity was not retained, verification can still report the observed configuration, but cannot prove equality with the requested result.

## 1. Close the programming context

Before verification:

1. stop transmitting programming payload frames;
2. classify the programming terminal condition;
3. send the scenario's close frame if the workflow reached a state where closing is defined and safe;
4. close or discard the transport session;
5. retain the programming journal unchanged.

Do not treat responses still arriving in the programming session as diagnostic read-back.

## 2. Start a fresh Device interview

Establish and authenticate a new command connection if the previous transport was discarded. Prefer selection by the exact Device ID used for programming, converting its eight-character hexadecimal display to the decimal transport value:

`*[WHO]*10#[ID]*0##`

Alternatives are:

| Selection method | Send | First-response window |
| --- | --- | ---: |
| diagnostic address | `*#[WHO]*[WHERE]*0##` | 15 s |
| local interaction | `*[WHO]*5*0##`, then perform the Device-side interaction | 300 s |

Collect the initial response stream during the first-response window and the 20-second further-information window used by MyHOME_Suite. Preserve:

- `DIMENSION 1` identity evidence;
- version `DIMENSION 2`, `3`, and `6` where reported;
- `DIMENSION 13` Device ID;
- every `DIMENSION 30` Module record;
- every `DIMENSION 32` address record;
- applicable `DIMENSION 31` and `34` errors;
- Device `WHAT 4`, timeout, abort, or transport closure.

Reject the verification attempt as a wrong-target observation if the returned Device ID or established identity is incompatible with the programmed Device.

## 3. Request detailed properties

After resolving the fresh Module/Object layout, send:

`*#[WHO]*0*38#0##`

Collect during the MyHOME_Suite eight-second response window:

- repeated `DIMENSION 35` indexed properties;
- applicable `DIMENSION 39` property errors;
- any `DIMENSION 310` Object-specific value.

Keep `DIMENSION 310` separate from the generic `INDEX` model. Close the diagnostic context with `*[WHO]*6*0##` after collection, using a finally-equivalent cleanup path.

## 4. Resolve the observed state

Build a new configuration model from the verification frames:

1. resolve Device and firmware identity;
2. key Modules by protocol internal `SLOT`;
3. resolve configured Objects from `DIMENSION 30.STATE=1`;
4. resolve Virgin Objects from `STATE=0`;
5. attach addresses by internal slot;
6. resolve each `DIMENSION 35.INDEX` in the Module's Object/firmware context;
7. decode values through ranges, filters, conditions, and applicable rules;
8. retain raw and decoded values;
9. attach errors without overwriting a valid reported value;
10. record interview and field-level completion statuses.

Never reuse a property interpretation solely because it was used to create the payload. Resolve the observed value independently so verification can expose an incorrect payload assumption.

### SQL example: independently resolve a read-back property

```sql
WITH applicable_conf AS (
    SELECT c.*, 'object' AS source_scope
    FROM EN_CONF AS c
    WHERE c.id_key_object = :observed_id_key_object
      AND c.id_firmware = 0

    UNION ALL

    SELECT c.*, 'firmware' AS source_scope
    FROM EN_CONF AS c
    WHERE c.id_key_object = 0
      AND c.id_firmware = :observed_id_firmware
)
SELECT
    c.source_scope,
    c.id_conf,
    c.conf_name,
    c.descr,
    c.idx,
    c.read_only,
    r.value,
    r.name AS range_name,
    r."default" AS default_value,
    r.min_value,
    r.max_value,
    r.step
FROM applicable_conf AS c
LEFT JOIN EN_CONF_RANGE AS r
  ON r.id_conf = c.id_conf
WHERE c.idx = :observed_index
ORDER BY c.source_scope, c.id_conf, r.progressive;
```

If this returns several compatible definitions, the read-back property remains ambiguous until filters and conditions select one.

## 5. Normalize intended and observed states

Compare semantic models, not response order.

Use canonical keys:

| Entity | Comparison key |
| --- | --- |
| Physical Device | exact Device ID |
| Module | internal `SLOT` |
| Object assignment | internal `SLOT` plus external `key_object` and configured state |
| address | internal `SLOT` plus decoded system/address semantics and raw `SYS/ADDR` |
| indexed property | internal `SLOT` plus resolved `id_conf`; retain raw `INDEX` |
| special property | internal `SLOT` plus established `DIMENSION 310` semantics |

Normalize only where the equivalence rule is established. Preserve padding, width, ordering, and raw encodings when they can be semantically significant.

Classify every intended field as:

- exact semantic and encoded match;
- semantic match with an established equivalent encoding;
- mismatch;
- not reported;
- observed but not intended;
- ambiguous;
- unresolved;
- error.

## 6. Compare the complete state

The comparison must detect more than changed values:

1. missing or additional Modules;
2. configured/unconfigured state changes;
3. wrong Object assignments;
4. missing, changed, or additional addresses;
5. missing, changed, or additional properties;
6. linked-property changes caused by Device-side normalization;
7. fixed or hidden values unexpectedly altered;
8. values accepted on the wire but outside the resolved effective domain;
9. identity or firmware changes;
10. partial read-back that prevents proof.

Do not automatically fail on an observed property absent from the intended payload if it is a known fixed, derived, or Device-generated value. Classify and explain it.

## Reference algorithm

```text
function verify_programming(programming_record, intended_state):
    close_or_abandon_programming_context_safely()
    observed_frames = acquire_fresh_interview(programming_record.device_selector)

    if observed Device ID differs:
        return wrong_target with raw evidence

    observed_layout = resolve_modules_objects_and_addresses(observed_frames)
    detailed_frames = acquire_DIMENSION_35_with_DIMENSION_38()
    observed_state = resolve_properties_independently(
        observed_layout, detailed_frames
    )

    expected = canonicalize(intended_state)
    actual = canonicalize(observed_state)
    comparisons = []

    for key in union(expected.keys, actual.keys):
        if key only in expected:
            comparisons.append(not_reported_or_missing(key))
        else if key only in actual:
            comparisons.append(observed_additional(key))
        else:
            comparisons.append(compare_with_established_equivalence(
                expected[key], actual[key]
            ))

    if any required field has a proven mismatch or explicit error:
        outcome = "failed"
    else if any required field is unresolved, ambiguous, or not reported:
        outcome = "indeterminate"
    else:
        outcome = "verified"
    retain acquisition completion separately, even if all required fields matched

    return outcome, comparisons, raw frames, resolver provenance
```

## Result classes

| Result | Meaning |
| --- | --- |
| verified | every required intended field was independently read back and matched |
| verified with explained normalization | differences are covered by established equivalence or Device-derived rules |
| failed | at least one required field is a proven mismatch or explicit error |
| partial | some useful state was recovered, but the complete intended state was not observed |
| indeterminate | timeout, transport loss, ambiguity, or missing evidence prevents a conclusion |
| wrong target | the fresh session selected a different Physical Device |
| programming rejected | programming evidence proves rejection and read-back confirms the prior/effective state |
| effective state unknown | destructive work may have begun, but no reliable fresh snapshot was obtained |

A partial or indeterminate result is not success.

## Retry and recovery

- Retry verification only under an explicit bounded policy.
- Start each retry in a new diagnostic session.
- Do not reprogram merely because one optional response was absent.
- If a mismatch is stable across fresh reads, diagnose the property, payload, and Device rules before another write.
- If the Device state is indeterminate after reset-all or interruption, recover by reading the complete state and constructing a new fully validated replacement payload.
- Never resume the original payload at the frame after the last locally recorded transmission.

## Expected result

Return:

- target Device ID and resolved identity;
- programming terminal classification;
- verification interview completion status;
- a complete intended-versus-observed comparison;
- raw frames and database provenance for each resolved field;
- unexplained additional state;
- errors and warnings;
- one explicit result class;
- a recommended next action that does not silently write again.

See [Read and Present a Device Configuration](read-device-configuration.md), [Program a Device](program-device.md), [Programming Session Lifecycle](../programming/session-lifecycle.md), and [Programming Error Handling](../programming/error-handling.md).
