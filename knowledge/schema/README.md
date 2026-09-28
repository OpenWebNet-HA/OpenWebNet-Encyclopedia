# Machine KB Schemas and Controlled Vocabulary

**Machine KB 0.1.0 schema contract.** These curated JSON Schema Draft 2020-12 files define the initial public record and artifact formats used by `machine-kb-v0.1.0`. The human Encyclopedia remains authoritative. See the [consumer contract](../../project/machine-kb/consumer-contract.md), [consumer ingestion guide](../CONSUMING.md), and [privacy policy](../policy/privacy.md).

| Schema | Applies to |
| --- | --- |
| [`common.schema.json`](common.schema.json) | Stable IDs, provenance, privacy, applicability, version scope, and value states |
| [`record.schema.json`](record.schema.json) | `namespace`, `entity`, `source`, `relationship`, `caution`, `question`, `term`, `claim`, and common record variants |
| [`id-registry.schema.json`](id-registry.schema.json) | Curated canonical ID lifecycle and one-step aliases |
| [`manifest.schema.json`](manifest.schema.json) | Published-artifact inventory, hashes, record counts, coverage metrics, and compatibility metadata |
| [`retrieval-chunks.schema.json`](retrieval-chunks.schema.json) | Retrieval section records with source context, privacy, qualification cues, and stable references |
| [`source-manifest.schema.json`](source-manifest.schema.json) | Closed pre-extraction source classification |
| [`prepared-source.schema.json`](prepared-source.schema.json) | Privacy-gated prepared source records |
| [`privacy-metadata.schema.json`](privacy-metadata.schema.json) | Public/sanitized privacy metadata |

The reference JSONL files are `knowledge/reference/namespaces.jsonl`, `entities.jsonl`, `sources.jsonl`, `relationships.jsonl`, `cautions.jsonl`, `questions.jsonl`, and `glossary.jsonl` (the `term` variant). Claims use `knowledge/claims/claims.jsonl`; retrieval uses `knowledge/retrieval/chunks.jsonl`; the curated lifecycle registry is `knowledge/id-registry.json`.

Each JSONL file contains only its documented variant. The build enforces path-to-kind mapping, canonical serialization, and cross-file references in addition to JSON Schema validation.

## Meaning of controlled fields

Three independent axes must be retained. `epistemic_status` describes the claim's standing; `value.state` says whether a typed value is supplied; `applicability.state` concerns a specified domain and target, with explicit version scope. `known` requires exactly one of `text`, `integer`, or `boolean`. `unknown`, `unresolved`, and `contradictory` require a reason and prohibit a supplied value. `not_applicable` requires a scoped reason and prohibits a known value. No null or missing required field means unknown. Exact decimal quantities use `text`, not floating-point JSON numbers.

| Vocabulary | Values and use |
| --- | --- |
| `epistemic_status` | `specified` (published normative specification), `catalogue_documented` (catalogue/database assertion), `observed` (public observation), `experimentally_confirmed` (repeatable public test), `corroborated_interpretation` (converging evidence), `inferred` (reasoned interpretation), `hypothesis` (untested explanation), `unresolved`, `contradicted`, `superseded`, `rejected`. A normative status is never inferred solely from syntax or observed support. |
| `confidence` | `high`, `medium`, `low`, `undetermined`; independent of evidence class and coverage. |
| `evidence_class` | `official_specification`, `official_catalogue`, `public_database`, `public_capture`, `public_experiment`, `configuration_software`, `implementation_artifact`, `firmware_interface`, `prior_validated_research`, `canonical_documentation`. Each provenance item identifies a canonical public page and section; a required `source_id` attributes every external evidence class; canonical documentation may omit it. |
| `applicability.state` | `applies`, `unknown`, `not_applicable`. The `domain`, `target`, and version `state` (`specified` with expression, `unknown`, or `not_versioned`) narrow the assertion. |
| `entity_type` | `physical_product`, `physical_device`, `firmware`, `module`, `object`, `configuration`, `address`, `protocol_identity`, `database_record`, `protocol_value`, `other`. Classifies the kind of domain entity represented by an entity record. |
| `predicate` | `part_of`, `has_part`, `documents`, `evidenced_by`, `applies_to`, `defined_in`, `related_to`, `contradicts`, `supersedes`, `replaces`, `qualifies`, `exposes`, `identifies`, `distinct_from`. |
| `privacy.classification` | `public` with no removed classes; `sanitized` with at least one controlled removed-value class. Neither allows private values in content. |

`context.namespace_id` is explicit even for source and question records. `context.description` disambiguates uses within a namespace; protocol numbers alone do not establish relationships. `relationships`, `cautions`, and `questions` are required set arrays and may be empty when none are known.

An `unresolved` record requires a question ID. `contradicted` requires both question and relationship IDs. Consumers must inspect the referenced records; presence of an ID alone does not settle evidence. `superseded` and `rejected` are preserved historical standings, never unconditional current guidance.

Schemas reject unknown properties. Adding a property or enum member after the first release is breaking unless an explicitly defined compatible extension point and fallback make it compatible. IDs have a closed kind vocabulary and 63-byte key limit. The registry requires reasons for deprecation and retirement and preserves multi-target replacements without claiming equivalence.

## Tests and golden bytes

Install `python -m pip install -r knowledge/tools/requirements-schema.txt`, then run:

```text
python -m unittest discover -s knowledge/tools -p test_schema.py -v
```

[`fixtures/valid/golden.jsonl`](fixtures/valid/golden.jsonl) is an exact two-record serialization vector. Valid and invalid fixtures exercise every record kind, registry lifecycle, evidence, namespace, privacy, applicability, incomplete knowledge, contradictory status, and byte rules. Fixtures are synthetic protocol concepts with no observed installation data. The validator is offline and does not call an LLM.

## Build infrastructure

[`../../build.py`](../../build.py) produces `knowledge/manifest.json` and all generated machine artifacts from the shared IR and curated inputs. The manifest lists artifact/schema paths, SHA-256 hashes, format versions, and applicable record counts. It deliberately excludes its own hash. Its input digest covers the semantic IR and resolved reference records; it contains no timestamp, local path, random value, or consumer setting.

Run [`../../check.py`](../../check.py) to perform two clean temporary builds, compare the bytes, validate schemas and canonical serialization, verify committed artifacts are fresh, check cross-artifact integrity, and run the final privacy gate. Both commands are local, deterministic, and model-free.
