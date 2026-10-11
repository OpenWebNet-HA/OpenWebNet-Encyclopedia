# MyOpenCommunity Scenario and Condition History Review

This continuation starts at `c7b79c36963767982347eb025846fa13f9e50dc0` on `docs/myopencommunity-integration`, following the [Lighting and Automation review](myopencommunity-lighting-automation-history-review.md). It follows WHO 0 programming, scenario controls, condition evaluation and their executable consumers across the four preserved repositories. Earlier chat examples are context, not a coverage boundary. Sources and archives remain read-only.

## Bounded history coverage

The [history dispositions](myopencommunity-scenario-history-dispositions.tsv) retain 27,848 changed-file edges and every selected retained parent, including merges. Independent reconstruction verifies 55,696 endpoint tree identities and 10,711 nonempty repository/blob identities. The [component dispositions](myopencommunity-scenario-component-dispositions.tsv) bind 9,696 normalized variants to original trees, complete-file byte hashes, component hashes, assertion identities and comparison references.

| Repository | Selected paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 153 | 18,342 | 4,158 | 3,790 | 6,491 |
| libqtcommon | 17 | 1,557 | 622 | 600 | 453 |
| BtExperience | 202 | 7,929 | 2,611 | 2,366 | 3,749 |
| MyHomeSystemEmulator | 12 | 20 | 4 | 4 | 18 |

Discovery screened 32,992 retained source, Configuration and build blobs for scenario, scenevo/scenari, CEN/CEN+, Auxiliary and WHO-leading frame identifiers. Earlier/removed paths with the same discovered basename, generic device/status models, tests and consumers are included. This is candidate discovery, not proof of semantic coverage of every repository. Shared pre-extraction history is not independent corroboration.

| Review method | Variants | Scope |
| --- | ---: | --- |
| Full component comparison | 1,407 | Scenario library/test bodies, condition evaluator/tests, modern product Configuration/state models/tests, notifier, selected removed direct writers/condition/timer bodies and generic simulator scenario consumers |
| Declaration scope screen | 3,728 | Declarations, enums, Configuration, build and outside-function candidates; no full semantic verdict |
| Candidate scope screen | 3,432 | Other namespace, generic factory/UI and consumer candidates; no full semantic verdict |
| Legacy selector/presentation screen | 730 | Older constructors, selectors and presentation helpers outside the selected direct wire/state comparison |
| Presentation scope screen | 399 | Rendering, labels and navigation helpers |

There are 825 normalized component identities present at the pinned endpoints. The fully compared components contain 999 normalized assertion/check/row-call occurrences; another 377 belong to screened candidates and are identity inventory only. Each expression has a helper/macro ordinal and hash within its enclosing original body. Data rows require their consuming test and setup; signal counts do not establish unasserted payloads.

Normalization removes comments and blank indentation and redacts private fixtures. Complete-file hashes remain byte-exact, including non-UTF-8 history. Comparison views retain literals; token spacing is compacted for reading, not execution. The 31 `comparison_view_anchor` references reuse complete normalized token views. `comparison_component` identifies the previously encountered same-basename/name variant, not a Git parent; overloads can share a name. Actual parent edges remain explicit in the history ledger.

| Disposition | Changed-file edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 512 | 151 |
| Corroborates existing scoped documentation | 150 | 150 |
| Excluded with reason | 27,186 | 9,395 |

Intermediate/removed variants are excluded as current or deployed rules while retaining their historical comparisons. Whole-file inventory comprises 13,586 endpoint pairs and 1,059,749 normalized diff lines; it is not full whole-file semantic review. In particular, declaration screens and older selector/presentation screens are not complete review of every constructor, malformed-input path or Configuration file. This pass closes the selected direct wire/state and modern application condition/control lineage, not every UI history or repository.

The [helper dispositions](myopencommunity-scenario-helper-dispositions.tsv) add 51 retained-parent edges for scale conversion, local time-edit helpers and generic simulator Action/Message headers. Seven distinct scoped views were compared in full. Empty declaration views do not assert header semantics; original endpoint hashes and parent identities remain recorded. Pinned QML Start, enabled toggle, Save/Cancel controls and assertion helpers were read separately. Their historical UI variants remain screened rather than silently counted as full semantic review.

