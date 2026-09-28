# Release Gates and Consumer Contract Status

**Status:** Machine KB 0.1.0 release preparation is complete in `main`, targeting `machine-kb-v0.1.0`. Bounded current-main semantic verification passed on 2026-09-28 for candidate `a819104eed5d8431478ef933235a616cde71a092`. Historical lineage remains explicit: independently certified candidate `5e5dda65b6ba8d5f4da2ec69126d4a9452455c50`, previous reconciled candidate `888706f39f4c3f5dba2a49db628b09011714084b`, and previous readiness/control commit `d4757986f8b35bcb7bb997a3fae9ef074bf437ec`. Subsequent licensing and consumer/release-documentation work changes no Machine KB factual content. Creating the tag or GitHub Release remains a separate explicitly authorized action.

## Intended consumer contract

The published dataset must be usable by an independent offline consumer without Python, an LLM, MCP, FastMCP, or any network service. It identifies stable entities and records, human-readable labels, source and evidence provenance, epistemic status, applicability/version scope, namespaces, cautions, unresolved states, relationships, and privacy classification. The versioned manifest identifies artifact versions, the input-content digest, exact hashes, and record counts. Generated ownership and compatibility rules are explicit; source-provenance paths are public repository-relative paths.

Schema compatibility versions are separate from content revisions recorded by Git and future release tags. Never silently repurpose an ID or remove a qualification. The compatibility and migration policy is defined in the [schema versioning policy](schema-versioning.md), including alias, deprecation, tombstone, breaking-change, privacy-withdrawal, and migration behavior.

## Final release checklist

- [x] Contract and schemas reviewed, versioned, and documented with compatibility and migration behavior.
- [x] Allowed sources and pre-extraction sanitization checked; prohibited/private sources are excluded before IR construction and sensitive publishable sources are sanitized before derivation.
- [x] Build verified offline and model-free from a clean revision; repeated builds are byte-identical and committed generated artifacts are fresh.
- [x] Schemas, vocabularies, IDs and aliases, namespaces, provenance, references, claims, and cross-artifact consistency pass validation.
- [x] Privacy classifications are valid and every generated output passes the final privacy scan; installed Device IDs and other prohibited private values remain blocked by pre-IR and final-scan controls.
- [x] Historical independent Phase 15 certification remains recorded for its exact candidate; the later post-readiness semantic delta received bounded current-main review with explicit provenance, applicability, epistemic, identity, and unresolved-state checks.
- [x] Manifest hashes and counts, artifact/schema versions, input-content digest, licensing, 0.1.0 release notes, the consumer ingestion guide, and consumer-facing golden examples are aligned with the intended release revision.
- [x] The [review ledger](review-ledger.md), [roadmap](roadmap.md), and project control status are current; no remaining release blocker is hidden in Machine KB project documentation.

## Verified release-candidate relationship

- Historical independently certified semantic candidate: 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50.
- Previous reconciled semantic/content candidate: 888706f39f4c3f5dba2a49db628b09011714084b.
- Previous readiness/control commit: d4757986f8b35bcb7bb997a3fae9ef074bf437ec.
- Starting merged main for this bounded verification: 29cd92f68f78a34155848a42b9626ff311d41b6d.
- Current reviewed semantic/content candidate: a819104eed5d8431478ef933235a616cde71a092.
- Current public artifact/schema format version: 0.1.0.
- Current schema compatibility version: 0.1.0.
- Generator version: ownkb-build-0.8.0.
- Current corpus: 7,449 claims, 1,423 references, 1,173 retrieval chunks, and 11,353 live IDs.
- ID lifecycle state: 11,353 live IDs, 0 aliases, 0 retired IDs. No existing stable ID was removed or repurposed; 53 deterministic new live IDs were added after d4757986f8b35bcb7bb997a3fae9ef074bf437ec.
- Release preparation targets `machine-kb-v0.1.0` at the exact revision that passes the final release suite; no intervening commit may be inserted between validation and tagging.

## Distribution readiness

