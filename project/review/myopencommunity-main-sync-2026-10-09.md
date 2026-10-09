# MyOpenCommunity Branch Synchronization

This review merges main revision `b2717281990c0f09641b44d17b6807bf5dc3efb4` into the integration branch at `85cdc049393b6aa9f315107327fce0cf12f0ba6f`. It preserves the device-description release and the scoped MyOpenCommunity provenance work. It does not publish a new KB release or merge the integration branch into main.

## Identifier collisions

Both branches allocated IDs after their shared baseline. Some spellings consequently identify different records in the two histories. Main's published device-release IDs retain their meaning. Unreleased integration additions use the common ID grammar with a `moc-` namespace component. The 2.0.0 candidate retrieval schema explicitly accepts that component for chunk IDs while retaining the six-digit numeric suffix requirement.

| Kind | Migrated IDs |
| --- | --- |
| Claim | 304 |
| Source | 86 |
| Chunk | 67 |
| Document | 1 |
| Section | 17 |
| Total | 475 |

The [revision-scoped migration map](myopencommunity-branch-id-migration-2026-10-09.json) maps previous integration IDs to current IDs. A previous ID is meaningful only together with the map's `source_revision`. These are not global aliases: the previous spellings now resolve to main's independently allocated records. Two mapped section identities were reserved empty sections rather than emitted records.

For example, integration claim `ownkb:claim:c007528` becomes `ownkb:claim:moc-c007528`; main's `ownkb:claim:c007528` remains the published device claim. Existing shared claims retain their identifiers, including corrected and retired claims. Earlier review reports remain historical records; the current provenance audit and machine inputs use the migrated IDs.

## Merge method and boundaries

Inputs were compared against both parents and their common ancestor. Claim, reference, lifecycle and coverage records were merged by identity; section/chunk identities were merged by their existing keys. Main's new device records were retained without reinterpretation. Integration references were translated consistently in claims, examination-to-claim mappings, context, coverage, canonical source records and lifecycle entries.

The merge keeps the 2.0.0 provenance compatibility candidate, original artifact locators, examination methods, conditions, limitations and finding dispositions. It also keeps main's device-unit completeness checks, catalogue verification, privacy gates and LFS storage. Generated artifacts are rebuilt from combined inputs rather than text-merged. Preserved implementations and synced source material are not edited.

This operation adds no new protocol conclusions and does not expand the reviewed repository coverage. The existing deferred and excluded findings retain their disposition. No historical integration ID is silently treated as an alias for a different published device finding.

## Verification

The regenerated candidate contains 74,218 claims, 7,996 chunks and 346 canonical documents. It retains all 124 evidence finding dispositions and their claim bindings. Input comparison confirms that all 66,466 added device claims, 36,045 added reference seeds and 116,443 added lifecycle entries from main are unchanged. Generated device claim records are byte-identical to main's records. All 226 tracked device-definition and source files compared against main are byte-identical.

Shared records retain the earlier integration branch changes, including section-content hash updates. One reference seed is updated from the shared baseline, and one lifecycle entry preserves the integration branch's prior retirement. The merged source/claim/chunk references pass the existing build joins without implicit aliases.

Passed checks at this stage: combined build; 28 device-tool tests; 55 evidence acceptance tests and all four canonical evidence packages; eight schema tests; style and core-value objective checks; 807 external artifact registrations; canonical-source audit with all 25 fingerprints verified and no failures.

The complete KB regression set passed: 220 tests, partitioned into independent build (4), claim (14), reference (5), remaining (164) and privacy (33) groups. The partition inventory accounts for every discovered test exactly once. These are Encyclopedia/KB tooling tests, not a new execution of the archived MyOpenCommunity suites.

The normal `check.py` passed on an isolated copy of all 707 tracked files, including hydrated LFS data: fresh double builds, manifest/schema validation, cross-artifact consistency, references, text hygiene, privacy and all 210 device definitions. All 707 files were fingerprint-compared to the working tree after validation with no differences. The final working-tree privacy scan also passed on all 21 public artifact and metadata surfaces. Only this validation report was completed afterward.

The first integrity attempt exposed the retrieval schema's narrower numeric-only ID rule. The candidate schema now explicitly permits `moc-` chunk IDs, with regression tests for valid numeric forms and malformed/foreign prefixes. All 7,996 chunks passed the corrected schema before the full checks were rerun. No validator or catalogue gate was bypassed.

The complete staged diff and parent comparisons were reviewed. Main remained at the recorded revision on the final remote check; the integration branch had no concurrent remote additions. No merge into main, force push, release tag or KB release is performed.
