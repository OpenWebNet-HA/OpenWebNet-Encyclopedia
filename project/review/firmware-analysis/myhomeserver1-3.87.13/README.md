# MyHOMEServer1 3.87.13 first-pass review capsule

This capsule supports the [build-specific analysis](../../../../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13.md). Exact reports, selected source excerpts and deterministic evidence retain the distinction between packaged implementation, host reconstruction and runtime/physical behavior. Original Firmware execution is zero. Wider Device/full-source review remains pending.

## Source reports

| Area | Exact retained report | Scope |
| --- | --- | --- |
| Input and applicability | [Independent input review](input-and-role-review.txt) | Archive/images/extraction and canonical product scope |
| Structural/data pass | [Inventory and embedded catalogue](inventory-report.txt) | Full defined regular-file prefix census, fresh ELF headers, selected application dependencies, read-only catalogue comparison |
| Startup/platform | [Boot and configuration](boot-report.txt) | Current SysV/script/default XML/daemon field and conditional launch source, managers and selected DTB |
| OPEN/SCS | [Protocol and translation](protocol-report.txt) | Distinct parser/provider families, fresh56-byte object, actual registration/direction/selected auxiliary branches |
| Synthesis | [First-pass synthesis](synthesis.txt) | Reviewed findings and cross-product boundaries |
| Coverage | [Examined scope](coverage.txt) | Explicit areas and incomplete layers; counts are not coverage percentages |
| Next questions | [Ranked investigations](remaining-questions.txt) | Actual database consumer, scenario lifecycle, fresh dispatch/STM, alarm/persistence ownership |

## Evidence identities and reproduction

[Report exports](source-exports.json) and [selected evidence exports](evidence-exports.json) identify exact source paths, sizes and SHA-256 hashes. The selected evidence directory includes original disassembly spans, source-byte assertions/relocations, startup line locators, selected public configuration, host-only examples and catalogue structural comparisons. It contains no original vendor binaries or raw database tables. The package and database are locally preserved original inputs; this first pass does not claim a new canonical archive registration.

Local source collectors live under `work/myhomeserver1-firmware/3.87.13/research/2026-10-31/`. Run the inventory `collect_inventory_v1.py --check`, boot `collect_boot_v1.py --check` and protocol `collect_protocol_v1.py --check` with host Python and `-B`. They read original-image metadata and bytes, host binutils and read-only SQLite; they never run vendor code. Initial output creation refuses overwrite, and actual first candidates and report-only correction history are retained separately.

The embedded catalogue is SHA-256 `79fcf2e2580dfe23349ead3d3e385ad8210cf44dddff3179a9c021644a7d1edb`. The distinct installer comparison input is `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Shared schemas or filenames do not merge those identities. Full typed-row digest comparisons expose changed tables without copying their raw records into this capsule.

## Review boundaries

Independent current source and final integration reviews are retained with the completion validation. Input review, source checks and mechanical ECV/ESG success are separate from full Device approval. Signature blobs are preserved but cryptographic verification remains unproved. Missing extras80/81/94/95, configured state, live providers, accepted inputs, I/O, electrical topology, concurrency and physical effects remain open. Earlier stopped authentication/session/framing investigations remain closed.

| Review or check | Record |
| --- | --- |
| Structural source | [Independent review](inventory-source-review.txt), [second source review](inventory-second-review.txt) |
| Boot source | [Independent review](boot-source-review.txt) |
| Protocol source | [Independent review](protocol-source-review.txt) |
| Final synthesis | [Integration review](integration-review.txt), [second integration review](integration-second-review.txt) |
| Reproduction | [Three host-only collector checks](source-checks.json) |
| Identity and preservation | [Final validation](validation.json) |
