# Connection and Sessions

OpenWebNet application frames are exchanged inside a connection to an OpenWebNet server. The public introduction specifies TCP port `20000` for an IP gateway and separates connection establishment into three phases:

1. establish the transport connection;
2. identify the requested session and, when required, authenticate;
3. exchange frames according to the selected session.

The framing language is transport-independent in principle, but the session selectors and sequences on this page describe the published TCP/IP gateway workflow.

## Initial server acknowledgement

After accepting a TCP connection, the server sends `*#*1##`. The client must receive this initial `ACK` before selecting a session.

| Session | Selector | Direction after setup | Purpose |
| --- | --- | --- | --- |
| Commands/actions | `*99*9##` | Primarily client to server, with replies | Send commands; request status or `DIMENSION` values; write supported `DIMENSION` values |
| Events | `*99*1##` | Server to client | Receive asynchronous bus events and property reports |
| Programmed scenario | `*99*0##` | Server to client in the published example | Forward traffic while programming an F420/03551 scenario module in configuration mode |

After the selector, the server can accept an open-range connection with `*#*1##`, send a legacy challenge, or declare HMAC with `*98*1##` or `*98*2##`. Do not require a separate selector `ACK` before accepting an authentication frame: the HMAC specification shows the declaration immediately after the client selector. Normal traffic begins only after the selected setup path completes.

These selectors belong to connection setup. They are not functional `WHO 99` commands and must not be fed to the ordinary functional-frame dispatcher.

## Commands/actions session

The commands/actions session is request-oriented. A client can send command frames, status requests, `DIMENSION` requests, and supported `DIMENSION` writes.

A command or write normally receives `ACK` or `NACK`. A status or `DIMENSION` request can produce one or more result frames followed by a terminating acknowledgement. See [Acknowledgements](acknowledgements.md).

Do not assume one response frame per request. The selected `WHERE`, gateway, and functional system can cause a request to expand into multiple reports.

## Events session

After `*99*1##` is accepted, the server forwards asynchronous OpenWebNet traffic. The published example includes ordinary command/status frames from more than one `WHO`; the connection is therefore a bus-event stream, not a subscription to one functional namespace.

An event connection is generally long-lived. A client should parse the byte stream incrementally, preserve arrival order, tolerate multiple complete frames in one transport read, retain `WHO`-specific parsing for each emitted frame, and reconnect and repeat session selection after transport failure.

The public introduction does not define per-`WHO` subscription filters or delivery guarantees. Implementations must not infer them.

## Programmed scenario session

The selector `*99*0##` is documented for programming an F420 (BTicino) or 03551 (Legrand) scenario module through Ethernet while that module is in configuration mode.

This is a specialized gateway session. It is distinct from functional scenario activation through `WHO 0`, scenario management through `WHO 17`, the MyHOME Suite scenario engine, and diagnostic or Device-programming workflows.

The public source gives the session boundary and selector but not a general-purpose programming API. The functional F420 frames are documented under [`WHO 0`](../functional/who-0-scenarios/).

## Historical local touchscreen channels

The BTicino touchscreen client at `TS10_1_0_23` uses four channels to its local OpenWebNet server:

| Client role | Selector |
| --- | --- |
| Monitor | `*99*1##` |
| Supervisor | `*99*10##` |
| Command writer | `*99*9##` |
| Request writer | `*99*0##` |

The request writer sends status and dimension requests; the supervisor uses the reader interface. This local use of selector `0` differs from the published scenario-programming role above and does not establish a general external-gateway request session. Likewise, the local supervisor selector is implementation evidence rather than an addition to the published gateway session table.

This client's connected flag and connection-up notification are set on TCP connection establishment, before sending the channel selector. They do not establish receipt of the server greeting, selector acceptance, or authentication success. Applications using this local lifecycle must not equate its connected state with the active-session state of the published gateway workflow. See [Local setup evidence](../project/review/myopencommunity-transport-history-review.md#local-client-setup-and-dispatch).

The VDK 2.0 simulator recognizes the same four selectors, but names `0` command and `9` request. Its labels do not change the published commands/actions selector. Neither implementation establishes external-gateway authentication behavior. See [Local channel evidence](../project/review/myopencommunity-reassessment.md#transport-and-session-boundaries).

## Authentication branch

A gateway can allow configured client IP addresses to connect without an OPEN password. Otherwise, session selection is followed by either the legacy OPEN challenge-response algorithm or the declared HMAC workflow.

Authentication establishes client access; it does not encrypt later OpenWebNet traffic. See [Authentication](authentication.md).

## State-machine requirements

A robust client should explicitly model these states:

| State | Accepted input |
| --- | --- |
| Awaiting server greeting | Initial `ACK` |
| Awaiting session result | Open-range `ACK`, legacy challenge, HMAC declaration, `NACK`, or connection close |
| Authenticating | Frames belonging to the negotiated authentication method |
| Active command session | Requests plus their result sequences |
| Active event session | Asynchronous OpenWebNet frames |
| Closed/failed | Reconnect from the transport layer |

Do not treat every `ACK` as equivalent. Its role is determined by the current state: greeting, selector acceptance, authentication result, operation result, or end-of-sequence marker.

## Evidence basis

The session selectors, TCP port, and basic sequences come from [OpenWebNet Introduction specification](https://archive.openwebnet-ha.org/sha256/97/d4/97d43e6493ff0dbc4a4dbecdff894b7ce4e2334873b4edfcbc6ad54fe1ef0be2.pdf), pages 6–10. HMAC negotiation is specified separately in [Hmac specification](https://archive.openwebnet-ha.org/sha256/78/7d/787dfb3a0a00f000666241b2011982636313a98944bb6032b19eaf8d12f98680.pdf). Observed gateway behavior can refine compatibility handling, but should not silently replace these published sequences.
