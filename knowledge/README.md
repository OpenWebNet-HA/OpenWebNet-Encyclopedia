# Machine-Readable Knowledge Base for LLMs and Automated Tools

This directory contains deterministic exports of the OpenWebNet documentation for ingestion by large language models and other machine processes. It supports complete-context loading, retrieval-augmented generation, claim-level reasoning, automated validation, and structured downstream processing.

The repository's human-readable Markdown pages remain authoritative. Generated records must identify their source page and preserve provenance, evidence status, version scope, protocol namespace, cautions, relationships, and unresolved questions. A machine consumer must be able to distinguish a published protocol fact from implementation evidence, a corroborated interpretation, and an open question.

## Machine-ingestion hierarchy

| Directory | Machine consumer and artifact |
| --- | --- |
| [`llm/`](llm/) | Complete deterministic `llm-corpus.md` for broad LLM context ingestion |
| [`retrieval/`](retrieval/) | Retrieval-ready `chunks.jsonl` for embedding, indexing, and RAG systems |
| [`claims/`](claims/) | Atomic `claims.jsonl` for evidence-aware reasoning, validation, and conflict detection |
| [`reference/`](reference/) | Controlled glossary, namespaces, sources, relationships, cautions, and open questions |
| [`policy/`](policy/) | Mandatory privacy and publication rules applied before machine artifacts are written |
| [`schema/`](schema/) | Machine-readable schemas and format contracts for every generated artifact |
| [`manifest.json`](manifest.json) | Deterministic inventory of the current public artifact set, compatibility versions, and content hashes |
| [`tools/`](tools/) | Deterministic generation, linting, validation, and consistency tooling |

Generated files belong in their audience-specific directory. The current public set is the LLM corpus, retrieval chunks, schemas, and manifest; claims and reference registries remain later phases. Do not mix source documentation, canonical evidence files, or manually maintained protocol prose into this hierarchy.

## Required machine semantics

Every applicable record must preserve:

- a stable identifier;
- its source document and section;
- the relevant `WHO`, diagnostic family, database, or other namespace;
- version and source-revision scope;
- evidence class and confidence;
- normative, implementation-specific, inferred, rejected, or unresolved status;
- cautions and known source contradictions;
- outbound relationships and identifiers;
- sufficient text or structured fields to interpret the record without guessing its namespace.

The generators must produce stable ordering and byte-for-byte repeatable output from the same repository revision. Validation must reject missing provenance, invalid references, namespace leakage, and incompatible duplicate claims.

## Privacy boundary

Every artifact in this directory is public and intended for broad automated distribution. The [Machine Knowledge Privacy Policy](policy/privacy.md) therefore applies before extraction, during normalization, and after generation. Concrete IP addresses, MAC addresses, installed Device IDs, credentials, private capture contents, installation topology, user identifiers, and similar private values must never enter an artifact. Protocol field names and placeholder grammars may be retained without their observed values.

Generation fails closed when a value cannot be classified safely. Redaction occurs before chunking and claim extraction so private text cannot survive in embeddings, metadata, identifiers, logs, or derived records.

## Build and verification

Run `python build.py` to generate the committed manifest, or pass `--output-root PATH` to write only build output beneath a clean temporary directory. Run `python check.py` to verify fresh canonical output, byte-for-byte double-build determinism, manifest schema and serialization, and the privacy publication gate.
