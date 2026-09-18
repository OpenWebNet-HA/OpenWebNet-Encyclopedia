# Frame Syntax

An ordinary OpenWebNet frame is an ASCII message that begins with `*`, contains `*`-separated tags, and ends with `##`.

~~~text
*tag1*tag2*...*tagN##
~~~

The introductory specification limits ordinary frame characters to decimal digits, `*`, and `#`. The meaning and permitted structure of each tag depend on the frame family and selected `WHO`.

## Common frame forms

| Frame class | Syntax | Purpose |
| --- | --- | --- |
| Command/status/event | `*WHO*WHAT*WHERE##` | Command, reported state, or asynchronous event |
| Status request | `*#WHO*WHERE##` | Request current state |
| `DIMENSION` request | `*#WHO*WHERE*DIMENSION##` | Request a property value |
| `DIMENSION` response/report | `*#WHO*WHERE*DIMENSION*VALUE...##` | Return or asynchronously report a property value |
| `DIMENSION` write | `*#WHO*WHERE*#DIMENSION*VALUE...##` | Write a supported property |
| `ACK` | `*#*1##` | Positive result or sequence terminator |
| `NACK` | `*#*0##` | Negative result or failed-sequence terminator |

`VALUE...` is notation used by this reference for the ordered value fields defined by that `DIMENSION`; the ellipsis is not transmitted.

Connection selectors and authentication frames use the same outer delimiters but have their own state-dependent grammars. See [Connection and Sessions](sessions.md) and [Authentication](authentication.md).

## Delimiters and empty tags

| Token | Role |
| --- | --- |
| `*` | Starts a frame and separates major tags |
| `##` | Terminates a frame |
| `#` | Participates in a frame variant or parameterized field according to context |

Tags can be empty. For example, `*#13**1##` contains an intentionally empty `WHERE`. A tokenizer must preserve that empty field rather than collapsing adjacent separators.

`#` has no single context-independent meaning. It can introduce a request family, prefix a writable `DIMENSION`, mark a group address, add routing qualifiers, or separate operation-specific parameters.

## Command, status, and event frames

The form `*WHO*WHAT*WHERE##` is direction- and session-dependent:

- in a commands/actions session, the client uses it to request an action;
- the server can use it to answer a status request;
- in an events session, it reports an asynchronous state change or event.

`WHAT` and `WHERE` can each contain `#`-introduced parameters when defined by the selected `WHO`. Parse them only after resolving the system.

## Status requests

A status request has form `*#WHO*WHERE##`. If `WHERE` is omitted where the system permits it, the request can address the complete system.

The server can return one or more normal command/status frames. The response sequence ends with `ACK` on success or `NACK` on failure; it is not safe to assume a single result frame.

## `DIMENSION` operations

A read request identifies `WHO`, `WHERE`, and `DIMENSION`. A response repeats those fields and appends ordered values. The same response form can also appear asynchronously on an events connection when a value changes or is reported periodically.

A write prefixes the `DIMENSION` selector with `#`. A syntactically valid write does not imply that the selected property is writable.

Some systems parameterize the selector itself. For example, diagnostic `32#SLOT` selects `DIMENSION 32` for one internal slot; the following `SYS` and `ADDR` remain ordinary `*`-separated values. The `#` inside the selector does not replace the major-field delimiter.

## Field scope

The semantic identity of a field includes its namespace and structural role:

- an operation is at least `(WHO, WHAT)` plus any `WHAT` parameters and target context;
- an address is `(WHO, WHERE)`;
- a property is at least `(WHO, DIMENSION)` plus selector parameters;
- user-facing meaning can additionally depend on the target Object.

Equal numeric values in different `WHO` namespaces do not imply equal meaning.

## Parsing requirements

Do not parse OpenWebNet with a single delimiter split and immediate integer conversion. Preserve the raw frame, recognize the family, preserve empty tags and leading zeroes, and then apply field-specific grammars.

See [Stream Parsing](stream-parsing.md) for an incremental parser model, [Addressing](addressing.md) for `WHERE`, [`WHAT`](what.md), [`DIMENSION`](dimensions.md), and [Acknowledgements](acknowledgements.md).

## Evidence basis

The common frame forms, alphabet, empty-tag rule, request/response direction, and acknowledgement-terminated sequences come from [`OWN_Intro_ENG.pdf`](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). System-specific extensions are documented only where the relevant `WHO` source, implementation database, or observed workflow establishes them.
