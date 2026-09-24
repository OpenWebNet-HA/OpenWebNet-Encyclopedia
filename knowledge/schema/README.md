# Machine Artifact Schemas

This directory contains machine-readable schemas and format contracts for every generated knowledge-base artifact.

Schemas define required provenance, evidence, namespace, version, caution, relationship, unresolved-status, and privacy-classification fields. They reject unexpected fields that could carry unreviewed private data and form the validation boundary for LLM ingestion, retrieval indexing, claim processing, and other automated consumers.

The privacy foundation is implemented before corpus schemas:

- [`source-manifest.schema.json`](source-manifest.schema.json) is a closed manifest
  for source classification. It has no extension fields that could conceal a
  private location or unreviewed value.
- [`privacy-metadata.schema.json`](privacy-metadata.schema.json) permits only the
  publishable classifications `public` and `sanitized`. A sanitized record must
  list typed removed-value classes; a public record must list none.
- [`prepared-source.schema.json`](prepared-source.schema.json) is the only record
  form the later parser/IR may consume. It requires closed publishable privacy
  metadata and contains no raw-source location beyond a public repository-relative
  path.

The broader common-record schemas remain a separate Phase 2 deliverable. They must
reuse the privacy metadata schema rather than create a second privacy vocabulary.
