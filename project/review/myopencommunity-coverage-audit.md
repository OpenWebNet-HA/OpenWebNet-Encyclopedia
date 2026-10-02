# MyOpenCommunity Coverage Audit

This continuation starts at `b9263843860b19c77a7d0def8520ea2c055e8b46` on `docs/myopencommunity-integration`. It uses the four preserved repositories, their retained histories, the [first integration review](myopencommunity-integration.md), and the [source reassessment](myopencommunity-reassessment.md). Conversation findings are context, not a coverage boundary. Synced project sources and archived checkouts remain unchanged.

## Coverage and disposition records

| Repository | Source revision | Indexed bodies | Test bodies | Assertion/check-call sites |
| --- | --- | ---: | ---: | ---: |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | 2,349 | 526 | 1,967 |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | 1,292 | 681 | 1,143 |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | 524 | 224 | 522 |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | 714 | 0 | 0 |

The [body and assertion dispositions](myopencommunity-dispositions.tsv) identify each indexed test/helper/implementation body by repository, revision, file, Git blob, symbol, source range and body SHA-256. Body hashes cover the UTF-8 encoding of indexed text, with replacement decoding for legacy non-UTF-8 bytes; the Git blob identifies the original byte-exact file. Assertion and helper-call rows inherit the containing case's feature disposition, except explicit debug-precondition exclusions. Repeated comparisons, Qt data rows and helper calls are source sites, not independent runtime cases or passing assertions. A helper's assertion may execute for many inputs. Empty overrides and setup/cleanup bodies remain indexed. The complete pinned test bodies and their inline assertion helpers were read, including model, media-player, file-browser and screen-state tests that supply no additional protocol vocabulary.

The [file dispositions](myopencommunity-file-dispositions.tsv) retain all 1,660 tracked entries. They provide context for declarations, enums, configuration tables, macros, symlinks and source outside recognized function bodies. A lexical balanced-brace index is a navigation aid, not a compiler AST or proof that every source statement was interpreted. Qt3 untyped methods, operators and some inline constructors require file-level review. Infrastructure exclusions do not assert that a file was executed or that each of its functions proves protocol semantics.

The [historical body dispositions](myopencommunity-historical-bodies.tsv) cover 2,594 indexed bodies across 170 distinct terminal blobs, including 349 test/helper bodies and 391 assertion/check-call sites. Their `terminal-variant-comparison` reason points to the scoped comparisons and supersession/exclusion table below; it does not promote the older version over the mature implementation. Function and case counts are navigation counts, not a count of newly established facts.

| Reason code | Meaning |
| --- | --- |
| `scoped-boundary` | Serializer, decoder, delegated API or exact check compared with the canonical feature page; retain the repository's scope |
| `client-state` | Cache, decoded state or product transition corroborates scoped client material; no universal state machine inferred |
| `configuration-mapping` | Object/instance fields, class selection and address construction corroborate configuration boundaries |
| `local-only` | UI, storage, formatting, scheduling, accessor or local property supplies no additional wire rule |
| `fixture-or-lifecycle` | Test setup, mock, cleanup or assertion harness rather than a device/protocol capability |
| `debug-precondition` | Debug assertion defines a library precondition, not hardware validation or a wire field domain |
| `misleading-test-name` | Both compared objects call decrease despite an increase-labelled test; no directional claim |
| `stale-fixed-sid` | Fixed-SID fixture disagrees with UUID-generating implementation; exact envelope comparison cannot establish that contract |
| `declarations-and-configuration-context` | File-level declaration/configuration context; actual wire meanings come from corresponding tests/implementations |
| `file-boundary-only` | Asset, build, presentation or dependency boundary; no additional protocol assertion |
| `terminal-variant-comparison` | Historical boundary compared with the mature implementation; superseded details remain excluded below |
| `legacy-mixed-dispatch-superseded` | Older combined UI/wire dispatcher is not an independent protocol reference; mature feature-specific serializers and decoders take precedence |
| `superseded-namespace-mismatch` | Older WHO-10 request / WHO-13 decoder mismatch cannot establish a namespace equivalence |
| `superseded-yearly-totalizer` | Older dimension-51 yearly-total interpretation is superseded by rolling monthly assembly |
| `empty-reset` | Empty implementation cannot establish the reset behavior expected by a stale fixture |

