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

## Error handling

When a `NACK` is received:

1. classify it using the active state: session selection, authentication, command/write, or result sequence;
2. discard or quarantine incomplete results where required;
3. do not invent an error reason absent another frame or implementation signal;
4. decide whether the session remains usable from the operation-specific workflow;
5. log the raw frame and state transition, redacting authentication data.

Connection closure can itself be the failure signal during authentication or unsupported negotiation.

## Evidence basis

The frame values, acceptance semantics, and end-of-sequence behavior come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf), particularly “Particular Open Messages” and the status/`DIMENSION` request sequences. Session-specific authentication behavior is refined by [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf).
