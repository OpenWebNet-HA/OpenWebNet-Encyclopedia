# OpenWebNet Protocol Documentation

Reference documentation for OpenWebNet, the MyHOME device model, diagnostic and programming protocols, and supporting MyHOME Suite implementation data.

## Documentation

| Section | Scope |
| --- | --- |
| [`protocol/`](protocol/) | Common OpenWebNet frame syntax, addressing, `WHAT`, `DIMENSION`, and acknowledgements |
| [`functional/`](functional/) | Functional OpenWebNet systems organized by `WHO` |
| [`diagnostics/`](diagnostics/) | Device discovery, interview, diagnostic operations, and diagnostic `DIMENSION` values |
| [`programming/`](programming/) | Device and Object configuration and programming workflows |
| [`device-model/`](device-model/) | Device → Module → Object → Configuration model |
| [`guides/`](guides/) | Practical guides providing complete paths from raw frames and high-level goals to presentable data, validated programming, and verification |
| [`scenario-engine/`](scenario-engine/) | MyHOME Suite scenario capability and execution model |
| [`internals/`](internals/) | MyHOME Suite implementation details relevant to the protocol |
| [`reverse-engineering/`](reverse-engineering/) | Methodology, correlations, inferred relationships, and unresolved questions |
| [`sources/`](sources/) | Canonical source material and provenance records |

## Conventions

Protocol fields and tokens are written as inline code, including `WHO`, `WHAT`, `WHERE`, `DIMENSION`, `ACK`, and `NACK`. Complete frames are likewise written as inline code when they fit naturally in prose or tables.

`WHAT`, `WHERE`, and `DIMENSION` semantics are scoped to their `WHO`. Identical numeric values in different systems do not imply identical meanings.

Reference material follows the canonical structure of the protocol or implementation model it documents. Landing pages and indexes may provide additional navigation organized around related functions or reader tasks, linking to the same canonical reference material rather than duplicating it.

The device-model terminology used throughout the reference is **Device → Module → Object → Configuration**. Database identifiers retain their original names when referenced directly.

Each documentation directory uses its `README.md` as its landing-page overview. Subject-specific reference material is kept in the other Markdown files in that directory.

## Sources and provenance

Canonical evidence is stored under [`sources/`](sources/). Source files are preserved as original evidence; derived schemas, analysis, and reverse-engineering notes belong elsewhere in the repository.

See [`sources/manifest.yaml`](sources/manifest.yaml) for machine-readable provenance and cryptographic fingerprints.

## License

Repository-authored documentation is licensed under the GNU General Public License v3.0. Canonical source materials under `sources/` retain the rights and licensing terms of their respective publishers and authors.