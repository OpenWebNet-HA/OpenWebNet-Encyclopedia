# Machine KB Review Ledger

Status snapshot: 2026-09-24. This ledger tracks Machine KB implementation and release findings. It does not replace the Encyclopedia's [ECV/ESG review ledger](../review/ecv-esg-review-ledger.md). Record future findings with ID, status, severity, affected paths/records, evidence, required action, reviewer, and verification; preserve superseded findings rather than silently deleting them.

| ID | Status | Severity | Scope and evidence | Required resolution / gate |
| --- | --- | --- | --- | --- |
| MKB-R01 | Open planned work | Release blocker | `knowledge/` has READMEs but no populated generated artifacts or schemas | Complete Phases 1-14 and validate candidate outputs |
| MKB-R02 | Open planned work | Release blocker | Existing `knowledge/tools/validate_privacy.py` scans generated forms after writing; no source classification, sanitizer, or schema validation yet | Implement Phase 3 pre-extraction protections and final release gates; retain scanner |
| MKB-R03 | Partially resolved | Release blocker | Phase 1 contract and curated Phase 2 schemas/fixtures exist; populated ID registry and released v1 interface absent | Allocate and review IDs and enforce cross-artifact references before release |
| MKB-R04 | Open planned work | Release blocker | No shared parser/IR, determinism checker, or complete CI | Complete Phases 4-5, 12-13; CI must not call an LLM |
| MKB-R05 | Not started | Release blocker | No generated candidate to audit | Complete independent Phase 15 epistemic certification and Phase 16 remediation |

No Machine KB candidate has been certified or released. These are explicit known gaps, not defects claimed to be fixed in Phase 0. Phase 0 control-file checks are recorded in [roadmap.md](roadmap.md).

Phase 1 challenge cases (rename, split/merge, revised claim, namespace collision, independent serializer, and private-source exclusion) are documented in [Consumer Contract](consumer-contract.md#stability-challenge-before-v1). Phase 2 must turn those cases into schema and golden-byte fixtures; Phase 3 must implement privacy preconditions.
