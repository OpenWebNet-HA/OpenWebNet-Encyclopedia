# Programming Error Handling

Programming failures must remain attached to the active session, target Device, transfer sequence, `slot`, Object, property, and attempted value.

## Terminal responses

| Frame | Meaning in `OPEN.db` | Classification |
| --- | --- | --- |
| `*[WHO]*51*[WHERE_FAKE]##` | wrong configuration | fatal error |
| `*[WHO]*52*[WHERE_FAKE]##` | configuration accepted | successful advanced-transfer result |
| `*[WHO]*3*0##` | abort configuration | direction-dependent abort |
| `*[WHO]*4*[WHERE_FAKE]##` | Device end of transmission | entry/virtual-transfer terminal marker |
| `*[WHO]*4*0##` | programmer end of transmission | closes advanced transfer payload |
| `*[WHO]*2*0##` | end programming session | outer session close |

`OPEN.db` also provides `WHERE = 0` variants of `WHAT 51` and `52` outside the canonical sequence rows. Preserve the received form.

## Structured errors

### Object state

`*#[WHO]*[WHERE]*31*[SLOT]*[CODE]*[STATE]##`

| Code | Meaning | `ConfKO` state |
| ---: | --- | --- |
| `0` | Object not implemented/unset | Error |
| `1` | Object busy | Error in `ConfKO`; informational in diagnostic contexts |
| `2` | Object already configured | Error |
| `3` | insufficient free Object capacity | Error |
| `4` | requested Object not implemented | Error |

The same busy frame can be nonfatal information during diagnostics and a transfer error during programming. Sequence context controls handling.

### Address

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

The boolean flag identifies an address error but does not encode its cause.

### Parameter

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

This is classified as error-and-information. `ConfKO` maps it to Warning so unsupported/unmanaged parameters need not invalidate all other writes.

## `ACK` and `NACK`

Ordered programming sequences do not list ordinary `ACK` or `NACK` as members, but `status4nack` defines their state transitions:

- entry-frame `NACK` → Undefined;
- virtual-configurator write `NACK` → Error;
- Object/address/reset `NACK` → Error;
- parameter or programmer end-of-transmission `NACK` → Warning;
- close-session `NACK` → Error.

Handle `NACK` relative to the last outstanding command and active sequence. Do not interpret an uncorrelated `NACK` after pipelining several writes.

## Timeout and transport loss

A timeout is not a negative acknowledgement and does not prove that the Device rejected or rolled back prior writes. Mark the result indeterminate, send programmer abort when safe and supported, close the transport according to application policy, and require diagnostic read-back before retry.

Because `ConfKO` starts by resetting all Objects, interruption during a replacement transfer can leave partial or uncertain state. Do not resume at an arbitrary later frame unless Device-specific behavior establishes that this is safe.

## Recovery policy

1. Stop sending new writes after a fatal error or ambiguous timeout.
2. Preserve every frame and state transition.
3. Send programmer `WHAT 3` abort if the active workflow supports recovery.
4. End or re-establish the connection.
5. Perform a fresh diagnostic interview.
6. Re-resolve the Device and catalogue context.
7. Rebuild the complete desired configuration.
8. Start a new programming session rather than assuming the previous transfer position.

`WHAT 7` is labelled as deleting stored Device configuration but is not part of a canonical programming scenario. Do not use it as a generic recovery operation without Device-specific evidence.
