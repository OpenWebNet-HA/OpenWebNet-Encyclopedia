# OpenWebNet Machine KB 0.1.1 Release Notes

**Release identity:** OpenWebNet Machine KB 0.1.1, intended Git tag `machine-kb-v0.1.1`.

This patch release corrects consumer-facing defects discovered after 0.1.0 while preserving the published 0.1.0 schema and artifact compatibility contract.

## Changes since 0.1.0

- Fix generated claim statements whose materialized table context leaked internal Markdown parser representations. The 1,120 affected claim statements are repaired; the change is confined to statement text and preserves claim IDs and non-text semantics. This resolves the corrective work tracked in issue #37.
- Bring the public schema vocabulary documentation back in sync with the JSON Schema, including the relationship predicates and entity-type vocabulary tracked in issue #38.
- Add a fail-closed generated-text hygiene gate and regression coverage so internal parser structures cannot enter published claim text unnoticed.
- Standardize the formal public name as OpenWebNet Machine KB while preserving technical identifiers such as the `ownkb:` namespace, `knowledge/` paths, and `machine-kb-vX.Y.Z` tag prefix.
- Advance the deterministic generator to `ownkb-build-0.8.2`.

## Compatibility

This is a patch release. No consumer migration is required.

- manifest format version: `0.1.0`;
- schema compatibility version: `0.1.0`;
- public artifact/schema format version: `0.1.0`;
- generator version: `ownkb-build-0.8.2`.

The stable-ID inventory remains 11,353 live IDs with zero aliases and zero retired IDs. No ID is removed, repurposed, or renumbered.

## Release contents

The corpus remains:

- 135 canonical documents;
- 1,207 canonical sections;
- 7,449 atomic claims;
- 1,423 reference records;
- 1,173 retrieval chunks;
- 11,353 live stable IDs.

The release includes the deterministic LLM corpus, retrieval chunks, atomic claims, ID registry, seven reference registries, public schemas, and manifest under `knowledge/`.

## Validation

The exact release revision must pass:

- the complete Machine KB unit suite;
- schema and golden-fixture tests;
- deterministic build and freshness checks;
- manifest, serialization, ID-lifecycle, and reference-integrity validation;
- cross-artifact consistency;
- final privacy validation;
- generated-text hygiene validation;
- ESG and ECV objective checks;
- git diff hygiene.

The machine artifacts remain offline-consumable and model-free. Repository-authored content remains under Apache License 2.0; source and vendored third-party materials retain their respective rights and provenance boundaries.

The formal tag and GitHub Release must point to the exact validated revision without intervening changes.
