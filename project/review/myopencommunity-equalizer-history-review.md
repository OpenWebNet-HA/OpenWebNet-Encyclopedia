# MyOpenCommunity Equalizer and Preset History Review

This continuation starts at `ca8c30d8d9b17fc9b0756cd8a052af02a5ceb0d1` on `docs/myopencommunity-integration`, following the [Sound history review](myopencommunity-sound-history-review.md) and [Alarm-clock history review](myopencommunity-alarm-clock-history-review.md). It closes a bounded comparison of the power-amplifier preset/tone/balance/loudness client, its direct Configuration/model/UI consumers and earlier retained implementations. Earlier chat examples are context, not the discovery boundary. Preserved repositories, Git objects and synced sources remain read-only.

## History index and semantic boundary

The [history dispositions](myopencommunity-equalizer-history-dispositions.tsv) retain 13,078 changed-file edges against every selected retained parent, including merges. Independent reconstruction verifies 26,156 endpoint tree identities and 5,097 nonempty repository/blob identities. The [component dispositions](myopencommunity-equalizer-component-dispositions.tsv) preserve exact tree revisions, whole-file SHA-256, normalized component/assertion hashes, comparison references, pinned presence and explicit review scope.

| Repository | Discovered/dependency paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 76 | 9,312 | 2,792 | 2,566 | 3,440 |
| libqtcommon | 4 | 653 | 286 | 275 | 152 |
| BtExperience | 75 | 3,113 | 1,394 | 1,302 | 1,505 |
| MyHomeSystemEmulator | 0 | 0 | 0 | 0 | 0 |

Discovery screens 32,992 retained C++/header, XML, QML, JavaScript and build blobs for power-amplifier, equalizer/preset/loudness, tone and balance identifiers, including earlier Italian names. Matching basenames close across earlier directory locations. Direct XML attribute/child helpers, frame writers, list insertion/lookup and control dependencies are added across retained paths. The emulator's 395 screened blobs identify no dedicated equalizer/preset model; this does not prove absence of generic dispatch.

| Review method | Component variants | Meaning |
| --- | ---: | --- |
| Full component comparison | 623 | Complete power-amplifier/helper/test bodies, legacy controls, direct XML/model dependencies, earlier sound-system factory bodies and complete selected QML controls |
| Field screen | 81 | Matching constants, names/counts, declarations and related fields; not full-header semantic closure |
| Prior semantic review reuse | 334 | Exact basename/name/body identities from Sound or Alarm-clock reviews, with prior IDs; no independent corroboration |
| Indexed scope only | 1,832 | Discovery/component/assertion identities only; broader UI, generic mappings, complete XML fixtures and unrelated media remain excluded from new claims |

Full comparisons contain 219 normalized assertion/check identities; the full inventory retains 948. Totals are 28 incorporated, 51 corroborating and 2,791 excluded components, and 43 incorporated, 45 corroborating and 12,990 excluded edges. The 387 identities present at pinned endpoints include indexed-only material. These are disposition counts, not atomic facts or proof of extraction completeness.

All 704 selected full-component/field variants are compared across earlier locations and intermediate revisions. Complete earlier `createSoundDiffusionSystem` factories are included, rather than certifying only their matching preset lines. Normalization removes comments and blank indentation and redacts private fixtures; raw hashes preserve original bytes. Comparison references identify previously encountered same-name/basename variants, not necessarily Git parents. Actual retained-parent edges preserve chronology separately. Shared ancestry is not independent evidence; no compact-view equivalence certifies an unread body.

This closes the stated client/control and direct-consumer boundary. It does not close every indexed factory/UI/configuration artifact, external OpenMsg parsing, generic emulator dispatch, band/curve programming by other software, hardware persistence or all four repositories. Repository exhaustion is not claimed.

## Sources and canonical placement

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Power-amplifier implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.cpp), [constants/API](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.h), [exact wire assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_media_device.cpp), [frame writers](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp), [XML helpers](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/xml_functions.cpp) |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Factory and consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/mediaobjects.cpp), [consumer assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_media_objects.cpp), [parent/instance fallback](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/xmlobject.h), [row lookup](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/mediamodel.cpp), [Object model](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/objectmodel.cpp), [preset menu](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/Components/SoundDiffusion/AmplifierEqualizer.qml), [settings controls](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/Components/SoundDiffusion/AmplifierSettings.qml), [loudness control](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/Components/SoundDiffusion/Loudness.qml) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Copied historical power-amplifier tests/implementations compared; shared lineage supplies no independent preset dialect |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | No dedicated equalizer/preset hit in the stated screen; generic configured dispatch remains separate |

