# Machine KB Project Control

This directory is the durable operating record for the [Machine-Readable Knowledge Base](../../knowledge/). Read this page and the [roadmap](roadmap.md) at the start of a new implementation session, then inspect the current branch and affected files. The human-readable Encyclopedia remains authoritative; `knowledge/` is its public machine projection.

**Current state (2026-09-25): Phases 0 through 11 complete.** The `machine-knowledge-base` branch has the privacy-gated shared IR, deterministic build/check infrastructure, generated LLM corpus and retrieval chunks, canonical reference registries, the atomic-claim framework, and bounded initial claim populations for every canonical documentation area. The [consumer contract](consumer-contract.md) and [version policy](schema-versioning.md) define the intended interface, but no public dataset has been certified or released. See the [roadmap](roadmap.md) and [review ledger](review-ledger.md) for exact counts, remaining domains, drift/CI work, and certification gates.

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

**Next:** Phase 12 adds cross-artifact consistency, drift, and change-impact checks. Guide documentation defects, full release CI, and independent certification remain open.
