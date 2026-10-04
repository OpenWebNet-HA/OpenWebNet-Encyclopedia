# MyOpenCommunity Sound History Review

This continuation starts at `a603ce35130aeecd9ffebaabeb6eff657a99531b` on `docs/myopencommunity-integration`, following the [CEN and Transversal review](myopencommunity-cen-history-review.md). It compares WHO 16/22 source activity, radio controls, virtual audio feedback and direct BtExperience consumers with the canonical sound pages. Earlier chat examples are context, not the discovery boundary. Preserved repositories, retained Git objects and synced sources remain read-only.

## History index and semantic boundary

The [history dispositions](myopencommunity-sound-history-dispositions.tsv) retain 28,231 changed-file edges against every selected retained parent, including merges. Independent reconstruction verifies 56,462 endpoint tree identities and 10,644 nonempty repository/blob identities. The [component dispositions](myopencommunity-sound-component-dispositions.tsv) retain source-tree revisions, raw complete-file SHA-256, normalized component hashes, assertion identities, comparison references, endpoint presence and explicit review methods.

| Repository | Discovered paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 182 | 20,773 | 4,722 | 4,292 | 7,495 |
| libqtcommon | 12 | 1,470 | 618 | 598 | 461 |
| BtExperience | 156 | 5,988 | 1,938 | 1,799 | 2,688 |
| MyHomeSystemEmulator | 0 | 0 | 0 | 0 | 0 |

Discovery screens 32,992 retained C++/header, XML, QML, JavaScript and build blobs for sound, amplifier, radio, matrix, virtual-source and WHO-leading 16/22 literals. Matching filenames and basenames close over earlier directory locations. The index includes generic factories, UI, local media and alarm files because they contain relevant identifiers; matching is not a semantic verdict on the whole file. No dedicated audio implementation is identified in the emulator's 395 screened blobs. This does not prove absence of generic literal dispatch or unsupported hardware functionality.

| Review method | Component variants | Meaning |
| --- | ---: | --- |
| Full component comparison | 454 | Retained critical source/radio/virtual-feedback decoder and writer bodies; earlier sound/radio/matrix interpreters; direct BtExperience sound consumers, factories and associated tests |
| Pinned full component comparison | 154 | Pinned sound-device writers/decoders, virtual/composite amplifier behavior and exact media-device tests; other historical variants of these components are not silently certified |
| Prior semantic review reuse | 90 | Exact basename/name/body identities from Scenario, Lighting/Automation and Auxiliary ledgers; explicit prior IDs retained, without independent sound corroboration |
| Indexed scope only | 6,863 | Discovery and component/assertion identities only; broader UI, declarations, generic Configuration, alarms and peripheral histories remain excluded from new claims pending semantic comparison |

The two full comparison methods contain 364 normalized assertion/check identities. Across all methods, 1,797 identities are retained as an inventory; indexed and reused assertions are not counted as newly reviewed. The 93 critical bodies were additionally read in full across their retained variants, without removing logging statements. Exact pinned media-device and BtExperience media-object tests take priority over comments. The targeted execution checks below do not replace these comparisons.

There are 637 normalized component identities present at pinned endpoints, including indexed-only material. The disposition totals are 39 incorporated, 315 corroborating and 7,207 excluded components; history edges total 201 incorporated, 284 corroborating and 27,746 excluded. Excluded includes intermediate bodies that must not become current/deployed rules, and indexed material whose semantics remain unreviewed. These totals are traceability counts, not proof of extraction completeness.

The broad whole-file inventory contains 13,648 endpoint pairs and 1,074,863 normalized diff lines. It is not full semantic coverage. Normalization removes comments/blank indentation and redacts private fixtures; raw hashes preserve original bytes, including non-UTF-8 source. Comparison references identify earlier encountered same-basename/name variants, not necessarily Git parents; actual retained-parent edges are separate ledger fields. Compact comparison views collapse presentation differences, but claims are verified against original bodies and actual parent corrections. Shared history is not independent evidence.

This closes the explicit source-activity, radio, virtual-feedback and direct-consumer boundary. It does not close every indexed sound-related UI, alarm scheduler, player/backend, configuration fixture, equalizer lifecycle or malformed-frame path, and does not claim repository exhaustion.

