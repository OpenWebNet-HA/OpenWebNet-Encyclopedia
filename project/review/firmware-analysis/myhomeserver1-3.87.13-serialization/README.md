# Serialization and action-owner transfer review

This capsule supports [MyHOMEServer1 serialization and action ownership](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-serialization.md). Evidence is static; original Firmware/helper/provider/JSON/process/thread/timer/network/bus/physical execution0.

| Area | Current report | Independent source review |
| --- | --- | --- |
|Actual raw serializer and same-result reparse|[Report](serializer-report.txt)|[Review](serializer-source-review.txt)|
|Candidate null/unsigned value contracts|[Report](provider-values-report.txt)|[Review](provider-values-source-review.txt)|
|Concrete compiled-action/control pair transfer|[Report v2](vector-ownership-report-v2.txt)|[Review](vector-ownership-source-review.txt)|

[Synthesis](synthesis.txt), [coverage](coverage.txt) and [ranked questions](remaining-questions.txt) distinguish source contracts from complete JSON roundtrip, configured activation, whole receiver lifetime and physical behavior.

[SOURCE_EXPORTS.json](SOURCE_EXPORTS.json) pins exact reports, collectors, original source/metadata and reviews. [Source checks](source-checks.json) reproduce saved outputs with --check. First generation refuses overwrite; immediate exact candidates and reports are retained. The vector collector's [version history](vector-version-history.json), [original report](vector-report-failed-v1.txt), [failed-guard record](vector-failure-v1.json) and [original collector](vector-collector-failed-v1.py.txt) preserve its zero-output first failure and grouped exception-index correction. A local root snapshot was taken after v2 existed; it is explicitly not represented as root pre-v2 preservation.

From the workspace:

```
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-11-01-serialization/serializer/collect_serializer_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-11-01-serialization/provider-values/collect_values_v1.py --check
python3 -B work/myhomeserver1-firmware/3.87.13/research/2026-11-01-serialization/vector-ownership/collect_vector_v2.py --check
```

[Documentary review](integration-review.txt) and [identity validation](validation.json) assess current integration and retained earlier evidence; final strict repository checks follow actual assembly. No vendor binaries, complete configuration, source-manifest edit, staging, commits, publishing, live contact or target execution form part of this batch. Wider Device/source gates remain pending; earlier execution ledgers unchanged. The existing allowance-limited continuation remains active separately from these immutable source artifacts.
