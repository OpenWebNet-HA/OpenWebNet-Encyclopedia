# OpenWebNet Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation or release session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; knowledge/ is its public machine projection.

**Current state (2026-09-30): OpenWebNet Machine KB 0.1.0 is published, and `main` is prepared for the corrective 0.1.1 patch release under intended tag `machine-kb-v0.1.1`.** The patch repairs the released table-context claim rendering defect, aligns schema vocabulary documentation, adds a generated-text hygiene gate, and formalizes the public product name while preserving the 0.1.0 schema/artifact compatibility contract and stable-ID inventory.

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

The [Encyclopedia Core Values](../encyclopedia-core-values.md) govern evidence and epistemic discipline. The [Encyclopedia Style Guide](../encyclopedia-style-guide.md) governs human prose; machine schemas and serialization are separate. The privacy policy is a mandatory publication rule. These project-control pages describe the prepared 0.1.0 release revision. They do not themselves create the Git tag, GitHub Release, or external publication.

**Next:** after exact-commit validation, explicit authorization may create `machine-kb-v0.1.0` on that unchanged revision and publish the matching GitHub Release.
