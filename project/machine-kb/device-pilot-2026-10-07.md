# Reviewed Device ingestion pilot, 7 October 2026

The Machine KB pipeline now supports bounded ingestion of accepted Device definitions. This candidate integrates ten representative definitions on `docs/devices-foundation`; 200 remain explicitly pending. It is a pilot candidate, with independent semantic certification still required before merge, tagging or release.

## Selection and outcomes

| Device | Representative surface | New claims | Material preserved boundary |
| --- | --- | ---: | --- |
| OWN-DEV-0001 | F418U2 universal dimmer | 465 | Physical/software domains, complete conversions, simultaneous 2023 source conflict and gateway-scoped first-hand evidence |
| OWN-DEV-0002 | F454 gateway/server | 205 | Two catalogue firmware tuples, later release history/HMAC, parameter associations and unresolved diagnostic semantics |
| OWN-DEV-0010 | PIR/ultrasonic/daylight sensor | 392 | One sensing and sixteen IR Modules, current/revision differences, empty subset restrictions and out-of-filter defaults |
| OWN-DEV-0021 | Single-relay lighting actuator | 152 | Load-specific ratings rather than universal 16 A capability; reset and zero-crossing configuration |
| OWN-DEV-0045 | Shutter actuator | 210 | Physical/software motor encodings, tenths-of-seconds pulse mapping, presets, calibration/slat bytes and default/filter conflicts |
| OWN-DEV-0076 | Two-output Room Controller | 128 | 1000 W/VA per output; physical outputs distinct from catalogue Modules and reusable dimmer load types |
| OWN-DEV-0200 | K4652M2 multifunction control | 457 | Physical width versus Modules, direct versus Virgin-only roles, LED/address conflicts and production-scoped feedback |
| OWN-DEV-0207 | F460 server | 209 | Candidate gateway placements, reusable F454 Object label, firmware defaults, app/server versions and source-specific capacity/dimensions |
| OWN-DEV-0209 | F459T documentation-gap case | 89 | Explicit SKU-to-item identity remains established; electrical/HVAC/EAN/procedural evidence remains unknown |
| OWN-DEV-0210 | Linea 5000 entrance panel | 248 | Entrance-panel identity versus reusable touchscreen/door-entry roles; source-specific radio/dimensions/capacity and pending payloads |

The 2,229 prepared source units have explicit dispositions: 2,044 claimed and 185 non-claim. Non-claim material is navigation, source inventory or non-propositional lead-in text, retained in the complete corpus/chunks and source registry where applicable. All 349 new sections, including empty structural headings, are accounted for. Field-domain and field-default assertions are separate; 478 scalar numeric defaults use the existing integer value representation. The graph includes 511 new configuration-field entities, source-scoped Firmware, Module and Object entities, distinct Virgin associations and commercial identities.

## Pipeline and compatibility

- The closed inventory enumerates all 210 definitions and validates the current queue's eight-check acceptance gate before any selected page enters the shared IR.
- Only integrated definitions enter the classified canonical source manifest. Category pages, indexes, guides and review logs are excluded.
- Device pages use the existing semantic `device-model` area and retain `devices/definitions/…` provenance paths. The public schema and format remain 0.1.0; no closed enum/property is extended. The legacy schema-pinned generator identifier remains unchanged; the Git candidate revision identifies this pipeline extension.
- Incremental allocation appends document/chunk IDs above both current mappings and lifecycle history and rejects alterations to an existing document/heading mapping. Routine builds do not allocate identities or refresh pins.
- Source-unit review fingerprints every table header/cell and governing paragraph/list/code block. Claims must retain all source-cell content and qualifications, map to the same section and name the same exact unit in atomicity, evidence and coverage reviews.
- Eight cases demonstrated that lexical block matching could select a different repeated table. New Device claims use explicit reviewed source units instead.
- Privacy handling preserves narrowly recognized public technical-sheet references and public web paths, while continuing to remove installed Device IDs, network addresses and private filesystem paths before derivation. Four pilot pages required sanitization.
- Canonical source provenance uses the first substantive section when the H1 is only a title. This keeps source references resolvable through retrieval without manufacturing an empty chunk.

