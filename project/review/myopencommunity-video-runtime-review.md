# MyOpenCommunity Video and Native Runtime Review

This bounded phase starts at `f26c68815a2faefd640c19a5d71e2d7b19471f6a` on `docs/myopencommunity-integration`. It follows both next avenues in the [discovery and browser review](myopencommunity-async-browser-review.md): retained video/platform-audio history and original worker/socket execution. Preserved repositories and synced sources remain read-only. Inventory counts are traceability, not reviewed findings or repository exhaustion.

## Sources and examination boundary

Exact pins remain BtExperience `b88cdac9665d28494f19d6a5d759acf8d5f00ad9`, libqtcommon `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2`, libqtdevices `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) and MyHomeSystemEmulator `4f93f44ee5ec7f89a3de9e040141755c847a5eda`. BtExperience is a client; common/devices are libraries. No simulator, gateway, bus or physical Device executes here.

Complete pinned GStreamer wrapper/backend/control files, AudioState implementation and declaration, XML client/device implementation and declaration are read with consumers, original XML tests, build choices and platform helpers. Earlier complete multimedia/discovery/test inspection is explicitly reused. The [parent-edge ledger](myopencommunity-video-runtime-history-dispositions.tsv) retains selected edges against every retained parent, including merges, earlier locations and removals. The [component ledger](myopencommunity-video-runtime-component-dispositions.tsv) distinguishes complete method-variant comparison, exact prior/shared-body reuse and indexed-only pending histories. Raw locations and hashes preserve bytes; normalized comparisons remove comments/whitespace while retaining literals. Comparison adjacency never identifies chronology.

The complete video-wrapper, external/private predecessor, GStreamer implementation and control method variants are compared. Selected AudioState arbitration, player callbacks, path transitions, volume conversion and source-activity variants are compared. Earlier AudioStateMachine state graphs, other hardware entry points, remaining UI/call handlers and every historical test variant are not closed by this phase. The ledger states the exact boundary. A selected-basename screen finding no emulator file is not proof of absent generic dispatch. Matching common/devices bodies are copied lineage, not independent corroboration.

## Findings and canonical placement

[Sound Diffusion](../../functional/who-22-sound-diffusion/#local-video-and-audio-routing) gains a compact local-video/platform-audio reference alongside the existing local-playback explanation. [UPnP Multimedia](../../functional/who-26-upnp-multimedia/#browser-state-and-recovery) extends header and queue recovery scope. [Stream Parsing](../../protocol/stream-parsing.md#separate-multimedia-xml-transport) qualifies XML framing and reconnect behavior. Established WHO 16, WHO 22, WHO 26, video-intercom and parsing pages are compared for canonical placement and presentation. No numeric OpenWebNet frame syntax changes or new canonical pages are needed.

Video selection uses case-sensitive `mpg`, `avi`, `mp4` suffixes. The external helper receives track and rectangle arguments; its backend accepts absolute paths or strings beginning `http`, and centers smaller video without enlarging it. The separate MPlayer 320 by 240 resolution guard is not called by this GStreamer path, so it is not a general hardware maximum. The helper exposes integer-second FLUSH/KEY_UNIT seeking, while the multimedia UI seek targets the audio player and playAt excludes video. Dead-helper resume restarts the video without cached audio position. Pause acknowledgement and optimistic resume notification remain different.

EOS and backend error emit different signals, but both connect to ordinary application quit. Main returns the event-loop result and initialization failure separately returns one. Wrapper normal zero means done; one/crash means stopped; other normal codes produce neither notification. The multimedia client's paused-video zero-exit exception does not distinguish a playing decoder error. Process-error logging is another callback. Controlled glue execution demonstrates the zero-exit stopped-signal route, not an actual decoder failure. Per-read metadata parsing accepts a partial title and does not retain its remaining fragment for later reads.

AudioState chooses the highest enabled local enum state. Its player-state callback ignores AboutToPause, but the separately connected output-state callback can reevaluate. Above local Ringtone it temporarily pauses Sound Diffusion and permits resumption at or below that threshold. These are application priorities, not bus command priorities. DAC conversion is zero to zero, one to 20, then integer-scaled 21..118; call volume uses 88/100 and four-digit hexadecimal local writes with separate mute. Entering LocalPlaybackMute sets hardware volume zero separately from cached player properties. Registered source activity selects on/off scripts; the pinned access callback only caches a flag. Non-X11 plugin arguments include ALSA plughw=0.0; X11 leaves output default. Earlier OSS/ALSA and scale variants describe code choices, not shipped Firmware boundaries.

OpenXml parseHeader adopts SID/PID/addresses rather than checking the outstanding request. The first valid header establishes welcome state without requiring WMsg. With a nonempty SID, welcome dispatch removes and requeues the head behind later commands. ACK 200 releases the next command before ACK response emission; answered ordinals remain local last-sent bookkeeping and can decrease. Disconnect retains unsent queue entries without replaying the sent entry or scheduling automatic reconnect. A new command starts another connection. The synthetic sequence demonstrates these paths without asserting that real service welcome messages have the same header/ordering.

## Historical corrections

| Actual retained-parent correction | Established change |
| --- | --- |
| [GStreamer state-message handling](https://github.com/OpenWebNet-HA/BtExperience/commit/6ae81e81edfe74321ed1a02672e1b13aa177c63e) | Uses the state-change message instead of querying current pipeline state for delayed notifications |
| [Standalone helper seek](https://github.com/OpenWebNet-HA/BtExperience/commit/e8b9046bcd9f079e0d30830abb6b57d86aa4f7dd) | Adds integer-second FLUSH/KEY_UNIT seek; the console test is not a passed QtTest or proof of UI wiring |
| [Pause transition callback](https://github.com/OpenWebNet-HA/BtExperience/commit/8fa5e07e4298ca8700f441cfd4ee15fd953ec13e) | Introduces the player-state callback that ignores AboutToPause; output-state callback remains separate |
| [Local-source active routing](https://github.com/OpenWebNet-HA/BtExperience/commit/932ceb410d198be6a627f3d7ae00cce58152d138) | Replaces ambient-model checks with SourceBase active notifications |
| [Fresh command SID](https://github.com/OpenWebNet-HA/libqtcommon/commit/ec221014404f58fc9f940a5b39ebcebd21120d5b) | Moves fresh UUID creation into buildCommand, alongside single outstanding-session dispatch; original fixed-SID test expectations remain |

These parent diffs are examined independently of representative snapshots. `9c0c20b06f259fa28072bd36780fe5603efce49b` only changes UUID string conversion in parseAck and is not attributed as the fresh-envelope change. Repository revisions and dates do not identify physical Firmware generations.

## Controlled helper execution

The [reproducer](checks/check_myopencommunity_video_runtime_helpers.py) reads exact Git pins and writes only to a separate scratch directory. The [execution record](myopencommunity-video-runtime-execution.json) retains original file/blob/body hashes and locations, helper fingerprint, compiler/Qt/moc versions and isolated dependency-package hashes. Matching official Qt development RPMs were signature/digest verified and extracted into scratch without installing or changing system packages. The helper expects existing Qt Core/Network development files plus Concurrent/Xml/Test headers under `--qt-prefix/usr/include/qt5`; g++, pkg-config, moc-qt5 and matching runtime libraries are required. Localhost networking must be permitted. Original fixtures, raw test logs and preserved source bodies are not published. Supplemental verbose runs record each original test invocation; this Qt logger reports individual failures and aggregate passes, so unreported individual pass entries are not fabricated.

| Run | Actual result and boundary |
| --- | --- |
| Original TestXmlClient | 5 passed entries, including lifecycle; three test methods pass unchanged under Qt 5. Double/garbage test loops do not compare every second retained message |
| Original TestXmlDevice | 32 passed, 2 failed entries, including lifecycle; 30 test methods pass. testBuildCommand and testBuildCommandWithArg fail because they expect supplied fixed SID while the implementation generates a fresh UUID |
| Native loopback | Original socket, decoder, session and queue files execute; synthetic server demonstrates reconnect buffer retention, split UTF-8 replacement, non-WMsg welcome state, welcome rotation, mismatched identity acceptance, ACK ordering and new-command reconnect |
| Native metadata worker | Entire original MediaPlayer translation unit/header, native QtConcurrent and watchers execute with hardware disabled and a synthetic MPlayer-shaped process. Reentrant replacement loses its watcher; owner destruction leaves worker uncancelled and it completes. Synthetic lowercase video suffixes are accepted while uppercase MP4 and mp3 are rejected; 320x240 passes, 321x240 fails |
| Native discovery worker | Original request and scan bodies use QtConcurrent and a gated substitute model. Owner destruction before gate release does not cancel the worker; it completes after release. Original unsafe completion is deliberately replaced by an empty slot |
| GStreamer control glue | Original control/parser/exit bodies execute with a synthetic backend. Command parsing, split metadata and zero-exit stopped-signal classification pass; no GStreamer API, decoder, plugin or overlay executes |

Original XML classes and test methods compile unchanged with a minimal QCoreApplication driver. Three original XML utility bodies are supplied rather than building unused lock-file dependencies; this is not the full archived application or original Qt 4 runtime. A friend adapter replaces only the XML endpoint with the same original client and exposes state. Synthetic network headers supply explicit SID/PID; real gateway/service contracts are not certified. Discovery substitutes the GUI model and completion slot, so original model affinity, concurrent flag visibility, completion safety and physical unmount races remain unresolved.

Source inspection, inspection of an expected assertion, and actual execution are recorded separately per claim. TestXmlDevice's two failures are retained as failures, not bypassed by editing archived tests. The helper verifies their exact names/counts and rejects different failures. No physical audio, video, bus, simulator or gateway evidence is inferred from these runs.

## Exclusions and unresolved questions

| Candidate | Disposition / remaining evidence |
| --- | --- |
| GStreamer helper execution certifies decoding, display or accurate seek | Deferred: GStreamer 0.10 dependencies/plugins, deployed build, real media and hardware are needed; controlled backend glue only runs |
| MPlayer 320x240 guard is a general Device maximum | Excluded: separate helper, not called by the reviewed GStreamer path |
| Local audio percentages/priorities define SCS rules | Excluded: platform register/script/state handling, not wire dimensions or bus priorities |
| Every decoder error is reported as stopped | Qualified: backend signal can lead to normal zero/done; actual decoder-error execution remains pending |
| Discarding a watcher stops its worker | Excluded for the controlled native worker cases; originals complete after owner destruction. Safe full-stack destruction remains deferred |
| Native discovery run closes completion/model/thread races | Deferred: original unsafe completion, GUI/QWS affinity, concurrent flag visibility and physical removal are not exercised |
| Original XML serializer tests all pass | Excluded: two original assertions fail; exact mismatch retained |
| Valid header adoption validates service response identity | Excluded: synthetic mismatched identity is accepted; true service ordering/handshake remains unresolved |
| Disconnect causes automatic reconnect or replay | Excluded for inspected/tested path: queue survives, new command reconnects, sent command is not reenqueued |
| Whole platform AudioStateMachine and all historical tests are exhausted | Deferred: indexed-only components retain explicit pending dispositions |
| Dates or a library update identify deployed Firmware versions | Excluded without product/build mapping |

The earlier deferred records `moc-e0134` and `moc-e0143` are narrowed with new execution evidence, not silently closed. Original QtConcurrent dispatcher and Qt 5 loopback gaps are now partly resolved; model/race/hardware and real-service questions remain. Real GStreamer execution remains distinct from control-glue execution.

## Machine KB integration

The existing v2 provenance model is reused without schema/generator redesign. New atoms retain original artifact repository/revision/file/blob/hash and examination location, separately from canonical explanation. Confidence remains independent of method. Source-inspected callers are not marked executed when only a callee or controlled substitute runs. Retained claims keep identifiers and statements; reviewed section pins/contexts are refreshed after checking placement. Thirty new claims (`moc-c074051` through `moc-c074080`) and eight claimed findings (`moc-e0144` through `moc-e0151`) are added, with `moc-e0152` corroborating the retained original assertion-limit finding. Eight new original-artifact records include the extension table, resolution constants and build dependencies. The existing UTF-8 claim is corroborated instead of duplicated. The section pins/contexts of 71 retained claims are refreshed; their identifiers and statements remain unchanged. Native metadata execution supplements retained watcher findings; discovery's new execution sits on its still-deferred finding. Device definition records and unrelated material are preserved.

The traceability ledgers contain 3,397 selected parent edges, 22,095 component occurrences and 1,079 file blobs. Only 238 distinct method variants are fully compared here; prior/shared reuse and 1,497 indexed or pinned-only historical variants remain separate. These counts do not represent reviewed conclusions. All selected paths also match an independent full-history changed-path inventory, including root and merge-parent changes.

## Validation

- The full normal repository check passes: two independent builds produce identical bytes; manifest freshness, schemas, cross-artifact consistency, references, text hygiene, privacy gates and Device definition completeness all pass. The catalogue/source checks run through the authorized read-only fetch setup outside the sandbox.
- Regeneration emits 74,305 claims, 8,000 search chunks and 346 documents. Independent semantic comparisons preserve every retained identifier and statement, all 66,466 Device definition claims, and all existing numeric OpenWebNet frame examples. Only the three reviewed pages change generated section content; 71 retained section pins and four retained provenance records change as documented above.
- All nine new finding records and their examination methods survive reading, search and claim generation. Exact source checks verify 53 examinations, 16 executed original files and 16 extracted bodies. Every selected history edge, endpoint and raw component span is checked against the read-only mirrors.
- The 77 relevant KB unit cases pass across the initial run and focused reruns. Two initial failures were stale expected coverage totals, corrected to the actual Protocol and Functional census without weakening validation. Evidence validation passes all four existing packages and 55 acceptance cases.
- The canonical-source audit verifies 25 fingerprints and five database integrity checks with no failures. The external artifact manifest validates all 807 entries. Forty-four local links/heading targets and 13 public evidence/correction URLs pass; ESG and ECV report zero objective failures. Existing advisory queues remain review candidates, not factual pass/fail judgements.
- The controlled runtime results and the two original XML assertion failures remain separate from documentation validation. Real GStreamer, Qt 4 deployment, GUI/model races, hardware and deployed service behavior remain outside the execution boundary.
