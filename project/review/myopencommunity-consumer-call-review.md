# MyOpenCommunity Audio Consumers and Call-Test History Review

This phase starts at `73b151105e0ec2f30f2bc6b3e6daac123a5e842e` on `docs/myopencommunity-integration`. It follows the [local audio/call review](myopencommunity-audio-call-review.md), closing the selected producer/consumer notification seam and retained call-test comparison. Preserved archives and synced sources remain read-only. This is a bounded semantic review, not repository exhaustion, physical audio certification or execution of the original application/test suites.

## Sources and examination boundary

The four mirrors retain BtExperience `b88cdac9665d28494f19d6a5d759acf8d5f00ad9`, libqtcommon `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2`, libqtdevices `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) and MyHomeSystemEmulator `4f93f44ee5ec7f89a3de9e040141755c847a5eda`. The earlier TS10 source at libqtdevices `13f0c2049666d234e9cd4b0396863da01636d0f5` and exact historical TouchX snapshots provide separate client/build scope. Historical UI code in a library repository remains client evidence.

The [parent ledger](myopencommunity-consumer-call-history-dispositions.tsv) follows selected basenames through earlier paths, removals and every retained parent, including merges. The [component ledger](myopencommunity-consumer-call-component-dispositions.tsv) distinguishes complete method-variant comparison, exact prior reviewed-body reuse and indexed-only pending material. Original file/blob/component hashes and locations are retained. Normalization strips comments/spacing while retaining literal tokens; copied common/devices bodies are not independent corroboration. The basename screen finds no emulator counterpart, which does not establish absence of generic simulator dispatch.

Whole compared lineages include all selected TestVideoDoorEntry and TestVideoDoorEntryDevice methods, MediaPlayerPage methods/constructor connections, LocalAmplifier methods, selected AudioPlayerPage playback/state/source callbacks, SoundDiffusionPage constructor/source loading/role checks, and GlobalProperties audio initialization/UPnP/CPU consumers. Selected original MediaPlayer, MultiMediaPlayer and SoundPlayer constructors, pause/resume/release, start/finish/termination and direct-access variants are compared; exact previously compared bodies reuse the playback and native-runtime reviews. Wider layout constructors, unrelated Sound Diffusion banners, display controls and unselected backend/GUI methods remain pending. Build definitions are read at the stated historical pins, not certified across every platform or deployed product.

The [assertion ledger](myopencommunity-consumer-call-assertion-dispositions.tsv) records inspected Qt assertions, DeviceTester check/checkSignals calls and paired expected values across the compared call-test variants, with exact revision/file/blob/location and assertion hashes. Lifecycle/helpers are recorded alongside assertion-bearing methods. No assertion inventory, expected result or manually invoked timer callback is reported as a passed original test.

The ledger contains 7,120 selected parent/file edges and 60,067 component occurrences. Of these, 5,499 occurrences represent complete method-variant comparison, 8,546 reuse exact previously reviewed bodies, and 46,022 remain indexed-only and pending. The compared reports contain 612 distinct normalized bodies; the assertion ledger contains 5,858 inspected assertion occurrences across 1,504 file/body-method instances. These are tracking counts, not distinct semantic findings, test-pass counts or proof of repository completion. File/symbol links connect matching original components to the structured findings without widening each finding's cited revision.

## Findings and canonical placement

[WHO 8 local call audio](../../functional/who-8-video-door-entry-telephony/#local-call-audio-in-btexperience) adds the conditional backend-exit outcomes. [Historical touchscreen call model](../../functional/who-8-video-door-entry-telephony/#historical-touchscreen-call-model) explicitly scopes idle guards to TS10 and records the earlier negative autoswitch notification marker. [WHO 22 local playback](../../functional/who-22-sound-diffusion/#historical-local-playback) adds actual player/output notification order and shared UPnP consumer termination. [Local video and audio routing](../../functional/who-22-sound-diffusion/#local-video-and-audio-routing) adds native Sound Diffusion pause scope. [Historical audio arbitration](../../functional/who-22-sound-diffusion/#historical-local-audio-arbitration) adds older TouchX policies and source registration. WHO 7, WHO 8, WHO 16, WHO 22 and the prior WHO 26 browser material establish neighboring placement. No new canonical page, namespace mapping or numeric wire form is created.

| Finding | Established scope |
| --- | --- |
| Local call interruption, exit 1/crash | With the pinned BtExperience/libqtcommon pair and controlled termination, original notifications retain logical Paused/output stopped and permit a restart after the call |
| Local call interruption, exit 0 | Original completion clears the audio track; after call exit the controller returns to Idle. The video paused-completion exception is not applied to audio |
| Local call interruption, normal exit 2 | The child is dead but no completion notification arrives; AboutToPause/output active and the pending call transition persist in the controlled run |
| Release notification order | Internal output is already stopped during the first player-state notification; the separate output notification follows. Releasing ordinary Paused emits another public Paused notification |
| Sound Diffusion suspension | Native pause retains a running process and reported active output; this role is excluded from the local-media direct-access check |
| Shared UPnP consumer | Another active category terminates other UPnP players, including paused ones; normal call resumption is not unconditional restoration after playlist reuse |
| Source registration | Nonempty source Configuration selects the first matching SourceMedia object; absent such an object, the guarded branch leaves playback unregistered |
| Earlier TouchX playback | At `4f3483f36134`, temporary pause retains the stack entry and resumed start does not push it again. Constructor connections and actual consumers establish the relationship |
| Earlier TouchX amplifier | At `795d40817436`, WHO 8 disable/restore uses temporary-off and reports OFF/ON when logically ON; TS10 frozen-level/900-second behavior remains separately scoped |
| Earlier idle receive | At `12fd4e143a50`, ordinary local-addressed answer/end/stop-video events need no active call. Later idle rejection is a library policy change |
| Autoswitch decoded marker | Negative numeric text at `bc8ebb2f89d5` precedes the address-preserving `@` marker; neither is a transmitted prefix |

Prior pause, release, termination classification and controller findings remain retained. New examinations corroborate the original audio-exit claims without replacing their identifiers, evidence methods or scope. Controlled native producer results extend the previous helper that supplied multimedia acknowledgements. The source/controller relationship is still conditional on the configured build and actual backend behavior.

## Historical corrections

| Actual retained parent relationship | Source and inspected expectations |
| --- | --- |
| [Idle call guard](https://github.com/OpenWebNet-HA/libqtdevices/commit/55cce59055e1eeb575eff1d30bfc3fad702f5c83), parent `85a41ee33cbb634dc744fa085729a3b58d780fc1` | Adds the ordinary idle-call guard, initializes IP call state and adds zero-notification expectations for unconnected answer/end/stop-video |
| [Negative autoswitch marker](https://github.com/OpenWebNet-HA/libqtdevices/commit/bc8ebb2f89d5d918e13c9d10eb04441751d17f7d), parent `c4c749f77b027f43cc31503aaa7fbaf474abd3fc` | Decoder converts autoswitch address to negative numeric text; matching test expects it |
| [Text-preserving autoswitch marker](https://github.com/OpenWebNet-HA/libqtdevices/commit/b3ee23d3a978a041f419a3100a5c723f8980b6c9), parent `3dfd00c6e9ce2a00d400f75cc99e6aff54c71515` | Decoder and expected result change together to `@` plus the original address text |
| [Earlier file relocation](https://github.com/OpenWebNet-HA/libqtdevices/commit/07938c30fb5318ee28a26770155040687c134014), parent `20b67275c780d5d0d4643ef446eabe6ad28877e5` | Removed devices-directory implementation equals the root-directory replacement byte-for-byte; removal is not disappearance of its receive policy |

Representative carrier snapshots and comparison adjacency are not interpreted as introduction dates. Both parents of the `12fd4e143a50` merge have identical selected call files; that merge does not introduce the older receive policy. Local boolean/address/enum payload changes in tests describe model representation, not new wire encoding. Earlier pager acceptance, waiting-answer state and END_OF_CALL versus zero-notification expectations remain revision-scoped; the earlier pager review already documents canonical forms. Repeated ringtone events versus changed-property notifications corroborate the existing application distinction. Hands-free and teleloop tests sometimes call their handlers manually. Changed mock writer storage (initialization cache versus live mock frame) does not change the readiness frame grammar.

## Controlled helper execution

The [reproducer](checks/check_myopencommunity_consumer_call_helpers.py) reads exact preserved Git pins and writes only to a supplied scratch directory. Its [execution record](myopencommunity-consumer-call-execution.json) retains eight exact original file/blob hashes, the helper fingerprint, compiler/Qt version, explicit controlled conditions and actual results.

Complete unchanged AudioState, MultiMediaPlayer, MediaPlayer and EntryInfo translation units/headers execute with native Qt 5.15.19 signals, timers, QProcess and QtConcurrent metadata plumbing. The selected build defines `MEDIAPLAYER_DISABLE_HARDWARE_FUNCTIONS`, `MEDIAPLAYER_MULTIPLE_PLAYERS` and `BT_EXPERIENCE_TODO_REVIEW_ME`: original hardware access is disabled and separate QProcess player instances are selected. No multimedia pause/release completion callback is injected. A synthetic slave child emits metadata and the pause marker; controlled SIGTERM behavior produces normal exits 0/1/2 or unhandled-signal crash. The unused GStreamer dependency aborts if any video operation is attempted. Source/config dependencies are substitutes and routing functions record requests only. The original SoundPlayer remains inactive.

Six controlled groups pass: native pause acknowledgement plus release/output ordering and restart; local call interruption for each of four exit outcomes; and native Sound Diffusion pause/resume retaining a running process. Call-exit checks observe a 600-ms event-loop snapshot; pause/resume checks wait up to four seconds for the original notifications. A pending transition in that snapshot is not a measured permanent hardware failure. These results do not measure real MPlayer/GStreamer, original Qt 4/QML behavior, hardware audio, captures, simulator or gateway behavior. An initial synthetic-child argument parser mistakenly read the original `-nolirc` argument as its exit selector; correcting that harness setup made the distinct exit scenarios execute as intended. This was not an archived test failure.

## Exclusions and unresolved questions

| Candidate | Disposition |
| --- | --- |
| Original historical call suites passed | Excluded. All compared assertions are expected-result inspection; no original suite runs |
| Historical timer expectation proves elapsed time or protocol timeout | Excluded. Manual callbacks, timer-active checks and mock process assertions establish narrower local behavior |
| Intermediate pager fixture with an extra field | Excluded as canonical syntax. Its asserted result does not override verified writers or establish hardware grammar |
| SIGCHLD/QProcess and shared-player revisions identify Firmware | Excluded. Earlier callbacks classify exits differently or clear process identity before completion; these are software implementations, not deployed Firmware boundaries |
| Hardware-routing requests prove audible effects | Excluded. Embedded helpers request platform-specific operations; X11 variants can be empty. No such operation or original platform build executes |
| CPU rescaling variants add protocol knowledge | Excluded. Compared debug/commented-write changes are application policy only |
| Local source/amplifier Configuration proves product capability | Excluded. It selects consumers; deployed hardware, service and routing availability need independent evidence |
| Native controlled exit result proves actual MPlayer exit convention | Deferred. Requires the original backend/version/runtime and observed termination behavior |
| Original Qt 4 application, full GUI and physical restoration | Deferred. QML, actual backend decoding, output ownership, service interaction and audible results remain unexecuted |
| Wider unselected GUI/build/helper history | Deferred with indexed identities. The completed semantic lineages do not close unrelated layout, display, Sound Diffusion banner or all backend methods |
| Generic simulator dispatch | Unresolved. No basename match is not a semantic absence proof; no simulator result is used as hardware evidence |

Source reading, expected assertion inspection and helper execution remain separate structured examinations. Confidence is independently recorded. New atomic findings identify original repositories, exact revisions/files/blobs and code locations, plus explanatory sections; the existing provenance schema remains unchanged. Existing Device definition claims and source inventories are preserved.

Findings `moc-e0162` through `moc-e0167` introduce 13 implementation-scoped claims, `moc-c074105` through `moc-c074117`. Finding `moc-e0168` adds execution corroboration to retained claims `moc-c074008` through `moc-c074010`. Finding `moc-e0169` records the deferred original-suite and deployment boundary. The new records contain 13 source inspections, three expected-test inspections and seven controlled-helper examinations; the same finding can have several methods.

## Validation

| Check | Result |
| --- | --- |
| Original native producer/controller helper | Six controlled groups pass; eight unchanged original file fingerprints and the reproducer fingerprint verified |
| Original archive locations | All 23 new examinations match exact original revisions, files, blobs and named code/test locations |
| Retained-history ledgers | 7,120 actual parent edges, 13,032 endpoint tree identities and 60,067 component locations/hashes verified against 2,396 original file blobs |
| Expected assertion ledger | All 5,858 assertion occurrences match original locations and assertion fingerprints across 54 file blobs; this is not test execution |
| Atomicity and evidence preflight | All 13 new claim mappings and eight finding records pass the existing parser, privacy preparation and evidence schema |
| Generated-output comparison | 74,342 claims, 8,002 chunks and 346 documents; 13 new claims, five changed chunks in the two canonical pages, no new chunks/documents |
| Retained records | All retained identifiers/statements preserved; 113 section digests refreshed and three retained claims gain execution corroboration. All 66,466 Device definition claims remain identical |
| Evidence propagation | All eight finding records, examination methods, source/claim relationships and qualifications survive reading, search and claim generation |
| Focused repository regressions | 23 original-evidence/identifier/LFS/text tests, 29 claim/reference/parser/credential-preparation tests, 33 privacy tests, six consistency tests, one complete double-build inventory test and eight schema tests pass |
| Existing capture evidence | Four packages validate; 55 acceptance tests pass. These packages supply no new audio-hardware evidence |
| Standard Machine KB check | Passes fresh double-build determinism, committed freshness, manifest/schema integrity, cross-artifact consistency, references, text hygiene, privacy and Device completeness |
| Device completeness | 210 definitions pass against the registered, fingerprint-verified private catalogue |
| Canonical-source audit | 25 source fingerprints and five databases verified, no failures; authorized read-only archive fetch used outside the sandbox |
| Links and frames | 46 local links/heading targets and 12 public archived-source/correction links pass; existing OpenWebNet frame examples are unchanged |
| External artifact inventory | All 807 registered artifacts pass integrity checks |
| Encyclopedia style and core values | Both mechanical gates pass with no objective failures; existing advisory queues remain 6,800 style and 14 core-value candidates |

The build regression exposed stale inventory snapshots from earlier phases. Expected non-Device claim, protocol-claim, functional-claim and non-Device chunk totals were refreshed alongside the 13 new claims; no assertion was removed or weakened. The corrected complete double-build test passes. Source material and Device definitions remain unchanged. The bounded comparison and pending material listed above remain the coverage boundary.