## Pinned source basis

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Scenario implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/scenario_device.cpp), [exact scenario assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_scenario_device.cpp), [Device assertion helper](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/device_tester.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | [Condition implementation](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scenevodevicescond.cpp), [condition assertions](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_scenevodevicescond.cpp), [scale conversion](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scaleconversion.cpp) |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Scenario models and Configuration](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/scenarioobjects.cpp), [application assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_scenario_objects.cpp), [notifier](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/scenariomodulesnotifier.cpp), [manual controls](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/Components/Scenarios/AdvancedScenario.qml), [Save/Cancel controls](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/SettingsAdvancedScenario.qml) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | [Generic scenario dispatch](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/bt_gen_dev.cpp), [action worker](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/genmsgworker.cpp), [XML serializer](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/gen_xmlserializer.cpp) |

Component IDs refer to the ledger, not protocol identifiers. Evidence priority is exact assertions, executable behavior, comments/meaningful identifiers, then labeled inference. No repository date is mapped to deployed Firmware.

## Programming state and address matching

Final ScenarioDevice writers and exact tests corroborate activation, start/stop recording, erase-all/erase-single and empty-dimension status-request forms. Scenario Plus writers remain WHO 25 and corroborate its existing canonical vocabulary. Assertions allowing scenario numbers `1..31` do not extend published F420 `1..16` or 3456 `1..20` capacities. Decoder `S0096` compares complete WHERE strings except for bare start `40`, which bypasses the address check. Bare stop `41` retains it. Parameterized start/stop use the first argument; unchecked extra arguments, absent frame-family guards and coercion do not extend valid grammar.

Lock always yields DIM_LOCK true and clears `is_unlocked`. Unlock yields DIM_LOCK false only when that cache was false. Start updates the unlock cache but forwards only DIM_START, with a programming pair and selected scenario or local sentinel `-1`. Stop forwards the false programming pair without updating the cache. Activation, erase, unavailable and memory-full cases fall through without a forwarded value. The header comment saying a DIM_START update implies unlocked is less precise than these executable transitions.

The startup test constructs a tester with DIM_LOCK but its final `checkSignals(1)` counts all valueReceived emissions. It does not assert a DIM_LOCK payload. DeviceTester filters by dimension only when obtaining result values; original decoder behavior establishes the separate programming payload and unlock suppression. This qualification prevents promoting a helper argument into a stronger assertion.

Product `ScenarioModule::valueReceived` (`S5684`) enters Editing for its own selected scenario only from Unlocked. A different selected scenario, including the sentinel, locks an Unlocked entry. Locked and Editing entries ignore further starts. Every stop returns an entry to Unlocked regardless of selected scenario; exact table-driven tests cover Locked/Unlocked/Editing with matching and different scenario numbers. Lock/unlock values directly select local state. `changeStatus` (`S5685`) emits programmingStopped only for Editing to Unlocked, not Editing to Locked. The notifier chooses the first configured Editing entry; that does not prove a globally exclusive hardware recorder.

