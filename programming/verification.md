# Programming Verification

Verification compares the intended configuration with a new runtime projection after the programming session has ended.

## Why read-back is required

`WHAT 52` establishes successful completion of the advanced transfer as represented by `OPEN.db`. It does not prove that every optional parameter was managed, because `DIMENSION 39` warnings can coexist with continued configuration.

Virtual-configurator transfer has no `WHAT 52` member in its canonical sequence. Its Device end marker and echoed values likewise do not replace a later installed-state check.

## Verification procedure

1. Record whether transfer ended with success, warning, error, abort, or timeout.
2. Send the outer session close `*[WHO]*2*0##` when the canonical workflow reaches close.
3. Wait for the configured close interval.
4. Start a new diagnostic interview by Device ID when available.
5. Reconfirm `DIMENSION 1` identity and `DIMENSION 13` Device ID.
6. Resolve every `DIMENSION 30` record by configured Object or Virgin Object.
7. Compare `DIMENSION 32` effective system/address tuples.
8. Compare `DIMENSION 35` indexed values using the resolved definitions.
9. Preserve `DIMENSION 310` separately.
10. Compare `DIMENSION 4` and `5` only as raw configurator reports until their precise semantics are established.
11. Classify each intended change independently.

## Result classes

| Result | Meaning |
| --- | --- |
| Verified | read-back matches the intended effective state |
| Verified with warnings | intended state matches but programming reported nonfatal omissions |
| Contradicted | read-back reports a different effective value or Object |
| Unverifiable | the Device does not report the relevant optional data |
| Indeterminate | identity, timeout, or transport state prevents reliable comparison |

Do not compare only display strings. Retain raw frames, decoded values, Object/firmware context, and conversion rules.

## Object replacement checks

After `ConfKO`, verify the entire Module layout rather than only the edited slot because the sequence resets all Objects before rebuilding them. Confirm that fixed and untouched Modules remain present with their intended Objects and addresses.

## Physical and advanced values

Diagnostic read-back reports effective configuration, not necessarily the method used to create it. A value compatible with a physical configurator cannot prove that jumpers were used. A value outside the established physical range can exclude physical configuration for that property.

See [Device Interview](../diagnostics/device-interview.md), [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 32`](../diagnostics/dim32-addressing.md), and [`DIMENSION 35`](../diagnostics/dim35-configuration.md).
