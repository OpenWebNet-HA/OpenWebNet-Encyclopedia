# MyOpenCommunity Energy and PIC History Review

This continuation starts at `084a65a202bcb79b7e953424a6c3af91a2225aa0` on `docs/myopencommunity-integration`, following the [transport review](myopencommunity-transport-history-review.md). The boundary follows the retained energy/PIC implementation lineage, not the earlier chat examples. Preserved sources, their Git histories and synced project references remain read-only.

## Bounded history coverage

The [history dispositions](myopencommunity-energy-history-dispositions.tsv) bind 6,344 changed-file edges to every relevant retained parent, including merges, with exact before/after Git blobs and content SHA-256 values. An independent reconstruction verifies the complete selected parent/path set and 12,688 endpoint tree identities. The [component dispositions](myopencommunity-energy-component-dispositions.tsv) bind 3,593 distinct normalized component variants to their actual source trees, complete-file hashes, component hashes and comparison identities. The 1,130 assertion occurrences have macro/ordinal identities and normalized expression hashes; each inherits its enclosing component's scoped disposition.

| Repository | Paths | Changed-file edges | Parent comparisons | Commits | Distinct nonempty endpoint blobs |
| --- | ---: | ---: | ---: | ---: | ---: |
| libqtdevices | 43 | 4,983 | 1,151 | 1,073 | 1,455 |
| libqtcommon | 6 | 477 | 199 | 194 | 122 |
| BtExperience | 18 | 842 | 433 | 420 | 434 |
| MyHomeSystemEmulator | 23 | 42 | 9 | 9 | 39 |

The 2,050 repository/blob identities include shared pre-extraction library history and are not independent corroboration. The path boundary includes removed and earlier locations of energy, platform and load classes/tests; removed energy views, banners and management consumers; BtExperience energy data/load/rate/model tests and Configuration fixtures; version/versio displays; and root/resource F520 plugin, serializer, status and build files.

| Review method | Component variants | Scope |
| --- | ---: | --- |
| Semantic component comparison | 2,079 | Energy/load/PIC executable functions, assertions, selected request/cache/consumer transitions and simulator handlers; nearest previously read body compared with each retained variant |
| Declaration/Configuration field comparison | 301 | Relevant selectors, constructors, mode/address/advanced mappings and build selection; unrelated header/UI/XML material is not a protocol verdict |
| Scope screen | 1,213 | Rendering, layout, unrelated platform consumers, tariff persistence and object lifecycle outside this energy/PIC boundary; no claim of complete semantic review |

There are 2,380 selected executable/field variants, with 624 component identities present at a pinned endpoint. File coverage is not whole-file semantic coverage. Unselected presentation methods remain outside the tranche; comment-only history is not claimed as exhaustively read. Normalization removes comments and blank indentation and redacts private fixture endpoints. Exact complete-blob hashes always refer to the unchanged source, not the normalized comparison.

| Disposition | File edges | Component variants |
| --- | ---: | ---: |
| Incorporated or used to qualify existing material | 363 | 71 |
| Corroborates existing scoped documentation | 993 | 372 |
| Excluded with reason | 4,988 | 3,150 |

Intermediate variants are excluded as current/deployed rules while retaining their semantic comparison and correction. Identity reuse is not independent evidence or execution of every revision/dependency combination. A pinned resource-copy method is still unbuilt unless the plugin project selects it. The boundary is a defensible stopping point for this energy/PIC lineage, not exhaustion of the repositories.

## Pinned source basis

