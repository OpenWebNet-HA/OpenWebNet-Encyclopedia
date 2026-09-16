# Overview

`ACK` and `NACK` are standalone OpenWebNet acknowledgement frames used to report positive or negative processing results.

| Result | Frame |
| --- | --- |
| `ACK` | `*#*1##` |
| `NACK` | `*#*0##` |

They do not contain `WHO`, `WHAT`, `WHERE`, or `DIMENSION` fields.

## `ACK`

`*#*1##` reports a positive acknowledgement. Its exact implication depends on the operation and session in which it appears; it should not be interpreted as a global statement about Device state.

## `NACK`

`*#*0##` reports a negative acknowledgement. The reason for rejection or failure is not encoded in the acknowledgement frame itself. Additional protocol frames, session state, or implementation-specific error handling may provide further information.

## Sequence context

Acknowledgements are interpreted in the context of the immediately preceding operation and the active protocol sequence. Implementations should associate an acknowledgement with the operation that is awaiting it rather than treating it as an independently addressable message.

See [`frame-syntax.md`](frame-syntax.md) for the common frame families.