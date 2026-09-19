# Phase 3 Source-Coverage Audit

This audit continues the [Review Ledger and Phase 1 Coverage Matrix](ecv-esg-review-ledger.md). It applies canonical ECV 5, 6, 7, and 8 without replacing them. Phase 3 began at `1340ee7e0979ae8d47c3cda7721083b80822b48f` on `general-once-over`, on 19 September 2026. The fixed project baseline remains unchanged.

The result is a source-coverage assessment, not a claim-by-claim correctness certificate. No major area has exhausted all reasonably relevant evidence families. Stored implementation coverage is substantial; independent runtime triangulation is limited. Two previously inaccessible PDFs were recovered, and direct source inspection corrected two inaccurate implementation-source attributions and one incomplete coverage description.

## Evidence states

States apply to a specific source and question, not to an entire file forever. A source can support one claim and leave another unexamined.

| Code | State | Meaning |
| --- | --- | --- |
| A | Absent from available corpus | No artifact of the specified kind is stored or available in this audit; no assertion that it does not exist elsewhere |
| I | Exists but inaccessible | Existence is recorded, but original contents cannot be inspected in this audit |
| U | Exists but unexamined | Available contents or relevant portions have not been examined for the stated question |
| N | Examined; no relevant evidence | A bounded inspection found no evidence for the stated question; never a universal absence conclusion |
| S | Supports documentation | Actual content supports the scoped source-role or coverage claim, not necessarily every semantic detail |
| Q | Contradicts or materially qualifies | Content conflicts with a claim, exposes an omitted source, or restricts its applicability |

## Inspection and reproducibility

All 25 primary artifacts now match both manifest size and SHA-256: 19 PDFs, five SQLite databases, and `OpenQuery.txt`. Both formerly remote-only PDFs were retrieved from the exact starting commit without changing their bytes. No primary source was edited.

The [Source-Coverage Probe](checks/audit_source_coverage.py) opens SQLite files read-only, verifies manifest fingerprints, checks database integrity, and reproduces the registry, sequence, timeout, address-rule, configuration-owner, translation, scenario-frame, validation-object, and query-text checks. Run from a complete checkout:

```sh
python3 project/review/checks/audit_source_coverage.py
python3 project/review/checks/check_esg.py . --show-candidates
```

The source probe requires PyYAML. Its JSON is diagnostic output, not a substitute for inspecting the cited pages or interpreting source authority. All five databases returned `integrity_check = ok`. Table surfaces were inspected across all five stores; selected substantive queries below were inspected for coverage. This is not semantic exhaustion of every row, condition, or conversion rule.

Post-edit verification: the ESG checker reports 136 human pages, 12 supporting pages, zero objective failures, and the same seven previously accepted Practical Guide duplication candidates. An independent link/fragment pass covers all 149 Markdown files, including the ledger, with no failures. All 31 ledger records retain the required fields. The checker now builds its link-target heading cache from all Markdown files, including the ledger, while retaining its existing editorial scope; this fixes a false missing-anchor report for valid finding links.

PDF text was extracted using `pdftotext -layout`. The page register below records actual inspection, not merely extraction success. `WHO_3.pdf` and `WHO_13.pdf` have garbled extracted text; their reference-table pages were rendered and inspected visually. HMAC's handshake diagram and ZigBee address/Automation pages were also visually inspected. Unlisted detailed flows and diagrams remain U for fresh semantic review. Page numbers below are one-based PDF page positions, not necessarily printed page numbers.

## Published-document inspection register

