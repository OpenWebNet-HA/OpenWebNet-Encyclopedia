# OpenWebNet Protocol Documentation

Reference documentation for OpenWebNet, the MyHOME device model, diagnostic and programming protocols, and supporting MyHOME Suite implementation data.

## Documentation

| Section | Scope |
| --- | --- |
| [Protocol](protocol/) | Common OpenWebNet frame syntax, addressing, `WHAT`, `DIMENSION`, and acknowledgements |
| [Functional Protocol](functional/) | Functional OpenWebNet systems organized by `WHO` |
| [Diagnostics](diagnostics/) | Device discovery, interview, diagnostic operations, and diagnostic `DIMENSION` values |
| [Programming](programming/) | Device and Object configuration and programming workflows |
| [Device Model](device-model/) | Device → Module → Object → Configuration model |
| [Practical Guides](guides/) | Practical guides providing complete paths from raw frames and high-level goals to presentable data, validated programming, and verification |
| [Scenario Engine](scenario-engine/) | MyHOME Suite scenario capability and execution model |
| [MyHOME Suite Internals](internals/) | MyHOME Suite implementation details relevant to the protocol |
| [Reverse Engineering](reverse-engineering/) | Methodology, correlations, inferred relationships, and unresolved questions |
| [Sources](sources/) | Canonical source material and provenance records |
| [Machine-Readable Knowledge Base for LLMs and Automated Tools](knowledge/) | Generated corpora, retrieval chunks, atomic claims, controlled reference data, schemas, and generation tools for machine ingestion |

## LLM and machine ingestion

The [Machine-Readable Knowledge Base for LLMs and Automated Tools](knowledge/) is the entry point for language models, retrieval systems, indexers, validators, code generators, and other automated consumers. Its directory names distinguish complete LLM context, retrieval units, atomic claims, controlled reference data, schemas, and generation tooling.

The human-readable Markdown documentation remains authoritative. Machine artifacts are deterministic derivatives that retain source paths, provenance, evidence status, version scope, protocol namespace, cautions, relationships, and unresolved questions. They must also pass the [Machine Knowledge Privacy Policy](knowledge/policy/privacy.md): concrete network addresses, installed Device identifiers, credentials, private capture contents, and other private or installation-specific data are prohibited.

## Conventions

Protocol fields and tokens are written as inline code, including `WHO`, `WHAT`, `WHERE`, `DIMENSION`, `ACK`, and `NACK`. Complete frames are likewise written as inline code when they fit naturally in prose or tables.

Use a simple hyphen (`-`) for parenthetical breaks and title separators; do not use Unicode U+2014.

Use the human-readable title of a page or resource as link text. Do not use the destination file or directory name as the label, such as `dimensions.md` or `who-1-lighting/`, unless the path itself is the subject being discussed.

`WHAT`, `WHERE`, and `DIMENSION` semantics are scoped to their `WHO`. Identical numeric values in different systems do not imply identical meanings.

Reference material follows the canonical structure of the protocol or implementation model it documents. Landing pages and indexes may provide additional navigation organized around related functions or reader tasks, linking to the same canonical reference material rather than duplicating it.

The device-model terminology used throughout the reference is **Device → Module → Object → Configuration**. Database identifiers retain their original names when referenced directly.

Each documentation directory uses its `README.md` as its landing-page overview. Subject-specific reference material is kept in the other Markdown files in that directory.

## Sources and provenance

Canonical evidence is stored under [Sources](sources/). Source files are preserved as original evidence; derived schemas, analysis, and reverse-engineering notes belong elsewhere in the repository.

See [Source Manifest](sources/manifest.yaml) for machine-readable provenance and cryptographic fingerprints.

## License

Repository-authored documentation is licensed under the GNU General Public License v3.0. Canonical source materials under `sources/` retain the rights and licensing terms of their respective publishers and authors.