[Sound Diffusion](../../functional/who-22-sound-diffusion/) gains a compact table within its existing Tone, balance, and presets section, the custom-ID/description qualification and a client capability boundary. Existing protocol tables and tested wire mapping are corroborated, not replaced. Sound System, matrix routing and UPnP neighboring pages are checked; no new reader page or Practical Guide is needed.

## Assertions, implementation and disposition

Pinned library assertions `E0207..E0222` establish relative high/low tone and balance emissions, next/previous presets, canonical write markers, setter indices `9 -> 11` and `10 -> 16`, loudness `0/1`, tone integer conversion and normalized preset reports. `E0219` asserts `2 -> 0`, `6 -> 4`, `11 -> 9`, `16 -> 10`, `25 -> 19`, and no signal for `12` or `15`. These corroborate the existing mapping; exact tests outrank malformed earlier writers and comments. The source setter `E0107` forwards indices outside `0..19` unchanged, which does not validate additional wire presets.

`E0092` initializes reads for `12,1,19,2,4,17,20`. Order comes from executable implementation rather than a dedicated initialization-order assertion. `E0093` gates by amplifier address, nonempty arguments and dimension-frame classification, delegates state/volume to the base, then decodes loudness, tones, balance and preset. It supplies no medium-tone `3`, 3D `18` or band-selector `21` branch. These class omissions do not prove that an amplifier lacks those capabilities or that another client cannot program them. The external OpenMsg parser and malformed-input domain are outside this review.

BtExperience factory `E1682` uses `epre11..epre20 == "1"` to include custom entries, defaulting their names to User 1..10. Instance fields override parent attributes. Child names starting with `pre` are read by prefix helper `E0007`; their numeric suffix changes a name only when its entry is enabled. The helper is distinct from `getChildrenExact`. This resolves the prior Sound review's unverified custom-tag handling, but does not establish a universal Configuration schema or bus label format.

Constructor `E1686` inserts ten built-ins with IDs `0..9`, then appends QMap custom entries in key order while preserving their IDs. `E1693` obtains the description by list row through ObjectDataModel and MediaDataModel, not by ID. The preset menu assigns `itemObject.objectId` to the preset property. Therefore the factory's ID `11` for the first custom preset is sent by the current library as wire `17`; a wire `16` report normalizes to index `10` and describes row `10`. With gaps, that row can name a different custom entry or be absent. ID `20` is forwarded unchanged, not mapped to the tenth custom wire value `25`. These are demonstrable client composition inconsistencies, not alternative OpenWebNet preset domains or physical results.

Exact consumer assertion `E1754` selects the appended entry's ID `11`, not its row `15`. `E1759` expects normalized value `12` to display `P3`, because its synthetic custom fixture uses keys `0..4` and `11` appended after the built-ins. Those assertions clarify the model's behavior but do not certify the Configuration factory's custom IDs. The original parser/model/serializer execution below verifies that composition separately with parent fallback, enabled flags and sparse entries.

`E1692`, `E1695` and the tone/balance delegates dispatch immediately. `E1704` changes local fields and emits notifications only for changed reports. Constructor zero/false values are cache defaults, not physical readings. The complete pinned Equalizer/Settings/Loudness QML flow selects existing presets and sends relative tone/balance or absolute loudness immediately, with no Save/Reset or band/curve editor in that flow. Neither display state nor a completed setter call confirms ACK, audible output or persistence.

## Historical corrections and exclusions

