# ScenarioSuite Database for MH202

`Scen_SuiteDB_ENG.db` is a separate MyHOME Suite scenario-editor source recovered from device package `1902_1.0_LGG`. It supplies object/area permissions, command-field declarations, status-evaluation rules and address catalogues. It is distinct from the two [ScenarioDevices databases](database-model.md), their four-table hierarchy and their identifier namespaces.

The database establishes declarations and checked relationships. The [generator consumers](scenario-suite-generator.md) establish selected use of those declarations. Neither evidence class alone proves an executed editor/compiler, installed Configuration, complete generated script grammar or Physical Device behavior.

## Source identity and structure

| Property | Exact source |
| --- | --- |
| Canonical artifact | `myhome-suite-3.5.38-mh202-1902-lgg-scen-suite-db-eng` in the [artifact manifest](../sources/artifact-manifest.yaml) |
| Original installer member | `default/resTargetDir4/devices/1902_1.0_LGG/xml/Steps/Step_2/Scen_SuiteDB_ENG.db` |
| Bytes / SHA-256 | `2542592` / `ae1e60ca9b06eeb1eecd5bc8e21ff5ba2bdb928aa47075a2e7d8995c41e06e29` |
| Installer / internal DB version | MyHOME Suite `3.5.38` / `ANA_VERSIONE_DB = 1,0,53` |
| Catalogue content | `79` tables, `16` families, `63` editor objects, `597` command definitions, `608` compilation rules, `67` status-request rules |
| Working tables | All `24` `TMP_` tables are empty in this shipped copy |

The database version, package label and MH202 Firmware `1.0.24` are different applicability scopes. Empty working tables provide schema without a configured scenario instance; they do not establish the absence of a generator or product feature.

There are no declared foreign keys. Source joins below use explicit column relationships and checked data patterns, not the enforced hierarchy of ScenarioDevices. `59` tables declare primary keys, including nine composite keys; `20` do not. A successful SQLite integrity check does not establish semantic completeness or validate every inferred relationship. See the [independent schema review](../project/review/scenario-suite-database-1.0.53/baseline-review.txt).

## Scenario areas and alarm restrictions

`ANA_AREA` labels area `3` WHEN IT HAPPENS, `4` ONLY IF, `5` EXECUTE and `6` Stop if it happens. Areas `7`, `8`, `9` identify trigger enable, trigger disable and panic. These labels corroborate the documented separation of scenario roles.

| Editor object | Object/association declarations | Interpretation boundary |
| --- | --- | --- |
| `39` Alarm | Start, OnlyIf and Stop; no Action permission or area `5` command associations | Supports the documented MH202 reaction/condition role; does not supply arming commands |
| `54` Engage Disengage | Start and Stop; no OnlyIf or Action associations | These names describe selected incoming events in this profile |
| `9` Delay / `45` Random delay | Seconds/minutes/hours choices in Action | Labels do not prove emitted script syntax or elapsed timing |
| `61` Astronomic clock | Sunrise/sunset in Start/Stop; day/night in OnlyIf | Separate commands and roles, without a complete clock/provider implementation |
| `7` CEN / `52` CEN PLUS | The only nonzero object-level enable/disable/panic flags in this table | Eligibility metadata, not proof of the only possible runtime producer |

The full permission-led join retains all `64` `ASS_OBJ_AREE` rows: `63` match editor objects and extra key `0` does not. Its intended consumer role is unresolved. Family activation and object permission remain separate.

Different declaration levels sometimes disagree. Alarm object `39` has Action disabled and no Action association, while its compilation rows `231..236` have `ACT_AREA=1`. Across all `608` rules, object-versus-rule comparisons retain differing Start, Stop, OnlyIf and Action flags. Consumer precedence remains unresolved; neither level alone is a complete product-support matrix.

`TMP_SCENARI` has `REPEAT`, `RESTART` and `SPT_PATH` columns, but no rows. These declarations do not prove full restart/panic recovery or a generated Start-to-OnlyIf-to-Action sequence. The [scheduler report](../project/review/scenario-suite-database-1.0.53/scheduler-report.txt) preserves complete permission data, selected timing metadata and comparisons with the reviewed firmware/manual evidence.

## Counter and Boolean operations in WHO 17

Exact joins map editor objects `66` Counter and `67` Boolean through `ASS_OBJ_CHI` to stored `OPEN_CHI = '17'`. These IDs are separate from the WHO value and from catalogue Objects.

