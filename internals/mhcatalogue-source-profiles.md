# MHCatalogue Source Profiles

The `MHCatalogue.db` embedded in MyHOMEServer1 Firmware `3.87.13` is a distinct source profile from the catalogue in MyHOME Suite `3.5.38`. It retains a large unchanged subgraph, omits many Suite records and includes some records absent from Suite. It is neither a strict subset nor a replacement for the canonical Suite Device descriptions.

This is database implementation evidence. It does not establish the actual catalogue-reader policy, accepted protocol commands, installed Configuration, released Firmware availability or physical compatibility. The [catalogue resolution model](catalogue-resolution.md) and [validation layers](validation-layers.md) still require source-scoped owner relationships.

## Source identities

| Profile | Canonical artifact ID | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Embedded MyHOMEServer1 `3.87.13` | `myhomeserver1-3.87.13-mhcatalogue` |2233344| `79fcf2e2580dfe23349ead3d3e385ad8210cf44dddff3179a9c021644a7d1edb` |
| MyHOME Suite `3.5.38` | `myhome-suite-3.5.38-mhcatalogue` |2625536| `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5` |

The embedded database is at image path `home/bticino/matrix_mx/MHCatalogue.db`, identical in normal and recovery. Its [canonical archive registration](../project/review/mhcatalogue-comparison-2026-10-31/archive-registration.json) retains it separately from the installer variant. The [firmware first pass](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13.md) identifies the adjacent binary, exact catalogue literal and SQLite imports. The later [consumer continuation](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-consumers.md) traces compiled opening and selected row-reader paths. The [ownership continuation](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-factories.md) identifies that reader's15-column SQL producer, including catalogue slots and system-ID destinations; full runtime eligibility remains unresolved.

Both sources declare database format `V=3/R=0` and data version `4.4.0`. Their `export_date` literals are `20240327` and `20260520`; actual generation/deployment chronology and the separate `date` field's format remain unproved. Equal data-version labels are insufficient to select interchangeable content. Use the source artifact identity, not the label or filename alone.

## Complete structural and data comparison

All 75 table definitions match exactly. The complete schemas differ by one embedded-only nonunique index, `EN_CONF_INDEX` on `EN_CONF(id_conf,id_key_object)`: 72 indexes versus Suite's 71. The other 146 schema objects match exactly. No query-plan or performance experiment was performed.

Every complete table row multiset was compared with types, duplicates and NULL preserved. Forty-two tables are identical and 33 differ. Of those 33, thirteen are strict embedded-row subsets and twenty contain embedded-only rows. These are source-data counts, not command counts or a firmware coverage percentage.

| Catalogue records | Embedded | Suite | Identical complete rows | Embedded-only full rows | Suite-only full rows |
| --- | ---: | ---: | ---: | ---: | ---: |
| Commercial Devices |331|541|330|1|211|
| Technical items |105|210|104|1|106|
| Firmware definitions |122|311|114|8|197|
| Build rows |104|308|97|7|211|
| Objects |95|158|94|1|64|
| Configuration fields |1760|2883|1589|171|1294|
| Configuration ranges |11412|14346|11057|355|3289|
| Object/Firmware associations |470|827|416|54|411|
| Firmware/package associations |0|35|0|0|35|

A changed same-key row contributes to both one-source columns. The [complete comparison ledger](../project/review/mhcatalogue-comparison-2026-10-31/evidence/catalogue/ALL_TABLE_DIFFERENCES.json) retains all 75 tables. The [structural report](../project/review/mhcatalogue-comparison-2026-10-31/catalogue-report.txt) separates literal differences, reconstructed ownership and unchanged reference/seed data.

## Retained identities and selected additions

The exact commercial tuple `(code,id_brand,id_line)` is nonempty and unique in each source. Brand and line tables are completely identical. All 330 matching tuples have identical complete Device and associated item rows, including their IDs. This independently supports correspondence for this exact pair; it is not a general guarantee of stable catalogue IDs.

The single embedded-only commercial/item record is `533`, code `L/N/NT4672`, label `Energy control actuator`. It is distinct from `L/N/NT4672N`. Its source associates buses `1/2`, systems `1/7`, item model `103`, Firmware definition `321` and external Object `39`, labelled `Actuator Control Item Loads`. Those identifiers belong to different namespaces. No new physical Device identity, electrical rating or installed support is inferred.

