# Planned Initial Machine KB Release Notes

**State:** Release-ready candidate documentation only. These notes do not announce a release, assign a release tag, or declare a v1 interface. Publication still requires explicit authorization.

## Candidate identity

- Independently certified semantic candidate: 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50.
- Release-content revision verified by the final checklist: b1560324c0b5733614e8eb90cd4f9d04b96edfa9.
- The commits after the certified semantic candidate contain certification and release-readiness control documentation only. No generated Machine KB artifact, claim, chunk, reference record, schema, canonical source, or semantic corpus content changed.
- diff_impact.py reports no generated-output change, no full semantic review requirement, and zero affected claim, chunk, and reference IDs.

## Interface and artifact versions

The current manifest declares manifest format version 0.1.0, schema compatibility version 0.1.0, public artifact/schema format version 0.1.0, and generator version ownkb-build-0.8.0. The manifest contains exact SHA-256 hashes, record counts where applicable, coverage data, and an input-content SHA-256 digest. Release naming and tagging are intentionally not assigned by this checklist.

## Initial compatibility baseline

There is no earlier public Machine KB release to migrate from. The current registry contains 11,173 live IDs with zero aliases and zero retired IDs. The first authorized publication will establish the compatibility baseline. Later identity-preserving renames use aliases; retired IDs remain tombstones; breaking contract changes require the migration behavior described in the [schema versioning policy](schema-versioning.md).

## Content and qualification

The candidate contains the generated LLM corpus, retrieval chunks, atomic claims, ID registry, seven reference registries, and the public schemas listed in knowledge/manifest.json. Epistemic status, applicability/version scope, source provenance, cautions, contradictions, and unresolved questions remain explicit data rather than being collapsed into unqualified facts.

Independent Phase 15 recertification passed after the Phase 16/16b remediation. Subsequent release-readiness work did not alter certified semantic content.

## Privacy and source handling

Private captures, logs, inventories, configuration exports, screenshots, and private submissions can be classified prohibited and are excluded before extraction. Publishable material containing recognized sensitive values is classified for sanitization and transformed before IR, claim, chunk, log, or ID creation. Final privacy validation remains a publication gate. Installed Device IDs and other prohibited concrete values are covered by dedicated regression tests.

## Consumer use

Published Machine KB artifacts are static, deterministic files intended for independent offline consumption. A consumer does not need Python, an LLM, MCP, FastMCP, or network access. Those technologies may be used by an external consumer implementation, but they are not part of the Encyclopedia or Machine KB deliverable.

The [schema guide](../../knowledge/schema/README.md) documents an exact two-record [golden JSONL serialization vector](../../knowledge/schema/fixtures/valid/golden.jsonl) for independent byte-level implementation checks.

## Licensing

Repository-authored documentation is licensed under GNU GPL v3 as stated in the root LICENSE and repository README. Canonical source materials under sources/ retain the rights and licensing terms of their respective publishers and authors. Generated records retain provenance so consumers can identify underlying source attribution and rights boundaries.

## Release boundary

No merge, tag, GitHub Release, publication, or released-v1 declaration is performed by these notes. Those actions require explicit user authorization after this release-readiness checklist.
