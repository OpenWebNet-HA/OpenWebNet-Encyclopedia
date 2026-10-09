# OpenWebNet Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation or release session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; knowledge/ is its public machine projection.

**Current status (2026-10-09):** all 210 accepted Device definitions and their Machine KB integrations are merged through [PR #48](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/pull/48) and published in [OpenWebNet Machine KB 0.2.0](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/releases/tag/machine-kb-v0.2.0), tag `machine-kb-v0.2.0`, validated revision `447e4c731f44c1e753efb33f245be5444f15912c`. The dataset contains 73,915 claims and 7,929 chunks across 345 canonical documents. Independent Phase 15 assessment and all exact-release mechanical gates passed.

**Published release:** [OpenWebNet Machine KB 0.2.0](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/releases/tag/machine-kb-v0.2.0) includes a hydrated offline bundle and `SHA256SUMS`. The [release notes](release-notes.md) and [audited statistics](release-statistics-0.2.0.json) describe its coverage of 541 catalogue commercial records and scoped inspection of 734 distinct PDFs. Release 0.1.2 remains the retained historical comparison baseline; earlier 0.1.0/0.1.1 tags and releases were withdrawn during archive/history cleanup. Historical certification records retain their exact-revision scope. The 0.1.0 schema/artifact contract and prior stable identities remain unchanged.

| File | Use |
| --- | --- |
| [Architecture](architecture.md) | Authority, boundaries, source flow, invariants, and implemented artifact flow |
| [Consumer Contract](consumer-contract.md) | Stable IDs, identity lifecycle, knowledge states, ordering, bytes, ownership, and compatibility boundaries |
| [Schema Versioning](schema-versioning.md) | Compatibility, migration, and release version policy |
| [Roadmap](roadmap.md) | Phase gates and verified completion status |
| [Decisions](decisions.md) | Durable implementation and policy decisions |
| [Maintenance](maintenance.md) | Change and review workflow |
| [Release Gates and Consumer Contract Status](release.md) | Verified final release checklist and authorization boundary |
| [OpenWebNet Machine KB 0.2.0 Release Notes](release-notes.md) | Coverage, changes, compatibility, validation, privacy, consumer use, and licensing |
| [Review Ledger](review-ledger.md) | Findings, gaps, certification state, and final release-readiness disposition |

The [Encyclopedia Core Values](../encyclopedia-core-values.md) govern evidence and epistemic discipline. The [Encyclopedia Style Guide](../encyclopedia-style-guide.md) governs human prose; machine schemas and serialization are separate. The privacy policy is a mandatory publication rule. Historical phase and release records retain their original candidate boundaries. Current candidate status is recorded above; these pages do not themselves authorize a merge, Git tag or GitHub Release.

**Next:** maintain the released evidence and consumer contract as new evidence arrives. The Device description and KB ingestion queues are complete; no further batch or schema migration is required.