Every existing claim, curated context, reference seed and lifecycle entry was preserved. Existing generated claims and chunks are unchanged. The existing catalogue source gains reciprocal links from the new graph; this is a relationship addition, not a source reinterpretation.

## Evidence and remaining limits

All input facts come from the ten accepted canonical Device definitions and their retained source inventory. The pilot is a representation migration, not renewed PDF discovery or a claim that previously unexamined payloads have now been inspected. Seventy-three public original fingerprints were matched to existing artifact-manifest registrations; no new original or PDF was uploaded. Private database/software payloads are not imported or redistributed.

Catalogue assertions use the public catalogue source and MyHOME Suite 3.5.38 applicability. Direct source-specific product citations retain manufacturer evidence where identifiable; mixed/reconciled assertions remain canonical synthesis. Commercial exports are official catalogue evidence. Retained first-hand observations remain bounded to the named Device/gateway research paths. Manufacturer-described behavior and diagnostic candidates do not become observed runtime behavior.

The F418U2 temperature disagreement has reciprocal contradiction links and an open resolution. Other dimensional/rating/default/filter discrepancies and unexamined XML, firmware, developer, environmental and BIM payloads remain explicit in claims, cautions and questions. No replacement default, hardware equivalence, universal protocol capability or installed firmware is inferred. F459T's missing specification is a documentation gap, not an unresolved identity.

All four projections are generated together: the LLM corpus, retrieval chunks, claims and reference registries. Candidate totals are 145 documents, 1,556 sections, 1,502 chunks and 10,004 claims. The remaining 200 definitions are not implicitly covered by these totals.

## Validation and continuation

The candidate was inspected as a full-review change because it extends the source topology and build semantics. The source-unit ledger, source/evidence classifications, representative semantic boundaries, identity allocation and generated diff were inspected; the pilot does not claim independent certification.

| Check | Result |
| --- | --- |
| Complete Machine KB check | Passed: two clean builds produced identical bytes; committed output freshness, manifests, schemas, cross-artifact consistency, references, text hygiene, privacy and Device completeness passed |
| Machine KB regression suite | 73 tests exercised: 71 passed initially; the two failures were repaired and their complete privacy (20 tests) and pilot semantics (6 tests) suites passed on rerun |
| Device ingestion negative and allocation tests | 8 passed, including omitted/corrupted rows, altered headers, wrong scope, stale acceptance, retired IDs and private/public identifier distinctions |
| Public schemas | 8 passed; schema files and compatibility version unchanged |
| Source-unit conservation | All 2,229 units and 349 new sections accounted for; no unmapped pilot claims |
| Existing data and identity preservation | All 7,449 existing claims, 1,173 chunks, 11,353 lifecycle entries, curated contexts, reference seeds and document/section mappings preserved |
| Device completeness | All 210 definitions passed against the fingerprint-verified MyHOME Suite 3.5.38 catalogue |
| Artifact manifest | 807 registrations passed; 73 originals reused by the pilot, no new originals |
| ECV human-page check | 378 pages, zero objective failures; 14 heuristic review candidates remain and are not certifications |
| Generated privacy scan | Passed across 20 generated artifact/metadata surfaces |
| Diff inspection | Scoped pipeline, curated-input, generated-artifact, regression and pilot-ledger changes; no Device rewrites, raw vendor payloads or public schema changes |

The initial privacy failures were public `LE`, `RA` and numeric `ST` manufacturer document references and an HTTPS product-sheet path, rather than installed identifiers or local paths. The detector and final scanner now share narrowly scoped handling; negative tests retain rejection of actual installed identifiers and local/file-URI paths. The F459T regression initially matched its nested catalogue-label sections as well as its identity row; its selector was corrected without changing the catalogue identity claim.

Expansion to further devices remains a separate bounded task; it must keep the same source-unit dispositions, evidence classification, acceptance, privacy and identity guarantees. Deterministic checks support this candidate but do not replace independent semantic certification.