| Source | Evidence inspected | Coverage result and applicability |
| --- | --- | --- |
| `OWN_Intro_ENG.pdf` | PDF pages 3, 5, 6: transport-independent intent, common frame types, TCP sessions | S: common syntax and TCP gateway session basis. Q: TCP setup is not the definition of every OpenWebNet transport. Detailed selector-flow re-adjudication remains U. |
| `Hmac.pdf` | Full extracted text; PDF page 4 handshake diagram rendered | S: authentication-only boundary, hash-input/wire distinction, final client acknowledgement. Q: client/server identity labels and hex constants disagree on PDF page 3. Independent working-vector resolution remains absent. |
| `WHO_0.pdf` | Cover/product scope and PDF page 3 tables | S: scenario-module grammar for the named products; not arbitrary user-authored scenario-engine persistence. Detailed flows remain U. |
| `WHO_1.pdf` | Contents; PDF pages 6, 7, 9, 10 | S: Lighting command coverage. Q: `WHAT 17` is 30 seconds in the table, but section 3.1.9 says 30 minutes. Current documentation uses the table value without this qualification. Defer semantic resolution. |
| `WHO_2.pdf` | PDF pages 6, 7, 8 parameter dictionary; contents/scope | S: advanced Automation has status, position, priority, and information fields; not merely three binary commands. Detailed operation and transport applicability remain U. |
| `WHO_3.pdf` | PDF page 4 visually rendered: command, address, dimension tables | S: Load Management vocabulary. Text extraction is unreliable; detailed measurement encoding and units remain U in this audit, with existing unresolved claims retained. |
| `WHO_4.pdf` | PDF pages 5, 6, 7, 65, 66, 68, 69, 70 | S: Temperature Control vocabulary, split-control fields, and separate published `WHO 1004` fault diagnostics. Q: this is not a complete public specification of Suite Device-interview/programming sequences. Remaining detailed flows remain U. |
| `WHO_5.pdf` | PDF pages 4 and 5; contents | S: Alarm vocabulary and distinct addresses. Q: page 5 includes an auxiliary `WHO 9` address reference, so lack of a dedicated `WHO 9` PDF is not total absence of published evidence. |
| `WHO_6_L4686SDK.pdf` | All eight pages extracted and read | Q: actual product-specific grammar exists, contrary to the namespace-only coverage impression. L4686SDK 1.0.0, 11 February 2009; not universal `WHO 6`. Address labels and flow arrows need Phase 4 scrutiny. |
| `WHO_7.pdf` | Cover, PDF page 3 command table, pages 5 and 6 command flows | S: Multimedia camera/resource operations. Q: flow notes use an address range broader than the documented enumerated range; existing discrepancy remains open. |
| `WHO_13.pdf` | PDF page 4 visually rendered: dimensions and first time request | S: external-interface status includes firmware/kernel/distribution metadata, in addition to time/network fields. These are firmware-facing observables, not firmware implementation code. Other flows remain U because extraction is unreliable. |
| `WHO_15-25.pdf` | Product scope; PDF pages 5, 13, 14 | S: distinct basic/evolved CEN and CEN+ button/event vocabularies. Q: not evidence for ZigBee binding behavior by itself. Remaining flows remain U. |
| `WHO_16.pdf` | PDF pages 4 and 6; contents | S: Sound System commands, addressing, and dimensions. Detailed flow coverage and properties without detailed flows remain U. |
| `WHO_17.pdf` | PDF pages 5 and 6; contents | S: scene start/stop/enable/disable and target-dependent scene addressing. N: these inspected command/address tables do not describe editor graph persistence. |
| `WHO_18.pdf` | Product scope and PDF page 4 | S: distinct Stop & Go, central/meter, and actuator address classes. Detailed event/scaling discrepancies remain U for fresh adjudication; the existing ledger is not independent corroboration. |
| `WHO_22.pdf` | Contents; PDF pages 8 and 9 | S: Sound Diffusion command, dimension, and address surface. Existing summary/detail and frequency-unit discrepancies require remaining flows and independent evidence; not freshly resolved. |
| `WHO_24.pdf` | Contents; PDF pages 4 and 5 | S: recipient/sender address composition and Lighting Management dimensions. Q: this is a distinct management address model, not ordinary Lighting addressing. Detailed read/write contradictions remain U. |
| `WHO_25.pdf` | Product scope and PDF page 4 | S: dry-contact/IR state functions and product-specific address classes; not a complete definition of all Transversal or ZigBee operations. |
| `OpenWebNet_Zigbee.pdf` | Contents; sections 3, 4, 5, 7; selected sections 9, 10, 11, 12, 13; rendered PDF pages 9 and 38 | Q: version 4.0 describes Legrand serial-interface framing, addresses, BUSY/NACK, discovery, management, binding, and variant functional surfaces. It cannot be reduced to an address substitution. Detailed flows and database-management diagrams remain partly U. Confidential footers qualify the claimed public-source provenance. |

## Implementation evidence inspected

