# Knowledge-Base Generation and Validation Tools

This directory contains deterministic generators, linters, validators, and consistency checks for the machine-readable knowledge base.

The [shared Markdown IR pipeline](IR.md) consumes only prepared canonical sources. Its closed source manifest and durable identity mapping live in [curated IR inputs](../inputs/README.md). It reports guide remediation hints without importing guide content into the IR.

Tooling reads the authoritative documentation and curated source metadata, produces the artifacts in the sibling machine-ingestion directories, validates them against the published schemas, and fails on broken provenance, references, namespace boundaries, stale generated output, or privacy violations.

Privacy validation is mandatory and fail-closed. Run `python knowledge/tools/validate_privacy.py` after generation and before publication. The generator sanitizes sensitive source values before constructing chunks, claims, identifiers, or metadata; the final scan is an additional release gate.

Generated-text hygiene is also mandatory and fail-closed. The validate_text_hygiene.py tool scans every string in the published JSON/JSONL surfaces plus the LLM corpus for high-confidence parser/AST serialization, runtime object representations, tracebacks, JavaScript object coercion, and other internal execution artefacts. The rules intentionally preserve legitimate OpenWebNet frames, JSON/code examples, SQL, hexadecimal values, and other technical notation. The same gate runs inside both build.py and check.py.

The repository build uses the curated source classification in `knowledge/inputs/canonical-sources.jsonl`. For standalone source-gate testing, run:

```text
python knowledge/tools/prepare_sources.py --manifest SOURCE-MANIFEST.jsonl --source-root . --output PREPARED-SOURCES.jsonl
```

The source manifest is JSONL with exactly `source_id`, `source_path`, `source_type`, and `classification`. `prohibited` sources are never opened; `sanitize` sources are replaced with typed markers before output; `publishable` sources fail on a detected sensitive shape.

Prepared-source output is an intermediate build product, not a public Machine KB artifact. Keep ad hoc prepared output outside the published artifact paths. The versioned public machine interface is the artifact/schema set enumerated by `knowledge/manifest.json`.

Use the top-level `python build.py` to regenerate the committed machine artifacts and `python check.py` for deterministic rebuild, freshness, schema, consistency, reference, and privacy validation.
