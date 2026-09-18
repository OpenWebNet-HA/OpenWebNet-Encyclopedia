# Protocol

OpenWebNet is a delimiter-framed application protocol used to exchange commands, events, state, measurements, configuration data, and service information with compatible gateways and systems.

The protocol has two layers that must not be collapsed:

1. a connection/session layer that selects commands, events, or programmed-scenario traffic and performs authentication where required;
2. an application-frame layer in which `WHO` selects a system and the remaining fields are interpreted in that system's grammar.

## Reference

| Topic | Purpose |
| --- | --- |
| [Frame Syntax](frame-syntax.md) | Common message families, delimiters, empty fields, and parameterized tags |
| [Connection and Sessions](sessions.md) | TCP gateway setup, session selectors, and session state |
| [Authentication](authentication.md) | Open-range behavior, legacy authentication boundary, and HMAC negotiation |
| [Stream Parsing](stream-parsing.md) | Incremental parsing, tokenization, request correlation, and defensive limits |
| [Addressing](addressing.md) | `WHERE` interpretation and the shared SCS A/PL routing model |
| [`WHAT`](what.md) | Command, state, and event selector semantics |
| [`DIMENSION`](dimensions.md) | Property request, report, and write forms |
| [Acknowledgements](acknowledgements.md) | `ACK`/`NACK` roles, including result-sequence termination |

## Core fields

| Concept | Purpose |
| --- | --- |
| `WHO` | Selects the functional, diagnostic, service, or connection-level namespace |
| `WHAT` | Identifies a command, event, or state within a `WHO` |
| `WHERE` | Identifies the destination or source according to that `WHO`'s address grammar |
| `DIMENSION` | Identifies a readable, reportable, or writable property within a `WHO` |
| `ACK` / `NACK` | Reports acceptance/failure or terminates a multi-frame response sequence |

`WHAT`, `WHERE`, and `DIMENSION` are not globally uniform namespaces. Resolve `WHO` and the frame family before interpreting them.

## Common application-frame families

| Purpose | Form |
| --- | --- |
| Command, state, or event | `*WHO*WHAT*WHERE##` |
| Status request | `*#WHO*WHERE##` |
| `DIMENSION` request | `*#WHO*WHERE*DIMENSION##` |
| `DIMENSION` response or report | `*#WHO*WHERE*DIMENSION*VALUE...##` |
| `DIMENSION` write | `*#WHO*WHERE*#DIMENSION*VALUE...##` |
| Positive acknowledgement | `*#*1##` |
| Negative acknowledgement | `*#*0##` |

The notation above describes structure, not a complete grammar. Fields can be empty or parameterized, and valid values depend on the selected system.

## Connection workflow

For the published TCP gateway workflow:

1. connect to port `20000`;
2. receive the server greeting `ACK`;
3. select the commands/actions, events, or programmed-scenario session;
4. complete authentication if the gateway requires it;
5. exchange application frames according to the active session.

Session selectors such as `*99*9##` are connection-control frames. They must not be interpreted as ordinary functional `WHO 99` traffic.

## Interpretation order

A reliable implementation should process a message in this order:

1. recover the complete raw frame from the byte stream;
2. recognize acknowledgement, session-control, or application-frame structure;
3. resolve `WHO`;
4. parse `WHAT`, `WHERE`, and `DIMENSION` using the selected namespace;
5. validate operation-specific ranges;
6. where a physical Device is involved, validate the target Object's capability.

Syntactic validity does not prove that a Device supports an operation. The functional reference defines wire semantics; the [Device Model](../device-model/) and catalogue evidence define Device/Object applicability.

## Reference organization

This directory contains mechanics shared across systems. Functional commands and properties are organized by `WHO` under [`functional/`](../functional/). Diagnostic and programming protocols reuse the frame language but define separate operations, sequences, and evidence boundaries under [`diagnostics/`](../diagnostics/) and [`programming/`](../programming/).

## Evidence basis

The common syntax and TCP session model are grounded in [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). HMAC behavior is grounded in [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf). System-specific semantics come from the corresponding public `WHO` document, MyHOME Suite implementation data, or explicitly identified observed traffic; those evidence classes are not treated as interchangeable.
