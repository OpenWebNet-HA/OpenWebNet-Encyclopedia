# `WHO 8` - Video Door Entry and Telephony

`WHO 8` identifies the OpenWebNet Video Door Entry and telephony system. The corpus establishes the namespace, MyHOME Suite service metadata, and historical BTicino touchscreen call and messaging behavior. It does not contain a complete public functional specification.

## Established implementation evidence

`OPEN.db` records:

- functional `WHO 8`;
- diagnostic family `WHO 1008`;
- `managed = 1`;
- the F422 public-riser-interface address rule `1[I1][I2][I3][I4]`, with advanced form `1[I1I2I3I4]`;
- one system-associated generic identification template, `*[WHO]*[WHAT]##`, labelled `cmd_ident`.

The template establishes that MyHOME Suite associates a service-identification operation with this system. Because the database does not enumerate the substituted `WHAT` semantics here, it does not justify a `WHAT` table.

## Historical touchscreen call model

The following forms are implementation evidence from `VideoDoorEntryDevice` and its exact tests at `TS10_1_0_23`. They describe the MyHome_Screen call stack, not guaranteed capabilities of every Video Door Entry gateway. `LOCAL`, `CALLER`, and `TARGET` are addresses in that stack; their full valid domains are not established.

| Operation | Implemented form |
| --- | --- |
| Call | `*8*1#KIND#MMTYPE#CALLER*TARGET##` |
| Answer | `*8*2#KIND#MMTYPE*LOCAL##` |
| End call | `*8*3#KIND#MMTYPE*4LOCAL##` |
| Camera autoswitch | `*8*4#LOCAL*TARGET##` |
| Cycle external units | `*8*6#LOCAL*ORIGINAL_CALLER##` |
| Caller-address report, SCS | `*8*9#KIND#MMTYPE*CALLER##` |
| Open / release lock | `*8*19*TARGET##` / `*8*20*TARGET##` |
| Stair light ON / OFF | `*8*21*LOCAL##` / `*8*22*LOCAL##` |
| Call process ready | `*8*37#MODE*LOCAL##` |
| Re-arm session, SCS | `*8*40#KIND#MMTYPE*CALLER##` |
| Camera up / down / left / right | `*8*59#PHASE*CALLER##` through `*8*62#PHASE*CALLER##` |

The end-call writer concatenates literal `4` before the local address; it is not a `#4` routing qualifier. For call-process readiness, `MODE` is `1` SCS or `2` IP. Camera movement uses `PHASE = 1` press/start and `2` release/stop. During a call, lock operations target the current caller; otherwise the implementation uses the local address.

| `KIND` base value | Implemented call kind |
| ---: | --- |
| `1..4` | Entrance panels PE1..PE4 |
| `5` | Camera autoswitch |
| `6` / `7` | Internal / external intercom |
| `13` | Floor call |
| `14` | Pager call |

Tests establish `MMTYPE = 2` for audio and `4` for audio/video. The parser also treats end-call `MMTYPE = 3` as a stop-video notification in SCS mode. Its fallback classification of other values as audio/video does not establish those values' protocol meanings.

The implementation recognizes `KIND > 1000` as an IP call and takes the caller from the third `WHAT` parameter; SCS caller information can arrive separately in `WHAT 9`. Values with `KIND % 1000` in `101..105` mark movable cameras. Preserve the complete value rather than reducing it to the entrance-panel ordinal.

The client keeps the original caller separately from the currently selected camera. A `WHAT 40` re-arm report updates the current address, media type and movable-camera flag, while cycling continues to target the original caller. Lock and movement commands use the current address. The `@` prefix used in decoded autoswitch notifications is a local application marker, not a wire-address prefix.

Exact tests also distinguish call state: a floor call (`KIND 13`) emits a ringtone without replacing an existing call's stored `KIND` or `MMTYPE`. Ordinary answer, end and stop-video frames are ignored while idle; pager and teleloop handling have separate guards. These are touchscreen state choices, not requirements on every decoder. See [Call-state evidence](../../project/review/myopencommunity-intermediate-history-review.md#call-address-and-state).

