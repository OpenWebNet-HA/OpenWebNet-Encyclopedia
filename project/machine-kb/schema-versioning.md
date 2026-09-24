# Schema, Format, and Release Versioning

**Status:** Phase 1 policy for implementation; no initial public release has occurred.

Use `MAJOR.MINOR.PATCH` for the shared public contract and independently for each artifact format listed in the manifest. Use Git commits and release tags for content snapshots. The manifest declares the contract version, format version for each file, generator version, input-content digest, and exact artifact hashes. A schema `$id` or equivalent refers to its compatible schema version; Phase 2 defines exact schema filenames and fields. A compatible build never requires a consumer to infer version from a Git date or path.

| Change | Version action | Example |
| --- | --- | --- |
| Patch | No consumer parsing or semantic change | Clarify prose, fix validator or generator while keeping output contract |
| Minor | Backward-compatible extension within a previously declared extension point | Add an optional artifact that manifest readers are explicitly required to ignore when unknown |
| Major | Breaking required field, enum, ID grammar, representation, or removal of a guaranteed file/alias | Rename a mandatory property or change unknown semantics |
| Content only | No contract/format version increment; new Git snapshot and manifest hashes | Correct a claim's evidence or add a record under existing schema |

Format and contract versions advance independently: a format change advances that artifact's version; advance the shared contract when cross-artifact semantics or guarantees change. A new enum, required property, or property in an object closed by `additionalProperties: false` is major unless v1 explicitly reserved an extension point with defined fallback behavior. Calling a change "optional" does not make it compatible with a strict old validator. At v1, publish exact compatibility rules alongside the actual schemas, including unknown enum handling. A consumer that cannot interpret an artifact's declared major version must reject that artifact rather than guess.

Within a major line, canonical IDs and published aliases remain resolvable; IDs never change meaning or get reused. Deprecation is announced with reason and replacement mapping where valid. Keep tombstones in the registry. A schema major change supplies a migration document and, where feasible, a machine-readable alias map. Old Git-tagged releases remain immutable snapshots. New releases do not promise to ship obsolete factual records forever; tombstones preserve identity and correction history.

Privacy or licensing withdrawals can override normal retention: remove exposed content immediately, record a non-sensitive withdrawal/tombstone where safe, publish corrected release notes and invalidate compromised release artifacts. Do not retain a private value to honor ID stability; never expose an old ID derived from one. A contract guarantee applies only to publishable data.

Before v1, the contract and schemas may change with reviewed decision-log entries; versions described here are a planned policy, not a claim that a stable v1 already exists. A release must include migration notes for any breaking change and pass the [release gates](release.md).
