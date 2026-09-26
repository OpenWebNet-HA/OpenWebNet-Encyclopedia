# Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation or release session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; knowledge/ is its public machine projection.

**Current state (2026-09-26): implementation, remediation, independent recertification, and the final release checklist are complete.** The independently certified semantic candidate is 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50; the final checklist verified release-content revision b1560324c0b5733614e8eb90cd4f9d04b96edfa9 and found no generated or semantic corpus changes after certification. The branch remains pre-release and has not been merged, tagged, published, or declared as a released v1 interface.

| File | Use |
| --- | --- |
| [Architecture](architecture.md) | Authority, boundaries, source flow, invariants, and implemented artifact flow |
| [Consumer Contract](consumer-contract.md) | Stable IDs, identity lifecycle, knowledge states, ordering, bytes, ownership, and compatibility boundaries |
| [Schema Versioning](schema-versioning.md) | Compatibility, migration, and release version policy |
| [Roadmap](roadmap.md) | Phase gates and verified completion status |
| [Decisions](decisions.md) | Durable implementation and policy decisions |
| [Maintenance](maintenance.md) | Change and review workflow |
| [Release Gates and Consumer Contract Status](release.md) | Verified final release checklist and authorization boundary |
| [Planned Initial Release Notes](release-notes.md) | Candidate identity, versions, migration state, privacy, consumer use, and licensing |
| [Review Ledger](review-ledger.md) | Findings, gaps, certification state, and final release-readiness disposition |

The [Encyclopedia Core Values](../encyclopedia-core-values.md) govern evidence and epistemic discipline. The [Encyclopedia Style Guide](../encyclopedia-style-guide.md) governs human prose; machine schemas and serialization are separate. The privacy policy is a mandatory publication rule. These project-control pages describe the pre-release candidate and do not themselves constitute a published dataset.

**Next:** wait for explicit authorization before any merge to main, tag creation, GitHub Release, publication, or released-v1 declaration.
