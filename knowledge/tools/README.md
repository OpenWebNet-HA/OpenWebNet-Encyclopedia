# Knowledge-Base Generation and Validation Tools

This directory contains deterministic generators, linters, validators, and consistency checks for the machine-readable knowledge base.

Tooling must read the authoritative documentation and source metadata, produce the artifacts in the sibling machine-ingestion directories, validate them against the published schemas, and fail on broken provenance, references, or namespace boundaries.

Privacy validation is mandatory and fail-closed. Run `python knowledge/tools/validate_privacy.py` after generation and before publication. The generator must sanitize sensitive source values before constructing chunks, claims, identifiers, or metadata; the final scan is an additional release gate.

Run the source gate before any extraction work:

```text
python knowledge/tools/prepare_sources.py --manifest SOURCE-MANIFEST.jsonl --source-root . --output PREPARED-SOURCES.jsonl
```

The manifest is JSONL with exactly `source_id`, `source_path`, `source_type`, and
`classification`. `prohibited` sources are never opened; `sanitize` sources are
replaced with typed markers before output; `publishable` sources fail on a detected
sensitive shape. The output order and JSON bytes are deterministic. Keep manifests
and prepared output outside publishable artifact directories until later build and
IR phases define their ownership.
