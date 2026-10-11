# MyOpenCommunity Intermediate History Review

This continuation starts at `a1593db2dfb1e507a3c566ee233119f388e18415` on `docs/myopencommunity-integration`. It follows the [remaining-source review](myopencommunity-remaining-source-review.md) with semantic comparison of intermediate revisions, starting with the `WHO 8` device and Guard Unit message lineage. Preserved sources and Git histories remain unchanged.

## Bounded history coverage

The [intermediate dispositions](myopencommunity-intermediate-dispositions.tsv) record 1,051 changed-file edges, with exact commit/parent identities, before/after Git blobs and content SHA-256 values, scope, method, disposition and semantic basis. They cover 333 parent comparisons in 324 device-library commits and ten supplementary BtExperience teleloop corrections. There are 303 distinct nonempty endpoint blobs across both sets; an absent file is recorded with a zero Git identity and `-` content hash.

| Disposition | Changed-file edges |
| --- | ---: |
| Incorporated or used to qualify evidence | 67 |
| Corroborates existing scoped documentation | 918 |
| Excluded with semantic reason | 66 |

The device-library boundary consists of C++ sources/headers and tests named `entryphone_device`, `videodoorentry_device` or `message_device`, including the accidentally committed `entryphone_device.sarchi.cpp`. Root, `devices/`, `test/` and `devices/test/` locations were followed across extraction and renaming. Retained refs were traversed with full Git history and every relevant parent compared, including merges; ordinary path-history simplification alone omitted a debug-only intermediate variant and numerous merge comparisons.

The initial 142 parent comparisons were reviewed by changed executable behavior, assertions and comments against the final pinned classes. Relocations were compared by exact blob identity or normalized class-name changes, with actual ringtone-enum differences retained. Another 191 full-history comparisons contain 186 pairs whose endpoint blobs were already reviewed, plus five comparisons involving one extra blob. That blob differs only by an added/reverted end-call debug line. Reusing exact reviewed blobs avoids counting repeated merge history as independent corroboration. It does not execute the different application/dependency combinations of those commits.

BtExperience's ten supplementary patches were selected for teleloop fields, association timers and state transitions, then read together with the final call objects, tests and configuration consumer. This is not a complete intermediate-history review of its video/audio/UI lineage. Other functional systems, parser/serializer infrastructure and simulator histories remain outside this bounded pass; the earlier four-repository inventories and disposition records remain intact.

## Call address and state

