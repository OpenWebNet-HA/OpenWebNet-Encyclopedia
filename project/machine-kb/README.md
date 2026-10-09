# OpenWebNet Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation or release session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; knowledge/ is its public machine projection.

**Current candidate (2026-10-09):** all 210 accepted Device definitions are integrated on `docs/devices-foundation`, with 73,915 claims and 7,929 retrieval chunks across 345 canonical documents. The [final expansion report](device-expansion-0014-2026-10-08.md) records source-unit conservation, semantic boundaries and validation. The [merge preparation review](merge-preparation-2026-10-09.md) tracks the final CI, catalogue and review gates. This expanded candidate has not been merged, independently certified or tagged as a new release.

**Published release:** OpenWebNet Machine KB 0.1.1 remains published under tag `machine-kb-v0.1.1` at validated release commit `40db576cae95fa3483121bab3bfdb68ea5e3c706`. That certification and release history applies to its exact revision; it does not certify the Device expansion. The expansion preserves the 0.1.0 public schema and artifact compatibility contract and existing identities.

| File | Use |
| --- | --- |
| [Architecture](architecture.md) | Authority, boundaries, source flow, invariants, and implemented artifact flow |
| [Consumer Contract](consumer-contract.md) | Stable IDs, identity lifecycle, knowledge states, ordering, bytes, ownership, and compatibility boundaries |
| [Schema Versioning](schema-versioning.md) | Compatibility, migration, and release version policy |
| [Roadmap](roadmap.md) | Phase gates and verified completion status |
| [Decisions](decisions.md) | Durable implementation and policy decisions |
| [Maintenance](maintenance.md) | Change and review workflow |
| [Release Gates and Consumer Contract Status](release.md) | Verified final release checklist and authorization boundary |
| [OpenWebNet Machine KB 0.1.1 Release Notes](release-notes.md) | Patch-release changes, compatibility, validation, privacy, consumer use, and licensing |
| [Review Ledger](review-ledger.md) | Findings, gaps, certification state, and final release-readiness disposition |

The [Encyclopedia Core Values](../encyclopedia-core-values.md) govern evidence and epistemic discipline. The [Encyclopedia Style Guide](../encyclopedia-style-guide.md) governs human prose; machine schemas and serialization are separate. The privacy policy is a mandatory publication rule. Historical phase and release records retain their original candidate boundaries. Current candidate status is recorded above; these pages do not themselves authorize a merge, Git tag or GitHub Release.

**Next:** complete the exact-candidate merge gates, then review the merge pull request. Tagging and release of the expanded KB require separate authorization and independent semantic certification.
