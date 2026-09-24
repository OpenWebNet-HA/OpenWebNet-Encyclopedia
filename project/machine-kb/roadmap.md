# Machine KB Roadmap and Completion State

Snapshot: 2026-09-24, branch `machine-knowledge-base`. A phase is complete only after its acceptance work and checks pass and its state is recorded here. The prior `knowledge/` skeleton predates Phase 0 and is preserved. This table describes implementation state, not the maturity of the human Encyclopedia.

| Phase | Scope / completion gate | State |
| --- | --- | --- |
| 0 | Persist architecture, decisions, maintenance, release gates, review state; verify and commit | **Complete** - this project-control area; no generator delivered |
| 1 | Public consumer contract, IDs, aliases, deterministic serialization, compatibility and versioning | **Complete** - contract and policy reviewed against long-term change cases; no v1 data released |
| 2 | Common schemas and ECV-aligned controlled vocabularies with invalid-case tests | **Complete** - curated schemas, valid/invalid fixtures, offline validator, golden JSONL; no dataset generated |
| 3 | Source classification and pre-extraction privacy pipeline; positive and negative fixtures | **Complete** - closed source-manifest and prepared-source schemas, deterministic local source gate, sanitization, source exclusion, schema tests, and retained final scanner |
| 4 | Canonical Markdown parser and shared semantic IR; exclude guides and prohibited inputs | **Complete** - closed canonical input manifest, curated identities, shared structural IR, guide remediation hints, full-tree integration and tests |
| 5 | Build manifest, deterministic rebuild comparison, and common build/check commands | **Complete** - top-level build/check entry points, canonical serialization, committed manifest and schema, clean double-build gate, and temporary-output support |
| 6 | Generated LLM corpus and retrieval chunks from the shared IR | **Complete** - deterministic full corpus, coherent section chunks, closed retrieval schema, manifest inventory and coverage, freshness and privacy validation |
| 7 | Generated reference registries: namespaces, glossary, sources, entities, relationships, cautions, questions | **Complete** - curated semantic seeds and generated canonical-source records, shared-IR provenance, chunk references, cross-file integrity, high-risk boundary tests |
| 8 | Reviewed atomic claim framework and representative fixtures | **Complete** - eight curated assertions, shared-IR join, source-section review pins, typed claim links, schema and integrity checks |
| 9 | Initial claim population, batch 1 | **Complete** - reviewed `protocol/` and `functional/` claims, exact WHO contexts, source/evidence classifications, preserved conflicts, bounded coverage ledger and duplicate/integrity gates |
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

## Phase 5 verification

- Added top-level `build.py` and `check.py`. The build derives an internal IR digest, inventories the current seven public schema contracts, and writes a canonical `knowledge/manifest.json` without timestamps, random values, absolute paths, network access, or consumer settings.
- Centralized compact UTF-8 NFC JSON/JSONL serialization rejects floats, out-of-range integers, non-NFC strings, duplicate or unsorted JSONL IDs, and unsupported types. JSONL record count support is centralized for later artifact renderers; schemas have no record count.
- `check.py` builds twice in clean temporary roots, compares manifest bytes, validates the manifest schema and exact serialization, verifies the committed manifest is fresh, and invokes the final privacy scan.

## Phase 6 verification

- Generated `knowledge/llm/llm-corpus.md` and `knowledge/retrieval/chunks.jsonl` exclusively from the shared IR. The corpus retains document and section boundaries, source paths, namespace context, and qualification cues. Each retrieval chunk is one nonempty canonical section and carries the same context in a closed schema.
- Committed 1,052 curated chunk identities. The complete canonical set has 123 documents and 1,081 sections; 1,052 content sections emit chunks and 29 empty structural sections are counted separately. All ten procedural guides are excluded, with the existing 183 remediation hints retained in manifest coverage.
- Extended the build manifest with corpus/chunk hashes and record counts, coverage dimensions, and artifact freshness validation. The double-build gate compares every generated artifact byte-for-byte and validates the chunk schema and canonical JSONL.

