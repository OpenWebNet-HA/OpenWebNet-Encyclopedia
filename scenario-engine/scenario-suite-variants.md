# ScenarioSuite MH200N and MH202 Database Variants

MyHOME Suite `3.5.38` contains two distinct payloads named `Scen_SuiteDB_ENG.db`. Complete schema and logical-row comparison establishes their exact differences; the basename alone does not identify one universal profile.

These are installer configuration sources associated with the [MH200N](../devices/definitions/own-dev-0131-mh200n-scenario-programmer.md) and [MH202](../devices/definitions/own-dev-0151-mh202-scenario-programmer.md) scenario programmers. They were not recovered from running gateways. No compiler, firmware, vendor expression or Physical Device was executed.

## Exact source profiles

Both files are `2542592` bytes and are registered in the [artifact manifest](../sources/artifact-manifest.yaml).

| Profile | Installer member suffix | SHA-256 / database-local version |
| --- | --- | --- |
| MH200N | `devices/1331_1.0_BT/xml/Steps/Step_2/Scen_SuiteDB_ENG.db`, identical LG alias | `83b7fa13c224012ebd1561fbc2895deb599b06223eb8e5041f565b7c5b7dbfd8` / `1.1.0` |
| MH202/common | `devices/1902_1.0_LGG/xml/Steps/Step_2/Scen_SuiteDB_ENG.db`, identical `default/resTargetDir2/db/Scen_SuiteDB_ENG.db` alias | `ae1e60ca9b06eeb1eecd5bc8e21ff5ba2bdb928aa47075a2e7d8995c41e06e29` / `1.0.53` |

Device-package member paths in this table begin under `default/resTargetDir4/`. Artifact IDs are `myhome-suite-3.5.38-mh200n-1331-1.0-scen-suite-db-eng` and `myhome-suite-3.5.38-mh202-1902-lgg-scen-suite-db-eng`. Suite release, package label, database version tuple and product Firmware remain separate namespaces. Numeric version ordering does not establish chronology, compatibility or an upgrade path.

## Complete comparison result

Both profiles have identical `79`-table schemas and `54406` rows each. Fifty-nine tables declare primary keys; twenty do not. No foreign keys are declared. Comparisons preserve SQLite value types and duplicate-row multiplicity, without equating rowid or physical row order with semantic identity.

Exactly eight rows retain their primary keys while changing nine nonkey cells. The sole database-version tuple is instead one removed and one added composite-key row. All differences occur in four tables; the other `75` tables match logically. All `24` working `TMP_` tables are empty in both sources.

Direction below is MH200N to MH202/common, as a comparison rather than a migration chronology.

| Table / source row | Exact difference |
| --- | --- |
| `ANA_COSA`, command `317` | `OPEN_COSA`: `1` → `4` |
| `ANA_OPEN_RULE_COMPILE`, rule `284` | `OPEN_FIELD_3`: `1` → `4` |
| `ANA_OGGETTI`, Movement `59`, Lighting `62`, Twilight `63`, Rain `64`, Wind `65` | Stored order `1..5` → `2..6` respectively |
| `ANA_OGGETTI`, Presence `69` | Family `13` → `15`; order `2` → `1` |
| `ANA_VERSIONE_DB` | Composite key `(1,1,0)` removed; `(1,0,53)` added |

The version table's key includes all three VERSION/RELEASE/BUILD columns. Its two one-sided rows are not two changed nonkey cells. Full exact row events and all unchanged-table fingerprints are retained in the [comparison report](../project/review/installer-databases-3.5.38/scenario-variants-report.v2.txt).

## Dimmer trigger-pattern distinction

Command `317` belongs to object `43` Dimmer `100`, with selected associations only in Start area `3` and Stop area `6`. Its unchanged label is Dimmer ON. Rule `284` has Start/Stop enabled and condition/action flags `0` in both profiles.

The rule's ordered fields are `#1`, `ID_DOVE`, literal `1` or `4`, and `[101-200]*`, followed by empty fields. The changed field therefore occupies a dimension-shaped position after WHO/WHERE in a trigger pattern. It is not an ordinary WHO `1` WHAT command being renamed, an executed accepted frame or a global replacement of dimension `1` with `4`.

The reviewed [actual generator](scenario-suite-generator.md) selects compile rules by object/command/area, materializes all ten fields and appends selected nonempty content. Under compatible profile/provider premises, choosing this rule changes a literal field of the constructed pattern. No concrete WHERE or configured scenario is invented.

All `67` status-rule rows are unchanged. Object `43`'s three status rows still request dimension `1` in both sources. Thus the trigger-pattern difference does not establish a profile-wide status-request change or explain a physical dimmer observation.

## Presence family and order

Presence `69` moves from family `13` Lighting/order `2` to family `15` Sensors/order `1`; the other five sensor objects shift their stored order by one. Family definitions themselves remain unchanged, with Lighting's `ATTIVA=0` and Sensors' `ATTIVA=1`.

This is a concrete membership/order distinction relevant to a potential family-based editor consumer. It does not prove a displayed/hidden UI change, enabled hardware feature or actual sensor behavior. Per-object permissions, family activation and runtime binding remain separate questions.

## Corroboration and limits

WHO `17` Counter/Boolean declarations, text-field metadata, address domains, status rules, permissions and associations are logically identical between these two exact sources. The [text-field consumer reference](scenario-suite-generator.md#counter-text-field-namespace) remains applicable to its reviewed source path; temperature/time range-row equality is not revived as a Counter relationship.

The [independent source review](../project/review/installer-databases-3.5.38/scenario-variants-source-review.txt) checks complete schema/key/row comparison and the contextual joins. Exact historical comparison drafts and refinements remain in the supporting record; the canonical version change is a composite-key removal/addition, not a nonkey-cell update.

The source differences are established implementation data. Active editor selection, successful compilation/export/deployment, accepted trigger grammar, runtime compatibility and physical outcomes remain unresolved. Existing MH202-specific findings keep their exact source scope rather than being generalized to every identically named database.
