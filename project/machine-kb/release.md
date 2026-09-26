# Release Gates and Consumer Contract Status

**Status:** Final release checklist complete for release-content revision b1560324c0b5733614e8eb90cd4f9d04b96edfa9. The independently certified semantic candidate is 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50; the verified revision descends from it only through certification and release-readiness control-document commits, with no generated or semantic corpus changes. The branch remains pre-release: no merge, tag, GitHub Release, publication, or released v1 interface is implied.

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