## Phase 7 verification

- Generated seven canonical registries from reviewed semantic seeds joined to the shared IR: 9 namespaces, 12 glossary terms, 135 sources, 10 entities, 22 relationships, 9 cautions, and 15 open questions. The source registry covers every canonical IR document and 12 directly relevant public evidence sources. The ZigBee specification retains its unresolved publication-provenance caution and question.
- Kept canonical definitions in the glossary. Entity records identify referents and use `defined_in` relationships rather than carrying a second definition. Added explicit relationships and tests for installed identities versus diagnostic and functional addresses, plus Physical Device, Firmware, Module, Object, Configuration, and `slot` boundaries.
- Added stable `reference_ids` to all 1,052 retrieval chunks. Every chunk references its canonical source and namespace; sections that own curated terms, entities, relationships, cautions, or questions reference those records as well.
- Referential-integrity validation rejects duplicate IDs, wrong registry kinds, dangling namespaces, relationships, cautions, questions, provenance documents/sections/sources, relationship endpoints, or chunk references. The manifest inventories and hashes every registry and checks record counts and freshness.
- Verified: `python build.py`; `python check.py`; `python -m unittest discover -s knowledge/tests -v`; `python -m unittest discover -s knowledge/tools -p 'test_schema.py' -v`; `python project/review/checks/check_esg.py .`; `python project/review/checks/check_ecv.py .`; `git diff --check`.

## Phase 8 verification

- Generated exactly eight reviewed atomic claims from one curated input joined to the shared privacy-gated IR. Samples cover WHO/WHAT context, DIMENSION 4/5 transport capacity, installed identity versus address, DIMENSION 30 state, observed gateway N_CONF versus its unresolved sentinel interpretation, and conflicting published authentication label/hex assertions.
- Added required subject entity, namespace, public source and section provenance, evidence class, epistemic status, applicability/version, cautions/questions, typed links, and prepared-section SHA-256. A changed source section blocks the build for review. The two authentication assertions remain separate, reciprocally conflicting, and unresolved.
- The manifest inventories and hashes the generated claims; validators cover missing references, stale source pins, malformed scope and links, asymmetric conflicts, and deterministic bytes. Broad claim population and general drift analysis remain Phases 9-12.
- Verified: `python build.py`; `python check.py`; both unittest suites (24 integration tests and 7 schema tests); ECV/ESG objective checks (zero failures); `git diff --check`.

## Phase 9 verification

- Populated 3,528 reviewed claims across all 71 canonical pages in `protocol/` and `functional/`; the five earlier non-domain framework claims bring the generated total to 3,533. The bounded coverage ledger accounts for all 518 source sections: 482 contain claims and 36 are reviewed structural, navigation, reference-list, or non-assertive sections.
- Added exact namespaces for every represented `WHO`, stable section-topic subject contexts, and the missing official public `WHO` source records. Claims retain source-section pins, public provenance, evidence class, epistemic status, confidence, applicability/version scope, cautions, questions, and typed claim links.
- Preserved seven additional source disagreements as fourteen separate, reciprocally contradicting unresolved claims. These cover Lighting `WHAT 17`, ZigBee Automation direction, ZigBee Energy reset and Frequency/Energy mappings, Multimedia camera range, ZigBee Join indication, and ZigBee `DIMENSION 73` behavior. No source was silently selected.
- Added fail-closed bounded-coverage validation and incompatible semantic-duplicate checks. Existing referential-integrity gates continue to reject duplicate IDs, dangling subjects, namespaces, sources, cautions, questions, relationships, and claim links.
- Verified: `python build.py`; `python check.py`; both unittest suites; ECV/ESG objective checks; privacy scan; `git diff --check`.

## Next session

Read the architecture, consumer contract, privacy policy, schemas, IR specification, reference and claim inputs, and these decisions. Continue Phase 10 with a separately committed bounded domain outside `protocol/` and `functional/`. Keep source-section review pins current only after adjudicating changed assertions and preserve qualified conflicts. The contract remains pre-release.
