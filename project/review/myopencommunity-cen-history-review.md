# MyOpenCommunity CEN and Transversal History Review

This continuation starts at `3efe8ea990ba5ea2781c9e50a2fbcd748bffdf0c` on `docs/myopencommunity-integration`, following the [Auxiliary review](myopencommunity-auxiliary-history-review.md). It reviews CEN/CEN+ configured actions, WHO 25 contact receipt and ScenarioPlus writers/controllers across the four preserved repositories and retained histories. Earlier chat examples are context, not a coverage boundary. Archives and synced sources remain read-only.

## Bounded history coverage

The [history dispositions](myopencommunity-cen-history-dispositions.tsv) bind 10,913 changed-file edges to every selected retained parent, including merges. Independent reconstruction verifies 21,826 endpoint tree identities and 3,681 nonempty repository/blob identities. The [component dispositions](myopencommunity-cen-component-dispositions.tsv) bind 339 normalized variants to actual source trees, byte-exact complete-file hashes, component hashes, assertion identities and comparison references.

| Repository | Selected paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 76 | 7,855 | 2,079 | 1,913 | 2,475 |
| libqtcommon | 14 | 989 | 380 | 368 | 266 |
| BtExperience | 76 | 2,065 | 823 | 774 | 936 |
| MyHomeSystemEmulator | 3 | 4 | 3 | 3 | 4 |

Discovery screened 32,992 retained C++/header, XML, QML, JavaScript and build blobs for CEN, ScenarioPlus, contact identifiers and WHO-leading literal forms. Discovered basenames are closed over earlier directory locations. Broad filename discovery also selects generic scenario and thermal Central files; those names are candidates, not evidence of a CEN implementation. The emulator's 395 screened blobs have no dedicated matching CEN/WHO 25 implementation; its three named-only scenario paths establish no new wire rule. Generic configured-message dispatch remains covered by the [Scenario review](myopencommunity-scenario-history-review.md), not evidence that the emulator models a physical CEN device.

The [numeric scope dispositions](myopencommunity-cen-numeric-scope-dispositions.tsv) separately retain 251 original blob matches and byte hashes. Their 43 distinct context views were compared for literal WHO 15/25 forms, selectors and numeric namespace construction; no additional path lies outside the history index. WHO 4 external-temperature dimensions, WHO 22 fields, duplicate-queue fixtures and XML duration values also contain 15/25 and are excluded as CEN wire evidence. These are context screens, not whole-file semantic review. Secondary views use UTF-8 replacement decoding where necessary; the complete source hashes remain byte-exact, and those views supply no new wire rule.

| Review method | Variants | Scope |
| --- | ---: | --- |
| Full component comparison | 170 | Contact constructors/query/init/decoders and exact tests; contact display consumers; ScenarioPlus/PPTSce writers, constructors and press/repeat/release callbacks; relevant complete legacy factories/loaders; modern contact selector and action description maps |
| Prior semantic review reuse | 15 | Exact basename/name/body identities from Scenario, Lighting/Automation or Auxiliary records; explicit prior component IDs retained |
| Consumer field comparison | 94 | Selected matching fields with neighboring lines in generic constructors, test registration, old scheduled constructors, other namespaces and UI |
| Declaration scope screen | 60 | Matching declarations, constants, XML fields/comments, enums, images and build fields |

There are 40 normalized identities present at the pinned endpoints. The 170 fully compared variants contain 44 normalized assertion/check occurrences. Across all methods, 88 occurrences are retained as identity inventory; reused and screened occurrences are not silently counted as newly reviewed assertions. The DeviceTester conversion and signal-count helper were already independently read in the Lighting/Automation and Auxiliary reviews; they do not assert unprovided parameters, routing or physical effects.

Normalization removes comments and blank indentation and redacts private fixtures. Original complete-file hashes retain all bytes, including historical non-UTF-8 files. The 74 comparison-view anchors reuse identical scoped projections; 15 prior references reuse exact semantic bodies. Shared history is not independent corroboration. A comparison_component is a previously encountered same-basename/name variant, not necessarily a Git parent. Actual parent edges are explicit in the history ledger.

| Disposition | Changed-file edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 73 | 11 |
| Corroborates existing scoped documentation | 284 | 20 |
| Excluded with reason | 10,556 | 308 |