All 114 shared Firmware definitions and their 104 item owners are identical. More strongly, each retained Firmware owner has identical complete child row bags for builds, Configuration modes, parameters, packages and connections. Removed associations in these five groups belong to omitted Firmware owners; added associations belong to embedded-only owners. Other Object/Configuration subgraphs still have differences.

| Embedded-only Firmware definition | Item / stored description | Version/revision | Catalogue status | Build |
| ---: | --- | --- | --- | --- |
|321|533 / Energy control actuator|`-1/-1`|Prototype|`-1`|
|798|2268 / Basic probe with wired sensor|`1.0`|RC|No build row|
|844|2273 / Adv - command advanced white|`1.4`|Prototype|`0`|
|849|2272 / Adv - command white|`1.4`|Prototype|`0`|
|850|2205 / Comando unico Living Now 2 moduli|`2.1`|Prototype|`0`|
|851|2233 / Comando-Attuatore Living Now Luci|`2.1`|Prototype|`0`|
|852|2237 / Comando-Attuatore Living Now Tapparelle|`2.1`|Prototype|`0`|
|853|2208 / Comando unico Living Now 3 moduli|`1.9`|Prototype|`0`|

These are stored status labels, not verified release maturity or compatibility. The 197 Suite-only Firmware definitions include 175 Official and 22 Deprecated records; therefore omitting only deprecated records cannot explain the selection. Firmware `798` is not simply the highest revision: the shared item also retains Official `2.0`. Missing build rows and explicit `-1` values remain distinct. The [Firmware graph report](../project/review/mhcatalogue-comparison-2026-10-31/firmware-report.txt) records every owner, build, mode and resource context.

All 50 package and 148 language-package rows remain identical even though the embedded Firmware/package link table is empty. The 23 embedded parameter rows and associations are exact retained Suite rows, belonging only to Firmware owners `23`, `110` and `122`. Reference paths are not evidence that their files are present or consumed. Package records are not automatically Firmware manifest extras `80/81/94/95.xtz`.

## Configuration IDs, equivalent fields and genuine changes

Only `EN_CONF` changes complete rows at shared declared primary keys. Its 68 shared-ID changes divide into two different effects:

| Effect | Count | Interpretation |
| --- | ---: | --- |
| Same integer ID now describes a different owner/field |48|Reused identifier; compare each source's own children and owner context |
| Same logical owner/name/index with changed metadata |20|Actual source-specific field metadata difference |
| Equivalent field moved to a different ID, with all non-ID metadata equal |114|Separate renumbering result; not included in the 68 same-ID total |

Equivalence uses an explicit unique context: external Object identity, resolved Firmware item/version/revision/slot/status/default context, field name and index. There are no duplicate contexts in this exact pair. Owner-zero sentinels are preserved. Field name, `idx` or `id_conf` alone is insufficient.

For example, Suite `EN_CONF.id_conf=5293` belongs to F454 item `1455`, version/revision `1.0`, field `AID`. Embedded `5293` belongs to load-management item `1162`, version/revision `3.0`, also `AID`. It is not evidence of changed F454 addressing. The child ranges are different source-owned records. This is why identifiers from these files must not be mixed during an import or comparison without mapping their contexts.

After resolving the 114 equivalent ID moves, projected field-only counts fall from `171/1294` to `57/1180` embedded/Suite. Remaining projected range differences fall from `355/3289` raw rows to `233/3167`. These normalizations preserve non-ID content and duplicate multiplicity; they do not erase genuine differences or establish a universal migration algorithm.

The 20 actual retained-field changes are narrow:

| Object / exact Configuration context | Source difference | Boundary |
| --- | --- | --- |
| External Object `218`, `G1..G10`, Configuration IDs `1332..1341` | `progressive` values `30..39` in Suite become `21..30` | Metadata sequence; field indices `240..249` and other complete field metadata remain unchanged |
| External Object `401`, Configuration IDs `1541..1549` | Nine `progressive` values decrease by1; four fields change type metadata from empty TEXT to integer `0` | Neither is SQL NULL; the type dictionary contains IDs `1..4`, with no invented meaning for `0` |
| External Object `130`, `PROXIMITY_ENABLE`, Configuration ID `4379` | `hidden` changes `0` to `1` | Not proof that proximity operation is disabled or unsupported |