| Editor operation | Stored `OPEN_COSA` fragment | Status declaration |
| --- | --- | --- |
| Counter value / set value | `6` / `#6*%cv%` | Request dimension `6`; reply function `EXTRACTVALUE`, dimension `6`, parameter string `1` |
| Counter increase / decrease | `#8*1*%cvs%` / `#8*0*%cvs%` | Adjustment declarations, distinct from the value request |
| Boolean True / False | `7*1`, `7*0` for events/conditions; `#7*1`, `#7*0` for actions | Request dimension `7`; `EXTRACTVALUE`, dimension `7`, parameter string `1` |

The selected compilation rules order `#ID_CHI`, `ID_DOVE`, `ID_COSA`. Substitution, formatting and reply-parameter indexing are not executed here.

Both objects offer exactly `1..128` addresses in their selected areas. The lists corroborate the separate word/byte slot domains in [MH202 source](../reverse-engineering/firmware-analysis/mh202-1.0.24-record-and-script-lifecycle.md#who-17-manager-slots-and-local-result-codes). Counter increase/decrease literals also agree with the selected DIM8 direction branches. This does not make them scene IDs, the `300` script-file domain or named interpreter variables.

Two declaration/consumer distinctions remain important:

- Boolean OnlyIf associations exist while the selected compilation rows have `COND_OK_AREA=0`; separate status rules have custom valuation enabled.
- The earlier candidate joins to temperature/time-labelled range rows are superseded as consumer relationships. The [actual graphic-type dispatcher](scenario-suite-generator.md#counter-text-field-namespace) selects `ANA_TEXT` row `2` CountValue and row `3` ValueStep, both `[0-32000]`, for these text fields. No Counter temperature/time units follow; effective UI enforcement and complete saved-project behavior remain unexecuted.

The [variable report](../project/review/scenario-suite-database-1.0.53/variables-report.txt) retains exact keys, address sets, status rules, metadata discrepancies and inherited firmware source locators.

## WHO 25 address profiles and command context

Objects `51` Scenario PLUS, `52` CEN PLUS and `53` Contact join through local `ID_CHI=14` to stored WHO `25`.

| Editor object | Complete stored address evidence | Scope |
| --- | --- | --- |
| Scenario PLUS | Prefix `1` concatenated with `1..255`; `255` choices per selected area | Device-package profile; not a universal public ScenarioPlus range |
| CEN PLUS | Prefix `2` concatenated with `0..2047`; `2048` choices per selected area | Corroborates the published CEN+ composition |
| Contact | Raw catalogue has `3` concatenated with `0..201`; object associations offer only `3` concatenated with `1..201` | General catalogue row `30` is excluded from Contact's selected choices |

The prefixes are concatenated fields, not decimal arithmetic offsets. Actual stored strings and complete sets support these claims, rather than just endpoint comparisons or placeholder names.

Contact fragments `31#1`/`32#1` occur in Start/Stop associations; `31#0`/`32#0` occur in OnlyIf. This corroborates the public event-versus-requested-state parameter distinction. The same WHO does not merge ScenarioPlus, CEN+ and dry-contact semantics. ScenarioPlus STOP is associated with Start/Stop but absent from its selected Action command list, despite the object's general Action permission.

### Published contact address forms

The original [WHO 25 specification](https://archive.openwebnet-ha.org/sha256/12/2d/122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927.pdf), version `1.0.0`, page `4`, specifies prefix `3` followed by `1..201` for virtual contacts, and prefix `3` followed by two digits `1..9` for physical configurators. The database corroborates the virtual form; the publisher establishes the separate physical form. `WHERE 339` fits the notation, without establishing a configured target or supported reply.

The [Dry Contact and IR reference](../functional/who-25-transversal/dry-contact-ir.md) is the canonical address treatment. The [preserved correction](../project/review/scenario-suite-database-1.0.53/CONTACT_PREFIX_CORRECTION.json) records the superseded omission of the prefix; the [address evidence](../project/review/scenario-suite-database-1.0.53/addressing-report.txt) retains complete database sets and source review.

## Evidence and limits

The [database evidence](../project/review/scenario-suite-database-1.0.53/) retains exact SQL relationships, selected complete sets, source variants and independent schema/data reviews. The original files are privately archived; the analysis uses read-only database inspection.

The [ScenarioSuite consumer reference](scenario-suite-generator.md) establishes area filtering, record materialization, Counter text-field resolution, reply-template use and script/index writers. Complete UI permission precedence, reply indexing/evaluation, configured project generation, deployment and physical behavior remain unresolved.

## Separate MH200N profile

The [complete profile comparison](scenario-suite-variants.md) identifies a separate MH200N package `1331` database, SHA-256 `83b7fa13c224012ebd1561fbc2895deb599b06223eb8e5041f565b7c5b7dbfd8`. Its schema matches this MH202/common source, while eight same-key rows and the composite version tuple differ. Findings retain this page's exact source identity; same-name files are not silently merged.