Repository-authored content is covered by the repository's Apache License 2.0; source materials under sources/ and vendored third-party materials retain the rights and licensing terms of their publishers and authors. The [Machine KB 0.1.0 release notes](release-notes.md) record this boundary, actual manifest versions, compatibility baseline, certified-candidate relationship, and consumer requirements.

The static [golden JSONL serialization vector](../../knowledge/schema/fixtures/valid/golden.jsonl) is documented in the [schema and controlled-vocabulary guide](../../knowledge/schema/README.md) and validated by the schema test suite. It is usable as data without MCP, FastMCP, an LLM, Python, or network access. Python tooling described in contributor documentation is optional validation/build machinery, not a consumer requirement.

## Validation

The final release-readiness run executes the repository-defined gates, including the complete Machine KB unit suite, schema golden/fixture tests, check.py, cross-artifact consistency, privacy validation, ESG/ECV checks, diff_impact.py from the certified candidate to the worktree, a fresh build.py run, and git diff --check.

The build and CI remain offline and model-free. Green mechanical validation is supporting evidence, not a substitute for the independent semantic certification already completed.

## Release boundary

This checklist and release preparation authorize no formal release action by themselves. The intended tag is `machine-kb-v0.1.0`. Explicit user authorization is still required before creating that tag, creating the GitHub Release, or publishing externally.

## Current-main reconciliation - 2026-09-27

The previous release-ready Machine KB revision 45bdf82b9697a254229fb7c4511cfb1f920ba457 was reconciled with authoritative main 2833269fdb09bb6abf2c8bafc43d9105f97861b6 from merge base 21fab01a45e5ffc3a242b16902569155c5c34483. The merge itself is d16ca82bf199a4ad0beace1efb3f96edfa1e4a7b; semantic/content candidate 888706f39f4c3f5dba2a49db628b09011714084b contains the regenerated and recertified Machine KB state.

Upstream scope is bounded to the new sound-matrix routing evidence and related canonical updates in WHO 16, WHO 22, reverse-engineering navigation/open questions, and the relationship register. The reconciliation adds the canonical reverse-engineering/sound-matrix-routing.md document.

Impact analysis against 45bdf82b9697a254229fb7c4511cfb1f920ba457 reports full_review_required true, generated_outputs_changed true, 30 changed paths, 402 affected claim IDs, 77 affected chunk IDs, and 96 affected reference IDs. The full-review flag is expected because canonical source topology, stable identities, reviewed claim/reference inputs, and privacy-build semantics changed.

The semantic delta contains 61 new claims and no removed claims. No pre-existing claim changed semantically; 88 existing claims changed only in their source-section SHA-256 pins after additive canonical edits. New epistemic states are 18 observed, 21 corroborated interpretations, 18 unresolved, 3 specified, and 1 experimentally confirmed. The 18 unresolved claims remain explicitly unknown with reasons and open-question links. Five new open questions and 19 new section-topic entities were added; no existing reference seed changed. The ID lifecycle gained 127 live IDs - 61 claims, 20 chunks, 20 sections, 19 entities, 5 questions, 1 document, and 1 source - with zero stale live IDs, for 11,300 live IDs total.

Bounded recertification reviewed the complete 61-claim addition, the changed relationship/open-question material, direct affected records through deterministic impact mapping, the 88 hash-only existing-claim changes, and adjacent unchanged high-risk sound/provenance/privacy boundaries. The claims preserve the authoritative source scope: 1ES routing and two-digit amplifier decomposition are corroborated from the observed installations rather than promoted to published specification; dual-dialect behavior remains Device-scoped; #E, base-band behavior, sources above 4, single-digit amplifier routing, and dual-dialect origin remain unresolved. Existing claim semantics were preserved.

The privacy adjustment prevents OpenWebNet frames such as separator-rich WHO 22/WHO 16 forms from being misclassified as star-separated network addresses while retaining sanitization and final-scan rejection for genuine star-separated IPv4 payloads. Positive and negative regression tests pass.

