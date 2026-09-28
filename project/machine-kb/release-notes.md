# OpenWebNet Machine KB 0.1.0 Release Notes

**Release identity:** OpenWebNet Machine KB 0.1.0, intended Git tag `machine-kb-v0.1.0`.

This document describes the exact initial public Machine KB release prepared from `main`. Creating the Git tag and GitHub Release is a separate formal release action and is not performed by this preparation commit.

## Release lineage

- Historical independently certified semantic candidate: `5e5dda65b6ba8d5f4da2ec69126d4a9452455c50`.
- Previous reconciled semantic/content candidate: `888706f39f4c3f5dba2a49db628b09011714084b`.
- Previous readiness/control commit: `d4757986f8b35bcb7bb997a3fae9ef074bf437ec`.
- Reviewed current-main semantic/content candidate: `a819104eed5d8431478ef933235a616cde71a092`.
- Subsequent Apache-2.0 relicensing and consumer/release documentation changes do not alter claim, retrieval, reference, stable-ID, or canonical semantic content.
- The exact released Git revision is the commit referenced by `machine-kb-v0.1.0` when the formal release action is authorized.

## Interface and artifact versions

The release manifest declares:

- manifest format version: `0.1.0`;
- schema compatibility version: `0.1.0`;
- public artifact/schema format version: `0.1.0`;
- generator version: `ownkb-build-0.8.0`.

The manifest contains exact SHA-256 hashes, record counts where applicable, coverage data, and the deterministic input-content SHA-256 digest.

## Initial compatibility baseline

This is the first public Machine KB release. It establishes the published compatibility baseline for the 11,353 live stable IDs in the registry. There are zero aliases and zero retired IDs.

Later identity-preserving renames use aliases. Retired IDs remain tombstones. IDs are never silently repurposed. Contract and format changes follow the [schema versioning policy](schema-versioning.md).

There is no earlier public Machine KB release to migrate from.

## Release contents

The 0.1.0 corpus contains:

- 135 canonical documents;
- 1,207 canonical sections;
- 7,449 atomic claims;
- 1,423 reference records;
- 1,173 retrieval chunks;
- 11,353 live stable IDs;
- 0 aliases;
- 0 retired IDs.

The release includes the deterministic LLM corpus, retrieval chunks, atomic claims, ID registry, seven reference registries, public schemas, and manifest under `knowledge/`.

Epistemic status, applicability/version scope, source provenance, cautions, contradictions, and unresolved questions remain explicit data rather than being collapsed into unqualified facts.

## Consumer use

Machine KB artifacts are static deterministic files intended for independent offline consumption. A consumer does not need Python, an LLM, MCP, FastMCP, embeddings, a vector database, or network access.

The [consumer ingestion guide](../../knowledge/CONSUMING.md) documents:

- direct full-context LLM ingestion;
- lexical, vector, and hybrid RAG/indexed retrieval;
- atomic claims and reference resolution;
- consumer-neutral MCP adapter patterns;
- manifest/version/hash validation;
- update and stable-ID lifecycle handling.

The [schema guide](../../knowledge/schema/README.md) documents the exact controlled vocabulary and an independent golden JSONL serialization vector.

## Privacy and source handling

Private captures, logs, inventories, configuration exports, screenshots, and private submissions are excluded before extraction when prohibited. Publishable material requiring sanitization is transformed before IR, claim, chunk, log, or ID creation. Final privacy validation remains a publication gate.

Installed Device IDs and other prohibited concrete values are covered by dedicated regression tests.

## Licensing

Repository-authored content is licensed under the Apache License 2.0 as stated in the root `LICENSE` and repository README.

Canonical source materials under `sources/` and vendored third-party materials retain the rights and licensing terms of their respective publishers and authors. Generated records retain provenance so consumers can identify underlying source attribution and rights boundaries.

Contributor consent for the Apache-2.0 relicensing is recorded in issue #35.

## Validation

The release-preparation revision is valid only after the exact-commit release suite passes:

- complete Machine KB unit tests;
- schema/golden-fixture tests;
- deterministic clean double-build and artifact freshness;
- manifest/schema/serialization checks;
- ID lifecycle and reference integrity;
- cross-artifact consistency;
- final privacy validation;
- ESG and ECV objective checks;
- Git diff hygiene;
- bounded review of the release-preparation metadata delta.

The formal tag and GitHub Release must point to that validated revision without intervening changes.
