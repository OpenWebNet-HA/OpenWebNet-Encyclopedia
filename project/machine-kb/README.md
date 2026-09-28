# Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation or release session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; knowledge/ is its public machine projection.

**Current state (2026-09-28): the Machine KB is integrated into main, and bounded current-main release verification has passed for semantic/content candidate a819104eed5d8431478ef933235a616cde71a092.** Historical lineage is preserved: independently certified candidate 5e5dda65b6ba8d5f4da2ec69126d4a9452455c50, previous reconciled candidate 888706f39f4c3f5dba2a49db628b09011714084b, and previous readiness/control commit d4757986f8b35bcb7bb997a3fae9ef074bf437ec. The current candidate includes the reviewed post-readiness WHO 1 dimmer/MH200 and WHO 2/LN4660M2 additions plus bounded Machine KB remediation. No Git tag, GitHub Release, external publication, or released v1 interface has been created.

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

**Next:** wait for explicit authorization before tag creation, GitHub Release creation, external publication, or any released-v1 declaration. The Machine KB is already integrated into main.