`incorporated` identifies evidence for this pass's additions; `corroborates` points to canonical material retained across the combined passes; `excluded` records why a source item supplies no publishable additional protocol knowledge. A canonical-page link is a feature destination, not a claim that every local property on that row is described there. The ledgers deliberately contain identifiers and hashes rather than fixture payloads, credentials, host values or raw configurations.

## Pages changed in this continuation

| Page | Addition or qualification |
| --- | --- |
| [Scenarios](../../functional/who-0-scenarios/) | Unparameterized programming indications, address bypass, basic IR actions and API-capacity boundary |
| [Lighting Commands](../../functional/who-1-lighting/what.md) | Coarse-to-fine client cache conversion, including `9` to `75` |
| [Temperature Control Dimensions](../../functional/who-4-temperature-control/dimensions.md) | Reported setpoint versus cached base after local offset subtraction |
| [Energy Dimensions](../../functional/who-18-energy-management/dimensions.md) | Client load-level labels, threshold enable/cache behavior and F520 simulator monitor-only power reply |
| [Energy Commands](../../functional/who-18-energy-management/what.md) | Force-read request option independent of graph decoder generation |
| [Video Door Entry and Telephony](../../functional/who-8-video-door-entry-telephony/) | Pager writer/receiver distinction and answer-driven call-state qualification |
| [UPnP Multimedia](../../functional/who-26-upnp-multimedia/) | Separate OpenXml request/response vocabulary and decoded media metadata |

The source reassessment record's Celsius/Fahrenheit boundary statement is also corrected. The reader-facing energy text no longer calls differential-current labels wholly unspecified: they are absent from the public specification but named by the historical client. Pager broadcast wording now applies to the writers rather than all accepted receive traffic.

## Scenario and basic IR controls

[Scenario assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_scenario_device.cpp) and [scenario decoder](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/scenario_device.cpp) establish unparameterized programming indications. `receiveGenericModuleIsProgramming`, `receiveGenericStopProgramming` and `receiveGenericStartProgramming` cover the absent scenario parameter and asymmetric address bypass. The start branch updates client state across module addresses; the comment about locking all modules does not establish physical recording, and its cached unlocked flag must not be paraphrased as a wire lock command.

[Basic/advanced IR serializers](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/airconditioning_device.cpp), [split object assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_splitscenarios_object.cpp), and [basic program configuration](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/splitbasicscenario.cpp) distinguish WHO-0 configured actions from WHO-4 dimension-22 split records. Optional OFF presence and command text are configuration policy. API scenario assertions `1..31` do not replace published physical capacities. Added to [Scenarios](../../functional/who-0-scenarios/).

## Probe state and load levels

[Probe assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_probe_device.cpp) and [probe decoder](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/probe_device.cpp) establish `receiveSetPointAdjusted`: offset `03`, reported setpoint `0250`, cached base `0220`. The adjustment applies when local status is normal and offset is known. Added to [Temperature Control Dimensions](../../functional/who-4-temperature-control/dimensions.md), without changing the published meaning of the transmitted temperature.

[Load assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_loads_device.cpp), [load enums and decoder](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/loads_device.h), and [product load tests](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_energy_load.cpp) establish dimension-73 classifications `1` OK, `2` warning, `3` critical. The published range remains canonical; no physical trip threshold follows from these enum names. Added to [Energy Dimensions](../../functional/who-18-energy-management/dimensions.md).