## Sources and canonical placement

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Sound implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.cpp), [API and constants](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.h), [exact media assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_media_device.cpp), [frame constructors](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp) |
| libqtdevices | `175e38f3b9fd751ec2c00ab09cc0aecae067f5b0` | [Earlier sound/radio/matrix interpreters](https://github.com/OpenWebNet-HA/libqtdevices/blob/175e38f3b9fd751ec2c00ab09cc0aecae067f5b0/frame_interpreter.cpp); exact source-tree revisions for other variants are in the component ledger |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Source/amplifier consumers and factories](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/mediaobjects.cpp), [exact consumer assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_media_objects.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Shared historical transport/UI matching; no independently established audio dialect from this review |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | No dedicated sound model found within the discovery screen; generic configured dispatch is separately covered by the Scenario review |

[Sound System](../../functional/who-16-sound-system/) gains a scoped volume/power-cache qualification and review link. [Sound Diffusion](../../functional/who-22-sound-diffusion/) gains tested source-selection and virtual-report forms, activity/cache scope, radio/RDS policy, percentage volume conversions, the relative-balance conflict and local-player/request boundaries. No new reader-facing page or Practical Guide is needed. [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md) remains canonical for captured routing and dialect pairs; its existing claims are corroborated without duplicating them. [UPnP Multimedia](../../functional/who-26-upnp-multimedia/) remains separate from a local player's use of UPnP media.

## Source activity and local control

SourceDevice uses WHO 22, WHERE `2#SOURCE`, multimedia type 4. Initialization requests dimension 13. The exact general-selection assertion (`S0172`) emits eight `35#4#AREA#SOURCE` commands at `3#AREA#0`, areas 1..8. `S0060..S0061` distinguish a null QString from literal `"0"`; the latter sends one area-0 command. This is a client expansion, not a newly established broadcast grammar.

The own-source decoder (`S0066`) accepts `2#SOURCE` or `5#2#SOURCE`. Dimension 13 replaces its active-area set with every flag index whose value is 1; exact tests exercise sixteen flags, including 0 and 15. WHAT 2 adds one area, and OFF dimension 12 clears the set. Monochannel WHAT 2 collapses its area to 0; the dimension-13 branch itself preserves flag indices. The documentation's monochannel qualification therefore concerns incoming area notifications, not automatic collapse of every possible response.

The [other-source correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/7a745545ee36a599bf7b8ff7925a0b092c65ab80), including `S0179`, removes a cached area when another source becomes active there. The dimension-13 other-source loop returns after removing its first overlapping flag. No claim of complete multi-area reconciliation from one competing vector is added. Earlier guard/notification-value changes are local decoder history, not alternative valid protocol grammars. Namespace subscription and the external OpenMsg parser remain upstream of these bodies.

BtExperience SourceBase (`S6034`, exact `S6139`) projects indices 0..8 and emits activeAreasChanged only for a changed list, activeChanged only across empty/nonempty state. SoundAmbient maintains current/previous sources and counts active amplifiers, notifying on first ON/last OFF. General-ambient last UI selection is not authoritative confirmation of every physical area.

VirtualSource's local next/previous methods (`S0079..S0080`) emit values with DIM_SELF_REQUEST, without a bus frame. Source-addressed WHAT 9/10 reach the local player; the general-amplifier delegate (`S0064`) accepts next 9 only when active in that area, or when its sole cached area is 0. It does not implement area-addressed previous 10. The [activation correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/5c8aeb5ff10dceced5c319d1c2b85e9327faf596) changes the virtual activation request from notification 2 to command 1 and updates the exact test. Published station 9/10 and track 11/12 labels are not overwritten by a method named nextTrack.

SourceMultiMedia (`S6042`) calls the player for next/previous, resumes paused playback and pauses when inactive. Bus-origin activation can force a stopped player to cycle configured local sources; a GUI self-request does not force that search. The [termination experiment reversal](https://github.com/OpenWebNet-HA/BtExperience/commit/88099739cbaa5a6b0635bc895312f50781721bd3) restores pause instead of terminate. This is application lifecycle, not a wire change. Early placeholder handlers do not independently prove complete playback support.

Factories (`S5963..S5970` and retained variants) select radio/aux/local source delegates and amplifier/general routing from Configuration. The [multichannel initialization correction](https://github.com/OpenWebNet-HA/BtExperience/commit/0c812ac32a95167d127e79b46c9ef5572d0bb945) explicitly sets both source and amplifier flags. Aux-labelled objects here use sound delegates, not WHO 9. USB/SD/UPnP object IDs and local media backends do not establish numeric WHO 26 frames.

## Radio, RDS and display scales

The [automatic-tuning correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/650201590441462d90439dd69135f29efbd58760) changes empty-step serialization from `5#`/`6#` to `5`/`6` and suppresses manual tuning while the cache is unknown. Earlier exact expectations establish those earlier client emissions, not preferred canonical syntax. `S0069..S0070` interpret frequency as MHz multiplied by 100, adjust by 5 per manual step and wrap at the client bounds 8750/10800. Earlier variants added, capped or wrapped the local estimate differently; none maps a deployed tuner Firmware generation.

BtExperience SourceRadio schedules a one-shot frequency read after manual tuning; exact `S6146` checks 9800 -> 9810 for two steps and an active request timer. Automatic search sets the displayed frequency to -1 and waits for receipt. A client estimate is not a physical tuning capture. Published unusually small step units remain unresolved rather than silently relabelled.

The [RDS subscription change](https://github.com/OpenWebNet-HA/libqtdevices/commit/78ed1032150e13b2861c90d667d6ad216c66427e) adds subscriber counting and a 100-ms delayed last stop. `S0074..S0077` start on the first subscriber, cancel a pending stop without another start, and resend 31 after received 32 only when updates remain enabled. Earlier variants subscribe during init and react unconditionally. The corrected behavior is local policy. Dimension 10 decodes every decimal value as QChar; the pinned library tests assert `hello!`, and the consumer asserts `Prova 123`, without establishing a fixed eight-character WHO 22 domain.

WHO 16 continues to carry eight separate dimension-8 values. The [Unicode correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/aa28c4d78b57907991aaf321a0ed94ba368734be) replaces two packed cache integers with eight character values and changes UI reconstruction; the wire field count does not change. Earlier sound interpreters (`S1877`, `S3787`, `S4751`, `S4957`) pass an unchanged-power marker for volume reports. Other earlier variants inferred ON. The new WHO 16 sentence is explicitly about clients that keep the caches separate, not all historical clients or a new physical power rule.

BtExperience's [percentage conversion change](https://github.com/OpenWebNet-HA/BtExperience/commit/a11dbdc84407454c2b30e467b54c072e5ecaa5b8) replaces raw application values with integer `P*31/100` for writes and `V*100/31` for display (`S6063`, `S6067`). Exact `S6157` checks 0 -> 0, 62 -> 19, 100 -> 31; `S6159` checks 12 -> 38 and 13 -> 41, suppressing equal display repeats. These API percentages are distinct from the already documented local 0..8 setting and icon bands. They are not acoustically calibrated and are not inverse conversions.

## Virtual feedback and balance conflict

VirtualAmplifier initializes OFF/0 and publishes those cached values through updateStatus/updateVolume (`S0105..S0107`). Exact `S0221..S0222` confirm general-speaker report addresses `5#3#AREA#POINT`, state `12*STATE*3` and volume `1*VOLUME`. The [address correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/5ca9a8eeb6463a7e8cf51a66116547898caefc35) changes both writers and tests from direct speaker addresses to that report form.

Its local volume operations emit self-request values without bus writes. Power operations also issue ordinary bus power commands. The factory constructs a virtual amplifier at its configured address and composites for matching area/general controls. Composites forward power and relative-volume operations to ordinary and virtual delegates, but do not provide authoritative aggregate state; no absolute-volume fanout is inferred from the absence of an override. Local requests and locally published reports are kept separate from receipt of physical amplifier feedback.

The [library balance correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/93afb0fd371b45a67486af313631aa8d70a7cf22) renames balanceUp to balanceLeft and balanceDown to balanceRight, correcting comments and callers while retaining exact 42#1/43#1 expectations. The [BtExperience delegate correction](https://github.com/OpenWebNet-HA/BtExperience/commit/aaf8e7bdd41dfadae71a8335444c91ad45f17f1a) follows those names. This contradicts the published relative-direction labels. No capture or hardware assertion resolves physical direction, so the published table remains and the conflict is visible beside the existing textual absolute-balance interpretation.

## Exclusions and unresolved work

| Candidate | Disposition |
| --- | --- |
| Repository dates or library revisions identify deployed Firmware generations | Excluded: no product/deployment mapping |
| Sixteen active flags prove published area capability 0..15 | Excluded: exact library acceptance; application projection is 0..8 |
| General source selection is one broadcast frame | Qualified: tested method expands null area to eight writes; explicit 0 differs |
| Competing source vectors fully reconcile all overlaps | Excluded: decoder returns after its first removal |
| Volume receipt universally proves amplifier ON | Excluded: cache variants differ, separate state reports exist |
| Manual 50-kHz cache step resolves published unit error or all tuner bands | Excluded: client estimate/policy without hardware verification |
| Earlier trailing-empty automatic frames are canonical syntax | Excluded: corrected writer/tests preferred; external parser tolerance unresolved |
| Every unsolicited RDS stop requires resubscription or 100-ms Device delay | Excluded: subscription and debounce are local policy |
| WHO 16 packed RDS cache means two wire fields or WHO 22 has eight-character limit | Excluded: wire and cache representations differ |
| Local next/previous method names override published track/station numbering | Excluded: consumer naming and scoped dispatch |
| Area-addressed previous 10 is supported by the next delegate | Excluded: delegate implements only next 9 |
| Virtual/composite reports confirm physical playback or all amplifier states | Excluded: local cache/request feedback; no aggregate parser |
| Relative balance left/right established by names or correction message | Unresolved: exact numbers conflict with publication; physical direction unverified |
| Configured radio count or preset fixture defines all product capacity | Excluded: Configuration and UI choices; published F500/F500N distinction retained |
| Custom preset-name factory is validated by preset wire tests | Excluded: factory tag/index matching has untested inconsistencies; tests cover wire index mapping, not configured labels |
| Private setup fields 9, 9, empty or matrix sentinels define general multimedia grammar | Excluded: writer/cache behavior without independent field semantics |
| Aux names, player UPnP support or empty emulator screen establish another numeric namespace | Excluded: direct delegates establish sound/local-media scope only |
| Indexed peripheral histories are fully reviewed | Excluded: 6,863 components retain indexed-only status; no semantic closure claimed |

Captures or hardware are needed for balance direction, actual tuning increments/band/wrap behavior, source-address/area domains beyond published values, setup fields and product/Firmware applicability. The external OpenMsg implementation is needed for malformed, missing and trailing-empty field acceptance. Broader alarm ordering/configuration, equalizer lifecycle, player/backend transitions and peripheral UI histories remain possible source-review avenues rather than hardware-only questions.

## Machine KB maintenance and validation

Existing sections retain their coverage status and claim counts, with additions marked as candidates for later atomic extraction. Retained claim digests are refreshed only when existing statements, supporting blocks/indexes and context remain identical. Nineteen existing claim digests are refreshed. Two context block indexes shift with the inserted WHO 16 paragraph; statements, source/evidence metadata and supporting block text remain identical. All 7,448 claim and 1,223 chunk identities are retained; eight retrieval texts and five qualification-cue sets reflect the canonical edits. No atomic claims or section identities are added or redesigned.

A Qt 5 Core harness compiles 22 original bodies and passes 31 comparisons for null/zero selection, sixteen area flags, competing-source removal, OFF/monochannel caches, next-only area dispatch, tuning/wrap/unknown cache, RDS subscriptions/stop receipt, combined frequency/station, virtual reports versus requests and percentage conversion/repeats. OpenMsg fields, output, signals, timer scheduling and delegates are controlled seams. It does not execute the complete archived suites, external parsing, real timer/event-loop behavior, transport or hardware, and does not prove history exhaustion.

| Validation | Result |
| --- | --- |
| Independent retained-history reconstruction | Pass: 28,231 edges, 56,462 endpoint tree identities, 10,644 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 7,561 source tree/content/body identities and 1,797 assertion identities; 364 assertions within the two full comparison methods; inventory distinguished from semantic coverage |
| Bindings and reused scope | Pass: all history/component bindings and destinations, comparison references and 90 prior exact-body references |
| Targeted original-body execution | Pass: 31 comparisons across 22 original bodies; controlled seams and scope stated above |
| Machine-KB unit/schema suites | Pass: 59 unit tests and eight schema tests; expected negative privacy fixtures rejected |
| Normal build and deterministic integrity | Pass: freshness, schemas, references, manifest, privacy and cross-artifact consistency |
| Artifact/canonical-source audits | Pass: 144 registered artifacts, 25 verified fingerprints, five database integrity results `ok`, no audit failures; authorized privileged R2 helper used |
| Links and wire examples | Pass: 25 local/anchor targets and 20 public source links; new forms verified against exact original assertions and writers |
| Style/Core Values and epistemic review | No objective failures; existing advisory candidates retained; protocol/client/product/Firmware scopes reviewed against neighboring sound/matrix/UPnP pages |
| Complete diff and Machine-KB impact | Two canonical pages, three provenance records and seven KB maintenance inputs/artifacts; statements/evidence/support unchanged, two block-index shifts; no full-KB review flag |

The first public-link check found an interpreter link pointing at a removing commit. It was corrected to the actual parent revision verified by the source tree and component ledger; the final link check passes. No validator was bypassed or changed.

The complete diff and staged contents are reviewed for duplication, unsupported generalization, canonical syntax, privacy, presentation and source immutability. Published tables, captured matrix routing and unrelated device-description work remain unchanged. The bounded review and its pending indexed peripheral coverage are explicit above.
