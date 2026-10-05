# Consuming the OpenWebNet Machine KB

The **OpenWebNet Machine KB** (shortened to **Machine KB** where the context is clear) is a static, deterministic, consumer-neutral dataset. It does not require an LLM, an MCP server, Python, a vector database, embeddings, or network access. Those are optional consumer choices.

Start with [`manifest.json`](manifest.json). It is the inventory and version entry point for the public machine artifacts. Only manifest-listed artifacts and schemas are part of the versioned machine interface.

## Choose the artifact for the job

| Goal | Primary artifact | Typical use |
| --- | --- | --- |
| Give an LLM broad or complete project context | [`llm/llm-corpus.md`](llm/llm-corpus.md) | Direct model context, long-context analysis |
| Search and retrieve relevant sections | [`retrieval/chunks.jsonl`](retrieval/chunks.jsonl) | RAG, lexical search, vector search, hybrid retrieval |
| Reason over atomic assertions and evidence | [`claims/claims.jsonl`](claims/claims.jsonl) | Evidence-aware answers, validation, conflict handling |
| Resolve namespaces, entities, sources, cautions, relationships, and open questions | [`reference/`](reference/) | Metadata hydration and structured reasoning |
| Discover formats, hashes, counts, and compatibility | [`manifest.json`](manifest.json) and [`schema/`](schema/) | Startup validation and update handling |

The human-readable Encyclopedia remains authoritative. Machine artifacts are deterministic projections of that documentation and public provenance.

## Always begin with the manifest

A consumer should:

1. Read `knowledge/manifest.json`.
2. Check that `schema_compatibility_version` and the format versions it needs are supported.
3. Use the manifest paths rather than assuming that every file under `knowledge/` is a public artifact.
4. Optionally verify the SHA-256 hash of each artifact before loading it.
5. Treat record counts as integrity metadata for that snapshot, not as a compatibility guarantee.

A consumer that cannot interpret a declared major format or compatibility version must reject that artifact rather than guess.

## Direct LLM context

For a model with sufficient context capacity, [`llm/llm-corpus.md`](llm/llm-corpus.md) is the simplest ingestion path.

Load the corpus as context and preserve its document and section boundaries, stable IDs, namespace context, provenance cues, applicability cues, cautions, and uncertainty cues. Do not strip those qualifiers merely to reduce prompt size.

The corpus is appropriate when the application benefits from broad context and does not need a retrieval index. If the model cannot accommodate the corpus comfortably, use the retrieval corpus instead of arbitrarily truncating the beginning or end.

An LLM consuming the corpus should be instructed to preserve the distinction between published specification, implementation evidence, observation, inference, contradiction, rejection, and unresolved knowledge.

## Retrieval and RAG

[`retrieval/chunks.jsonl`](retrieval/chunks.jsonl) is the intended retrieval projection. Each JSONL record is one nonempty canonical section rather than an arbitrary token window.

Each record includes:

- a stable chunk ID;
- document and section IDs;
- source path and section hierarchy;
- namespace context;
- provenance;
- privacy classification;
- qualification cues;
- stable `reference_ids`;
- the section text.

A typical ingestion flow is:

```text
manifest.json
    |
    v
chunks.jsonl
    |
    +--> lexical, vector, or hybrid index
    |
    v
retrieve relevant chunks
    |
    +--> resolve reference_ids when useful
    |
    v
LLM or other consumer
```

Index the chunk `text` together with enough metadata to return its stable ID, source/document/section identity, namespace context, qualification cues, and `reference_ids`.

The Machine KB chunks are already semantic section units. Consumers should normally index them intact. If an external system must subdivide a chunk, the resulting subchunks are consumer-local objects: retain the parent `ownkb:chunk:` ID and Machine KB metadata rather than inventing new Machine KB IDs.

Retrieval rank or vector similarity is not evidence strength. A highly ranked unresolved, hypothetical, rejected, superseded, contradicted, or narrowly applicable record remains qualified exactly that way.

## Atomic claims and reference data

[`claims/claims.jsonl`](claims/claims.jsonl) is useful when an application needs assertion-level reasoning rather than section-level retrieval.

