# Compiled scene-actions review

This capsule supports [MyHOMEServer1 compiled scene actions](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-actions.md). It records selected original constructors, callable captures, operational wait/stop/completion code and local target lookup. Original Firmware, scene, timer/thread, service, SQL, network/bus and physical execution is0. Finite host branches/arithmetic and external API semantics are separately bounded.

## Source and review

| Area | Exact source report | Independent source review |
| --- | --- | --- |
| SLEEP capture/request | [SLEEP report](sleep-report.txt) | [Source review](sleep-source-review.txt) |
| Shared operational methods | [Common-action report](common-report.txt) | [Source review](common-source-review.txt) |
| SCENARIO local target route | [Authoritative v2 report](scenario-report-v2.txt) | [Source review](scenario-source-review.txt) |

The [synthesis](synthesis.txt), [coverage](coverage.txt) and [ranked questions](remaining-questions.txt) retain complete-input/provider/lifecycle/concurrency limits. Current code evidence does not prove elapsed time, immediate interruption, runtime registry contents, target launch success, physical support or full Device approval.

## Exact evidence and reproduction

[SOURCE_EXPORTS.json](SOURCE_EXPORTS.json) pins reports, current collectors, selected original disassembly, guards/relocations/PIC/RTTI/provider metadata and source reviews. No vendor binary, database, image or configured scene is copied into Git. [API semantics](api-semantics.json) and [SLEEP API context](sleep-api-context.json) identify maintainer documentation separately from target binaries/headers and ordinary successful ABI assumptions.

From the workspace:

```
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-actions/sleep/collect_sleep_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-actions/common/collect_common_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-actions/scenario/collect_scenario_v1.py --check
```

[Parent reproduction checks](source-checks.json) reproduce63 deterministic outputs. The common report has15 explicitly supplied host branch/arithmetic cases; there are no supplied scene/tree/runtime clock fixtures, original helper execution or API-success primitives. Counts describe reproducibility and navigation, not whole-firmware coverage. Generation refuses overwrite; --check is read-only. Original firmware inputs and prior reports remain immutable.

The [original SCENARIO report v1](scenario-report-v1.txt) and [exact wording correction](scenario-branch-wording-history.txt) remain separate from authoritative v2: zero falls through the selected CBNZ while nonzero takes its branch. Source, effects, collector and results are unchanged. Root SLEEP's actual pre-generation byte-guard draft/audit remains in local research, correcting one transcribed byte before initial execution/output; the original instruction and interpretation never changed. Exact first candidates and report versions were retained before review.

## Integration and unresolved boundaries

[Independent documentary integration review](integration-review.txt) assesses current pages and exports. [Identity validation](validation.json) verifies original/source/export/snapshot identities, prior-dossier preservation, the retained pre-edit factory page and local branch. Actual review and validation targets must exist before final strict repository ESG/ECV checks, recorded in the local research dossier; no placeholder or exemption completes a gate.

Operational duration setters in other derived actions, natural scene registry producers, shared stop/reset aliases, trigger/condition callbacks, configured scene assets and extras80/81/94/95 remain open. Full provider/kernel behavior, lifecycle/unwind/concurrency, measured timing and physical outcomes are unproved. Previously closed authentication/session/framing/equivalent routes remain closed. Existing uncommitted work is preserved; no source-manifest edit, staging, commit, publication, live contact or automation is part of this batch.
