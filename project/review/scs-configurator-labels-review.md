# SCS Configurator Labels Review

This scheduled continuation starts from `6deef8b471a23ba520083cb3a03b61f471c9df89` on `docs/myopencommunity-integration`. It addresses the user's request for established meanings, functions, legal position context and software/numerical counterparts of configurator labels. The existing MyOpenCommunity Lighting/Automation, HVAC, CEN, Auxiliaries and integration reviews remain source context, not a vocabulary boundary. Sources and preserved archives remain read-only.

## Discovery and bounded coverage

The complete MyHOME Suite 3.5.38 firmware-scoped `EN_CONF` candidate set is read through a read-only SQLite connection: 1,463 definitions, 131 distinct symbols and 3,985 associated range rows. All these definitions use `idx=-1`; the structural pattern is therefore especially unsafe as a literal socket test. The [catalogue dispositions](scs-configurator-catalogue-dispositions.tsv) retain definition/Firmware IDs, version components, item descriptions, names/descriptions, every nonnumeric range name, range-row counts and SHA-256 of sorted exact range records. The catalogue fingerprint is `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`.

| Disposition | Definitions | Meaning |
| --- | ---: | --- |
| Contextual vocabulary corroboration | 747 | Definition-specific field names/functions; product examples do not certify every Firmware's physical implementation or numeric range |
| Excluded as evidence of a physical position | 583 | Identity, network, software or function metadata; no socket inferred from `idx=-1` |
| Unverified position/function | 133 | Exact inventory/domain retained, but no new manufacturer-verified function/range claim in this review |

The 131-symbol inventory discovers labels beyond PUL/SLA/O/I, including toroid-direction, pulse scaling, reference-actuator, hotel, probe, keypad, dimmer and sensor fields. The named physical-like range vocabulary is compared with manufacturer plug listings, product position tables and Suite function help. Numeric rows remain exact definition domains, not universally valid plug settings. Object-scoped settings and filters supply context through the established Configuration/catalogue resolver; no whole-catalogue physical-topology or filter reachability closure is claimed here.

The [source dispositions](scs-configurator-source-dispositions.tsv) fingerprint 39 retrieved manufacturer accessory listings, sheets/help pages and the manufacturer-authored older guide at its public mirror. The sheet revisions and page locators are cited in the canonical reference and [candidate dispositions](scs-configurator-claim-dispositions.tsv). Source-host names are not used to infer Firmware dates. The Suite help's `MHS_function_0304b` path and the retained catalogue's 3.5.38 revision are separate scopes. No source binary or copied manual is committed.

Product-sheet comparisons cover F428, F411U2, F411/4, the MHKIT1116 combined actuator/control instructions, H4660M2-family advanced shutter controls, H4651M2-family special controls, 4692/4693 probe roles, F430/2, H4691/LN4691 thermostat, F520, 3522N, F422, BMSE2002 sensor, 4610 Alarm detector, F503, hotel indicator/key-card switch, Classe 100 V16B and 353000 keypad. The full relevant position/mode tables and their adjacent notes are compared. Suite lighting/Automation control and all four actuator families are read; other retrieved function pages and the hotel-system guide corroborate navigation/category scope without new wire claims.

PDF text extraction is cross-checked visually for the MHKIT1116 page-5 combined mode table and advanced shutter-control page-2 destination/arrow table. In particular, the rendered table confirms local cyclic PUL and `M1=CEN` combinations, and that the shutter sheet actually says `I=0` complete system. The web PDF screenshot route failed to resolve those pages; local Poppler rendering and visual inspection supplied the check without modifying PDFs. No PDF is authored or re-exported.

## Placement and corrections

| Canonical page | Addition or qualification |
| --- | --- |
| [SCS Configurator Labels](../../device-model/configurators.md) | New navigable reference: literal/function names, command versus actuator roles, positions, represented system families, Configuration modes, exact catalogue encodings and unresolved boundaries |
| [Device Model](../../device-model/README.md) | Navigation to the reference |
| [Configuration](../../device-model/configuration.md) | Links established definitions and separates manufacturer-confirmed PUL Room/General exclusion from simulator-specific group/status behavior |
| [Lighting dimensions](../../functional/who-1-lighting/dimensions.md) | Replaces misleading “pull-actuator” terminology with PUL and removes uncertainty about established definitions while preserving client classifier/polling scope |
| [Automation dimensions](../../functional/who-2-automation/dimensions.md) | Identifies PUL shutter-info flag as actuator mode, distinct from monostable up/down and physical plug/mode read-back |
| [Temperature Control addressing](../../functional/who-4-temperature-control/addressing.md) | Distinguishes zone, actuator number, numeric SLA socket and lettered SLA plug |
| [CEN](../../functional/who-15-cen/README.md) | CEN marking does not universally select WHO15: destination-riser and shared thermostat-load uses |
| [Auxiliaries](../../functional/who-9-auxiliaries/README.md) | Separates AUX plug, channel socket and analogue audio connector |
| [Catalogue Resolution](../../internals/catalogue-resolution.md) | Links established meanings without weakening exact definition/range resolution or normalizing irregular tokens |