A claim carries its stable ID, statement, subject, namespace/context, applicability and version scope, provenance, evidence class, epistemic status, confidence, value state, cautions, open questions, relationships, source-section digest, and typed links to other claims.

Load claims and the registries under [`reference/`](reference/) into maps keyed by stable `ownkb:` ID. When a retrieved claim or chunk references a caution, question, relationship, entity, namespace, or source, resolve the referenced record rather than interpreting the ID itself.

In particular:

- `unresolved` and `hypothesis` are not established facts;
- `rejected` and `superseded` are preserved history, not current guidance;
- contradictory claims remain distinct attributable records;
- `applicability` and version scope limit the assertion;
- absence of a record is not a negative assertion;
- equal numeric values in different namespaces do not imply identity.

For the 2.0.0 working contract, resolve every provenance entry rather than treating the first entry as the original source. `canonical_documentation` identifies the explanatory page. An original implementation source has `artifact_locator` with repository, revision, path, fingerprints and public locator. Its provenance `examination` records method, role, direct finding versus interpretation, relationship, code/offset location, applicable claim IDs, conditions and limitations. Only execution methods contain an execution result.

Retrieval `evidence_support` carries reviewed findings, claim IDs and dispositions, including deferred and excluded findings. Preserve it alongside the text and resolve its original source IDs. Mixed sections can retain specification claims while adding implementation claims; never assign a section's strongest method to every sentence or claim. Confidence is a separate claim field, with no method ranking. See [Provenance contract migration](../project/machine-kb/provenance-v2-migration.md).

The exact field vocabulary is documented in [`schema/README.md`](schema/README.md) and enforced by the JSON Schemas.

## MCP adapters

MCP and FastMCP are external consumers of the Machine KB. The project intentionally does not prescribe a server implementation, transport, programming language, embedding model, or tool naming scheme.

A practical MCP server can initialize as follows:

```text
read manifest
    |
    +--> verify supported versions and optional hashes
    |
    +--> load/index retrieval chunks
    |
    +--> load claims by stable ID
    |
    +--> load reference registries by stable ID
    |
    v
expose consumer-defined MCP resources/tools
```

Illustrative MCP operations might include:

```text
search_knowledge(query)
get_chunk(id)
get_claim(id)
get_entity(id)
get_source(id)
get_question(id)
```

These names are examples only and are not part of the Machine KB contract.

An MCP adapter should return the Machine KB qualifications needed to interpret a result, not only the text that matched. It should not silently collapse contradictory records, promote an inference to specification, drop applicability/version scope, or rewrite stable IDs.

A useful server can expose the manifest itself as a resource so clients can inspect the exact dataset and compatibility versions behind an answer.

## Minimal consumer algorithm

A technology-neutral consumer can follow this sequence:

```text
manifest = parse("knowledge/manifest.json")
require_supported(manifest.schema_compatibility_version)

for artifact in manifest.artifacts:
    if artifact is needed:
        optionally_verify_sha256(artifact.path, artifact.sha256)
        load_using_declared_format(artifact.path, artifact.format_version)

index retrieval chunks if search is needed
key claims and reference records by stable ID
preserve namespace, provenance, epistemic status, applicability, cautions, and questions
```

JSONL files contain one canonical JSON object per line. Consumers should parse each line independently and validate against the published schema when strict validation is useful.

## Updating a consumer

Git tags identify immutable content snapshots. The manifest identifies the contract and artifact versions for a snapshot.

When moving to a newer release:

1. Compare the manifest compatibility and artifact format versions.
2. Reject unsupported major versions.
3. Compare artifact hashes to determine what changed.
4. Rebuild only the consumer indexes or caches affected by changed artifacts if desired.
5. Honor aliases, deprecations, and tombstones in [`id-registry.json`](id-registry.json).
6. Never reuse a retired ID for a different meaning.

Content can change without a schema version change. Consumers must therefore use release identity and manifest hashes when they need exact reproducibility.

## What the Machine KB does not require

A conforming consumer does not need:

- MCP or FastMCP;
- an LLM;
- embeddings;
- a vector database;
- Python, JavaScript, or another particular language;
- LangChain, LlamaIndex, or another framework;
- OpenAI, Anthropic, or another model provider;
- network access.

Those technologies can be useful adapters around the dataset, but none is part of the published Machine KB interface.
