# MyOpenCommunity Transport History Review

This continuation starts at `7a75fc0409574911b28afa11cf0094e41d539ab8` on `docs/myopencommunity-integration`. It follows the [intermediate history review](myopencommunity-intermediate-history-review.md) through transport, frame-helper, address-matcher and XML corrections. Earlier chat findings supplied context, not the search boundary. Preserved sources and Git histories remain unchanged.

## Bounded history coverage

The [history dispositions](myopencommunity-transport-history-dispositions.tsv) bind 3,586 changed-file edges to commit/parent identities, exact before/after Git blobs, content SHA-256 values and scoped component identities. The [component dispositions](myopencommunity-transport-component-dispositions.tsv) record 564 distinct normalized method/declaration variants and their semantic comparison points. The 186 assertion occurrences, including executable assertion guards, have macro/ordinal identities and normalized expression digests within their component; the disposition applies to each recorded assertion. Component source revisions are checked against their actual Git tree, including before-change endpoints. Every variant was read, including obsolete implementations and assertions; repeated endpoint identities reuse that review.

| Repository | Changed-file edges | Parent comparisons | Commits | Distinct nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: |
| libqtdevices | 3,166 | 982 | 932 | 909 |
| libqtcommon | 365 | 161 | 160 | 57 |
| BtExperience | 33 | 24 | 24 | 12 |
| MyHomeSystemEmulator | 22 | 4 | 4 | 22 |

The 1,000 repository/blob identities are not independent sources: the libraries retain shared pre-extraction history. All retained refs were traversed with full history and every relevant parent compared, including merges. An independent reconstruction matches the complete parent/path boundary; 7,172 endpoint tree checks bind the recorded blobs to those revisions. Removed files and earlier locations are included.

| Disposition | File edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify evidence | 211 | 28 |
| Corroborates existing scoped documentation | 533 | 84 |
| Excluded with scoped reason | 2,842 | 452 |

A file-edge disposition concerns changed scoped components, not every line of the file. Edges with unchanged scoped executable code, or no selected component, are excluded from this tranche. A non-final variant remains excluded as a current rule unless its exact implementation/assertion is reused by a pinned endpoint; its comparison and historical correction are still recorded. Incorporation does not imply a newly discovered rule at every listed commit.

The boundary follows all retained locations of `openclient`, `frame_functions`, `frame_classes`, writer/address/XML tests, `xmlclient`, and emulator `openmsg`, `tcpserver` and F422 sources/headers. In `device` files, only the connection manager, reconnect constant and earlier address helpers/declarations were reviewed; in `pulldevice` and earlier `generic_functions`/`genericfunz` files, only address helpers/declarations were reviewed. BtExperience coverage here is its earlier generic address-helper locations, not its complete application/network history. Empty or absent helper declarations contribute no component. Unselected device, generic-helper and application methods remain outside this pass.

Normalization removes comments and blank indentation, and redacts private fixture endpoints before comparison. The recorded content hash always identifies the original complete Git blob. The component digest identifies the normalized reviewed body, not a substitute archive. Final original comments were read where needed for scope; this is not a claim to have read all historical comment-only changes. Methods and remaining declarations were compared against the nearest already-read variant, then checked against pinned source and exact assertions. Identity reuse neither executes each revision/dependency combination nor corroborates it independently.

## Pinned source basis