The pager call/answer writers use broadcast `WHERE = 4` and include the local address after `KIND` and `MMTYPE`, for example `*8*1#14#2#11*4##`. Exact receive tests also accept a pager call addressed to the local endpoint and an answer with a non-broadcast `WHERE`. The client waits for the answer event when initiating a pager conversation; it does not derive SCS caller-address state from that answer alone. Its call-state guards are client behavior, not a universal broadcast-only receive rule. See [pager history](../../project/review/myopencommunity-coverage-audit.md#historical-corrections).

### Teleloop and local multimedia events

| `WHAT` | Implementation meaning / form |
| ---: | --- |
| `63` / `64` | Silence / restore the local multimedia amplifier; received events |
| `76` | Start teleloop: `*8*76*LOCAL##` |
| `77` | Associate teleloop: `*8*77#ID*LOCAL##`; received value identifies the association |
| `78` | Teleloop timeout event: `*8*78*LOCAL##` |
| `79` | Tested session event: `*8*79#KIND#MMTYPE#ID*LOCAL##` |

The `WHAT 79` receive test establishes the field order with `KIND = 1`, `MMTYPE = 4` and `ID = 5`. The decoder emits a boolean session event during a call; it does not validate those parameters against the association. The application treats that event as a teleloop answer to a pending, unanswered call.

The touchscreen application uses an 11-second association timer. It accepts the association result only while that timer is active; received `WHAT 78` and timer expiry end the pending association. Neither establishes a wire-protocol timeout. At `TS10_1_0_23`, a nonzero stored ID registers the association frame for connection initialization; changing the ID replaces that frame, and zero removes it without sending an unlink command. This supersedes an earlier delayed device-init path. See [Teleloop evidence](../../project/review/myopencommunity-intermediate-history-review.md#teleloop-association-and-session).

## Historical Guard Unit messaging

The same touchscreen stack implements Guard Unit messages under `WHO 8`. This is distinct from the [`WHO 12` Messages namespace](../who-12-messages/).

| Stage | Tested or implemented form |
| --- | --- |
| Begin from Guard Unit | `*8*9012#ID*LOCAL#00#GUARD##` |
| Ready / busy reply | `*8*9013*GUARD#00#LOCAL##` / `*8*9014*GUARD#00#LOCAL##` |
| Parameter block | `*#8*LOCAL#00#GUARD*#9001*VALUES##` |
| Message data | `*#8*LOCAL#00#GUARD*#9002*CHAR1*CHAR2*...##` |
| Checksum | `*8*9017#CHECKSUM*LOCAL#00#GUARD##` |
| End | `*8*9001*LOCAL#00#GUARD##` |
| Bad checksum reply | `*8*9015#VALUE*GUARD#00#LOCAL##` |
| Timeout reply | `*8*9016#COUNT*GUARD#00#LOCAL##` |

`9001` therefore has distinct parameter-write and ordinary end-command roles. The tests preserve the `00` address component and the empty positions within parameter blocks; the complete parameter schema remains unknown.

Data values are decimal 16-bit character codes appended as `QChar` values. The message parser expects U+000E, a timestamp `dd/MM/yy hh:mm`, U+000F, then text. Its test parses `08/03/10 17:32` as 8 March 2010 at 17:32. This establishes the historical application format, not an arbitrary UTF-8 text payload.

The checksum helper splits each 16-bit character into high byte then low byte. For unsigned byte sequence `b[0..n-1]` with non-negative modulo reduction, the low checksum byte is `(1 + sum(b)) mod 256`; the high byte is `(n + sum(i*b[n-i], i=1..n-1)) mod 256`. Combining high then low byte reproduces the exact test vector `Bticino` followed by U+F0E2 -> `0xE49B`; this is not a named standard CRC.

The archived helper uses plain `char` and C++ remainder, so this formula is not a byte-exact description for every input/build. For U+FFFF alone, the original helper returns `-1` with signed `char`, versus `511` (`0x01FF`) with unsigned `char`. Physical Guard Unit behavior for such input remains unconfirmed. See [Checksum evidence](../../project/review/myopencommunity-intermediate-history-review.md#message-checksum-and-test-limits).

Verification uses the rightmost five decimal characters of the received checksum argument. On failure, the receiver replies with that numeric value in `9015`, then clears the pending message before a later end frame can publish it. The rejection argument is therefore not necessarily the begin frame's message ID.

At `TS10_1_0_23`, the 5-second inactivity timer restarts after parameter/data blocks and a matching checksum. A timeout reports the accumulated UTF-16 code-unit count, not the checksum byte count. An active receive answers another begin with busy. Older implementation revisions used a 3-second timer and optional `#8` address components; these are historical variants, not permission to normalize arbitrary addresses. See [Messaging evidence](../../project/review/myopencommunity-integration.md#video-door-entry-and-messaging).

## Evidence boundary

The public corpus has no dedicated `WHO 8` specification. `WHO 6`, `WHO 7`, and `WHO 8` share an application domain but remain independent namespaces. Do not reuse `WHO 7` camera commands or addresses under `WHO 8` without direct evidence.

Diagnostic traffic belongs to `WHO 1008`; the numeric relationship does not make functional and diagnostic frames interchangeable.

## Decoder guidance

Decode the historical forms only in the applicable touchscreen context. Preserve other fields losslessly, including unknown call kinds, message parameters, and addresses. Device-specific applicability still requires a resolved implementation, specification, or observed traffic; the historical classes do not establish a universal grammar.

See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md), [`WHO 6`](../who-6-basic-video-door-entry/), and [`WHO 7`](../who-7-multimedia-video/).
