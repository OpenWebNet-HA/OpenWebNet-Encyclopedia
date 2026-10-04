# MyOpenCommunity Alarm-clock History Review

This continuation starts at `5b19a7c9ecbc14c969ae99d602f28007c1dd702b1` on `docs/myopencommunity-integration`, following the [Sound history review](myopencommunity-sound-history-review.md). It covers sound-system wake-up alarms, their local scheduling, sound delegates and direct Configuration consumers. Earlier chat examples are context rather than a discovery boundary. Preserved repositories, retained Git objects and synced sources remain read-only.

## History index and semantic boundary

The [history dispositions](myopencommunity-alarm-clock-history-dispositions.tsv) retain 13,998 changed-file edges against every selected retained parent, including merges. Independent reconstruction verifies 27,996 endpoint tree identities and 5,798 nonempty repository/blob identities. The [component dispositions](myopencommunity-alarm-clock-component-dispositions.tsv) retain exact source-tree revisions, raw whole-file SHA-256, normalized body hashes, assertion identities, comparison references, endpoint presence, review methods and scoped dispositions.

| Repository | Discovered/dependency paths | Changed-file edges | Parent comparisons | Commits | Nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 93 | 10,764 | 3,253 | 2,970 | 4,238 |
| libqtcommon | 6 | 568 | 278 | 269 | 140 |
| BtExperience | 36 | 2,666 | 1,334 | 1,255 | 1,420 |
| MyHomeSystemEmulator | 0 | 0 | 0 | 0 | 0 |

Discovery screens 32,992 retained C++/header, XML, QML, JavaScript and build blobs for AlarmClock, AlarmSoundDiff, alarm_clock, alarm_sound, sveglia and WakeUp identifiers. Matching filenames close over earlier directory locations. Relevant date/time parsers, list-shift utilities, media callbacks and QML cache dependencies are added across their retained paths. No dedicated alarm-clock implementation is identified in the emulator's 395 screened blobs; this does not prove absence of generic dispatch.

| Review method | Component variants | Meaning |
| --- | ---: | --- |
| Full component comparison | 792 | Complete alarm/helper/test bodies; selected legacy scheduler, learning, startup, ramp and stop bodies; direct Configuration, callback, cache, notification, parser and popup dependencies |
| Field screen | 13 | Weekday masks, interval constants and matching declarations; not full header semantic closure |
| Prior semantic review reuse | 235 | Exact basename/name/body identities from the Sound review, with prior component IDs; no independent alarm corroboration |
| Indexed scope only | 1,654 | Discovery/component/assertion identities only; broader UI, factories, declarations and peripheral histories excluded from new claims pending semantic comparison |

The full comparisons contain 235 normalized assertion/check identities; 595 are retained across the whole inventory. The 411 component identities present at pinned endpoints include indexed material. Totals are 103 incorporated, 16 corroborating and 2,575 excluded components, and 113 incorporated, 34 corroborating and 13,851 excluded history edges. These count component dispositions, not atomic facts or extraction completeness. Removed and intermediate bodies are excluded as current/deployed rules even when they establish the historical lineage described below.

All 805 selected full-component/field variants are compared across earlier paths and intermediate revisions, including 297 selected legacy core-method variants and retained popup confirm/dismiss bodies. Whole-file indexing comprises 7,547 endpoint pairs and 546,686 normalized diff lines; it is not full semantic coverage. Normalization removes comments/blank indentation and redacts private fixtures, while raw hashes preserve original bytes. Comparison references identify previously encountered same-name/basename variants, not necessarily parents; actual retained-parent edges are recorded separately. No compact-view equivalence is used to certify an unread body. Shared ancestry is not independent evidence.

This closes the stated alarm-control/scheduler and direct-consumer boundary. It does not close all indexed UI/declarations, the complete playback backend, equalizer/preset lifecycle, external OpenMsg parsing or every repository component, and does not claim repository exhaustion.

## Sources and canonical placement

| Repository | Revision | Relevant source |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Alarm sound helper](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.cpp), [constants/API](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/media_device.h), [exact helper assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_media_device.cpp), [date/time parser](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/platform_device.cpp) |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Alarm scheduler and Configuration](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/alarmclock.cpp), [exact alarm assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_alarm_clock.cpp), [source/amplifier delegates](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/mediaobjects.cpp), [cache](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/qmlcache.cpp), [popup dispatch](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/gui/skins/default/js/popup.js) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Historical copied alarm-helper tests indexed and compared; no independent scheduler or dialect |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | No dedicated alarm model within the discovery screen; generic configured dispatch remains separate |

[Sound Diffusion](../../functional/who-22-sound-diffusion/) gains the exact dimension-6 station-write form, a compact historical alarm-control table and playback/fallback qualifications. [Sound System](../../functional/who-16-sound-system/) gains a scoped alarm-client mixed-dialect qualification beside its existing mixed-client discussion. [Scenario execution model](../../scenario-engine/execution-model.md) gains the separate alarm scheduler, weekday mask, one-shot and Configuration behavior. Advanced-scenario weekday order remains unchanged. No new reader-facing page or Practical Guide is needed; ordinary sound writers and captured routing remain on their existing canonical pages.

