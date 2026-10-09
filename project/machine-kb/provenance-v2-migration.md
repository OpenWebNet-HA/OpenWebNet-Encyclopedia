# Structured Provenance Migration

The working branch moves schema compatibility to **2.0.0** with generator `ownkb-build-0.9.0`. This is a compatibility candidate, not a new published release. Published `machine-kb-v0.2.0` and the retained `machine-kb-v0.1.2` baseline keep their 0.1.0 parsing contract; earlier 0.1.0/0.1.1 releases were withdrawn during archive/history cleanup. Adding fields to closed public objects is breaking under the [schema-versioning policy](schema-versioning.md), even when older records omit them.

## Artifact versions

| Artifact | Working version |
| --- | --- |
| Record/common/retrieval/manifest/ID-registry/evidence-review schemas | 2.0.0 |
| Claims, references, retrieval and reading corpus | 2.0.0 |
| Manifest serialization format | 0.1.0; compatibility field is 2.0.0 |
| ID lifecycle registry format | 0.1.0; schema dependency now resolves common types at 2.0.0 |
| Privacy/prepared-source/source-manifest input schemas | Unchanged |

Shared baseline and published main IDs are retained. Colliding unreleased integration IDs are resolved through the [revision-scoped branch migration](../review/myopencommunity-main-sync-2026-10-09.md); they cannot be global aliases because main assigned those spellings to different records. The working retrieval schema accepts both `ownkb:chunk:rNNNNNN` and the reconciled `ownkb:chunk:moc-rNNNNNN` form. This is part of the unreleased 2.0.0 candidate. Corrected claims keep their IDs; new IDs are allocated above the complete lifecycle registry, including retired IDs. Evidence finding IDs are stable review-ledger keys: append new keys, never regenerate them from section order or reuse withdrawn keys.

## Original evidence and explanation

`provenance.location` identifies the Encyclopedia section explaining a finding. `source_id` resolves either that canonical document or its underlying evidence. An original source's `artifact_locator` identifies a Git repository/revision/path/blob/SHA-256/line count/public URI, or an immutable artifact version/SHA-256 and optional public URI. Source records retain public metadata, not copied code, firmware payloads, credentials or private fixtures.

`provenance.examination` records:

- `method`: source inspection, test-expectation inspection, helper execution, static firmware analysis, dynamic firmware oracle or hardware observation;
- `implementation_role`: client, library, simulator, gateway or firmware;
- `conclusion_kind`: direct finding or interpretation;
- `relationship`: supports, corroborates, qualifies or contradicts;
- `code_location` or `artifact_location`: symbol/line range or address-space/offset range;
- `claim_ids`: the individual assertions to which this examination applies; an empty list retains contextual or unmaterialized evidence without attributing it to an atom;
- `conditions` and `limitations`, plus stable finding/review references;
- `execution`, required only for execution/observation methods, with material, setup, input cases, result and retained record locator.

Inspection and static analysis cannot contain an execution result. The model does not automatically rank methods or derive confidence from them. A high-confidence source finding establishes pinned code behavior; it does not become high-confidence physical behavior. The existing epistemic status and confidence fields retain their separate meanings.

Provenance arrays are canonically sorted sets, not an evidence ranking. Consumers must examine all entries. Canonical documentation is explicitly the explanation, not independent corroboration of the underlying implementation. Reused bodies, copied tests and one run cited in several findings remain shared evidence.

## Reading and search

`knowledge/inputs/evidence-reviews.json` is the curated join between reviewed dispositions, original sources, section explanations and retained/new claims. It is a build input rather than a separate public API. `evidence_support` in retrieval chunks publishes its finding summaries, dispositions, reasons, claim IDs and original provenance. Search text and the reading corpus render those entries, including conditions, execution inputs/results and deferrals. Source IDs also enter the chunk's reference set.

A section containing a published specification and a historical implementation retains both. Examination-to-claim mappings prevent an inspected test or controlled helper from being inherited by every claim in that section. Deferred findings contain no claim IDs and retain their reason; counts are not a semantic-coverage certification.

## Consumer migration

Check manifest compatibility before ingestion and validate with the new schemas. Preserve `artifact_locator`, `examination` and `evidence_support` when indexing, filtering or exporting. Resolve original evidence separately from canonical explanations. Follow `claim_ids` rather than promoting section-level methods to unrelated claims. Do not assume `provenance[0]` is primary evidence or count same-source/same-run entries as independent support.

Static firmware analysis and dynamic firmware oracle remain distinct method values. Hash-pinned artifacts and offset locations support their future inputs without pretending either method has been exercised in this audit. Unlisted evidence stays unestablished.
