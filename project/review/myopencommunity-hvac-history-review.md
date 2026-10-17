# MyOpenCommunity HVAC and Thermoregulation History Review

This continuation starts at `ec58772c04db38df05c5833e4fae51e1da13c7cc` on `docs/myopencommunity-integration`, following the [energy/PIC review](myopencommunity-energy-history-review.md). The boundary follows retained HVAC, thermal, probe, BACnet and Configuration consumers across the four preserved repositories. Earlier chat examples are context, not a coverage boundary. Preserved sources and synced references remain read-only.

## Bounded history coverage

The [history dispositions](myopencommunity-hvac-history-dispositions.tsv) bind 7,760 changed-file edges to every relevant retained parent, including merges. Independent reconstruction verifies the complete selected parent/path set, 15,520 endpoint tree identities and 2,799 repository/blob identities. The [component dispositions](myopencommunity-hvac-component-dispositions.tsv) bind 5,314 distinct normalized variants to actual source trees, complete-file SHA-256 values, component hashes and comparison identities. The 513 assertion occurrences have macro/ordinal identities and normalized expression hashes, checked against the original enclosing bodies. Each inherits its component's scoped disposition.

| Repository | Selected paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 69 | 4,675 | 1,044 | 1,003 | 1,354 |
| libqtcommon | 8 | 361 | 127 | 122 | 47 |
| BtExperience | 96 | 2,724 | 978 | 939 | 1,398 |
| MyHomeSystemEmulator | No dedicated thermal model established | 0 in this named lineage | 0 | 0 | 0 |

Shared pre-extraction library history is not independent corroboration. The selected paths include earlier/removed locations of thermal/probe/air-conditioning implementations and tests, BACnet classes/tests, shared temperature conversions, BTouch/BtExperience thermal/split objects and tests, removed pages/views/banners and thermal/air-conditioning Configuration fixtures. Factory dispatch is followed into executable constructors rather than inferred from UI category names.

| Review method | Variants | Scope |
| --- | ---: | --- |
| Semantic component comparison | 1,383 | Executable serializers, decoders, assertions and selected cache/consumer transitions; retained bodies compared with a previously read normalized variant |
| Declaration / inline-state comparison | 286 | Core and product enums, signatures, inline state and relevant helper bodies |
| Declaration reference screen | 370 | Removed/UI declarations and numeric/address/WHO references; not complete semantic review of every inline UI method |
| Configuration selector field comparison | 96 | Thermal/central/zone/probe/fan-coil and basic/advanced selection fields; unrelated XML content is outside the verdict |
| Factory dispatch field comparison | 67 | Thermal/split/external-probe cases; unrelated plugin cases are outside the verdict |
| Scope screen | 3,112 | Rendering, layout, lifecycle and other presentation methods outside the wire/state/selection boundary |

There are 2,202 selected executable/field variants and 670 identities present at pinned endpoints. The 3,686 distinct before/after blob pairs are an inventory and reuse mechanism, not a count of fully reviewed whole files. Normalization removes comments and blank indentation and redacts private fixture values; original complete-file hashes remain byte-exact, including non-UTF-8 historical files. Meaningful comments on generation, workarounds and date/duration interpretation were checked separately; comment-only history is not claimed as exhaustively read.

| Disposition | Primary file edges | Primary component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 440 | 53 |
| Corroborates existing scoped documentation | 778 | 456 |
| Excluded with reason | 6,542 | 4,805 |

Intermediate and removed variants are excluded as current/deployed rules while retaining their comparison and correction. Presence in a pinned source tree does not establish selection by its product factory or a physical Firmware generation.

### Removed status-model closure

Old thermal/probe/fan-coil constructors reference generic status-model files whose names do not identify HVAC. The [status history dispositions](myopencommunity-hvac-status-history-dispositions.tsv) cover all 520 changed-file edges and retained parents of their four historical paths. The [status component dispositions](myopencommunity-hvac-status-component-dispositions.tsv) compare 25 distinct thermal constructor/declaration variants, with original blob and normalized body identities independently verified. Other generic status components are outside this thermal closure.

These variants change cache defaults from zero to unset, separate four-zone and 99-zone cache structures, add/remove program/status fields, and retain internal min/max/step values. An intermediate constructor's invalid `OR` guard can reject either expected type. None establishes physical startup values, sensor ranges or a supported Firmware branch. Earlier thermal/probe wire implementations remain covered by the primary component ledger, not inferred from status-field labels.

### Emulator boundary

A content screen of 395 retained source/Configuration/build blobs found no dedicated thermal serializer or decoder lineage. The apparent `*4*` hits are `WHO 30` payloads; string `split` hits are generic parsers. The [built generic device](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/bt_gen_dev.cpp) uses an exact-frame scenario map and configured responses, selected by its [plugin project](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_GEN_DEV_PGIN/bt_GEN_DEV_PGIN.pro). It supplies no independent thermal hardware behavior. Existing generic parser/transport limitations remain in the [transport review](myopencommunity-transport-history-review.md). This screen and dispatch inspection are not full semantic review of every simulator method.

## Pinned source basis