## Exact assertions and executable behavior

Pinned helper assertions `A0201..A0210` check source 7, station 33 and selected amplifiers, including the dimension-6 station write, initial volume 8, Follow Me, stop frames and learning updates. The start test counts seven frames and checks membership, not order. Startup order comes from the executable helper: source area 0, optional nonzero radio station, ascending selected amplifier indices, one multichannel source selection per encountered area 1..8, raw initial value below 10 or 8 otherwise, then Follow Me. Negative stored values exclude amplifiers. Stop ignores its source argument and turns off selected amplifiers. Source/station/count fixtures do not establish product domains.

The helper's learning gate records OFF as inactive and volume receipt as an active learned amplifier/value; ON is not the same learning branch. Registered-source availability and selected amplifier settings determine local isValid; station validity or physical playback is not checked. These are alarm-learning/cache policies, not general power semantics or hardware validation.

BtExperience assertions `A2224..A2231` distinguish timer start from the first sound tick, exact single-amplifier source/volume-zero/ON order, the ramp, snooze, restart and expiry. `A2230` expects levels `i-1` for ticks 1..8 at a 25% target, then no command at ticks 9/10. The comment claiming a target of 8 is weaker evidence and is not adopted. The two integer conversions explain the sequence: `t*100/31` percent, then `P*31/100` wire volume, with the configured percentage as a gate rather than a final exact-volume write.

`A2124..A2125` and popup `A2286..A2287` establish that explicit Stop only stops timers, while snooze sends OFF and starts a 5-minute timer. `A2142` sends OFF at the final sound tick; the nominal sound interval is 2 minutes. Earlier helper Stop does send OFF. No universal Stop behavior or preceding source/volume restoration is inferred. Ringing is timer activity, without physical playback confirmation or an acknowledgement check in the alarm controller.

`A2119..A2121` establish local-time scheduling, timeout weekday gating, one-shot disable for mask zero and the nominal 30-minute restart window. Constants reverse the advanced-scenario mask: Monday bit 6, Sunday bit 0. Scheduling checks enabled state; direct triggers do not. The next candidate is today at the configured time or tomorrow if already reached, followed by weekday checks at timeout. Date/time notifications cause local-clock recalculation rather than adopting their payload. Restart uses time-of-day seconds without a date/lower-bound guard, so midnight and clock-change correctness are not established.

`A2111..A2112` resolve positive amplifier_uii as application Object IDs, choose the first configured source of type Aux/RDS/IP/SD/USB, multiply stored volume by 10 and truncate on save by dividing by 10. These are client Configuration conventions, not bus address or alarm protocol fields. Editable time/weekdays emit change notifications and rearm before Save; cache Reset emits changes and recalculates too. The advanced-scenario Reset qualification must not be copied onto this scheduler.

`A2143` switches actual running type to beep after a false first-content callback, turns the amplifier OFF and restarts with a 5-second beep interval; configured type remains unchanged and callbacks received while not ringing are ignored. IP-radio first-content status checks configured playlist availability, not network playback. Local-media completion `A2197` dereferences its termination pointer after deletion in the retained body; reliable USB/SD completion cannot be certified from it. Notifier configured-type state is not proof that fallback display or audible playback succeeds.

## Historical corrections and exclusions

The compared lineage includes early sveglia WHO 16 serializers (source, station dimension 7, environment routing, raw starting/ramped volume), mixed WHO 22 routing with WHO 16 amplifier control, WHO 22 helper delegation and the later BtExperience controller. Earlier minute-polling windows, weekday/weekend enums, NVRAM/audio-state learning, selection sentinels and local beep/display restoration differ from the pinned scheduler. These establish client revisions, not physical Firmware generations or bus audio restoration.

