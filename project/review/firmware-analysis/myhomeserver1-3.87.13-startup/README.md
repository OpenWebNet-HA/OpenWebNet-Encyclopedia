# Startup and scene-registry source review

This capsule supports [MyHOMEServer1 startup and scene registry](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-startup.md). It connects original entry/main, selected service construction and literal thread flag, same-object loader/runner contexts, numeric map population and the nested-action lookup context. Original Firmware/parser/filesystem/clock/thread/service/network/bus/physical execution is0. These are compiled source joins, not an observed startup or installed scene.

## Reports and independent review

| Area | Exact report | Source review |
| --- | --- | --- |
| Executable/startup/loader arguments | [Startup report](startup-report.txt) | [Independent review](startup-source-review.txt) |
| Container/ID/insertion/SCENARIO context | [Registry report](registry-report.txt) | [Independent review](registry-source-review.txt) |

The [synthesis](synthesis.txt), [coverage](coverage.txt) and [ranked remaining questions](remaining-questions.txt) retain active configuration, loading order/readiness, provider/lifetime/concurrency and physical gaps. No source-name equality, constructor request, local Boolean or registry key is promoted to runtime success or a public ID-domain/support rule.

## Exact evidence and reproduction

[SOURCE_EXPORTS.json](SOURCE_EXPORTS.json) pins the current source reports, collectors, original disassembly/byte/PIC/relocation/entry/node metadata and independent reviews. Only a whitelisted noncredential scenesPath is exported from configuration. No vendor ELF/image/database, complete configuration or configured scene is copied into Git.

From the workspace:

```
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-startup/startup/collect_startup_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-startup/registry/collect_registry_v1.py --check
```

[Two parent checks](source-checks.json) reproduce44 outputs. Startup has four finite host branch examples; there are no supplied scenes/trees/runtime objects or original provider/target execution. Counts describe reproduction/navigation, not whole-firmware coverage. First generation refuses existing output files and retains immediate exact report/collector/output copies; --check is read-only. No candidate corrections, overwrite or guard relaxation was required.

## Integration and limits

[Independent documentary review](integration-review.txt) assesses the current pages and exports. [Identity validation](validation.json) checks current source/report/export/snapshot pins, retained earlier reference versions, previous dossiers and the local branch. Final strict repository checks follow actual review/validation copies, with no placeholder or link exemptions; local FINAL_CHECKS.json records them.

The exact source ordering permits constructor/trigger registration before map insertion and requests the service thread before loading. Selected duplicate refusal therefore means no replacement in that wrapper, not no earlier side effects, atomic load, observed race or complete readiness policy. Category2 may alter its key before insertion; complete category/rewrite/error behavior stays open.

Missing configured scenes/extras80/81/94/95, actual process/configuration/provider success, second-tree uses, later registry mutation, shared stop/reset ownership, full lifetime/unwind/concurrency, timing and physical outcomes remain unresolved. Earlier firmware execution ledgers, wider Device/source gates and closed authentication/session/framing/equivalent boundaries are unchanged. No staging, commit, publishing, source-manifest edit, automation or live contact is part of this batch.
