# Overview

`WHO 13` defines functional Gateway operations. It must be distinguished from the TCP/OpenWebNet transport role of a gateway: authentication, connection establishment, command/event sessions and generic `ACK`/`NACK` handling are protocol-layer concerns, while `WHO 13` frames address gateway functions through the ordinary OpenWebNet message grammar.

## Protocol role

The published `WHO 13` specification describes gateway-specific commands and information exchange. The MyHOME_Suite `OPEN.db` model also represents Gateway as a functional system, confirming that these operations belong to a `WHO` namespace rather than to the framing layer itself.

Consequently, a client should model two separate concepts:

| Layer | Responsibility |
| --- | --- |
| OpenWebNet gateway session | TCP connection, authentication, session selection, `ACK`/`NACK`, timeouts |
| `WHO 13` functional traffic | Gateway-specific `WHAT`, `WHERE`, parameters and information |

## Address and parameter handling

`WHO 13` values are system-specific. Numeric fields must not be reinterpreted using Lighting A/PL, Thermoregulation zones, or another functional namespace merely because the common frame delimiters are identical.

Where a gateway operation returns structured information, the complete parameter tuple should be retained. Generic OpenWebNet parsers should first classify `WHO`, then dispatch the remaining fields to the `WHO 13` grammar.

## Relationship to diagnostic gateway traffic

MyHOME_Suite also uses diagnostic families such as `WHO 1013` for gateway/device diagnostics. Those are separate namespaces. A frame under `WHO 1013` is not an extended form of functional `WHO 13` and is documented under [`../../diagnostics/`](../../diagnostics/).

The canonical public specification is preserved as `WHO_13.pdf` under [`../../sources/openwebnet-public/pdf/`](../../sources/openwebnet-public/pdf/). Common session behavior is documented under [`../../protocol/`](../../protocol/).