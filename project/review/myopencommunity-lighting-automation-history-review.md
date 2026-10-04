# MyOpenCommunity Lighting and Automation History Review

This continuation starts at `df4387d8497c523579f477198f451734aebbbcbc` on `docs/myopencommunity-integration`, following the [Alarm review](myopencommunity-alarm-history-review.md). It follows the retained `WHO 1` / `WHO 2` serializers, decoders, exact tests, state models and relevant Configuration consumers across the four preserved repositories. Earlier chat examples are context, not a coverage boundary. Archives and synced sources remain read-only.

## Bounded history coverage

The [history dispositions](myopencommunity-lighting-automation-history-dispositions.tsv) bind 23,061 changed-file edges to every relevant retained parent, including merges. Independent reconstruction verifies 46,122 endpoint tree identities and 8,809 nonempty repository/blob identities. The [component dispositions](myopencommunity-lighting-automation-component-dispositions.tsv) bind 6,666 distinct normalized variants to actual source trees, byte-exact complete-file hashes, component hashes and comparison identities.

| Repository | Selected paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 130 | 16,283 | 3,769 | 3,435 | 5,792 |
| libqtcommon | 16 | 1,633 | 556 | 539 | 499 |
| BtExperience | 159 | 5,084 | 1,883 | 1,746 | 2,460 |
| MyHomeSystemEmulator | 30 | 61 | 8 | 8 | 58 |

Discovery screened 32,992 retained source/Configuration/build blobs for Lighting, dimmer, Automation, pull, contact, F411/F422 identifiers and WHO-leading frame literals. Earlier/removed names, generic device/status/interpreter models, tests and consumer references are included. That screen defines candidates, not semantic coverage of every repository. Shared pre-extraction history is not independent corroboration; libqtcommon retains shared tests and namespace-overlap fixtures, not a separately established Lighting dialect.

| Review method | Variants | Scope |
| --- | ---: | --- |
| Full core/product component comparison | 1,423 | Library Lighting/Automation/pull bodies, exact tests, product models and declarations/inline state |
| Full direct wire/state comparison | 585 | Removed direct writers/decoders, selected controller transitions, F411/F422 models/serializers and declarations |
| Pinned complete callback comparison | 4 | Safe Up/Down and Open/Close controls and their delegates |
| Automated field/scope screen | 4,654 | Generic factory/UI/Configuration/build and unrelated namespace candidates; no complete semantic verdict |

There are 2,012 fully compared component/callback variants and 651 normalized identities present at pinned endpoints. The 1,134 assertion/check-call occurrences in fully compared components have macro/helper-call ordinals and normalized expression hashes verified against original enclosing bodies. Another 606 occurrences belong to screened candidates and are identity inventory, not asserted semantic coverage. Helper arguments alone need their enclosing setup and implementation; test names, empty overrides and signal counts do not establish unasserted payloads.

Normalization removes comments and blank indentation and redacts private fixtures; original complete-file hashes remain byte-exact, including historical non-UTF-8 files. Qualified names split over lines and free functions are recognized. `comparison_component` points to the previously encountered same-basename/component variant, not a Git parent; overloads can share that name. Actual parent edges remain explicit in the history ledger. The 1,982 `comparison_view_anchor` references identify literal-preserving comparison-view reuse, not necessarily complete-body equivalence or manual review. Their field projections can omit unrelated behavior.

| Disposition | Changed-file edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 426 | 104 |
| Corroborates existing scoped documentation | 665 | 271 |
| Excluded with reason | 21,970 | 6,291 |

Intermediate/removed variants are excluded as current or deployed rules while retaining their historical comparisons. Whole-file inventory comprises 11,071 endpoint pairs and 919,548 normalized diff lines; this is not full whole-file semantic review. The 4,654 screened variants include older UI-only cache/rendering/factory branches that were not all manually compared. This bounded review closes the selected core/product and direct wire/state lineage, not every historical UI, malformed-input path, comment-only change or repository.

### Configuration closure

The [Configuration dispositions](myopencommunity-lighting-automation-configuration-dispositions.tsv) bind 466 original XML identities to source and selector-projection hashes. Twenty-nine distinct views compare old page IDs `1`/`2`, their model/control IDs, modern `200x`/`300x` and fine-dimmer selectors, instance overrides, linked Objects and F411 resource output identifiers with executable consumers. Fields include WHERE, PUL, mode, fixed/custom time and start/stop speed, without copying installation values into public provenance. Equivalent namespace/flag/field-presence shapes are reused; configured duration/address values are not claimed as physical capacities.

