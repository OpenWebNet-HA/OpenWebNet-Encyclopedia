# Isolated original double-helper review

This capsule supports [serialization/provider evidence](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-serialization.md). One root-executed canonical isolated corpus uses original packaged JsonCpp double construction and SAME-object readback for four finite supplied bit patterns. It is separate from full JSON, scheduler or physical execution.

| Evidence | Artifact |
| --- | --- |
|Original source/ABI/canary/tool verification|[Static verification v2](evidence/verification/REPORT.v2.txt)|
|Frozen method and strict boundaries|[Plan v3](evidence/harness/REPORT.PLAN.v3.txt), [source preflight](evidence/harness/SOURCE_PREFLIGHT.json)|
|Independent review BEFORE execution|[Preflight review](isolation-preflight.txt), [root approval](execution-approval.json)|
|Actual canonical outcome and exact ledger|[Results report](evidence/harness/REPORT.RESULTS.txt), [saved results](evidence/harness/RESULTS.json), [run receipt](canonical-run-receipt.json)|
|Independent source/saved-trace audit AFTER execution|[Helper review](helper-source-review.txt), [root result audit](root-result-audit.json)|
|Analysis tooling unchanged|[After check](evidence/verification/AFTER_CHECK.txt), [all63 identities](evidence/verification/TOOL_TREE_AFTER.json)|

Canonical totals:8 top-level entries,340 original code-hook visits,0 C primitive callbacks,12 actual-definition linker redirects,8 EXIT and0 guard stops=360 code-hook callbacks. Four data-relocation setup writes and CPU/FP/register/storage setup are separate. Constructor56/readback29 visits per case; nested original helpers are not extra top-level entries. Positive zero, negative zero, negative one and1.25 preserve exact64-bit patterns. No failed guest attempt or verification CPU replay. Peer audits saved traces/source without CPU execution; root performed the single canonical run.

Original provider /usr/lib/libjsoncpp.so.1.9.5 SHA5916ac361655304327bbf9b2632c1724e49e25b3dd2a10bb27aaa815503ebc36 defines applicability. Candidate self-binding, synthetic canary, zero caller storage and hard-float register setup are explicit. [Synthesis](synthesis.txt), [coverage](coverage.txt) and [remaining questions](remaining-questions.txt) retain full JSON/member/map/assignment/serializer/reparse, effective loader/provider, destructor/nonempty/error/unwind, lifetime/concurrency and physical limits. Scheduler/process/targetOS/services/network/bus/physical execution0; this original-provider helper ledger is no longer0.

[SOURCE_EXPORTS.json](SOURCE_EXPORTS.json) pins exact source/harness/results/history/review bytes. Unexecuted harness v1/v2, original plan/history, independent verification ordering-only failedv1, root snapshots and separate successors remain retained. No fallback or weakened guest guard. Earlier F454/MH202 ledgers and unavailable historical draft limitations are unchanged; no new missing history.

From the workspace run python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-11-01-double-isolation/harness/isolate_double_v3.py --check and verification/collect_verification_v2.py --check for STATIC reproduction only. They do not run the corpus. Explicit run refuses an existing marker; saved canonical results are immutable and replay must not accumulate.

[Documentary review](integration-review.txt) and [identity validation](validation.json) assess bounded integration/earlier evidence preservation; actual strict ESG/ECV/diff follow assembly. Wider Device/source gates pending. No source-manifest change, staging/commit/publish, live contact or closed transport/authentication/session/framing body was investigated. Mutable allowance coordination remains separate.
