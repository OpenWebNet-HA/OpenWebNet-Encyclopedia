# Worker lifetime, receiver aliases and action construction

This capsule supports [MyHOMEServer1 worker lifetime and action construction](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-lifetime.md). Source is static; original Firmware/helper/provider/process/clock/thread/timer/JSON/network/bus/physical execution0. Raw captures, holder state and source disposal requests do not establish adequate lifetime or a defect.

| Area | Current source report | Independent source review |
| --- | --- | --- |
|Thread states, selected owners and teardown|[Report v2](worker-ownership-report-v2.txt)|[Review](worker-ownership-source-review.txt)|
|22 manually traced receiver candidates|[Report](reset-alias-report.txt)|[Review](reset-alias-source-review.txt)|
|BN3L schema and compiled construction/move/append|[Report](schema-activation-report.txt)|[Review](schema-activation-source-review.txt)|

[Synthesis](synthesis.txt), [coverage](coverage.txt) and [ranked remaining questions](remaining-questions.txt) retain configured-input, serializer, provider, owner/unwind/concurrency, reset and physical limits. No full command-support/JSON-acceptance or whole-firmware alias/lifetime claim is made.

[SOURCE_EXPORTS.json](SOURCE_EXPORTS.json) pins exact collectors, original spans/metadata, reports and source reviews. [Source checks](source-checks.json) record read-only reproduction. First generation refuses overwrite and immediately freezes outputs/code/reports; no vendor binaries or full configurations are exported. The [original worker report](worker-ownership-report-v1.txt) and [wording refinement](worker-ownership-wording-refinement.json) preserve the precise normal-return fallthrough and state+4 versus action+4 namespace corrections, with code/results unchanged.

From the workspace:

```
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-lifetime/reset-alias/collect_alias_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-lifetime/worker-ownership/collect_ownership_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-10-31-lifetime/schema-activation/collect_activation_v1.py --check
```

[Documentary review](integration-review.txt) and [identity validation](validation.json) assess this bounded integration and retained prior evidence; strict repository checks follow actual assembly. Wider Device/source gates remain pending, earlier execution ledgers unchanged. No staging, commit, publishing, source-manifest edit or live contact is part of this batch. Ongoing allowance-controlled research scheduling is recorded in local research control, separately from firmware evidence.