| Repository | Preserved revision | Main transport sources |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Local client](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/openclient.cpp), [frame helpers](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp), [address matcher](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/pulldevice.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | [Writer assertions](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_clientwriter.cpp), [XML client](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/xmlclient.cpp), [XML assertions](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_xmlclient.cpp) |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | Earlier generic helpers are bound by the dispositions; the [project consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/BtObjects.pro) selects external common-stack dependencies |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` (VDK 2.0) | [Parser](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/libplant/openmsg.cpp), [active TCP handler](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_own_GTW_PGIN/tcpserver.cpp), [F422 model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F422_DEV_PGIN/btf422_dev.cpp) |

Repository names and source paths in these review records are provenance. Canonical reader pages retain implementation scope and link here, without an archaeology narrative.

## Local client setup and dispatch

`Client::socketConnected` sets `is_connected`, emits `connectionUp`, then calls `sendChannelId`. It does not await the greeting, authenticate or confirm selector acceptance. `ClientWriter::socketConnected` reserves a setup placeholder, invokes the base callback, starts its inactivity clock and sends pending traffic. The second placeholder is appended by `sendChannelId`. These are local lifecycle/FIFO assumptions, not the published gateway state machine. [Connection and Sessions](../../protocol/sessions.md) now makes that distinction explicit.

`TestClientWriter::newConnection` flushes and consumes selector output, then directly clears `ack_source_list`. It does not receive the two setup ACKs whose positions it removes. Operation tests establish FIFO ACK/NACK attribution, mixed namespaces, subscriber fan-out, delayed sending, byte-identical batch deduplication and proactive reconnect replay, but not handshake correctness. [Acknowledgements](../../protocol/acknowledgements.md) now also states that the writer accepts only ACK/NACK input; it does not collect result frames on the writer connection. The reader separately dispatches by `WHO` and filters monitor status requests.

The [replay correction and test](https://github.com/OpenWebNet-HA/libqtdevices/commit/4fefbcbf03044086f1ca7d3592fe4a62483568d3) distinguish outstanding frames from new traffic; the [partial-channel reconnect correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/b6f36b6e6e6be46670cc24eeff5787a13af380c5) retries until the required local channels are connected. The [unexpected-ACK guard](https://github.com/OpenWebNet-HA/libqtdevices/commit/ae54c71ae8905113d9d64da326b08d172bd1dae1) follows `Q_ASSERT_X`, so it is not proof of debug-build malformed-input safety. Earlier monolithic open/send/close, regex dispatch, compressor, keepalive and watchdog variants do not add protocol vocabulary or delivery guarantees.

## Numeric framing and classification

The four QString constructors preserve the supplied WHO, address, selector and values, including leading zeroes, local/group qualifiers, empty WHERE and partial-write empty values. They corroborate [Frame Syntax](../../protocol/frame-syntax.md). The companion `is...Frame` helpers call `OpenMsg::IsNormalFrame`, `IsStateFrame`, `IsMeasureFrame` or `IsWriteFrame`. That touchscreen class comes from the external common OpenWebNet stack, absent from the four preserved repositories. The emulator's similarly named class is a different implementation and cannot fill this evidence gap.

The pinned local byte framer appends `readAll`, takes bytes through the first `##`, and retains the remainder; its caller drains further complete chunks. It does not search for a leading `*`, bound the incomplete buffer or clear it in the connection/disconnection callbacks. The controlled helper execution retains leading garbage/CRLF and joins newly supplied input to a partial buffer retained through disconnect. This establishes code behavior at the I/O seam, not a captured reconnect failure. [Stream Parsing](../../protocol/stream-parsing.md) keeps defensive parser guidance separate from these historical limits.

## Address matcher lineage

The original [29 address comparisons](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_checkaddress.cpp) were compiled with the unchanged three helper bodies. Five independent comparisons establish the previously underqualified edge: `12#3` versus `12`, and the reverse, both return `NOT_MINE`; equal `12#3` returns `P2P`; `0#3` versus configured `12#3` returns `NOT_MINE`; equal `#45` returns `P2P` through raw equality. These are matcher outcomes, not assertions of valid wire ranges or physical group membership.

The final helper compares complete strings first, then normalizes incoming `#3` only for collective matching. It does not normalize the configured qualifier. [Addressing](../../protocol/addressing.md) now qualifies its earlier blanket wording accordingly. Earlier generic/device helper locations reveal the removal of pull-mode filtering and a formerly broader unqualified-environment rule. For example, an older assertion allowed environment `100` to match `1015#4#12`; the pinned assertion rejects it. The older `splitWhere` use of `left(-1)` for an unqualified string has the same Qt result as returning the whole string, so its rewrite adds no new address semantics.

Neighboring-page review found that [Lighting Addressing](../../functional/who-1-lighting/addressing.md) still presented every `#3` form as published grammar, contradicting the shared reference. The [Lighting specification](https://archive.openwebnet-ha.org/sha256/8a/da/8adafaaeac5e07a5eee247792f70b659e4ea9d99b45fffbd415f94a49976fb4a.pdf), printed page 7, was fetched with its exact SHA-256 verified and the complete WHERE table checked. It enumerates unqualified private-riser and Level-4 forms, not `#3` forms. The Lighting row now identifies Level 3 as an implementation model with operation-specific applicability; only Level 4 is attributed to the published table. This correction does not assert that unlisted forms are invalid.

F422's historical correction adds a short-field-list guard. It does not resolve the already documented general-target bypass, dropped empty group components or narrower simulator interface range. No new physical F422 claim follows from that crash fix.

## Simulator parser and active read path

The unchanged VDK parser removes `##`, drops empty `*` components and recognizes a command only when the first tag converts to a nonzero integer. Ordinary `WHO 0` commands are rejected; empty WHERE in `*#13**1##` shifts `1` into WHERE. Partial-write empty values likewise lose their positions. ACK is accepted by this parser under its broad “diagnostics” label, and delimiter-free input such as `1*1*12` can be accepted. Serializer output is appended to the supplied string; the diagnostic serializer rejects both missing WHO/WHERE, rather than rejecting either missing field. These are defects/implementation choices, not alternative protocol syntax.

Accepted sockets connect `readyRead` to `startRead`, not to the alternate `cmdRead`. The active handler reads a chunk, emits its first functional frame, then returns while further bytes in that chunk have already been consumed. Its `m_msg` member also holds incomplete input shared across clients. Controlled executions independently confirm lost consecutive-frame tails, split terminator completion and cross-client fragment combination attributed to the latter socket. The 1,024-byte local read array and unbounded requested read size are an additional source-level concern; no oversized input or crash experiment was run. Reader prose records the relevant stream/parser limitations, not every defect.

## XML buffering and assertion limits

The [UTF-8 correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/552c51add7ef95c31261a3481eaaf927a1997434) explicitly converts each received chunk. The [whitespace correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/1a216b18d8270a9e1c91d5786860fe2a6c73f11e) replaces `simplified` with `trimmed`, preserving spaces and newlines inside the envelope. The final independent conversion of each read still replaces a split multibyte character with replacement characters. A complete UTF-8 `é` is preserved, while its two bytes delivered in separate reads produce two U+FFFD characters in the controlled Qt5 execution.

The final double/garbage tests assert two received events, but remove the first event before looping over the remaining spy count. They check only the first event's argument, not both payloads or their order. The independent execution checks both outputs directly. The parser retains the closing tag in its buffer; that does not prevent the tested subsequent extraction and establishes no new XML protocol requirement. [Stream Parsing](../../protocol/stream-parsing.md) qualifies extraction versus incremental character decoding. XML session/acknowledgement fields remain separate from ordinary OpenWebNet and `WHO 26`.

## Deliberate exclusions and unresolved questions

| Finding | Disposition or evidence limit |
| --- | --- |
| Local connected flag implies accepted/authenticated session | Contradicted by callback order; corrected reader scope |
| Two setup placeholders prove a successful handshake | Fixture clears them directly; no setup exchange assertion |
| Writer tests prove full multi-frame command-result correlation | Writer ignores non-ACK input; operation FIFO tests have narrower scope |
| Touchscreen classifier accepts/rejects all malformed forms | External stack implementation unavailable; constructors do not establish decoder grammar |
| Emulator parser/serializer shortcuts define valid syntax | `WHO 0` rejection, empty-field shifts, permissive delimiters and append behavior are model defects |
| Alternate `cmdRead` loop proves active multi-frame handling | Not connected by the accepted-socket path |
| All transport fragments are isolated per client/reconnect | Contradicted in the reviewed local/simulator code; no physical-gateway generalization |
| XML event count proves exact contents/order of both messages | Assertion loop weakness; independently checked only in the targeted helper execution |
| Fixed XML ports, private addresses, regex compression and keepalive/watchdog intervals | Local defaults/policies, not protocol constants; private values omitted |
| Historical library corrections identify deployed Firmware generations | No release/capture/device mapping establishes deployment scope |
| F422 guard proves physical routing correctness | Crash guard only; model shortcuts remain qualified |

Captures or hardware remain necessary to establish greeting/authentication behavior of the historical local server, real replay/duplicate effects, deployed revisions affected by these fixes, and physical F422/gateway routing and buffering. The absent external stack must be recovered to verify its complete classifier grammar. Remaining intermediate functional/device/simulator and BtExperience application/configuration lineages are still open. This bounded review does not establish exhaustion of the four repositories.

## Machine KB maintenance and validation

The existing coverage mechanism records five implementation sections as deferred atomic-extraction candidates and refreshes the existing Lighting section's review reason, retaining all statuses/counts. Sixty-three claim records have prepared-section digests refreshed. Of these, four existing Lighting routing claims are qualified: two Level-3 claims now use medium-confidence, version-scoped implementation provenance; the advanced-form and published-qualifier claims restrict specification attribution to Level 4. Their evidence/atomicity context was reviewed and two context records change. The other 59 claim seeds preserve their assertions and scope; five generated statements also refresh the surrounding materialized table context. No new atomic claims, section/chunk identities or claim statuses are added, removed or redesigned.

The initial build correctly rejected stale context mappings after the Lighting correction. The mappings and evidence classifications were reviewed against the corrected table and source boundary, then regenerated through the normal builder. No check or validation gate was bypassed.

| Validation | Result |
| --- | --- |
| History boundary and endpoint hashes | PASS: independent full-history parent/path set, 3,586 edges and 7,172 endpoint tree checks; all 1,000 repository/blob content hashes recorded |
| Component provenance | PASS: 564 source-revision/tree/content/body identities; all component references resolve, with 186 normalized assertion occurrences recorded |
| Original simulator parser/serializers | 17 comparisons PASS using unchanged source with Qt5 Core |
| Original local builders/framer/setup helpers | 13 comparisons PASS using unchanged method bodies with controlled byte-input/callback seams |
| Original active simulator read handler | 7 comparisons PASS with controlled byte-input/callback seams; no oversized input tested |
| Original XML receive/parse helpers | 6 comparisons PASS with controlled byte-input/callback seams, checking both payloads independently and reproducing split-character corruption |
| Original address helpers/assertions | 34 comparisons PASS: 29 unchanged archived assertion bodies and five independent qualifier/equality comparisons |
| Canonical placement and neighboring pages | Frame syntax, `WHO 0`, Lighting/Automation addressing, session/authentication, WHAT/DIMENSION and acknowledgement pages reviewed; implementation limits remain separate from protocol rules |
| Wire examples | Constructors, empty-field examples and matcher examples checked against exact assertions/original helper execution; malformed simulator inputs remain labeled defects in this record |
| Links and anchors | PASS: 45 local links/anchors, 41 public source/provenance links, all HTTP 200 |
| Build and final `check.py` | PASS: deterministic artifacts, freshness, schemas, consistency, references, text hygiene and privacy |
| Machine-KB unit tests | 59 PASS; after the Lighting correction, 19 claim-framework and Phase-12 consistency tests additionally pass; expected rejection fixtures are part of the successful privacy tests |
| Schema tests | 8 PASS |
| ESG / ECV | 146 human pages, 39 support pages; 0 objective failures; 127 style candidates and 13 existing identifier candidates |
| Epistemic drift | Existing scoped replay/parser-guidance candidates reviewed; repeated syntax/range occurrences retain their functional/interface contexts |
| Artifact manifest | PASS, 144 artifacts |
| Canonical-source audit | PASS through authorized R2 helper: 25 verified fingerprint records, 5 database integrity results `ok`, 0 failures |
| Machine-KB impact and complete diff | 416 affected claims, 48 chunks and 50 references reviewed; complete record comparison confirms only 63 claim digest updates, four qualified existing assertions and their reviewed context, six retrieval texts/derived qualification cues, matching corpus text and deterministic manifest |
| Whitespace diff | PASS, including staged new ledgers |

The 77 targeted comparisons do not execute the full legacy Qt TCP/test suites, external stack, every historical dependency combination or physical hardware. All earlier TSV source/body/history ledgers and identity/reference inputs remain byte-for-byte unchanged. The corpus retains 7,448 claims and 1,223 chunks. New atomic extraction remains deferred.