Actual-parent corrections include [percentage ramp and exact tests](https://github.com/OpenWebNet-HA/BtExperience/commit/8eedd27ea62b8e16c6dcfa4cef0466495ada925f), [snooze OFF and missing-amplifier guard](https://github.com/OpenWebNet-HA/BtExperience/commit/e5aa10fffdb1b8245307214b255bb20398fc323d), [date/time recalculation](https://github.com/OpenWebNet-HA/BtExperience/commit/b02a41e55e64fafed3735c2ef1bd6b3dda1c0932), and [10-point UI volume steps](https://github.com/OpenWebNet-HA/BtExperience/commit/516943e692181858c73fe44dfcaf55c0e02a7d03). The library's [initial day-list shift](https://github.com/OpenWebNet-HA/libqtdevices/commit/3fd4362b7c851ee05b1bdc26e7437804681898cf) and [removal](https://github.com/OpenWebNet-HA/libqtdevices/commit/3e64783040d67134c7b160b9f04c47efeb606446) are compared with intermediate implementations; configuration-alignment comments do not establish a deployed Firmware boundary. Earlier malformed routing separators and raw address-offset corrections remain intermediate emission history; canonical syntax follows corrected writers/tests.

| Candidate | Disposition |
| --- | --- |
| Weekday flags have one universal application ordering | Excluded: alarm and advanced-scenario masks differ |
| Explicit Stop universally sends OFF or restores earlier audio | Excluded: compared stop methods differ; no bus source/volume snapshot restoration |
| 25% ramp reaches 8 because the comment says so | Corrected against exact assertions and integer execution: tested sequence reaches 7 |
| Alarm initialization is atomic, inspects ACK, or confirms sound | Excluded: local sequential dispatch and timer state only |
| Every USB/SD search or failed stream reliably falls back to beep | Excluded: availability callback differs from playback; unsafe local completion and backend scope remain |
| Stored amplifier reference, volume, fixture station/counts define wire domains | Excluded: client Configuration and test fixtures |
| isValid proves a playable station or selected hardware | Excluded: registered-source/selection check only |
| Calendar, DST, missed-event, duplicate-trigger or midnight behavior is guaranteed | Excluded: local-time/timer implementation without those guarantees |
| Source dates, namespace migration or day-shift comments identify Firmware generations | Excluded: no product/deployment mapping |
| Retained copied tests provide independent corroboration | Excluded: shared ancestry and exact-body reuse are explicit |
| All indexed peripheral UI/player paths are semantically closed | Excluded: indexed-only dispositions preserved |

Captures/hardware remain necessary for deployed client/Firmware applicability, audible playback and physical effects after Stop/snooze/expiry. Source/runtime investigation remains possible for complete backend failure propagation, asynchronous search lifetime, actual timer/event-loop and calendar behavior, and broader indexed UI/equalizer/preset paths. These are distinct evidence gaps.

## Machine KB maintenance and validation

All 7,448 retained claim identities, statements, metadata and supporting blocks remain unchanged; 16 final section digests are refreshed and no context indexes shift. Two new section and chunk identities are allocated through existing registries, retaining prior identities (1,225 current chunks). Their coverage records explicitly defer candidate atomic extraction. No new atomic claims or KB redesign is performed.

A Qt 5 Core harness compiles 26 original method bodies and passes 32 comparisons covering startup order, double-truncated ramp, Stop/snooze/expiry, restart, fallback, weekday masks, one-shot disable, local-clock recalculation and helper ordering/selection. Timers, signals and delegates are controlled seams; Qt supplies the local clock. This does not run the complete archived suites, real elapsed event-loop timing, transport, external parsing, player backends or hardware, and does not prove history exhaustion.

| Validation | Result |
| --- | --- |
| Independent retained-history reconstruction | Pass: 13,998 edges, 27,996 endpoint tree identities, 5,798 nonempty repository/blob identities |
| Component/assertion provenance | Pass: 2,694 source tree/content/body identities and 595 assertion identities; inventory distinguished from semantic coverage |
| Bindings and reused scope | Pass: all history/component bindings and destinations, comparison references and 235 prior exact-body references |
| Targeted original-body execution | Pass: 32 comparisons across 26 original bodies; controlled seams and limits stated above |
| Machine-KB unit/schema suites | Pass: 59 unit tests and eight schema tests; expected negative privacy fixtures rejected |
| Normal build and deterministic integrity | Pass: freshness, schemas, references, manifest, privacy and cross-artifact consistency |
| Artifact/canonical-source audits | Pass: 144 registered artifacts, 25 verified fingerprints, five database integrity results `ok`, no audit failures; authorized privileged R2 helper used |
| Links and wire examples | Pass: 36 local/anchor targets and 17 public source links; added frame checked against exact original assertions and writer |
| Style/Core Values and epistemic review | No objective failures; existing advisory candidates retained; scope and presentation compared with neighboring sound/matrix/UPnP and scenario pages |
| Complete diff and Machine-KB impact | Three canonical pages, three provenance records, ten KB maintenance inputs/artifacts and three coverage-test fixtures; retained claim statements/evidence/context unchanged |

The initial unit run found three stale fixed-count expectations after adding the two nonclaim sections/chunks. Expected retrieval totals and functional/scenario section counts are updated, preserving exact assertions and all claim totals. Change-impact flags identity-file edits for full review: the two section/chunk allocations, retained assignments, registry entries, coverage records, unchanged claims/context and generated differences are explicitly reviewed. No check is bypassed. The initial public-link attempt lacked sandbox DNS access; the authorized external retry passes.

The complete diff and staged contents are reviewed for duplication, unsupported generalization, canonical syntax, privacy, presentation and source immutability. Existing published tables, advanced-scenario semantics and captured matrix routing are preserved. The bounded review and pending indexed/backend coverage remain explicit above.
