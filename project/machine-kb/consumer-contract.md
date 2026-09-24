# Machine KB Consumer Contract

**Design status:** Phase 1 contract, approved for implementation on `machine-knowledge-base`; no dataset or schema has been released. The first release must satisfy this contract and its concrete schemas before consumers rely on it. The human-readable Encyclopedia remains authoritative. The dataset is transport-neutral and can be consumed offline without a model, server, MCP, FastMCP, or a particular programming language.

## Publication surface

A release publishes `knowledge/manifest.json` as the inventory and version entry point. It lists each public artifact by repository-relative path, artifact format version, SHA-256 of its exact bytes, and record count where applicable. Its own hash is not included in itself. The initial artifact families are `knowledge/llm/llm-corpus.md`, `knowledge/retrieval/chunks.jsonl`, `knowledge/claims/claims.jsonl`, and the reference registries under `knowledge/reference/` (entities, namespaces, glossary, public sources, relationships, cautions, and open questions). The manifest enumerates actual files; an empty directory or README is not an artifact. Exact reference registry file names and record schemas are fixed in Phase 2 before the first release. Schema files under `knowledge/schema/` are also inventoried. Only listed artifacts and schema files constitute the versioned public interface; tools and project-control Markdown are not machine data.

All records must carry the schema-defined stable ID, namespace/context, source provenance, evidence/epistemic qualification, applicability/version scope, privacy classification, and relevant relationships or cautions. Source locations use public repository-relative paths and section IDs, never private evidence paths. The manifest contains an input-content digest, generator version, schema compatibility version, and artifact hashes; it contains no nondeterministic timestamp or circular digest of its own bytes. The public source license remains applicable; generated material does not acquire rights to underlying publisher sources.

## Stable IDs

Canonical grammar (ASCII, lowercase):

```text
id       = "ownkb:" kind ":" key *(":" key)
key      = alpha *(alpha / digit / "-")
alpha    = "a" ... "z"
digit    = "0" ... "9"
kind     = "document" / "section" / "namespace" / "entity" /
           "source" / "claim" / "chunk" / "relationship" /
           "caution" / "question" / "term"
```

Keys must begin with a letter, end with a letter or digit, contain no adjacent hyphens, and be at most 63 characters each. An ID is at most 255 ASCII bytes. The kind and keys are case-sensitive; an ID with other spelling is invalid, not an alternate match. This grammar defines syntax, not automatic allocation. A curated ID registry and validator will guard uniqueness, aliases, retirement, and reuse before public records exist.

Allocation rules:

- Document: `ownkb:document:diagnostics-dimensions`; section: `ownkb:section:diagnostics-dimensions:dim-thirty`. Section keys are explicit durable anchors within a document, not heading text, ordinal, or slug generated afresh. A document move keeps both IDs.
- Namespace: `ownkb:namespace:who`; entity: `ownkb:entity:who:lighting` or `ownkb:entity:device-model:physical-device`. Entity namespace keys identify context, not numeric equality across namespaces.
- Claim: `ownkb:claim:c000001`; chunk: `ownkb:chunk:r000001`; public source: `ownkb:source:s000001`; relationship: `ownkb:relationship:x000001`; caution: `ownkb:caution:k000001`; question: `ownkb:question:q000001`; term: `ownkb:term:physical-device`. Opaque tokens are allocated and tracked, never recomputed from prose or source offsets. These are illustrative IDs, not records or claims.
- An ID identifies one semantic unit for its lifetime. A changed title, file path, serialization, or corrected wording does not change the ID if the unit's meaning remains continuous. Materially different meaning gets a new ID and explicit replacement/deprecation metadata. A split or merge retains an old ID only where one resulting unit has genuinely continuous identity; otherwise retire it and link all replacements. Never silently repurpose an old ID.
- No ID component may derive from private observed values, hash private data, or encode an installation-specific identifier. Public protocol numbers are allowed only in their explicit namespace. Do not infer semantic identity from equal numbers or matching slugs.

IDs are public stable references, not resolvable URLs and not a promise that a claim's statement or confidence will never change. Record paths and section locations are metadata, not identity. A reference can target a canonical live ID or a retained alias/tombstone; validation rejects dangling targets.

## Aliases, deprecation, and removal

The curated registry retains every published canonical ID and its history. Each alias maps to exactly one canonical ID, with reason and first release. Alias chains and cycles are forbidden; resolve in one step. Aliases are for identity-preserving renames and legacy spellings, not for claiming equivalence between genuinely different meanings. Published aliases remain resolvable indefinitely within a major contract line. Never assign an alias or retired ID to a different unit.

Deprecation marks a live ID as discouraged and supplies a reason and optional replacement IDs. A retired ID remains as a tombstone with its kind, reason, last release, and zero or more `replaced_by` targets; a split may have several targets, so consumers must not automatically substitute one. A tombstone cannot be used as a current factual record. If a fact is rejected or superseded, retain its epistemic history separately from ID lifecycle. Removal of an alias/tombstone or breaking of its resolution guarantee requires a major compatibility version and migration notes; privacy removal can require urgent withdrawal as described in [versioning](schema-versioning.md).

