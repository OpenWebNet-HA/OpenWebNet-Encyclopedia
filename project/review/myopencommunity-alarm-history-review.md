# MyOpenCommunity Alarm History Review

This continuation starts at `5aaeb5513e397b707e6b4e983d5364997ba218c8` on `docs/myopencommunity-integration`, following the [HVAC review](myopencommunity-hvac-history-review.md). It follows the retained `WHO 5` alarm library, tests, removed controllers and BtExperience Configuration/consumers across the four preserved repositories. Earlier chat examples are context, not a coverage boundary. Preserved archives and synced sources remain read-only.

## Bounded history coverage

The [history dispositions](myopencommunity-alarm-history-dispositions.tsv) bind 16,107 changed-file edges to every relevant retained parent, including merges. Independent reconstruction verifies the selected parent/path set, 32,214 endpoint tree identities and 6,458 nonempty repository/blob identities. The [component dispositions](myopencommunity-alarm-component-dispositions.tsv) bind 3,829 distinct normalized variants to actual source trees, byte-exact complete-file hashes, component hashes and comparison identities. The 237 assertion occurrences have macro/ordinal identities and normalized expression hashes, verified against their original enclosing bodies. Each inherits the component's scoped disposition.

| Repository | Selected paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 83 | 11,112 | 3,205 | 2,911 | 4,194 |
| libqtcommon | 2 | 207 | 207 | 202 | 78 |
| BtExperience | 112 | 4,788 | 1,735 | 1,614 | 2,186 |
| MyHomeSystemEmulator | No dedicated alarm lineage established | 0 in this boundary | 0 | 0 | 0 |

Discovery screened 32,992 retained source/Configuration/build blobs for alarm identifiers and WHO-leading frame literals, then closed over earlier/removed names, generic device/status/interpreter models, factory consumers, tests and build declarations. That screen defines candidates, not semantic coverage of every repository. Shared pre-extraction history is not independent corroboration. The libqtcommon paths contain client-writer/energy fixtures screened for namespace overlap, not an independent alarm implementation.

| Review method | Variants | Scope |
| --- | ---: | --- |
| Semantic component comparison | 817 | Selected serializers, decoders, exact assertions and alarm state/consumer transitions |
| Declaration / inline-state comparison | 90 | Core and product enums, signatures, inline state and helper bodies |
| Factory / decoder field comparison | 668 | Alarm-specific dispatch/address fields; unrelated generic cases are outside the verdict |
| Declaration reference comparison | 333 | Shared/removed alarm declarations and identifiers; not complete semantic review of every inline UI method |
| Consumer callback field comparison | 107 | Password submission, feedback, partialization and scenario callbacks; unrelated rendering omitted |
| Configuration field comparison | 31 | Named alarm fields, supplemented by selector closure below |
| Build field comparison | 287 | Inclusion/selection references; no independent wire evidence |
| Scope screen | 1,496 | Presentation, lifecycle, layout, settings and unrelated namespace fixtures |

There are 2,333 selected executable/field variants and 247 normalized identities present at pinned endpoints. Component normalization removes comments and blank indentation and redacts private fixture values; original complete-file hashes remain byte-exact, including historical non-UTF-8 files. Method discovery includes qualified names split over lines and earlier `items.cpp` alarm bodies. Comparison views preserve string literals while ignoring spacing/brace placement; field methods retain only alarm fields and adjacent context. The 1,091 `comparison_view_anchor` references reuse identical views, not necessarily identical complete bodies. The ordinary `comparison_component` points to the previously encountered variant of the same basename/component, not a retained Git parent. Actual parent edges remain explicit in the history ledger.

| Disposition | Changed-file edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 85 | 40 |
| Corroborates existing scoped documentation | 192 | 83 |
| Excluded with reason | 15,830 | 3,706 |

Intermediate/removed variants are excluded as current or deployed rules while retaining their historical comparison. A pinned identity can be shared with an earlier path/repository; this is normalized implementation reuse, not independent evidence. The 8,334 before/after blob pairs and 638,673 normalized whole-file diff lines are inventory/reuse data, not a claim of full whole-file semantic review. Thirty-three distinct meaningful alarm comments were checked against executable behavior; comment-only history is not claimed as exhaustively read.

### Configuration and simulator closure

The [Configuration dispositions](myopencommunity-alarm-configuration-dispositions.tsv) bind 219 distinct XML blob identities to byte-exact source hashes and selector-projection hashes. Eight distinct views compare old page `3`/item `23`/`24`, product system `6`, zone object `13000` then `13001`, auxiliary `13101` and scenario `13010` fields with executable consumers. Projections retain selected `id`, `cid`, `where`, `mon`, zone-number and scenario-zone fields, omitting names, credentials and unrelated Configuration. Two old XML files have encoding-declaration inconsistencies; a Latin-1 read permits inspecting the same original bytes, without asserting runtime acceptance or altering the archive. Sample counts, scenario sets and object IDs do not establish physical panel capabilities. Their values are not copied into public provenance.

