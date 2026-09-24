# Machine KB Decisions

Record durable choices here with status and rationale. A later decision may supersede an earlier one, but must cite it and retain the history. Unsettled details remain explicitly open.

| ID | Status | Decision and reason |
| --- | --- | --- |
| MKB-001 | Accepted | Human Encyclopedia pages remain authoritative. Machine records are attributable projections, so corrections must reach canonical prose. |
| MKB-002 | Accepted | Publish a public, deterministic, consumer-neutral dataset. MCP/FastMCP is an independent external consumer, never an Encyclopedia component. |
| MKB-003 | Accepted | Use one normalized semantic parser/IR for all output families. Reviewed claim inputs may enrich the model; renderers must not establish competing semantics. |
| MKB-004 | Accepted | Never publish private or installation-specific information. Exclude prohibited sources and sanitize before derivation; schema gates and a final scan provide additional checks. Fail closed. |
| MKB-005 | Accepted | CI and build validation are deterministic and require no LLM. Assisted review is an authoring activity for changed, especially high-risk, knowledge. |
| MKB-006 | Accepted | Practical Guides are procedural and excluded from canonical Machine KB extraction. Promote guide-only facts to canonical documentation first. |
| MKB-007 | Accepted | Stable IDs, schema and vocabulary, provenance, epistemic and applicability status, relationships, versioning, CI validation, and a public consumer contract are release requirements. No concrete grammar or vocabulary is frozen in Phase 0. |
| MKB-008 | Accepted, Phase 1 | Use lowercase `ownkb:` kind/key IDs with curated durable allocation, never path/heading/content hashes or private values. Preserve alias/retirement history; split/merge replacements may be multiple and do not imply equivalence. [Contract](consumer-contract.md#stable-ids) |
| MKB-009 | Accepted, Phase 1 | Manifest inventory, canonical UTF-8/NFC/LF bytes, compact sorted JSONL, bounded exact integers, and explicit ordering produce reproducible outputs across consumer languages. [Contract](consumer-contract.md#ordering-and-bytes) |
| MKB-010 | Accepted, Phase 1 | Separate epistemic standing, value availability, and scoped applicability. Represent unresolved and contradictory evidence explicitly; missing records or nulls make no negative assertion. Exact enum values await Phase 2. [Contract](consumer-contract.md#meaning-of-incomplete-or-conflicting-knowledge) |
| MKB-011 | Accepted, Phase 1 | Curate ID/alias registry and reviewed claim inputs in Git; generate all public data through one IR. Contract and per-artifact formats use compatibility versions distinct from Git content snapshots. [Versioning](schema-versioning.md) |
| MKB-012 | Accepted, Phase 1 | A closed-schema property or enum addition is breaking unless a predefined extension point and fallback make it compatible. Privacy withdrawal takes priority over ID retention. [Versioning](schema-versioning.md) |
| MKB-016 | Accepted, Phase 3 | Every candidate source is classified by a closed local manifest before extraction. Prohibited private-source classes are never opened; public sources with recognised sensitive shapes require deterministic sanitization before any derived record exists. Prepared records carry only `public` or `sanitized` privacy metadata, and the final generated-tree scanner remains mandatory. |

| MKB-013 | Accepted, Phase 2 | Curated Draft 2020-12 schemas close record and nested metadata shapes. Every record requires context, applicability/version, provenance/evidence, epistemic status/confidence, privacy, and relationship/caution/question sets. [Vocabulary](../../knowledge/schema/README.md) |
| MKB-014 | Accepted, Phase 2 | Separate epistemic standing, typed value, and scoped applicability. Contradicted records require question and relationship references; unresolved records require a question. Cross-artifact truth and referential checks remain mandatory before release. |
| MKB-015 | Accepted, Phase 2 | Fix the seven planned reference registry names in [schema documentation](../../knowledge/schema/README.md). Schemas and fixtures are curated; generated records remain empty. Registry location and manifest/Markdown formats are later decisions. |

| MKB-017 | Accepted, Phase 4 | A closed canonical Markdown manifest feeds the existing sanitization gate, then a single structural IR. `guides/` is excluded before extraction; a separate path/line hint report identifies candidate guide-only facts for human review. Committed path and heading-anchor mappings retain opaque IDs across editorial changes. Lexical qualification cues preserve evidence for review without inventing claims. |

## Open decisions for Phase 1 and later

| ID | Target phase | Question |
| --- | --- | --- |
| MKB-O03 | Resolved in 2 | Common record schemas and controlled vocabularies in `knowledge/schema/` |
| MKB-O04 | Resolved, 3 | Source classification and deterministic sanitization use safe fixtures and retain scanner limits; future field transforms require policy and test updates |
| MKB-O05 | Partly resolved in 4; remainder 8 | Shared Markdown IR implemented; reviewed claim input representation remains open |
| MKB-O06 | 2 | Concrete registry schemas and golden serialization examples; exact reference file names and corpus format before v1 |
