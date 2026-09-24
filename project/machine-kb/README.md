# Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; `knowledge/` is its public machine projection.

**Current state (2026-09-24): Phase 0 complete.** The `machine-knowledge-base` branch already has the `knowledge/` hierarchy, [privacy policy](../../knowledge/policy/privacy.md), initial [privacy scanner](../../knowledge/tools/validate_privacy.py), and [privacy CI workflow](../../.github/workflows/knowledge-privacy.yml). The generated datasets, schemas, shared parser/IR, consumer contract, and comprehensive checks have not yet been implemented. The existing privacy scanner is an initial final-output check, not a complete privacy guarantee. See the [roadmap](roadmap.md) and [review ledger](review-ledger.md) for exact status.

| File | Use |
| --- | --- |
| [Architecture](architecture.md) | Authority, boundaries, source flow, invariants, planned artifacts |
| [Roadmap](roadmap.md) | Phase gates and verified completion status |
| [Decisions](decisions.md) | Durable decisions and questions still to resolve |
| [Maintenance](maintenance.md) | Change and review workflow |
| [Release and Consumer Contract](release.md) | Planned public interface and release gates; no v1 contract is published yet |
| [Review Ledger](review-ledger.md) | Findings, gaps, and certification state |

The [Encyclopedia Core Values](../encyclopedia-core-values.md) govern evidence and epistemic discipline. The [Encyclopedia Style Guide](../encyclopedia-style-guide.md) governs human prose; machine schemas and serialization are separate. The privacy policy is a mandatory publication rule. These project-control pages describe the planned implementation and do not themselves constitute released schemas or generated data.

**Next:** Phase 1 defines and reviews the consumer contract, identifier grammar, compatibility policy, deterministic serialization, and representation of unknown or contradictory knowledge. Preserve existing files and decisions. Do not populate outputs before their contract and privacy path are specified.