A content screen of all 395 retained emulator source/Configuration/build blobs found no dedicated alarm serializer/decoder lineage. The built [generic device](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/bt_gen_dev.cpp) dispatches by exact-frame scenario map, selected by its [plugin project](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/bt_GEN_DEV_PGIN.pro). Configured responses are not independent panel evidence. This dispatch inspection and screen do not claim full semantic review of every simulator method.

## Pinned source basis

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Alarm implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/antintrusion_device.cpp), [alarm declarations](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/antintrusion_device.h), [exact assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_antintrusion_device.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Namespace-overlap fixture screen; no independent alarm claim |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Alarm Configuration and state consumers](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/antintrusionsystem.cpp), [product assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_antintrusion_object.cpp), [UI callbacks](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/Components/Antintrusion/AntintrusionSystem.qml) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | Generic dispatch/build boundary above; no new physical alarm model |

Component identifiers below refer to the provenance ledger, not protocol identifiers.

## Password commands and feedback

Exact library assertions (`A0080..A0084`) corroborate password-bearing `36` and `50`, the inverse eight-bit partialization mask and central request `*#5*0##`. The final bodies (`A0055..A0061`) retain the 6-second partialization-to-toggle delay and another 5 seconds to request state; other controls request state after 5 seconds. The armed cache changes optimistically. These are library scheduling/cache choices, not panel deadlines or password acceptance rules.

Pinned product `valueReceived` (`A2027`) initializes armed state on the first report. Subsequently, while waiting, a changed armed state emits acceptance; unchanged state emits refusal if no partialization reports remain pending. Partialization sets a counter to the number of configured zones and a false change flag. Each matching configured-zone report decrements the counter; any state change sets the flag. At zero, any change emits acceptance, otherwise refusal. It does not track distinct zones, compare the full requested mask, or correlate a report to a request. Repeated reports can finish the counter early. Late zone reports can finish this partialization check after timeout; the armed-state path requires the waiting flag.