The [initial re-arm implementation and assertions](https://github.com/OpenWebNet-HA/libqtdevices/commit/eb980660fd3f2f589928c9598069c2c9719872e7), [media-change correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/47450043bdfe4b05c5345aa57a13ee8ffe25883c), [final call tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_videodoorentry_device.cpp) and [final implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/videodoorentry_device.cpp) establish:

- `WHAT 9` stores original and current caller addresses; `WHAT 40` can change the current address while retaining the original. Exact re-arm tests distinguish `20` from `21`, and test both media types.
- Cycling targets `master_caller_address`, while lock/movement methods target `caller_address`. The reader table now says `ORIGINAL_CALLER` to avoid conflating them after a re-arm report.
- The [string-address correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/b3ee23d3a978a041f419a3100a5c723f8980b6c9) replaces a local negative-number autoswitch marker with `@` plus the complete string. [CCTV handling](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/vct.cpp) removes that marker before talker lookup and suppresses professional-studio auto-opening for autoswitch. Neither marker is sent as a wire address.
- The [floor-call correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/7f6cd2e5543e6d22236b4c48bd408d5c9223bfe5) and final test retain the previous `KIND = 1`, `MMTYPE = 4` when `KIND 13` arrives.
- [Idle receive guards and exact negative tests](https://github.com/OpenWebNet-HA/libqtdevices/commit/55cce59055e1eeb575eff1d30bfc3fad702f5c83) reject ordinary answer/end/stop-video value notifications while idle. Later pager/teleloop exceptions and the separate basic class prevent generalizing this to all `WHO 8` traffic.

These extend the historical touchscreen model on [Video Door Entry and Telephony](../../functional/who-8-video-door-entry-telephony/). They do not change published gateway semantics or establish complete address domains.

## Teleloop association and session

The [session implementation](https://github.com/OpenWebNet-HA/libqtdevices/commit/4cb81edfd22fd4f9ba9ab4414c8da72c24112009) and [exact receive tests](https://github.com/OpenWebNet-HA/libqtdevices/commit/2a032a09124d5274d6a6ce75e410917e2e25cb2f) establish `*8*79#KIND#MMTYPE#ID*LOCAL##`, tested with `1`, `4`, `5`. The parser emits boolean `TELE_SESSION` after the call-state guard; it does not compare the tuple with the configured association. The [CCTV state assertions](https://github.com/OpenWebNet-HA/BtExperience/commit/d52cdc818b946f6bb2250f06a0aaec55d8f2f393) show a pending call becoming answered with teleloop true, then resetting on termination. The [Intercom extension](https://github.com/OpenWebNet-HA/BtExperience/commit/1ffa606ad939ae408a24ddf370f291ccca17ef13) supports the same pending/unanswered guard through implementation evidence.

The [earlier init-path test](https://github.com/OpenWebNet-HA/libqtdevices/commit/23c7adbfa35d33732a28290af8149c0716de1444) sends `*8*77#7*LOCAL##` from `init()`. The [subsequent connection-init correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/a4eea243634f8a20d356d791eea318d019fc5d47) deletes that test and moves the frame into the cache's initialization list. Final `setTeleloopId` removes the previous nonzero-ID frame, registers the new one if nonzero, and sends no unlink for zero. [Cache dispatch](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/devices_cache.cpp) sends registered initialization commands through `FrameSender` with `DELAY_NONE` before normal/lazy device initialization. This explains the historical delay correction, not a measured packet deadline.

The [association application and assertions](https://github.com/OpenWebNet-HA/BtExperience/commit/04c8a528a08229e71149ef9f864e70066b0c60f5) accept a result only while associating. The [millisecond correction](https://github.com/OpenWebNet-HA/BtExperience/commit/909ca5fa5d75701b531c9ae1bc498a76ee883d77) changes the initial 11-ms mistake to 11 seconds. The [expiry correction](https://github.com/OpenWebNet-HA/BtExperience/commit/f9e35aaca6a93f223dbc096cba9a28d525fdd87c) moves the active-timer guard to received timeout handling; a single-shot expiry callback must still signal after its timer stops. Tests that begin with ID zero do not establish that a timeout clears a pre-existing association.

## Message checksum and test limits

The [checksum implementation history](https://github.com/OpenWebNet-HA/libqtdevices/commit/21ed266edd52cbe10aa7c4ab77bccd7c028815c8) briefly passed `message.toUtf8()` back into a QString checksum helper; the [subsequent correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/e27546020780d09f9fdf750a9248dc1662e6ff9e) uses the accumulated QString directly. The initial single-byte character append and absent checksum logic are superseded implementations, not alternative valid payload encodings.

The final checksum/parse helpers and Message equality operator were compiled unchanged with Qt5 Core, once with signed plain `char` and once with unsigned plain `char`. Each build passed eight independent comparisons: the archive's `0xE49B` vector, empty/ASCII checksums, two high-byte input results, exact timestamp, exact parsed text, and the defective equality behavior. U+FFFF alone returns `-1` versus `511`; U+8000 alone returns `-127` versus `641`. The reader formula is therefore now explicitly the unsigned-byte, non-negative-modulo form; it is not claimed as byte-exact across builds or as physical Guard Unit behavior. These 16 comparisons do not execute the full legacy receive/transport suite.

`Message::operator==` compares `m2.text` with itself. Its [introduction](https://github.com/OpenWebNet-HA/libqtdevices/commit/0c785c9517a843c32abd58f261d1148357ad2e44) includes direct datetime/text assertions, but the [later struct comparison](https://github.com/OpenWebNet-HA/libqtdevices/commit/ef62372f15f830f278f4ef973dbb7104efefa03f) loses independent text checking. The harness compares parsed text directly and confirms that equal timestamps with different text nevertheless compare equal through this operator. Final buffer assertions also establish the accumulated string. Likewise, two final caller-report test cases convert a string address to bool through `DeviceChecker<T>`; their true assertions cannot prove its exact value. Direct string/state assertions and executable assignments supply that evidence.

Final `MessageDevice` restarts its 5-second timer for parameter/data blocks and a matching checksum, and `sendTimeout` uses QString length, counting UTF-16 code units rather than checksum bytes. An end frame publishes a nonempty buffer without a separate checksum-success flag. The successful end-to-end fixture does not prove that every publish requires a prior checksum, validates the parameter schema, or preserves sender/destination identity across all chunks. No such enforcement guarantee is added.

## Deliberate exclusions and unresolved questions

| Finding | Reason for exclusion or limit |
| --- | --- |
| Teleloop ID `1..9` as universal wire range | Added to an application property comment; setter/parser do not enforce it; tests establish only sample IDs |
| Timeout clears a previous teleloop ID | Tests start from zero; timeout handler stops association without clearing stored ID |
| Teleloop session tuple authenticates the association | Decoder discards the fields into a boolean; no matching/authorization assertion |
| Early short end-call form or temporary external-intercom kind `6` | Subsequent correction/tests establish literal `4` prefix and external kind `7` |
| Full malformed-frame safety | Debug assertions and incomplete field validation are not a total acceptance/rejection grammar |
| All messages require checksum success or validated parameters | No success flag; parameter block only restarts timer; tests cover particular successful/rejected sequences |
| Comment checksum weights, 3-second timer and received-byte wording | Executable loop, final constant and QString length take precedence |
| UI/plugin `enable` and `mode` as protocol fields | Local persistence/configuration selects association ID; no extra wire vocabulary |
| Library state fixes as Firmware releases | Source dates and commits do not identify deployed product/Firmware revisions |

Hardware/captures remain necessary for unusual message character/checksum behavior, complete call/teleloop address and ID domains, real association/reconnect behavior, and deployed revisions affected by historical fixes. No repository exhaustion claim follows from this bounded lineage review, endpoint reuse or helper execution. The subsequent [transport history review](myopencommunity-transport-history-review.md) covers serializer/parser, local session and address-matcher corrections. Remaining functional/device/simulator lineages are still open.

## Machine KB maintenance and validation

The existing coverage mechanism refreshes the three historical sections' candidate/deferred review annotations. Six retained claims have only their prepared-section digests refreshed; their exact supporting blocks, indexes, statements, applicability and context are unchanged. The corpus retains 7,448 claims and 1,223 chunks, with no added/retired identities. New atomic extraction remains deferred.

| Validation | Result |
| --- | --- |
| Dispositions and retained history boundary | PASS: 1,051 file edges, 2,102 endpoint tree/hash checks; independently reconstructed full-history parent/path set matches the device-library ledger |
| Original checksum, text parser and equality helpers | 16 comparisons PASS across signed/unsigned plain-char builds; checks include deliberate reproduction of equality weakness |
| Reader and neighboring pages | Video Door Entry, Basic Video Door Entry, Multimedia System and session pages reviewed for scope, canonical placement and presentation |
| Frame examples | `WHAT 78/79` syntax checked against exact receive tests; cycling placeholder corrected against original/current caller state; all other existing frames unchanged |
| Local links and heading anchors | 17 checked, all resolve |
| Public source/provenance links | 27 checked, all HTTP 200 |
| Build and final `check.py` | PASS: deterministic artifacts, freshness, schemas, consistency, references, text hygiene and privacy |
| Machine-KB unit tests | 59 PASS; final coverage-annotation change additionally checked by claim-framework and consistency suites |
| Schema tests | 8 PASS |
| ESG | 146 human pages, 38 support pages; 0 objective failures, 127 advisory candidates |
| ECV | 0 objective failures; 13 existing identifier candidates unchanged |
| Epistemic drift | Changed-page candidate is the existing scoped decoder paragraph; repeated frame/range candidates retain distinct contexts |
| Artifact manifest | PASS, 144 artifacts |
| Canonical-source audit | PASS through authorized R2 helper: 25 verified fingerprints, 5 database integrity results `ok`, 0 failures |
| Change impact and complete diff | 13 affected claims, 7 chunks, 6 references reviewed; actual generated changes are six digest fields, three retrieval texts, matching corpus text and deterministic manifest |
| Whitespace diff | PASS, including staged new records |

All earlier source/body/history ledgers are byte-for-byte unchanged. Coverage statuses/counts and all claim/context/identity records retain their meanings. No full legacy Qt receive/transport suite or hardware experiment was executed.
