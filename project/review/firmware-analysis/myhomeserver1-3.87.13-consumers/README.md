# MyHOMEServer1 3.87.13 consumer-continuation review

This capsule supports the [catalogue and scene-consumer analysis](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-consumers.md). It records current compiled requests/dataflow, distinct provider families and explicit incomplete joins. Original vendor/target SQL/runtime/physical execution is zero. It does not broaden published command semantics or complete Device review.

## Exact source reports

| Area | Retained report | Positive scope |
| --- | --- | --- |
| Catalogue consumer | [Authoritative v2 report](catalogue-report.txt) | Absolute-path opening requests, separate prepared row-reader/store path and separate registered SQL-string initializer |
| Scheduler consumer | [Scene-file consumer](scheduler-report.txt) | Setting/getter/directory/file/JsonCpp parse/same-object-root constructor to three member factories |
| C JSON data provider | [Data and local receipt helpers](providers-report-v2.txt) | Fresh20/32layouts, local Boolean result builder and distinct selected predicates |
| Consultation | [Read-only preflight](preflight-review.txt) | Candidate providers, source boundaries and missing configured assets |
| Synthesis | [Results](synthesis.txt) | Source-confirmed application joins and unresolved ownership/activation |
| Coverage | [Examined scope](coverage.txt) | Exact method limits, without whole-firmware percentages |
| Next joins | [Ranked remaining questions](remaining-questions.txt) | Reader SQL producer, factories/runner, execution/timing and nontransport action handoff |

## Evidence and reproduction

[Source exports](SOURCE_EXPORTS.json) identify exact source paths, sizes and SHA-256 hashes for the reports and selected original disassembly/byte/literal/call metadata. No original firmware/library binary or configured scene is committed. The existing source archive/database registrations remain separate; no new upload or source-manifest change is part of this batch.

The catalogue source's [version history](catalogue-version-history.json) preserves the initial pre-output assertion-encoding failure and actual old report/collector identities. The authoritative v2 corrects file-byte assertion order and failure wording without replacing any generated output or changing firmware interpretation. Scheduler exploratory locator errors and the discarded wrong-mode disassembly are disclosed in its report. Actual first candidates remain immutable in the local research dossier.

From the workspace, reproduce with host Python only:

```
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-consumers/catalogue/collect_catalogue_v2.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-consumers/scheduler/collect_scheduler_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-consumers/providers/collect_json_provider_v1.py --check
```

The current three collectors reproduce59outputs including manifests, using original-byte reads, image-link metadata, host binutils and explicit resolved-node host cases. They do not run the original code, SQL, parser, filesystem APIs or services. Initial creation refuses existing output files; --check writes no candidate. Counts are method/navigation scope rather than semantic or physical coverage.

## Review and completion

| Review/check | Record |
| --- | --- |
| Catalogue original source | [Independent source review](catalogue-source-review.txt) |
| Scheduler original source | [Independent source review](scheduler-source-review.txt) |
| C JSON original source | [Source review](providers-source-review.txt), [second source review](providers-second-review.txt) |
| Current integration | [Integration review](integration-review.txt), [second documentary review](integration-second-review.txt) |
| Host reproduction | [Three current checks](source-checks.json) |
| Source/history/preservation | [Final identity validation](validation.json) |

Current-source review, documentary consistency, mechanical completion and wider Device approval are separate scopes. Compiled opening/parse/factory requests do not establish actual file access, eligibility, trigger activation, action success, bus delivery or physical effects. Earlier reference versions are retained before the two current crosslinks advance. Configured assets, missing extras80/81/94/95, dynamic providers, full state/lifetime/unwind, timing and concurrency remain open. Previously stopped authentication/session/framing/equivalent investigations remain closed.
