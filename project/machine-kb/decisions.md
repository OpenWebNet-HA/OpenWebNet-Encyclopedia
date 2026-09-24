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

## Open decisions for Phase 1 and later

| ID | Target phase | Question |
| --- | --- | --- |
| MKB-O01 | 1 | Stable ID grammar, aliases, retirement, and source-location versus entity identity |
| MKB-O02 | 1 | Public artifact names, ordering/serialization, unknown/null/contradiction semantics, and compatibility/version policy |
| MKB-O03 | 2 | Exact schema shapes and controlled epistemic/evidence/relationship vocabularies mapped to Encyclopedia language |
| MKB-O04 | 3 | Source classification and field-aware sanitization, including safe public fixtures and scanner limits |
| MKB-O05 | 4 and 8 | IR structure and reviewed claim input representation |
