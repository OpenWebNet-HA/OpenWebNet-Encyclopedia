# Curated IR inputs

`canonical-sources.jsonl` is the closed classification list for every Markdown page in the seven canonical documentation areas. It deliberately contains no `guides/` entries. The source gate rejects a newly added canonical page until it is classified here. A `sanitize` entry is reviewed source policy, not permission to include raw private material. Private captures, logs, inventories, and exports never belong in this manifest as publishable inputs.

`identities.json` maps each canonical path and heading anchor to a durable document or section ID. Its initial allocation was reviewed and committed once. On a move or heading rename, update the mapping key while retaining its ID. Never run `--bootstrap-identities` in routine builds. If a section changes meaning, curate a new identity and retain lifecycle history before publication. No public IDs have yet been released.

The guide remediation check emits path and line only, without copying guide text or adding it to the IR. Review its hints against the canonical pages, then promote any genuine guide-only fact to canonical documentation before publishing derived outputs. Heuristic flags include false positives; an empty hint list does not certify complete coverage.
