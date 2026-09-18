# Knowledge-Base Generation and Validation Tools

This directory contains deterministic generators, linters, validators, and consistency checks for the machine-readable knowledge base.

Tooling must read the authoritative documentation and source metadata, produce the artifacts in the sibling machine-ingestion directories, validate them against the published schemas, and fail on broken provenance, references, or namespace boundaries.

Privacy validation is mandatory and fail-closed. Run `python knowledge/tools/validate_privacy.py` after generation and before publication. The generator must sanitize sensitive source values before constructing chunks, claims, identifiers, or metadata; the final scan is an additional release gate.
