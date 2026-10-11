# MyOpenCommunity Auxiliary History Review

This WHO 9 continuation starts at `1d61c7847d4e7feab740002d895f9f79c4c29c68` on `docs/myopencommunity-integration`, following the [Scenario and Condition review](myopencommunity-scenario-history-review.md). It follows the auxiliary status receiver and condition consumers, including removed implementations, and checks the boundary with Alarm and sound-source uses of “Aux”. The four preserved repositories and retained histories remain read-only. Earlier chat examples are context, not a coverage boundary.

## Bounded history coverage

The [history dispositions](myopencommunity-auxiliary-history-dispositions.tsv) retain 11,664 changed-file edges and every selected retained parent, including merges. Independent reconstruction verifies 23,328 endpoint tree identities and 4,787 nonempty repository/blob identities. The [component dispositions](myopencommunity-auxiliary-component-dispositions.tsv) bind 884 normalized variants to original trees, complete-file byte hashes, component hashes, assertion identities and comparison references.

| Repository | Selected paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 75 | 8,203 | 2,688 | 2,469 | 3,122 |
| libqtcommon | 4 | 553 | 341 | 333 | 227 |
| BtExperience | 57 | 2,908 | 1,328 | 1,248 | 1,438 |
| MyHomeSystemEmulator | 0 | 0 | 0 | 0 | 0 |

Discovery screened 32,992 retained C++/header, XML, QML, JavaScript and build blobs for auxiliary identifiers and WHO-leading literal forms. Discovered basenames are closed over every earlier directory location; generic device, condition, Alarm, Configuration and sound consumers are included. A second literal-frame screen includes XML/text boundaries and finds no additional paths outside that index. The emulator's 395 screened blobs contain no dedicated WHO 9/Auxiliary implementation in this discovery boundary. Generic configured-message dispatch is covered by the prior Scenario review; absence of a dedicated class does not prove absence of every possible configured WHO 9 message.

The [numeric scope dispositions](myopencommunity-auxiliary-numeric-scope-dispositions.tsv) separately retain 407 original blob matches and byte hashes. Their 36 distinct context views were compared: numeric case/selector 9 also denotes Lighting levels, Alarm disarming, camera WHAT, local hardware/calendar fields and prototype condition categories. No additional dedicated WHO 9 decoder was identified. These are namespace-context screens, not whole-file semantic review. The scoped-view hash covers the original matching lines with their nearby context; it is distinct from the complete-file hash.

| Review method | Variants | Scope |
| --- | ---: | --- |
| Full component comparison | 123 | Auxiliary constructors, query/init/reset/decoders, exact auxiliary tests, Auxiliary condition/predicate/UI-value bodies and tests, shared condition initialization/save/edge handling, generic decoded-value forwarding and Alarm auxiliary-source parser |
| Prior semantic review reuse | 115 | Exact basename/name/body identities from the Scenario or Alarm component records; explicit prior IDs retained |
| Consumer field comparison | 251 | Selected Aux/frame candidates with neighboring lines, generic factories, Configuration consumers, other-namespace tests and UI |
| Audio/UI boundary screen | 240 | Sound-source namespace/delegate and presentation lines |
| Declaration scope screen | 155 | Aux-matching declarations, enums, XML, build fields and outside-function lines |

There are 76 normalized identities present at the pinned endpoints. The 123 newly compared full components contain 21 normalized assertion/check occurrences. Across all methods, 290 occurrences are retained as identity inventory; reuse and field-screen occurrences are not silently counted as new full semantic review. Exact assertion helpers were read separately: DeviceTester checks converted DIM_STATUS payloads, while checkCondition counts condSatisfied emissions and clears the spy after each frame.

Normalization removes comments and blank indentation and redacts private fixtures. Complete-file hashes remain byte-exact, including non-UTF-8 history. Comparison views retain literals. The 233 comparison-view anchors reuse identical scoped projections; the 115 prior semantic references reuse exact normalized bodies. Shared pre-extraction history is not independent corroboration. A comparison_component is a previously encountered same-basename/name variant, not necessarily a Git parent. Actual parent edges are explicit in the history ledger.

| Disposition | Changed-file edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 46 | 6 |
| Corroborates existing scoped documentation | 215 | 32 |
| Excluded with reason | 11,403 | 846 |

Whole-file inventory comprises 6,113 endpoint pairs and 571,277 normalized diff lines; it is not full whole-file semantic coverage. Intermediate variants remain excluded as current/deployed rules while retaining historical comparisons. In particular, field and declaration screens do not certify every Configuration value, generic factory, sound operation, UI lifecycle or malformed-input branch. This pass closes the selected auxiliary receiver/condition lineage and its namespace boundaries, not every repository or every consumer implementation.

