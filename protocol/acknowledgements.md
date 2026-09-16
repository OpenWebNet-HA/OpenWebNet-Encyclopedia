# Overview

OpenWebNet defines standalone positive and negative acknowledgement frames.

| Result | Frame |
| --- | --- |
| ACK | `*#*1##` |
| NACK | `*#*0##` |

These frames do not contain `WHO`, `WHAT`, or `WHERE` fields.

## ACK

`*#*1##` indicates positive acknowledgement of the operation for which an acknowledgement is expected.

## NACK

`*#*0##` indicates negative acknowledgement. The meaning of the failure and the subsequent protocol action depend on the operation or sequence in progress.

## Sequence context

Acknowledgements must be interpreted in session context. They are not self-describing responses and do not identify the operation to which they apply.

MyHOME Suite additionally represents operation-specific error handling, status transitions, and timeouts in `OPEN.db`. Those sequence semantics belong with the corresponding diagnostic, programming, or service workflow rather than in this common acknowledgement reference.

See [`frame-syntax.md`](frame-syntax.md) for the other common frame classes.