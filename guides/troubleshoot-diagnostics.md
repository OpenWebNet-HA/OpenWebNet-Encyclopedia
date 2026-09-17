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
