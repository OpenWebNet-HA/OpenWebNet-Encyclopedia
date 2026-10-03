# Stream Parsing

OpenWebNet frames are application messages carried over a transport stream. A transport read is not a frame boundary: one read can contain part of a frame, exactly one frame, or several consecutive frames.

A parser should consume bytes incrementally and emit a frame only after the terminating `##` has been received.

## Character set

The introductory specification defines ordinary OpenWebNet frames using decimal digits `0..9`, `*`, and `#`. A frame begins with `*` and ends with `##`. Major tags are separated by `*`. A tag can contain decimal digits and `#`, and empty tags are permitted.

Do not apply this ordinary-frame alphabet blindly to other transport layers or vendor extensions. Validate at the layer whose grammar is being parsed.

## Incremental algorithm

1. Find `*` as the start of a candidate frame.
2. Append subsequent bytes to a bounded buffer.
3. When the buffer ends in `##`, emit the complete raw frame.
4. Continue with bytes remaining in the same transport read.
5. On length, character, or timeout failure, diagnose the malformed candidate and resynchronize at the next plausible `*`.

Preserve the exact raw frame. Numeric conversion belongs to later semantic decoding.

## Parsing layers

| Layer | Responsibility |
| --- | --- |
| Stream framing | Find the leading `*` and terminating `##` |
| Tag tokenization | Split major fields on `*` while preserving empty fields |
| Frame-family recognition | Distinguish acknowledgement, session, command/status, request, response, and write forms |
| Field grammar | Parse parameterized `WHAT`, `WHERE`, or `DIMENSION` selectors |
| System semantics | Interpret values only after resolving `WHO` |
| Capability validation | Check whether the target Device/Object supports the operation |

This order prevents errors such as converting a `WHERE` to an integer before preserving leading zeroes or splitting every `#` as though it had one global role.

## Empty tags

The canonical syntax permits omitted tags. Empty fields are significant in frames such as gateway-management requests where `WHERE` is intentionally empty.

For example, tokenizing `*#13**1##` must retain the empty field between the two `*` delimiters. Removing empty strings shifts `DIMENSION 1` into the wrong position.

## Parameter separators

`#` is interpreted inside the grammar of its enclosing field. It can appear in a parameterized `WHAT`, a qualified `WHERE`, a write selector such as `#DIMENSION`, or a parameterized diagnostic selector such as `32#SLOT`. It is not a universal separator at the frame-tokenization layer.

## Request correlation

A command connection can receive a single acknowledgement, one or more result frames followed by `ACK`, or provisional frames followed by `NACK`.

Because the public protocol defines no transaction identifier, avoid overlapping requests on one command session unless the gateway and operation explicitly support it. On a result sequence terminated by `NACK`, the introductory specification permits the client to regard earlier frames in that sequence as invalid.

## Limits and recovery

The public introduction does not specify a universal maximum frame length, request timeout, or result count. Use configurable defensive limits rather than invented protocol constants:

- bound the receive buffer and incomplete-frame lifetime;
- never execute a partial frame;
- retain malformed raw input only for opt-in diagnostics;
- redact authentication material;
- close or resynchronize according to the connection's trust boundary.

## Encoding model

Keep protocol values as strings until their field grammar has been identified. This preserves leading zeroes, fixed-width Device IDs, empty fields, routing qualifiers, and encoded values that merely look decimal.

Only the system-specific decoder should expose typed integers, temperatures, durations, masks, or identifiers.

## Historical implementation limits

The BTicino touchscreen frame helpers independently construct command, status request, dimension request, and dimension write families using the forms in [Frame Syntax](frame-syntax.md). Their parameter names do not redefine the wire fields: a helper can accept a complete dimension selector and value string in a variable named `what`.

At `TS10_1_0_23`, frame-family recognition delegates to a separate OpenWebNet stack absent from the four preserved repositories. The constructors establish serialization behavior, but do not establish that stack's complete acceptance grammar. The local byte framer drains consecutive `##`-terminated chunks and retains an incomplete tail, without finding a leading `*` or enforcing a buffer limit. Its disconnect/reconnect methods also retain that tail. These implementation limits do not replace the incremental guidance above. See [Numeric framing evidence](../project/review/myopencommunity-transport-history-review.md#numeric-framing-and-classification).

The touchscreen reader also explicitly ignores status-request frames received on the monitor channel, following a historical multi-touchscreen failure. That filtering is client policy; a bus-event parser should still recognize the request family rather than assume that all incoming traffic is a state report.

The VDK 2.0 parser instead splits fields while dropping empty components and calls hash-prefixed functional traffic “diagnostics”. Neither behavior defines protocol grammar. In particular, it is unsuitable as evidence that empty `WHERE` or partial-write values can be discarded, or that every `*#WHO` frame belongs to a diagnostic namespace. See [Frame and parser evidence](../project/review/myopencommunity-integration.md#frame-families-and-parsing).

That simulator parser also rejects ordinary `WHO 0` commands. Its active TCP read handler shares an incomplete-frame buffer across clients and returns after emitting the first functional frame, losing further frames already consumed in the same read. These are simulator limitations, not restrictions on [Scenarios](../functional/who-0-scenarios/) or OpenWebNet stream behavior. See [Simulator transport evidence](../project/review/myopencommunity-transport-history-review.md#simulator-parser-and-active-read-path).

### Separate multimedia XML transport

The touchscreen common library also implements a UTF-8 TCP transport framed by `<OWNxml ...>` and `</OWNxml>`, with namespace `http://www.bticino.it/xopen/v1`. Tests establish extraction of consecutive XML messages and messages surrounded by unrelated text. Its envelope contains `Hdr/MsgID` (`SID`, `PID`), `Dst/IP`, `Src/IP`, and a `Cmd` element.

The final library preserves whitespace inside an extracted message, but converts each transport read from UTF-8 separately. A multibyte character split across reads can therefore be corrupted even when XML envelope buffering succeeds. Envelope extraction does not establish complete incremental UTF-8 decoding. See [XML buffering evidence](../project/review/myopencommunity-transport-history-review.md#xml-buffering-and-assertion-limits).

These are XML transport fields, not transaction identifiers in ordinary `*...##` frames. Media-server browsing and track-selection operations use this separate interface; the source does not establish their numeric mapping to [`WHO 26`](../functional/who-26-upnp-multimedia/). XML acknowledgements and session identifiers must therefore remain distinct from [OpenWebNet acknowledgements](acknowledgements.md). See [Multimedia transport evidence](../project/review/myopencommunity-reassessment.md#multimedia-xml-boundary).

## Evidence basis

The character set, delimiters, empty-tag rule, and common frame families come from [OpenWebNet Introduction specification](https://archive.openwebnet-ha.org/sha256/97/d4/97d43e6493ff0dbc4a4dbecdff894b7ce4e2334873b4edfcbc6ad54fe1ef0be2.pdf). The incremental transport guidance is an implementation consequence of delimiter-framed messages over TCP; it is identified as parser guidance rather than a quoted protocol guarantee.
