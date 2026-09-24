# Retrieval Corpus

[`chunks.jsonl`](chunks.jsonl) is the deterministic retrieval projection of the shared semantic IR. A chunk is one nonempty canonical section, so it retains a coherent section boundary rather than an arbitrary token window. Every record carries a curated stable chunk ID, document and section IDs, source path, section hierarchy, namespace context, provenance, privacy classification, lexical applicability, caution, uncertainty and provenance cues, and stable `reference_ids`.

Every chunk references its canonical source record and resolved namespace. Where a section owns canonical glossary, entity, relationship, caution, or open-question records, the chunk references those records instead of adding a separate structured definition.

`guides/` does not enter this corpus. Empty structural sections are counted separately in `knowledge/manifest.json`; the manifest also distinguishes canonical coverage, excluded guides, and emitted chunks. Validate records with [`../schema/retrieval-chunks.schema.json`](../schema/retrieval-chunks.schema.json), or run `python check.py`.