| Source | Direct result | Authority and limit |
| --- | --- | --- |
| `OPEN.db` | 33 system rows, 88 frame records, 251 operation/system associations; all system association counts queried. Systems `1`, `20`, `8` each have 65 operations; `2` has 46; `5` has 1; `38` has 9. Interface rows `10` and `11` have zero direct associations. | S: stored registry and implementation templates. Q: the earlier “shared” count for interface rows did not represent a direct association. No runtime inheritance is inferred. |
| `OPEN.db` workflows | 17 sequences; 147 ordered frame associations; 17 timeout definitions; all sequence compositions queried, with `DiagKO` and `ConfKO` inspected in detail. `DiagKO` includes all-slot request, indexed responses, busy error, and special parameter; `ConfKO` starts with mandatory reset-all. | S: stored ordering, repetition, mandatory/status metadata and defaults. Not live execution, Device support, durability, recovery, or transaction guarantees. |
| `OPEN.db` parameters/addresses | All 19 address rules inspected; selected parameter associations for identity, Module, address, indexed and special responses inspected. `N_CONF` is labelled Configurator number; `SYS` is labelled KeyObject system; special response `id_open=78` has no associated parameter rows. | S: names/templates/domains. N: no parameter association establishes generic `DIMENSION 310` decoding. Q: labels alone do not settle `SYS` namespace or configurator encoding. |
| `MHCatalogue.db` | 74 tables; 541 Devices, 311 firmware definitions, 1,725 placement rows, 2,883 configuration definitions, 14,346 range rows. All configuration owners split into 1,420 Object and 1,463 firmware rows, with neither both nor neither nonzero. System/item/Device counts reproduce the coverage page. | S: capability and ownership structures. Not installed state or UI-selection algorithms. Full relationship-orphan revalidation and every conditional rule remain U in Phase 3. |
| `MHCatalogue.db` translation | All three `EN_PHY_TO_ADV_TRANS` records: firmware `160`, `691`, `722`. Sample Object `400` definitions include several property symbols sharing index `2`. | S: sparse explicit conversion registry and need for context. Q: a global index lookup or universal translation table is unsupported. Product diagrams cited for physical-position interpretation are not separately preserved. |
| Both ScenarioDevices stores | All four table schemas, counts, frame distributions, selected exact action templates, and parameter type distributions inspected. Program Files: 57 literal, 95 null, 5 symbolic frames. ProgramData: 55 literal, 91 null, 5 symbolic. Literal families are `0`, `1`, `2`, `4`, `14`. | S: capability/template coverage and revision differences. N: inspected schemas have no dedicated scenario-instance/node/edge/history model. Null or symbolic rows are not evidence of unsupported capabilities. |
| ScenarioDevices action examples | Both stores label `WHO 14` lock/unlock frames; both attach `*1*17*WHERE##` to a door-lock action. Only Program Files has local-control and fan-coil action rows. | S: stored labels and exact templates. Q: target-specific UI labels are not independent proof of wire timing, Device support, or which revision is loaded. |
| `rules.db3` | Both schemas; all Object/count groups: `95` has 149 rules, `96` has 152, `184` has 107; 194 disable-linked rows. Sample comparison and linked-property expressions inspected. | S: selected thermostat validation/dependency evidence. N: no general functional `WHO` registry in these two schemas. Full evaluator behavior and enum contracts remain U or require APP evidence. |
| `OpenQuery.txt` | Entire file read; exact named address query inspected. It uses commas, not the previously alleged `&`. Incomplete-query notes and commented TODO are retained. | S: named SQL and intended selection/order. Q: previous bitwise-expression attribution is false for the manifest revision. Execution/callers remain inaccessible. |

## Updated coverage matrix by major area

This matrix advances, rather than replaces, Phase 1's canonical placement and per-namespace map. PUB, CAT, REG, SCN, VAL, SUP, RES, OBS, EXP, APP, and FW retain the ledger definitions. A support result is bounded to the inspections above. U applies to the remaining available portions, even where a sampled part supports documentation.

