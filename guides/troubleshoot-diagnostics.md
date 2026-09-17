# Troubleshoot Diagnostics

## Goal

Classify incomplete discovery or interview results without converting silence, optionality, or ambiguous identity into false conclusions.

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
| detailed properties | after resolving Modules, send `*#[WHO]*0*38#0##` |

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

See [Diagnostic Error Handling](../diagnostics/device-interview.md#errors-and-abnormal-termination) and [Address Discovery](../diagnostics/address-discovery.md).