| Repository | Preserved revision | Relevant sources |
| --- | --- | --- |
| libqtdevices | `736f41c4df17d8782f15b441c59bdf72a56f56ed` (`TS10_1_0_23`) | [Energy implementation](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/energy_device.cpp), [energy assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_energy_device.cpp), [platform assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_platform_device.cpp), [load assertions](https://github.com/OpenWebNet-HA/libqtdevices/blob/736f41c4df17d8782f15b441c59bdf72a56f56ed/test/test_loads_device.cpp) |
| libqtcommon | `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2` | Shared retained pre-extraction implementation/tests are bound by the ledgers; not a second independent implementation |
| BtExperience | `b88cdac9665d28494f19d6a5d759acf8d5f00ad9` | [Measurement consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/energydata.cpp), [product assertions](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/test/test_energy_data.cpp), [load consumer](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/BtObjects/energyload.cpp), [Configuration fixture](https://github.com/OpenWebNet-HA/BtExperience/blob/b88cdac9665d28494f19d6a5d759acf8d5f00ad9/conf/energymanagement/archive.xml) |
| MyHomeSystemEmulator | `4f93f44ee5ec7f89a3de9e040141755c847a5eda` (VDK 2.0) | [Built F520 model](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F520_DEV_PGIN/btf520_dev.cpp), [file queries](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F520_DEV_PGIN/f520xmlserializer.cpp), [plugin build selection](https://github.com/OpenWebNet-HA/MyHomeSystemEmulator/blob/4f93f44ee5ec7f89a3de9e040141755c847a5eda/bt_F520_DEV_PGIN/bt_F520_DEV_PGIN.pro) |

The component identities below are provenance references into the ledger, not new protocol identifiers.

## Request selection and capability state

`E0016` initializes graph encoding as older. Automatic mode subscribes to `PlatformDevice` and applies the first PIC value `<= 22` to request syntax. Forced-read mode leaves the platform pointer null and sets the syntax flag independently. The [library option](https://github.com/OpenWebNet-HA/libqtdevices/commit/59effd83e6bef4ea90ec2a8e87ffcffab7c402fe) and [BtExperience consumer change](https://github.com/OpenWebNet-HA/BtExperience/commit/c515b77b684721ae2dd3491036b8770f3b8e6071) establish actual product selection: pinned `parseEnergyData`, `E2263`, always passes `FORCE_REQUEST_FRAMES`. Older energy views and parser variants omit it. XML mode controls measurement selectors; family display labels do not override mode. The Gas fixture with mode `5` is therefore not evidence to remap gas wire identifiers.

The six exact graph request pairs already documented are retained. The targeted execution checks all twelve emitted forms, without replacing the absent external `OpenMsg` classifier. Measurement `advanced` delegates to graph support, while load `advanced` selects consumption-meter presentation. Header descriptions associating advanced devices with more than a year's data cannot independently establish physical retention.

Historical tests inject `*#18*WHERE*777##` and assert a pending graph's newer request. The [dead-code removal](https://github.com/OpenWebNet-HA/libqtdevices/commit/ef57482d0268df7908b76488a9628d04c7277875) removes that decoder branch and injection/upgrade assertions. The pinned tests still named `receiveInvalidFrameRequest...` (`E0192..E0194`) only assert the initial older request. They do not test a received invalid frame. `777` is neither promoted to a universal invalid-operation response nor equated with `NACK`.

The [automatic-update correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/e8151e508684a69b441d5a09d867c0af28f4741f) makes a `1200` report update device graph capability as well as automatic-report handling. Exact tests establish capability/timer state; final `E0048` independently establishes pending-request resubmission in executable code. Stop/restart, polling reference counts, delayed stopping, compressor windows and request ordering are local policies. No source date or commit subject establishes the affected deployed Firmware.

## Packet decoding and cache boundaries

[Energy Dimensions](../../functional/who-18-energy-management/dimensions.md#legacy-graph-values-and-unavailable-data) now records the exact older `56`, `57` and `510` packet layouts. Daily packet `1` contributes its second payload value; packet `9` contributes two hourly bytes plus the total's high byte, and packet `10` supplies the low byte. Average packet `1` is skipped, with later bytes paired across boundaries. Monthly packet `1` contributes two bytes and subsequent packets three.

The paired sentinel correction preserves `(3,255)` and `(255,3)` while normalizing only `(255,255)`. Earlier per-byte suppression and partial-word inclusion are library corrections, not separate deployed wire generations. The pinned partial-month test supplies a truncated prefix and asserts complete pairs only. It does not exercise missing interior frames or arbitrary reorder recovery. The library's newer graph methods use `i + 1` arrival positions rather than tag keys; packet/tag `1` resets the shared graph buffer. None of this guarantees lossless or interleaving-safe transport.

BtExperience `E2290` expands a current-period graph using local time/day and reads `QMap::operator[]` for absent positions, which inserts zero. The documented qualification is therefore that displayed zero can be a cache fill. It is distinct from the library's unavailable-value normalization, a real wire zero, and the calendar-year cache's separate `-1` incomplete marker. Duplicate requests, refresh intervals, cache expiry, currency changes and consumption goals add no wire semantics.

## Dates, units and derived totals

The exact scalar assertion retains `4294967294u`, while `4294967295` is normalized to zero. Earlier signed `strtol`/integer substitutions and the [unsigned correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/f9742adeb7a55afd8469471a12c75dbeca181f90) cannot establish a smaller physical counter range or a second universal sentinel. Byte graphs multiply electricity by 100 only; scalar/new graph normalization and product kW/kWh conversion are different stages. Comments about calories/litres/dm³ remain scoped historical labels.

`E0060` reconstructs a month-only graph's year as the latest month occurrence, with the newer `514` decoder subtracting another year. A future-numbered month can consequently be placed two calendar years earlier under that decoder. This is documented as date policy, not reinterpretation of the published current-year graph. The scalar `52#Y#M` decoder uses `2000 + Y`; an early four-digit request/assertion subsequently corrected to a two-digit offset is not Firmware evidence.

The [totalizer correction](https://github.com/OpenWebNet-HA/libqtdevices/commit/fdf660ba02f4cdde6e6267e1a0a0534ea4a2b3f8) distinguishes all-time wire `51` from library rolling sums. `E2291`, `E2293` and product year assertions establish BtExperience's calendar-year completeness rule: all twelve months for a past year, January through the current month for the current year. A separate view derives the last twelve months. `E2299` ignores the library-derived year values in favor of these monthly caches. Hardcoded January 2010 UI eligibility, earlier rolling twelve-month limits and average divisors are application policies, not storage guarantees.

The earlier five-field load `71` decoder/assertion was replaced with six fields. Existing published six-field material remains canonical; no five-field Firmware boundary is claimed. The load product tests delegate control to methods with confusing forceOn/forceOff labels. Exact emitted `WHAT` values remain authoritative, not those labels. Removed `WHO 3` consumers corroborate its distinct `WHAT 2` forcing namespace.

## F520 model lineage

The plugin build selects root sources, not the older resource copies. `E3356` is the built command handler; `E3416` is a resource-copy variant. The root `512` tag `25` divides the sum of 24 hourly averages by 24; the resource copy sums them. Root scalar `52#Y#M` queries by month and ignores `Y`. Root `E3393` supplies `514` values as current minus previous-year file values. [Energy Dimensions](../../functional/who-18-energy-management/dimensions.md#f520-simulator-scope) now records these calculation limits explicitly.

The file-average query also contains a malformed closing wrapper and fallback behavior; its helper fixes February at 28 days and truncates float averages to integers. The all-time accumulator updates on hour-number change rather than a complete timestamp, and periodic reporting uses callback counts and suppresses unchanged values. These limitations reinforce the model scope, but do not justify physical integration, precision, leap-year or Firmware claims. The prior monitor-only power-read qualification and unimplemented `72`/`75` remain unchanged. Leading empty write components and simulator echo shapes cannot substitute for the absent touchscreen stack's classification grammar.

Removed version displays request PIC triples under diagnostic `WHO 1013` `DIMENSION 6`, separate from functional `WHO 13` `DIMENSION 20`. Their older mismatched namespaces/field selection and later display corrections do not resolve the latter's two trailing fields. That finding remains excluded from new reader-facing schema claims.

## Exclusions and unresolved questions

| Candidate generalization | Evidence-based disposition |
| --- | --- |
| Git dates identify deployed old/new F520 or PIC Firmware | No capture/release/device mapping; excluded |
| PIC cutoff selects graph encoding in the pinned product | Constructor forces reads; syntax and capability state are independent |
| `777` is a public NACK substitute | Transient removed branch/test fixture only; excluded |
| Advanced flag proves retention from January 2010 or beyond one year | UI eligibility/header description only; excluded |
| Prefix test proves arbitrary lost-packet recovery | Tests omit interior gaps/reordering; excluded |
| Displayed zero proves measured zero | QMap cache fill and unavailable normalization can both produce zero |
| Older five-field `71` is a supported Firmware alternative | Superseded library/assertion without physical evidence; excluded |
| Simulator `512`/`514` formulas establish physical semantics | Unbuilt/root differences and file arithmetic; model scope only |
| `WHO 1013` PIC triple resolves `WHO 13 DIMENSION 20` trailing fields | Different operation/namespace without mapping; unresolved |
| Local expiry, polling, compressor, goals, tariff and UI limits are protocol requirements | Application/library choices; excluded |

Captures or hardware are needed for precise Firmware acceptance of each request family, physical historical-series ordering and missing data, opaque legacy headers, year retention and `512` tag-25/`514` meanings. The external touchscreen stack remains needed for malformed-frame and echo classification. Other functional/HVAC and Device-description lineages remain separate work. The bounded history traversal and targeted execution do not establish repository exhaustion.

## Machine KB maintenance and validation

Three existing nonclaim coverage sections retain their status/count while linking this review as deferred atomic-extraction context. Eleven existing claim digests refresh because of prepared-document positioning; their supporting blocks, block indexes, materialized statements and claim seeds remain unchanged. No claims or section/chunk identities are added or redesigned. The corpus remains at 7,448 claims and 1,223 chunks.

| Validation | Result |
| --- | --- |
| Independent retained-parent/path reconstruction | Pass: 6,344 edges, 12,688 endpoint tree checks and 2,050 repository/blob identities |
| Source/component and ledger verification | Pass: 3,593 component tree/content/body identities, 1,130 assertion digests, comparison and endpoint references, canonical destinations and disposition counts |
| Targeted archived-helper execution | Pass: 31 comparisons using 15 original EnergyDevice methods and three helpers with Qt 5 Core; includes twelve request forms, paired bytes, unsigned values, date policy and an independent absent-QMap-entry check |
| Execution boundary | Controlled token/output seam, not the absent external OpenMsg classifier; neither the complete archived product suites nor hardware were executed |
| `build.py` and `check.py` | Pass: deterministic artifacts, manifest, schemas, references, text hygiene, privacy and cross-artifact consistency |
| Machine-KB unit/schema suites | Pass: 59 unit tests and 8 schema tests; expected negative privacy fixtures rejected |
| Artifact and canonical-source audits | Pass: 144 registered artifacts; all 25 source fingerprints verified, five database integrity checks `ok`, no source-audit failures |
| Links and examples | Pass: 24 local/anchor targets, 17 public source links; new byte-pair example and existing request matrix checked against assertions and executable serializers |
| Encyclopedia style and convention checks | No objective failures across 146 reader pages and 40 support pages; 127 pre-existing style candidates and 13 existing identifier candidates remain review-only |
| Epistemic review | Existing load-level candidate remains explicitly client-scoped; changed material preserves library/product/simulator boundaries and makes no deployed Firmware claim |
| Complete diff and KB impact | Only two canonical pages, three provenance records and six KB maintenance artifacts/inputs; 11 claim digests and three zero-claim coverage reasons change, with 7,448 claim and 1,223 chunk identities retained |

The final review compares both changed pages with their neighboring Energy/PIC pages and checks whitespace before committing. Generated outputs are reproduced by the normal build. The subsequent HVAC and Device-description work remains separate.
