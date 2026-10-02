# MyOpenCommunity Source Reassessment

This reassessment starts from the four preserved source trees, their build descriptions, test inventories, configuration families, and retained Git history. It audits the [first integration](myopencommunity-integration.md) and adds independently discovered omissions. The supplied recovery conversation remains context, not the coverage boundary or claim evidence.

Starting revision: `ab57221c4df063764d236397f64b7bbebd9b00b8`. Branch: `docs/myopencommunity-integration`. No archived source or synced project file was modified.

## Coverage method and limits

The [source inventory](myopencommunity-source-inventory.tsv) enumerates all 1,660 tracked entries at the four pinned revisions, including three BtExperience dependency symlinks. Every preserved file or link was compared with its Git blob identity; zero content differences were found. Each inventory row identifies its coverage group and review scope. Inventory coverage is not a claim that every asset, every test assertion, or every historical revision was semantically read or executed.

| Repository | Pinned substantive tree | Tracked entries | Indexed test `.cpp` files | Indexed Qt assertion sites |
| --- | --- | ---: | ---: | ---: |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | 1,266 | 21 | 1,214 |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` | 97 | 20 | 726 |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | 45 | 10 | 229 |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | 252 | 0 | 0 |

The test inventory includes harness/main files; assertion counts describe source sites, not passing runtime cases. DeviceTester checks and data-driven rows add evidence beyond those counts. The emulator instead contains a manual test document, inspected as a separate evidence class.

The three library/product `master` trees each contain only two placeholder/licence files. Their full identities are `211ffe968d50a3d2380c6e9c4ce6a42b33711a6d`, `2754ae6fde96fafe9fc222c27c3ccb58f489695b`, and `0d1e90af9cc940f755b0d4f0d18d4d2b303e39fd` respectively. They do not supersede the substantive TS10 trees. Retained histories contain 7,649, 1,518, 4,935, and 27 commits respectively; those counts overlap through extracted project history and are not independent corroborating sources. History subjects and changed source paths were triaged to locate removed classes, generation changes, and corrections. Relevant patches and the earlier BTouch snapshot were compared with mature implementations. This is not an assertion that every historical commit was reviewed line by line.

Executable libraries, exact frame assertions, object-layer tests, direct-frame/configuration scans, and simulator dispatch/build boundaries were compared by subsystem below. UI assets, translations, font/audio/image files, installer scaffolding, generated resource source, and build outputs do not supply new protocol rules merely by being present. Certificate contents were not used. External dependency symlinks are retained as boundaries, not dereferenced into an assumed recovered protocol implementation.

## Subsystem dispositions

| Source subsystem | Result of combined first pass and reassessment |
| --- | --- |
| Frame constructors/classification | Four families confirm canonical syntax; helper variable names do not rename wire fields |
| Incremental TCP client and subscriptions | Framing confirms stream model; monitor status-request filtering and local channel roles now recorded |
| Writer ACK/NACK, batching and reconnect tests | FIFO association, subscriber fan-out, duplicate removal and outstanding-frame replay now scoped as client choices |
| Device cache, lazy initialization, compressor, delayed slots, time helpers | Initialization and coalescing infrastructure; no new protocol vocabulary or universal deadlines |
| Address matcher and exact address tests | Global/level/interface/environment distinctions and lack of inferred group membership now recorded |
| Lighting and fine/coarse dimmers | Existing syntax confirmed; invalid timer payload and collective-command capability detection documented |
| Automation and contact device classes | Existing direction confirmed; contact correction retained; product category does not determine namespace |
| Scenario module and ScenarioPlus | `WHO 0` corroboration and `WHO 25` extension retained; API index domain not converted into a physical capacity claim |
| Alarm and alarm-product tests | Existing events, source domains, password controls and zone mask retained with eventual-state scope |
| StopGo base, Plus and BTest | Controls, mask and interval retained; discovered fixture prefix conflict now explicit |
| Probe and central-unit generations | Signed values, external query, composite addressing, timed-manual behavior and workaround scope reviewed |
| Basic/advanced split controls and object programs | Exact partial-write frames retained; program selection/configuration limits are UI policy |
| All four BACnet classes and record tests | Field order retained; fan/direction enum domains, reset-zero write and empty-report coercion added |
| Energy graph/scalar/update/PIC tests | Legacy/newer graph and PIC axes retained independently; scaling/sentinel/cache choices remain scoped |
| Load and product energy-load tests | Status and totalizer syntax confirms canonical material; misleading force API names not promoted |
| Product energy data/rates/goals | Display/cache/currency/goal behavior is application policy; no additional physical measurement guarantees |
| Platform properties and product platform layer | Gateway/PIC/clock evidence retained; local properties not generalized to external gateways |
| Video door entry, camera movement, intercom/pager and teleloop | Existing integration checked against separate message/call classes; unknown full address domains remain unresolved |
| Guard Unit message receiver and product message model | Transaction/checksum evidence retained; local timers not generic protocol deadlines |
| Sound sources, radios, amplifiers and power amplifiers | Tested syntax/conversions retained; virtual-amplifier temporary-off events added |
| Old `WHO 16` matrix/initialization history | Earlier routing/state evidence retained; corrected source dialects not universal translations |
| Common-library condition predicates | Lighting initialization qualified with Auxiliary exception, inclusive ranges and temperature band |
| Product advanced/scheduled scenario models | Enable/weekday and time-versus-Device gating added; literal configured actions not inferred numeric grammars |
| Multimedia XML client/device and exact XML tests | Separate envelope/framing boundary added; no invented `WHO 26` numeric mapping |
| Common media/file/tree/list/entry/signal wrappers | Application infrastructure; no new OWN registry; XML identifiers kept separate from wire ACK |
| Product configuration, object identity/model, UI mappings and groups | Instance-over-object attribute precedence checked; category and group labels not equated with wire namespace/collective target |
| QML/JavaScript, GUI and configuration frame references | Boundary scan directs protocol evidence to underlying serializers; presentation names and sample action literals not capability guarantees |
| F411 variants/configuration/PUL/manual cases | Existing simulator scope retained; manual failed collective cases cannot establish hardware support |
| F422 routing/configuration and crash-fix history | Existing routing limitations retained; no broadened real-interface ranges |
| Built F520 model/resource files/history | Existing simulation boundaries retained; unbuilt `resources/` source copies excluded from compiled capabilities |
| F454 TCP/HTTP/HTTPS model and session handling | Fallback ACK retained; local selector names distinguished from published roles; no real gateway authentication claim |
| Camera plugin/status/schema/manual cases | `WHO 6` selection/deactivation and broader simulated range added with simulator scope |
| Generic-device XML scenarios/messages/worker | Replies are fixture-driven exact-string triggers with scripted loops/delays, not discovered physical-device vocabulary |
| Plant/bus/bus-connection/PlantMessage/factories | Qt signal/message abstraction; internal IDs not wire transaction identifiers |
| Simulator UI/graphs/plant files/default fixtures | Configuration and simulation scaffolding, not physical timing or data-accuracy evidence |
| Emulator manual `TEST.docx` | Camera cases corroborate model behavior; malformed ACKs and contradictory/failed collective rows quarantined |

No additional supported namespace or product capability is inferred from stale declarations, comments alone, unused copied source, or UI identifiers. The existing first-pass additions remain in their canonical pages rather than being duplicated here.

## Address matching

[Exact matcher tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_checkaddress.cpp) and [Matcher implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/pulldevice.cpp) establish the added address table. Incoming unqualified `0` matches across levels, incoming `#3` is normalized to the unqualified level, local qualifiers must match textually, and extended environment `00` / `100` is not a point-number shortcut. The group assertions only prove that group membership cannot be inferred from a point/interface string; they do not establish full group matching.

