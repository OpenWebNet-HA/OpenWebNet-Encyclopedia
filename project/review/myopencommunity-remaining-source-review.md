# MyOpenCommunity Remaining Source Review

This pass starts at `490d81ac0f2f55cb022c5b3fa8b046b8cc014cde` on `docs/myopencommunity-integration`. It completes the marker-negative deletion queue left by the [coverage audit](myopencommunity-coverage-audit.md), using the preserved Git histories and the two earlier reviews. Conversation examples are context, not a coverage boundary.

## Bounded coverage

The [remaining-source dispositions](myopencommunity-remaining-dispositions.tsv) account for all 469 previously unresolved deletion edges, representing 456 distinct byte-exact Git blobs. Each row records repository, deletion commit, resolved parent commit, original path, Git blob, SHA-256, scope, review method, semantic basis and disposition. The parent/path resolves to the recorded blob; both hashes were checked. Identical blobs share a semantic review, with every deletion edge retained separately.

| Repository | Deletion edges reviewed |
| --- | ---: |
| libqtdevices | 319 |
| libqtcommon | 9 |
| BtExperience | 141 |
| MyHomeSystemEmulator | 0 remaining in this queue |

| Disposition | Edges | Distinct blobs |
| --- | ---: | ---: |
| Incorporated | 1 | 1 |
| Corroborates existing scoped documentation | 83 | 82 |
| Excluded with semantic reason | 385 | 373 |

The [history dispositions](myopencommunity-history-dispositions.tsv) now retain 689 edges with no `unresolved-boundary` rows. Its earlier 220 dispositions are unchanged. A canonical-page destination indicates the relevant feature, not that every local property deserves reader-facing documentation.

C++ declarations, inline methods, JavaScript and QML were read for behavior and delegation, including handlers, bounds, state changes and timers. Configuration trees were inspected through every element/attribute and distinct field, collapsing repeated numbered item names; private/local setup values were suppressed. XML fixtures were compared with their configuration, skin and font consumers. Vendor Qt/QWS files were excluded through their input/output boundary and method inventory: touchscreen events, calibration and `mouseChanged` are local pointer handling. This is not a correctness audit of every vendor calibration expression. Comments and names alone were not promoted to protocol rules; absence of search markers was not used as exclusion evidence.

## Volume conversion evidence