Actual-parent corrections are checked for [preset decoder normalization](https://github.com/OpenWebNet-HA/libqtdevices/commit/1a974f34d7f71d09482d2e7a43efdc302be5094a), [preset setter conversion and exact tests](https://github.com/OpenWebNet-HA/libqtdevices/commit/15d8a99d467a8698cb7bb80e06656ccc34832331), [loudness write marker and assertions](https://github.com/OpenWebNet-HA/libqtdevices/commit/f7140682440d94413dba8659d37ac838921daf89), [sparse custom keys and QML ID selection](https://github.com/OpenWebNet-HA/BtExperience/commit/f37039c05ff71e823da728b29fe7f9b7cbbe54f3), and [enabled-entry filtering](https://github.com/OpenWebNet-HA/BtExperience/commit/815768184a59689638e048f305f884145294da64). The decoder conversion moved from earlier UI handling into the library; the later setter correction supplied the reverse conversion. Chronology is client history, not evidence of deployed Firmware generations.

Compared earlier factories consume list-style preset children, then indexed `pre` children, then sparse maps and enabled flags. Earlier core UI keeps fixed placeholder slots, wraps local preset counters and uses local tone/loudness presentation before executable delegates exist. The earlier lowercase device model has an empty or short-circuited receive path and a local preset bound of `20`; that bound is not a wire domain. Some early balance controls swap icons/handlers, and placeholder preset names differ. Neither those local counters nor header claims that the last ten rows are custom establish a fully populated menu, bus domain or physical preset curve. Historical handler/parser guards and malformed emission fixes remain scoped to their implementations.

| Candidate | Disposition |
| --- | --- |
| Menu IDs, row numbers, normalized indices and wire presets are interchangeable | Corrected: factory/model/serializer composition distinguishes all four |
| Custom labels or `epre` flags program an amplifier curve | Excluded: names/existence only; no curve serializer in the reviewed flow |
| Equalizer menu establishes eight-band editing | Excluded: it selects presets; published band selectors remain separate |
| Setter inputs outside `0..19` are valid additional presets | Excluded: unvalidated forwarding is not support evidence |
| Changed display or setter completion proves sound, ACK or persistence | Excluded: local dispatch/cache only |
| Missing decoder branches prove missing physical capability | Excluded: class coverage only |
| Balance method names resolve published right/left conflict | Excluded: no new physical-direction evidence; canonical unresolved statement retained |
| Early placeholder names/counters revise current published domains | Excluded: local presentation and intermediate code |
| Commit dates or conversion changes identify deployed Firmware | Excluded: no product/deployment mapping |
| Indexed XML/configuration or shared copied tests close all source coverage | Excluded: field/index scopes and shared ancestry remain explicit |

Captures or hardware are needed for deployed applicability, actual preset curves and effects, persistence across power/reconnection, physical balance direction, and band/3D support and payload domains. Further source work can compare remaining generic mapping/UI fixtures, other programming clients and the complete configuration generation/export path. That is distinct from the demonstrated factory/model mismatch.

## Machine KB maintenance and validation

Ten retained claim digests are refreshed after extending the existing section. All 7,448 retained claim identities, statements, evidence metadata, supporting blocks and context indexes remain unchanged; no new section/chunk identity or atomic claim is added. The existing zero-claim Tone, balance, and presets coverage record keeps its status/count and now points to this review alongside the Sound review. Candidates are recorded here for later atomic extraction.

A targeted Qt harness compiles 39 original method bodies plus the inline XmlObject class and passes 89 comparisons. It checks canonical serialization, all 20 normalized preset mappings, gaps and unchanged out-of-domain forwarding, report classification, tone/loudness conversion, immediate setters, repeated reports, original list insertion/row lookup, parent/instance Configuration fallback, enabled prefix-tag labels, sparse selection/description mismatches and the existing `P3` fixture. Qt supplies actual DOM parsing. Signals, base-cache handling, translation, device-cache ownership and OpenMsg fields are controlled seams. This does not run the full archived suites, external frame parsing, QML rendering/event delivery, hardware or physical playback.

Two official Qt XML headers are fetched to the temporary harness directory because development headers are absent locally, and linked against the installed Qt 5 XML library. No system package, source archive or repository build dependency is changed. The initial broad type-matching helper was stopped after excessive backtracking; an explicit return-type pattern handles earlier pointer-template factory returns. Final inventories and provenance are rebuilt and independently verified with that corrected extractor.

| Validation | Result |
| --- | --- |
| Independent retained-history reconstruction | Pass: 13,078 edges, 26,156 endpoint tree identities, 5,097 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 2,870 tree/content/body identities and 948 normalized assertion identities; inventory distinguished from semantic coverage |
| Bindings and prior scope | Pass: all component/history bindings and canonical destinations; 334 prior exact-body references verified |
| Targeted original-body execution | Pass: 89 comparisons across 39 original methods plus inline XML helper; controlled seams stated above |
| Machine-KB unit/schema suites | Pass: 59 unit and eight schema tests; expected negative privacy fixtures rejected |
| Normal build and deterministic integrity | Pass: freshness, schemas, references, manifest, privacy and cross-artifact consistency; final coverage refresh checked again |
| Artifact/canonical-source audits | Pass: 144 registered artifacts, 25 verified fingerprints, five database integrity results `ok`, no audit failures; authorized R2 helper used |
| Links and wire examples | Pass: 16 local/anchor targets and 19 public source/archive links; current writers/assertions and targeted execution verify the cited syntax |
| Style/Core Values and epistemic review | No objective failures; advisory repeated ranges and existing observations reviewed, with scoped implementation wording retained |
| Complete diff and Machine-KB impact | One canonical page, three provenance records and six KB maintenance inputs/artifacts; no retained claim statement, supporting block, context, section/chunk ID or coverage count changes |

The final diff is reviewed against neighboring sound pages for density, canonical placement, unsupported generalization, duplication and scope. No old wire/domain statement is replaced: the new qualification separates client menu/description behavior from the existing wire mapping. Sources and archives remain unchanged.
