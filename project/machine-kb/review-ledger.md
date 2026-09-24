# Machine KB Review Ledger

Status snapshot: 2026-09-24. This ledger tracks Machine KB implementation and release findings. It does not replace the Encyclopedia's [ECV/ESG review ledger](../review/ecv-esg-review-ledger.md). Record future findings with ID, status, severity, affected paths/records, evidence, required action, reviewer, and verification; preserve superseded findings rather than silently deleting them.

| ID | Status | Severity | Scope and evidence | Required resolution / gate |
| --- | --- | --- | --- | --- |
| MKB-R01 | Open planned work | Release blocker | `knowledge/` has READMEs but no populated generated artifacts or schemas | Complete Phases 1-14 and validate candidate outputs |
| MKB-R02 | Resolved, Phase 3 | Release blocker | Closed source classification, deterministic pre-extraction sanitization, publishable-only privacy schema, safe fixtures, and retained output scan | Consume only prepared records in Phase 4 onward; preserve the scanner as the final publication gate |
| MKB-R03 | Partially resolved | Release blocker | Phase 1 contract and versioning policy now defined; populated ID registry and released v1 interface absent | Allocate and review IDs and enforce cross-artifact references before release |
| MKB-R04 | Partially resolved | Release blocker | Shared parser/IR, deterministic public corpus/chunks, manifest, and clean double-build gate pass; complete CI and cross-artifact checks remain | Complete Phases 7, 12-13; CI must not call an LLM |
| MKB-R05 | Not started | Release blocker | No generated candidate to audit | Complete independent Phase 15 epistemic certification and Phase 16 remediation |
| MKB-R06 | Open remediation review | Substantive | Phase 4 guide check reports 183 candidate factual lines across ten guides, with possible false positives | Review each hint and promote genuine guide-only facts to canonical prose before corpus publication |

No Machine KB candidate has been certified or released. These are explicit known gaps, not defects claimed to be fixed in Phase 0. Phase 0 control-file checks are recorded in [roadmap.md](roadmap.md).

Phase 1 challenge cases (rename, split/merge, revised claim, namespace collision, independent serializer, and private-source exclusion) are documented in [Consumer Contract](consumer-contract.md#stability-challenge-before-v1). Phase 2 must turn those cases into schema and golden-byte fixtures; Phase 3 must implement privacy preconditions.