Two historical XML files require a Latin-1 read because their declared encoding does not match the bytes. One lighting XML blob has a duplicate attribute and remains unparsed/excluded; no repair or runtime acceptance is assumed. UI resource output counts, sample instances and unchecked serializer setters do not establish hardware capabilities, valid wire grammar or atomic Configuration behavior.

## Pinned source basis

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Lighting implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/lighting_device.cpp), [Lighting assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_lighting_device.cpp), [Automation implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/automation_device.cpp), [pull assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_pull_manager.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Retained shared tests and namespace-overlap fixture screen; no independent wire claim |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Lighting models/Configuration](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/lightobjects.cpp), [application assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_light_objects.cpp), [Automation models](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/automationobjects.cpp), [safe control](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/Components/ControlUpDownStopSafe.qml) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | [F411 model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F411_DEV_PGIN/btf411dev.cpp), [F422 model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F422_DEV_PGIN/btf422_dev.cpp) |

Component IDs below are ledger references, not protocol identifiers. Assertion precedence is exact tests, executable behavior, comments/identifiers, then labeled inference.

## Level conversion and cached state

`L0009` is the final inverse converter. It maps zero to OFF, then requested fine levels into the coarse thresholds documented in [Lighting WHAT](../../functional/who-1-lighting/what.md#historical-client-level-conversion). The coarse setter (`L0027`) ignores speed; the fine setter (`L0037`) uses `100 + level` and the supplied speed in `DIMENSION 1`. Exact library assertions cover the wire outputs, including requested `75`/speed `9`; executable boundary checks cover every requested integer `0..100`. Neither the inverse nor the already documented forward table establishes a physical dimming curve. Unchecked negative/out-of-range setter input is not an extension of the protocol domain.

Final decoder/cache bodies `L0021`, `L0029`, `L0040` and their exact assertions distinguish state from level/speed freshness. `DIMENSION 1` raw `100` sets OFF without overwriting the remembered level or emitting a fresh level/speed. Nonzero reports update the level; only ON reports forward speed. Dimension writes update local level without forwarding speed. Coarse/fine relative commands while OFF set ON while retaining the remembered level; while ON they clamp to coarse `2..10` / fine `1..100`. For ordinary ON/OFF frames, unknown-level collective ON starts a delayed query, point ON does not, and OFF cancels it. These are local prediction/query choices, not a substitute for a point report.

`WHAT 19` sets the local dimmer-problem value. Product `Dimmer::valueReceived` / `Dimmer100::valueReceived` (`L4360`, `L4381`) clear the local broken flag on any decoded ON/OFF value, including OFF. Received speed is not adopted as the product's configured ON speed. Fine consumers use the fine attribute to avoid duplicating a coarse percentage update. [Lighting Dimensions](../../functional/who-1-lighting/dimensions.md) gains the scoped freshness and relative/query qualifications; WHAT gains the fault-handling note. No physical cause/recovery rule is inferred.

## Timed actions and Configuration selection

Product `Light::setActive` (`L4343`) sends the selected fixed/custom timer directly. `Dimmer100::setActive` (`L4374`) first sends ON through its configured-speed dispatcher, then the timer operation. Positive configured speed is parameterized; zero/negative selects plain ON/OFF. Exact product tests, including `TestDimmer100::testSetTiming` (`L4429`), establish the ON-then-DIMENSION-2 example in [Historical timer handling](../../functional/who-1-lighting/dimensions.md#historical-timer-handling). This sequence does not require all timer writes to be preceded by ON or prove gateway acceptance.

Parent Configuration defaults and per-instance overrides select WHERE, PUL, coarse/fine model, fixed/custom timing and start/stop speed (`L4319`). Fine support is explicit class selection, not detected deployed Firmware. The presentation CID can alter the point/collective display flag without defining wire addressing. A linked Lighting group (`L4320`, `L4348`) dispatches each referenced Object individually. The fine-group fallback can select a plain LightGroup for an initially linked fine fixed collective Object; the factory does not prove a universal least-capable-dimmer selection rule.

Staircase Objects (`L4321..L4326`) delegate to `WHO 8`, whose canonical commands remain on [Video Door Entry](../../functional/who-8-video-door-entry-telephony/). [Lighting](../../functional/who-1-lighting/README.md#functional-model) adds the category/group distinction without duplicating that wire table.

## Automation controls and namespace boundaries

The final Automation decoder (`L0067`) recognizes decoded base WHAT `0`, `1`, `2`; its writers emit ordinary STOP/UP/DOWN and status requests. It does not implement the published positioning dimensions. Acceptance without a frame-family check is parser permissiveness, not additional valid grammar. PPT contact handling (`L0071`) belongs to `WHO 25`; final closed/open values corroborate [Dry Contact](../../functional/who-25-transversal/dry-contact-ir.md), despite older swapped local booleans.

Product selectors `L4274..L4278` retain the already documented `WHO 1` two-state, `WHO 2` three-state, `WHO 25` contact and `WHO 8` door-entry delegates. Pinned safe Up/Down and Open/Close callbacks send ordinary UP/DOWN on press and STOP on release through the three-state setter. The mode flag selects this interaction; it does not set advanced command priority or prove a hardware safety/interlocking feature. [Automation](../../functional/who-2-automation/README.md#historical-product-labels) gains that qualification. Older delayed releases/manual releases remain client policy, not physical generation boundaries.

## Historical corrections, simulator corroboration and exclusions

The retained full component comparisons follow intermediate corrections, removed earlier locations and every selected parent. Coarse caches once used WHAT times ten, while later code separates coarse indices and fine levels; an early fine decoder retained raw `134` before subtracting the offset to `34`. `WHAT 10` once fell through to `80` before explicit `100`. Earlier inverse rounding, OFF-level resets, empty setters, timer offset APIs and collective/pull classifications were revised. These are client corrections and cache/API changes, not demonstrated actuator wire-version splits.

Removed controllers include compile-disabled alternatives, stale `WHO 1` state queries in Automation paths, an initially recursive group sender and a TCP demo that sends human-readable text. Older minute/second guards accepting `60` do not replace published ranges. A removed `1000#` handler is implementation support for an already published wrapper, not proof of a deployed family boundary. Misspelled/mismatched test names, synthetic `###`/`####` terminators and empty inherited overrides do not establish additional wire semantics.

F411 serializers, per-output LED/state models and 1/2/4-output constructors corroborate the already qualified [Configuration model](../../device-model/configuration.md). Point/group versus general/area/PUL behavior and shortcut WHAT-to-OFF handling remain simulator scope. ACK ordering, duplicate requester/event dispatch and partial XML mutation do not prove physical success, duplicate reports or atomic hardware programming. F422 strip/append routing and general bypass corroborate [Addressing](../../protocol/addressing.md); historical interface-range changes, unchecked setters and empty-token splitting do not establish physical Firmware versions. Resource/build inconsistencies are excluded as protocol evidence. No device page changes are needed for those already incorporated findings.

| Candidate | Disposition |
| --- | --- |
| Repository dates or library revisions identify actuator Firmware generations | Excluded: no capture/release/device mapping |
| Coarse/fine conversion specifies a universal physical output curve | Excluded: client cache/setter table; separate published labels and target observations retained |
| `WHAT 19` proves a fault cause or an OFF report proves physical recovery | Excluded: local broken-flag behavior only |
| Timed fine ON-first behavior is mandatory protocol order | Excluded: application action sequence, not all writers |
| “Safe” UI mode selects advanced Safety priority or guarantees interlocking | Excluded: ordinary movement/STOP callbacks |
| PUL flags, delayed polling or model/fixture counts define hardware limits | Excluded: Configuration and client/simulator policy |
| Removed PPT writers or stale `WHO 1` Automation queries extend `WHO 2` grammar | Excluded: separate `WHO 25`/prototype/correction behavior, without deployed corroboration |
| Malformed terminators, coercion or missing family guards extend valid syntax | Excluded: fixtures/parser permissiveness; absent external OpenMsg classification unresolved |
| Simulator ACK, duplicate dispatch or partial XML parsing proves hardware behavior | Excluded: executable simulator shortcuts/local persistence |
| Empty overrides or test names prove payloads not asserted by their bodies | Excluded: scaffolding/naming, including level-up tests invoking decrement |

Captures/hardware are still needed for deployed PUL/advanced capability behavior, level/speed freshness while OFF, physical fault meanings/recovery, coarse-to-output curves, timing reports and target/Firmware applicability. The existing `WHAT 17` 30-second/30-minute specification conflict remains unresolved; library comments do not settle physical duration. The external OpenMsg stack is needed to settle malformed-input classification. Remaining generic UI-only history can receive a separate semantic review if its behavior becomes the research target; automated screening here is not exhaustion.

## Machine KB maintenance and validation

Six existing sections record scoped additions as candidates for later atomic extraction while retaining coverage status/count. Sixty-one retained claim records refresh section digests, including parent sections affected by child text. Existing statements, sources, supporting block text/indexes and context are unchanged. The corpus retains 7,448 claims and 1,223 chunks. No atomic claims or section/chunk identities are added or redesigned.

The targeted Qt 5 Core harness compiles 72 original method bodies (Lighting, Automation/PPT, frame constructors, BtTime support and selected product methods). It passes 140 comparisons, including all inverse integer levels `0..100`, exact writers, decoder/cache/fault behavior, timer ordering and base Automation states. Token/family classification, address-class result, output, timer activity, product base callback and signal sinks are controlled seams. It does not execute full archived Qt suites, external OpenMsg parsing, actual sockets/event-loop timing, complete UI consumers or hardware.

Supplemental assertion/helper sources are pinned independently; hashes below are original file bytes, without fixture contents:

| Source | Revision | SHA-256 |
| --- | --- | --- |
| [Device assertion helper](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/device_tester.cpp) | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | `35c594b227c917dccdd8fe80c5e4590385a8efa6837f6b6d8e44843f0c4a0c20` |
| [Device assertion declarations](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/device_tester.h) | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | `f2ed7abc25de9a54225f76f7844737d61a3f86fe1b315cf67ccbf8507bca9936` |
| [Extended timer implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/bttime.cpp) | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | `aebbded4121a0e1a16138acd13e0a46362be5a90a8f72fab758cccc8d2d3cdaf` |
| [Frame constructors](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp) | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | `b85b10858286272af2c4f73be051af884e9fc29deee66a2b9533aff9f58364a8` |
| [Object signal assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/objecttester.cpp) | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | `c36e77df1150ef884e41d8b61d9102ba341250fb84cefe4b6f599e3964c34003` |
| [Product byte comparisons](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_btobject.cpp) | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | `33a5aa04fc8f43301017aab40e84669e8645fb501c14a5c11237b03264cb7cd8` |
| [Local socket mock](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/openserver_mock.cpp) | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | `a722783fd9b01ed8c050009cd03aeddfeed95008e10eb4accdb2f79a409d024e` |

The product comparison helper flushes both clients and compares each mock's `readAll()` bytes; the timed tests build the expected ON/timer sequence on the comparison client. Original serializers independently establish ordering. Mock setup discards initial traffic; these assertions do not test handshake or physical execution.

| Validation | Result |
| --- | --- |
| Independent history reconstruction | Pass: 23,061 edges, 46,122 endpoint tree identities, 8,809 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 6,666 source tree/content/body identities, 1,740 assertion/check-call identities and 7,282 comparison references; all edge bindings/destinations verified, semantic coverage distinguished above |
| Configuration selector comparison | 29 views across 466 original XML identities; two encoding fallbacks and one malformed file retained as limitations |
| Targeted original-body execution | Pass: 140 comparisons, 72 original bodies, with controlled seams and execution limits above |
| Normal build / integrity check | Pass: deterministic artifacts, manifest, schemas, references, text hygiene, privacy and consistency |
| Machine-KB unit / schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact / canonical-source audits | Pass: 144 registered artifacts, all 25 fingerprints verified, five database integrity results `ok`, no source-audit failures; authorized privileged R2 helper used |
| Links / wire examples | Pass: 52 local/anchor targets and 19 public source links checked; changed frames checked against exact assertions and original writers |
| Style / Core Values | No objective failures; pre-existing style/identifier candidates remain advisory |
| Epistemic / neighboring-page review | Protocol, client, Configuration and simulator scopes separated; published vocabulary/ranges and unresolved `WHAT 17` retained |
| Complete diff / Machine-KB impact | Four canonical pages, four provenance records and six KB maintenance inputs/artifacts; unchanged claim/chunk identities and supporting contexts; no full-KB review flag |

The full diff is reviewed for unsupported generalization, duplicate placement, canonical frames, privacy, neighboring-page consistency and source immutability. The branch is committed and pushed without merging. This closes the bounded Lighting/Automation review, not all MyOpenCommunity extraction.