| Major area | Relevant available sources and inspected support | Other relevant families and exact boundary | Coverage assessment |
| --- | --- | --- | --- |
| Protocol | PUB Introduction and HMAC S; ZigBee Q; REG templates S; existing discrepancy records RES S | OBS originals I; controlled gateway/transport EXP A; APP runtime I; legacy algorithm source A; remaining PDF flows U | Common grammar and TCP authentication source basis supported. Cross-transport completeness and independently reproducible authentication are not established. |
| Functional Protocol | Dedicated PUB tables S for listed namespaces; REG full namespace map S; CAT system capabilities S; SCN exact frames S; ZigBee Q | Dedicated PDFs A for the eleven Phase 1 namespaces; OBS originals I; cross-product EXP A; remaining detailed flows U | Broad source-backed surface, uneven completeness. `WHO 6` is under-integrated, not source-absent. `WHO 9` has a narrow cross-document lead. ZigBee families require integration and scoped adjudication. |
| Device Model | CAT ownership, placement and system surfaces S; REG identity/Module labels S; RES relationship records inspected | Product configuration diagrams referenced by research I (not preserved as separate artifacts); OBS/UI originals I; systematic EXP A; remaining CAT joins/conditions U | Stored capability model is well represented. Runtime projection, physical-position corroboration and selection precedence are not independently reproducible from this corpus alone. |
| Diagnostics | REG frame/parameter/sequence/timeout evidence S; CAT identity context S; PUB Temperature Control faults S; ZigBee discovery Q | Sanitized replay corpus A; original captures I; non-Lighting/firmware/transport EXP A; detailed remaining sequences U for semantics | Strong Suite management-template coverage, not universal Device support. Published fault diagnostics and ZigBee discovery remain distinct from Suite interview mechanisms. |
| Programming | REG `ConfKO` and sequence metadata S; CAT constraints S; VAL rules S; SUP query text S; ZigBee management/boot boundary Q | APP consumer code/traces I; restore-safe acceptance/persistence/abort EXP A; original programming captures I; remaining evaluator semantics U | Implementation workflow and constraint evidence exists. No independent certification of programming effects or safe recovery across Devices. ZigBee management is not proof of SCS programming parity. |
| Scenario Engine | Both SCN stores S; REG workflow model and PUB scene control provide adjacent context; RES revision/identifier limits inspected | APP loader, event matcher and project save behavior I; persisted project/graph fixture A; runtime EXP A; all-row semantic-delta revalidation U | Capability coverage is reproducible. Neither table completeness nor scene commands establishes full runtime graph semantics. |
| MyHOME Suite Internals | All five database schemas and selected contents S; SUP entire query file S/Q; manifest installation metadata S | Installer known but not provided I; executable code, resource bundles and runtime traces I/A; consumers and caching U until acquired | Data layout and query text are supported. Algorithms, localization, loading precedence and cache/migration behavior remain unavailable. Corrected false query attribution. |
| Practical Guides | REG diagnostic/programming sequence data, CAT constraints, VAL and canonical PUB references S; guide validation source chain inspected | End-to-end sanitized test fixtures A; original observations I; execution under concrete gateway/Device versions not performed | Guides compose evidence, not an independent evidence family. SQL/workflow semantics and safe execution remain Phase 4/testing work, not certified by readable prose. |
| Reverse Engineering | RES Relationship Register, rejected interpretations, open questions and prior review inspected; CAT/REG/SCN/VAL/SUP probes reproduce selected structural bases | Original captures/UI/product diagrams I; a full reproducible experiment archive A; every historical conclusion's derivation U | Structural findings have retrievable primary support. Observation-derived findings remain secondary records; repeated prose is not independent corroboration. |
| ZigBee cross-cutting coverage | PUB version 4.0 source now accessible and partly inspected; firmware/version readout and boot handoff provide narrow FW-interface evidence | No matching live interface/Device tests A; supplier publication provenance unverified; remaining diagrams/flows U; referenced external driver/bootloader notes unexamined and outside core OpenWebNet scope | Access gap closed; documentation integration gap remains. Scope extends to interface-visible mechanisms only, not underlying ZigBee or bootloader internals. |

## Functional namespace source-family disposition

| Namespace group | PUB disposition | Implementation disposition | Remaining coverage limit |
| --- | --- | --- | --- |
| `WHO 0`, `1`, `2`, `4` | Dedicated sources S; ZigBee Q for `1`, `2`, `4` | Literal SCN frames S; REG/CAT management/capability context S where associated | Device applicability, detailed flow review, and source contradictions |
| `WHO 3`, `5`, `7`, `15`, `16`, `17`, `22`, `24` | Dedicated sources S at inspected scope | REG identity S, but no direct operation associations; SCN does not enumerate literal frames for these namespaces | Public grammar is not exhaustive runtime coverage; remaining detailed pages U |
| `WHO 6` | L4686SDK source Q: exists and provides actual grammar | REG identity S; direct operation mapping N | Product-specific reference integration and source discrepancy review |
| `WHO 13`, `18`, `25` | Dedicated sources S; ZigBee Q | REG templates/address rules S where associated; SCN not a literal source for these families | Distinguish variant-specific operations and address semantics |
| `WHO 8`, `23`, `27` | Dedicated public source A | REG identity/family and respectively 1, 65, 9 associations S; ordinary functional completeness not established | Exact functional vocabulary and runtime tests |
| `WHO 9` | Dedicated source A; narrow auxiliary-address evidence in `WHO_5.pdf` S | REG identity S; SCN auxiliary event/condition rows have no literal frames | Cross-document integration and complete functional vocabulary |
| `WHO 14` | Dedicated source A | REG identity S; two exact SCN lock/unlock templates S | Target-specific support and any additional vocabulary |
| `WHO 10`, `11`, `12`, `19`, `26` | Dedicated source A | REG identity S; direct associated operations N; literal SCN family coverage N | These bounded database negatives do not establish protocol absence |
| `WHO 99` | Dedicated source A; common session/service context in Introduction | REG identity S; direct associated operations N | Broader service vocabulary not established; full selector re-review U |