## Meaning of incomplete or conflicting knowledge

Separate three axes. A record's `epistemic_status` describes the evidence-backed standing of its assertion; a value's `value_state` describes whether a value is supplied; `applicability.state` describes whether a proposition applies in its explicitly identified scope. Exact enum sets and shapes are defined in Phase 2, but these semantics are binding:

| Situation | Required representation | Consumer interpretation |
| --- | --- | --- |
| Known value | `value_state = known` and typed value | Use only with attached namespace, provenance, and scope |
| Unknown value | `value_state = unknown`, no invented value, with reason or open-question reference | No assertion about the value or its absence |
| Not applicable | `applicability.state = not_applicable` with identified scope and reason; no purported value for that scope | Only that scope is excluded; not a global negative |
| Unresolved interpretation | Open question and qualified competing interpretations or explicit unresolved status, with provenance | Do not choose one interpretation as established |
| Contradictory evidence | Distinct attributable statements linked by an explicit contradiction relationship and scope, with an open resolution if needed | Do not collapse them into an unconditional merged fact |
| Rejected or superseded interpretation | Explicit epistemic history and links to supporting correction | Do not treat a historical claim as current fact |

Missing mandatory fields are invalid. JSON `null`, absent fields, empty strings, and empty arrays do not silently mean unknown, not applicable, or contradicted. Phase 2 schemas may permit optional fields where they have a documented meaning. A missing *record* means no published assertion; it must not be read as a negative assertion. Consumers must retain evidence class, cautions, transport/device/version limits, and namespace context when presenting or transforming records.

## Ordering and bytes

All generated text is UTF-8 without BOM, Unicode NFC, LF line endings, and exactly one trailing LF for nonempty files. Empty JSONL files are zero bytes. JSONL has one compact JSON object per line, no blank lines, sorted by canonical ID in ASCII byte order. Within objects, field names are ASCII and sorted in byte order. No insignificant JSON whitespace or escaped printable Unicode/slashes; use standard escapes for quote, backslash, and controls (`\b`, `\f`, `\n`, `\r`, `\t`, otherwise lowercase `\u00xx`). No floating-point JSON numbers: exact decimal quantities use schema-defined strings, and integers must lie within the exact interoperable range `[-9007199254740991, 9007199254740991]`. Duplicate object keys and non-NFC strings are invalid. Arrays representing sets sort by canonical ID or schema-defined key and contain no duplicates; ordered semantic sequences retain their explicit order. The standalone manifest uses the same compact JSON rules and one trailing LF. The corpus Markdown uses UTF-8/NFC/LF and a fixed source/section order defined by its format version in Phase 6; no traversal-order or current-time dependence.

Record order is for reproducibility, not semantic ranking. Same canonical inputs, curated inputs, schemas, and generator version must yield byte-for-byte identical artifacts. No network or LLM call is permitted during a build or CI. The initial generator must publish golden serialization examples before release so independent implementations can verify exact bytes.

## Ownership and compatibility

Canonical Encyclopedia Markdown and public provenance are edited by authors. ID/alias registry and reviewed structured claim inputs are curated in Git and checked against canonical prose. All manifest, LLM corpus, retrieval, reference, and claim outputs are generated from one normalized IR; do not hand-edit them. A reviewed claim input enters the same IR and must not override its source. Generated schema files, if any, must declare their ownership; Phase 2 schemas are curated source contracts unless explicitly marked generated.

The [version policy](schema-versioning.md) states compatibility guarantees and limits. Consumers can rely on published IDs, manifest inventory, schemas, documented semantics, and versioned file formats within a compatibility line. They cannot rely on a fixed record count, ordering as priority, unchanged wording, unchanged source paths, completeness of all real-world behavior, or an unqualified meaning for numeric values. This contract does not prescribe APIs, embeddings, tokenization, programming-language objects, or a server.

## Stability challenge before v1

| Change pressure | Decision that prevents avoidable breakage | Residual risk / release check |
| --- | --- | --- |
| Page or heading renamed | Curated document/section IDs survive location changes | Parser needs stable anchor mapping and redirect verification |
| Long section split or rechunked | Opaque chunk IDs and explicit retirement/replacement | Review unit continuity; no hash/ordinal IDs |
| Evidence revises a claim | Keep ID only for continuous assertion; preserve provenance, epistemic history, contradiction links | Reviewer must judge whether semantic identity changed |
| One value used in two protocol namespaces | Entity IDs carry namespace; records require context | Schema and validator must reject context leakage |
| Two interpretations split one entity | Multiple replacements; no automatic alias to either | Consumer must handle tombstone with several targets |
| Consumer written in another language | Restricted numeric model and specified bytes | Publish golden vectors and independent round-trip test |
| Private source is accidentally included | Source exclusion before IR, restricted schema, final scan and release gate | Existing scanner alone cannot prove safety; block release until Phase 3 |

Phase 2 must test these cases against real schemas. Any resulting contract change before the first release must be recorded here and in [decisions](decisions.md); after release it follows semantic compatibility rules.
