# Release Gates and Consumer Contract Status

**Status:** Current-main reconciliation passed for semantic/content candidate 888706f39f4c3f5dba2a49db628b09011714084b. It incorporates authoritative main 2833269fdb09bb6abf2c8bafc43d9105f97861b6 through merge commit d16ca82bf199a4ad0beace1efb3f96edfa1e4a7b, superseding previous release-ready candidate 45bdf82b9697a254229fb7c4511cfb1f920ba457 as the future merge candidate. The independently certified pre-reconciliation semantic candidate remains 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50 as historical evidence; the new upstream semantic delta received bounded recertification and the full release-validation suite passed. The branch remains pre-release: no merge, tag, GitHub Release, publication, or released v1 interface is implied.

## Intended consumer contract

The published dataset must be usable by an independent offline consumer without Python, an LLM, MCP, FastMCP, or any network service. It identifies stable entities and records, human-readable labels, source and evidence provenance, epistemic status, applicability/version scope, namespaces, cautions, unresolved states, relationships, and privacy classification. The versioned manifest identifies artifact versions, the input-content digest, exact hashes, and record counts. Generated ownership and compatibility rules are explicit; source-provenance paths are public repository-relative paths.

Schema compatibility versions are separate from content revisions recorded by Git and future release tags. Never silently repurpose an ID or remove a qualification. The compatibility and migration policy is defined in the [schema versioning policy](schema-versioning.md), including alias, deprecation, tombstone, breaking-change, privacy-withdrawal, and migration behavior.

## Final release checklist

- [x] Contract and schemas reviewed, versioned, and documented with compatibility and migration behavior.
- [x] Allowed sources and pre-extraction sanitization checked; prohibited/private sources are excluded before IR construction and sensitive publishable sources are sanitized before derivation.
- [x] Build verified offline and model-free from a clean revision; repeated builds are byte-identical and committed generated artifacts are fresh.
- [x] Schemas, vocabularies, IDs and aliases, namespaces, provenance, references, claims, and cross-artifact consistency pass validation.
- [x] Privacy classifications are valid and every generated output passes the final privacy scan; installed Device IDs and other prohibited private values remain blocked by pre-IR and final-scan controls.
- [x] Independent Phase 15 factual and epistemic certification remains applicable; the certified-candidate-to-release diff changes only project control documentation and has zero affected claim, chunk, or reference IDs.
- [x] Manifest hashes and counts, artifact/schema versions, input-content digest, licensing, planned release notes, and consumer-facing golden examples were checked against the intended release revision.
- [x] The [review ledger](review-ledger.md), [roadmap](roadmap.md), and project control status are current; no remaining release blocker is hidden in Machine KB project documentation.

## Verified release-candidate relationship

- Independently certified semantic candidate: 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50.
- Intended release-content revision verified by this checklist: b1560324c0b5733614e8eb90cd4f9d04b96edfa9.
- Changes between those revisions: certification and release-readiness control documentation only; diff_impact.py reports full_review_required false, generated_outputs_changed false, and zero affected claim, chunk, and reference IDs.
- Current public artifact/schema format version: 0.1.0.
- Current schema compatibility version: 0.1.0.
- Generator version: ownkb-build-0.8.0.
- ID lifecycle state: 11,173 live IDs, 0 aliases, 0 retired IDs. With no earlier public Machine KB release, this initial publication will establish the compatibility baseline.
- The dedicated final release-readiness completion commit is documentation/control state only and is reported after it is created and pushed; it does not change the verified Machine KB artifacts.

## Distribution readiness

Repository-authored documentation is covered by the repository's GNU GPL v3 license; source materials under sources/ retain the rights and licensing terms of their publishers and authors. The [planned initial release notes](release-notes.md) record this boundary, actual manifest versions, migration state, certified-candidate relationship, and consumer requirements.

The static [golden JSONL serialization vector](../../knowledge/schema/fixtures/valid/golden.jsonl) is documented in the [schema and controlled-vocabulary guide](../../knowledge/schema/README.md) and validated by the schema test suite. It is usable as data without MCP, FastMCP, an LLM, Python, or network access. Python tooling described in contributor documentation is optional validation/build machinery, not a consumer requirement.

## Validation

The final release-readiness run executes the repository-defined gates, including the complete Machine KB unit suite, schema golden/fixture tests, check.py, cross-artifact consistency, privacy validation, ESG/ECV checks, diff_impact.py from the certified candidate to the worktree, a fresh build.py run, and git diff --check.

The build and CI remain offline and model-free. Green mechanical validation is supporting evidence, not a substitute for the independent semantic certification already completed.

## Release boundary

This checklist authorizes no release action by itself. Explicit user authorization is still required before merging machine-knowledge-base into main, creating a tag, creating a GitHub Release, publishing the Machine KB, or declaring a released v1 interface.

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

This reconciliation supersedes 45bdf82b9697a254229fb7c4511cfb1f920ba457 as the future authorized-merge candidate lineage. It does not authorize merging machine-knowledge-base into main, tagging, creating a GitHub Release, publishing, or declaring a released v1 interface.
