# Installer Database Preservation and Analysis

This capsule preserves the completed archival and bounded analysis of newly identified MyHOME Suite3.5.38 databases. Twenty installer paths represent thirteen unique SQLite payloads. All thirteen were read back from private R2 and SHA/size-verified; seven additive canonical artifact records were published on main in commit `974eced66cf40fdc5b5dc3417357244db710d848`. Existing registry entries were preserved. Vendor database binaries and the analysis branch were not published.

## Source tracks

| Track | Methodical source scope | Exact report / independent review |
| --- | --- | --- |
| Four device-specific systems profiles | Every table/row and all six variant pairs, declared relations, bounded normalized child bags and selected constraints | [Report](systems-report.txt), [review](systems-source-review.txt) |
| MH200N versus MH202/common ScenarioSuite | All79schemas/row bags/keys per profile; complete eight same-key updates and version-key replacement; contextual joins | [Current report](scenario-variants-report.v2.txt), [review](scenario-variants-source-review.txt) |
| Project/plant templates | All27structures/28declared FK rows/38seed or reference rows, with sensitive defaults withheld | [Report](project-templates-report.txt), [review](project-templates-source-review.txt) |
| Canonical archive | Thirteen payloads, twenty member paths, seven descriptors, saved readback attestations and additive registry blocks | [Independent local review](archive-source-review.txt), [readback receipts](archive-readback-receipts.json), [registration](canonical-registration.json) |

The canonical treatments are [Device Application Databases](../../../internals/device-application-databases.md), [ScenarioSuite Variants](../../../scenario-engine/scenario-suite-variants.md), [Project and Plant Templates](../../../internals/project-and-plant-templates.md) and the [installer census](../../../internals/installation-and-source-layout.md#installer-database-census).

## Provenance and verification

[Provenance](provenance.json) pins nineteen exact exports, three reproducible collectors, current canonical registry identity and archive scope. The [member map](canonical-member-map.json) retains every source path and canonical ID; the [inventory](installer-database-inventory.json) pins the installer/layout/index and individual files. Archive-only metadata publication preceded this analytical work.

Successful `--check` runs reparse unchanged source data and compare exact evidence without writes. Full structural/row comparisons are separate from selected semantic interpretations; they do not certify every consumer, UI policy or physical capability. An independent source review checks each author area. The [integration review](integration-review.txt) checks final canonical prose; the [validation](validation.json) retains identity/preservation/branch results. Strict ECV/ESG results are saved separately in `postwrite-checks.json` and pinned by the completion record.

The archive reviewer verified local object bytes, saved remote readback receipts and registry snapshots. That review does not claim an additional independent R2download, ACL query or Git-host query. The parent archival transaction itself performed the configured-helper downloads and remote canonical-head verification.

## Preserved source refinements and privacy

The [project pre-output history](project-preoutput-history.json) retains a failed zero-FK assumption; its guard stopped before evidence generation, and the new collector records the original22+6relationships. The [scenario version-key history](scenario-version-key-history.v2.json) retains the initial incorrect expected matched-version-row count; the full composite key instead yields one removed and one added version tuple. Exact failed drafts, failures and first successful candidates remain in local evidence.

The [sanitized project schema](project-schema-sanitized.json) and [finite reference data](project-reference-rows.json) withhold credential-bearing schema defaults, populated plant network/GUID/identifier/contact values and raw sensitive declarations. Ordinary structural defaults remain recorded. The [scenario changes](scenario-logical-differences.v2.json) export only the exact whitelisted manufacturer-row differences, while [context queries](scenario-context-queries.v2.json) preserve their selected source context. The [systems source rows](systems-selected-source-rows.json) retain selected noncredential template declarations. No private user project is supplied or fabricated.

UI/template limits are not universal protocol or physical limits. Retained disconnected templates do not prove feature absence or a runtime defect. Scenario trigger-pattern literals are not ordinary WHAT substitutions. Empty project templates do not establish installed state or cross-file identity binding. No vendor expressions, regexes, CLR/JavaScript/ARM code, target services, gateway/bus or Physical Device ran. Wider Device gates and closed authentication/session/framing boundaries remain unchanged.