Manufacturer-defined PUL momentary command behavior is stated directly. Actuator PUL is not universally a momentary local-key mode: MHKIT1116 explicitly labels local ON/OFF cyclic operation with PUL while excluding Room/General controls. OFF can select a timed shutter mode, and CEN can select a combined actuator arrangement or thermostat shared load. SLA actuator followers and averaging probe Slaves are different roles. The earlier cautious client/simulator interpretations remain valid for status/classification and deployment, but are insufficient grounds to withhold established manufacturer meanings.

The new reference contains tables rather than a source-code narrative or Practical Guide. Existing wire/address references remain canonical; no separate product page or generic scenario namespace table is invented. Neighboring Configuration, Firmware, Modules and Lighting/Automation/CEN/Temperature/Auxiliaries pages are compared before and after editing.

## Contradictions, omissions and exclusions

The older manufacturer guide's printed page 36 explicitly permits group and point PUL ON/OFF while excluding Room/General. Suite Lighting, Automation, shutter and dimmer help explicitly excludes general/group/room for Master PUL and Slave PUL. This is a source-level disagreement; it does not establish that physical versus virtual mode, manufacturing generation or Firmware accounts for it. F411U2/F4114 sheets dated 23 March 2021 mention Room/General exclusion and omit group handling in their PUL description. Omission is not promoted to a contradictory claim.

The special control's sheet describes `I=0` local line, while the advanced shutter-control sheet says complete system. Both descriptions retain product scope. Suite blade-control prose prints 15 seconds where the shutter-control sheet specifies 1.5 seconds; no universal blade threshold is added. SPE system/function selectors differ between the special wall control and F428; no global SPE-to-WHO table is derived.

The following remain excluded or unresolved:

- Deployed PUL group-command and collective-status behavior, or a physical Firmware/mode boundary explaining the source disagreement.
- Simulator group acceptance or status suppression as proof of physical behavior; missing client decoders as evidence of absent hardware support.
- Universal raw numbers, `EN_CONF.progressive` to diagnostic `C1..C12` ordering, or global empty/zero equivalence.
- Normalization of catalogue `PLU` to `PUL`, or `I/O` to `O/I`. Exact Firmware659/669 tokens are retained; the prior rule25 question remains open.
- A speculative long-form expansion of CEN. Its manufacturer-defined functions are documented; the acronym is not expanded without an explicit source.
- Legacy pulse-counter `SM`/`G` scale/unit assumptions; their definitions alone do not establish those semantics.
- Complete meanings/ranges for the 31 unverified candidate symbols: `A2/-`, `AC_C0`, `AC_C1`, `AC_CU_M`, `AC_P0`, `AC_P1`, `DL`, `LOAD`, `M1_1`, `M1_2`, `M2_1`, `M2_2`, `N1_1`, `N1_2`, `N2_1`, `N2_2`, `N_1`, `N_2`, `P1`, `P1AB`, `P1CD`, `P2`, `P2A`, `P2B`, `P2C`, `P2D`, `PL1/N1`, `PL2/N2`, `S1`, `ZA/A`, `ZB/PL`. Reused letters do not certify device-specific socket interpretation.
- Electrical resistor values, unreviewed products/revisions, all catalogue Object/filter branches, every advanced UI property or all four archived repositories. Inventory is not semantic exhaustion.

A guessed `comando_luce.html` URL returns 404; the discovered `modalita_comando_luce.html` is retrieved and used. The English index is unavailable through web fetch, so the actual Italian index supplies function-page discovery. An older Virtual Configurator PDF endpoint returns 403; that manual is not used to add a workflow or equivalence claim. These access failures do not affect the retrieved primary function sheets.

## Archived-source comparison

The prior [Lighting/Automation history review](myopencommunity-lighting-automation-history-review.md), [HVAC history review](myopencommunity-hvac-history-review.md), [CEN review](myopencommunity-cen-history-review.md) and [Auxiliaries review](myopencommunity-auxiliary-history-review.md) are reused with their stated semantic boundaries. This continuation does not recertify their complete retained-parent inventories or run the full archived application suites.

| Repository | Revision | Path | Whole-file SHA-256 |
| --- | --- | --- | --- |
| libqtdevices | 736f41c4df17d8782f15b441c59bdf72a56f56ed | pulldevice.cpp | 8ceb3565abd8ea980a341df7e9cb51f5ea1227c4bb837d43ecac87cafbd562fa |
| libqtdevices | 736f41c4df17d8782f15b441c59bdf72a56f56ed | test/test_pull_manager.cpp | a0e43ce64d481daa5b8f269ab6f3c7cfb02ef84151de397f48ff57a743969ff1 |
| BtExperience | b88cdac9665d28494f19d6a5d759acf8d5f00ad9 | BtObjects/lightobjects.cpp | 82313500b0a66c39e2812c3a3690e70edfbe708b9b49fe5f02e4901155522297 |
| MyHomeSystemEmulator | 4f93f44ee5ec7f89a3de9e040141755c847a5eda | bt_F411_DEV_PGIN/btf411dev.cpp | e7b5bbfab197d06c3db5df0d7b8c4cf02748647f904f40fda3e2466e5a326230 |