A targeted Qt 5 harness compiled the original `splitWhere`, `getEnvironment`, and `checkAddressIsForMe` function bodies, the original `AddressType` declaration, and all eleven original test-function bodies. Only QtTest class scaffolding/QCOMPARE dispatch was replaced with assertion reporting. All 29 archived comparisons passed. This is narrower than rebuilding the complete legacy suite and does not test physical bus routing.

## Transport and session boundaries

[Local channel and writer implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/openclient.cpp), [Writer tests](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_clientwriter.cpp), [Connection dispatch](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_classes.cpp), and [Simulator selectors](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_own_GTW_PGIN/tcpserver.cpp) establish the channel/FIFO/batch/reconnect additions. The client names selector `0` request and `9` command; VDK names them command and request. Roles are derived from executable dispatch, not reconciled by renaming the public introduction's scenario-programming session. Two setup placeholders are queued for initial acknowledgements; subscriber WHO comes from the pending original frame. No ACK namespace field is invented.

The [Monitor request-filter correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/8e9331b03281f26c45233059c3654af437cb7134) moves filtering into the shared reader. It explains why monitor traffic cannot be assumed to consist entirely of state reports. The client-specific 25-second proactive reconnect and source-comment 30-second local-server inactivity behavior are not promoted into universal gateway timeout rules. Outstanding commands can be replayed; source comments asserting that such commands were not executed are not sufficient proof of exactly-once delivery.

