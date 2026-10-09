# OpenWebNet Machine KB 0.2.0

## The Device library joins the KB

OpenWebNet Machine KB 0.2.0 connects commercial product references to **210 reviewed Device definitions**, their documented capabilities, configuration models and source evidence. Coverage spans **541 commercial records** in the MyHOME Suite 3.5.38 catalogue, with additional printed references and packages available through the commercial index.

The KB grows from **7,449 to 73,915 claims**, nearly ten times its previous size. That growth brings product-level detail into the same knowledge base as the protocol, programming, diagnostics and Device model documentation.

| Release highlights | Coverage |
| --- | ---: |
| Reviewed technical Device definitions | 210 |
| Catalogue commercial records covered | 541 |
| Distinct PDFs inspected within documented product scopes | 734 |
| Atomic claims | 73,915 |
| Retrieval chunks | 7,929 |

## From a product reference to its documented capabilities

A product code is the starting point. The Device library connects it to the relevant technical definition, commercial variants, manufacturer documents and catalogue configuration data. Readers can follow those relationships through the [commercial index](../../devices/index.md); software can use the corresponding claims, retrieval chunks and reference records.

That makes it easier to investigate a Device's documented role, compare references that share a catalogue item, find the applicable Firmware and configuration fields, and trace an assertion back to its evidence. Definitions cover physical controls and connections alongside software fields, legal values, defaults, conditions, filters, conversions, modes and package associations.

The distinctions matter. Physical capabilities retain their manufacturer-document scope. Reusable Module, Object and Virgin Object associations retain their catalogue and Firmware scope. Installed behavior remains an observation question where hardware evidence is absent.

All **210 accepted definitions are now integrated** into the four Machine KB projections: the LLM corpus, retrieval chunks, atomic claims and reference registries. The Device description and ingestion queues are complete.

## Built from a substantial source investigation

The Device research and review examined **734 distinct PDFs at their relevant product sections**, alongside **30 retained HTML product records**. The work included technical sheets, installation and programming manuals, catalogues, regional documents and historical revisions. Ratings, load tables, configuration procedures and diagrams were reconciled where their product and revision scopes allowed it.

The semantic-review campaign added **80 PDF originals and three HTML originals** to the archive. Across the complete advance from release 0.1.2, including the earlier description research, **632 new PDF originals** were registered. KB ingestion then reused those registered originals by fingerprint.

The evidence remains navigable: the [Device source index](../../sources/devices/index.md) links retained originals, the [review records](../review/device-reviews-0201-0210-2026-10-07.md) document inspection scopes, and the [artifact manifest](../../sources/artifact-manifest.yaml) preserves SHA-256 fingerprints and byte lengths.

Inspection was scoped to the applicable product material. The figures do not claim every unrelated page or translated chapter of a multi-product document was read. One inspected PDF was ruled out for a mismatched product association; the counting details below retain that distinction.

## More knowledge, the same consumer contract

| Public content | 0.1.2 | 0.2.0 |
| --- | ---: | ---: |
| Canonical documents | 135 | 345 |
| Atomic claims | 7,449 | 73,915 |
| Retrieval chunks | 1,173 | 7,929 |
| Reference records | 1,423 | 37,678 |
| Live stable identities | 11,353 | 127,796 |

The Device integration adds **66,466 claims**. All 57,493 prepared Device source units have reviewed dispositions: 54,702 claimed and 2,791 nonclaim. Governing prose and source qualifications remain attached to the material they constrain.

Existing consumers keep the **0.1.0 schema, manifest and artifact-format contract**. No consumer schema migration is required. All 7,449 earlier generated claims, 1,173 earlier retrieval chunks and 11,353 earlier lifecycle entries remain unchanged; existing reference identities remain resolvable. Generator version remains `ownkb-build-0.8.2`.

For offline use, the published release bundle contains the full data files, public schemas, manifest, ID registry and consumer guidance. GitHub's generated source archives may contain Git LFS pointers; consumers need hydrated files or the hydrated bundle. See [Consuming the Machine KB](../../knowledge/CONSUMING.md) for direct context, retrieval and claim-based integration.

## Reviewed, with uncertainty preserved

Every Device description passed the eight-check acceptance gate. A separate read-only reviewer returned **CERTIFIED** for the Phase 15 factual and epistemic assessment of the migration and inspected control follow-ups. The review covered the changed machinery, global invariants across all four projections and explicit risk sampling.

The final audit repaired standalone context in **18 claims**, including selector functions, ordered calibration steps and an all-slot self-learning condition. Claim identities, evidence-unit keys and source pins were preserved.

Validation of the semantic candidate passed 206 KB regression tests, eight schema tests, 28 Device/catalogue tests and 55 evidence tests, together with deterministic builds, freshness, provenance, reference/lifecycle integrity, privacy and ECV/ESG objective checks. All ten PR results passed before merge. The [merge preparation record](merge-preparation-2026-10-09.md) preserves the certification scope and candidate lineage.

Documented gaps remain visible. Missing exact-product manuals, historical or regional discrepancies, unexamined payloads and hardware corroboration gaps remain part of the data. The **268 conflicting claim records** retain reciprocal relationships and questions. Parameter, Firmware and package references do not imply inspection of their payloads; acceptance does not establish installed Firmware or current service availability. Independent review does not exhaustively reread every manufacturer original or prove hardware behavior.

## Coverage and counting details

| Measure | Count |
| --- | ---: |
| Commercial lookup mappings, including supplementary printed references and packages | 602 |
| Distinct displayed brand/line-reference pairs | 601 |
| Catalogue brand labels / product-line labels | 4 / 18 |
| PDF originals in the Device evidence index | 733 |
| Additional PDF inspected and rejected for a mismatched product association | 1 |
| HTML product records in the Device evidence index | 30 |

The Legrand Arteor `572736` reference has two lookup mappings because its publisher and catalogue associations conflict. It counts once among distinct brand/line-reference pairs. Shared technical-item membership does not establish identical hardware across commercial variants. Coverage describes the retained catalogue and documentation, rather than every product currently sold.

PDF counts use distinct archival SHA-256 fingerprints, so shared manuals are counted once. The additional inspected PDF, `ST-00001842-EN`, was excluded from a lighting dossier because it concerns a different shutter product. The retained HRM SCS guide has explicit examined-page scopes in review 0151-0160. HTML originals remain HTML even where a legacy archive URL ends in `.pdf`. The [audited release statistics](release-statistics-0.2.0.json) record each counting boundary.

## Release and licensing

[OpenWebNet Machine KB 0.2.0](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/releases/tag/machine-kb-v0.2.0), tag `machine-kb-v0.2.0`, was published on 2026-10-09 at validated revision `447e4c731f44c1e753efb33f245be5444f15912c`. The accepted dataset was merged through [PR #48](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/pull/48) at `29a07b4934fd4fb5da3e5b04d841bc698bfc6c6f`. Exact-release catalogue validation, hosted KB validation and Encyclopedia compliance passed before tagging. The hydrated offline bundle and `SHA256SUMS` are attached to the release; bundle SHA-256 is `32398d8f45260bb1989f6826a09f2ece49b10c9d6f33241756266c9eea10f5ad`.

The retained comparison baseline is 0.1.2. Earlier 0.1.0/0.1.1 tags and releases were withdrawn during archive/history cleanup. Repository-authored content remains under Apache License 2.0; manufacturer originals and third-party material retain their own rights and provenance. The public bundle excludes the private catalogue database, manufacturer originals, Firmware/software payloads, credentials and installation-specific identifiers.
