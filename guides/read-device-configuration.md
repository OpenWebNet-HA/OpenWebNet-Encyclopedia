# Read Device Configuration

## Goal

Build a complete installed-state projection containing identity, Modules, Objects, addresses, and detailed parameters.

## Procedure

1. Select the Device by ID, address, or local interaction.
2. Collect the initial interview through `WHAT 4` or a recorded abnormal termination.
3. Build the Module list from `DIMENSION 30`.
4. Attach `DIMENSION 32` tuples by internal slot.
5. Request detailed information with `*#[WHO]*0*38#0##` only after the Module layout is known.
6. Collect repeated `DIMENSION 35` records during the Suite eight-second window.
7. Preserve `DIMENSION 310` separately because it has no generic `INDEX`.
8. Resolve each `INDEX` only in the Device/firmware/slot/Object context.
9. Preserve raw values when no unique catalogue definition exists.

## Output shape

For each Module record:

| Field | Evidence |
| --- | --- |
| internal slot | `DIMENSION 30.SLOT` |
| Object/Virgin Object | `DIMENSION 30.KEYO` plus `STATE` |
| system/address | `DIMENSION 32` |
| indexed properties | repeated `DIMENSION 35` |
| special value | optional `DIMENSION 310` |
| errors | `DIMENSION 31`, `34`, and `39` |

The `DIMENSION 38` source label includes reset terminology. Use it on unfamiliar Devices only with suitable safety evidence.

## Completion

Distinguish explicit `WHAT 4` completion, timeout, abort, and transport closure. Optional missing records must remain “not reported,” not “unsupported” or “zero.”

See [Device Interview](../diagnostics/device-interview.md) and [`DIMENSION 35`](../diagnostics/dim35-configuration.md).