The original [conversion helpers](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scaleconversion.cpp) were compiled separately with six checks: raw `1010` converts to -10 Celsius tenths and 302 Fahrenheit tenths; the inverse helpers recover `1010`; raw `1000` converts to zero Celsius but 2120 Fahrenheit tenths. All six checks passed. This corrects the previous review record's zero-equivalence statement. It does not establish an extra wire sentinel or hardware behavior.

## Threshold enable state

[Energy product assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_energy_data.cpp) and [energy product implementation](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/energydata.cpp) distinguish current threshold, remembered nonzero threshold and enabled state. `testSetEnableThresholds` and `testReceiveThresholdValue` verify zero writes on disable, restoration on enable and retained nonzero cache after a zero report. Dimension `516` supplies enabled state independently. Added to [Energy Dimensions](../../functional/who-18-energy-management/dimensions.md).

The lower decoder's `parseFrame` return flag does not determine whether nonempty threshold values are emitted: the base device's dispatch consumes the populated value list. A false return on `516`/`517` is therefore not published as a broken threshold implementation.

## OpenXml media vocabulary

[XML response assertions](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_xmldevice.cpp), [media serializers/decoders](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/xmldevice.cpp), and [tag identifiers](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/xmldevice.h) establish server selection/listing, parent browse, next/previous track, ranked lists and navigation context. The table on [UPnP Multimedia](../../functional/who-26-upnp-multimedia/) records the actual XML tags, arguments, results and metadata. The existing canonical stream page remains the envelope/framing destination.

Fixed-SID builder/header/reset fixtures are inconsistent with the mature builder's UUID and queued response correlation. The reset method is empty despite its fixture. Local application error enums are not numeric wire return codes. No numeric OWN command registry, external-gateway support or stable SID contract is inferred.

## Coarse lighting levels

[Dimmer assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_lighting_device.cpp) and [level conversion](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/lighting_device.cpp) establish the fine cache table for coarse `WHAT 2..10`, including `9` to `75`. Older removed coarse classes/tests retained `9` as `90`, while fine classes expected `75`; those were different cached representations, not a hardware percentage calibration. [Lighting Commands](../../functional/who-1-lighting/what.md) now states the mature client table and links the existing capture-derived dimension discussion.

## Historical corrections

The [history dispositions](myopencommunity-history-dispositions.tsv) retain 689 deletion edges across C++, headers, XML, QML and JavaScript, including exact pinned-blob equivalences. The direct boundary search found 89 edges and 66 distinct noncurrent C++/header blobs. A second search followed indirect device API calls, decoded values, constructors and status subscriptions, yielding another 86 candidate blobs. Eighteen additional terminal blobs covered configuration loaders, scale conversion, local time/state and delegated UI mappings. These terminal variants were compared by relevant serializer/decoder/configuration/state behavior, not treated as current protocol rules. There are 469 unresolved deletion edges; these are edges, not necessarily 469 unique files or protocol-bearing implementations. Marker-negative records remain explicitly unresolved where their semantics have not been independently adjudicated; absence of a marker is not an exhaustion proof.