## Pinned source basis

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Auxiliary implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.cpp), [API and local value identifier](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.h), [exact assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_media_device.cpp), [status serializer](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp), [request/forwarding delegates](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/device.cpp), [assertion helper](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/device_tester.h) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | [Auxiliary condition implementation](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scenevodevicescond.cpp), [condition assertions/helper](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_scenevodevicescond.cpp) |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Condition/action Configuration](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/scenarioobjects.cpp), [scenario assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_scenario_objects.cpp), [Alarm-source parser](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/antintrusionsystem.cpp), [sound-source consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/mediaobjects.cpp) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | No dedicated WHO 9 model identified in the scoped retained-content screen; generic scenario/message dispatch was reviewed separately |

Component IDs are review identities, not protocol identifiers. Evidence priority is exact assertions, executable behavior, comments/meaningful identifiers, then labeled inference. The generic status serializer also matches transport component `T0238`; its prior retained history remains in the [Transport review](myopencommunity-transport-history-review.md). The external OpenMsg acceptance grammar remains unavailable in these four sources.

## Binary status and address matching

AuxDevice constructs WHO `9` with the supplied address (`U0009`). Its private requestStatus calls the generic request delegate with an empty string (`U0010`), selecting the literal serializer `*#9*WHERE##`. init invokes that request (`U0011`). TestAuxDevice::sendRequestStatus (`U0024`) compares the emitted request exactly; receiveStatus (`U0025`) asserts true from `*9*1*WHERE##` and false from `*9*0*WHERE##`. Its fixture address `22` proves those assertions, not an address range or Automation A/PL grammar.

The final decoder (`U0012`) compares the complete configured address with whereFull, requires a normal command/event frame, maps WHAT 1/0 to boolean DIM_STATUS, and rejects other WHAT cases without a value. DIM_STATUS is a local enum whose header explicitly says its value does not matter; it is not a WHO 9 DIMENSION identifier. The generic constructor subscribes the receiver to WHO 9; parseFrame itself is not a standalone all-namespace validator. Unchecked WHAT parameters or external-parser coercions do not extend valid grammar.

The decoder has no previous-state suppression. device::manageFrame (`U0007`) forwards every nonempty decoded list, including repeats. The dedicated AuxDevice API provides status querying/receipt, with no named ON/OFF control methods. Generic inherited command/frame writers and literal RawDevice actions still exist; that API limitation neither prohibits WHO 9 control nor establishes a physical relay operation, command support or response flow.

[WHO 9 - Auxiliaries](../../functional/who-9-auxiliaries/README.md) gains a compact scoped request/receive table and these address/state qualifications. Its existing namespace and corpus limitations remain valid. No public address-domain, independent dimension catalogue, ACK/event ordering or hardware capability is invented.

## Condition and namespace boundaries

