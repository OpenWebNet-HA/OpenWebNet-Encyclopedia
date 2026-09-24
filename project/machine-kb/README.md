# Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; `knowledge/` is its public machine projection.

**Current state (2026-09-24): Phases 0 through 2 complete.** The `machine-knowledge-base` branch has the `knowledge/` hierarchy, [privacy policy](../../knowledge/policy/privacy.md), initial [privacy scanner](../../knowledge/tools/validate_privacy.py), and [privacy CI workflow](../../.github/workflows/knowledge-privacy.yml). The [consumer contract](consumer-contract.md) and [version policy](schema-versioning.md) specify the intended first release interface, but no public dataset has been released. Generated datasets, shared parser/IR, and cross-artifact checks remain pending. Curated [Phase 2 schemas](../../knowledge/schema/README.md) and fixtures now exist. The privacy scanner is an initial final-output check, not a complete privacy guarantee. See the [roadmap](roadmap.md) and [review ledger](review-ledger.md) for exact status.

| File | Use |
| --- | --- |
| [Architecture](architecture.md) | Authority, boundaries, source flow, invariants, planned artifacts |
| [Consumer Contract](consumer-contract.md) | Stable IDs, identity lifecycle, knowledge states, ordering, bytes, ownership, and compatibility boundaries |
| [Schema Versioning](schema-versioning.md) | Compatibility and release version policy |
| [Roadmap](roadmap.md) | Phase gates and verified completion status |
| [Decisions](decisions.md) | Durable decisions and questions still to resolve |
| [Maintenance](maintenance.md) | Change and review workflow |
| [Release and Consumer Contract](release.md) | Planned public interface and release gates; no v1 contract is published yet |
| [Review Ledger](review-ledger.md) | Findings, gaps, and certification state |

The [Encyclopedia Core Values](../encyclopedia-core-values.md) govern evidence and epistemic discipline. The [Encyclopedia Style Guide](../encyclopedia-style-guide.md) governs human prose; machine schemas and serialization are separate. The privacy policy is a mandatory publication rule. These project-control pages describe the planned implementation and do not themselves constitute released schemas or generated data.

**Next:** Phase 3 classifies sources and protects the pre-extraction privacy path. Preserve existing files and decisions. Do not populate outputs before their input classification and privacy path are specified.
