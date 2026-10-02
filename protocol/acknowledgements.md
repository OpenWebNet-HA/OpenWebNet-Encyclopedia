# Acknowledgements

`ACK` and `NACK` are standalone OpenWebNet frames. They contain no `WHO`, `WHAT`, `WHERE`, or `DIMENSION` field.

| Result | Frame |
| --- | --- |
| `ACK` | `*#*1##` |
| `NACK` | `*#*0##` |

Their meaning depends on the active connection state and operation. They are not globally equivalent to “the Device is now in the requested state.”

The roles below primarily follow the TCP gateway introduction. Product-specific extensions include L4686SDK `*#*x##` error forms and the [ZigBee Interface](zigbee-interface.md) BUSY NACK `*#*6##` followed by NACK. Do not reject or correlate these through a two-value acknowledgement model without the applicable interface context.

## Roles of `ACK`

The canonical introduction uses `ACK` in several roles:

- the server greeting after a TCP connection opens;
- acceptance of a session selector;
- authentication negotiation or authentication success;
- positive processing result for a command or write;
- terminating marker after one or more status or `DIMENSION` response frames.

For a command or write, `ACK` indicates that the gateway considered the message syntactically and semantically acceptable in that interaction. It does not independently prove the final physical state of an actuator. When final state matters, request or observe the relevant state afterward.

## Roles of `NACK`

`NACK` reports that the message or active operation failed semantic or syntactic processing. The frame contains no reason code.

In a multi-frame status or `DIMENSION` response, `NACK` can also terminate the sequence. The introductory specification states that the client may consider frames received earlier in that response sequence invalid. A client should therefore stage multi-frame results until it receives the terminating acknowledgement.

## Correlation

OpenWebNet acknowledgement frames do not carry transaction identifiers. Correlation comes from connection state and request ordering.

On a command session, keep at most one unresolved request unless the specific gateway behavior proves that pipelining is supported. On an event session, do not attach an unrelated asynchronous event to a pending command merely because it arrives nearby in time.

### Ordering across connections

Request ordering on one connection does not order operations on another. Historical BTicino clients explicitly handle this: LAN writes are sent immediately and followed by a delayed status read, while energy graph requests are directed through one connection. These are application strategies against observed ordering problems, not protocol timing constants. See [Platform and ordering evidence](../project/review/myopencommunity-integration.md#platform-properties-and-ordering).

### Historical client correlation and replay

The touchscreen writer associates each ACK/NACK with the oldest pending frame on that connection, then notifies subscribers for the original frame's `WHO`. Two initial acknowledgement positions are reserved for connection and channel setup. Exact tests cover mixed namespaces and multiple subscribers; the ACK itself still carries no namespace or request identifier.

Within one queued send batch, this writer removes byte-identical duplicates. On its proactive inactivity reconnect, it requeues frames whose acknowledgements remain outstanding before newly queued traffic. This is client behavior, not a delivery guarantee: absence of an ACK does not prove that an operation had no effect, and replay is not inherently safe for non-idempotent commands. See [Writer tests and implementation](../project/review/myopencommunity-reassessment.md#transport-and-session-boundaries).

### Simulator fallback acknowledgements

The VDK 2.0 F454 model returns a fallback ACK after a 500 ms timeout for a pending status request, even when no Device result arrived; other unhandled TCP operations receive NACK. Its internal plant-message identifiers are not fields in the wire ACK. This is simulator behavior, not evidence that physical F454 Firmware uses that deadline or acceptance policy. See [Simulator evidence](../project/review/myopencommunity-integration.md#simulator-models).

## Error handling

When a `NACK` is received:

1. classify it using the active state: session selection, authentication, command/write, or result sequence;
2. discard or quarantine incomplete results where required;
3. do not invent an error reason absent another frame or implementation signal;
4. decide whether the session remains usable from the operation-specific workflow;
5. log the raw frame and state transition, redacting authentication data.

Connection closure can itself be the failure signal during authentication or unsupported negotiation.

## Evidence basis

The frame values, acceptance semantics, and end-of-sequence behavior come from [OpenWebNet Introduction specification](https://archive.openwebnet-ha.org/sha256/97/d4/97d43e6493ff0dbc4a4dbecdff894b7ce4e2334873b4edfcbc6ad54fe1ef0be2.pdf), particularly “Particular Open Messages” and the status/`DIMENSION` request sequences. Session-specific authentication behavior is refined by [Hmac specification](https://archive.openwebnet-ha.org/sha256/78/7d/787dfb3a0a00f000666241b2011982636313a98944bb6032b19eaf8d12f98680.pdf).