| Additional correction patch | Disposition |
| --- | --- |
| [Pull state argument guard](https://github.com/OpenWebNet-HA/libqtdevices/commit/e0cc57927f059feea8a025b9ec7abb3685a9bdb9) | Positive argument needed for measured dimmer state; client capability detection already scoped |
| [Invalid dimmer report](https://github.com/OpenWebNet-HA/libqtdevices/commit/714def8356d9e0f4de936b2de129ae261aa421dc) | Guard replaces assertion crash; malformed report acceptance does not expand syntax |
| [Preset write remapping](https://github.com/OpenWebNet-HA/libqtdevices/commit/15d8a99d467a8698cb7bb80e06656ccc34832331) | Corroborates existing UI-to-wire preset distinction |
| [Automatic radio tuning](https://github.com/OpenWebNet-HA/libqtdevices/commit/650201590441462d90439dd69135f29efbd58760) | Corroborates already documented omitted automatic-search argument |
| [Pager caller state](https://github.com/OpenWebNet-HA/libqtdevices/commit/9729bf48146fb7978763c182563f8a009dd22f59) and [pager receive forms](https://github.com/OpenWebNet-HA/libqtdevices/commit/5d2287c646110d06b42eb16380e8d0fb5924bfa4) | Qualifies broadcast-only wording: writers broadcast, receiver also accepts local calls/nonbroadcast answers and waits for answer state |
| [Probe request terminator](https://github.com/OpenWebNet-HA/libqtdevices/commit/419c78bab26e6de4c9d3cd09bbfcb1e1b5d360c8) | Confirms `##`; old missing terminator excluded |
| [Local probe protection](https://github.com/OpenWebNet-HA/libqtdevices/commit/e4e85e09ffb893c7f3fd0e667e456ba074783a3e) | Corrects local cache branch; no new offset encoding |
| [Thermal date/time/duration](https://github.com/OpenWebNet-HA/libqtdevices/commit/039d36189c2f87b97624aabb4a521ec24f64464a) and [dimension guard](https://github.com/OpenWebNet-HA/libqtdevices/commit/df1cb6b764583f53851432f08d075c28652e57f0) | Current guarded decoder retained; ordinary `WHAT 30` does not become dimension 30 |
| [Hot-water selector](https://github.com/OpenWebNet-HA/libqtdevices/commit/e527b42cedaceac08f3e0f5007fe652b143b0d21) and [mode/type separation](https://github.com/OpenWebNet-HA/libqtdevices/commit/fc741a4e081f9b10710104d98e6be6cd23f38a1a) | Current `1134` mapping retained; older heat selector is superseded |
| [Empty ACK queue guard](https://github.com/OpenWebNet-HA/libqtdevices/commit/ae54c71ae8905113d9d64da326b08d172bd1dae1) | Debug assertion still present; no universal crash-free ACK guarantee |
| [XML request queue and UUID](https://github.com/OpenWebNet-HA/libqtdevices/commit/9a06b102918b4a559bbe5600b68450a0539e07ec) | Explains conflict with stale fixed-SID fixtures |
| [Client command ordinal](https://github.com/OpenWebNet-HA/libqtdevices/commit/dea9af70d2c5e37aefbe9185077ae2491870b61f) | Application counter; not a new wire identifier |
| [Forced energy read requests](https://github.com/OpenWebNet-HA/libqtdevices/commit/59effd83e6bef4ea90ec2a8e87ffcffab7c402fe) | Adds force-read option independent of graph decoding; affected hardware/PIC combinations unspecified |

The pager qualification is on [Video Door Entry and Telephony](../../functional/who-8-video-door-entry-telephony/). The force-read qualification is on [Energy Commands](../../functional/who-18-energy-management/what.md). Earlier correction patches remain traced in the two previous records.

## Simulator dispatch

The built [F520 model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F520_DEV_PGIN/btf520_dev.cpp) constructs but replaces the external destination before emitting the dimension-113 response, so the read report reaches the monitor path. This is added as a simulator limitation in [Energy Dimensions](../../functional/who-18-energy-management/dimensions.md). It does not describe physical F520 request-channel behavior.

F411 mode/output/group serialization, F422 general versus qualified routing, F454 gateway/session dispatch, generic scripted messages, camera selection and plant/bus state were rechecked against the existing integration. No extra device capability is inferred from unbuilt F520 resource copies, manually failed cases, fallback ACKs, local message IDs or simulation clocks.

## Exclusions and unresolved evidence

| Finding | Reason for exclusion or unresolved status |
| --- | --- |
| Extra `#` suffixes and write-marker receive fixtures | Permissive client/test inputs; examples retain canonical frame families and `##` |
| Old yearly totals attributed to dimension 51 | Superseded by mature rolling-month assembly; not restored as current dimension semantics |
| Older version helper mixing WHO 10 and WHO 13 | Request/decoder mismatch; does not override the PIC dimension-20 model |
| Removed thermostat writer with missing `*#4*#` prefix | Incomplete old implementation fragment, not an alternative frame grammar |
| Old UI group loops, `pul` flags, capacities and ranges | Application class/configuration policy; not physical membership or support evidence |
| UI graphs, goals, tariffs, playback, screensavers and file models | Local presentation/cache/storage behavior without additional device/protocol facts |
| Calendar maxima and throttling/retry/poll intervals | Library/product constraints, not universal device ranges or protocol deadlines |
| Fixed XML SID, empty reset and stale fixtures | Conflicting executable implementation takes precedence over exact but obsolete expectations |
| Precise BACnet adapter/Firmware applicability and scales | Requires product documentation, captures or hardware evidence |
| StopGo configured `2N` versus published `1N` | Existing discrepancy remains; hardware/capture evidence needed |
| Graph interruption and PIC request compatibility | Comments identify symptoms without affected product/Firmware versions |
| F520 request/monitor delivery and timing accuracy | Model behavior cannot settle physical device semantics |

This pass reaches a defensible stopping point for the pinned functional test bodies, direct/delegated protocol boundaries, configuration selection and documented terminal historical variants. It does **not** claim that the repositories are exhausted. Every intermediate historical revision has not been semantically reviewed, marker-negative deletion entries remain a follow-up queue, external dependency targets are incomplete, and the full legacy Qt suites cannot be rebuilt from these archives alone. The index and two small execution harnesses do not substitute for that work. The remaining hardware questions cannot be settled by further interpretation of client names or simulator output alone.

## Validation and Machine KB maintenance

Three new documentation sections are recorded through the existing identity/chunk/coverage mechanism as deferred atomic-claim work. Of 213 affected retained claims, 212 preserve their supporting text and materialized meaning; the remaining claim is narrowed to the public specification's absence of load-level labels. One editorial page-summary claim is retired with a registry tombstone. The corpus now contains 7,448 claims and 1,222 retrieval chunks. No new atomic claims or Machine-KB design are introduced. Fixed-count unit-test expectations are updated to reflect these reviewed changes, retaining all integrity checks.

| Validation | Result |
| --- | --- |
| Reader-page and neighboring-page review | Seven changed pages reviewed; frame families, placeholders and local routing parameters retained |
| Local documentation paths and heading anchors | 87 checked, all resolve |
| Public provenance links | 72 checked, all HTTP 200 |
| Disposition ledgers | Unique body/check IDs, source hashes and canonical destinations verified; 1,660 inventory Git blobs checked against the pinned trees |
| Deterministic build and `check.py` | PASS, including freshness, schemas, references, text hygiene, cross-artifact consistency and privacy |
| Machine-KB unit tests | 59 PASS; four initial fixed-count failures corrected after reviewed section additions and claim retirement |
| Schema tests | 8 PASS |
| ESG | 146 human pages, 36 support pages, 0 objective failures; 127 advisory candidates |
| ECV | 0 objective failures; 13 existing public-identifier candidates retained after contextual review |
| Epistemic drift | Advisory queue reviewed for changed pages; new load-level candidate explicitly retains client scope and excludes physical thresholds |
| Artifact manifest | PASS, 144 artifacts |
| Canonical-source audit | PASS using the R2 helper outside the sandbox: 25 fingerprints, 5 database integrity checks, 0 failures |
| Full diff and change impact | 480 affected claims, 95 chunks and 85 references identified; complete generated delta reviewed, with one retained statement narrowed and no other retained claim-meaning changes |
| Whitespace diff check | PASS |

The six-check converter harness passed separately from the prior 29-comparison address-matcher harness; neither is reported as a full legacy suite run. Private audit inputs and fixture values are not included in the committed review records.
