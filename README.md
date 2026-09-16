# OpenWebNet Protocol Documentation

Professional reference documentation for the OpenWebNet protocol and the MyHOME data model used by BTicino and Legrand systems.

The project combines the published OpenWebNet specification with implementation information represented by the canonical MyHOME Suite corpus. Unknown or undocumented behavior remains explicitly identified as unknown; inferred behavior is not presented as canonical protocol semantics.

## Reference

| Section | Purpose |
| --- | --- |
| [`protocol/`](protocol/) | Common OpenWebNet frame language, addressing, `WHAT`, Dimensions, and acknowledgements |
| `functional/` | Functional systems and their WHO-specific commands, addressing, Dimensions, and values |
| `diagnostics/` | Device discovery, interview, diagnostic WHATs, and diagnostic Dimensions |
| `programming/` | Device and Object configuration and programming operations |
| `device-model/` | Device → Module → Object → Configuration model |
| `scenario-engine/` | MyHOME Suite scenario capability model |
| `internals/` | Implementation structures used by MyHOME Suite |
| `reverse-engineering/` | Methodology, correlations, inferred structures, and open questions |
| [`sources/`](sources/) | Canonical source corpus and provenance manifest |

Sections that are not yet present are part of the approved documentation structure and will be added as their reference material is written.

## Conventions

Canonical names and nomenclature are used wherever the source corpus defines them. Protocol fields, frame fragments, database identifiers, paths, and short literal values are formatted as inline code. Numeric examples are used only where they clarify an encoding or protocol rule.

`WHAT` and Dimension meanings are scoped to their `WHO`; the same numeric value can have different semantics in different systems. Common concepts are documented under [`protocol/`](protocol/), while system-specific value references belong with the corresponding functional or diagnostic system.

Database queries use SQL. Algorithmic implementation examples default to Python 3.

## Sources

Canonical evidence is registered in [`sources/manifest.yaml`](sources/manifest.yaml). Files under [`sources/`](sources/) are preserved as evidence and are not modified to encode interpretations or reconstructed relationships.

## License

This repository is distributed under the [GNU General Public License v3.0](LICENSE). Canonical source material under `sources/` retains the rights and provenance of its respective publishers.