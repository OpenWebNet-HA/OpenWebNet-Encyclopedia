# MHCatalogue source-profile comparison review

This capsule supports [MHCatalogue Source Profiles](../../../internals/mhcatalogue-source-profiles.md). It compares the exact embedded MyHOMEServer1 `3.87.13` and installer MyHOME Suite `3.5.38` databases. Original databases remain private canonical artifacts; no vendor binary or raw database is copied into Git. Vendor, stored-expression, firmware and physical execution are zero.

## Source reports and coverage

| Area | Report | Scope |
| --- | --- | --- |
| Whole-source comparison | [Catalogue report](catalogue-report.txt) | All75tables/complete typed row bags, keys, schema/index/type differences, commercial matching and source profiles |
| Firmware graph | [Firmware and resources](firmware-report.txt) |114shareddefinitions/five child relation bags, alladded definitions/builds/modes, resources and selectedcanonical products |
| Objects/configuration | [Object and field relationships](objects-report.txt) |68same-ID changes,114equivalent IDmoves, normalized child ranges and actual retained-field metadata differences |
| Synthesis | [Results and implications](synthesis.txt) | Source selection versus IDreuse, genuine changes and consumer limits |
| Coverage | [Examined scope](coverage.txt) | Exact data/source/review scope; counts are not complete firmware coverage |
| Remaining work | [Reader questions](remaining-questions.txt) | Actual catalogue eligibility/version/field-resolution consumers, not unfinished row comparisons |
| Input consultation | [Source comparison preflight](source-preflight.txt) | Identity, product/model/owner boundaries and matching anchors |

Both databases pass complete integrity and declared-FK checks. They share all75table definitions but differ by one extra embedded index. DATA4.4.0 metadata is the same despite content differences. The [embedded archive registration](archive-registration.json) pins its distinct canonical record; Suite's different SHA remains a separate source.

## Evidence and reproducibility

[Base exports](BASE_EXPORTS.json) and [Object evidence exports](OBJECT_EXPORTS.json) pin exact source paths, sizes and SHA-256 hashes. The evidence directory retains all-table fingerprints/key differences, safe commercial/context mappings, version/build/mode ledgers, queries and source-specific configuration correspondence. Arbitrary raw condition/filter/default/state records and credentials are not exported wholesale. Selected public manufacturer labels and numeric metadata are explicit whitelists.

Local collectors are under `work/mhcatalogue-comparison/2026-10-31/`:

```
python3 -B catalogue/compare_catalogues_v2.py --check
python3 -B catalogue/collect_supplement_v2.py --check
python3 -B firmware/collect_firmware_v1.py --check
python3 -B objects/collect_objects_v1.py --check
python3 -B objects/collect_selected_ranges_v1.py --check
```

Run those relative commands from the local comparison directory. The five current collectors reproduce42outputs including their manifests, using host SQLite read-only/immutable/query-only connections with trusted_schema disabled. Initial creation refuses overwrite. Actual first candidates and reported earlier failed assumptions/metadata clarifications are preserved, with no reconstructed missing history or original database modification. These are source comparisons, not original consumer execution or Device acceptance tests.

## Independent review and completion

| Review | Record |
| --- | --- |
| Whole-source evidence | [Source review](catalogue-source-review.txt), [second source review](catalogue-second-review.txt) |
| Firmware graph | [Independent review](firmware-source-review.txt) |
| Object/configuration graph | [Independent review](objects-source-review.txt) |
| Final source-profile integration | [Integration review](integration-review.txt), [second documentary review](integration-second-review.txt) |
| Reproduction | [Five current collector checks](source-checks.json) |
| Identity/preservation | [Final validation](validation.json) |

Exact report/source/evidence identities, historical reference snapshots, final mechanical proof and current branch state are retained separately from source-semantic reviews. Earlier source scopes and Device definitions are not replaced by the embedded selection. Missing products, empty association tables, Prototype/RC/default/status flags and reused IDs do not independently establish runtime support, physical behavior or a general migration policy. Wider Device review remains pending; previously stopped authentication/session/framing investigations remain closed.