| Repository | Revision | Relevant sources |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Thermal implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/thermal_device.cpp), [thermal assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_thermal_device.cpp), [probe implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/probe_device.cpp), [probe assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_probe_device.cpp), [split implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/airconditioning_device.cpp), [split assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_air_conditioning_device.cpp), [BACnet implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/bacnet_device.cpp), [BACnet assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_bacnet_device.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Shared retained pre-extraction tests and [temperature conversion](https://github.com/OpenWebNet-HA/libqtcommon/blob/825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2/scaleconversion.cpp); identities bound by ledgers |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Thermal Configuration and consumers](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/thermalobjects.cpp), [probe consumers](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/thermalprobes.cpp), [probe product assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_thermalprobes_object.cpp), [advanced split consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/splitadvancedscenario.cpp) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` (VDK 2.0) | Generic dispatch/build boundary above; no new thermal physical model claim |

Component identifiers below refer to the provenance ledger, not protocol identifiers.

## Configuration and address selection

Pinned `parseControlUnit99` / `parseZone99` (`H3059`, `H3058`) construct central `0` and zone `Z`, whose command targets become `#0` and `#Z`. Four-zone `parseControlUnit4` / `parseZone4` (`H3061`, `H3060`) construct central `0#C`, composed zone `Z#C`, and separate simple fan-coil target `Z`. The library prefixes central-scope commands/writes with `#`; fan-coil DIM 11 request/write uses the simple target. Exact probe assertions use composed `23#1` while checking fan-coil frames at `23`. The [Addressing page](../../functional/who-4-temperature-control/addressing.md#historical-central-unit-variants) now gives the operation-specific table.

Older central-prefix construction moved between constructors and writers, and some request paths changed connection selection without changing final wire fields. Old Configuration defines append `00` for external probes; an older temperature-view callback checks only the first address character. Those are client transformations/matching defects, not proof that address forms are universally interchangeable. The existing historical external-address qualification remains.

Basic IR and advanced split factories select separate classes: `WHO 0` configured scenario actions versus `WHO 4` DIM 22. [`WHO 0`](../../functional/who-0-scenarios/README.md#historical-touchscreen-behavior) already documents that distinction and arbitrary `1..31` API assertions. No duplicate namespace rule is added. Mode bitmasks, configured OFF codes, mode/speed availability indexes, sample temperature ranges and UI object IDs do not establish physical capacities or Firmware generations. BACnet classes are not selected by the pinned ordinary thermal/split factory; their existence does not prove deployment on the described 3550/4695 central units.

## Calendar mode sequences

`ThermalDevice::setHolidayDateTime` and `setWeekendDateTime` are verified against exact full concatenated output assertions. Vacation sends `33002#(3100 + program)`, DIM 30 date, then DIM 31 time. Daily holiday sends `315#(3100 + program)`, then the same date/time sequence. The product's final timed-program `apply` delegates to these setters. [Temperature Control Commands](../../functional/who-4-temperature-control/what.md#vacation-program-and-scenario-forms) now states the order and the dummy two-day strategy, linking the existing date/time dimensions.

Tests use program 15 and 12 to exercise arithmetic/serialization. These values do not extend the public program domain. Intermediate holiday/weekday labels and delegation reversals are app corrections, not alternate wire meanings. The holiday report tests store `13004` / `23004` suffix `4` in an internal program slot despite the day-count meaning; that cache convention does not establish weekly program 4. Existing command/report day-count distinctions remain authoritative.

The four-zone timed-manual path still uses a dummy-duration command followed by DIM 32 after a local delay. Earlier QTime/BtTime and empty-body transitions do not settle whether a deployed target interprets the latter as duration or clock deadline. Existing [timed-manual qualification](../../functional/who-4-temperature-control/dimensions.md#historical-timed-manual-dimension-32) remains unchanged.

## Probe state and fan-coil corrections

Exact product assertions traverse plant manual -> local OFF -> local protection -> local normal and expect the displayed state to return to manual. `H3159` and `H3170` preserve separate plant and local state; local override takes precedence without replacing the cached plant state. The product masks its displayed offset outside normal adjustment, including an exact OFF-plus-offset-3 test expecting zero. [DIM 13](../../functional/who-4-temperature-control/dimensions.md#dimension-13---local-set-offset) now distinguishes that client view from physical reset behavior.

Earlier state-precedence corrections, the fan-coil Auto enum/assertion change from 4 to final 0, and request-connection selection are library/app changes. Final exact product and library assertions agree with the already published Auto 0 meaning. No new physical generation is asserted. Existing signed-temperature, DIM 12 offset subtraction, external DIM 15#1, fan-coil and four-zone missing-notification material is corroborated. The historical signed boundary difference at 1000 remains scoped converter behavior.

## Partial split writes and report checking

Pinned `AdvancedAirConditioningDevice::parseFrame` (`H0180`) matches full WHERE and DIM 22, then checks only the first report while a pending write exists. It compares requested nonempty fields only at positions actually supplied by the report, clears the pending record even on mismatch/short input, and emits an error only for a compared mismatch. Exact tests establish zero error signals for a matching partial fan report, one for a dry mismatch, none for the following repeat, and none for unsolicited input. OFF clears the pending check and sends `0***`.

The original helper execution additionally exercises a short tokenized report: omitted requested positions are not checked, and the pending record is consumed. This is the decoder/check policy after classification, not proof that the external OpenMsg classifier accepts every short wire frame. [DIM 22](../../functional/who-4-temperature-control/dimensions.md#historical-partial-split-writes) now qualifies the earlier broad comparison sentence: no positive confirmation, repeated checking, complete-field verification or physical-state guarantee is established.

Earlier missing reply checking, empty OFF/scenario stubs, malformed setpoint prefixes and incomplete refresh terminators are superseded code, not alternate accepted syntax. Variable-width split temperatures and client speed/swing rejection remain implementation choices, not universal hardware acceptance ranges.

## Exclusions and unresolved questions

| Candidate | Disposition |
| --- | --- |
| Repository dates or library revisions identify deployed Firmware generations | Excluded: no capture/release/device mapping |
| UI thermal/HVAC category implies `WHO 4` | Excluded: executable basic IR delegate uses `WHO 0` |
| Fixture program/scenario IDs or min/max fields establish device capacity | Excluded: serializer/API/Configuration policy only |
| Earlier Auto 4 is a supported fan-coil Firmware variant | Excluded: client enum/test correction; final Auto 0 corroborates existing specification |
| Holiday suffix cached as program identifies a weekly program | Excluded: internal cache slot does not override reported day count |
| Short split report proves physical completion | Excluded: helper skips absent positions; classifier/hardware acceptance unresolved |
| Central mode or physical offset resets when local knob overrides the display | Excluded: separate client cache and masked offset do not establish physical reset |
| Generic simulator configured reply corroborates thermal hardware | Excluded: exact-frame script, no dedicated thermal model established |
| BACnet class presence proves selected hardware, scaling or fault codes | Excluded: factory selection and adapter/device evidence absent |
| Malformed/empty removed implementations are alternative wire grammar | Excluded: incomplete or corrected client code |

Captures or hardware are still needed for the exact 4695 Firmware scope of delayed setpoint notifications, physical acceptance of composed addresses/partial split writes, the external report's trailing `1111`, DIM 32 deadline versus duration, BACnet units/fault values and adapter compatibility. The absent external touchscreen stack is needed for classification of malformed/short frames. This bounded lineage review does not claim repository exhaustion or complete UI behavior; unrelated device-description and other functional lineages remain separate work.

## Machine KB maintenance and validation

Four existing coverage sections retain their status/count and record the added scoped client findings as candidates for later atomic extraction. Existing claim statements, source assignments and reviewed supporting blocks/indexes remain unchanged. Maintenance verifies the established explicit context indexes against unchanged supporting blocks and the normal context matcher. New client prose does not displace the official table context of an existing claim. The 116 existing claim section digests refresh; all other claim seed fields and published statements remain unchanged. The corpus retains 7,448 claims and 1,223 chunks. No atomic claims or section/chunk identities are added or redesigned.

| Validation | Result |
| --- | --- |
| Independent primary history reconstruction | Pass: 7,760 edges, 15,520 endpoint tree identities and 2,799 repository/blob identities |
| Primary component and assertion verification | Pass: 5,314 tree/content/body identities and 513 normalized assertion identities; comparison/endpoint references and canonical destinations resolve |
| Removed status-model closure | Pass: 520 edges across four paths and 228 parent comparisons; 25 thermal constructor/declaration identities |
| Targeted archived-helper execution | Pass: 23 comparisons using 23 original bodies with Qt 5 Core and controlled token/output/time seams; basic/advanced writes, calendar order, padding and one-report split checks |
| Execution boundary | External OpenMsg classifier and complete archived Qt/product suites not executed; no hardware validation |
| Normal build and integrity check | Pass: deterministic artifacts, manifest, schemas, references, text hygiene, privacy and cross-artifact consistency |
| Machine-KB unit / schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact / canonical-source audits | Pass: 144 registered artifacts, all 25 fingerprints verified, five database integrity results `ok`, no source-audit failures; established privileged R2 helper used |
| Links / wire examples | Pass: 35 local/anchor targets and 16 public links; changed forms checked against exact assertions and original serializers |
| Style / Core Values checks | No objective failures across 146 reader pages and 41 support pages; 127 pre-existing style candidates and 13 identifier candidates remain advisory |
| Epistemic / neighboring-page review | Changed material remains explicitly client-scoped; published ranges and existing historical qualifications preserved; `WHO 0` material linked rather than duplicated |
| Complete diff / KB impact | Three canonical pages, five provenance records and six KB maintenance inputs/artifacts; 116 claim digests and four coverage reasons change; claim/chunk identities and source contexts retained; no full-KB review flag |

Both scalar/dimension and command/address presentations were compared with their established neighboring pages. The reader-facing additions use existing sections, with one compact address table. No Device description acquires a new compatibility or Firmware claim. Whitespace and staged changes are checked before committing; the branch is pushed without merging. This closes the bounded HVAC lineage, not the entire repository extraction.