Final validation for 888706f39f4c3f5dba2a49db628b09011714084b passed:
- 54 Machine KB unit tests.
- 7 schema/golden-fixture tests.
- python3 check.py deterministic rebuild, manifest, schema, consistency, reference, freshness, and privacy gates.
- Cross-artifact consistency: 135 canonical documents, 1,203 sections, 7,415 claims, 1,412 references, 1,169 retrieval chunks, 34 empty sections, 10 excluded guides, and 183 guide-remediation hints.
- Privacy validation across 20 generated artifacts and metadata surfaces.
- ESG objective failures: 0.
- ECV objective failures: 0.
- git diff --check: clean.

This reconciliation superseded 45bdf82b9697a254229fb7c4511cfb1f920ba457 in the historical authorized-merge candidate lineage and was subsequently integrated into main. It did not itself create a tag, GitHub Release, publication, or released v1 interface.

## Bounded current-main initial-release verification - 2026-09-28

Verification started from merged main at 29cd92f68f78a34155848a42b9626ff311d41b6d and reviewed the complete delta from previous readiness/control commit d4757986f8b35bcb7bb997a3fae9ef074bf437ec. The former machine-knowledge-base branch/worktree had already been safely pruned and was not recreated.

The starting Git delta contained 29 commits and six changed canonical Encyclopedia files. Semantic scope was bounded to WHO 1 dimmer behavior, MH200/F418U2 evidence, WHO 2/LN4660M2 centralized-control and advanced-automation behavior, related provenance corrections, identities, generated artifacts, and regression tests. No schema/build/privacy machinery changed in that starting delta.

Bounded Machine KB remediation added the missing WHO 1/MH200 representation, including 22 claims, one public-trace source, four unresolved questions, and one topic entity; two observation-derived implementation-guidance claims were tightened from protocol applicability to implementation applicability. A stale regression guard was corrected from 26 to 27 external sources and now explicitly checks the legitimate LN4660M2 public-trace source ownkb:source:s000161.

Against d4757986f8b35bcb7bb997a3fae9ef074bf437ec, semantic/content candidate a819104eed5d8431478ef933235a616cde71a092 has:
- 34 added claims, 0 removed claims;
- 111 changed existing claim records, of which 102 are source-section-hash-only, six keep the same atomic assertion while generated context expands, and three make genuine semantic corrections to WHO 2 command grammar by separating the event-session selector from command parameters;
- 4 added retrieval chunks and 7 changed existing chunks;
- 11 added reference records, 0 removed or modified existing references;
- 53 added live IDs, 0 removed or repurposed IDs, 0 aliases, and 0 retired IDs.

Final validation passed:
- 54 Machine KB unit tests and 7 schema/golden-fixture tests;
- deterministic clean double-build and byte-identical reproducibility;
- manifest hash/count/freshness validation;
- ID lifecycle and reference-integrity validation;
- cross-artifact consistency: 135 documents, 1,207 sections, 7,449 claims, 1,423 references, 1,173 chunks, 34 empty sections, 10 excluded guides, and 183 guide-remediation hints;
- privacy validation across 20 generated artifacts and metadata surfaces;
- ESG objective failures: 0;
- ECV objective failures: 0;
- git diff --check: clean.

The Machine KB is ready for the initial formal release operation, but no Git tag, GitHub Release, external publication, or released-v1 declaration is created by this verification.

## Machine KB 0.1.0 release preparation - 2026-09-28

The initial public release identity is fixed as Machine KB `0.1.0` with intended Git tag `machine-kb-v0.1.0`.

Release preparation after semantic candidate `a819104eed5d8431478ef933235a616cde71a092` is bounded to licensing, consumer/support documentation, release-control metadata, and removal of the `(pre-release)` label from schema titles. The schema title change is metadata-only: schema `$id`, required fields, properties, enums, constraints, compatibility version, record semantics, and generator behavior are unchanged.

`knowledge/manifest.json` is regenerated so its schema hashes match the prepared release files. All non-schema machine artifacts must remain byte-identical to the reviewed semantic candidate, and manifest corpus counts plus the input-content digest must remain unchanged.

The release operation may proceed only if the exact preparation revision passes the complete validation suite and `machine-kb-v0.1.0` does not already exist locally or on `origin`.
