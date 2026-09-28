# Schema, Format, and Release Versioning

**Status:** Active policy for the Machine KB 0.1.0 initial public release, intended tag `machine-kb-v0.1.0`.

Use `MAJOR.MINOR.PATCH` for the shared public contract and independently for each artifact format listed in the manifest. Git tags identify immutable content snapshots. The manifest declares the schema compatibility version, format version for each artifact, generator version, input-content digest, and exact artifact hashes.

A compatible build never requires a consumer to infer version from a Git date or path.

| Change | Version action | Example |
| --- | --- | --- |
| Patch | No consumer parsing or semantic-contract change | Clarify prose or fix a validator/generator while keeping the output contract |
| Minor | Backward-compatible extension within an explicitly declared extension point | Add an optional artifact that manifest readers are defined to ignore when unknown |
| Major | Breaking required field, enum, ID grammar, representation, or removal of a guaranteed file/alias | Rename a mandatory property or change unknown-value semantics |
| Content only | No contract/format version increment; new release snapshot and manifest hashes | Correct a claim's evidence or add a record under an existing schema |

Format and contract versions advance independently. A format change advances that artifact's version. Advance the shared compatibility version when cross-artifact semantics or guarantees change.

A new enum value, required property, or property in an object closed by `additionalProperties: false` is breaking unless the existing contract explicitly defines a compatible extension point and fallback behavior. Calling a field "optional" does not make it compatible with an older strict validator.

A consumer that cannot interpret an artifact's declared major version must reject that artifact rather than guess.

## Initial 0.1.0 baseline

Machine KB 0.1.0 is the first public release and establishes the initial compatibility baseline.

The release publishes:

- schema compatibility version `0.1.0`;
- public artifact/schema format version `0.1.0`;
- stable IDs with lifecycle metadata;
- exact schemas and controlled vocabularies;
- golden serialization bytes;
- manifest hashes and counts;
- migration state with no earlier public release.

The `0.x` version indicates project maturity, not permission to silently break the published contract. After the first public release, breaking contract or format changes require an explicit major-version action under this policy, migration documentation, and release review.

## Stable IDs and lifecycle

Within a compatibility line, canonical IDs and published aliases remain resolvable. IDs never change meaning and are never reused.

Deprecation records a reason and replacement mapping where valid. Retired IDs remain tombstones. A split may have multiple replacements and must not imply automatic equivalence.

Old Git-tagged releases remain immutable snapshots. New releases do not promise to ship obsolete factual records forever, but tombstones preserve identity and correction history.

Privacy or licensing withdrawal overrides normal retention. Remove exposed content immediately, retain only a non-sensitive withdrawal/tombstone where safe, publish corrected release notes, and invalidate compromised release artifacts. Never retain a private value merely to preserve ID stability.

## Release implementation rule

Before creating a release tag:

1. Run the complete release validation on the exact intended revision.
2. Verify committed artifacts are fresh and deterministic.
3. Verify schema compatibility and per-artifact versions.
4. Verify manifest hashes/counts and privacy gates.
5. Verify migration notes for any breaking change.
6. Verify the intended tag does not already exist.
7. Tag exactly the validated commit without intervening changes.

Release notes identify contract/artifact versions, migration impact, privacy/licensing boundaries, and the semantic candidate lineage.

For Machine KB 0.1.0, the intended initial-release tag is `machine-kb-v0.1.0`.