## Material qualifications deferred to Phase 4

1. Lighting `WHAT 17`: public summary and detailed heading disagree on seconds versus minutes. The ScenarioDevices door-lock label does not resolve timing. Preserve both locations; do not silently choose a repaired value.
2. ZigBee: PDF page 11 labels an Automation example UP while using `WHAT 2`; page 38 gives UP as `1` and DOWN as `2`. Page 53's reset summary gives `0` while its detailed frame uses `75`. These are source-internal conflicts, not evidence for inventing new semantics.
3. HMAC identity constants remain internally inconsistent. A source diagram confirms the final client ACK, but does not resolve the constants.
4. Existing Sound Diffusion, Lighting Management, Energy Management, and Multimedia discrepancy records remain open. This coverage pass did not re-adjudicate all relevant detailed flows.
5. The ZigBee document has Confidential footers; manifest/source-set wording alone is not independent evidence of public release. Clarify acquisition and publication provenance before asserting it is unambiguously public. No redistribution-rights conclusion is made here.

## Genuine residual evidence gaps

- **Original observation provenance (I/A):** raw private captures are intentionally excluded; there is no complete sanitized replay corpus with exact Device/firmware/gateway, selectors, timing, successful/negative controls and expected outputs. Derived frame examples are not substitutes for that corpus.
- **Product-diagram provenance (I):** the research cites F420, F429 and H4652/3 physical configurator layouts, but the specific diagrams, editions and page references are not preserved as separate source artifacts. Keep the established interpretation scoped; acquire those references for independent reproduction rather than reopening the meaning without evidence.
- **Runtime/software evidence (I/A):** the installer is fingerprinted but not redistributed; executable consumers, file/query traces, resource bundles and controlled UI/save observations are unavailable here. Needed for firmware-selection precedence, Object replacement, address-rule rendering, caching/migration, localization, scenario loading/matching and persistence.
- **Hardware/transport experiment matrix (A):** no systematic cross-family, firmware, gateway, SCS/ZigBee comparison or restore-safe programming tests. Needed for optional dimensions, end/abort/error behavior, persistence, outer address choice and support generalization.
- **Specific unresolved fields:** discriminating non-Lighting `DIMENSION 32.SYS` responses; controlled configurator changes for `DIMENSION 4`/`5`; Object-specific `DIMENSION 310` captures/decoder evidence; hardware/microcontroller version correlation; catalogue-wide physical-position count equivalence; complete physical-to-advanced conversion behavior.
- **Missing dedicated references (A):** the eleven namespaces listed in Phase 1 still lack dedicated public PDFs in this corpus. Narrow cross-source evidence for `WHO 9`, `14`, and `99` must not be mistaken for a complete reference. Legacy OPEN password transformation source is also not preserved.
- **Independent contradiction resolution (A):** working HMAC vectors and applicable Device/interface observations for conflicting public tables/flows, including newly recorded Lighting and ZigBee conflicts.
- **Available but unexamined material (U):** unlisted PDF pages/diagrams, every conditional catalogue/validation rule, all semantic revision differences, and claim-level verification of every research conclusion. These are examination backlogs, not missing-source claims.
- **ZigBee provenance/integration:** public-release provenance remains unverified; the document is accessible, and its integration is now a review backlog rather than an access problem. No source establishes parity with Suite's SCS interview/programming model.
- **Firmware boundary:** published version queries and boot-mode handoff are available narrow FW-interface evidence. Firmware binaries, running-firmware traces, and implementation internals are absent. The referenced non-OpenWebNet upload/driver documents were not examined because their internals are outside the encyclopedia boundary; no new firmware access was attempted.

The false bitwise-query issue and the two-PDF access issue are no longer genuine gaps. No unobserved behavior was converted into a claim of nonexistence.