The final DeviceConditionAux starts the base condition initialized, selects the configured 0/1 predicate and creates AuxDevice with the supplied address. It consumes only the local DIM_STATUS boolean. The exact startup test (`U0056`) counts a first matching OFF report, suppresses a repeated match, resets satisfaction on ON, and fires on a later OFF. The other tests (`U0055`, `U0057..U0059`) cover startup and unchanged/changed save behavior. They corroborate the existing [Scenario Engine condition evaluation](../../scenario-engine/execution-model.md#historical-touchscreen-condition-evaluation), which remains the canonical location for those application rules.

BtExperience's Auxiliary condition selector delegates to that class. DeviceConditionObject temporarily disables initialization and enables it through its object lifecycle; this does not change wire namespace or establish guaranteed startup telemetry. ActionAux description IDs 109/110 label OFF/ON, but a configured action's literal frame controls its actual namespace. The exact advanced-scenario tests inject WHO 9 predicates while sending an independently configured action. These are application conditions/actions, not device-stored WHO 0 scenarios or proof of physical WHO 9 control.

parseAntintrusionAux (`U0677`) instead creates AntintrusionAlarmSource entries from numeric Configuration source IDs, attaching them to the WHO 5 alarm system. The prior Alarm review covers the technical-alarm decoder and source-number filters. Neither its numeric limits nor its older leading-prefix conversion (`U0859`) define WHO 9 addressing. The Auxiliaries page links to the canonical Alarm path and states the separation.

AuxPage/AuxSource/SourceAux and older sorgente_aux bodies are sound-source consumers. Their delegates and direct writers use WHO 16 or WHO 22, including next-track commands whose WHAT happens to be 9. Audio source IDs, UI enum values and Aux labels do not identify WHO 9. Those bodies remain namespace-boundary screens rather than a new complete sound-history review.

## Historical corrections and exclusions

The [AuxDevice rewrite](https://github.com/OpenWebNet-HA/libqtdevices/commit/eb53f45278d4472650a8cbfb29e1f63fe0f7137a) introduced the modern 0/1 decoder without an address guard. The [address-check correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/44a5d6fc63eb03c26f6bc9c00a798474b2da575b) adds exact complete-WHERE comparison. Actual retained-parent patches establish that direction; the comparison-view encounter order alone does not. This is a library bug correction, not a new routing grammar or deployed Firmware boundary.

Earlier aux_device variants compare integer addresses or canonical decimal strings, accept an integer WHAT through a local stat_var, suppress repeated equal values, and initialize/reset local state using 0 or sentinel -1. Old init calls an external OpenMsg::createReadDim with WHO/WHERE and no explicit dimension. That identifier alone does not prove a wire DIMENSION request or its output syntax. Temporary assertion/fatal stubs in old condition callbacks establish incomplete local implementations, not bus rejection rules.

The [Auxiliary startup correction](https://github.com/OpenWebNet-HA/libqtcommon/commit/475fb1f45022ea5f07db8b304651458aad9f5dbb) changes the Auxiliary constructor to start initialized and adds an exact first-matching-report test. The commit explains a client startup issue; it does not guarantee that a physical endpoint replies to the initialization query. Removed conditions also include equality-only and initially suppressed callbacks. These differences are application revisions, not proof of physical device generations.

| Candidate | Disposition |
| --- | --- |
| WHAT 0/1 proves control support or relay polarity on every auxiliary | Excluded: exact receive tests and generic writers do not establish physical target capabilities |
| Fixture `22` proves numeric range or A/PL addressing | Excluded: one configured/tested address only |
| WHO 5 technical-source limits define WHO 9 address range | Excluded: distinct namespace and consumer |
| Local DIM_STATUS defines a wire DIMENSION | Excluded: internal enum; tested reports are ordinary WHAT frames |
| Old createReadDim proves a dimension request | Excluded: external serializer output not available from these sources |
| Duplicate reports must be suppressed by the protocol | Qualified: historical receiver/cache and scenario predicate policies differ |
| First matching state must trigger every integration | Excluded: tested touchscreen condition policy only |
| Aux audio/UI labels imply WHO 9 | Excluded: executable sound delegates use WHO 16/22 |
| Address-bypass bug defines broadcast or routed behavior | Excluded: intermediate client defect corrected before the pinned endpoint |
| Historical revision dates establish deployed Firmware boundaries | Excluded: no deployment/version mapping |

Captures or hardware evidence are still needed for the physical WHO 9 address domain, supported controls and direction, collective/routed target support, other WHAT/DIMENSION values, initial-query replies, session/ACK/report ordering and device/Firmware applicability. External OpenMsg evidence is needed for malformed/parameterized-frame acceptance. There is no basis for claiming repository exhaustion.

## Machine KB maintenance and validation

The existing Corpus status section records the supported additions as candidates for later atomic extraction, preserving its coverage status and two existing claims. Two retained claim digests are refreshed; statements, sources, supporting blocks/indexes and context remain unchanged. The corpus retains 7,448 claims and 1,223 chunks. No atomic claim, section or chunk identity is added or redesigned.

A targeted Qt 5 Core harness compiles 13 original bodies and passes 29 comparisons covering status serialization/init, boolean decoding, exact address equality, nonmatching family/WHAT rejection, repeated-value forwarding and predicate/save/initialization edges. OpenMsg fields/classification, signal sinks, object construction and query dispatch are controlled seams. A routed-looking string verifies textual preservation/comparison, not physical route support. This does not run the complete archived suites, real transport, external parsing or hardware, and is not the basis for history coverage.

| Validation | Result |
| --- | --- |
| Independent history reconstruction | Pass: 11,664 edges, 23,328 endpoint tree identities and 4,787 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 884 original tree/content/body identities and 290 normalized assertion identities; semantic versus screened coverage distinguished above |
| Bindings and namespace screens | Pass: all edge bindings, 879 comparison references, 115 prior semantic references, canonical destinations and 407 numeric-scope byte/view hashes; status serializer matches prior transport body T0238 |
| Targeted original-body execution | Pass: 29 comparisons across 13 original bodies; controlled seams and limits above |
| Normal build / integrity check | Pass: deterministic artifacts, manifest, schemas, references, text hygiene, privacy and cross-artifact consistency |
| Machine-KB unit / schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact / canonical-source audits | Pass: 144 registered artifacts, all 25 fingerprints verified, five database integrity results `ok`, no audit failures; authorized privileged R2 helper used |
| Links / wire examples | Pass: 13 local/anchor targets and 15 public source links; WHO 9 forms checked against original writer/delegates and exact assertions |
| Style / Core Values | No objective failures; existing advisory style/identifier candidates retained |
| Epistemic / neighboring-page review | Binary state, receiver policy, scenario conditions and WHO 5/16/22 consumers remain separately scoped; address and hardware gaps preserved |
| Complete diff / Machine-KB impact | One canonical page, four provenance records and six KB maintenance inputs/artifacts; two claim digests and one retrieval text/qualification refresh, identities/supporting context unchanged; no full-KB review flag |

The complete diff is reviewed for source immutability, privacy, literal frame syntax, duplication, unsupported generalization and neighboring-page presentation. Sources, archives and unrelated device-description work remain unchanged. This closes the bounded auxiliary receiver/condition review, not all MyOpenCommunity extraction.
