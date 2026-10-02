# MyOpenCommunity Integration Review

This record traces documentation additions to the preserved MyOpenCommunity repositories. The earlier repository-recovery findings were retrieved from the supplied conversation history, including later corrections to earlier provisional conclusions. Claims were then checked against the preserved source, exact test assertions, and relevant history before integration. Conversation summaries are discovery aids, not independent protocol evidence.

Branch: `docs/myopencommunity-integration`. Starting revision: `ded12800d30f5d7dbf743b3d8c53750202a577f7`. No source archive or synced `sources/` file was changed.

The subsequent [Source Reassessment](myopencommunity-reassessment.md) expands coverage from the four source trees independently of the conversation findings, records a complete tracked-file inventory, and integrates additional omissions and contradictions. This first-pass record is not an assertion of exhaustive repository-history review.

## Evidence scope

| Preserved repository | Inspected revision | Role |
| --- | --- | --- |
| [BtExperience archive](https://github.com/OpenWebNet-HA/BtExperience) | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` (`TS10_1_0_23`) | Product object layer, build composition, alarm/message/call tests |
| [Device library archive](https://github.com/OpenWebNet-HA/libqtdevices) | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | Exact frame tests, device behavior, and pre-split history |
| [Common library archive](https://github.com/OpenWebNet-HA/libqtcommon) | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` (`TS10_1_0_23`) | Condition evaluation and shared application abstractions |
| [VDK simulator archive](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator) | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | F411, F422, F520, F454 simulation and parser limitations |

The historical BTouch snapshot used for matrix evidence is `79e92d2d43bd893ce9af5f3234b75830144c7aca` in the device-library archive, dated 25 February 2008. The similarly dated common-library commit preserves a different extracted tree; commit hashes and paths were checked rather than copied from earlier summaries.

The [product build composition](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/btobjects.pri) directly compiles the device/common libraries. Agreement between these components is product-use corroboration, not independent implementations of the protocol. VDK identity is supported by the [VDK 2.0 installer definition](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_MyOpenBag_Scripts/MyOpenSimulatorSetup.iss); simulator behavior remains separately scoped.

Evidence order is exact tests/assertions, executable behavior, comments/identifiers, then inference. Historical tests were inspected, not executed against hardware or rebuilt with their unavailable legacy dependencies. Documentation validation is recorded separately below.

## Frame families and parsing

| Evidence | Verified result / disposition |
| --- | --- |
| [frame constructors](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_functions.cpp) and [client dispatch](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_classes.cpp) | Command, status-request, dimension-request, and dimension-write forms confirm existing Frame Syntax. The helpers' argument named `what` can contain a dimension/value string; no field redefinition. Parser guidance cross-reference added without repeating the grammar. |
| [VDK parser and serializer](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/libplant/openmsg.cpp) | Multiple dimension values are serialized with successive `*` delimiters. `SkipEmptyParts` and the broad “diagnostics” label are implementation limitations, explicitly excluded from grammar. |

## Lighting and automation

[Lighting tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_lighting_device.cpp) (`receiveInvalidVariableTiming`, fine-level and increment/decrement tests) and [Lighting decoder](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/lighting_device.cpp) establish ignored `255*255*255` timer state. Existing level offset `100`, speed, four-field writes, and ordinary/advanced dimmer distinctions were confirmed. [Automation tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_automation_device.cpp) confirm up `1`, down `2`, stop `0`; no inversion by Firmware is established.

The ordinary-dimmer 75% example versus Dimmer100 175 emission describes coarse UI quantization, not a revised percentage table. Early `WHAT 1000#...` compatibility parsing, 4-second/9-second pull timings, and the 18-second pulse default are not promoted to general protocol rules.

## StopGo

[StopGo tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_stopandgo_device.cpp) (`sendOpen`, `sendClose`, self-test/tracking controls, frequency and single-bit tests), [StopGo implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/stopandgo_device.cpp), and [StopGo interval domain](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/stopandgo_device.h) establish `21` open, `22` close, `23/24`, `28/29`, dimension `212` read/write, and `1..180` days. All thirteen status-mask bits were compared against the existing published `b13..b1` table.

[Open/close correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/90b31a3e21ba3bf3c93d0fafd11c11a44fd74bb6) and [Mask-order correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/e00dda2997537651e688d0fc745006fcb6828ec9) supersede the earlier reversed labels. Scheduled/compressed status reads are client policy. Early dimension constants `21..29`, `210`, `211`, `213`, `214`, and `WHAT 25` are excluded from a reference registry: declarations and conflicting names alone do not establish operative payloads or support.

## Energy generations and measurements

[Energy frame and value tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_energy_device.cpp) and [Energy implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/energy_device.cpp) establish:

- exact older/newer request pairs and old-PIC alternatives in `sendRequest...OldPic` tests;
- `platformValueReceived` uses the first PIC value with cutoff `<= 22`, independently of `has_new_frames`;
- modes `1..5` map to update types `1,4,2,4,3`; tests cover all start/stop forms with `255`/`0`;
- `113`, `1134`, `1130`, and executable mode-5 `1132` current reads;
- threshold state/value tests establish `516` four-field order and `517#1/#2` read/write syntax;
- legacy byte graphs, scaling factor 100 only for electricity, pair assembly across frames, and sentinel substitutions;
- newer tagged `511..514` series, calendar filtering, prior-year selection, and resubmission after capability detection;
- 10-second fallback polling and single-connection graph dispatch are library behavior.

`receiveCumulativeMonthGraph` specifically proves `(3,255)` is a valid pair; only `(255,255)` is unavailable in paired decoding. Scalar `4294967295` becomes zero in the application's cache, not a universal physical zero. The source's “dUnits” comment is broader than the executable mode-specific multiplier and was qualified accordingly. Its watt/litre/dm³/calorie unit labels are retained as source-comment evidence, without correcting published energy/power terminology or asserting physical integration units.

[Load tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_loads_device.cpp) and [Load decoder](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/loads_device.cpp) corroborate six-field `71`, `72#N` energy/reset timestamp, and the scalar sentinel. Forcing API names are not protocol names: `forceOn()` emits `74` (end forcing), `forceOff(150)` emits `73#15`, and `enable()` emits `73` rather than published `71`. The latter behavior has a TODO and is not used to redefine actuator enable/force semantics. Existing published ten-minute encoding remains canonical.

The application constructs a rolling twelve-month yearly display from `53` and `52#Y#M`; dimension `51` remains all-time. Missing-byte substitution, calculated average denominators, frame-order assumptions, and lack of late-frame recovery do not establish Device guarantees.

## Alarm controls and events

[Alarm tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_antintrusion_device.cpp) and [Alarm implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/antintrusion_device.cpp) establish `36#PASSWORD`, `50#PASSWORD#MASK`, central target `0`, left-to-right eight-zone mask, and source-validation domains. [Product alarm state handling](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/antintrusionsystem.cpp) and [Product alarm tests](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_antintrusion_object.cpp) corroborate these distinctions and eventual-state password feedback. The 6-second then 5-second sequence is application timing, not a protocol deadline. No password format, accepted-password acknowledgement, or security policy is inferred.

The historical `impanti_device` WHO-16 constructor is a stale inconsistency: its operative WHO-5 handlers and frames do not support a hidden sound-system alarm dialect.

## Video door entry and messaging

[Call and camera tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_videodoorentry_device.cpp), [Call state machine](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/videodoorentry_device.cpp), and [Call identifiers](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/videodoorentry_device.h) establish the call/answer/end syntax, literal `4` end prefix, SCS/IP readiness, caller handling, kinds, movable-camera test, locks, stairs, pager, teleloop, and multimedia events. `MMTYPE 2/4` is tested; end `3` is executable stop-video handling. The fallback for other types is not a complete enum. [Product call handling](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/vct.cpp) and [Product call tests](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_videodoorentry_objects.cpp) establish the 11-second local association timer and product use, not an independent protocol timeout.

[Message tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_message_device.cpp) (`testChecksum`, `testParseMessage`, reply writers, complete/bad-checksum transactions), [Message receiver](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/message_device.cpp), and [Message timer](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/message_device.h) establish transaction stages, opposite address direction, decimal character values, timestamp delimiters, checksum vector, reject/cleanup, and 5-second timer. The checksum high byte is length plus the weighted byte sum; the low byte is one plus the byte sum, each modulo 256, with the source's exact indexing. Reader-facing examples preserve the unknown parameter-block fields. [Messaging timeout/address correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/408251372dfc70aff212498904f99d165c820c72) supersedes the stale 3-second comment and optional level-8 address layout. [Rejected-message end correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/0873f2d387b56a82cd6e9935153f615753679add) prevents later publication of a bad-checksum message.

[Product message system](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/messagessystem.cpp) confirms application consumption. Guard Unit traffic is under WHO 8; it is not moved to the unrelated WHO-12 namespace.

## Platform properties and ordering

[Platform exact tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_platform_device.cpp) and [Platform implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/platform_device.cpp) establish LAN `9`, first-field PIC `20`, gateway/DNS `50..52`, empty-WHERE reads, clock-write empties, and fixed weekday `00`. They do not establish F454/MH202 support or the latter two PIC fields. Clock schemas remain the published forms; client emissions are separately labelled.

The LAN writer uses immediate dispatch then a 1-second delayed request; [Connection dispatch](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/frame_classes.cpp) and the energy request strategy corroborate absence of global cross-connection ordering. [Immediate platform dispatch correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/933e8afbfe3f405d5b0276445828745e6436c137) and [Fan-coil ordering correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/9434c885f2f481cdc0454c09a980cb3f6b0ab2e4) retain historical provenance. Earlier TouchX startup failures are not promoted into current gateway defect claims.

## Temperature control

| Evidence | Integrated result / boundary |
| --- | --- |
| [Probe tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_probe_device.cpp) and [Probe implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/probe_device.cpp) | External `15#1`, report field positions and unknown `1111`; four-zone composite addresses; 10-second missing-setpoint workaround. |
| [Central-unit tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_thermal_device.cpp) and [Central-unit implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/thermal_device.cpp) | Existing mode/holiday/manual grammar corroborated; dimension `32` two-field duration handling and 200 ms four-zone write sequence added, with end-time terminology ambiguity retained. |
| [Split tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_air_conditioning_device.cpp) and [Split writer](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/airconditioning_device.cpp) | Empty partial-write positions, fan/dehumidification and OFF forms, comparison of supplied fields only. |
| [BACnet record tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_bacnet_device.cpp), [BACnet serializers/decoders](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/bacnet_device.cpp), and [BACnet enums](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/bacnet_device.h) | WHO-4 dimensions 50..53, ordered write/report records, partial writes, internal -1 sentinel, status/mode domains. No adapter model/Firmware or universal scaling inferred. |
| [Historical central-type declaration](https://github.com/OpenWebNet-HA/libqtdevices/blob/79e92d2d43bd893ce9af5f3234b75830144c7aca/items.h) and [Four-zone notification workaround](https://github.com/OpenWebNet-HA/libqtdevices/commit/3ade09cf4a3ff7fb905a4a46dacb7c30cfa03b1a) | 3550/4695 distinction and historical addresses scoped to product source; affected Firmware revisions unknown. |

The two-day holiday setup followed by explicit date/time writes is an application sequence, not an alternative published vacation-count interpretation. Historical probe throttling intervals, rapid-write compression, and corrected fan-field indexing do not alter canonical value tables.

## Sound dialects and matrix state

[Historical matrix decoder](https://github.com/OpenWebNet-HA/libqtdevices/blob/79e92d2d43bd893ce9af5f3234b75830144c7aca/frame_interpreter.cpp), [Eight-environment four-source model](https://github.com/OpenWebNet-HA/libqtdevices/blob/79e92d2d43bd893ce9af5f3234b75830144c7aca/device.cpp), and [Alarm-clock routing emitter](https://github.com/OpenWebNet-HA/libqtdevices/blob/79e92d2d43bd893ce9af5f3234b75830144c7aca/sveglia.cpp) establish both receipt and emission of WHO-16 `1ES`, normalization to `10S`, and the eight-value `1000/11` state read. No evidence for base-band routing, `#E`, source 5..9, or environment 9 was promoted. The current capture-derived reference is extended, and its claim range is bounded to demonstrated environments `1..8`.

[Matrix dialect correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/66ff93636979fa4b7f7a9ac3593da51b3a6e81c1) verifies the September 2009 removal of the WHO-16 routing decoder. Operation-specific hybrid clients qualify the dual-dialect origin question without resolving the MH200N capture origin.

[Media exact tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_media_device.cpp) and [Media serializers/decoders](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.cpp) establish speaker power/volume, preset 55/56 syntax, RDS 31/32 and decimal text, automatic/manual tuning, area/general rendering, sixteen active-area flags, UI tone/balance/preset conversions, and private `7/#15` initialization. `createMediaInitFrame` and its four exact assertions support all exposed flags and empty positions; constants `9*9` remain unknown. The [May 2010 initialization tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/c4c72360b2983905a18b33ed48f6c70b31afce79/devices/test/test_media_device.cpp) preserve earlier empty-source and monochannel amplifier layouts; older setup payloads are not made interchangeable. Published tone-response errors and WHAT-21 semantics remain unresolved.

## Transversal functions

[ScenarioPlus controls](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/scenario_device.cpp) establishes WHO-25 `11#0`, `12`, `13#0#5`, `14#0#5`, `15`. [Step correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/34da414f84b15a18964e134b7496ccb2db81ecf4) changes 1 to 5; the parameter's complete domain and ScenarioPlus address domain remain unconfirmed. [Contact tests](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_automation_device.cpp) and [Contact-state correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/abd28f2e190be5f46e0deaff12feb97fdba2a633) establish contact 31 closed / 32 open. IR semantics remain independently published.

WHO-0 scenario programming, locking and delete tests corroborate the existing reference. The library allows scenario indices up to 31; that API/assertion domain does not expand product-specific F420/3456 capabilities. WHO-17 scenario controls and WHO-9 auxiliary state already belong in their canonical pages and were not duplicated.

## Simulator models

| Evidence | Integrated result / excluded generalization |
| --- | --- |
| [F411 behavior](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F411_DEV_PGIN/btf411dev.cpp) and [F411 configuration serialization](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F411_DEV_PGIN/f411xmlserializer.cpp) | Per-output A/PL/group and Device mode/bus; click status and PUL filtering. Output records are not equated with catalogue Modules. Any-WHAT-except-1 OFF is a simplified decoder, not protocol semantics. |
| [F422 routing](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F422_DEV_PGIN/btf422_dev.cpp) | Matching non-general qualified traffic strips/re-adds local-bus routing; feedback stays unqualified. General forwarding precedes interface checks; group/empty splitting and narrow configurator domains are not hardware rules. |
| [F520 energy model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F520_DEV_PGIN/btf520_dev.cpp) | Scalar/history mappings corroborate existing grammar. File data, fixed year 13, and stubbed 72/75 do not establish physical F520 support, accuracy or Firmware limits. The internal dimension-0 switch is empty-string numeric conversion of a write marker in `#1200#Type`, not a new dimension. |
| [F454 gateway model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_own_GTW_PGIN/btowngtw.cpp) | F454 resource identity, TCP/HTTP/HTTPS surfaces and 500 ms fallback behavior; internal IDs do not add wire transaction IDs. HTTP/image behavior is simulator transport plumbing, not new OpenWebNet vocabulary. |

## Application condition evaluation

[Condition transition tests](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/test/test_scenevodevicescond.cpp) and [Condition evaluator](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scenevodevicescond.cpp) establish initialization suppression, false-to-true notification, repeated-state suppression, and changed-condition reinitialization. Added to Execution Model as a distinct touchscreen implementation, without inferring MyHOME Suite runtime or matching-ID behavior. Shared XML clients, media wrappers, scale conversions, and UI identifiers remain application infrastructure rather than new OWN registries.

## Integration dispositions

| Encyclopedia page | Substantive addition / correction |
| --- | --- |
| [Functional Source Coverage](../../functional/source-coverage.md) | Historical implementation source class and navigation to the scoped additions |
| [Lighting Dimensions](../../functional/who-1-lighting/dimensions.md) | Historical invalid timer payload |
| [Alarm Protocol](../../functional/who-5-alarm/protocol.md) | Password controls, textual zone mask, eventual-state timing |
| [Alarm Addressing](../../functional/who-5-alarm/addressing.md) | Tested event-source domains |
| [Video Door Entry and Telephony](../../functional/who-8-video-door-entry-telephony/) | Call/camera/teleloop and Guard Unit message model; corrected namespace-only decoder advice |
| [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md) | Platform properties, PIC first field, clock variants; qualified previous DIM20 absence statement |
| [Sound System](../../functional/who-16-sound-system/) | Historical routing provenance, matrix read and mixed-dialect behavior |
| [Energy Commands](../../functional/who-18-energy-management/what.md) | StopGo controls and independent graph/PIC compatibility matrix |
| [Energy Dimensions](../../functional/who-18-energy-management/dimensions.md) | Self-test interval, measurement/update selectors, thresholds, legacy decoding and F520 simulation scope |
| [Sound Diffusion](../../functional/who-22-sound-diffusion/) | Tested corrections, activity/RDS, UI conversions and private setup |
| [Transversal Functions](../../functional/who-25-transversal/) | Separate historical ScenarioPlus family |
| [Dry Contact and IR](../../functional/who-25-transversal/dry-contact-ir.md) | Corrected historical contact interpretation |
| [Temperature Control Addressing](../../functional/who-4-temperature-control/addressing.md) | Central generation and notification workaround |
| [Temperature Control Dimensions](../../functional/who-4-temperature-control/dimensions.md) | External probe, partial split, timed-manual and BACnet records |
| [Addressing](../../protocol/addressing.md) | F422 local-bus boundary evidence and model limitations |
| [Acknowledgements](../../protocol/acknowledgements.md) | Cross-connection ordering and F454 simulator fallback |
| [Stream Parsing](../../protocol/stream-parsing.md) | Constructor corroboration and parser limitations |
| [Configuration](../../device-model/configuration.md) | F411 output configuration model and scope |
| [Execution Model](../../scenario-engine/execution-model.md) | Common-library condition transition behavior |
| [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md) | Added source emitter/decoder evidence and bounded environment range |
| [Open Questions](../../reverse-engineering/open-questions.md) | Replaced obsolete DIM20/routing provenance gaps with narrower questions |

## Remaining questions and excluded claims

The functional sections retain unresolved fields locally: full PIC tuple and external-gateway applicability; WHO-13 dimension 40; external-probe trailing data; timed-manual absolute-end versus duration terminology; BACnet units/fault codes and adapter applicability; WHO-8 complete address domains/message parameters; initialization constants and read support; sound base-band/group/environment-9/source-5..9 routing; origin of paired MH200N reports; precise Firmware revisions behind historical workarounds.

No source-backed change is made to general Automation direction, alarm security guarantees, universal device capabilities, simulator precision, or diagnostic/programming field correlations. Obsolete contradictory source labels are superseded by their fixes, not presented as competing protocol variants. Repository preservation, installer recovery, developer identities, packaging and UI scaffolding are not reader-facing protocol facts.

## Machine KB boundary

No new atomic-claim extraction or Machine KB redesign is undertaken. The current repository has curated claims and explicit section coverage, rather than a separate candidate-claim queue. Confirmed additions and unresolved boundaries above are available for a subsequent atomic derivation pass. Normal freshness maintenance updates document/section/chunk identities and the generated documentation corpus; new sections are explicitly marked as not yet materialized into atomic claims. Existing assertions affected by corrected prose are reviewed and qualified rather than merely repinned. Existing IDs are retained.

The claim inventory remains 7,449. Thirty-five new sections receive section/chunk identities and deferred-derivation coverage entries. Review of 444 affected assertions distinguishes 427 digest-only changes from 15 revised assertions and two changed materialized contexts. The existing DIM20 question is narrowed to payload and gateway applicability. No existing document, section, chunk, claim, or lifecycle identity is removed or reassigned. Existing inventory assertions in three test files account for the 35 additions: retrieval totals 1,208 entries (previously 1,173), with the corresponding section and deferred-derivation counts in each affected domain.

The full impact review includes the changed documents and their transitive records. Generated changes are confined to the documentation corpus, retrieval chunks, the reviewed assertions/question, lifecycle additions, and manifest freshness. Namespace, entity, relationship, glossary, caution, and source registries are unchanged.

## Validation

The final human-page and generated-artifact diff review checks scope, duplicate reference material, and lossless frame syntax. The new sound-dialect/decoder advisory candidates are explicitly implementation-scoped; repeated frame/range candidates retain canonical reference or corroboration context. All 64 pinned archive file/commit links resolve in the preserved Git histories; the style check verifies local destinations and heading anchors.

The canonical-source audit cannot complete in this environment: `/usr/local/sbin/openwebnet-r2-data-fetch` is unavailable. It cannot retrieve the existing private-archive copies of `MHCatalogue.db`, `OPEN.db`, both ScenarioDevices databases, `rules.db3`, or `OpenQuery.txt`, so their fresh fingerprint/integrity checks remain unverified. The external artifact manifest passes its own verification. No audit rule, source fingerprint, or archive policy is changed to hide this limitation.

| Validation | Result |
| --- | --- |
| Validation-script compilation | Pass, all five scripts used by the compliance workflow |
| Encyclopedia Style Guide | Pass, zero objective failures; 125 advisory candidates |
| Encyclopedia Core Values | Pass, zero objective failures; 13 contextual-review candidates |
| External artifact manifest | Pass, 144 artifacts |
| Normal build and `check.py` | Pass, deterministic rebuilds, freshness, manifest, schemas, references, cross-artifact consistency, text hygiene, and privacy |
| Unit suite | Pass, all 59 tests after inventory expectations were updated |
| Schema suite | Pass, all eight tests |
| Standalone generated-artifact privacy check | Pass, 20 artifact/metadata surfaces |
| Advisory epistemic review | Reviewed against baseline and source; no new unqualified protocol promotion |
| Local links, heading anchors, pinned archive references | Pass |
| Complete diff, stable-ID retention, and whitespace review | Pass |
| Canonical-source audit | Incomplete/failing because the configured private-archive fetch helper is unavailable, as detailed above |

Historical Qt assertions were inspected as evidence, not reported as rebuilt or hardware-executed tests. The source-audit limitation remains a separate prerequisite for a fully passing source-integrity run.
