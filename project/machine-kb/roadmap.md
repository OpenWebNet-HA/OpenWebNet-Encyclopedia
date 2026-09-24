# Machine KB Roadmap and Completion State

Snapshot: 2026-09-24, branch `machine-knowledge-base`. A phase is complete only after its acceptance work and checks pass and its state is recorded here. The prior `knowledge/` skeleton predates Phase 0 and is preserved. This table describes implementation state, not the maturity of the human Encyclopedia.

| Phase | Scope / completion gate | State |
| --- | --- | --- |
| 0 | Persist architecture, decisions, maintenance, release gates, review state; verify and commit | **Complete** - this project-control area; no generator delivered |
| 1 | Public consumer contract, IDs, aliases, deterministic serialization, compatibility and versioning | **Complete** - contract and policy reviewed against long-term change cases; no v1 data released |
| 2 | Common schemas and ECV-aligned controlled vocabularies with invalid-case tests | **Complete** - curated schemas, valid/invalid fixtures, offline validator, golden JSONL; no dataset generated |
| 3 | Source classification and pre-extraction privacy pipeline; positive and negative fixtures | **Complete** - closed source-manifest and prepared-source schemas, deterministic local source gate, sanitization, source exclusion, schema tests, and retained final scanner |
| 4 | Canonical Markdown parser and shared semantic IR; exclude guides and prohibited inputs | **Complete** - closed canonical input manifest, curated identities, shared structural IR, guide remediation hints, full-tree integration and tests |
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

## Phase 1 verification

- Reviewed page/heading moves, section splits and rechunking, evidence revisions, namespace collisions, multi-target retirement, cross-language serialization, and privacy withdrawal. Contract rules and remaining implementation checks are recorded in [Consumer Contract](consumer-contract.md#stability-challenge-before-v1).
- Defined ID syntax and lifecycle, manifest discovery, deterministic bytes, ownership, knowledge-state semantics, and compatibility policy. Concrete schemas, registry, golden vectors, and all generated records remain Phase 2 onward.
- Verified: `git diff --check`; `python project/review/checks/check_esg.py .` (0 objective failures); `python project/review/checks/check_ecv.py .` (0 objective failures); relative-link existence across `project/machine-kb/*.md`; `python knowledge/tools/validate_privacy.py` (passed, **0 generated artifacts scanned**). These checks verify the Phase 1 documentation and existing mechanical gates, not an unreleased dataset.

## Phase 3 verification

- Added a closed JSONL source manifest with a fixed classification and source-type vocabulary. Prohibited captures, logs, inventories, configuration exports, screenshots, and private submissions are excluded before their files are opened. Filename/path forms associated with those sources may not be labelled publishable.
- Added deterministic pre-extraction sanitization. It fails closed for an unclassified source, unexpected manifest field, unsafe path, misclassified private source, sensitive material in a `publishable` source, or a `sanitize` source that matches no defined transformation. It emits sorted compact JSONL only after replacing recognised sensitive forms with typed non-reversible markers.
- Added publishable-only privacy metadata and prepared-source schemas with `additionalProperties: false`, plus safe fixtures and unit tests. The existing full-output pattern scanner remains the final publication gate. No test fixture contains a private value.
- Verified: `python -m unittest discover -s knowledge/tests -v`; `python knowledge/tools/validate_privacy.py`; `python -m json.tool knowledge/schema/privacy-metadata.schema.json`; `python -m json.tool knowledge/schema/source-manifest.schema.json`; `python -m json.tool knowledge/schema/prepared-source.schema.json`; `git diff --check`; `python project/review/checks/check_esg.py .`; `python project/review/checks/check_ecv.py .`.

## Phase 2 verification

- Implemented closed Draft 2020-12 common, record variant, and curated ID lifecycle schemas. Evidence, confidence, epistemic standing, typed value state, scoped applicability, privacy, and references are distinct and required.
- Verified seven schema tests covering all record kinds, registry lifecycle, invalid cases, and exact JSONL bytes. Existing ECV/ESG and privacy checks also ran; the privacy scanner still scans zero generated artifacts.
- Cross-artifact integrity, input sanitization, source agreement, and release certification remain later gates.

## Phase 4 verification

- Combined the completed Phase 2 schema work and Phase 3 source gate on this branch; normalized Phase 3 source IDs and privacy removal classes to the consumer contract and Phase 2 vocabulary.
- Parsed all 123 canonical Markdown pages into one internal IR with 1,081 sections. Two public documentation pages require deterministic sanitization. No guide page entered the IR.
- Flagged 183 candidate guide-only factual lines across ten guide pages for human documentation review. This is a heuristic remediation queue, not 183 established omissions; path and line only are emitted.
- Tests cover representative protocol, functional, diagnostics, programming, device-model, internals, reverse-engineering, and procedural guide fixtures, structural preservation, stable identities, unsupported HTML, and byte determinism. No output families have been implemented.

## Next session

Read the architecture, consumer contract, privacy policy, schemas, IR specification, and these decisions. Implement Phase 5's manifest, deterministic rebuild comparison, and common build/check commands from the single IR. Keep guides excluded and review the guide remediation queue before corpus publication. The contract remains pre-release.
