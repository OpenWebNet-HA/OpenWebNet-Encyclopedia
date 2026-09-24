# Atomic Claims

`claims.jsonl` is generated from the reviewed `knowledge/inputs/claim-records.json` joined to the privacy-gated shared IR. This Phase 8 sample contains eight deliberately narrow claims; it does not claim coverage of the Encyclopedia.

Each claim must retain provenance, evidence class, confidence, namespace, scope, cautions, and relationships. Contradictory source statements and unresolved interpretations remain separate qualified records; generation must not silently select or synthesize a resolution.

`subject_id` refers to one canonical entity. `claim_links` explicitly names claims that support, qualify, or contradict another assertion; a contradiction is reciprocal, shares subject and namespace, and carries an open question on both sides. A reported raw value and its possible interpretation are separate claims. Provenance names a public source and the canonical document and section where its interpretation was reviewed. The `source_section_sha256` hashes that *prepared IR section*, not a private raw source; the curated input pins it. Any change to that section blocks the build until a reviewer revisits every dependent claim and updates the pinned digest, even when the claim still reads correctly. This deliberately conservative Phase 8 change gate is not the full Phase 12 cross-artifact drift analysis.
