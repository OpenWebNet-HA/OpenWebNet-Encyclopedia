# Product-Specific Firmware Follow-Up Evidence

This capsule supports [F454 alarm/AV paths](../../../../reverse-engineering/firmware-analysis/f454-2.0.51-product-paths.md) and [MH202 scenario resources](../../../../reverse-engineering/firmware-analysis/mh202-1.0.24-scenario-resources.md). It extends the existing local branch with selected source evidence motivated by documented product roles. It does not close wider Device reconciliation or runtime/physical gaps.

## Reports and source reviews

| Subject | Exact report | Independent source check |
| --- | --- | --- |
| F454 alarm software ownership | [Report](f454-alarm-report.txt) | [Source review](f454-alarm-source-review.txt) |
| F454 mutable AV state writers | [Report](f454-av-report.txt) | [Source review](f454-av-source-review.txt), including role1 existing-mode2 admission |
| MH202 actual manufacturer resources | [Current report v2](mh202-resources-report.v2.txt) | [Source/extraction review](mh202-resources-source-review.txt), [applicability review](mh202-resources-applicability-review.txt) |
| MH202 panic declaration and Firmware consumer | [Report](mh202-lifecycle-report.txt) | [Source review](mh202-lifecycle-source-review.txt) |

The [product-scope review](product-scope-review.txt) uses the existing reviewed Device/manual synthesis; it is not a fresh primary-document or hardware audit. The source reviews independently check current selected source/code and reproduction with stated boundaries. Reviewer knowledge of a related resource area does not make every finding an independently discovered result.

## Exact provenance and preserved history

[Provenance](provenance.json) pins original source identities, author reports, collectors, exact exports and source reviews. [Pre-edit document snapshots](pre-edit-documents/SOURCE_SNAPSHOTS.json) preserve the earlier branch references. The capsule contains derived reports, not vendor binaries, original images or a self-contained Firmware runtime.

The initial [resource report](mh202-resources-report.txt) called a bounded filename inventory pre-acquisition. Its actual capture followed acquisition and excluded the whole new acquisition/output tree. [Chronology refinement](mh202-resources-chronology-refinement.json) retains the exact old/new wording and identities. The collector still reproduces immutable v1 evidence; current v2 wording is separately source-reviewed. No extraction result changes.

[Extraction version history](extraction-version-history.json) retains failed format/MD5 hypotheses before the successful size/CRC32 guarded extraction. [Reference refinement history](reference-refinement-history.json) preserves initial page candidates and the explicit role1 admission addition. Prior overnight unavailable intermediate histories remain unverified; this new capsule does not authenticate missing bytes.

## Reproduction and limits

The four local read-only static collectors regenerate69 deterministic outputs. The resource source reviewer additionally reconstructs the original counted index and twenty-one selected pages/files in memory using its own reader; no installer, Tcl, .NET or Firmware code is evaluated. Encrypted payloads are not decrypted. A matching registered installer is not a fresh Authenticode verification.

New original/native process execution is zero; earlier helper corpora are pinned historical evidence, not repeated coverage. Configuration/export/provider/active-registry, initial AV activation, electrical attribution, real scripts, full lifecycle and physical outcomes retain their stated gaps. No private project data, packaged secrets or vendor binaries are included. Mechanical validation does not replace full semantic review or authorize a physical/runtime conclusion.