Whole-file inventory comprises 4,722 endpoint pairs and 492,265 normalized diff lines; it is not whole-file semantic coverage. The selected functional bodies, tests and direct consumers have a bounded disposition; screens do not certify every generic factory, XML value, UI lifecycle, malformed-input branch or comment-only change. Earlier controller behavior is incorporated explicitly as historical application behavior, despite being absent at the TS10 endpoint. Other intermediate variants remain excluded as current/deployed rules. This is not repository exhaustion.

## Source basis and reused dispatch evidence

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Contact implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/automation_device.cpp), [contact API/local value](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/automation_device.h), [exact contact assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_automation_device.cpp), [ScenarioPlus writers](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/scenario_device.cpp), [generic delegates](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/device.cpp), [frame constructors](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp) |
| libqtdevices | `20b67275c780d5d0d4643ef446eabe6ad28877e5` | [Earlier ScenarioPlus controller](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/bann_scenario.cpp), [scenario factory](https://github.com/OpenWebNet-HA/libqtdevices/blob/20b67275c780d5d0d4643ef446eabe6ad28877e5/scenario.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Shared historical tests and scenario consumers; no independently established CEN dialect |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Contact selector and state consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/automationobjects.cpp), [scenario parsers/dispatch/labels](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/scenarioobjects.cpp), [object factory](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/btobjectsplugin.cpp) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | No dedicated model identified within the content/namespace screen; generic dispatch separately reviewed |

Component IDs are review identities, not protocol identifiers. Evidence priority is exact assertions, executable behavior, comments/meaningful identifiers, then labeled inference. Pinned dispatch bodies were re-read and matched to prior Scenario identities `S5674` (scheduled parser), `S5687..S5690` (four scheduled controls), `S5695` (action construction) and `S5696` (literal send). The corresponding generic status/command serializers remain in the Transport review; no external OpenMsg acceptance grammar is recovered here.

## CEN and CEN+ configured actions

The older factory (`C0035` and its compared variants) selects configured scheduled action strings. Earlier branches construct `*15*WHAT*WHERE##` from separate fields; later branches read a literal `open` frame gated by presence/value. Modern parseScheduledScenario and its four controls preserve the selected literal through RawDevice, with no automatic button-phase sequence.

The retained Configuration fixtures associate independent WHO 15 button frames with enable, disable, start and stop. Other fixtures reuse the same button frame for different labels. These are configured meanings, not a universal WHO 15 table in which buttons 1/2/3/4 mean scenario management. The [CEN action connection](../../functional/who-15-cen/README.md#action-connection) gains this concise qualification; the [Scenario Engine](../../scenario-engine/execution-model.md#historical-touchscreen-condition-evaluation) remains canonical for dispatch and local notifications.

ActionObject::buildDescriptionMap (`C0329`, earlier `C0333`/`C0336`) assigns CEN labels to IDs 94..97, CEN+ labels to 98..101 and ScenarioPlus labels to 102..106. Those are description-map keys; ActionObject stores the supplied literal and sendFrame sends it unchanged. They are not WHAT values. The CEN+ “Start pressure” label is not an independently established immediate-press wire event: the published WHAT 22 definition remains start of extended pressure. This label does not override the published short/long event sequence or timing.

The [CEN+ action/event section](../../functional/who-25-transversal/cen-plus.md#action-and-event-connections) gains the metadata/literal distinction. No dedicated retained CEN/CEN+ receiver or rotary generator was identified in this discovery boundary. Absence of such a class neither disproves generic literal support nor proves a new dialect. Configuration comments corroborate the WHO 15/25 distinction and the CEN+ `2` prefix, but their broader CEN address hints do not supersede the published address table.

## ScenarioPlus writers and controller

The pinned ScenarioPlusDevice uses WHO 25 with the supplied address and five writers (`C0023..C0028`). Its macro values establish the already documented 11..15 family, independent of CEN+ 21..28. The [step correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/34da414f84b15a18964e134b7496ccb2db81ecf4) changes increase/decrease from `#0#1` to `#0#5`. Actual retained-parent patches establish that direction. The commit compares the step with fine dimmers; it does not establish the physical ScenarioPlus step unit, full accepted range or a deployed Firmware boundary.

The earlier controller (`C0014..C0018`) connects press to increase/decrease and release to stop. The first press sends immediately and starts the 1000-ms timer; another press while that timer is active does not send again. Timer callbacks repeat the selected command. Stop cancels each active timer and sends stop for each canceled direction. Unexpected timer IDs and simultaneous direction timers are local callback behavior, not protocol event classification. This controller is absent at the TS10 endpoint and is documented as earlier application behavior.

The pinned ScenarioPlusDevice has no dedicated parseFrame override or scenario-state cache; generic parseFrame defaults to false. Writer calls do not confirm physical execution/state. The [WHO 25 historical controls](../../functional/who-25-transversal/README.md#historical-scenarioplus-controls) gain the timing/feedback qualifications without duplicating the frame table. No dedicated exact ScenarioPlus writer assertion was found; the evidence is executable writers plus their constants and delegates, not the WHO 0 tests in the same files.

Legacy factories sometimes concatenate a separate `what` field, `*`, and WHERE before constructing the ScenarioPlus controller. This application assembly is not sufficient evidence for a valid composite address or a new frame grammar. BtExperience's retained ID/quick-link entries for ScenarioPlus also do not prove an active factory case: its pinned object-factory switch does not construct a dedicated ScenarioPlus object. Neither residue establishes device capability.

## Contact receipt and product state

PPTStatDevice uses WHO 25 with the supplied address (`C0006`); init requests status (`C0007..C0008`). The exact request assertion (`C0032`) expects `*#25*10##`. The receive assertions (`C0033`) separately establish true for `31#0` and `31#1`, and false for `32#0` and `32#1`. Their fixture address is one tested address, not an exhaustive domain. The incomplete `*25*10##` fixture produces no value; it is not a complete invalid-frame grammar test.

The final decoder (`C0009`) compares where.toInt with the decoded numeric WHERE, maps 31/32 to one local boolean and does not suppress equal repeats. Generic manageFrame forwards every nonempty list (exact Auxiliary reuse). The namespace subscription is upstream; parseFrame alone is not an all-namespace validator. The decoder does not preserve parameter context or explicitly guard the frame family. Acceptance permissiveness and unavailable external-parser coercions do not extend valid syntax. DIM_STATUS is a local value identifier, not a wire DIMENSION.

The [polarity correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/abd28f2e190be5f46e0deaff12feb97fdba2a633) changes both implementation and four exact expectations from the reversed local boolean to 31=true/32=false. Other retained variants change frame-family guards and move namespace filtering into common infrastructure. These are library revisions, not proof of a physical open/closed meaning changing by Firmware generation. Older skins swap image names/content; presentation identifiers do not establish contact or IR polarity.

BtExperience's factory maps Automation contact entries into parseAutomation2, whose contact selector creates PPTStatDevice with the unchanged configured WHERE (`C0321`). Its contact consumer starts active=false (`C0322`) and emits activeChanged only when the boolean changes (`C0324`). First false and repeated equal reports therefore do not emit a change notification; first true does. Older contact banners instead redraw on received values. Neither the initial display nor notification policy guarantees a physical reading or redefines a bus event.

[Dry Contact and IR](../../functional/who-25-transversal/dry-contact-ir.md#historical-contact-interpretation) narrows the former `31#x`/`32#x` wording to the tested #0/#1 forms and gains the local-state, address and selector qualifications. Its published WHAT/parameter/address tables and separate IR detection meaning remain intact.

## Exclusions and unresolved evidence

| Candidate | Disposition |
| --- | --- |
| CEN button numbers universally mean enable/disable/start/stop | Excluded: meanings are assigned by configured scenario actions |
| CEN+ description IDs 98..101 are wire WHAT or an immediate-press event | Excluded: label keys; literal action controls the frame |
| ScenarioPlus one-second repeat is mandatory CEN+ timing | Excluded: earlier application timer, different WHAT family |
| ScenarioPlus #5 specifies a universal step unit/range | Unresolved: writer/correction does not establish device interpretation |
| Contact tests establish arbitrary WHAT parameters | Corrected: only #0 and #1 are asserted |
| Numeric contact matching establishes normalization/routing support | Excluded: client integer comparison and unavailable parser behavior |
| Contact DIM_STATUS is a wire DIMENSION | Excluded: internal boolean value identifier |
| Initial inactive display or change signal confirms physical state | Excluded: local initialization/notification policy |
| Reversed old boolean/images identify physical Firmware generations | Excluded: library/test/presentation corrections without deployment mapping |
| Old composite factory strings or sample WHERE values define address domains | Excluded: assembly/fixtures without exact validity or hardware evidence |
| Retained ScenarioPlus IDs prove a dedicated BtExperience object at TS10 | Excluded: metadata residue without a corresponding factory case |
| Shared WHO 25 implies ZigBee binding, CEN+, contact and ScenarioPlus share grammar | Excluded: distinct interface/family contexts; no new binding model found here |

Captures or hardware are still needed for ScenarioPlus step units/ranges, address domain and Device/Firmware applicability; contact routed/collective support, initial-query response and ACK/report ordering; and physical CEN/CEN+ generation/timing variations. The external OpenMsg implementation is needed for parameter/malformed-frame acceptance. No rotary or ZigBee binding claim is added from this repository evidence. Generic UI/Configuration history outside the explicitly compared bodies remains screened, not exhausted.

## Machine KB maintenance and validation

Four existing sections record these scoped additions as candidates for later atomic extraction, retaining coverage status/count. Fifty retained claim digests are refreshed, including parent sections; statements, sources, supporting blocks/indexes and context are unchanged. The corpus retains 7,448 claims and 1,223 chunks. No atomic claim, section or chunk identity is added or redesigned.

A targeted Qt 5 Core harness compiles 22 original bodies and passes 21 comparisons covering contact queries/decoding/repeats, contact initialization/change notifications, five ScenarioPlus writers, press/repeat/release and timer cancellation. Parser fields, output/delegate dispatch, signal sinks, construction and timer scheduling are controlled seams. Parameter preservation is established by original exact tests, not this seam. The harness does not execute the complete archived suites, OpenMsg parsing, transport, real event-loop timing or hardware; it is not the basis for retained-history coverage.

| Validation | Result |
| --- | --- |
| Independent history reconstruction | Pass: 10,913 edges, 21,826 endpoint tree identities and 3,681 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 339 original tree/content/body identities and 88 normalized assertion identities; semantic and screened coverage distinguished above |
| Bindings and scope | Pass: all history bindings, component destinations/comparison references, 15 prior semantic references, seven pinned dispatch reuses and 251 numeric byte/view records |
| Targeted original-body execution | Pass: 21 comparisons across 22 original bodies; constants match original sources; controlled seams and limits above |
| Normal build / integrity check | Pass: deterministic artifacts, freshness, manifest, schemas, references, text hygiene, privacy and cross-artifact consistency |
| Machine-KB unit / schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact / canonical-source audits | Pass: 144 registered artifacts, all 25 fingerprints verified, five database integrity results `ok`, no audit failures; authorized privileged R2 helper used |
| Links / wire examples | Pass: 29 local/anchor targets and 13 public source links; contact forms checked against exact assertions, ScenarioPlus forms against original constants/writers/delegates |
| Style / Core Values | No objective failures; existing advisory identifier/style candidates retained |
| Epistemic / neighboring-page review | CEN, CEN+, ScenarioPlus, contact, IR and ZigBee scopes separated; published ranges/timing unchanged; remaining hardware/parser questions retained |
| Complete diff / Machine-KB impact | Four canonical pages, four provenance records and six KB maintenance inputs/artifacts; 50 claim digests, four retrieval texts and two qualification-cue refreshes; identities/supporting context unchanged; no full-KB review flag |

The first integrity-check attempt overlapped the privacy suite's temporary fixture creation/removal and encountered a removed test file. The complete unchanged integrity check passes when rerun after the suite finishes. No validator or fixture was bypassed or changed.

The complete diff and staged changes are reviewed for literal syntax, duplicate placement, unsupported generalization, privacy, source immutability and presentation alongside WHO 0, WHO 2, CEN/CEN+, Dry Contact/IR, ZigBee Binding and Scenario Engine. Sources, archives and unrelated device-description work remain unchanged. This closes the bounded CEN/transversal client review, not all MyOpenCommunity extraction.
