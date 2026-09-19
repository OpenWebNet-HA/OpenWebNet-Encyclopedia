# Documentation Review - 18 September 2026

This review continues the documentation-wide pass on `general-once-over`, starting from commit `d1d8ecdef0d1a63edf631b2de8d7b797403170e3`. The already merged protocol review and established Device Model, diagnostic, programming, and reverse-engineering decisions remain the baseline.

## Scope and completed corrections

| Area | Review result |
| --- | --- |
| Protocol | Corrected session-selection/authentication branching, final client authentication acknowledgement, proof serialization, and failure throttling; recorded the published identity-constant discrepancy. |
| Functional references | Expanded Temperature Control dimensions and holiday commands; corrected Lighting Management address composition and payloads; added Sound Diffusion payload examples and source discrepancies; removed an unsupported atomic-clock guarantee. |
| Diagnostics | Added the public Temperature Control fault model, keeping it distinct from Suite Device interviews; aligned discovery termination and version-payload explanations. |
| Device Model | Preserved configured Object versus Virgin Object resolution; corrected firmware 157's placement count to 11 alternatives across four `slot` positions. |
| Programming and guides | Scoped product queries by catalogue system, preserved firmware candidates, corrected slot and rule queries, distinguished decimal wire IDs from hexadecimal display, added cleanup, and processed active sequence outcomes before subsequent writes. |
| Scenario Engine | Corrected shared-placeholder rendering and the parameter table; narrowed open questions to genuinely unresolved mappings. |
| Internals and reverse engineering | Preserved established namespace and ownership boundaries; corrected a nonexistent SQL column and clarified the position of `N_CONF`. |
| Navigation and style | Replaced path-only navigation labels with page titles, removed em dashes, repaired an obsolete address anchor, and checked Markdown tables. |

The accepted interpretation of `DIMENSION 1.N_CONF` as a physical configurator-position count remains intact. `EN_DEVICE.name` remains the preferred Device description; Module, `slot`, Object, and database row identity remain separate concepts. Existing one-page functional references remain consolidated.

## Validation

- Checked every Markdown page for local link targets and heading fragments, table-column consistency, and whitespace errors.
- Prepared 51 concrete SQL statements against the five canonical SQLite databases, with the documented cross-database aliases. Three generic parent/child schema examples were excluded from preparation because they intentionally use illustrative tables. Preparation checks schema and syntax, not runtime Device behavior.
- Cross-checked catalogue counts and firmware-placement examples against the canonical database; retained wildcard, missing-build, ownership, and multi-system distinctions.
- Compared all 24 locally available canonical non-Markdown source files with the baseline Git blob hashes: all matched exactly. No source database, support file, PDF, or diagram was edited.
- Used the baseline remote tree when publishing so unavailable source binaries remain preserved.

## Evidence limits and remaining research

This is a documentation and source-data review, not a hardware interoperability test. Existing capture-derived findings retain their stated scope; no new Device capture or programming operation was performed.

Two canonical PDFs could not be retrieved in this review environment: `OpenWebNet_Zigbee.pdf` and `WHO_6_L4686SDK.pdf`. Their existing repository bytes and previously documented findings are preserved, but this pass does not claim a fresh page-by-page verification of those files.

The [authentication reference](../protocol/authentication.md) and [Sound Diffusion reference](../functional/who-22-sound-diffusion/) identify source contradictions that require independent implementation or traffic evidence. Other unresolved research, including firmware-selection precedence, configurator-value encoding, and non-Lighting confirmation of `DIMENSION 32.SYS`, remains in [Open Questions](open-questions.md). These are evidence boundaries, not reasons to substitute speculative protocol behavior.
