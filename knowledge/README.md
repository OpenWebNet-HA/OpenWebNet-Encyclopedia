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
| [`schema/`](schema/) | Machine-readable schemas and format contracts for every generated artifact |
| [`tools/`](tools/) | Deterministic generation, linting, validation, and consistency tooling |

Generated files belong in their audience-specific directory. Do not mix source documentation, canonical evidence files, or manually maintained protocol prose into this hierarchy.

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
