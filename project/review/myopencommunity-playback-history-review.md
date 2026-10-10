# MyOpenCommunity Playback Backend Review

This phase starts at `4c1f2b3040d7484c51236904fe6c099c960cb254` on `docs/myopencommunity-integration`, after synchronizing with main. It follows the [Sound](myopencommunity-sound-history-review.md), [Alarm-clock](myopencommunity-alarm-clock-history-review.md), [Equalizer](myopencommunity-equalizer-history-review.md) and [KB provenance](myopencommunity-kb-provenance-audit.md) reviews. The bounded subject is local audio source discovery, player state, retry and failure delivery to the alarm controller. Archived sources, retained histories and synced source material remain read-only.

## Sources and examination boundary

| Repository | Exact pin | Role in this phase |
| --- | --- | --- |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | Client source, playlist, player, alarm and direct audio-state consumers |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Audio process wrapper, local/UPnP list managers and OpenXml browser dependencies |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | Earlier player/page/list implementations across retained locations |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` | Prior sound-model boundary retained; no new simulator execution or hardware claim |

The preserved OpenWebNet-HA Git mirrors supply reachable retained histories and exact pinned commit objects. The former local archive directories were unavailable in this environment; the public preservation mirrors were retrieved without changing the repository's canonical sources. Earlier review conclusions were read before tracing the newly reviewed helpers. No generic protocol survey substitutes for those sources.

Complete pinned files read include BtExperience mediaobjects.cpp (media source classes), multimediaplayer.cpp, playlistplayer.cpp, the client GStreamer wrapper, and test_multimedia_player.cpp; common mediaplayer.cpp and list_manager.cpp are read in full. Direct scoped dependencies include external GStreamer error/EOS handling, source declarations, UPnPListModel's shared device, AlarmClock startup/fallback, AudioState pause/release/resume consumers, OpenXml browser error paths, the library build definitions and archived test build file. These dependency scopes do not certify the whole UI, build or OpenXml library history.

The [parent-edge ledger](myopencommunity-playback-history-dispositions.tsv) records 1,389 actual retained-parent file edges, including merge parents, across earlier selected basenames and locations: 502 BtExperience, 325 libqtcommon and 562 libqtdevices. The [component ledger](myopencommunity-playback-component-dispositions.tsv) records 13,179 component occurrences across those file variants. It distinguishes 182 distinct fully compared method variants, 65 matching common-library bodies reused through shared lineage, 489 variants with pinned-file inspection but pending historical comparison, and 457 indexed-only variants. Repeated occurrences account for 1,943, 818, 5,889 and 4,529 ledger rows respectively. These totals describe the ledger, not findings or extraction completeness.

Complete initial method bodies and all distinct normalized variants are compared for discovery/completion, source cycling, playlist generation/loop/unmount, stopped-state handling, termination, player pause/release/resume/source change, done/stopped ordering, local volume/mute setters, process launch/finish/error, metadata request/completion, UPnP response/error/selection/index, loop tests and the legacy page's server-down/current-file/done consumers. The ledger names the exact covered methods. Comparison adjacency is between method variants, not necessarily Git parents. Actual correction chronology is verified separately against retained parents. Overloaded playlist generators are compared together but source support identifies the relevant overload explicitly. Normalization preserves string/character literals and removes comments/whitespace; whole-file and raw line-range hashes preserve original bytes. Matching shared bodies provide no independent corroboration.

The complete pinned test file's preconditions, sanity, play, multiple play, pause/resume, repeated pause, output release/resume, source replacement while playing/paused, empty source, seek, completion and local playlist expectations were inspected. Only loop-test histories were fully compared. Fixture initialization requests MPlayer null audio output and relies on the archived Qt/GStreamer stack. These are inspected expectations, not passed suites or audible-output evidence.

The selected basename/history screen identifies no dedicated emulator playback file. It does not establish absence of generic emulator dispatch or close all four repositories. Metadata subprocesses, complete legacy page UI, every historical test, full GStreamer/video behavior, generic browser/configuration code and headers retain explicit pending boundaries.

## Findings and canonical placement

[Sound Diffusion](../../functional/who-22-sound-diffusion/#historical-local-playback) receives a compact client behavior table and limitations. Its existing alarm paragraph now identifies the one-shot callback and absence of later failure delivery in that path. [UPnP Multimedia](../../functional/who-26-upnp-multimedia/#local-playlist-integration) receives the asynchronous OpenXml selection/index and error-delivery qualification. Existing protocol, amplifier and numeric WHO tables are retained. Neighboring Sound System and UPnP pages were read; procedural guides and new canonical pages are unnecessary.

| Reviewed finding | Disposition / individual claims |
| --- | --- |
| First-content discovery and local playlist scope | moc-e0125; `ownkb:claim:moc-c073994`, `ownkb:claim:moc-c073995`, `ownkb:claim:moc-c073996`, `ownkb:claim:moc-c073997` |
| Logical playback state and output ownership | moc-e0126; `ownkb:claim:moc-c073998`, `ownkb:claim:moc-c073999`, `ownkb:claim:moc-c074000`, `ownkb:claim:moc-c074001` |
| Playlist retries and local removal handling | moc-e0127; `ownkb:claim:moc-c074002`, `ownkb:claim:moc-c074003`, `ownkb:claim:moc-c074004` |
| USB/SD completion lifetime and callback attribution | moc-e0128; `ownkb:claim:moc-c074005`, `ownkb:claim:moc-c074006`, `ownkb:claim:moc-c074007` |
| Audio process completion and error coverage | moc-e0129; `ownkb:claim:moc-c074008`, `ownkb:claim:moc-c074009`, `ownkb:claim:moc-c074010`, `ownkb:claim:moc-c074011` |
| Local player properties are distinct from backend commands | moc-e0130; `ownkb:claim:moc-c074012`, `ownkb:claim:moc-c074013` |
| UPnP playlist selection and asynchronous index | moc-e0131; `ownkb:claim:moc-c074014`, `ownkb:claim:moc-c074015`, `ownkb:claim:moc-c074016` |
| UPnP failure delivery and first-content boundary | moc-e0132; `ownkb:claim:moc-c074017`, `ownkb:claim:moc-c074018`, `ownkb:claim:moc-c074019`, `ownkb:claim:moc-c074020` |
| Alarm fallback subscription ends after first result | moc-e0133; `ownkb:claim:moc-c074021` |

IP-radio first-content success is based on configured entry count after starting a playlist; it is not a connection/decoder result. USB/SD uses breadth-first extension matching and selects the first audio entry rather than arbitrary leading directories; its generated local playlist filters to the selected file type. Ordinary pause retains active audio output, while release stops the backend and retains logical pause. Resume attempts the cached time, including its fractional seconds; no seek fidelity is established. Playing follows process startup, not sound.

The stopped-state path advances unless user track change or the loop guard suppresses it. The pinned guard tests the predecessor of the saved starting index with a strict elapsed threshold of 2,000 ms times item count. It emits loopDetected and prevents that advance; the guard itself does not terminate/reset the pinned list. Local unmount handling tests a path prefix and terminates the selected playlist, not its separate discovery worker.

USB/SD completion deletes its result flag before reading it and does not clear the owning member. If a replacement search has not changed that member, a later mounted search can write through the deleted flag. The worker uses the flag both for cancellation and unsuccessful search. SourceMultiMedia handles completion through the current source index without checking sender/request identity. These source facts establish unsafe client paths; they do not predict deterministic crashes, timing or deployed product behavior.

While active, the common wrapper classifies normal exit 0 as done, normal exit 1 or crash as stopped, and other normal exits with neither notification. The process-error callback logs only. Its compile-time direct-access update is distinct from exit classification. The local player volume/mute setters cache properties and notify; separate AudioState consumers must not be erased from the account of output behavior.

UPnP browsing and playlist control share UPnPListModel's static OpenXml device. Track selection sends the entry name; current URL/metadata updates on the service response. Next/previous changes index before that response. Error notification is selective: track-selection/invalid-response SERVER_DOWN emits serverDown, but the handler does not clear current track or stop playback. The pinned BtExperience playlist connects currentFileChanged rather than serverDown. Earlier AudioPlayerPage consumes serverDown for page-state handling. SourceUpnpMedia inherits default false first-content behavior and separately supports explicit selected-entry playback. None of these paths supplies a numeric WHO 26 encoding.

AlarmClock disconnects firstMediaContentStatus after its first result. Startup/fallback has no player-error or loopDetected subscription. A later failed stream or loop notification therefore does not itself cause that fallback. The previous cautious availability statement is refined, not expanded into a hardware guarantee; retained claims `moc-c007787` and `moc-c007788` keep their identifiers and statements.

## Historical corrections

| Actual retained-parent change | What comparison establishes |
| --- | --- |
| [Loop boundary correction](https://github.com/OpenWebNet-HA/BtExperience/commit/d56b2eb49ab232e4dd6f39dc215027b8f338da4b) | Earlier same-index checking changes to predecessor checking and adds reset expectations; no deployed Firmware boundary |
| [Initial directory-selection correction](https://github.com/OpenWebNet-HA/BtExperience/commit/b5f362f67cb4967c82d89134495161ef8d973573), [move into completion](https://github.com/OpenWebNet-HA/BtExperience/commit/c6a80a15d287af66fc63e47355f856d96385cd40) | Directory skipping moves from playlist generation to first audio selection; delete-before-read remains |
| [Resource release](https://github.com/OpenWebNet-HA/BtExperience/commit/d874628f431f084e2f2713268f899c056eb481ee) | Internal released state becomes distinct from ordinary logical pause; later audio/video differences remain client policy |
| [Completion ordering](https://github.com/OpenWebNet-HA/BtExperience/commit/2759bded6c89e90985c2feef3a93ea36a8d49836) | Clear source before publishing Stopped to avoid reentrant next-item clearing; a paused-video zero-exit exception is separate from audio classification |
| [Forced source-cycle reset](https://github.com/OpenWebNet-HA/BtExperience/commit/d924976050143f28e5c5668d9959a3f8af8fa9ba) | Force starts source iteration afresh; does not add request identity to late callbacks |
| [Multiple players](https://github.com/OpenWebNet-HA/libqtcommon/commit/1a9114800a268f493719c1a41594741cb4b6a260), [process kill correction](https://github.com/OpenWebNet-HA/libqtcommon/commit/782bf6dee9433e5a2d0f4a0a5002825f9e149b02) | Process ownership and termination vary by compile-time selection and library revision; the pinned library build defines multiple players and disables hardware functions |
| [Pause signal correction](https://github.com/OpenWebNet-HA/libqtcommon/commit/9e0866575c178bdf0c0071f9cf7be1b6c1c4076e) | Pause request, acknowledgement and local state notification evolve; no runtime/test-pass claim follows from the diff |
| [Legacy page lineage](https://github.com/OpenWebNet-HA/libqtdevices/commit/c26095b324ce1845ee775daa38d6cbb052ee3696) | Earlier ts_10 page/list copies consume serverDown; copied lineage is not independent evidence or a universal termination contract |

## Controlled helper execution

The [reproducer](checks/check_myopencommunity_playback_helpers.py) reads six original method bodies from the pinned preserved Git objects, writes only to a separate scratch directory and compiles controlled C++ substitutes. The [execution record](myopencommunity-playback-execution.json) pins original repository/revision/file/blob/content/body hashes, helper hash, compiler and conditions. No archive source body or private fixture is copied into public review files.

Run from the repository root with `--repositories` naming a read-only directory containing BtExperience.git, libqtcommon.git, libqtdevices.git and MyHomeSystemEmulator.git, and `--output` naming a disposable directory outside those mirrors. g++ is required. The script does not fetch or modify preserved repositories.

Eighteen controlled comparisons pass for active/inactive normal 0/1/2 and crash exits, three-item loops at 5,999 versus 6,000 ms, one-item/no-list/reset handling, stopped-state advance with/without user-change suppression, and selective XML server-down delivery. Five original bodies cover those comparisons. The sixth, SourceLocalMedia::pathScanComplete, runs separately under AddressSanitizer with an empty cancelled result and a heap-allocated true flag. AddressSanitizer identifies the original post-deletion read as heap-use-after-free. Repeated-search writes and worker interleavings were not executed.

Process signals are counters; list/index/count, elapsed time and XML error codes are controlled inputs. Completion watcher/model/sender are substitutes. LAYOUT_TS_10 is omitted; its direct-display/audio-state branch is not tested. BT_EXPERIENCE_TODO_REVIEW_ME is defined. No original test suite, Qt event loop, QtConcurrent worker, real MPlayer process, GStreamer decoder, network, bus, simulator or physical hardware runs. These conditions are preserved in individual helper-execution provenance, separately from source inspection and test-expectation inspection. Confidence remains about the exact observed code/helper result, independently of evidence method.

## Exclusions and unresolved questions

| Candidate | Disposition / next evidence needed |
| --- | --- |
| First-content true, Playing, changed index or bus ACK proves audible playback | Excluded: different local milestones; a decoder/output observation is needed |
| Every unavailable stream causes beep fallback | Corrected: the reviewed alarm consumes only the first availability callback |
| LoopDetected is a complete error diagnosis or always terminates the list | Excluded: timed retry heuristic and advance suppression only |
| USB/SD flag defects predict one deterministic physical outcome | Deferred: QtConcurrent scheduling, memory visibility, cancellation, model affinity, late callbacks and destruction need controlled runtime analysis |
| Unmount cancels discovery | Excluded for the reviewed path: playlist termination and discovery cancellation are separate |
| serverDown invalidates current track and stops every client | Excluded: manager preserves state; consumer connections differ |
| Local volume/mute properties fully describe device output | Excluded: setters alone cannot close separate AudioState/amplifier consumers |
| External MPlayer/GStreamer exit conventions certify every stream failure | Deferred: wrapper classification is exact, but backend versions, full suites, decoded playback and seek fidelity remain unestablished |
| UI labels or OpenXml calls establish numeric WHO 26 traffic | Excluded: no new numeric serializer in this path |
| Repository dates identify shipped Firmware generations | Excluded: no deployed build/product mapping |
| Missing resetSourceIndex in the pinned class proves a particular runtime failure | Deferred: older implementation exists; current connection validity/runtime effects were not executed |
| Selected file/method inventories close the remaining backend history | Excluded: indexed and pinned-only histories remain explicitly pending |

Two structured deferred findings retain original sources: asynchronous discovery scheduling/removal and the complete external media runtime/test environment. Remaining source work can follow metadata-process lifetimes, full browser cancellation/navigation, remaining historical player tests, GStreamer/video backend paths and legacy UI consumers. Captures or hardware are needed for deployed applicability, audible output, stream-failure behavior and seek accuracy. This review closes the specified compared methods and source-level failure paths, not the repositories or the entire asynchronous runtime.

## Machine KB integration

Twenty-eight new revision-scoped implementation claims are added with six new original-file source records. Nine claimed and two deferred reviewed findings map methods and exact code ranges to the canonical sections. Typed claim links qualify the retained availability/fallback claims. Source inspection, inspected expected results and controlled helper execution remain separate; execution support maps only the atoms actually exercised. The UPnP generator is named by overload. Original artifact locators remain distinct from the explanatory page, and qualifications survive claim, reading and search outputs through the existing v2 provenance model. No schema/generator redesign or public release-version change occurs.

Two section and two chunk identities are allocated above the complete lifecycle registry. All retained IDs and claim statements remain unchanged. Thirty-three retained claim section pins are reviewed and refreshed after page extension; neighboring source blocks and context mappings are preserved. Device definitions and unrelated catalogue work remain untouched.

## Validation

| Validation | Result |
| --- | --- |
| Controlled original-body execution | Pass: 18 comparisons and the expected AddressSanitizer heap-use-after-free result; conditions above |
| Original-source locators | Pass: 32 examination mappings independently checked against pinned file/blob/SHA-256, line counts and named symbols |
| History/component identities | Pass: 1,389 parent edges, 2,386 distinct endpoint tree identities, 13,179 component occurrences and 580 repository/blob identities; semantic scopes remain distinct |
| Claim provenance and links | Pass: 28 new claims plus retained link targets through unmodified render/context/evidence/schema/scope/serialization validators |
| Output scope and evidence survival | Pass: all 11 new dispositions and methods survive reading/search/claims; 28 claims and two chunks added; 33 retained section hashes refreshed |
| Unrelated Device knowledge | Pass: all 66,466 Device-definition claims remain byte-equivalent as JSON records |
| Existing unit suites | Pass: all 220 Machine-KB, eight schema, 28 Device and 55 evidence-package tests; source wording/conditions and typed links were subsequently refined without code/schema changes, with final-state provenance and normal rebuild checks repeated |
| Style, Core Values and artifact inventory | Pass: no objective failures; 807 registered artifacts; advisory observations are not evidence verdicts |
| Canonical-source audit | Pass: 25 fingerprints, five database integrity results `ok`, no failures; authorized read-only R2 helper used |
| Links and frames | Pass: style/link check and eight underlying public source URLs resolve; existing frame examples unchanged and no new wire encoding asserted |
| Normal deterministic documentation/KB check | Pass: two deterministic builds, committed-output freshness, schemas, cross-artifact consistency, references, text hygiene, privacy gates and Device definition completeness |

The full diff is reviewed for presentation, placement, duplication and scope. The final refinement separates the unconditional post-deletion read from the conditional owning-member write, and adds typed qualification links to retained availability/fallback claims. The original helper and archived test scopes are unchanged. No source, archive, Device definition, retained claim statement, schema or generator is edited. The final-state normal check is repeated after that refinement.