## HVAC values and partial records

[Probe object tests](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_thermalprobes_object.cpp), [Probe object conversion](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/thermalprobes.cpp), [Shared converter](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scaleconversion.cpp) establish raw `1010` to signed `-10` tenths. This is product decoding, not an unrestricted negative-setpoint encoding rule. The code has different comparison spelling at the `1000` Celsius/Fahrenheit boundary, but both yield zero Celsius there; no new special-state meaning is inferred.

[BACnet enums](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/bacnet_device.h), [BACnet assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_bacnet_device.cpp), and [BACnet serialization/decoding](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/bacnet_device.cpp) establish fan and air-direction codes, the sixth-position reset `0`, and empty-report coercion. `sendResetFilterStatus`, `sendSetFanStatus`, `sendSetAirDirectionStatus`, and the corresponding partial receive tests were checked. Status-only writers preserve unused positions; receivers convert present empty strings to zero rather than preserving the same unset sentinel. Full report counts describe the declared record schema, not a requirement that every report contain every field. Exact adapter/Firmware applicability and physical scales remain unresolved.

## StopGo address discrepancy

The [February 2013 fixture correction](https://github.com/OpenWebNet-HA/BtExperience/commit/e0837759e80376ab14c8f781b3dae8591646e69e), [Mature energy configuration](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/conf/energymanagement/archive.xml), [Configuration parser](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/stopandgoobjects.cpp), [Instance-attribute precedence](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/xmlobject.h), and [Unchanged WHERE emission](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/stopandgo_device.cpp) establish that `22`, `23`, and `25` reach the class unchanged. The top-level Object `where="1"` does not prefix/replace those instance values. Mature unit fixtures often use arbitrary `1`, proving serializer behavior rather than an address grammar. The published `1N` family remains canonical; `2N` is an unresolved product discrepancy, not a second general address registry.

## Lighting and Automation state

[Collective-command state assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_pull_manager.cpp), [Lighting tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_lighting_device.cpp), and [State manager](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/pulldevice.cpp) establish the collective-command comparison strategy and unresolved advanced cases. Some unused test literals contain excess terminating hashes; those are not copied into the reference grammar. Request delays, optimistic cached state and capability names remain client policy. No reversed Automation direction is found in the operative mature tests.

## Product model boundaries

[Automation object parser](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/automationobjects.cpp) constructs Lighting, contact and door-entry classes for different Automation UI categories, and iterates configured Object lists for group operations. Three-state movement uses the Automation device. Product `cid`, `id`, `uii`, inherited attributes and list indices are not physical Device IDs, diagnostic Modules, or wire WHAT/DIMENSION registries. The existing Device Model remains the canonical source for those distinctions.

## Condition and scenario behavior

[Condition tests](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_scenevodevicescond.cpp), [Condition implementation](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scenevodevicescond.cpp), [Advanced-scenario tests](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_scenario_objects.cpp), and [Scenario execution](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/scenarioobjects.cpp) establish the Auxiliary startup exception, inclusive ranges, temperature band, amplifier state/volume ordering, and time-versus-Device gates. `testAuxAtStart`, temperature boundary rows, volume range rows, `testDeviceCondition`, `testWeekdayCondition`, and `testTimeDeviceCondition` were checked. Celsius thresholds use stored tenths; Fahrenheit conversion occurs before the same numeric ±10 comparison, so the latter is not a universal ±1 °C physical band. No ScenarioDevices graph schema or universal trigger contract is inferred.

## Multimedia XML boundary

[XML extraction tests](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_xmlclient.cpp), [XML client](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/xmlclient.cpp), [XML device tests](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_xmldevice.cpp), and [XML device implementation](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/xmldevice.cpp) establish the separate UTF-8 envelope and media browsing/selection surface. No `*26*...##` emission or explicit numeric WHO-26 mapping was found there. The exact builder tests contain a stale fixed-SID expectation while the mature builder generates a UUID; tests and implementation therefore do not corroborate a stable SID/reuse contract. SID/PID lifecycle, ACK RC meanings as general contracts, fragmented multibyte correctness and universal XML session support are deliberately excluded. No fixture password, host or developer identity is copied into reader examples.

[Virtual amplifier tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_media_device.cpp), [Virtual amplifier parser](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.cpp), and [Amplifier interface comments](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.h) establish temporary-off recognition and the class's one-second local-interruption description. The matching area/point distinction is exact assertion evidence; the duration is explicitly an implementation description rather than a physical timing guarantee.

## Simulator and fixture boundaries

[Camera executable model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_CAM_DEV_PGIN/btcam_dev.cpp), [Camera configuration](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_CAM_DEV_PGIN/camerastatus.cpp), and [Manual test document](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/TEST/TEST.docx) establish the camera addition. Manual cases 12/13/15 cover activation and switching; the executable constant is 60,000 ms. The file's ACK strings omit canonical delimiters, some collective OFF results incorrectly say yellow, and several PUL collective cases are marked FAIL. They cannot override executable/source/published semantics merely because other rows say OK.

[F520 build description](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F520_DEV_PGIN/bt_F520_DEV_PGIN.pro) compiles the plugin-root implementation. The ten source/build files under `resources/` are older copies; their differences were checked without unioning their branches into a hypothetical F520 capability set. The x6000 removal commit changes simulation speed UI, not an energy unit multiplier.

[Generic-device dispatch](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/bt_gen_dev.cpp), [Generic message worker](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/genmsgworker.cpp), and [Generic XML scenario loader](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/gen_xmlserializer.cpp) show exact-string triggers and scripted response loops/channel/delay choices. Plant/bus plugins forward internal messages through Qt signals. Arbitrary fixture replies and internal IDs remain simulation behavior, not physical Device tests or wire transaction IDs.

## Page changes and corrections

| Existing page | Additional knowledge or qualification |
| --- | --- |
| [Common Addressing](../../protocol/addressing.md) | Tested cross-level/general/local/environment matching and group limitation |
| [Connection and Sessions](../../protocol/sessions.md) | Local request/supervisor selectors; simulator naming discrepancy |
| [Acknowledgements](../../protocol/acknowledgements.md) | FIFO subscriber correlation, batch deduplication and reconnect replay scope |
| [Stream Parsing](../../protocol/stream-parsing.md) | Monitor request-family handling and separate XML framing/envelope |
| [Temperature Control Dimensions](../../functional/who-4-temperature-control/dimensions.md) | Signed probe interpretation, BACnet enums, reset/report and empty/missing distinction |
| [Basic Video Door Entry](../../functional/who-6-basic-video-door-entry/) | Camera simulator selection/timer/image scope and address-range discrepancy |
| [Energy Management Addressing](../../functional/who-18-energy-management/addressing.md) | StopGo fixture-prefix discrepancy alongside canonical `1N` |
| [Sound Diffusion](../../functional/who-22-sound-diffusion/) | Tested virtual-amplifier temporary-off matching |
| [Lighting Dimensions](../../functional/who-1-lighting/dimensions.md) | Collective-command capability-detection boundary |
| [Automation](../../functional/who-2-automation/) | UI category and application-group namespace boundaries |
| [Execution Model](../../scenario-engine/execution-model.md) | Auxiliary initialization exception, predicate and scenario gating |
| [Open Questions](../../reverse-engineering/open-questions.md) | StopGo addressing and external-endpoint compatibility gaps |

The branch changes 25 existing Encyclopedia pages in total: the 21 listed in the [first integration dispositions](myopencommunity-integration.md#integration-dispositions), with the 12 additions or qualifications above overlapping eight of those pages. No new reader-facing page was created.

The first pass's Lighting-specific initialization statement is retained, with the Auxiliary exception made explicit. BACnet write-empty semantics are now qualified by the different report behavior. The public StopGo address table remains a published claim, with contradictory implementation fixtures recorded separately. No published operation is silently replaced by a simulator branch.

## Deliberately excluded and unresolved

- Physical acceptance, full domain, Firmware scope or gateway translation for StopGo `2N`.
- External-gateway support for local channel `0` / supervisor `10`, or a numeric WHO-26 mapping for XML commands.
- Stable XML SID lifecycle inferred from tests contradicted by the mature UUID builder.
- Additional wire operations inferred solely from stale constants, UI categories, unbuilt source copies, or scripted generic-device fixtures.
- Group membership inferred from an interface suffix; expanded Automation collective routing support based on the shared matcher.
- Universal reconnect deadlines, exactly-once replay, simulator camera timeout, physical energy accuracy, or common-libraries' cache/goal policy.
- Broader signed-setpoint domains and universal BACnet units/fault codes without adapter evidence.
- Previously documented remaining tuple/message/routing/generation questions in the [first-pass review](myopencommunity-integration.md#remaining-questions-and-excluded-claims).

The 51 indexed C++ test files and 2,169 assertion sites are not reported as executed suites. Complete legacy builds need unavailable external `common_files`/libcommon/OpenMsg and historical UI dependencies. Qt 5 Core supports the targeted matcher harness; that pass does not substitute for legacy integration or hardware tests.

## Machine KB maintenance

No new atomic claims are extracted. Eleven new documentation sections receive stable identities and deferred-derivation coverage through the established mechanism. The claim inventory remains 7,449. All 177 affected existing assertions retain identical source-block text and materialized statement meaning; their changed digests reflect section structure. They are reviewed and repinned without modifying their assertions or existing IDs. Generated document/chunk freshness is maintained through the normal build.

## Validation

All 25 changed Encyclopedia pages were reviewed with their established neighbors for presentation, canonical placement, duplicate material, frame delimiters/empty fields, and evidence scope. New semantic-review candidates concern explicitly scoped client behavior and reference examples, not an unqualified protocol rule. All 93 pinned archive file/commit references across the two reviews resolve in preserved Git history. The style check verifies local link destinations and heading anchors, including the source inventory.

| Validation | Result |
| --- | --- |
| Source preservation against pinned Git blobs | Pass, all 1,660 tracked entries; zero differences |
| Archived matcher assertion harness | Pass, all 29 assertions from eleven original test bodies; targeted scope only |
| Normal build and `check.py` | Pass, deterministic artifacts, freshness, manifest, schemas, references, consistency, text hygiene and privacy |
| Repository unit suite | Pass, all 59 tests |
| Schema suite | Pass, all eight tests |
| Encyclopedia Style Guide | Pass, zero objective failures; 125 advisory candidates |
| Encyclopedia Core Values | Pass, zero objective failures; 13 contextual-review candidates |
| External artifact manifest | Pass, 144 artifacts |
| Standalone generated-artifact privacy check | Pass, 20 artifact/metadata surfaces |
| Advisory epistemic review | Reviewed; new client choices and simulator behavior remain explicitly scoped |
| Archive references, local links and heading anchors | Pass |
| Complete diff, existing assertion/ID retention and whitespace review | Pass |
| Canonical-source audit | Pass after local archive access was restored; six private fingerprints/sizes verified, five SQLite integrity checks `ok`, no probe failures |

The initial canonical-source audit was blocked by the missing fetch helper. On 2 October 2026, the local archive setup was restored and its missing `rclone` dependency installed. The unchanged audit then retrieved `MHCatalogue.db`, `OPEN.db`, both ScenarioDevices databases, `rules.db3`, and `OpenQuery.txt` through the passwordless-sudo helper outside the execution sandbox. All six files matched the manifest SHA-256 and byte size; all five SQLite integrity results were `ok`; the registry, sequence, timeout, address, configuration, catalogue, scenario, validation and support-query probes completed with zero failures. Private files were materialized in the audit's temporary directory. No source fingerprint, audit rule or archive policy was altered.
