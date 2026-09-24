# Machine Reference Data

This directory contains generated controlled reference data for machine consumers: `namespaces.jsonl`, `glossary.jsonl`, `sources.jsonl`, `entities.jsonl`, `relationships.jsonl`, `cautions.jsonl`, and `questions.jsonl`.

Canonical definitions live only in the glossary. Entity records identify referents and link to glossary terms with `defined_in` relationships; they do not carry duplicate definitions. Sources include one generated record for every canonical IR document plus reviewed public evidence-source records. Unresolved source qualifications remain linked cautions and questions.

The semantic records are generated from [`../inputs/reference-records.json`](../inputs/reference-records.json) after its section IDs are joined to the shared IR. Canonical-document source records are generated directly from that IR. Reference records provide the stable identifiers used by retrieval chunks and future atomic claims. `python check.py` validates schema, provenance, registry kinds, every cross-reference, manifest counts and hashes, deterministic bytes, and privacy.