At the exact pins above, `testSimpleLight_on` asserts NOT_PULL for point OFF, general ON, point ON, and PULL for point OFF, general ON, point OFF; `testSimpleLight_off` supplies the analogous opposite-state comparison. `PullStateManager::moreFrameNeeded` requires a collective frame and later point comparison, with separate advanced-state handling. These exact assertions corroborate the retained classifier qualification and do not measure physical PUL relay mechanics.

BtExperience factory fields read parent `pul` defaults and instance overrides before selecting the library's PULL/NOT_PULL enum. This is an application capability flag, not evidence that a plug was read/programmed. Emulator `execCommand` independently guards General/Room command and status branches by PUL while leaving point/group paths available. The latter remains an executable model choice. The basic manufacturer semantics have independent published support; the archives are not used as their sole authority. Copied libqtcommon lineage remains prior review context, not independent hardware corroboration.

## Candidate claims and Machine KB

The [34 candidate dispositions](scs-configurator-claim-dispositions.tsv) record incorporated/corroborating findings and evidence-based exclusions, with canonical destinations. They are review candidates, not newly generated Machine-KB atomic assertions. Compound rows can be split during a later atomic extraction task.

The new canonical page is classified publishable and receives curated document/source/section identities, with no routine bootstrap. It adds 17 sections and 15 retrieval chunks. All 7,448 retained atomic identities/statements remain unchanged: 304 section digests are refreshed only after comparing materialized assertions and exact supporting blocks against the baseline; 12 context/evidence block indices shift together. New sections are explicitly reviewed nonclaim material with later extraction deferred. Golden count fixtures are updated for 136 canonical documents, 1,240 chunks, and the Device Model coverage totals; checks are not bypassed.

An initial build detects reuse of source ID161, already allocated to an unrelated public capture outside the canonical-source manifest. The new source is corrected to the next unallocated global source ID163 before building. Existing source identities remain intact. A subsequent lifecycle check identifies the two new organizational headings without blocks: they receive section identities and coverage entries, but no emitted chunk/reference ID. Their premature live-registry entries are removed to match the actual artifact set; the curated heading identities remain. Input JSON formatting is preserved.

## Validation

| Check | Result |
| --- | --- |
| `python3 build.py` | Pass; curated inputs generate fresh artifacts |
| `python3 check.py` | Pass; deterministic double build, manifest/schema, references, lifecycle, cross-artifact consistency, text hygiene and privacy |
| `python3 -m unittest discover -s knowledge/tests -v` | 59 tests pass |
| `python3 -m unittest discover -s knowledge/tools -p test_schema.py -v` | 8 tests pass |
| Encyclopedia style gate | 0 objective failures; 199 advisory candidates across the corpus |
| Editorial consistency/privacy gate | 0 objective failures; 13 existing instance-ID review candidates |
| Epistemic drift audit | Advisory queue reviewed for changed pages; no unsupported claim promoted |
| Artifact manifest | Pass; 144 artifacts |
| Canonical-source audit through authorized archive helper | 25 fingerprints verified; all five SQLite integrity checks `ok`; no failures |
| Changed-page links | 101 local targets/anchors and 27 distinct public links pass |
| Frame examples | New illustrative `*1*1*11##` and `*1*0*11##` checked against canonical Lighting grammar; no invented PUL wire code |
| Complete/staged diff and whitespace | Reviewed; no source/archive edits, unrelated changes, automatic claim extraction or whitespace errors |

The style advisory additions are four manufacturer PDF filenames inside human-readable links, not bare database references. Epistemic candidates in the new reference flag sentences that explicitly limit catalogue/simulator evidence; their scoped wording is retained. Repeated numerical ranges are independent product selectors, with canonical wire definitions linked rather than copied. Existing public-capture ID candidates are outside this change.

Input and generated-artifact comparisons retain all 7,448 claim IDs and statements; only the reviewed section pins and 12 exact support indexes change. Registry additions are limited to the new document, source, 15 emitted sections and 15 chunks; the two organizational heading identities are retained separately. Coverage adds only the new reference's 17 reviewed sections. The fetched shared branch matches the starting HEAD before commit.

The complete diff and staged changes are reviewed for unsupported generalizations, duplicate definitions, provenance/privacy and preservation of unrelated work. Sources and archive objects remain unchanged. No hardware tests or captures are fabricated; the remaining deployment questions require product-specific evidence.
