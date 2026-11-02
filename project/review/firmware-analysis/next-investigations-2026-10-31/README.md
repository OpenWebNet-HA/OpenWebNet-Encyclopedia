# F454 and MH202 Source Continuations

This capsule preserves five bounded source tracks completed on the existing `docs/static-firmware-analysis-findings` branch. It extends earlier product-specific and ScenarioSuite database work. All new original ARM/CLR instructions, vendor processes, services, gateway/bus exchanges and Physical Device executions are zero. Static decoded instruction counts and host source ledgers are not execution or coverage percentages.

## Reviewed findings

| Track | New source relation | Exact report / independent review |
| --- | --- | --- |
| F454 AV status | `bt_answering_machine` DIM35 formatter to conditional frontend split index4; selected private-state producers | [Report](f454-av-producers-report.txt), [review](f454-av-producers-source-review.txt) |
| ScenarioSuite generator | Selected database filters and row conversion to command/line construction and `.spt`/`info.xml` writer calls | [Report](mh202-generator-report.txt), [review](mh202-generator-source-review.txt) |
| F454 alarm board | Original serial nodes, two DM365 records and separate BASI record; conditional third-slot allocation | [Report](f454-alarm-board-report.txt), [review](f454-alarm-board-source-review.txt) |
| MH202 generated lifecycle | Actual basename/BEGIN/IIF and ordinary-delay producer syntax to selected native consumers | [Report](mh202-generated-lifecycle-report.txt), [review](mh202-generated-lifecycle-source-review.txt) |
| ScenarioSuite field consumers | Graphic3 selects `ANA_TEXT2/3`, not numerically equal temperature/time range rows; original multiplier1 origin | [Current report](mh202-database-consumers-report.v3.txt), [review](mh202-database-consumers-source-review.txt) |

The human-facing findings are in [F454 video and board attribution](../../../../reverse-engineering/firmware-analysis/f454-2.0.51-av-and-board.md), [ScenarioSuite generator](../../../../scenario-engine/scenario-suite-generator.md) and [MH202 generated-script consumers](../../../../reverse-engineering/firmware-analysis/mh202-1.0.24-generated-scenarios.md).

## Provenance and reproduction

[Provenance](provenance.json) pins sixteen exact exports, five collectors, both freshly rehashed original Firmware archives, the selected database identity and analysis-tool metadata. Full original-path/method-token/IL or ELF-VA/span hashes remain in the reports and private local evidence. The vendor database, assemblies, firmware and kernel are not exported into Git.

Run each pinned collector with `--check` from the workspace. Checks read original source and reproduce saved source evidence; they do not load vendor CLR code or replay original firmware. The generator and supplemental database reports share selected methods, so their decoded IL counts are not independent additive coverage. Earlier native corpora remain unchanged and are not replayed or counted anew.

The [validation record](validation.json) records source/export/snapshot identities, protected completed dossiers, mechanical ECV/ESG checks and branch status. The [integration review](integration-review.txt) assesses the final prose against the reviewed sources; it is separate from each independent source review. These checks do not close wider Device reconciliation gates.

## Preserved refinements and limits

The [database development history](database-consumer-development-history.json) retains the pre-promotion raw-branch coordinate error and preliminary manually typed RVA corrections. The [preliminary report](mh202-database-consumers-preliminary.txt) and [second report](mh202-database-consumers-report.v2.txt) are retained exactly. The [header wording refinement](database-header-wording-refinement.v2.json) distinguishes the tiny constructor header from recorded fat method headers. Current source outputs were unchanged by that prose correction.

The actual graphic-type consumer supersedes the earlier provisional Counter-to-`ANA_RANGE` connection. Earlier database reports and their snapshots remain unchanged. A [lifecycle pre-generation note](lifecycle-pre-generation-refinement.txt) discloses the staged PIC-literal correction, including the absence of an exact earlier staged draft; it does not certify unavailable intermediate bytes. The alarm-board report retains exact pre-output machine-name assertion drafts. A [review-location correction](review-location-correction.json) records relocation of one newly created review out of a completed directory, without altering any earlier indexed artifact. Older overnight run18/run21 intermediate-history limits remain explicitly unverified.

F454 electrical SCS AI wiring and initial role1 `bt_vct` activation remain unresolved. MH202 still lacks a genuine configured generated export, complete expression/reply-indexing behavior, full Stop/panic/restart/gate/FIFO lifecycle and observed deployment. Special selector state, active providers, actual timing, object lifetime, concurrency and physical outcomes remain open. The closed authentication/session/framing investigation was not reopened.
