# MyOpenCommunity Merge and Compatibility Review

This review starts from closure commit `04a9efa358f3e72d8648d9583807a5127c6e4e1d` and published main `b2717281990c0f09641b44d17b6807bf5dc3efb4`. It reviews the integration's parsing contract, identifier conservation and required PR gates. The [bounded closure review](myopencommunity-closure-review.md) defines research completion and residual questions; this review does not extend its evidence boundary or certify physical Devices.

## Compatibility disposition

The **2.0.0 compatibility candidate is a breaking change** from the published 0.1.0 parsing contract. It is appropriate for merge with its migration guidance, but a consumer must explicitly support it. Merge does not create a Machine KB release or change the immutable 0.2.0 and retained 0.1.2 snapshots. A subsequent release needs exact-revision release validation.

| Reviewed change | Consumer implication |
| --- | --- |
| Original source `artifact_locator` | Resolve repository/revision/file/fingerprints separately from the explanatory Encyclopedia section |
| Provenance `examination` | Retain method, implementation role, direct finding/interpretation, relationship, claim mapping, conditions and limitations |
| Execution versus inspection | Only execution/observation methods carry results; expected-test inspection does not establish a test pass |
| Retrieval `evidence_support` | Preserve reviewed dispositions and original evidence, including deferrals; do not attribute section-wide support to every claim |
| Reconciled chunk ID grammar | Accept retained `rNNNNNN` and integration `moc-rNNNNNN` keys as opaque identities |
| Manifest and artifact versions | Check compatibility before ingestion; claims, references, reading and retrieval use 2.0.0; manifest serialization and lifecycle registry format remain 0.1.0 |
| Static Firmware and dynamic oracle | Distinct methods and execution requirements; no automatic credibility ranking or assertion that these methods ran in the repository review |

An actual original-source record is rejected by the hydrated published-baseline schema. The additions are not optional-field compatibility within its closed objects. The [provenance migration](../machine-kb/provenance-v2-migration.md) and [consumer contract](../machine-kb/consumer-contract.md) describe the new requirements.

## Identifier and content comparison

The hydrated claim bytes on main match the `machine-kb-v0.2.0` LFS object. Comparison uses those full bytes, not the transport pointer. All published lifecycle IDs and aliases remain accounted for. The candidate contains 74,366 claims versus 73,915 on main: 452 additions and one retired editorial summary. Twenty-seven retained statements are corrected or recontextualized while keeping their IDs. They concern Lighting routing scope, WHO 13 PIC evidence, Energy labels, WHO 22 expected tests/RDS, WHO 8 applicability, related open questions and demonstrated WHO 16 environments. These are reviewed corrections, not silent identity reallocations. All 66,466 Device claim records remain identical.

The removed summary is `ownkb:claim:c003080`. Its retained tombstone explains the removal without asserting an equivalent replacement. This review corrects `last_release` to 0.2.0 because that immutable snapshot still contains it. No published ID is reused. The [revision-scoped branch migration](myopencommunity-main-sync-2026-10-09.md) remains distinct from global aliases.

Original MyOpenCommunity sources support 454 distinct current claims. The 176 finding records have 142 claimed, 14 corroborating, 18 deferred and two excluded dispositions. Their examination entries include 283 source inspections, 81 expected-test inspections and 57 helper-execution citations. Shared bodies or executions can appear in several entries; these counts are not independent experiments or completeness certification.

## Corrections in this review

| Defect | Correction and verification |
| --- | --- |
| Retrieval restricted finding IDs to `moc-eNNNN`, while review/common schemas accepted other prefixes | Align retrieval with the existing finding-ID grammar. Synthetic static Firmware and dynamic-oracle evidence now passes through claims, reading and schema-validated retrieval with its qualifications |
| Retired summary's last-release metadata predates its actual latest publication | Record 0.2.0 and assert the retained tombstone's identity, reason and absent equivalence replacement |
| Current schema/architecture/control text still labelled the schema 0.1.0 or described withdrawn releases as available | Distinguish published snapshots from the working 2.0.0 candidate, update working counts and remove a duplicated malformed link |
| Hosted canonical-source audit failures were masked by a pipeline | Require the existing trusted exact-commit status after a real local source audit, and include audit/public-source inputs in its digest |

No claim statement, applicability, confidence, original evidence or finding disposition changes in this review. Regeneration changes only the lifecycle registry and manifest; the existing 2.0.0 candidate version is retained because it is unpublished.

## Fail-closed source validation

The [main compliance run](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/actions/runs/37982601490) reported success even though its source-audit JSON contained six unavailable private artifacts and a missing-artifacts failure. The audit itself returned failure; the default-shell pipeline returned the successful `tee` result. A green status did not establish a completed audit.

The revised local `Device catalogue validation` gate runs the unchanged read-only canonical-source auditor, private catalogue completeness and all Device regressions. A failure prevents a success attestation. Hosted compliance authenticates the result for the exact candidate, validates the public-input digest, checks the artifact manifest and exercises status-transport regressions. It retains only public proof metadata. Archive credentials, private bytes and database probes remain local. The [maintenance procedure](../machine-kb/maintenance.md#private-catalogue-ci-result) defines the broadened gate and revalidation requirements.

Regressions reject missing, pending, failed, superseded, wrong-author, wrong-commit and stale-input proofs; malformed manifests and escaping paths also fail. Controlled audit-failure fixtures cannot publish success or private details. Changed public source bytes, manifests, audit tools or workflows invalidate an earlier proof. This fixes the actual hosted provisioning and masked-failure cause without weakening source validation.

## Validation boundary

Local preflight passes: a fresh build; 12 original-evidence tests, four ID-migration tests, eight schema tests and 12 status-gate tests; all 55 evidence acceptance tests; all four evidence packages; artifact inventory for 807 artifacts; ESG and ECV with zero objective failures; and the canonical-source audit with 25 fingerprints, five databases and zero failures. Preserved repositories and synced source material remain read-only.

The complete hosted KB unit suite, freshness, deterministic double-build, privacy and compliance results must be checked on the final PR head. Its authenticated private-source attestation must match that same SHA and digest. This review does not substitute for those checks or copy an earlier green result to a new commit. The first local full-suite attempt, started before the fixes, was interrupted and is not reported as passing.

The content is complete enough for merge within the closure review's stated bounds. Full historical runtimes, physical captures and product/Firmware associations remain separate follow-up evidence requirements. No merge, release tag or expanded factual certification is authorized by this record.
