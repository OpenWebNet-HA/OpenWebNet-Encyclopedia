# Machine KB Roadmap and Completion State

Snapshot: 2026-09-24, branch `machine-knowledge-base`. A phase is complete only after its acceptance work and checks pass and its state is recorded here. The prior `knowledge/` skeleton predates Phase 0 and is preserved. This table describes implementation state, not the maturity of the human Encyclopedia.

| Phase | Scope / completion gate | State |
| --- | --- | --- |
| 0 | Persist architecture, decisions, maintenance, release gates, review state; verify and commit | **Complete** - this project-control area; no generator delivered |
| 1 | Public consumer contract, IDs, aliases, deterministic serialization, compatibility and versioning | Pending - next |
| 2 | Common schemas and ECV-aligned controlled vocabularies with invalid-case tests | Pending |
| 3 | Source classification and pre-extraction privacy pipeline; positive and negative fixtures | Pending - initial policy/scanner/CI already present, not sufficient alone |
| 4 | Canonical Markdown parser and shared semantic IR; exclude guides and prohibited inputs | Pending |
| 5 | Build manifest, deterministic rebuild comparison, and common build/check commands | Pending |
| 6 | Generated LLM corpus and retrieval chunks from the shared IR | Pending |
| 7 | Generated reference registries: namespaces, glossary, sources, entities, relationships, cautions, questions | Pending |
| 8 | Reviewed atomic claim framework and representative fixtures | Pending |
| 9 | Initial claim population, batch 1 | Pending |
| 10 | Initial claim population, batch 2 | Pending |
| 11 | Initial claim population, batch 3 | Pending |
| 12 | Cross-artifact consistency, drift, and change-impact checks | Pending |
| 13 | Full CI, contributor workflow, release machinery | Pending - initial privacy CI already present |
| 14 | Full candidate generation and mechanical cleanup | Pending |
| 15 | Independent factual and epistemic certification of the candidate | Pending |
| 16 | Remediate findings, rerun gates, release and merge when explicitly authorized | Pending |

## Phase 0 verification

- Confirmed the clean remote branch at `8f3f8512f6c779209d618353e255e90842c5bcc2` before edits; existing Machine KB work was retained.
- Added only project-control Markdown and a link from `project/README.md`. No datasets, schemas, generator, or CI behavior changed.
- Verified: `git diff --check`; `python project/review/checks/check_esg.py .` (0 objective failures); `python project/review/checks/check_ecv.py .` (0 objective failures); relative-link existence across these control pages; `python knowledge/tools/validate_privacy.py` (passed, **0 generated artifacts scanned**). These checks do not certify an unreleased dataset.

## Next session

Read [README](README.md), [architecture](architecture.md), [decisions](decisions.md), [release](release.md), the [privacy policy](../../knowledge/policy/privacy.md), and affected existing `knowledge/` files. Implement Phase 1 only; challenge compatibility choices before freezing them. Update decisions, ledger, and this table after its checks. Do not treat the Phase 0 release outline as a published v1 contract.
