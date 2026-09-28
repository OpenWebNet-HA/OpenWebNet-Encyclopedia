# Planned Initial Machine KB Release Notes

**State:** Current-main initial-release candidate documentation only. The Machine KB is already integrated into main. These notes do not announce a formal release, assign a release tag, create a GitHub Release, publish externally, or declare a released v1 interface.

## Candidate identity

- Historical independently certified semantic candidate: 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50.
- Previous reconciled semantic/content candidate: 888706f39f4c3f5dba2a49db628b09011714084b.
- Previous readiness/control commit: d4757986f8b35bcb7bb997a3fae9ef074bf437ec.
- Starting merged main for the bounded current-main verification: 29cd92f68f78a34155848a42b9626ff311d41b6d.
- Current reviewed semantic/content candidate: a819104eed5d8431478ef933235a616cde71a092.
- From d4757986f8b35bcb7bb997a3fae9ef074bf437ec through the current semantic/content candidate, the bounded delta adds 34 claims, 4 retrieval chunks, 11 reference records, and 53 live IDs. It removes no claims, references, chunks, or IDs.
- Of 111 changed existing claim records, 102 are source-section-hash-only changes, six retain the same atomic assertion while generated surrounding context expands, and three correct WHO 2 command-parameter wording by separating the event-session selector from command parameters.
- Current corpus: 7,449 claims, 1,423 reference records, 1,173 retrieval chunks, and 11,353 live IDs.

## Interface and artifact versions

The current manifest declares manifest format version 0.1.0, schema compatibility version 0.1.0, public artifact/schema format version 0.1.0, and generator version ownkb-build-0.8.0. The manifest contains exact SHA-256 hashes, record counts where applicable, coverage data, and an input-content SHA-256 digest. Release naming and tagging are intentionally not assigned by this checklist.

## Initial compatibility baseline

There is no earlier public Machine KB release to migrate from. The current registry contains 11,353 live IDs with zero aliases and zero retired IDs. The first authorized publication will establish the compatibility baseline. Later identity-preserving renames use aliases; retired IDs remain tombstones; breaking contract changes require the migration behavior described in the [schema versioning policy](schema-versioning.md).

## Content and qualification

The candidate contains the generated LLM corpus, retrieval chunks, atomic claims, ID registry, seven reference registries, and the public schemas listed in knowledge/manifest.json. Epistemic status, applicability/version scope, source provenance, cautions, contradictions, and unresolved questions remain explicit data rather than being collapsed into unqualified facts.

Independent Phase 15 recertification remains historical evidence for the earlier certified candidate. Subsequent current-main changes were reviewed as a bounded post-readiness delta covering WHO 1 dimmer and MH200/F418U2 evidence, WHO 2/LN4660M2 centralized-control evidence, related provenance and identity updates, and corresponding Machine KB claims and references. The complete current-main mechanical, privacy, consistency, ESG, and ECV gates passed after that bounded review.

## Privacy and source handling

Private captures, logs, inventories, configuration exports, screenshots, and private submissions can be classified prohibited and are excluded before extraction. Publishable material containing recognized sensitive values is classified for sanitization and transformed before IR, claim, chunk, log, or ID creation. Final privacy validation remains a publication gate. Installed Device IDs and other prohibited concrete values are covered by dedicated regression tests.

## Consumer use

Published Machine KB artifacts are static, deterministic files intended for independent offline consumption. A consumer does not need Python, an LLM, MCP, FastMCP, or network access. Those technologies may be used by an external consumer implementation, but they are not part of the Encyclopedia or Machine KB deliverable. The [consumer ingestion guide](../../knowledge/CONSUMING.md) documents direct LLM, RAG/indexed, claims/reference, and MCP-adapter patterns.

The [schema guide](../../knowledge/schema/README.md) documents an exact two-record [golden JSONL serialization vector](../../knowledge/schema/fixtures/valid/golden.jsonl) for independent byte-level implementation checks.

## Licensing

Repository-authored content is licensed under the Apache License 2.0 as stated in the root LICENSE and repository README. Canonical source materials under sources/ and vendored third-party materials retain the rights and licensing terms of their respective publishers and authors. Generated records retain provenance so consumers can identify underlying source attribution and rights boundaries.

## Release boundary

The Machine KB is already integrated into main. No Git tag, GitHub Release, external publication, or released-v1 declaration is performed by these notes. Those remaining release actions require explicit user authorization.