[WHO 0](../../functional/who-0-scenarios/README.md#historical-touchscreen-behavior) gains the cache/address qualification and a compact local transition table. Its published operations, routing forms, session selectors and capacities remain unchanged.

## Conditions and automatic execution

The final DeviceCondition base initializes on the first managed predicate value without emitting. Unrelated values do not initialize it. Later false-to-true transitions emit; repeated true values do not, and false values rearm the edge. Auxiliary starts initialized and permits the first matching state to emit. A changed save requests state again: previously satisfied clears satisfied while retaining initialized, whereas previously unsatisfied clears initialized. An unchanged save does neither. Exact tests cover initialization, repeated events, inclusive bounds and saved-condition behavior; helper/setup context distinguishes wire bytes from local predicate operands.

Light predicates use local booleans. Coarse/fine dimmers use local inclusive bands; bare ON without a level substitutes `1`, not a measured percentage. Volume predicates use cached amplifier ON and inclusive volume limits; ON alone supplies no volume operand. Temperature predicates use converted tenths of the selected scale and inclusive ±10 around the threshold. Conversion helpers establish ±1.0 °C or ±1.0 °F application bands, not a universal thermostat tolerance. UI percentage ranges, condition editing bands and fixture counts are not physical capacities.

Advanced scenario consumers (`S5673..S5675`) select configured `<scen>` time/device children only with status `1`, local enabled/day values and one literal action. Scheduled controls select separate `<schedscen>` enable/start/stop/disable `<open>` strings, suppressed when presence converts to false. Modern parsers and their state/persistence consumers were fully compared; generic factory and older selector/Configuration candidates remain screened. Installed values are not copied into the provenance ledgers.

Automatic advanced execution requires enabled state and current weekday. With time present, Device edges do not invoke the action; the time event checks current Device satisfaction. Without time, the Device edge can start it. `AdvancedScenario::start` (`S5735`) bypasses all these gates, and the pinned QML Start button calls it directly. Enable changes local state and persists without a WHO 17 writer or automatic start. Disabling does not stop Device condition-cache updates. There is no asserted replay queue of events seen while disabled.

Days use Monday bit 0 through Sunday bit 6; both UI day 0 and Qt day 7 identify Sunday. Editable `gui_days` governs live gating before Save. Save copies the baseline and persists; Reset restores it. Time uses a local QTime timer, modulo one day, and rearms after timeout. Platform date/time attribute presence recalculates from the local clock without using payload values as a scheduling clock. Time Reset changes editable values but does not rearm immediately. Cancel pops the settings page; its comment says reset happens outside the page. No atomic rollback of timers and weekdays is inferred.

Action type and Command IDs choose descriptions, including CEN, CEN+ and Scenario Plus labels; sendFrame passes the configured literal unchanged. Those IDs are not WHAT and do not select WHO. Raw scheduled controls have no identified local scheduler or scene execution-state decoder. Nonempty commands drive button availability, not hardware capabilities. Local started/stopped/enabled/disabled signals follow dispatch, not ACK or observed effect; an empty ActionObject can still be followed by an advanced started notification.

[Execution Model](../../scenario-engine/execution-model.md#historical-touchscreen-condition-evaluation) gains precise save/initialization behavior, selected-scale and operand qualifications, automatic/manual control distinctions, local weekdays/timer behavior and literal-action/scheduled-control namespace boundaries. Existing MyHOME Suite unknowns remain distinct. WHO 17 and CEN tables are linked rather than duplicated.

## Historical corrections and simulator exclusions

Removed Qt3/Qt4 condition bodies include equality-only predicates, initial matching events, missing/reset satisfied-state guards, mixed status-list APIs and earlier temperature conversion mistakes. Retained shared libqtdevices commits [centralized initialization/edge handling](https://github.com/OpenWebNet-HA/libqtdevices/commit/b3581d88) and [the Auxiliary startup exception](https://github.com/OpenWebNet-HA/libqtdevices/commit/9765c64d) explicitly change implementation/tests. They do not establish physical generations. Older timer code uses repeated positive wrapping or singleShot alternatives; the pinned modulo expression also permits zero delay at exact equality. No inclusive next-day or missed-event guarantee is derived from those alternatives. Scale-conversion history also changes the Celsius sign boundary from `>1000` to `>=1000`; the pinned Fahrenheit helper retains `>1000`. Their different treatment of input `1000` is a converter corner case, not evidence of accepted wire values or a physical temperature-generation split.

BtExperience corrections [persist enable state](https://github.com/OpenWebNet-HA/BtExperience/commit/d96db1ce) and [restore weekday edits](https://github.com/OpenWebNet-HA/BtExperience/commit/d1824bf9) change local persistence/baseline handling. Earlier inverted hasStart/hasStop/hasEnable/hasDisable methods, removed direct action paths and notification signature changes are local revisions, not WHO 17 or device Firmware changes. Older forced-trigger implementations also bypass automatic gates; they do not impose a universal OpenWebNet manual-trigger policy.

The emulator's generic scenario map keys exact configured trigger text. Duplicate keys replace prior entries. The worker walks configured actions/messages and iterates from starting index through repeat index inclusively, rather than interpreting repeat as an independent count. CMD/MON/GUI channels and message delays belong to simulator dispatch. Message expansion substitutes `[index]` and inclusive random ranges, reseeding locally. Unchecked malformed tokens can stall expansion; they are not wire syntax or physical failure rules. ScenarioTest/Indesit fixture names, XML lists and generic dispatch do not establish F420 recording memory, transactionality or hardware scheduling. These findings are retained as exclusions rather than adding an unrelated emulator execution model to reader-facing protocol pages.

| Candidate | Disposition |
| --- | --- |
| API scenario range proves F420/3456 storage capacity | Excluded: assertions validate library inputs, not published device capacities |
| Bare start address bypass means all physical modules record together | Excluded: local cached-state acceptance only |
| START/STOP always emits an unlock value | Qualified: separate programming payload and cache behavior |
| Every “started” notification proves ACK or execution | Excluded: local signal after dispatch, including empty advanced action |
| Advanced enable or action Command IDs select WHO 17 | Excluded: local persisted flag or description metadata; literal frame controls namespace |
| Manual Start obeys automatic gates | Corrected scope: direct action dispatch bypasses those gates in this client |
| Saving always suppresses the next predicate event | Qualified: depends on previous satisfaction; unchanged save is a no-op |
| Bare dimmer ON establishes a measured percentage | Excluded: local fallback operand `1` |
| Condition bands define physical hysteresis or thermostat tolerance | Excluded: inclusive application predicates and selected-scale conversion |
| Cancel/Reset atomically restores live weekday/timer state | Excluded: live editable weekday gating, delayed timer rearm and external reset call boundary |
| Local timer establishes DST, timezone, restart or missed-event policy | Excluded: local QTime/modulo interval only |
| Simulator trigger/repeat/ACK behavior describes real scenario controllers | Excluded: generic simulator implementation and unchecked Configuration |
| Retained dates/revisions identify deployed Firmware generations | Excluded: no captures, device releases or deployment mapping |

Captures/hardware are still needed to establish physical bare 40/41 behavior, recording ownership and ordering across modules, availability/memory-full reports, actual stored-action capacity/order and target/Firmware applicability. Complete touchscreen runtime evidence is needed for timezone/DST, restart and missed-event recovery. The external OpenMsg stack is needed to settle malformed-frame classification. Older selector/UI history remains a separate semantic-review boundary, not evidence of repository exhaustion.

## Machine KB maintenance and validation

Two existing sections record scoped additions as candidates for later atomic extraction, retaining coverage status/count. Four retained claims refresh section digests; statements, sources, supporting blocks/indexes and context are unchanged. The corpus retains 7,448 claims and 1,223 chunks. No atomic claim or section/chunk identity is added or redesigned.

A targeted Qt 5 Core harness compiles 37 original method bodies and passes 45 comparisons: exact WHO 0 writers, full address equality/bare-start bypass, programming/unlock cache, product state transitions, predicate initialization/save/repeat edges, automatic versus manual gates, weekdays and conversion/time helpers. OpenMsg tokenization, transport writers, predicate device querying, signal sinks, action dispatch and object construction are controlled seams. It does not execute the complete archived suites, external OpenMsg parsing, actual sockets/timer events, complete QML consumers or hardware. This harness supports selected claims and is not the basis for history-coverage counts.

| Validation | Result |
| --- | --- |
| Independent history reconstruction | Pass: 27,848 edges, 55,696 endpoint tree identities, 10,711 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 9,696 tree/content/body identities, 1,376 normalized assertion/check/row-call identities; semantic coverage distinguished above |
| Bindings and helper closure | Pass: all component edge bindings, 7,632 comparison references, canonical destinations and 51 supplemental helper parent/hash bindings |
| Targeted original-body execution | Pass: 45 comparisons across 37 original bodies; controlled seams and execution limits above |
| Normal build / integrity check | Pass: deterministic artifacts, manifest, schemas, references, text hygiene, privacy and consistency |
| Machine-KB unit / schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact / canonical-source audits | Pass: 144 registered artifacts, all 25 fingerprints verified, five database integrity results `ok`, no source-audit failures; authorized privileged R2 helper used |
| Links / wire examples | Pass: 19 local/anchor targets and 18 public source links; WHO 0 forms checked against original writers and exact assertions |
| Style / Core Values | No objective failures; existing advisory style/identifier candidates retained |
| Epistemic / neighboring-page review | Protocol, product, Configuration and simulator scopes separated; published capacities and unresolved hardware behavior preserved |
| Complete diff / Machine-KB impact | Two canonical pages, four provenance records and six KB maintenance inputs/artifacts; four claim digests and two retrieval texts refreshed, identities/supporting context unchanged; no full-KB review flag |

The complete diff is reviewed for source immutability, privacy, unsupported generalization, duplicate placement, literal frames and neighboring-page consistency. This closes the bounded scenario/control-condition review, not all MyOpenCommunity extraction.
