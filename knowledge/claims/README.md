# Atomic Claims

[`claims.jsonl`](claims.jsonl) is generated from the reviewed [`knowledge/inputs/claim-records.json`](../inputs/claim-records.json) joined to the privacy-gated shared IR.

The current initial-release candidate contains 7,449 claims across all eight canonical domains. The bounded claim ledger covers 135 canonical documents and 1,207 sections: 1,111 sections contain one or more reviewed claims and 96 are explicitly reviewed non-claim sections.

Each claim retains provenance, evidence class, confidence, namespace, scope, cautions, questions, relationships, and epistemic status. Contradictory source statements and unresolved interpretations remain separate qualified records; generation does not silently select or synthesize a resolution.

`subject_id` refers to one canonical entity. `claim_links` explicitly names claims that support, qualify, or contradict another assertion. A contradiction is reciprocal, shares subject and namespace, and carries an open question on both sides. A reported raw value and its possible interpretation are separate claims.

Provenance names a public source where required and the canonical document and section where its interpretation was reviewed. `source_section_sha256` hashes that prepared IR section, not a private raw source. The curated input pins it. Any change to that section blocks the build until a reviewer revisits every dependent claim and updates the pinned digest.

[`knowledge/inputs/claim-coverage.json`](../inputs/claim-coverage.json) accounts for every section in the bounded canonical domains. `claimed` means that the section has at least one reviewed atomic assertion. `nonclaim` is limited to reviewed structural, navigation, reference-list, procedural, or non-assertive sections and records a reason. It is invalid for the ledger count to disagree with generated claims.

Exact WHO, diagnostic, Device Model, implementation, research, and ScenarioDevices namespaces and section-topic subject entities preserve context without treating equal values in different systems as identical.

Practical Guides remain excluded. Guide-only factual material is a documentation defect until it is promoted into an appropriate canonical section and reviewed there.

For consumer-side use of claims and their reference records, see [Consuming the Machine KB](../CONSUMING.md).
