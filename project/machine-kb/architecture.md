# Machine KB Architecture

## Authority and scope

The human-readable Encyclopedia is the source of canonical factual and epistemic knowledge. The Machine KB is a public, deterministic, protocol-independent dataset derived from it and public source provenance. A correction to knowledge starts in canonical human documentation; generated artifacts must not introduce an independent interpretation. The [Core Values](../encyclopedia-core-values.md), especially evidence, applicability, namespace, privacy, and consistency rules, apply to every representation.

`guides/` contains procedural Practical Guides that may repeat canonical facts for human readers. Exclude them as independent sources of canonical Machine KB claims, reference facts, retrieval chunks, and LLM corpus. Promote any guide-only factual knowledge into a canonical non-guide page before extraction. Exclude private captures, installation exports, logs, inventories, and other prohibited inputs before parsing, even when they inform sanitized conclusions in human documentation.

MCP and FastMCP are external consumers. No server, transport adapter, service-specific schema, endpoint, or dependency on either belongs in this project. Consumers may be LLMs, retrieval systems, validators, code generators, or independent services; all receive the same published data contract.

## One semantic pipeline

1. Classify input sources as publishable, requiring sanitization, or prohibited. Apply the [privacy policy](../../knowledge/policy/privacy.md) before constructing derived text, IDs, metadata, or logs.
2. Parse canonical Encyclopedia Markdown and public source metadata once into a normalized semantic intermediate representation (IR). Preserve document and section identity, namespace, applicability/version scope, provenance, evidence class, epistemic status, cautions, unresolved questions, and explicit relationships. The IR may remain internal to the build.
3. Render the existing intended output families from that same IR: `knowledge/llm/`, `knowledge/retrieval/`, `knowledge/reference/`, and `knowledge/claims/`. Claims may use reviewed curated structured inputs, but must join the same normalized model and validation path. Do not independently re-parse the Encyclopedia for each renderer or infer claims blindly from prose.
4. Validate schema and controlled vocabulary, stable IDs and aliases, source and relationship integrity, namespace and applicability, contradictory or unresolved status, output freshness, deterministic bytes, and privacy. Publication fails closed on missing or ambiguous privacy classification or unresolved validation failures.

Records need stable, non-private IDs, source paths and attributable evidence, qualified epistemic status, explicit relationships, and a versioned consumer contract. Identical input revisions must produce byte-for-byte identical outputs without network access, wall-clock timestamps, random IDs, or an LLM in CI. LLM assistance can help curate and review changed claims outside CI; only reviewed structured data is committed as build input.

The current `knowledge/` directories and privacy scanner are a skeleton. This page sets invariants, not a finalized ID grammar, schema vocabulary, IR layout, artifact encoding, or release version; those are later gated decisions. See [Decisions](decisions.md) and [Roadmap](roadmap.md).