Exact product tests (`A2055..A2059`, `A2069..A2072`) simulate changed/unchanged states and local gates. Their “right/wrong code” names are not evidence of panel password validation. The product's 10-second timer (`A2023`, `A2028`) can expire before the library's combined 11-second query. `requestPartialization` (`A2033`) also emits timeout immediately if `canPartialize` rejects the operation; [historical correction](https://github.com/OpenWebNet-HA/BtExperience/commit/d4016fa9e619de551070b5fafcd4c00b94a0b642) explicitly prevents a stuck local UI. A timeout is not necessarily an elapsed response deadline, much less a panel refusal.

`canPartialize` (`A2035`) requires a disarmed system and at least one changed local selection. The header's advice to call while active contradicts that executable guard and tests; behavior wins. Selected zone state is inverse to the library's partialized bit. Scenario `apply` (`A2016`) edits local selection; received active state (`A2011`) overwrites selection as well. This is a local alarm scenario, not a `WHO 0` wire command or proof of a panel restriction.

[Alarm Protocol](../../functional/who-5-alarm/protocol.md#historical-password-controls) qualifies the previous broad feedback sentence with the exact two checks, local gate/selection behavior and timeout distinction. No new panel compatibility or Firmware boundary is asserted.

## Event decoding and local alarm list

The final decoder (`A0053`, `A0062`) and exact tests (`A0085..A0093`) corroborate existing numeric filters: zone/intrusion `1..8`, tamper `0..15`, anti-panic `9`, technical/reset `1..15`. Armed/disarmed `8`/`9` have no WHERE check. `zoneNumber` does not check conversion success, so a malformed `#N` can coerce to zero; this is parser permissiveness, not canonical address grammar. The header's tamper/technical upper limit 16 loses to executable guards and assertions. Maintenance is ignored in an exact test, and other published battery/mains/silent values are not forwarded by this model; their protocol existence is unaffected.

Product `addAlarm`/`isDuplicateAlarm` (`A2029`, `A2031`) require configured zones for intrusion, configured auxiliaries for technical alarms and configured zones for tamper sources `0..8`; tamper `9..15` and anti-panic `9` need no configured source. Exact tests (`A2067`, `A2068`) reject otherwise valid unconfigured zone/auxiliary events from the displayed list. Deduplication uses alarm type and source number. `WHAT 13` removes the matching technical entry; a transition from disarmed to armed clears all local entries. Alarm timestamps use local receipt time (`A2029`, `A2017`), not a wire timestamp. No reset command is sent when the list clears.

[Alarm Addressing](../../functional/who-5-alarm/addressing.md#historical-event-validation) corrects the earlier implication that library and application accept the same sources, separating the decoder table from product Configuration filters. [Event connection](../../functional/who-5-alarm/protocol.md#event-connection) describes the scoped list behavior without presenting it as a complete panel event journal.

## Historical corrections and exclusions

Removed `impAnti`/`zonaAnti`, `items.cpp`, status/interpreter models and successive dedicated controllers use the same operative `WHO 5` command/status families, while revising cache initialization, zone matching, mask selection, insertion sequencing and local list clearing. Older acceptance of intrusion source `15`, changed armed-report WHERE matching and MANOMISSION-to-TAMPER naming are client revisions, not a demonstrated panel dialect. The stale `WHO 16` constructor/cache identifier is not the operative `WHO 5` decoder namespace.

Some older insertion sequences are ACK-gated and use different local delays. A legacy `openNakRx` invokes `openAckRx`, so either callback can advance the sequence. A “5 seconds” comment beside an executable 6-second delay is not a second timing specification. Older UI clearing can happen on submission or insertion independently of physical reset. These variations explain why ACK/local feedback/list clearing cannot establish physical success.

| Candidate | Disposition |
| --- | --- |
| Library commits or repository dates identify deployed Firmware generations | Excluded: no capture/release/device mapping |
| Header upper limit 16 extends decoder acceptance | Excluded: exact guards/assertions stop at 15 |
| “Right code” test names establish password format or authentication | Excluded: tests inject state reports; fixture credentials are not an acceptance rule |
| ACK or local accepted signal confirms the password and full mask | Excluded: client uses changed state/report counts; removed NACK can advance ACK continuation |
| A timeout proves panel refusal | Excluded: local gate can emit it immediately; timer can precede delayed query |
| `WHO 16` identifier proves a second alarm wire namespace | Excluded: stale model identifier versus operative `WHO 5` handlers |
| Earliest WHERE `1` / WHAT `11` or `2` branches establish deployed control syntax | Excluded: `Insert`/`DeInsert` prototypes only log and have empty behavior |
| Malformed `#N` accepted by numeric coercion establishes valid grammar | Excluded: unchecked conversion, not a supported address form |
| Fixture zone/scenario sets or auxiliary counts establish physical capacities | Excluded: local Configuration and serializer domains only |
| Local alarm clearing or scenario selection resets/programs the panel | Excluded: cache/selection transitions without that wire operation |
| Generic simulator replies corroborate alarm hardware | Excluded: configured exact-frame scripts |

Captures or hardware are still needed to establish panel/gateway/Firmware applicability of password controls and target `0`, password format/acceptance, ACK/NACK meaning during those controls, complete mask application, report timing and physical partialization restrictions. The absent external OpenMsg stack is needed to settle which malformed wire inputs reach the decoded helper. This closes a bounded alarm lineage, not repository exhaustion or a complete UI/physical-panel review.

## Machine KB maintenance and validation

Existing Event connection, Historical password controls and Historical event validation coverage sections retain their status/count and record scoped additions as candidates for later atomic extraction. Existing claim statements, source assignments and supporting blocks/indexes are preserved; eight retained claim records refresh their section digests. The corpus retains 7,448 claims and 1,223 chunks. No atomic claims or section/chunk identities are added or redesigned.

The targeted harness uses 34 original method bodies with Qt 5 Core and controlled token/output/signal/timer seams; 33 comparisons pass. It checks exact password frames/mask, delay scheduling, decoder filters/coercion, configured-source filtering, deduplication/reset/arming clear, selected/active state and feedback counting/timeout. It does not execute the complete archived Qt/product suites, external OpenMsg classification, actual sockets/event-loop timing or hardware.


| Validation | Result |
| --- | --- |
| Independent history reconstruction | Pass: 16,107 edges, 32,214 endpoint tree identities and 6,458 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 3,829 tree/content/body identities, 237 assertion identities, 4,248 comparison references and all edge bindings/destinations |
| Configuration closure | Eight selector views compared across 219 original XML identities; encoding inconsistencies retained as a runtime limitation |
| Targeted original-helper execution | Pass: 33 comparisons using 34 original bodies; controlled seams and execution limits above |
| Normal build and integrity check | Pass: deterministic artifacts, manifest, schemas, references, text hygiene, privacy and cross-artifact consistency |
| Machine-KB unit / schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact / canonical-source audits | Pass: 144 registered artifacts, all 25 fingerprints verified, five database integrity results `ok`, no source-audit failures; established privileged R2 helper used |
| Links / wire examples | Pass: 17 local/anchor targets and nine public links; changed wording checked against exact assertions and original serializers |
| Style / Core Values checks | No objective failures across 146 reader pages and 42 support pages; 127 pre-existing style candidates and 13 identifier candidates remain advisory |
| Epistemic / neighboring-page review | Client-scoped qualifiers; official vocabulary/ranges retained; Alarm and neighboring functional/address/session pages compared |
| Complete diff / Machine-KB impact | Two canonical pages, four provenance records and six maintenance inputs/artifacts; eight claim digests and three coverage reasons change; stable claim/chunk identities and source contexts; no full-KB review flag |

The complete diff is reviewed for unsupported generalization, duplicate placement, wire syntax, private fixture leakage and source immutability. The existing sections use compact tables and concise client notes. Device descriptions gain no unsupported compatibility or Firmware claims. Whitespace and staged changes are checked before commit, then the branch is pushed without merging. This closes the bounded alarm review, not the entire repository extraction.
