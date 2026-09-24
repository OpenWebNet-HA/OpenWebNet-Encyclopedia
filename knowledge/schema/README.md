# Machine KB Schemas and Controlled Vocabulary

**Pre-release Phase 2 contract (schema revision `0.1.0`, not a published dataset version).** These curated JSON Schema Draft 2020-12 files are implementation inputs, not generated outputs. They specify common JSONL record shapes for the planned reference registries, claims, and retrieval chunks. No public records or manifest are released yet. The human Encyclopedia remains authoritative. See the [consumer contract](../../project/machine-kb/consumer-contract.md) and [privacy policy](../policy/privacy.md).

| Schema | Applies to |
| --- | --- |
| [`common.schema.json`](common.schema.json) | Stable IDs, provenance, privacy, applicability, version scope, and value states |
| [`record.schema.json`](record.schema.json) | `namespace`, `entity`, `source`, `relationship`, `caution`, `question`, `term`, `claim`, and `chunk` records; closed variant shapes |
| [`id-registry.schema.json`](id-registry.schema.json) | Curated canonical ID lifecycle and one-step aliases (not generated JSONL) |
| [`manifest.schema.json`](manifest.schema.json) | Deterministic published-artifact inventory, hashes, record counts, coverage metrics, and fixed build compatibility metadata |
| [`retrieval-chunks.schema.json`](retrieval-chunks.schema.json) | Closed records derived from canonical IR sections, with source context, privacy, and qualification cues |

The planned reference JSONL names are `knowledge/reference/namespaces.jsonl`, `entities.jsonl`, `sources.jsonl`, `relationships.jsonl`, `cautions.jsonl`, `questions.jsonl`, and `glossary.jsonl` (the `term` variant). Claims use `knowledge/claims/claims.jsonl`; retrieval uses `knowledge/retrieval/chunks.jsonl`. The curated ID registry's location will be set with the parser/curation inputs before publication. The manifest and Markdown corpus formats are later phases. Each JSONL file contains only its named variant. A file cannot be inferred from a bare schema validation; a future build must enforce path-to-kind mapping and cross-file references.

## Meaning of controlled fields

Three independent axes must be retained. `epistemic_status` describes the claim's standing; `value.state` says whether a typed value is supplied; `applicability.state` concerns a specified domain and target, with explicit version scope. `known` requires exactly one of `text`, `integer`, or `boolean`. `unknown`, `unresolved`, and `contradictory` require a reason and prohibit a supplied value. `not_applicable` requires a scoped reason and prohibits a known value. No null or missing required field means unknown. Exact decimal quantities use `text`, not floating-point JSON numbers.

| Vocabulary | Values and use |
| --- | --- |
| `epistemic_status` | `specified` (published normative specification), `catalogue_documented` (catalogue/database assertion), `observed` (public observation), `experimentally_confirmed` (repeatable public test), `corroborated_interpretation` (converging evidence), `inferred` (reasoned interpretation), `hypothesis` (untested explanation), `unresolved`, `contradicted`, `superseded`, `rejected`. A normative status is never inferred solely from syntax or observed support. |
| `confidence` | `high`, `medium`, `low`, `undetermined`; independent of evidence class and coverage. |
| `evidence_class` | `official_specification`, `official_catalogue`, `public_database`, `public_capture`, `public_experiment`, `configuration_software`, `implementation_artifact`, `firmware_interface`, `prior_validated_research`, `canonical_documentation`. Each provenance item identifies a canonical public page and section; a required `source_id` attributes every external evidence class; canonical documentation may omit it. `canonical_documentation` alone does not claim external corroboration. |
| `applicability.state` | `applies`, `unknown`, `not_applicable`. The `domain`, `target`, and version `state` (`specified` with expression, `unknown`, or `not_versioned`) narrow the assertion. A version expression is descriptive until a future controlled syntax is justified by source material. |
| `predicate` | `part_of`, `has_part`, `documents`, `evidenced_by`, `applies_to`, `defined_in`, `related_to`, `contradicts`, `supersedes`, `replaces`, `qualifies`. A contradiction is a relationship between distinct attributable records; it does not merge their assertions. |
| `privacy.classification` | `public` with no removed classes; `sanitized` with at least one controlled removed-value class. Neither allows private values in content. |

`context.namespace_id` is always explicit, even for source and question records. `context.description` disambiguates uses within a namespace; protocol numbers alone do not establish relationships. `relationships`, `cautions`, and `questions` are required set arrays and may be empty when none are known. An `unresolved` record requires a question ID; `contradicted` requires both question and relationship IDs. Consumers must inspect the referenced records; presence of an ID alone does not settle evidence. `superseded` and `rejected` are preserved historical standings, never unconditional current guidance. Source path strings are public repository-relative Markdown paths and must be checked against actual non-guide canonical pages before publication.

Schemas reject unknown properties. Adding a property or enum member after v1 is a major format change unless an explicit compatible extension point is introduced. IDs have a closed kind vocabulary and 63-byte key limit. The registry requires reasons for deprecation and retirement and preserves multi-target replacements without claiming equivalence. The validator additionally checks collisions, alias chains, target existence, ordering, NFC, duplicate JSON keys, exact integer range, and canonical byte serialization. Referential integrity across artifacts, replacement continuity, claim/source agreement, sanitized provenance, and coverage are later gates and require review beyond JSON Schema.

## Tests and golden bytes

Install `python -m pip install -r knowledge/tools/requirements-schema.txt`, then run `python -m unittest discover -s knowledge/tools -p test_schema.py`. [`fixtures/valid/golden.jsonl`](fixtures/valid/golden.jsonl) is an exact two-record serialization vector. The valid and invalid fixtures exercise every record kind, registry lifecycle, evidence, namespace, privacy, applicability, incomplete knowledge, contradictory status, and byte rules. Fixtures are synthetic protocol concepts with no observed installation data. The validator is offline and does not call an LLM.

The Phase 3 privacy foundation also defines [source classification](source-manifest.schema.json), [prepared sources](prepared-source.schema.json), and [privacy metadata](privacy-metadata.schema.json). The parser must consume prepared sources after the privacy gate.

## Build infrastructure

[`../../build.py`](../../build.py) produces the pre-release `knowledge/manifest.json` from the shared IR and a fixed inventory of current public schema contracts plus the generated LLM corpus and retrieval chunks. The manifest lists schema paths, SHA-256 hashes, and format versions; The corpus reports document count and the chunk file reports record count. The manifest deliberately excludes its own hash. It contains a deterministic digest of the semantic IR, fixed generator and schema compatibility versions, and no timestamp, local path, random value, or consumer setting.

Run [`../../check.py`](../../check.py) to perform two clean temporary builds, compare the bytes, validate the manifest schema and canonical JSON bytes, verify the committed manifest is fresh, and run the final privacy scanner. Both commands are local and offline.
