# OpenWebNet Protocol Documentation

Reference documentation for OpenWebNet, the MyHOME device model, diagnostic and programming protocols, and supporting MyHOME Suite implementation data.

## Documentation

| Section | Scope |
| --- | --- |
| [Protocol](protocol/) | Common OpenWebNet frame syntax, addressing, `WHAT`, `DIMENSION`, and acknowledgements |
| [Functional Protocol](functional/) | Functional OpenWebNet systems organized by `WHO` |
| [Diagnostics](diagnostics/) | Physical Device discovery, interview, diagnostic operations, and diagnostic `DIMENSION` values |
| [Programming](programming/) | Physical Device and Object configuration and programming workflows |
| [Device Model](device-model/) | Physical Device → Firmware → Module → Object → Configuration model |
| [Practical Guides](guides/) | Practical guides providing complete paths from raw frames and high-level goals to presentable data, validated programming, and verification |
| [Scenario Engine](scenario-engine/) | MyHOME Suite scenario capability and execution model |
| [MyHOME Suite Internals](internals/) | MyHOME Suite implementation details relevant to the protocol |
| [Reverse Engineering](reverse-engineering/) | Methodology, correlations, inferred relationships, and unresolved questions |
| [Sources](sources/) | Canonical source material and provenance records |
| [Machine-Readable Knowledge Base for LLMs and Automated Tools](knowledge/) | Generated corpora, retrieval chunks, atomic claims, controlled reference data, schemas, and generation tools for machine ingestion |
| [Project Standards](project/) | Encyclopedia Core Values and human-facing Encyclopedia Style Guide |

## LLM and machine ingestion

The [Machine-Readable Knowledge Base for LLMs and Automated Tools](knowledge/) is the entry point for language models, retrieval systems, indexers, validators, code generators, and other automated consumers. Its directory names distinguish complete LLM context, retrieval units, atomic claims, controlled reference data, schemas, and generation tooling.

The human-readable Markdown documentation remains authoritative. Machine artifacts are deterministic derivatives that retain source paths, provenance, evidence status, version scope, protocol namespace, cautions, relationships, and unresolved questions. They must also pass the [Machine Knowledge Privacy Policy](knowledge/policy/privacy.md): concrete network addresses, installed Physical Device identifiers, credentials, private capture contents, and other private or installation-specific data are prohibited.

## Sources and provenance

Canonical evidence is stored under [Sources](sources/). Source files are preserved as original evidence; derived schemas, analysis, and reverse-engineering notes belong elsewhere in the repository.

See [Source Manifest](sources/manifest.yaml) for machine-readable provenance and cryptographic fingerprints.

## License

Repository-authored documentation is licensed under the GNU General Public License v3.0. Canonical source materials under `sources/` retain the rights and licensing terms of their respective publishers and authors.