For Object `401` field `M`, four range IDs also move. The selected label at progressive `3` changes only word order: `Blades control and bistable` versus `Bistable and blades control`. This is not four new modes. Selected numeric range metadata also remains context-specific: Object `39` has `PL` range `0..9`, whereas Object `401` has `0..15`; neither becomes a universal protocol address rule. Exact safe row keys and normalization methods are retained in the [Object/Configuration report](../project/review/mhcatalogue-comparison-2026-10-31/objects-report.txt).

## Applicability and unresolved consumers

The embedded source omits canonical F454 item `1455`, MH202 item `1902` and MyHOMEServer1's own item `2198`, while Suite contains them. It also omits several Suite product-family groups but retains broad system, bus and reference tables. This supports a differently selected catalogue profile. It does not establish the selection algorithm, a universal incompatibility list or the server's full capabilities. The published Device roles, F454 alarm interface and MH202 scheduler are not reassigned from shared catalogue vocabulary.

All retained condition rows, slot-condition links, conversion rules and `RIF_*`/`TMP_ID` data are exact source subsets or unchanged tables as recorded in the ledger. Their presence does not establish evaluated conditions or a captured installation. Inferred ownership audits remain separate from the three declared foreign keys; actual permissive types, NULL-bearing keys and unmatched reference values are retained without silently borrowing parents from the other source.

The [review capsule](../project/review/mhcatalogue-comparison-2026-10-31/README.md) preserves exact source reports, full-table fingerprints, safe context ledgers, queries, normalization rules, first candidates, correction history and independent reviews. Stored expressions/defaults were not executed or exported wholesale. The later [consumer](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-consumers.md) and [factory/owner](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-factories.md) analyses identify actual catalogue-opening requests and the selected15-column reader/SQL producer: column13 supplies slots and column14 the system ID. Full selection among Device/Firmware alternatives, fallback and missing or Prototype/RC policy remain unresolved. Database declarations and those selected source paths do not establish installed compatibility or complete runtime behavior.

## F460/F461 catalogue profile

[F460 `2.0.12` and F461 `2.0.11`](../reverse-engineering/firmware-analysis/f460-2.0.12-and-f461-2.0.11.md) contain the same embedded `MHCatalogue.db` payload: 2,633,728 bytes, SHA-256 `bd2ff4d326692c85bc4eb3f86504d615758da97dc832389fac523734574833e9`. Its provenance is the two registered Firmware packages; it is not represented as a separately registered extracted database.

| Comparison | Identical complete table row multisets | Different table row multisets |
| --- | ---: | ---: |
| F460/F461 versus MyHOMEServer1 | 52 | 23 |
| F460/F461 versus Suite | 42 | 33 |

All three profiles share the same 75 table definitions. The owner-aware ID correspondence, field equivalence and normalizations above were established for the MyHOMEServer1/Suite pair. They are not a mapping for F460/F461, and equal F460/F461 database bytes do not establish equal binary readers or installed features.

### F460 catalogue consumer

In the inspected F460 `matrix_mx` path, a callable registry entry for key `89` selects the query constructor. Three values from the same supplied owner become the constructor's `$modobj$`, `$line_modobj$` and `$brand_modobj$` substitutions; the constructor supplies `$key_object$ = 89` separately. This distinguishes the query/class key from owner fields and from Device or WHO identities.

The constructor, 15-column SQL producer and reader are connected by original dataflow. Reader column `13` supplies `EN_KEY_OBJECT.slots`; column `14` supplies `AS_OBJECT_SYSTEM.id_system`, followed by decimal conversion into the reader's own fields. These are F460 source relationships, without borrowed MyHOMEServer1 offsets. The [query/reader evidence](../project/review/firmware-analysis/f460-f461-run04-2026-11-01/README.md) and [registry/owner evidence](../project/review/firmware-analysis/f460-f461-run05-2026-11-01/README.md) retain the original locators and reviewed call-target joins.

Actual root Configuration, inclusion of key `89`, owner values, successful query execution, complete row selection, missing/null handling and fallback policy remain unresolved. The local argument mapping is therefore useful for tracing source-owned catalogue selection, but is not proof that a configured product or Firmware alternative is supported. No corresponding F461 reader is established by the shared data bytes.
