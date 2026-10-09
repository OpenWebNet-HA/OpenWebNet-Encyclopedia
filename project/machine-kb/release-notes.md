# OpenWebNet Machine KB 0.2.0 Release Notes

**Release identity:** OpenWebNet Machine KB 0.2.0; intended tag `machine-kb-v0.2.0`. Release preparation is authorized; publication remains subject to the exact-revision gates. The accepted Device dataset was merged through [PR #48](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/pull/48) at `29a07b4934fd4fb5da3e5b04d841bc698bfc6c6f`.

This release adds the complete accepted Device inventory to the Encyclopedia and its four Machine KB projections. It describes commercial identities, product capabilities, firmware/build applicability and reusable configuration surfaces while preserving manufacturer-source boundaries, unknowns and conflicts.

## Device and commercial coverage

| Measure | Coverage |
| --- | ---: |
| Accepted technical Device definitions, all integrated into the KB | 210 |
| Commercial records in the MyHOME Suite 3.5.38 catalogue | 541 |
| Commercial lookup rows, including supplementary printed references and packages | 602 |
| Distinct displayed brand/line-reference pairs in that lookup | 601 |
| Catalogue brand labels / product-line labels | 4 / 18 |

One commercial reference can map to a shared technical definition; shared catalogue membership does not establish identical hardware or installed firmware. The Legrand Arteor `572736` reference intentionally appears under two definitions because publisher and catalogue associations conflict. It contributes two lookup rows and one brand/line-reference pair. These figures describe retained catalogue and documentation coverage, not every currently sold product or observed Physical Device. See the [commercial index](../../devices/index.md) and [catalogue evidence](../../devices/inventory/).

## Manufacturer evidence and PDF inspection

| Measure | Count |
| --- | ---: |
| Distinct retained PDFs examined at relevant product sections during Device research/review, including one rejected scope match | 734 |
| Distinct PDF originals in the Device evidence index | 733 |
| Retained HTML product records in that index, counted separately | 30 |
| New PDF originals archived during the 210 semantic reviews | 80 |
| New HTML originals archived during those reviews | 3 |
| New registered PDF originals since the 0.1.2 release baseline, including description research | 632 |

PDFs are deduplicated by archival SHA-256, not filename, language label, citation count or number of Devices sharing a manual. Inspection covers applicable product sections, ratings, configuration tables, diagrams and revision comparisons; it does not assert that unrelated pages or every translated chapter of a multi-product document were read. `ST-00001842-EN` was examined and excluded from a lighting dossier because it concerns a different shutter product. The retained HRM SCS guide has explicit reviewed page scopes in review 0151-0160. HTML originals remain HTML even where the archive's legacy object URL ends in `.pdf`.

The [Device source index](../../sources/devices/index.md), [final batch review and evidence scopes](../review/device-reviews-0201-0210-2026-10-07.md) and fingerprint/byte-length [artifact manifest](../../sources/artifact-manifest.yaml) retain the evidence and inspection limits. The [release statistics](release-statistics-0.2.0.json) state each counting boundary. KB ingestion reused registered originals; it was not a second PDF-discovery campaign.

## KB growth since 0.1.2

| Public content | 0.1.2 | 0.2.0 candidate |
| --- | ---: | ---: |
| Canonical documents | 135 | 345 |
| Atomic claims | 7,449 | 73,915 |
| Retrieval chunks | 1,173 | 7,929 |
| Reference records | 1,423 | 37,678 |
| Live stable identities | 11,353 | 127,796 |

The 210 definitions add 66,466 Device-derived claims. All 57,493 prepared Device source units have reviewed dispositions: 54,702 claimed and 2,791 nonclaim. Commercial/system relations, firmware/build/status/default, direct and Virgin Object membership, field domains and defaults, conditions, filters, conversions, modes, connections, parameters, packages and governing prose remain scoped to their sources. Parameter, firmware and package references do not imply inspection of their payloads.

The final independent-review remediation restored missing standalone context in 18 existing claims: selector functions, ordered calibration steps and a repeated all-slot self-learning condition. Claim identities, exact evidence-unit keys and source pins were preserved. All 7,449 earlier generated claims, 1,173 earlier retrieval chunks and 11,353 earlier lifecycle entries remain unchanged; existing reference identities remain resolvable.

## Compatibility and consumption

This is a new content release. The release label does not advance the parsing contract:

- schema compatibility, manifest and public artifact formats remain `0.1.0`;
- generator version remains `ownkb-build-0.8.2`;
- existing stable IDs are preserved; no consumer schema migration is required;
- the manifest records current hashes, counts and input-content digest.

The four projections are the LLM corpus, retrieval chunks, atomic claims and reference registries, with public schemas, the ID registry and manifest. See [consumer guidance](../../knowledge/CONSUMING.md). Large repository files use Git LFS: repository source archives may contain pointer files, so consumers need hydrated data or the separately supplied hydrated release bundle. The data can be consumed offline without Python, a model, MCP or a network service.

## Review, validation and remaining evidence limits

All 210 descriptions passed the eight-check acceptance gate. A separate read-only reviewer returned **CERTIFIED** for the Phase 15 factual/epistemic assessment of the migration and inspected control follow-ups. Its scope includes the full changed machinery, global invariants across all four projections and explicit risk sampling. It does not independently prove hardware behavior or exhaustively reread every manufacturer original. The [merge preparation record](merge-preparation-2026-10-09.md) preserves that scope and the semantic candidate lineage.

The validated semantic candidate passed 206 KB regression tests, eight schema tests, 28 Device/catalogue tests, 55 evidence tests, deterministic double-build/freshness, provenance/reference/lifecycle integrity, privacy checks and ECV/ESG objective checks. All ten PR results passed before merge. Release publication requires completed validation for the exact tagged revision, authenticated local catalogue validation, verified bundle hashes and no intervening data changes.

Missing exact-product manuals, historical/regional discrepancies, unexamined payloads and hardware corroboration gaps remain explicit. The 268 conflicting claim records retain reciprocal relationships and questions; acceptance does not resolve them or infer installed firmware or current service availability.

Repository-authored content remains under Apache License 2.0. Manufacturer originals and third-party material retain their own rights and provenance. The private catalogue database, firmware/software payloads, credentials and installation-specific identifiers are not included in the public release bundle. Earlier 0.1.0/0.1.1 tags and releases were withdrawn during archive/history cleanup; 0.1.2 is the retained comparison baseline.