Added [Local volume and display scales](../../functional/who-22-sound-diffusion/README.md#local-volume-and-display-scales). This extends historical application notes; it corrects no published volume domain or existing frame example.

The [original conversion helpers](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/generic_functions.cpp#L511) define `localVolumeToAmplifier`, `scsToLocalVolume` and `scsToGraphicalVolume` at lines 511..556. Local settings use `0..8`; amplifier volume uses `0..31`. Local conversions round to the nearest integer, while the `LAYOUT_TS_10` icon conversion truncates. The alternative TS3.5 icon branch uses nine explicit bands rather than the same rounding formula.

The [local amplifier caller](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/sounddiffusionpage.cpp) initializes its amplifier level through the forward helper and converts received/changed levels back to the local audio setting. The [audio state machine](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/ts_10/audiostatemachine.cpp) asserts the local `0..8` range in `changeVolumePath`. The [amplifier banner](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/bann_amplifiers.cpp) and [power-amplifier banner](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/poweramplifier.cpp) select icons from reported volume using the graphical helper.

All three original function bodies were compiled unchanged with Qt5 `qRound`, once for each layout branch. Each build passed 86 comparisons: all nine local values and round trips, all 32 amplifier values through local and graphical conversions, and invalid amplifier inputs `-1` and `32`. These 172 comparisons verify the extracted helpers, not the complete legacy application or suite. No bound is inferred for arbitrary inputs to the unchecked forward helper. No physical loudness calibration or Firmware applicability follows from a build-layout macro.

## Corroboration and exclusions

| Material reviewed | Disposition and evidence boundary |
| --- | --- |
| Device declarations and configuration factories | Corroborate class selection and delegated APIs already covered in Configuration and functional pages; item IDs are not `WHO` numbers |
| Thermal plant/probe, lighting, scenario, sound, energy and video configuration fixtures | Corroborate configuration inputs and dispatch; sample cardinalities, defaults and creator/XML versions do not establish physical capacities or Firmware support |
| Bound energy overview/detail/graph screens | Delegate consumption/currency choice, graph periods and visibility-driven polling to the reviewed EnergyData model; no new wire dimensions |
| Energy mockups | Literal wattage/energy/date samples, `120` or `180` minute forcing text and `30` day self-test text lack device bindings; exclude as duration, limit or metering evidence |
| Graph arithmetic | Goal scaling, colour bands, fixed maxima and `cumulativeValue / 10` average are local presentation; exclude as device thresholds or measurement formulas |
| Lighting and thermal date/time controls | Local editing, fixed-timing selection, year wrapping and delegated `apply()` calls do not independently define wire fields or hardware ranges |
| Alarm timestamps, messages and security controls | Current local timestamps, dummy popup dates, character counters, keypad limits, passwords and screen locks do not establish panel time, message capacity or gateway authentication |
| Older BTouch radio widget | `setRDS` truncates its label to eight characters, but no caller was found at its deletion parent; exclude from `WHO 22` payload-length claims |
| Media, UPnP and radio screens | File browsing, pagination and subscription lifecycle delegate to reviewed implementations; playlists, favourites and labels add no wire rule |
| Qt model assertions and filtering | Require initialized local models and validate UI ranges; not bus address matching, protocol acceptance or Physical Device validation |
| TCP examples, RSS/Atom, browser, weather and vendor pointer drivers | Separate application/input/output boundaries; no additional OpenWebNet knowledge |
| Hardware storage, audio routes, timers, screen savers and animations | Local persistence, audio/display policy and rendering; no protocol deadlines or device support inferred |

These exclusions supplement the per-source reasons in the ledger. No raw configuration, host address, credential, personal fixture content or copied licensed implementation is committed.

## Remaining questions and coverage limits

The bounded deletion queue is closed. The repositories are not declared exhausted: intermediate revisions between pinned and terminal-deleted variants still need semantic comparison, and complete legacy builds require dependencies not provided by these archives. Helper checks do not settle full Qt3/Qt4 integration behavior.

Captures or hardware/product evidence remain necessary for physical volume calibration and Firmware applicability, StopGo address discrepancies, BACnet mappings/scales, PIC request compatibility, F520 reply-channel behavior and simulator timing accuracy. Earlier reviews retain the competing interpretations and product-specific limits. A UI label or fixture cannot close those questions.

## Machine KB maintenance and validation

The existing identity, retrieval chunk and coverage mechanisms record one added historical-volume section, with new atomic claims deferred to subsequent work. Ten affected retained claims were compared against exact supporting blocks and materialized meaning; only their prepared-section digest changes. The corpus retains 7,448 claims and now has 1,223 chunks. There is no Machine-KB redesign or new atomic-claim extraction.

| Validation | Result |
| --- | --- |
| Source dispositions | 469 edges / 456 distinct blobs verified; all 220 earlier dispositions unchanged; canonical destinations resolve |
| Reader and neighboring pages | Sound Diffusion and Sound System reviewed; scoped addition matches existing historical notes and reference tables |
| Frame examples | No added frames; existing examples on the changed reader page remain byte-for-byte unchanged and retain their documented families/scopes |
| Local documentation links and heading anchors | 34 checked, all resolve |
| Public provenance links | 41 checked, all HTTP 200 |
| Original volume helpers | 172 comparisons PASS across both layout branches |
| Build and `check.py` | PASS: deterministic artifacts, freshness, schemas, consistency, references, text hygiene and privacy |
| Machine-KB unit tests | 59 PASS after correcting three stale fixed-count expectations for the added section/chunk; all integrity assertions retained |
| Schema tests | 8 PASS |
| ESG | 146 human pages, 37 support pages; 0 objective failures, 127 advisory candidates |
| ECV | 0 objective failures; 13 existing identifier candidates unchanged |
| Epistemic drift | Changed-page candidates reviewed; repeated ranges belong to distinct contexts, existing MH200N observation remains Device-scoped |
| Artifact manifest | PASS, 144 artifacts |
| Canonical-source audit | PASS using the authorized R2 helper: 25 verified fingerprints, 5 database integrity results `ok`, 0 failures |
| Change impact and complete diff | 105 affected claims, 17 chunks, 12 references; identity-triggered full review completed; retained claim statements/scopes unchanged |
| Whitespace diff | PASS |

Generated changes consist of one added corpus section/chunk, its identity/lifecycle/coverage records, ten reviewed digest updates and the deterministic manifest. The changed section's exact supporting blocks and materialized retained statements are unchanged. The full legacy suites were not executed.
