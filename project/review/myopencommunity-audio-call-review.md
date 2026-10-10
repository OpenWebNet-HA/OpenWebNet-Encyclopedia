# MyOpenCommunity Local Audio and Call Review

This phase starts at `af601f0f0546f8545b45b3d5a3fe762ebb7741ad` on `docs/myopencommunity-integration`. It follows the older audio graph and remaining call/UI avenue in the [video/runtime review](myopencommunity-video-runtime-review.md). Preserved repositories and synced sources remain read-only. The boundary is local audio arbitration and its call consumers, not repository exhaustion or a complete historical Qt application certification.

## Sources and examination boundary

The four preserved mirrors retain the earlier pins: BtExperience `b88cdac9665d28494f19d6a5d759acf8d5f00ad9`, libqtcommon `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2`, libqtdevices `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) and MyHomeSystemEmulator `4f93f44ee5ec7f89a3de9e040141755c847a5eda`. The older TS10 application/library tree at libqtdevices `13f0c2049666d234e9cd4b0396863da01636d0f5` supplies the explicitly revision-scoped historical graph, build and consumer findings. Historical UI consumers hosted in that repository remain client evidence, distinct from its library graph.

The [parent ledger](myopencommunity-audio-call-history-dispositions.tsv) compares selected files against every retained parent, including merges, earlier locations and removals. The [component ledger](myopencommunity-audio-call-component-dispositions.tsv) distinguishes complete method/handler comparisons, exact prior reviewed-body reuse, pinned-only inspection and indexed-only pending material. QML block and single-line handlers are parsed separately from C++ methods. Original raw file/component hashes and locations are retained; normalized hashes remove comments/spacing but preserve literals. Comparison adjacency is not chronology, and copied common/devices history is not independent corroboration. A basename screen finding no emulator file does not establish absence of generic simulator dispatch.

Complete AudioStateMachine graph/method variants, generic StateMachine variants, both ringtone-manager lineages, and selected call activation/deactivation, pager-start, grabber, delayed-answer and cached-property variants are compared. Current AudioState remaining variants are compared, with exact normalized-body reuse of the previously compared methods. Selected QML answer/end/ringtone/floor/pager/mute/volume/grabber handlers are compared. Pinned BtExperience call test methods and their assertions are inspected in full. The [assertion ledger](myopencommunity-audio-call-assertion-dispositions.tsv) maps each inspected assertion to its method and disposition; an assertion inventory is not a passed suite.

Older TS10 build definitions select the PXA270 graph and a separate X11 implementation. Its original MediaPlayerPage, MediaPlayer and SoundPlayer consumers are read at the historical revision to establish pause, completion and direct-access notification relationships. Older LocalAmplifier and VideoDoorEntryDevice consumers distinguish WHO 8 silence/restore from WHO 22 temporary-off requests. Their wider historical variants, unrelated UI/build methods and every original test revision remain explicitly pending. Existing call-address, pager, teleloop, Sound Diffusion and playback reviews provide corroborating context without widening their evidence scope.

## Findings and canonical placement

[WHO 8 local call audio](../../functional/who-8-video-door-entry-telephony/#local-call-audio-in-btexperience) gains the local call/ringtone/pager/control table, camera-delay limitation and callback cleanup qualification. [WHO 22 historical local arbitration](../../functional/who-22-sound-diffusion/#historical-local-audio-arbitration) compares the old priority stack with the newer boolean flags, source configuration, transition completion, logical amplifier silence and separate local timers. WHO 6, WHO 7, WHO 16, WHO 22 and WHO 26 neighboring pages are consulted for placement. No new canonical page or numeric frame definition is created.

Older stack call/mute/call-ringtone/floor states precede alarms, which precede ordinary playback. Screensaver is inserted just above beep and beep just above idle. Re-entering the current generic state pushes another occurrence without path callbacks; removal removes one. Newer AudioState enabling sets a boolean flag. These are distinct implementation policies, not firmware-generation boundaries or bus priorities.

The old logical stack top changes before delayed path callbacks complete. Direct-access notification normally completes a pending transition; a native ten-second guard also completes it while direct access can still be reported true. Its source configuration determines whether local media/amplifier activity use separate states or shared Sound Diffusion. Old media consumers temporarily pause and resume on their state notifications; their backend completion and actual device-release order are not exercised by the graph substitute.

The old temporary-off flag retains logical ON status. A silenced volume change is cached, and restoration uses the latest cache. Its WHO 22 temporary-off consumer schedules one-second restoration. Its WHO 8 consumer instead freezes the level, reports silenced level 1, suppresses repeated silence and schedules a 900-second fallback. Restoration reports the frozen value in Sound Diffusion and zero otherwise. Manufacturer/physical amplifier behavior is not established by these client report choices or comments claiming similar behavior.

Current call properties cache and notify; QML consumers select local operations. With notifications enabled, ringtone exclusion still reserves call-ringtone audio, while the disabled-notification branch returns first. Keep-state call ringtones retain priority after player stop and are cleared by call end; floor playback normally releases its state. An empty path returns before enabling its state. Pager direction chooses local microphone/speaker routing, but both pager states map to VdeCallVolume at this revision. IP/teleloop states are selected by the UI without dedicated entry/exit routing cases in the controller; the older graph has dedicated IP callbacks. Neither observation identifies product capability.

During camera cycling the QML grabber handler acts only in ScsVideoCall, and CCTV ignores QProcess startup. The native original controller schedules audio-on after 300 ms. Explicit disable cancels it; call-state exit neither cancels nor makes its callback recheck state. Controlled execution records an on request after idle. The source comment saying leaving the state prevents on is therefore stronger than the executable path. This correction does not assert an actual hardware noise or deployed race frequency.

Ringtone completion is emitted before cleanup. A synchronous receiver that starts another automatic ringtone replaces the manager's state field; subsequent cleanup clears the replacement state. This is demonstrated with controlled players and original manager/controller logic, not an observed call UI failure.

## Historical corrections

| Actual retained parent | Established change |
| --- | --- |
| [Call mute](https://github.com/OpenWebNet-HA/libqtdevices/commit/f14efc3032154bd9d183e593a37fc15830c30838), parent `07404b972365b5ad9c2d59948d8ef57d15ebbb6e` | Replaces microphone volume 0/1 changes with separate Zarlink mute/restore requests and preserves SCS/IP routes around mute |
| [Camera audio delay](https://github.com/OpenWebNet-HA/BtExperience/commit/22a09d8efbd655ba221a68a09c879942407ffe9f), parent `6fc87ddc730d21339cf81dc6c25930c4b4e119ce` | Adds the 300-ms native timer and explicit-disable cancellation; does not add call-exit cancellation |
| [Ringtone replacement](https://github.com/OpenWebNet-HA/BtExperience/commit/5127118e0ed1a38968f0eabbeb0c8b9379b6b798), parent `926e37bbeda9af50cc7d437a05bf2f39a5c56174` | Initializes automatic-exit bookkeeping and releases an earlier automatically managed state before a replacement request; finished-signal emission still precedes cleanup |

These parent diffs are read independently of representative snapshots. Revisions such as `06ce4eaa5143` and `0fb85c0bf2de` merely carry compared bodies; they are not misidentified as the commits introducing those bodies. Repository dates do not identify deployed Firmware.

## Controlled helper execution

The [reproducer](checks/check_myopencommunity_audio_call_helpers.py) reads exact Git pins and writes to a supplied scratch directory. The [execution record](myopencommunity-audio-call-execution.json) retains original file/blob hashes, helper fingerprint, compiler and Qt version, explicit conditions and actual outcomes. It requires g++, pkg-config, moc-qt5, installed Qt Core development headers and matching Xml headers under `--qt-prefix/usr/include/qt5`; isolated headers from the preceding runtime review are reused without installing packages.

| Controlled run | Outcome and boundary |
| --- | --- |
| Current controller / ringtone manager / generic stack | Pass. Complete original translation units and headers run with native Qt 5 timers/signals. Checks duplicate stack removal, idempotent flags, IP/teleloop no-route requests, 300-ms delayed-on after call exit, explicit cancellation, controlled local and Sound Diffusion pause/resume, normal/keep-state/empty ringtones and synchronous replacement cleanup |
| Older graph | Pass. Original selected graph and logical-amplifier method bodies and complete original generic stack run with native Qt 5 timers/signals. Checks call/alarm/lower-state restoration, screensaver/beep insertion, ten-second forced completion with direct access still true, and cached-volume restoration after temporary silence |
| Original call QtTest expectations | Inspected only. Incoming/outgoing/idle/ringtone/floor/pager/camera/teleloop/auto-open/hands-free/rearm/association assertions are mapped. Some timer tests invoke callbacks manually; mock grabber and writer assertions do not establish hardware actions |

Hardware/process functions record requests and never execute routing scripts, device IO, EEPROM or process termination. Current multimedia/beep/source, enum and XML dependencies are controlled substitutes; pause and output-release acknowledgement ordering is deliberately supplied. Older startup, path callbacks, volume-path and hardware helpers are substitutes; original graph methods execute, but those callbacks do not certify routing. The current controller's helper result is conditional on those player notifications, rather than proof that a physical output was released. No QML, complete original Qt 4 application, original call QtTest suite, simulator, gateway, decoder or audible output executes.

Source inspection, expected-assertion inspection and helper execution have separate per-finding examinations in the existing KB model. Confidence is recorded independently. Atomic claims reference underlying files/revisions, while canonical sections provide explanatory provenance. Existing identifiers and previous findings remain retained.

## Exclusions and unresolved questions

| Candidate | Disposition / evidence still needed |
| --- | --- |
| Timers define physical amplifier or OpenWebNet timeouts | Excluded. Ten-second transition guard, one-second temporary-off consumer, 900-second silence fallback and 300-ms camera delay are separate local software choices |
| Empty ringtone always reserves call audio | Excluded. Original manager returns before state enable; the excluded-ringtone UI branch explicitly enables it, subject to notifications |
| IP/teleloop states prove support or non-support | Excluded. State selection and missing dedicated routing cases do not establish product capability or deployed wiring |
| Simulator execution proves audible/hardware behavior | Excluded. No simulator executes here and no physical audio result is observed |
| All original call tests passed or timer delays were exercised | Excluded. Their expectations are read; hands-free and association tests can manually invoke timeout handlers |
| Repeated old state requests are idempotent | Excluded for the retained generic stack; duplicates persist until individually removed. Newer flags behave differently |
| Empty prototype/X11/removed callbacks represent current hardware | Excluded. Historical variants remain scoped to their source/build; placeholder/no-op methods do not establish a hardware contract |
| SourceStateConstraint enforces its supplied list | Excluded from reader-facing protocol claims. The historical constructor does not copy its parameter into its member list; this is a generic helper defect, not an OpenWebNet rule |
| Full GUI and deployed call/audio runtime | Deferred. Requires original QtQuick/Qt build/runtime, actual backend/process notification order and capture/hardware evidence; source comments cannot close it |
| Wider LocalAmplifier/media-consumer/build histories and all call-test revisions | Deferred with indexed component/parent records. Selected graph/handler closure does not close all producer/consumer history or remaining repositories |

No physical Firmware boundary, WHO 8 global receive contract, hardware timeout, audible restoration guarantee or complete repository extraction is asserted. Remaining useful work is the indexed consumer/test lineage and the deployed routing/backend questions, with captures or hardware required for the latter.

## Validation

| Check | Result |
| --- | --- |
| Original helper execution and fingerprints | Pass: two runs / 12 controlled groups, eight exact original file fingerprints; original call suite remains unexecuted |
| Retained inputs | Pass: all prior claim identifiers/statements and findings retained; only 41 section pins/context positions refreshed, 24 new claims and 11 original-artifact references |
| Retained history and component identities | Pass: 5,607 actual-parent edges, 10,466 endpoint tree identities, 41,973 component occurrences and 1,827 file/blob identities |
| Original assertion identities | Pass: 184 inspected assertions across 22 assertion-bearing methods; 27 source methods include lifecycle/helpers, not 27 passed tests |
| Links / frame examples | Pass: 38 local link/heading targets and 14 public archived-source/correction links; existing OpenWebNet frame examples unchanged |
| Canonical-source audit | Pass: 25 fingerprints and five databases through the authorized read-only archive-fetch setup; no failures |
| ESG / ECV | Pass: zero objective failures; advisory candidates remain review prompts, not protocol verdicts |
| Regeneration and evidence propagation | Pass: 74,329 claims and 8,002 search chunks; all nine new finding records and their examination methods survive reading/search/claim generation |
| Retained generated knowledge | Pass: 24 new claims; only 41 retained section fingerprints refreshed. All 66,466 Device definition claims remain identical |
| Artifact inventory | Pass: 807 artifact records; no inventory/source changes |
| Unit and regression tests | Pass: 23 original-evidence/identifier/LFS/text-hygiene tests and 58 claim-framework/reference/privacy/cross-artifact tests |
| Schema fixtures and evidence packages | Pass: eight schema tests and all four retained evidence packages |
| Canonical publication check | Pass: two independent builds agree byte-for-byte; saved outputs are fresh. Manifest, schemas, cross-artifact consistency, references, text hygiene, privacy gates and Device definition completeness pass |

Selected comparison/reuse covers 485 distinct normalized method/handler bodies. The ledger retains 35,723 indexed-only historical occurrences as pending; neither count is an exhaustion claim. Machine-KB regeneration, unit/privacy checks and canonical freshness/determinism validation pass. Preserved repositories and synced sources remain unchanged.
