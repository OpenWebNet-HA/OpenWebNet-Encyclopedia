# ECV/ESG Review Ledger

This ledger records the formal review of the human-facing OpenWebNet Encyclopedia against the canonical [Encyclopedia Core Values](../encyclopedia-core-values.md) (ECV) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md) (ESG).

It is a review artifact, not canonical protocol knowledge. Phase 1 establishes the inventory, canonical-placement map, evidence-corpus register, coverage matrix, and explicit evidence gaps. It does not adjudicate protocol claims or authorize speculative protocol changes.

Phase 3 continues this record in the [Source-Coverage Audit](phase-3-source-coverage.md), including an updated major-area matrix, actual inspection register, reproducible database probes, source-state distinctions, and residual evidence gaps. Phase 1 statements below are historical unless explicitly updated; they are not current claims that the two recovered PDFs remain inaccessible.

## Review baseline and scope

| Field | Value |
| --- | --- |
| Branch | `general-once-over` |
| Fixed starting baseline | `2f5ac62d754965e3b4604c6faabf8482eed12d7d` |
| Baseline verification | The authoritative branch head and requested baseline were identical when Phase 1 began. |
| Canonical ECV | `project/encyclopedia-core-values.md` read in full at the fixed baseline |
| Canonical ESG | `project/encyclopedia-style-guide.md` read in full at the fixed baseline |
| Phase | Phase 1 - inventory and coverage mapping |
| Included documentation | Root documentation page and all Markdown under `device-model/`, `diagnostics/`, `functional/`, `guides/`, `internals/`, `programming/`, `protocol/`, `reverse-engineering/`, and `scenario-engine/` |
| Included evidence | The complete baseline `sources/` tree, `sources/manifest.yaml`, source-provenance pages, and repository-authored records that preserve earlier research or evidence limits |
| Excluded from factual adjudication | Claim-by-claim truth review, new protocol interpretations, remediation edits, interoperability testing, and application or firmware reverse engineering not already represented in the corpus |

The Phase 1 inventory contains 136 human-facing encyclopedia pages: the root page plus 135 pages across the nine subject areas. The baseline also contains three project-governance pages, seven source-provenance pages, and one asset-documentation page. These eleven supporting pages are inventoried separately because they govern or describe the encyclopedia rather than form its protocol content.

## Ledger conventions

### Status

| Status | Meaning |
| --- | --- |
| Open | Finding has been recorded and needs later work. |
| Investigating | Evidence collection or adjudication is in progress. |
| Remediation ready | Required change is established and can be implemented. |
| Fixed | Remediation has been made but not independently verified. |
| Verified | Remediation or inventory result has been checked against its acceptance criteria. |
| Accepted evidence gap | The absence or inaccessibility is explicit, bounded, and must not be converted into a protocol conclusion. |
| Superseded | A later finding replaces this record while preserving its history. |

### Severity

| Severity | Meaning |
| --- | --- |
| Blocking | Review cannot make a reliable conclusion in the affected scope. |
| Substantive | Could materially affect protocol correctness, applicability, provenance, or implementation safety. |
| Editorial | Affects clarity, consistency, navigation, or ESG compliance without presently changing protocol meaning. |
| Informational | Inventory, traceability, or process record with no present defect claim. |

### Evidence classes

| Code | Evidence class |
| --- | --- |
| PUB | Published OpenWebNet specification or official technical document |
| CAT | MyHOME Suite catalogue or capability database |
| REG | MyHOME Suite OpenWebNet registry, sequence, or address-rule database |
| SCN | MyHOME Suite ScenarioDevices database |
| VAL | MyHOME Suite validation-rule database |
| SUP | Preserved support file, query registry, or installation-layout evidence |
| OBS | Sanitized protocol capture or directly observed behavior |
| EXP | Controlled Physical Device experiment or interoperability test |
| APP | Configuration-software runtime or user-interface behavior |
| FW | Legitimately observable firmware-facing interface or firmware behavior |
| RES | Prior validated research, relationship register, rejected hypothesis, or reproducible derived analysis |
| META | Manifest, provenance, fingerprint, or review-control evidence |

Evidence classes describe what a source can support. They do not create an authority ranking that overrides disagreement, applicability, or counterevidence.

## Canonical placement and major dependencies

| Encyclopedia area | Canonical responsibility | Major dependencies | Non-canonical or compositional material |
| --- | --- | --- | --- |
| Protocol | Common frame syntax, sessions, authentication, acknowledgements, addressing primitives, `WHAT`, and `DIMENSION` mechanics | Published common specifications; functional references for namespace-specific semantics; observed gateway behavior where explicitly scoped | Functional, diagnostic, and programming pages must not redefine common syntax without cross-reference. |
| Functional Protocol | Runtime functional systems organized by `WHO`; each `WHO` directory is canonical for that namespace | Relevant public `WHO` document, `OPEN.db`, ScenarioDevices, catalogue applicability, and observed traffic | `functional/source-coverage.md`, `functional/open-db-coverage.md`, and `functional/cross-database-coverage.md` are cross-source coverage maps. |
| Device Model | Physical Device → Firmware → Module → Object → Configuration model and identifier boundaries | `MHCatalogue.db`, diagnostic identity/module data, and observed Suite presentation behavior | Guides and programming pages consume this model. |
| Diagnostics | Diagnostic-family architecture, discovery, interview, identity, Module/Object reporting, addressing, and configuration reading | `OPEN.db` management sequences, `MHCatalogue.db`, selected public diagnostic material, captures, and Device experiments | Guides compose diagnostic procedures but are not the canonical definition of individual dimensions. |
| Programming | Programming families, selection, session lifecycle, writes, validation, error handling, and verification | `OPEN.db` sequences, `MHCatalogue.db` constraints, `rules.db3`, diagnostic state, and capture-backed workflows | Practical programming guides may repeat canonical material to remain executable. |
| Scenario Engine | Scenario capability catalogue, matching, parameters, frame templates, and known execution boundary | Both ScenarioDevices revisions, functional references, catalogue context, and application behavior | User-authored graph persistence and runtime scheduling remain outside established corpus coverage. |
| MyHOME Suite Internals | Implementation-specific source layout, registry, catalogue resolution, validation, localization, and data-store responsibilities | All five databases, `OpenQuery.txt`, installation evidence, and application behavior | Must not be presented as universal OpenWebNet behavior. |
| Practical Guides | End-to-end executable workflows | Canonical Protocol, Device Model, Diagnostics, Programming, and Functional pages | Repetition is permitted where necessary for independently executable workflows. |
| Reverse Engineering | Method, evidence discipline, correlations, relationship history, rejected interpretations, and open questions | All evidence families, with claim-level applicability and reproducibility | Stable conclusions belong in their canonical subject area; research history remains here. |

The strongest documented cross-area link dependencies at the baseline are: Functional Protocol → Protocol; Diagnostics → Device Model; Programming → Diagnostics and Device Model; Guides → Diagnostics, Programming, and Device Model; Scenario Engine → Functional Protocol; and Internals → Device Model, Diagnostics, Programming, Scenario Engine, Functional Protocol, and Protocol.

## Complete human-facing page inventory

Paths below are literal inventory subjects, not navigation labels. Landing pages are the `README.md` files in their respective directories.

### Root

```text
README.md
```

### Device Model - 8 pages

```text
device-model/README.md
device-model/configuration.md
device-model/firmware.md
device-model/modules.md
device-model/objects.md
device-model/physical-devices.md
device-model/sources-and-identifiers.md
device-model/virgin-objects.md
```

### Diagnostics - 12 pages

```text
diagnostics/README.md
diagnostics/address-discovery.md
diagnostics/architecture.md
diagnostics/device-discovery.md
diagnostics/device-interview.md
diagnostics/dim1-device-identity.md
diagnostics/dim30-modules.md
diagnostics/dim32-addressing.md
diagnostics/dim35-configuration.md
diagnostics/dimension-reference.md
diagnostics/temperature-control-faults.md
diagnostics/what-reference.md
```

### Functional Protocol - 54 pages

```text
functional/README.md
functional/cross-database-coverage.md
functional/open-db-coverage.md
functional/source-coverage.md
functional/who-0-scenarios/README.md
functional/who-1-lighting/README.md
functional/who-1-lighting/addressing.md
functional/who-1-lighting/dimensions.md
functional/who-1-lighting/what.md
functional/who-2-automation/README.md
functional/who-2-automation/addressing.md
functional/who-2-automation/dimensions.md
functional/who-2-automation/what.md
functional/who-3-load-management/README.md
functional/who-4-temperature-control/README.md
functional/who-4-temperature-control/addressing.md
functional/who-4-temperature-control/dimensions.md
functional/who-4-temperature-control/what.md
functional/who-5-alarm/README.md
functional/who-5-alarm/addressing.md
functional/who-5-alarm/protocol.md
functional/who-5-alarm/what.md
functional/who-6-basic-video-door-entry/README.md
functional/who-7-multimedia-video/README.md
functional/who-8-video-door-entry-telephony/README.md
functional/who-9-auxiliaries/README.md
functional/who-10-navigation/README.md
functional/who-11-energy-distribution/README.md
functional/who-12-messages/README.md
functional/who-13-integration-gateway/README.md
functional/who-13-integration-gateway/capabilities.md
functional/who-13-integration-gateway/dimensions.md
functional/who-14-special-commands/README.md
functional/who-15-cen/README.md
functional/who-16-sound-system/README.md
functional/who-17-scenario-management/README.md
functional/who-18-energy-management/README.md
functional/who-18-energy-management/addressing.md
functional/who-18-energy-management/dimensions.md
functional/who-18-energy-management/what.md
functional/who-19-interface/README.md
functional/who-22-sound-diffusion/README.md
functional/who-23-access-control/README.md
functional/who-24-lighting-management/README.md
functional/who-24-lighting-management/addressing.md
functional/who-24-lighting-management/dimensions.md
functional/who-24-lighting-management/protocol.md
functional/who-24-lighting-management/what.md
functional/who-25-transversal/README.md
functional/who-25-transversal/cen-plus.md
functional/who-25-transversal/dry-contact-ir.md
functional/who-26-upnp-multimedia/README.md
functional/who-27-nurse-call/README.md
functional/who-99-service-identification/README.md
```

### Practical Guides - 9 pages

```text
guides/README.md
guides/discover-devices.md
guides/program-device.md
guides/read-device-configuration.md
guides/retrieve-actuator-group-memberships.md
guides/retrieve-configured-cen-buttons.md
guides/troubleshoot-diagnostics.md
guides/validate-configuration-value.md
guides/verify-programming.md
```

### MyHOME Suite Internals - 9 pages

```text
internals/README.md
internals/catalogue-resolution.md
internals/data-store-responsibilities.md
internals/implementation-boundaries.md
internals/installation-and-source-layout.md
internals/localization-and-presentation.md
internals/openwebnet-registry-and-state-machines.md
internals/scenario-capability-loading.md
internals/validation-layers.md
```

### Programming - 12 pages

```text
programming/README.md
programming/address-programming.md
programming/architecture.md
programming/configuration-programming.md
programming/device-selection.md
programming/dimension-reference.md
programming/error-handling.md
programming/object-programming.md
programming/session-lifecycle.md
programming/validation.md
programming/verification.md
programming/what-reference.md
```

### Protocol - 9 pages

```text
protocol/README.md
protocol/acknowledgements.md
protocol/addressing.md
protocol/authentication.md
protocol/dimensions.md
protocol/frame-syntax.md
protocol/sessions.md
protocol/stream-parsing.md
protocol/what.md
```

### Reverse Engineering - 11 pages

```text
reverse-engineering/README.md
reverse-engineering/capture-analysis.md
reverse-engineering/cross-database-correlation.md
reverse-engineering/database-relationship-reconstruction.md
reverse-engineering/documentation-review-2026-09-18.md
reverse-engineering/evidence-and-confidence.md
reverse-engineering/hypothesis-testing.md
reverse-engineering/methodology.md
reverse-engineering/open-questions.md
reverse-engineering/rejected-relationships.md
reverse-engineering/relationship-register.md
```

### Scenario Engine - 11 pages

```text
scenario-engine/README.md
scenario-engine/capability-coverage.md
scenario-engine/capability-resolution.md
scenario-engine/categories-and-matching.md
scenario-engine/database-model.md
scenario-engine/execution-model.md
scenario-engine/frame-templates.md
scenario-engine/functional-correlations.md
scenario-engine/open-questions.md
scenario-engine/parameters.md
scenario-engine/sources-and-identifiers.md
```

## Supporting-page inventory

### Project governance - 3 pages

```text
project/README.md
project/encyclopedia-core-values.md
project/encyclopedia-style-guide.md
```

### Source provenance - 7 pages

```text
sources/README.md
sources/myhome-suite/README.md
sources/myhome-suite/3.5.38/README.md
sources/myhome-suite/3.5.38/databases/README.md
sources/myhome-suite/3.5.38/support/README.md
sources/openwebnet-public/README.md
sources/openwebnet-public/pdf/README.md
```

### Asset documentation - 1 page

```text
assets/diagrams/README.md
```

## Source and evidence corpus inventory

The source manifest records two stored source sets. Stored source artifacts are preserved byte-for-byte and must not be edited to encode conclusions. The 23 locally materialized primary files matched the manifest SHA-256 values during this phase. Two additional PDF blobs are present in the authoritative baseline and fingerprinted in the manifest but were not locally materialized for fresh content inspection.

### Published OpenWebNet documents - 19 files

| Source | Primary scope | Phase 1 inspection state |
| --- | --- | --- |
| `Hmac.pdf` | HMAC authentication | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `OWN_Intro_ENG.pdf` | Common syntax, TCP sessions, namespace summary | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `OpenWebNet_Zigbee.pdf` | ZigBee-backed OpenWebNet variant and transport-specific behavior | Present in authoritative Git tree and manifest; not locally materialized; no fresh page-by-page inspection |
| `WHO_0.pdf` | Scenarios | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_1.pdf` | Lighting | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_2.pdf` | Automation | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_3.pdf` | Load Management | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_4.pdf` | Temperature Control, including published `WHO 1004` fault diagnostics | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_5.pdf` | Alarm | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_6_L4686SDK.pdf` | Product-specific `WHO 6` SDK surface | Present in authoritative Git tree and manifest; not locally materialized; no fresh page-by-page inspection |
| `WHO_7.pdf` | Multimedia | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_13.pdf` | Gateway management | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_15-25.pdf` | CEN and CEN+ | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_16.pdf` | Sound System | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_17.pdf` | Scenario Management | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_18.pdf` | Energy Management | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_22.pdf` | Sound Diffusion and Multimedia | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_24.pdf` | Lighting Management | Locally present; SHA-256 verified; content not re-adjudicated in this phase |
| `WHO_25.pdf` | Dry-contact and IR state functions | Locally present; SHA-256 verified; content not re-adjudicated in this phase |

No dedicated public functional specification is stored for `WHO 8`, `9`, `10`, `11`, `12`, `14`, `19`, `23`, `26`, `27`, or `99`. This is a coverage statement about the current corpus, not evidence that those systems lack further protocol semantics.

### MyHOME Suite 3.5.38 implementation corpus - 6 files

| Source | Inventory surface | Phase 1 inspection state |
| --- | --- | --- |
| `MHCatalogue.db` | 74 non-internal tables; Physical Devices, items, firmware, Modules/slots, Objects, Virgin Objects, configurations, conditions, conversions, ranges, localization keys, and associations | SHA-256 verified; schema and row-count surface inventoried |
| `OPEN.db` | 23 non-internal tables; namespaces, operations, parameters, sequences, timeouts, gateways, address rules, and system associations | SHA-256 verified; schema and row-count surface inventoried |
| `ScenarioDevices-program-files.sqlite` | Four tables; 44 Objects, 157 commands, 42 parameters, and 29 Object/system rows | SHA-256 verified; schema and row-count surface inventoried |
| `ScenarioDevices-programdata.sqlite` | Four tables; 42 Objects, 151 commands, 40 parameters, and 27 Object/system rows | SHA-256 verified; schema and row-count surface inventoried |
| `rules.db3` | Two tables; 408 rules and 194 linked-parameter disable rows | SHA-256 verified; schema and row-count surface inventoried |
| `OpenQuery.txt` | Preserved named SQL query registry from the installed application | SHA-256 verified; file presence and structure inventoried |

The MyHOME Suite installer is recorded in `sources/manifest.yaml` by product version, size, SHA-256, Authenticode status, signer, and timestamp, but is intentionally not redistributed. Its binary contents were therefore not examined in this phase.

### Database table surface

The complete table-name surface was enumerated read-only. This is a structural inventory, not a claim that every table has been semantically interpreted.

| Database | Tables |
| --- | --- |
| `MHCatalogue.db` | `AS_BUS_INTERFACE`, `AS_BUS_ITEM`, `AS_BUS_SYSTEM`, `AS_CONNECTION_FIRMWARE`, `AS_DEPENDENT_DEVICES`, `AS_DEVICE_PICTURE`, `AS_FIRMWARE_CONFIG_MODE`, `AS_FIRMWARE_PARAMETERS`, `AS_FIRMWARE_VIRGIN_OBJECT`, `AS_FW_PACKAGE`, `AS_HIDDEN_KCONF`, `AS_ICON_KO`, `AS_ITEM_SYSTEM`, `AS_KO_CMD_KO_DEV`, `AS_LANGUAGE_PACKAGE`, `AS_OBJECT_COLLECTION`, `AS_OBJECT_FIRMWARE`, `AS_OBJECT_FUNCTION`, `AS_OBJECT_SYSTEM`, `AS_OBJECT_VIRGIN_OBJECT`, `AS_SET_RANGE`, `AS_SLOT_CONDITION`, `CONF_SYMBOL_REF`, `DB_INFO`, `EN_AUX_SUBTYPE`, `EN_BOX_TYPE`, `EN_BRAND`, `EN_BUILDS`, `EN_BUS`, `EN_BUS_TYPE`, `EN_CHAR_ALLOW`, `EN_COLLECTION`, `EN_COLLECTION_TYPE`, `EN_CONDITION`, `EN_CONF`, `EN_CONFIG_MODE`, `EN_CONF_DATA_TYPE`, `EN_CONF_RANGE`, `EN_CONF_TYPE`, `EN_CONNECTION`, `EN_CONV_RULE`, `EN_DEVICE`, `EN_FILE`, `EN_FILTER`, `EN_FILTER_RANGE`, `EN_FIRMWARE`, `EN_FLOOR_TYPE`, `EN_ICON`, `EN_ITEM`, `EN_KEY_OBJECT`, `EN_LABELS`, `EN_LANGUAGE`, `EN_LINE`, `EN_OBJECT_ITEM_FAMILY`, `EN_PACKAGE`, `EN_PARAMETERS`, `EN_PARAMETERS_TYPE`, `EN_PHY_TO_ADV_TRANS`, `EN_PICTURE`, `EN_ROOM_TYPE`, `EN_SLOTS`, `EN_SLOT_KO_VIRGIN`, `EN_SPECIAL_FUNCTION`, `EN_STATUS`, `EN_SW_INIT`, `EN_SYSTEM`, `EN_UNICODE_RANGE`, `EN_UNICODE_SET`, `EN_VIRGIN_OBJECT`, `MACRO_TASKS`, `RIF_ANA_GROUP`, `RIF_MH_COLLECTION_OBJECTS`, `RIF_MH_OBJECT`, `TMP_ID` |
| `OPEN.db` | `AS_GATEWAY_OPEN`, `AS_OPEN_ADDRESS_RULE`, `AS_OPEN_PARAM`, `AS_OPEN_SEQUENCE`, `AS_OPEN_SYSTEM`, `AS_SCENARIO_SEQUENCE`, `AS_SYSTEM_ADDRESS_RULE`, `AS_TIMEOUT_OPEN_SEQUENCE`, `EN_ADDRESS_RULE`, `EN_ITEM_GATEWAY`, `EN_OPEN`, `EN_OPEN_ERROR_TYPE`, `EN_OPEN_PARAM`, `EN_OPEN_TYPE`, `EN_PARAM_RANGE`, `EN_PARAM_TYPE`, `EN_PROTOCOL_TYPE`, `EN_SCENARIO`, `EN_SCENARIO_TYPE`, `EN_SEQUENCE`, `EN_STATE_VALUE`, `EN_SYSTEM`, `EN_TIMEOUT` |
| `ScenarioDevices-program-files.sqlite` | `Commands`, `DeviceObjects`, `ObjectSystems`, `Parameters` |
| `ScenarioDevices-programdata.sqlite` | `Commands`, `DeviceObjects`, `ObjectSystems`, `Parameters` |
| `rules.db3` | `DisablelinkedParameter`, `rules` |

### Other relevant evidence families

| Evidence family | Repository state | Review consequence |
| --- | --- | --- |
| Private network captures | Intentionally excluded for privacy | Capture-supported claims can be reviewed only through sanitized derived records unless a privacy-safe reproducible dataset is later supplied. Absence of raw captures is not negative protocol evidence. |
| Controlled Device experiments | No complete experiment corpus is stored | Hardware-specific or universal-behavior claims require later experimental review. |
| MyHOME Suite runtime/UI traces | Only derived observations and stored data are represented | Selection algorithms, localization, database precedence, persistence, and runtime control flow remain only partially coverable. |
| Firmware-facing interfaces | No general firmware corpus is stored | Firmware-specific behavior cannot be generalized from catalogue or wire syntax alone. |
| Prior validated research | Preserved in Reverse Engineering, source-coverage pages, relationship records, and the earlier documentation review | Usable as RES evidence only with its original applicability and source chain retained. |

## Coverage matrix

“Relevant evidence” identifies source families that should be considered in the deep review; it does not claim that every family has already been exhausted. “Current boundary” records the Phase 1 coverage limit and must not be read as proof of protocol absence.

For the post-inspection state, use the [Phase 3 Coverage Matrix](phase-3-source-coverage.md#updated-coverage-matrix-by-major-area) and [Functional Namespace Disposition](phase-3-source-coverage.md#functional-namespace-source-family-disposition). They preserve this canonical map while distinguishing absent, inaccessible, unexamined, bounded negative, supporting, and qualifying evidence.

| Major area | Canonical page set | Relevant evidence families | Current boundary or known gap |
| --- | --- | --- | --- |
| Common frame syntax and parsing | `protocol/frame-syntax.md`, `protocol/stream-parsing.md` | PUB: `OWN_Intro_ENG.pdf`; OBS; gateway APP behavior | Published TCP framing is present; transport-variant applicability, especially ZigBee-backed use, is not yet integrated. |
| Sessions and acknowledgements | `protocol/sessions.md`, `protocol/acknowledgements.md` | PUB: `OWN_Intro_ENG.pdf`, `Hmac.pdf`; REG; OBS | Gateway/version-specific pipelining and asynchronous-event behavior need scoped observations. |
| Authentication | `protocol/authentication.md` | PUB: `Hmac.pdf`, `OWN_Intro_ENG.pdf`; OBS; APP | Published identity-constant discrepancy remains unresolved and blocks a fully independent implementation recipe. |
| Common addressing, `WHAT`, and `DIMENSION` | `protocol/addressing.md`, `protocol/what.md`, `protocol/dimensions.md` | PUB common and system documents; REG address rules; SCN; OBS | Namespace-specific semantics must remain in their `WHO`; ZigBee-specific addressing applicability is not yet mapped. |
| Functional cross-source coverage | `functional/source-coverage.md`, `functional/open-db-coverage.md`, `functional/cross-database-coverage.md` | All PUB; CAT; REG; SCN; RES | Inventory exists, but deep review must verify source-role claims and non-overlap. |
| `WHO 0` Scenarios | `functional/who-0-scenarios/` | PUB: `WHO_0.pdf`; SCN; OBS | Device support and later extensions require implementation or traffic evidence. |
| `WHO 1` Lighting | `functional/who-1-lighting/` | PUB: `WHO_1.pdf`; REG; SCN; CAT; OBS/EXP | Device-specific support and ZigBee-backed differences are not established by the SCS-oriented sources alone. |
| `WHO 2` Automation | `functional/who-2-automation/` | PUB: `WHO_2.pdf`; REG; SCN; CAT; OBS/EXP | Device-specific support and ZigBee-backed differences require scoped evidence. |
| `WHO 3` Load Management | `functional/who-3-load-management/` | PUB: `WHO_3.pdf`; REG; SCN; OBS/EXP | Numeric scaling, signedness, precision, and one energy unit remain unestablished. |
| `WHO 4` Temperature Control | `functional/who-4-temperature-control/` | PUB: `WHO_4.pdf`; REG; SCN; VAL; CAT; OBS/EXP | Later-device extensions and Device applicability require implementation or observed evidence. |
| `WHO 5` Alarm | `functional/who-5-alarm/` | PUB: `WHO_5.pdf`; REG; SCN; OBS/EXP | No fresh hardware or gateway interoperability coverage in this phase. |
| `WHO 6` Basic Video Door Entry | `functional/who-6-basic-video-door-entry/` | PUB: `WHO_6_L4686SDK.pdf`; REG; SCN; OBS/EXP | Public source is product-specific and was not freshly inspected; generic `WHO 6` coverage cannot yet be established. |
| `WHO 7` Multimedia | `functional/who-7-multimedia-video/` | PUB: `WHO_7.pdf`; REG; SCN; OBS | Published address-range discrepancy remains part of the source boundary. |
| `WHO 8` Video Door Entry and Telephony | `functional/who-8-video-door-entry-telephony/` | REG; SCN; CAT; OBS/EXP | No dedicated public specification; Device-specific semantics remain incomplete. |
| `WHO 9` Auxiliaries | `functional/who-9-auxiliaries/` | REG; SCN; CAT; OBS/EXP | No dedicated public specification; complete `WHAT`/`DIMENSION` vocabulary is not established. |
| `WHO 10` Navigation | `functional/who-10-navigation/` | REG; SCN; OBS | Namespace is known; command semantics remain largely unsupported. |
| `WHO 11` Energy Distribution | `functional/who-11-energy-distribution/` | REG; SCN; OBS | No dedicated public specification and insufficient direct wire evidence. |
| `WHO 12` Messages | `functional/who-12-messages/` | REG; SCN; OBS | Payload encoding, recipients, text representation, notification type, and acknowledgement behavior remain unknown. |
| `WHO 13` Integration/Gateway | `functional/who-13-integration-gateway/` | PUB: `WHO_13.pdf`; REG; SUP; OBS/APP | Later gateway models and implementation-interface extensions require scoped evidence. |
| `WHO 14` Special Commands | `functional/who-14-special-commands/` | SCN; REG; OBS | No dedicated public specification; current wire evidence is implementation-derived. |
| `WHO 15` CEN | `functional/who-15-cen/` | PUB: `WHO_15-25.pdf`; REG; SCN; CAT; OBS/EXP | Device filtering and later behavior require implementation/Device evidence. |
| `WHO 16` Sound System | `functional/who-16-sound-system/` | PUB: `WHO_16.pdf`; REG; SCN; OBS | Some globally listed properties lack detailed published flows. |
| `WHO 17` Scenario Management | `functional/who-17-scenario-management/` | PUB: `WHO_17.pdf`; SCN; REG; OBS/APP | Runtime scene persistence and execution behavior are outside the stored capability databases. |
| `WHO 18` Energy Management | `functional/who-18-energy-management/` | PUB: `WHO_18.pdf`; REG; SCN; CAT; OBS/EXP | Heterogeneous Device families must not share addressing/operation semantics without evidence. |
| `WHO 19` Interface | `functional/who-19-interface/` | REG; SCN; OBS | No dedicated public specification; complete authoritative field vocabulary is unavailable. |
| `WHO 22` Sound Diffusion | `functional/who-22-sound-diffusion/` | PUB: `WHO_22.pdf`; REG; SCN; OBS | Published summary/detail contradictions and unusual frequency units require independent evidence. |
| `WHO 23` Access Control | `functional/who-23-access-control/` | REG; CAT; OBS/EXP | No dedicated public specification; functional semantics remain incomplete. |
| `WHO 24` Lighting Management | `functional/who-24-lighting-management/` | PUB: `WHO_24.pdf`; REG; SCN; OBS/EXP | Published payload/address discrepancies require preserved qualification and testing. |
| `WHO 25` Transversal functions | `functional/who-25-transversal/` | PUB: `WHO_15-25.pdf`, `WHO_25.pdf`; REG; SCN; OBS/EXP | CEN+ and dry-contact/IR subdomains require source-specific scoping. |
| `WHO 26` UPnP Multimedia | `functional/who-26-upnp-multimedia/` | REG; SCN; OBS | No dedicated public specification; semantics cannot be copied from adjacent multimedia systems. |
| `WHO 27` Nurse Call | `functional/who-27-nurse-call/` | REG; SCN; OBS/EXP | Namespace and diagnostic association exist; functional fields remain incompletely established. |
| `WHO 99` Service Identification | `functional/who-99-service-identification/` | PUB: `OWN_Intro_ENG.pdf`; REG; OBS | Common selector flow is published; broader service semantics need direct evidence. |
| Physical Device and firmware identity | `device-model/physical-devices.md`, `device-model/firmware.md`, `device-model/sources-and-identifiers.md` | CAT; REG; diagnostics OBS; APP | Exact firmware-selection precedence and hardware/microcontroller mapping remain unknown. |
| Modules, Objects, Virgin Objects | `device-model/modules.md`, `device-model/objects.md`, `device-model/virgin-objects.md` | CAT; diagnostics OBS/EXP; APP | Complete Object-replacement rule and UI-to-slot behavior are not preserved. |
| Configuration model | `device-model/configuration.md` | CAT; VAL; REG; diagnostics OBS/EXP; APP | Physical-to-advanced translation is explicit for only a small subset; universal `N_CONF` database equivalence remains unproven. |
| Diagnostic discovery and interview | `diagnostics/device-discovery.md`, `diagnostics/device-interview.md`, `diagnostics/what-reference.md` | REG; CAT; OBS/EXP; selected PUB | Private raw captures are unavailable; generalization across diagnostic families and firmware requires later tests. |
| Diagnostic identity and Module data | `diagnostics/dim1-device-identity.md`, `diagnostics/dim30-modules.md` | REG; CAT; OBS/EXP | Applicability outside observed Devices and all namespace choices needs confirmation. |
| Diagnostic addressing | `diagnostics/address-discovery.md`, `diagnostics/dim32-addressing.md` | REG; CAT; OBS/EXP; APP | `DIMENSION 32.SYS`, rule selection/rendering, and outer `WHERE` selection remain unresolved. |
| Diagnostic configuration and other dimensions | `diagnostics/dim35-configuration.md`, `diagnostics/dimension-reference.md` | REG; CAT; VAL; OBS/EXP | `DIMENSION 4`, `5`, and `310`, plus some Object-specific values, require controlled evidence. |
| Temperature Control fault diagnostics | `diagnostics/temperature-control-faults.md` | PUB: `WHO_4.pdf`; OBS/EXP | Published model exists; Device-generation applicability has not been experimentally exhausted. |
| Programming architecture and lifecycle | `programming/architecture.md`, `programming/session-lifecycle.md`, `programming/what-reference.md` | REG; CAT; OBS/EXP; APP | Capture-backed lifecycle evidence cannot be independently replayed from the published corpus. |
| Address/Object/configuration programming | `programming/address-programming.md`, `programming/object-programming.md`, `programming/configuration-programming.md`, `programming/dimension-reference.md` | REG; CAT; VAL; OBS/EXP; APP | Standalone reset lifecycle, address selection, and some Device-specific field meanings remain unresolved. |
| Programming validation and verification | `programming/validation.md`, `programming/verification.md`, `programming/error-handling.md`, `programming/device-selection.md` | CAT; REG; VAL; SUP; OBS/EXP; APP | Runtime behavior, rollback, and Device-specific consequences require hardware/software validation. |
| Scenario capability catalogue | `scenario-engine/database-model.md`, `scenario-engine/capability-coverage.md`, `scenario-engine/sources-and-identifiers.md` | Both SCN files; CAT; REG; RES | Database precedence/synchronization and cross-source identifier semantics remain unknown. |
| Scenario resolution and execution | `scenario-engine/capability-resolution.md`, `scenario-engine/categories-and-matching.md`, `scenario-engine/frame-templates.md`, `scenario-engine/parameters.md`, `scenario-engine/execution-model.md` | SCN; functional PUB; REG; APP/OBS | Symbolic/missing frames, enum contracts, matching IDs, graph persistence, ordering, branching, retries, and scheduling lack complete evidence. |
| MyHOME Suite internals | `internals/` | CAT; REG; SCN; VAL; SUP; APP | Callers, caching, migration, localization resources, selection algorithms, and runtime control flow are not preserved in the source corpus. |
| Practical workflows | `guides/` | All canonical page families plus OBS/EXP | Workflows must be checked later for alignment with canonical claims and safe failure behavior; they do not independently establish protocol semantics. |
| Reverse-engineering method and history | `reverse-engineering/` | All evidence classes | Raw private captures are excluded; reproducibility varies with retained source chains and must be assessed claim by claim. |
| ZigBee-backed OpenWebNet | No dedicated human-facing canonical treatment at this baseline | PUB: `OpenWebNet_Zigbee.pdf`; relevant functional PUB; OBS/EXP; APP/gateway behavior | The source exists, but OpenWebNet-visible ZigBee applicability, addressing differences, Diagnostics impact, and Programming impact are not integrated into the encyclopedia. Underlying ZigBee internals remain outside project scope unless exposed through OpenWebNet. |

## Phase 2 deterministic ESG audit

Phase 2 used the reusable checker at `project/review/checks/check_esg.py` together with repository-wide `rg` searches and focused parsers. The automated scope was the 136 human-facing encyclopedia pages. The same structural, link, heading, em-dash, fence, and link-label checks also covered the eleven project-governance, source-provenance, and asset-documentation pages, excluding this ledger from self-review.

The deterministic checks covered:

- internal link targets and Markdown heading fragments;
- one-H1 and heading-level progression;
- `README.md` landing pages for every human-documentation directory containing Markdown;
- Unicode em dashes and trailing whitespace;
- the obsolete formal terms “internal slot”, “internal-slot”, and “logical slot”;
- obvious filename, directory-name, and path-only link labels, with source artifact names retained when the resource name itself is the subject;
- bare protocol and database literal candidates outside code spans;
- inclusive numeric range notation;
- Physical Device ID case/width candidates in explicit Device-ID contexts;
- fenced transcript direction syntax when a block is identified as a transcript or exchange;
- stale root-level conventions; and
- exact duplicated long paragraphs.

Final result: zero objective failures. Seven duplicate-paragraph candidates remain, all in Practical Guides where ESG 13 permits repetition needed to keep a workflow independently executable. Thirteen remaining en dashes are citation page ranges, not integer domains. Source database/support filenames used as labels are the names of the resources themselves and therefore fall within the ESG 13 path-subject exception.

## Findings

Every record carries the fields required for later phases. Evidence not inspected is stated explicitly; no missing source is treated as proof of absence.

### P1-INV-001 - Human-facing documentation inventory

- **Finding ID:** `P1-INV-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** Repository root and nine human-facing subject areas
- **Claim/issue:** Establish the complete Phase 1 human-facing page population.
- **ECV/ESG rule:** ECV 5, 6, 13, 20; ESG 9, 11, 13
- **Evidence inspected:** Authoritative baseline recursive Git tree; all Markdown paths; page H1 headings; root navigation
- **Evidence class:** META
- **Applicability:** Fixed baseline only
- **Finding:** 136 human-facing encyclopedia pages are present and enumerated above. Project governance and source-provenance pages are classified separately.
- **Required remediation:** None for inventory; later review phases must update this record if the page population changes.
- **Resolution:** Complete page-path inventory and canonical-placement map added to this ledger.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Count reconciled by directory: root 1, Device Model 8, Diagnostics 12, Functional 54, Guides 9, Internals 9, Programming 12, Protocol 9, Reverse Engineering 11, Scenario Engine 11.
- **Open evidence gap:** Page presence does not establish factual correctness, completeness, or ESG compliance.

### P1-INV-002 - Primary source corpus inventory

- **Finding ID:** `P1-INV-002`
- **Status:** Verified
- **Severity:** Informational
- **Path:** `sources/`, `sources/manifest.yaml`
- **Claim/issue:** Establish the complete stored primary source population and its provenance controls.
- **ECV/ESG rule:** ECV 5, 6, 7, 8, 18
- **Evidence inspected:** Manifest, authoritative baseline tree, locally materialized source files, SHA-256 values, database schemas and row counts
- **Evidence class:** META, PUB, CAT, REG, SCN, VAL, SUP
- **Applicability:** Source sets `openwebnet-public` and `myhome-suite-3.5.38`
- **Finding:** The baseline records 19 public PDFs and six MyHOME Suite implementation artifacts. Twenty-three locally materialized primary files match their manifest SHA-256 values; two PDF blobs are authoritative but not locally materialized.
- **Required remediation:** None for inventory. Deep review must preserve source roles and inspect the two remote-only PDFs before claiming fresh exhaustive coverage of their subject areas.
- **Resolution:** File-level source register and structural database inventory added above.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Manifest paths reconciled with the authoritative recursive Git tree; local checksums compared with manifest entries.
- **Open evidence gap:** Byte identity does not establish that every source has been semantically exhausted.

### P1-GAP-001 - Private capture corpus unavailable

- **Finding ID:** `P1-GAP-001`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `sources/README.md`, `sources/manifest.yaml`, capture-derived documentation
- **Claim/issue:** Raw network captures are intentionally excluded for privacy.
- **ECV/ESG rule:** ECV 2, 4, 6, 8, 17, 18; ESG 3, 15
- **Evidence inspected:** Source policy, manifest policy, capture-analysis methodology, prior review record
- **Evidence class:** META, RES
- **Applicability:** All claims based on observed traffic or prior Device interviews
- **Finding:** Capture-supported conclusions may be preserved with scope and provenance, but this published corpus cannot independently replay or exhaust the underlying private observations.
- **Required remediation:** Later deep review must identify capture-derived claims, verify their visible evidence status and applicability, and request only sanitized reproducible evidence where necessary.
- **Resolution:** Gap made explicit; no protocol conclusion inferred from capture absence.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Repository source policy explicitly states captures are excluded because they may contain private installation data.
- **Open evidence gap:** Sanitized raw frames, capture metadata, Device/firmware conditions, and negative/control observations are not comprehensively available.

### P1-GAP-002 - Two public PDFs not freshly inspectable

- **Finding ID:** `P1-GAP-002`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** `sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf`, `sources/openwebnet-public/pdf/WHO_6_L4686SDK.pdf`
- **Claim/issue:** Both PDFs are present and fingerprinted in the authoritative repository but are not materialized in the local review workspace.
- **ECV/ESG rule:** ECV 5, 6, 7, 8, 12, 20
- **Evidence inspected:** Manifest entries, authoritative Git tree entries, functional source-coverage page, prior review record
- **Evidence class:** META; PUB existence only
- **Applicability:** ZigBee-backed OpenWebNet and product-specific `WHO 6` coverage
- **Finding:** Their existence, size, and fingerprint are established; their contents were not freshly reviewed in Phase 1.
- **Required remediation:** Materialize and inspect both PDFs in a later evidence-review phase before certifying those subject areas.
- **Resolution:** Phase 1 inspection boundary preserved historically. Phase 3 retrieved both files from the authoritative commit, verified their fingerprints and inspected their contents at the scope recorded in `P3-COV-001`. The access gap is closed; integration and semantic review are not complete.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Baseline tree contains both blobs and manifest fingerprints; local baseline snapshot lacks both files.
- **Open evidence gap:** Page-level claims, diagrams, examples, caveats, and internal contradictions in these documents remain unexamined in this phase.

### P1-GAP-003 - ZigBee-backed OpenWebNet not integrated

- **Finding ID:** `P1-GAP-003`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** Protocol, Functional, Diagnostics, Programming, Device Model, and source-coverage sections
- **Claim/issue:** The baseline contains `OpenWebNet_Zigbee.pdf` but no canonical human-facing treatment of its OpenWebNet-visible differences.
- **ECV/ESG rule:** ECV 5, 6, 11, 12, 13, 14, 20; ESG 10, 13, 15
- **Evidence inspected:** Complete human-facing path inventory; repository-wide ZigBee term search; manifest and source coverage
- **Evidence class:** META, RES
- **Applicability:** OpenWebNet variants/transports, especially Lighting, Automation, addressing, Diagnostics, and Programming
- **Finding:** Current coverage cannot establish where SCS-specific behavior is being treated as universal or how ZigBee-backed systems affect the documented mechanisms.
- **Required remediation:** Later factual review must inspect the canonical ZigBee PDF, map only OpenWebNet-visible differences, scope SCS behavior, and leave underlying ZigBee internals outside the encyclopedia unless mediated by OpenWebNet.
- **Resolution:** Phase 3 recovered and inspected the source; Phase 4 added the source-scoped ZigBee interface treatment and qualified shared protocol claims; Phase 5 connected that boundary to the functional namespace owners. No SCS behavior was transferred by namespace equality.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** `protocol/zigbee-interface.md`, `protocol/scope-and-architecture.md`, the six linked functional owners, and the Diagnostics/Programming applicability notices were checked in Phases 4, 5, and 7. The original baseline omission is closed; detailed unintegrated source material remains an explicit gap.
- **Open evidence gap:** Diagnostic-family behavior, programming behavior, address translation, gateway mediation, and Device applicability on ZigBee-backed systems.

### P1-GAP-004 - Functional namespaces without dedicated public specifications

- **Finding ID:** `P1-GAP-004`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `functional/who-8-video-door-entry-telephony/`, `who-9-auxiliaries/`, `who-10-navigation/`, `who-11-energy-distribution/`, `who-12-messages/`, `who-14-special-commands/`, `who-19-interface/`, `who-23-access-control/`, `who-26-upnp-multimedia/`, `who-27-nurse-call/`, `who-99-service-identification/`
- **Claim/issue:** The stored public corpus has no dedicated functional specification for these namespaces.
- **ECV/ESG rule:** ECV 1, 2, 4, 5, 6, 7, 10, 20; ESG 3, 15
- **Evidence inspected:** `functional/source-coverage.md`, manifest, public PDF inventory, relevant landing pages
- **Evidence class:** PUB absence in current corpus, REG, SCN, CAT, RES
- **Applicability:** Listed functional namespaces only
- **Finding:** Namespace existence and narrow implementation evidence can be reviewed; complete public grammar cannot be claimed from the current corpus.
- **Required remediation:** Deep review must verify that each page visibly distinguishes namespace identity, implementation evidence, observations, and unknown fields.
- **Resolution:** Coverage boundary recorded; absence is not treated as nonexistence.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Public source register reconciled with the functional coverage table.
- **Open evidence gap:** Canonical public specifications, exact implementation templates, or sanitized observed traffic for unsupported fields.

### P1-GAP-005 - Diagnostics and programming rely on non-public evidence

- **Finding ID:** `P1-GAP-005`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `diagnostics/`, `programming/`, associated guides
- **Claim/issue:** Most MyHOME Suite Device interview and programming mechanisms are established from implementation data and private observations rather than a complete public protocol specification.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8, 10, 14, 17, 20; ESG 3, 15
- **Evidence inspected:** Diagnostic/programming page inventory, `OPEN.db` surface, catalogue surface, prior review, source policy
- **Evidence class:** REG, CAT, VAL, OBS-derived RES
- **Applicability:** Diagnostic families, configuration reading, and Device programming workflows
- **Finding:** Coverage exists but independent reproducibility and general applicability cannot yet be established across all Devices, firmware, gateways, diagnostic families, or transports.
- **Required remediation:** Claim-level deep review must tag evidence class/applicability, separate syntax from support and behavior, and preserve open fields.
- **Resolution:** Phases 4 through 7 separated stored sequence syntax, catalogue capability, observed workflow behavior, and target applicability throughout Diagnostics, Programming, and their Guides. The unavailable independent evidence is now accurately represented and accepted as a bounded gap.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Deterministic drift review checked all mentions of the high-risk diagnostic dimensions and repeated management frames; canonical pages and guide copies retain evidence and applicability qualifications. No complete public diagnostic/programming specification or controlled Device matrix is present.
- **Open evidence gap:** Sanitized captures, controlled Device matrices, gateway/version matrices, abort/error paths, and transport variants.

### P1-GAP-006 - Application runtime and localization evidence incomplete

- **Finding ID:** `P1-GAP-006`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `internals/`, `scenario-engine/`, `reverse-engineering/open-questions.md`
- **Claim/issue:** Stored databases and `OpenQuery.txt` do not preserve callers, selection precedence, caching/migration, localization resources, or full runtime control flow.
- **ECV/ESG rule:** ECV 1, 2, 4, 5, 6, 7, 8, 10, 16, 20; ESG 3, 15
- **Evidence inspected:** Implementation-boundary pages, open questions, support-file inventory, installer manifest record
- **Evidence class:** CAT, REG, SCN, VAL, SUP, RES
- **Applicability:** MyHOME Suite 3.5.38 implementation behavior only
- **Finding:** Database structure can establish stored capability and associations, but not the complete application algorithm or UI semantics.
- **Required remediation:** Later review must scope implementation claims and identify where APP evidence or legitimate runtime tracing is required.
- **Resolution:** Internals and Scenario Engine now consistently classify database structures as implementation capability and keep consumer, loader, localization, UI, and persistence behavior unresolved. The missing runtime layer is accepted as an explicit evidence gap.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** `internals/implementation-boundaries.md`, `internals/localization-and-presentation.md`, `scenario-engine/database-model.md`, `scenario-engine/execution-model.md`, and the canonical open-question list were sampled against the Phase 4 conclusions; no stored row is presented as proof of unavailable application behavior.
- **Open evidence gap:** Installer/application binary inspection, file-access traces, executed-query traces, localization resources, UI workflows, and persistence behavior.

### P1-GAP-007 - Scenario execution persistence and control flow unavailable

- **Finding ID:** `P1-GAP-007`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `scenario-engine/`
- **Claim/issue:** ScenarioDevices files describe capabilities but do not establish complete user-authored graph storage or runtime execution.
- **ECV/ESG rule:** ECV 1, 2, 4, 5, 6, 7, 10, 16, 20; ESG 3, 15
- **Evidence inspected:** Both ScenarioDevices schemas and row surfaces; Scenario Engine open questions; Internals coverage
- **Evidence class:** SCN, RES
- **Applicability:** MyHOME Suite 3.5.38 Scenario Engine
- **Finding:** Capability templates, categories, and parameters can be inventoried, while graph persistence, branches, ordering, event matching, scheduling, retries, and error handling remain incompletely supported.
- **Required remediation:** Later factual review must prevent capability rows from being presented as complete runtime behavior and identify the missing APP/OBS evidence.
- **Resolution:** Phase 4 separated stored capability templates and a proposed safe rendering algorithm from actual matching, graph persistence, scheduling, and runtime control flow. The Scenario Engine canonical pages retain this boundary; the missing runtime evidence is accepted as a bounded gap.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** `scenario-engine/execution-model.md`, `database-model.md`, `categories-and-matching.md`, and `frame-templates.md` visibly distinguish established stored capability, proposed processing, and unavailable runtime behavior. Neither preserved ScenarioDevices database contains an identified complete scenario-instance graph model.
- **Open evidence gap:** Runtime/editor traces, persisted user project data, and application mapping code.

### P1-GAP-008 - Hardware and firmware applicability not exhaustively testable

- **Finding ID:** `P1-GAP-008`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** Device Model, Diagnostics, Programming, Functional Protocol
- **Claim/issue:** The corpus does not contain a comprehensive controlled experiment matrix across products, firmware, gateways, and transports.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 10, 12, 16, 20; ESG 3, 15
- **Evidence inspected:** Catalogue scope, documented observations, open questions, previous review boundaries
- **Evidence class:** CAT, OBS-derived RES, EXP absence
- **Applicability:** Any claim generalized beyond a specific observed Device/firmware/gateway combination
- **Finding:** Catalogue capability and published syntax cannot substitute for runtime support or behavior.
- **Required remediation:** Later review must narrow unsupported universals and define targeted experiments for high-value uncertainties.
- **Resolution:** Evidence boundary accepted; individual overgeneralizations, if found, remain separate findings.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** No comprehensive experiment corpus is present under `sources/`.
- **Open evidence gap:** Device/firmware matrices, negative controls, transport comparisons, and restore-safe programming tests.

### P1-GAP-009 - High-priority unresolved semantic areas

- **Finding ID:** `P1-GAP-009`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `reverse-engineering/open-questions.md` and linked canonical pages
- **Claim/issue:** Known unresolved areas require targeted evidence rather than editorial completion.
- **ECV/ESG rule:** ECV 1, 2, 3, 4, 6, 8, 9, 10, 17, 20; ESG 3, 15
- **Evidence inspected:** Open Questions, Relationship Register, rejected relationships, prior review record
- **Evidence class:** RES, CAT, REG, SCN, OBS-derived RES
- **Applicability:** Individual questions as scoped in their canonical pages
- **Finding:** Highest-priority gaps include `DIMENSION 32.SYS`; `DIMENSION 4`/`5`; Object-specific `DIMENSION 310`; hardware/microcontroller version mapping; address-rule selection/rendering; firmware selection precedence; Object replacement; physical-to-advanced translation; catalogue-wide `N_CONF` equivalence; ScenarioDevices precedence; and application runtime/localization behavior.
- **Required remediation:** Carry each question into claim-level review and later evidence acquisition without reopening already established boundaries.
- **Resolution:** Each surviving question is represented as Unknown or Unresolved in `reverse-engineering/open-questions.md` and its canonical owner. Phase 4 resolved `N_CONF` meaning while retaining count-equivalence and diagram provenance limits; the evidence-sensitive `DIMENSION 32` portion is tracked separately as `P4-FAC-003`.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Phase 7 traced every listed subject to the current open-question entry and canonical page. None is presented as settled; programming pages fail closed where unresolved encoding would affect a write.
- **Open evidence gap:** The discriminating observations listed in `reverse-engineering/open-questions.md`.

### P1-ESG-001 - Deterministic ESG review not yet performed

- **Finding ID:** `P1-ESG-001`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** All 136 human-facing pages
- **Claim/issue:** Phase 1 inventoried pages and dependencies but did not perform the later deterministic or semantic ESG pass.
- **ECV/ESG rule:** ESG 1-15 and Editorial Mechanics
- **Evidence inspected:** Page paths, H1 headings, local-link dependency graph, canonical ESG
- **Evidence class:** META
- **Applicability:** Fixed baseline human-facing documentation
- **Finding:** The deterministic portion of the ESG review has been completed. Semantic evidence vocabulary, page flow, presentation choices, example classification, and entity-context questions remain for later judgment.
- **Required remediation:** None for the deterministic pass. Continue with the later semantic ESG phase using the open Phase 2 findings below.
- **Resolution:** Mechanical violations were corrected and recorded in `P2-ESG-001` through `P2-ESG-005`; ambiguous questions remain separate.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** `project/review/checks/check_esg.py` reports zero objective failures after remediation across 136 human pages and eleven supporting Markdown pages.
- **Open evidence gap:** Semantic ESG compliance remains outside the deterministic pass.

### P1-ECV-001 - Deep factual review not yet performed

- **Finding ID:** `P1-ECV-001`
- **Status:** Open
- **Severity:** Informational
- **Path:** All canonical subject pages
- **Claim/issue:** Phase 1 maps relevant evidence but does not decide whether each substantive claim satisfies the ECV.
- **ECV/ESG rule:** ECV 1-20
- **Evidence inspected:** Canonical ECV, complete page inventory, source register, current open questions and evidence limits
- **Evidence class:** META
- **Applicability:** Fixed baseline
- **Finding:** The coverage matrix is a starting map, not certification of truth, completeness, source exhaustion, or applicability.
- **Required remediation:** Perform claim-level source review in later phases, prioritizing Substantive gaps and high-risk implementation guidance.
- **Resolution:** Pending later phase.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Scope limitation is stated at the top of this ledger and in every relevant gap.
- **Open evidence gap:** Determined per claim during deep review.

### P2-INV-001 - Asset documentation added to supporting inventory

- **Finding ID:** `P2-INV-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** `assets/diagrams/README.md`
- **Claim/issue:** Phase 1's supporting-page inventory omitted the diagram-asset documentation page even though it is reader-facing repository documentation.
- **ECV/ESG rule:** ECV 13, 20; ESG 9, 11, 13
- **Evidence inspected:** Authoritative Markdown path inventory; page heading and links; installed-diagram table
- **Evidence class:** META
- **Applicability:** Supporting documentation at the Phase 2 branch state; the 136-page encyclopedia-content count is unchanged
- **Finding:** One supporting page was omitted from the Phase 1 count. The complete supporting population is three project-governance pages, seven source-provenance pages, and one asset-documentation page.
- **Required remediation:** Add the page to the supporting inventory and deterministic audit scope.
- **Resolution:** The supporting inventory and checker now include `assets/diagrams/README.md`, increasing the supporting-page total from ten to eleven.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** The checker reports 136 human pages and eleven supporting pages; the repository-wide Markdown pass also includes this page.
- **Open evidence gap:** None for page presence or mechanical coverage. Diagram content accuracy remains a later semantic/evidentiary question.

### P2-ESG-001 - Deterministic ESG checker and full mechanical pass

- **Finding ID:** `P2-ESG-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** All 136 human-facing pages; eleven supporting Markdown pages; `project/review/checks/check_esg.py`
- **Claim/issue:** Establish a repeatable mechanical ESG audit and run it across the complete Phase 1 page population.
- **ECV/ESG rule:** ECV 8, 13, 19, 20; ESG 2, 5-9, 11, 13, Editorial Mechanics
- **Evidence inspected:** Authoritative Markdown tree; internal targets and fragments; headings; directory layout; characters; code spans; fences; links; exact paragraph duplication
- **Evidence class:** META
- **Applicability:** Human-facing documentation at the Phase 2 branch state; structural checks additionally apply to governance and provenance pages
- **Finding:** The reusable checker now encodes the deterministic checks described in the Phase 2 audit section. Its final run reports 136 human pages, eleven supporting pages, zero objective failures, and seven review candidates.
- **Required remediation:** Re-run the checker after later documentation changes and investigate any new objective failure before merging.
- **Resolution:** Checker added; all objective failures found in this phase remediated.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** `python3 project/review/checks/check_esg.py . --show-candidates` exits successfully with `objective_failures=0`.
- **Open evidence gap:** The checker cannot decide semantic evidence vocabulary, applicability, page-flow quality, or whether an unlabeled frame block is intended as a transcript.

### P2-ESG-002 - Obsolete formal `slot` terminology

- **Finding ID:** `P2-ESG-002`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** 44 pages across Device Model, Diagnostics, Guides, Internals, Programming, Protocol, and Reverse Engineering
- **Claim/issue:** The baseline used “internal slot”, “internal slots”, and “internal-slot” as formal model terms despite ESG 2 requiring the numeric/indexed concept to be written as `slot`.
- **ECV/ESG rule:** ESG 2, 5
- **Evidence inspected:** Case-insensitive repository search outside code spans; all 167 matching occurrences and their surrounding lines
- **Evidence class:** META
- **Applicability:** Reader-facing formal terminology; quoted source labels such as “ko slot” remain unchanged
- **Finding:** 167 obsolete formal-term occurrences were present across 44 pages.
- **Required remediation:** Replace the obsolete phrase with `slot` or `slot` positions without changing Module/Object semantics or quoted source identifiers.
- **Resolution:** All 167 occurrences remediated mechanically. Source field names and quoted legacy labels were preserved.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** The final checker and independent `rg` search find no “internal slot”, “internal-slot”, or “logical slot” occurrence in the 136-page human-facing scope.
- **Open evidence gap:** None for these literal phrases. Broader entity-context choices such as Device versus Physical Device remain semantic.

### P2-ESG-003 - Canonical range notation

- **Finding ID:** `P2-ESG-003`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** 57 human-facing pages containing numeric or identifier ranges
- **Claim/issue:** Numeric and identifier domains used en-dash notation instead of the ESG 6 two-period form.
- **ECV/ESG rule:** ESG 5, 6
- **Evidence inspected:** Repository-wide en-dash and range-pattern searches; inline code and plain-text range candidates; citation context
- **Evidence class:** META
- **Applicability:** Protocol/data domains and identifier intervals, not bibliographic page citations
- **Finding:** The baseline contained 333 en-dash characters in the human-facing scope. Mechanical classification identified 320 range/domain occurrences requiring `..`; the remaining 13 occurrences are page-number citation ranges.
- **Required remediation:** Convert unambiguous value, identifier, percentage, temperature, selector, address, and position intervals to `..`; preserve citation page ranges.
- **Resolution:** All 320 domain/range occurrences converted. Citation page ranges remain unchanged because they are not integer domains.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Final candidate output contains no protocol/data range. Independent search finds only 13 en dashes, all in explicit page citations.
- **Open evidence gap:** None for the remediated syntax. Whether a prose sequence should be expressed as a range is a writing judgment, not a protocol-domain check.

### P2-ESG-004 - Heading, link-label, and protocol-literal mechanics

- **Finding ID:** `P2-ESG-004`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** `functional/who-24-lighting-management/dimensions.md`; `functional/who-17-scenario-management/README.md`; seven functional evidence links; six source-provenance pages
- **Claim/issue:** One page skipped from H1 to H3; one link used a destination slug as its visible label; six manifest links exposed relative paths; seven specification link labels left `WHO n` unformatted.
- **ECV/ESG rule:** ESG 5, 9, 13
- **Evidence inspected:** Heading parser; deterministic link-label candidates; bare protocol-literal candidates outside code spans
- **Evidence class:** META
- **Applicability:** Listed pages and labels only
- **Finding:** Each case had a single unambiguous mechanical correction with no protocol-semantic effect.
- **Required remediation:** Correct the heading level, use human-readable titles, and format literal `WHO` identifiers as code.
- **Resolution:** H3 changed to H2; `scenario-engine` label changed to “Scenario Engine”; path labels changed to “Source Manifest”; specification labels now code-format `WHO n`.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Final checker reports no heading failures, missing/non-human-readable path labels, or bare literal candidates in the remediated cases.
- **Open evidence gap:** None.

### P2-ESG-005 - Links, landing pages, em dashes, IDs, and transcript syntax

- **Finding ID:** `P2-ESG-005`
- **Status:** Verified
- **Severity:** Informational
- **Path:** Complete human-facing page population and supporting Markdown
- **Claim/issue:** Verify the requested mechanical classes that produced no confirmed violation.
- **ECV/ESG rule:** ESG 5, 6, 8, 9, 11, 13, Editorial Mechanics
- **Evidence inspected:** Link/fragment resolver; directory/README map; Unicode search; Physical Device ID context scan; fenced-block parser; root conventions check
- **Evidence class:** META
- **Applicability:** Phase 2 branch state
- **Finding:** No broken internal link or fragment, missing landing-page README, Unicode em dash, stale root conventions section, lowercase explicit Physical Device ID, or malformed explicitly identified transcript was found.
- **Required remediation:** None.
- **Resolution:** Verified without documentation changes.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Final checker reports zero objective failures; independent searches corroborate zero em dashes and no obsolete root conventions section.
- **Open evidence gap:** Unlabelled multi-frame reference blocks require semantic classification before transcript-direction rules can be applied to them.

### P2-ESG-006 - Repeated Practical Guide material

- **Finding ID:** `P2-ESG-006`
- **Status:** Verified
- **Severity:** Informational
- **Path:** `guides/read-device-configuration.md`, `guides/retrieve-actuator-group-memberships.md`, `guides/retrieve-configured-cen-buttons.md`
- **Claim/issue:** Exact-paragraph comparison found seven repeated blocks concerning discovery inputs, interview dimensions, timing, cleanup, and related material.
- **ECV/ESG rule:** ESG 13
- **Evidence inspected:** Exact normalized paragraphs of at least 180 characters across all human-facing pages
- **Evidence class:** META
- **Applicability:** Practical Guides only
- **Finding:** Every exact duplicate detected is confined to Practical Guides and supports independently executable workflows. ESG 13 expressly permits this form of repetition.
- **Required remediation:** None in this phase. Reconsider only if a later semantic review finds contradiction or drift between the repeated workflows.
- **Resolution:** Reviewed and retained.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** No exact long-paragraph duplication was detected outside Practical Guides.
- **Open evidence gap:** Semantic equivalence and future drift cannot be established by exact-text comparison alone.

### P2-AMB-001 - Device entity terminology requires semantic review

- **Finding ID:** `P2-AMB-001`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** Human-facing pages using “Device” or “Devices” outside literal identifiers and source quotations
- **Claim/issue:** Deterministic replacement cannot decide whether each occurrence denotes a Physical Device, product model, generic device, protocol endpoint, catalogue record, or source wording.
- **ECV/ESG rule:** ECV 15; ESG 2, 3
- **Evidence inspected:** Repository terminology searches and the canonical entity definitions
- **Evidence class:** META
- **Applicability:** Entity terminology across all subject areas
- **Finding:** The obsolete `slot` phrase was mechanically decidable, but Device/Physical Device usage is context-dependent and cannot be safely normalized in this phase.
- **Required remediation:** Review entity references during the semantic ESG/ECV pass; change only occurrences whose referent is established.
- **Resolution:** Phase 6 reviewed entity terminology semantically and retained context-appropriate uses: Physical Device for an installed hardware instance; Device for a protocol target, source term, product/device family, or context whose physical-instance identity is not established. Phase 7 found no case where a stronger abstraction could be selected without changing meaning.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Repository-wide lower-case and capitalized Device searches were reviewed against the canonical entity boundary. Literal source phrases, code variables, target-device compounds, and generic device-family wording remain distinguishable from installed Physical Device references.
- **Open evidence gap:** None for the editorial classification. Individual unresolved identity relationships remain under their substantive findings.

### P2-AMB-002 - Unlabelled multi-frame blocks require semantic classification

- **Finding ID:** `P2-AMB-002`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** Functional and protocol pages containing fenced lists of request, response, report, or write frame forms
- **Claim/issue:** A parser can enforce `Source -> Destination: frame` once a block is a transcript, but cannot decide from multiple frame-shaped lines alone whether the block is a temporal exchange or a compact reference list.
- **ECV/ESG rule:** ESG 7, 8, 14, 15
- **Evidence inspected:** All fenced blocks; explicit transcript/exchange labels; frame-line direction syntax; surrounding headings and prose
- **Evidence class:** META
- **Applicability:** Unlabelled or reference-form fenced blocks only
- **Finding:** The apparent initial candidates in Lighting, Load Management, and Sound System pages are introduced as request/response forms or property forms, not represented as observed transcripts. They were not rewritten mechanically.
- **Required remediation:** During semantic ESG review, identify any block intended as a real exchange; if so, add explicit source/destination labels and evidence status.
- **Resolution:** Phase 7 classified all eight current multi-frame candidates as compact request, response, report, write, or property-form references. None claims to reproduce an observed temporal exchange, so transcript direction labels are inapplicable.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Candidate blocks in Lighting, Load Management, and Sound System were inspected with their headings and introducing prose. Explicitly labelled transcripts/exchanges continue to pass the direction parser.
- **Open evidence gap:** None for the current blocks; newly added blocks still require the same classification.

## Phase 3 findings

The [Source-Coverage Audit](phase-3-source-coverage.md) supplies the detailed source/page register, major-area matrix and bounded residual-gap list for these records.

### P3-COV-001 - Previously inaccessible PDFs recovered

- **Finding ID:** `P3-COV-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** sources/openwebnet-public/pdf/
- **Claim/issue:** Two primary documents existed but were not locally inspectable in earlier phases.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** META, PUB
- **Applicability:** Exact manifest revisions; not later releases
- **Finding:** All 25 primary files matched size and SHA-256; all five database integrity checks passed. WHO 6 was read in full as extracted text; ZigBee was inspected selectively, including rendered address and Automation pages.
- **Required remediation:** None for access. Continue the remaining page/claim review and integration.
- **Resolution:** Closed P1-GAP-002 access gap only.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Source-Coverage Probe reports 25 verified fingerprints, no failures, and five integrity results of ok.
- **Open evidence gap:** Unexamined detailed PDF flows and diagrams remain; publication provenance is separately open.

### P3-COV-002 - Major-area source coverage assessed

- **Finding ID:** `P3-COV-002`
- **Status:** Verified
- **Severity:** Informational
- **Path:** project/review/phase-3-source-coverage.md
- **Claim/issue:** Assess relevant source families by actual content rather than artifact presence alone.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** PUB, CAT, REG, SCN, VAL, SUP, RES, META
- **Applicability:** Phase 3 starting commit and inspected source portions
- **Finding:** The audit records all nine major areas plus cross-cutting ZigBee, all 19 PDFs, all five databases and the complete query file. Supporting, qualifying, bounded-negative, absent, inaccessible and unexamined states are explicit. No major area is certified as source-exhausted.
- **Required remediation:** Use the updated matrix to prioritize Phase 4; do not promote coverage inspection into universal correctness.
- **Resolution:** Coverage/provenance audit complete at its explicitly bounded inspection depth.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Read-only schema/content queries and PDF page inspection are enumerated in the audit; reproducible probes committed.
- **Open evidence gap:** Live behavior, source portions not examined, unavailable originals and missing dedicated references remain distinct.

### P3-PROV-001 - Incorrect OpenQuery source attribution

- **Finding ID:** `P3-PROV-001`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** internals/openwebnet-registry-and-state-machines.md; internals/implementation-boundaries.md; reverse-engineering/open-questions.md
- **Claim/issue:** Documentation attributed a bitwise expression to the canonical query file.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** SUP, META
- **Applicability:** MyHOME Suite 3.5.38 OpenQuery.txt with manifest SHA-256
- **Finding:** The exact systemaddressruleDictQuery contains comma-separated address_rule_adv and level_2_rule fields. It contains no ampersand. The alleged bitwise-expression defect was not supported by this source.
- **Required remediation:** Correct the attribution and remove the false open question while retaining correction history.
- **Resolution:** Corrected all three affected pages; did not modify the evidence file or infer runtime consumers.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Whole-file read and exact query extraction; query_contains_ampersand is false in the reproducible probe.
- **Open evidence gap:** Actual callers and address-rule consumer behavior remain unobserved; the alleged expression is no longer a genuine gap.

### P3-PROV-002 - Direct association counts for Automation interfaces

- **Finding ID:** `P3-PROV-002`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** functional/open-db-coverage.md
- **Claim/issue:** The direct EN_OPEN association column said shared for interface system rows 10 and 11.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** REG
- **Applicability:** OPEN.db system rows 10 and 11 only
- **Finding:** A complete left join shows zero direct AS_OPEN_SYSTEM associations for each interface row, while system 1 has 65. Shared diagnostic-family labels do not establish runtime operation inheritance.
- **Required remediation:** Report zero direct associations, preserving diagnostic-family identity.
- **Resolution:** Corrected the two source-coverage table cells and their descriptions; no runtime semantics inferred.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Grouped query covers all 33 system rows and reproduces the zero counts.
- **Open evidence gap:** Whether runtime software inherits or selects operations through another context requires APP evidence.

### P3-COV-003 - WHO 6 product-specific coverage omitted

- **Finding ID:** `P3-COV-003`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** functional/who-6-basic-video-door-entry/README.md
- **Claim/issue:** The page presented namespace-only coverage despite an available product-specific specification.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** PUB
- **Applicability:** L4686SDK version 1.0.0 dated 11 February 2009
- **Finding:** The eight-page source contains command/address tables and send/receive flows for cameras, calls, locks and stair lighting. It does not establish universal WHO 6 support.
- **Required remediation:** Acknowledge and link the source; defer detailed grammar integration and discrepancies to Phase 4.
- **Resolution:** Corpus-status wording corrected without copying adjacent namespace semantics.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** All eight extracted pages read; source fingerprint verified.
- **Open evidence gap:** Detailed integration, inconsistent address labels/direction arrows, and wider product applicability remain open.

### P3-COV-004 - ZigBee scope materially qualifies the coverage map

- **Finding ID:** `P3-COV-004`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** Protocol, Functional, Diagnostics, Programming and Device Model; functional/source-coverage.md
- **Claim/issue:** ZigBee evidence is not limited to addressing and is not integrated into the human reference.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** PUB, FW-interface, META
- **Applicability:** Legrand serial interface described by ZigBee OpenWebNet 4.0, 22 November 2016
- **Finding:** Source sections describe serial framing, busy responses, discovery including WHO 1000 neighbor queries, management, firmware metadata, binding and variant functional surfaces. No inspected source establishes parity with Suite's SCS programming/interview model.
- **Required remediation:** Integrate only OpenWebNet-visible mechanisms in Phase 4 with exact interface applicability; keep bootloader and underlying ZigBee internals out of scope.
- **Resolution:** Phase 4 added the source-scoped ZigBee interface boundary and qualified shared protocol claims; Phase 5 linked the six functional owners and corrected the coverage statement. OpenWebNet-visible transport, acknowledgement, addressing, management, and conflict boundaries are integrated without importing underlying radio or bootloader internals.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Phase 7 confirmed the interface page and linked canonical owners retain exact interface applicability, distinguish SCS, and leave detailed unexamined flows and live behavior open.
- **Open evidence gap:** Detailed source flows/diagrams, live interface tests, variant conflicts, and publication provenance.

### P3-PROV-003 - Public-corpus classification requires a qualification

- **Finding ID:** `P3-PROV-003`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** sources/openwebnet-public/README.md; sources/openwebnet-public/pdf/README.md; sources/manifest.yaml
- **Claim/issue:** Public-source wording conflicts with Confidential markings in the supplied ZigBee document.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** META, PUB
- **Applicability:** OpenWebNet_Zigbee.pdf version 4.0 only
- **Finding:** The document has Confidential page footers. The manifest records supplied-corpus provenance, not an independently verified public-release chain. This does not by itself establish legal status or invalidate technical content.
- **Required remediation:** Obtain acquisition/publication provenance before asserting unambiguous public-release status; preserve source bytes.
- **Resolution:** Qualified the two provenance introductions, functional coverage reference, and canonical ZigBee interface page. The unavailable publication/acquisition chain is accepted as an explicit provenance gap; no legal or technical conclusion is inferred from the footer alone.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Footer confirmed in extracted text and rendered PDF pages 9 and 38; all current reader-facing introductions preserve the qualification.
- **Open evidence gap:** Publication/acquisition history and any applicable redistribution authorization are not established by this audit.

### P3-CON-001 - Published source conflicts require semantic adjudication

- **Finding ID:** `P3-CON-001`
- **Status:** Superseded
- **Severity:** Substantive
- **Path:** functional/who-1-lighting/what.md; protocol/authentication.md; OpenWebNet_Zigbee.pdf
- **Claim/issue:** Source evidence materially qualifies selected unqualified interpretations and examples.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** PUB, SCN, RES
- **Applicability:** Specific source revisions and page locations in the Phase 3 inspection register
- **Finding:** WHO 1 summary gives WHAT 17 as 30 seconds, while section 3.1.9 says 30 minutes. ZigBee page 11's UP example uses 2, while page 38 assigns UP to 1; page 53 reset table gives 0 but detailed frame uses 75. HMAC identity-constant discrepancy remains confirmed. ScenarioDevices labels do not independently settle these conflicts.
- **Required remediation:** Phase 4 must preserve conflicting locations and seek applicable independent evidence before selecting semantics; also inspect existing WHO 7, 18, 22 and 24 discrepancy records.
- **Resolution:** Phase 4 replaced this broad queue entry with `P4-FAC-002`, `P4-FAC-003`, `P4-FAC-005`, and `P4-REV-001`. Their canonical guardrails are applied and the unresolved evidence-sensitive questions remain queued individually.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Phase 7 checked every current `ASTRA-FINAL-REVIEW` record and its canonical pages; this historical umbrella record adds no separate fifth review item.
- **Open evidence gap:** Working authentication vectors and target-scoped Device/interface observations; remaining detailed public-flow inspection.

### P3-GAP-001 - Secondary research and runtime reproducibility limits

- **Finding ID:** `P3-GAP-001`
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** Device Model; Diagnostics; Programming; Scenario Engine; Internals; Guides; Reverse Engineering
- **Claim/issue:** Prior validated research is not a substitute for retrievable independent primary observations.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8; ESG 3, 15
- **Evidence inspected:** Phase 3 inspection register and reproducible source probe; source locations stated in this finding
- **Evidence class:** RES, CAT, REG, SCN, VAL, SUP, META
- **Applicability:** Stored Suite 3.5.38 artifacts and the specific documented Device/firmware observations only
- **Finding:** Selected structural counts, ownership patterns, sequence composition, scenario-frame distributions and validation Object groups reproduce from source. Private captures, UI observations and cited product configuration diagrams cannot be independently replayed here. Installer fingerprint is available but binary/runtime artifacts are not. Narrow firmware-interface specifications exist, unlike a general firmware implementation corpus.
- **Required remediation:** Acquire only privacy-safe reproducible evidence and precise product-document references; keep semantic uncertainties scoped. Do not reopen established meanings solely because original observations are not retained.
- **Resolution:** Residual gaps consolidated in Phase 3; P1-GAP-001 and P1-GAP-005 through P1-GAP-009 remain substantively open or accepted as before.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Manifest/tree absence checks, direct source probes, Relationship Register and rejected-interpretation review; no hardware experiment or software execution claimed.
- **Open evidence gap:** Sanitized captures; product diagram editions/pages; APP loaders/resources/traces; controlled Device/gateway/transport matrix; SYS/configurator/special-parameter/firmware-selection and scenario-runtime questions.

## Phase 4 factual and epistemic findings

This cost-optimized pass starts at `6b25b581d1a5c8189d9589ec89d8aa844adebb54` and continues the existing inventory and source-coverage assessment. See the [Phase 4 Audit](phase-4-factual-audit.md) for scope, retained conclusions and the final-review handoff. `ASTRA-FINAL-REVIEW` means the documented guardrail is in place but substantive adjudication needs independent evidence or disproportionate further work; it is not a verified semantic resolution.

### P4-FAC-001 - Generic grammar must admit scoped response and product variants

- **Finding ID:** `P4-FAC-001`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** protocol/frame-syntax.md; protocol/dimensions.md; protocol/acknowledgements.md; functional/who-6-basic-video-door-entry/README.md
- **Claim/issue:** Generic response text required selector/address equality; WHO 6 remained namespace-only despite an available product reference.
- **ECV/ESG rule:** ECV 2, 4, 7, 9, 10, 12, 17, 20
- **Evidence inspected:** Phase 3 WHO 1004 and WHO 22 inspection results; canonical Temperature Control Faults and Sound Diffusion pages; WHO_6_L4686SDK.pdf sections 1 and 2 and tables (all extracted pages read in Phase 4).
- **Evidence class:** PUB, RES
- **Applicability:** Published WHO 1004 collective faults, WHO 22 source-address replies, and L4686SDK 1.0.0 only.
- **Finding:** WHO 1004 request selector 20 returns 21; WHO 22 can change source address. L4686SDK Camera OFF omits WHERE, incoming broadcast call uses special 4100, and ACK means sent on SCS rather than physical success. These counterexamples invalidate universal field equality/arity or two-result assumptions.
- **Required remediation:** Qualify generic grammar; add bounded WHO 6 reference without repairing inconsistent labels/arrows.
- **Resolution:** Applied; WHO 6 distinguishes send from receive-only operations, preserves broadcast sentinel and unknown error codes.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Compared changed forms and value ranges with the cited source sections; preserved inconsistent endpoint label and direction caveats.
- **Open evidence gap:** L4686SDK error-code enumeration, exact endpoint-number mapping and ambiguous arrows require applicable product evidence.

### P4-FAC-002 - Lighting WHAT 17 duration remains contradictory

- **Finding ID:** `P4-FAC-002`
- **Status:** ASTRA-FINAL-REVIEW
- **Severity:** Substantive
- **Path:** functional/who-1-lighting/what.md; functional/cross-database-coverage.md
- **Claim/issue:** Documentation asserted 30 seconds and treated ScenarioDevices label as compatible settled meaning.
- **ECV/ESG rule:** ECV 1, 2, 3, 4, 7, 10, 16, 19
- **Evidence inspected:** P3-CON-001 / Phase 3 WHO_1.pdf page register: summary table versus section 3.1.9; both ScenarioDevices stored door-lock templates; both affected pages.
- **Evidence class:** PUB, SCN, RES
- **Applicability:** Preserved WHO_1.pdf revision and stored Suite 3.5.38 door-lock capability; no target experiment.
- **Finding:** 30 seconds versus 30 minutes is an unresolved internal source contradiction. A door-lock resource key and frame template cannot independently choose duration or establish actual emission.
- **Required remediation:** Expose both durations in the canonical command table and dependent coverage page; seek target-scoped timing evidence before selecting one.
- **Resolution:** Unsupported certainty removed. Canonical duration is Unresolved; stored capability label retained separately.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Targeted cross-page search found both previously unqualified duration claims and both are now qualified; no timing value invented.
- **Open evidence gap:** Known product/firmware/gateway experiment measuring WHAT 17 behavior with controlled timing and independent reference if available.

### P4-FAC-003 - Address namespaces and PL=0 interpretation cannot be collapsed

- **Finding ID:** `P4-FAC-003`
- **Status:** ASTRA-FINAL-REVIEW
- **Severity:** Substantive
- **Path:** protocol/addressing.md; diagnostics/dim32-addressing.md; programming/address-programming.md; programming/validation.md
- **Claim/issue:** Shared routing model implied broader WHO 2 support; diagnostic example rendered PL=0 as functional WHERE 10; programming recipe implied address-rule rendering established ADDR encoding.
- **ECV/ESG rule:** ECV 1, 2, 4, 7, 9, 10, 12, 15, 20
- **Evidence inspected:** Canonical WHO 1/WHO 2 address tables and Phase 3 PUB/REG address evidence; DIMENSION 32 example; OPEN.db SYS label and 0..65535 ADDR domain already inspected in Phase 3; current programming procedures.
- **Evidence class:** PUB, REG, RES
- **Applicability:** SCS published A/PL syntax; Suite management DIMENSION 32; specific secondary observed-layout example only.
- **Finding:** WHO 2 public source establishes local-bus point form, not all Lighting collective forms. PL=0 is outside the cited point grammar; prior rendered 10 is not a justified usable address. Functional WHERE, selection WHERE and numeric ADDR are distinct. SYS namespace and conversion cannot be inferred from equal numbers or a template.
- **Required remediation:** Restrict routing claim; preserve prior PL=0 interpretation as unresolved; require independently established SYS/ADDR encoding before writes.
- **Resolution:** Applied guardrails. No sentinel, address decoder or cross-database SYS identity selected.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Checked changed claims against existing WHO-specific address domains and Phase 3 source limits. Prior example retained as history, no longer offered as valid WHERE.
- **Open evidence gap:** Recover raw SYS/ADDR and exact Object/firmware context for PL=0 example; discriminating non-Lighting SYS responses; validated address encoder/consumer including routing and offsets.

### P4-FAC-004 - Catalogue consistency and templates are not runtime proof

- **Finding ID:** `P4-FAC-004`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** programming/validation.md; programming/configuration-programming.md; programming/session-lifecycle.md; guides/program-device.md; scenario-engine/categories-and-matching.md; scenario-engine/execution-model.md; functional/who-1-lighting/what.md; functional/cross-database-coverage.md
- **Claim/issue:** Validation claimed to prove Physical Device support; template rows were described as emission; sent close implied closed state; proposed matching logic looked like recovered behavior.
- **ECV/ESG rule:** ECV 1, 2, 4, 7, 10, 15, 16, 17
- **Evidence inspected:** Phase 3 CAT ownership/idx and SCN template/schema findings; Phase 3 REG stored sequence/timeout authority limits; current validation, transfer, matching and graph prose.
- **Evidence class:** CAT, REG, SCN, RES
- **Applicability:** Suite 3.5.38 stored artifacts; no executed consumer or Device experiment.
- **Finding:** Passing known constraints proves only consistency with inspected evidence. Candidate property union includes firmware idx=-1 fields, not unsigned INDEX writes. Hardware-version selection has no established mapping. Transmission of WHAT 2 is not confirmed closure or durability; an absent graph schema is not proof of impossible serialization.
- **Required remediation:** Separate capability, candidate selection, algorithm proposal, transmission and observed state; retain unknown consumer behavior.
- **Resolution:** Applied. Matching pseudocode explicitly proposed; graph conclusion bounded to inspected schemas; close classified Close sent; timeout before writes no longer guarantees unchanged Device.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Reviewed each revised assertion against Phase 3 authority boundaries and canonical INDEX 0..255 domain; no source bytes or wire templates changed.
- **Open evidence gap:** APP consumer/matching/serialization evidence and target-scoped acceptance, closure, persistence and recovery experiments remain unavailable.

### P4-FAC-005 - Detailed-read guides omit DIMENSION 38 effect ambiguity

- **Finding ID:** `P4-FAC-005`
- **Status:** ASTRA-FINAL-REVIEW
- **Severity:** Substantive
- **Path:** guides/program-device.md; guides/read-device-configuration.md; guides/retrieve-actuator-group-memberships.md; guides/retrieve-configured-cen-buttons.md; guides/validate-configuration-value.md; guides/verify-programming.md; guides/troubleshoot-diagnostics.md
- **Claim/issue:** Guides unconditionally send 38#0 while canonical diagnostics preserves the reset/select versus retrieval ambiguity.
- **ECV/ESG rule:** ECV 1, 2, 4, 7, 10, 14, 19, 20
- **Evidence inspected:** Phase 3 DiagKO composition and template label; diagnostics/dim35-configuration.md Reading detailed parameters; seven guide call sites and read-guide pseudocode.
- **Evidence class:** REG, RES
- **Applicability:** Suite DiagKO all-Module operation; non-destructive applicability not established across families/firmware.
- **Finding:** Membership in a retrieval sequence is not sufficient proof that reset/select has no state-changing effect. Guide repetition dropped a material canonical qualification and could turn verification into an uncharacterized operation.
- **Required remediation:** Gate every exposed guide call on established target effects; classify unavailable read-back instead of assuming safety; obtain controlled before/after evidence.
- **Resolution:** Seven call sites and executable-looking read pseudocode now preserve the boundary. Canonical ambiguity retained; no destructive interpretation asserted.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Targeted DIMENSION 38 call-site review confirms explicit gate in all seven affected guides; no operation or timeout changed.
- **Open evidence gap:** Restore-safe target experiments or applicable implementation evidence explaining reset/select effects, scope and repetition behavior.

### P4-FAC-006 - Missing physical match is not advanced-only evidence

- **Finding ID:** `P4-FAC-006`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** device-model/configuration.md; diagnostics/dim35-configuration.md; programming/validation.md
- **Claim/issue:** Absence of a matching physical field was sufficient for advanced-only or Virtual-only classification.
- **ECV/ESG rule:** ECV 1, 2, 4, 7, 15, 16
- **Evidence inspected:** Phase 3 sparse EN_PHY_TO_ADV_TRANS findings and unavailable product diagrams; existing physical-counterpart resolution text.
- **Evidence class:** CAT, RES
- **Applicability:** Resolved Object/firmware contexts with potentially incomplete physical mappings.
- **Finding:** Resolving the correct firmware does not make the physical-interface or conversion evidence exhaustive. A bounded metadata negative cannot exclude an unrepresented counterpart.
- **Required remediation:** Retain no counterpart established unless independent evidence establishes complete physical scope and excludes a counterpart.
- **Resolution:** Applied consistently in canonical model, diagnostic interpretation and programming classification.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Compared the three revised classifications; all distinguish absent metadata from excluded capability.
- **Open evidence gap:** Complete applicable physical-interface diagrams and conversion mappings where a stronger exclusion is needed.

### P4-FAC-007 - N_CONF landing page contradicted established interpretation

- **Finding ID:** `P4-FAC-007`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** device-model/README.md
- **Claim/issue:** Landing page still called N_CONF unresolved while canonical identity pages and research established physical configurator-position count.
- **ECV/ESG rule:** ECV 3, 8, 15, 19
- **Evidence inspected:** Phase 3 product-diagram provenance boundary; diagnostics/dim1-device-identity.md; device-model/physical-devices.md; reverse-engineering/open-questions.md.
- **Evidence class:** REG, RES
- **Applicability:** Established interpretation preserved from prior validated research; no fresh product-diagram reproduction claimed.
- **Finding:** The stale unknown label is a representation-consistency defect, not new evidence against the interpretation. Catalogue-wide row-count equivalence remains separately unresolved.
- **Required remediation:** Align landing page to canonical conclusion while retaining provenance and count-equivalence limits.
- **Resolution:** Applied; N_CONF not repurposed as Object, Virgin Object or firmware class.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Compared landing statement to all three canonical/research treatments; original diagram gap retained.
- **Open evidence gap:** Specific product-diagram editions/pages and catalogue-wide equivalence remain Phase 3 gaps; meaning not reopened.

### P4-FAC-008 - Historical commands are an enumeration, not a range

- **Finding ID:** `P4-FAC-008`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** functional/who-18-energy-management/what.md
- **Claim/issue:** WHAT 57..510 falsely denotes hundreds of values while adjacent source-backed table lists four commands.
- **ECV/ESG rule:** ECV 9, 20
- **Evidence inspected:** Existing canonical command table and historical-operation sections: 57, 58, 59, 510; Phase 3 WHO 18 source basis.
- **Evidence class:** PUB, RES
- **Applicability:** Published WHO_18.pdf historical-series commands only.
- **Finding:** The intended set is {57,58,59,510}; inclusive-range notation expands unsupported vocabulary.
- **Required remediation:** Write the four-value enumeration explicitly.
- **Resolution:** Applied without changing any actual command frame.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Compared prose with all four table entries and detailed subsections.
- **Open evidence gap:** No new gap for enumeration; existing operation-specific runtime and source discrepancies remain.

### P4-FAC-009 - ZigBee applicability must qualify shared protocol claims

- **Finding ID:** `P4-FAC-009`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** protocol/zigbee-interface.md; protocol/README.md; protocol/addressing.md; protocol/acknowledgements.md; diagnostics/README.md; programming/README.md; functional/who-13-integration-gateway/README.md; functional/who-18-energy-management/README.md; functional/who-25-transversal/README.md
- **Claim/issue:** TCP setup, SCS addressing and Suite management surfaces could be read as transport-wide despite Phase 3's known variant evidence.
- **ECV/ESG rule:** ECV 2, 4, 7, 9, 10, 11, 12, 14, 15, 18, 20
- **Evidence inspected:** Phase 3 ZigBee inspection register reused; Phase 4 targeted text inspection of sections 2.3, 3.1 through 3.9 and 5.3 for newly stated serial/address/BUSY/discovery boundaries.
- **Evidence class:** PUB, RES
- **Applicability:** Legrand serial interface described by ZigBee OpenWebNet 4.0 only; public-release provenance unresolved; no runtime test.
- **Finding:** Serial setup, product/unit/#9 WHERE, BUSY then NACK, WHO1000 neighbor discovery and separate management/binding invalidate address-only or TCP-universal integration. Source SYS family suffix is not DIMENSION32 SYS; product-address bytes do not establish Suite Device-ID identity.
- **Required remediation:** Add compact canonical interface boundary and scoped entry-point qualifications; defer unexamined detailed flows.
- **Resolution:** Applied using symbolic identifiers only. No MAC examples, new device observations, bootloader internals or speculative wire repairs added.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Compared each new transport/address/BUSY claim to named source subsections. Conflicts and unexamined flows explicitly preserved.
- **Open evidence gap:** Detailed variant reference integration, interface experiments, publication provenance and unexamined flows remain; this correction is not exhaustive ZigBee certification.

### P4-REV-001 - Independent adjudication of source contradictions

- **Finding ID:** `P4-REV-001`
- **Status:** ASTRA-FINAL-REVIEW
- **Severity:** Substantive
- **Path:** protocol/authentication.md; protocol/zigbee-interface.md; functional/who-7-multimedia-video/README.md; functional/who-18-energy-management/what.md; functional/who-22-sound-diffusion/README.md; functional/who-24-lighting-management/dimensions.md
- **Claim/issue:** Conflicting public literals/flows cannot be settled by choosing the more plausible or more detailed source location.
- **ECV/ESG rule:** ECV 1, 2, 3, 7, 9, 10, 12, 20
- **Evidence inspected:** P3-CON-001 and Phase 3 register; current authentication proof discrepancy; current WHO7/18/22/24 preserved discrepancy sections; ZigBee conflicts carried into canonical variant page.
- **Evidence class:** PUB, RES
- **Applicability:** Exact supplied source revisions and operations, not all commands in those namespaces.
- **Finding:** HMAC copen/sopen versus hex constants, ZigBee UP 1/2 and reset 0/75 remain unresolved. Existing WHO7 range conflict, WHO18 forcing-duration upper bound, WHO22 malformed frames/tone and unit discrepancies, and WHO24 read/write mismatches remain source contradictions. Prior qualification is retained; Phase 4 did not freshly re-extract every detailed flow.
- **Required remediation:** Use independently validated authentication vectors or target-scoped operation tests and exact source locations. Do not repair frames by generic grammar or transfer SCS values into ZigBee.
- **Resolution:** No unsupported selection made. HMAC and previously qualified functional sections retained; newly exposed ZigBee conflicts visible canonically.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Checked current caveats against Phase 3 findings; independent behavioral resolution intentionally not claimed.
- **Open evidence gap:** Working HMAC vectors; safe product/interface tests; remaining detailed source-flow adjudication. Lighting timing is separately P4-FAC-002.

### P4-ARC-001 - Incidental canonicality handoff for Phase 5

- **Finding ID:** `P4-ARC-001`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** guides/; protocol/addressing.md; protocol/zigbee-interface.md; device-model/; diagnostics/; reverse-engineering/open-questions.md
- **Claim/issue:** Factual work exposed duplicated semantics and unclear ownership that could recreate corrected drift.
- **ECV/ESG rule:** ECV 11, 12, 13, 14, 15, 16, 19
- **Evidence inspected:** P4-FAC-003, 005, 007 and 009 changed claims and existing Phase 1 canonical-placement map.
- **Evidence class:** META, RES
- **Applicability:** Documentation architecture only; no new wire conclusions.
- **Finding:** Seven guides repeated DIMENSION38 without canonical caveat; common routing prose exceeded WHO2 reference; N_CONF landing drifted from identity reference; physical versus advanced classification spans model/diagnostics/programming. New ZigBee boundary is canonical for interface applicability, not an alternate complete WHO encyclopedia.
- **Required remediation:** Phase 5 Sol: retain independently executable guide material but preserve canonical applicability caveats; cross-reference DIMENSION38 definition; keep SCS/variant address applicability explicit; centralize entity/counterpart definitions and keep research as history. Integrate future ZigBee operation details under their WHO/mechanism owners with interface links, avoiding duplicate numeric tables.
- **Resolution:** Phase 5 added the cross-area scope/architecture owner, centralized `DIMENSION 38` detailed-read ownership under Diagnostics, linked guide copies to that owner, preserved Device Model identity ownership, and connected the ZigBee interface boundary to its functional namespace owners. No ambiguous semantics were selected.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Phase 5 inspected every named path and dependency, checked the changed ownership links, and retained all four Phase 4 `ASTRA-FINAL-REVIEW` qualifications.
- **Open evidence gap:** The unresolved semantics in `P4-FAC-002`, `P4-FAC-003`, `P4-FAC-005`, and `P4-REV-001`; future detailed ZigBee integration must follow the established ownership rule.

### P4-AUD-001 - Bounded factual audit and retained findings

- **Finding ID:** `P4-AUD-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** project/review/phase-4-factual-audit.md; project/review/ecv-esg-review-ledger.md
- **Claim/issue:** A cost-constrained pass must not turn focused inspection into an exhaustive factual certificate.
- **ECV/ESG rule:** ECV 1, 2, 5, 6, 7, 8, 16, 19, 20
- **Evidence inspected:** Canonical ECV/ESG; Phase 1 ledger inventory/matrix; Phase 2 findings; Phase 3 report; targeted canonical pages and named source sections in this phase's findings.
- **Evidence class:** META, RES, PUB, REG, CAT, SCN
- **Applicability:** Phase 4 starts at 6b25b581d1a5c8189d9589ec89d8aa844adebb54; source revisions unchanged.
- **Finding:** Retained correctly scoped STATE-dependent Object/Virgin Object resolution, firmware -1 versus missing build distinction, SYS unknown boundary, configuration ownership sentinels, optional diagnostic support and acceptance-versus-readback separation. No complete raw-capture archive, APP execution or Device experiment became available.
- **Required remediation:** Use the phase report and ledger for later work; retain Phase 3 genuine gaps and unexamined portions.
- **Resolution:** Focused corrections and final-review handoff recorded; no inventory restart, source fingerprint rerun, prose polishing or mechanical ESG/link sweep.
- **Reviewer/model:** GPT-6 Astra, Medium reasoning (Phase 4)
- **Verification:** Claim-level inspection and post-edit reading used; remote committed blob verification provides change integrity, not protocol interoperability certification.
- **Open evidence gap:** All Phase 3 residual gaps not explicitly closed remain; unchanged pages are not automatically approved by this pass.

### P5-ARC-001 - Cross-area OpenWebNet scope and mechanism ownership

- **Finding ID:** `P5-ARC-001`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** protocol/scope-and-architecture.md; README.md; protocol/README.md; diagnostics/README.md; programming/README.md; device-model/README.md
- **Claim/issue:** Transport/interface behavior, runtime functional control, discovery, interview, detailed configuration reading, programming, and catalogue capability lacked one canonical cross-area ownership map.
- **ECV/ESG rule:** ECV 11, 12, 13, 14, 15, 16, 19; ESG 10, 13
- **Evidence inspected:** Phase 1 canonical-placement map; Phase 4 report; P4-ARC-001; existing Protocol, Device Model, Diagnostics, and Programming landing pages and architecture pages.
- **Evidence class:** META, RES
- **Applicability:** Documentation architecture and navigation; no protocol behavior or transport support newly asserted.
- **Finding:** The local landing-page boundaries were substantially consistent, but a reader had to reconstruct the complete layer model across sections. This left OpenWebNet scope and composed-workflow boundaries vulnerable to drift.
- **Required remediation:** Establish one cross-area map and have the principal landing pages consume it while retaining their subject-specific definitions.
- **Resolution:** Added OpenWebNet Scope and Architecture and linked it from the five principal entry points. The page defines scope, mechanism separation, interface applicability, entity/identity boundaries, and canonical owners from conclusions already established by Phase 4.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** Changed passages inspected against ECV 11 through 16 and Phase 4; post-edit link/fragment checks pass.
- **Open evidence gap:** Detailed operation applicability remains bounded by Phase 3/4 evidence; the architecture map does not certify an interface or Device.

### P5-ARC-002 - Device entities, protocol identities, and addresses have explicit owners

- **Finding ID:** `P5-ARC-002`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** protocol/scope-and-architecture.md; device-model/README.md; device-model/sources-and-identifiers.md; diagnostics/architecture.md; programming/device-selection.md
- **Claim/issue:** Physical Device, catalogue Device record/SKU, installed Device ID, diagnostic `WHERE`, functional `WHERE`, Module/`slot`, Object/Virgin Object, and Configuration are frequently composed in one workflow and require a stable cross-area boundary.
- **ECV/ESG rule:** ECV 9, 13, 15, 16, 19; ESG 2, 13
- **Evidence inspected:** Phase 4 P4-FAC-003, P4-FAC-006, and P4-FAC-007; Device Model canonical hierarchy and identifier matrix; diagnostic address roles; programming selection boundaries.
- **Evidence class:** META, RES, CAT, REG
- **Applicability:** Documentation entity model and identifier ownership; existing factual correlations and uncertainties are unchanged.
- **Finding:** The detailed definitions were already correct in Device Model, but no cross-area entry point summarized which identity selects which layer. Local descriptions were not competing definitions and should remain for comprehension.
- **Required remediation:** Link the architecture map to the detailed Device Model policy and state the identity/address separations without collapsing local context.
- **Resolution:** Added the entity/identity boundary table and made Device Model the explicit canonical owner. Individual entity-page definitions were retained because they agree and provide local context.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** Compared all table entries with Sources and Identifier Boundaries, Device Model, Diagnostic Architecture, and Device Selection; no namespace mapping was added.
- **Open evidence gap:** Exact diagnostic-address relationships and `DIMENSION 32` decoding remain `P4-FAC-003`.

### P5-ARC-003 - Detailed configuration reading has one canonical protocol definition

- **Finding ID:** `P5-ARC-003`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** diagnostics/dim35-configuration.md; diagnostics/device-interview.md; device-model/configuration.md; guides/
- **Claim/issue:** `DIMENSION 38` frames, `DiagKO` ordering, and their unresolved reset/select effect were substantially defined in both Diagnostics and Device Model, while guides necessarily repeated the operational step.
- **ECV/ESG rule:** ECV 1, 3, 10, 13, 14, 19; ESG 13
- **Evidence inspected:** P4-FAC-005 and P4-ARC-001; diagnostic detailed-read page; Device Interview; Device Model configuration projection; all seven guide call sites identified in Phase 4.
- **Evidence class:** META, RES, REG
- **Applicability:** Documentation ownership only; `DIMENSION 38` effects remain unresolved by Device family and firmware.
- **Finding:** Diagnostics is the proper owner of the management frame and sequence. Device Model should own catalogue correlation, and Practical Guides may repeat the operation only with the canonical qualification required for safe execution.
- **Required remediation:** Remove the competing frame/sequence definition from Device Model; link Device Interview and guide copies to the diagnostic owner; preserve each guide's operational caveat.
- **Resolution:** Applied. Device Model now summarizes only the projection/correlation; Device Interview links the later phase; all exposed guide copies retain the Phase 4 gate and link to the canonical treatment.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** Targeted search confirms the canonical definition remains in Diagnostics and each guide call site retains the effect qualification; internal links pass.
- **Open evidence gap:** `P4-FAC-005` remains `ASTRA-FINAL-REVIEW`; no non-destructive interpretation was selected.

### P5-ARC-004 - ZigBee applicability links to functional namespace owners

- **Finding ID:** `P5-ARC-004`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** protocol/zigbee-interface.md; functional/source-coverage.md; functional/who-1-lighting/README.md; functional/who-2-automation/README.md; functional/who-4-temperature-control/README.md; functional/who-13-integration-gateway/README.md; functional/who-18-energy-management/README.md; functional/who-25-transversal/README.md
- **Claim/issue:** The new ZigBee interface boundary named six functional namespaces, but three owners lacked variant notices and the source-coverage page still said the inspected material had not been integrated.
- **ECV/ESG rule:** ECV 3, 11, 12, 13, 19; ESG 13
- **Evidence inspected:** P4-FAC-009, P4-ARC-001, protocol/zigbee-interface.md, the six functional landing pages, and functional/source-coverage.md.
- **Evidence class:** META, RES
- **Applicability:** Canonical placement for the source-scoped Legrand ZigBee interface; no detailed operation support added.
- **Finding:** The interface page should own cross-cutting transport/applicability limits while each functional directory owns any established runtime semantics. Stale coverage wording obscured the bounded Phase 4 integration.
- **Required remediation:** Add reciprocal owner links and bounded notices; state accurately that interface boundaries are integrated while detailed operations remain incomplete.
- **Resolution:** Applied to the interface page, the three previously unlinked `WHO` owners, and the source-coverage statement. Existing `WHO 13`, `18`, and `25` notices were retained.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** All six namespace owners are linked from the interface page; each owner now has an interface boundary directly or through its existing notice; no conflicting value was adjudicated.
- **Open evidence gap:** Publication provenance, unexamined detailed flows, interface testing, and ZigBee conflicts remain as recorded in Phase 3 and `P4-REV-001`.

### P5-ARC-005 - Practical Guide repetition retains canonical qualifications

- **Finding ID:** `P5-ARC-005`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** guides/read-device-configuration.md; guides/retrieve-actuator-group-memberships.md; guides/retrieve-configured-cen-buttons.md; guides/troubleshoot-diagnostics.md; guides/validate-configuration-value.md; guides/program-device.md; guides/verify-programming.md
- **Claim/issue:** The guide exception permits operational repetition, but repeated `DIMENSION 38` instructions must remain connected to the canonical uncertainty so future edits do not recreate Phase 4 drift.
- **ECV/ESG rule:** ECV 3, 13, 14, 19; ESG 13
- **Evidence inspected:** P4-FAC-005; P4-ARC-001; seven guide call sites and the canonical diagnostic treatment.
- **Evidence class:** META, RES
- **Applicability:** Independently executable Practical Guides; no guide was treated as protocol authority.
- **Finding:** Removing the repeated step would impair executable workflows. Retaining the frame, stop condition, and applicability caveat while linking the canonical owner satisfies the Practical Guide exception.
- **Required remediation:** Preserve local operational context and add canonical links wherever absent.
- **Resolution:** Six missing links added; program-device.md already linked correctly and was left unchanged.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** Targeted search confirms seven qualified guide call sites and canonical links; wording still stops execution where effects are not established.
- **Open evidence gap:** End-to-end guide validation and `DIMENSION 38` target effects remain unavailable.

### P5-ARC-006 - Machine KB consistency cannot yet be evaluated

- **Finding ID:** `P5-ARC-006`
- **Status:** Accepted evidence gap
- **Severity:** Informational
- **Path:** repository-wide; project/encyclopedia-core-values.md; project/review/phase-5-architecture-audit.md
- **Claim/issue:** ECV 19 requires canonical consistency between human documentation and the Machine KB, but this branch contains no Machine KB representation.
- **ECV/ESG rule:** ECV 19
- **Evidence inspected:** Phase 1 complete repository inventory; current top-level tree; ECV 19; Phase 5 canonical ownership changes.
- **Evidence class:** META
- **Applicability:** `general-once-over` human encyclopedia at Phase 5.
- **Finding:** There is no second representation to compare. Absence of a Machine KB is not evidence of consistency or inconsistency.
- **Required remediation:** When a Machine KB is introduced, derive or validate it against the canonical owners and preserve the same unresolved/observed/inferred states and applicability boundaries.
- **Resolution:** Evidence gap recorded; no placeholder machine representation manufactured.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** No Machine KB directory or representation appears in the complete Phase 1 inventory or current branch tree.
- **Open evidence gap:** The future Machine KB schema, content, generation path, and consistency validation.

### P5-REV-001 - Phase 4 Astra queue retained through restructuring

- **Finding ID:** `P5-REV-001`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** protocol/authentication.md; protocol/zigbee-interface.md; protocol/addressing.md; diagnostics/dim32-addressing.md; diagnostics/dim35-configuration.md; functional/who-1-lighting/what.md; functional/who-7-multimedia-video/README.md; functional/who-18-energy-management/what.md; functional/who-22-sound-diffusion/README.md; functional/who-24-lighting-management/dimensions.md
- **Claim/issue:** Architecture changes must not silently resolve or obscure factual conflicts handed off by Astra.
- **ECV/ESG rule:** ECV 1, 2, 3, 7, 10, 12, 13, 19
- **Evidence inspected:** `P4-FAC-002`, `P4-FAC-003`, `P4-FAC-005`, `P4-REV-001`; Phase 4 report; every Phase 5 changed passage touching those boundaries.
- **Evidence class:** META, RES
- **Applicability:** The four exact Phase 4 final-review records and their existing source/Device/transport scopes.
- **Finding:** Lighting timing, `DIMENSION 32`/routing interpretations, `DIMENSION 38` effects, authentication constants, ZigBee conflicts, and retained functional contradictions still require evidence adjudication. Canonical ownership can be improved without choosing among them.
- **Required remediation:** Retain all four Phase 4 records as `ASTRA-FINAL-REVIEW`; use the evidence specified by each record before changing their factual conclusions.
- **Resolution:** Queue retention verified. This tracking record is closed so it is not counted as a duplicate fifth issue; the four underlying Phase 4 records remain `ASTRA-FINAL-REVIEW` with all qualifications visible.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** Phases 5 and 7 compared current canonical text with each Phase 4 guardrail; no disputed value, mapping, effect, or frame repair was selected. Ledger status search now returns exactly the four underlying records.
- **Open evidence gap:** Exactly the evidence listed in `P4-FAC-002`, `P4-FAC-003`, `P4-FAC-005`, and `P4-REV-001`.

### P5-AUD-001 - Bounded architecture audit

- **Finding ID:** `P5-AUD-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** project/review/phase-5-architecture-audit.md; project/review/ecv-esg-review-ledger.md
- **Claim/issue:** Phase 5 must resolve architectural drift without repeating Phase 4 source analysis or turning a bounded pass into an exhaustive new factual certification.
- **ECV/ESG rule:** ECV 1, 5, 6, 7, 8, 13, 19
- **Evidence inspected:** Canonical ECV/ESG; existing inventory/canonical map; Phase 3 assessment; Phase 4 report and findings; targeted dependent pages.
- **Evidence class:** META, RES
- **Applicability:** Phase 5 starts at `694da72957f584e0c744613a80543ab069767462`.
- **Finding:** The requested architecture issues could be resolved from established conclusions. No new source inspection or ambiguous protocol adjudication was necessary.
- **Required remediation:** Record scope, ownership decisions, verification, residual gaps, and the exact Astra queue.
- **Resolution:** Phase 5 report and ledger entries added; Phase 4 remains factual authority.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phase 5)
- **Verification:** Changed-file review, deterministic link/fragment checks, ESG checker, and targeted architecture searches completed after remediation.
- **Open evidence gap:** All Phase 3/4 gaps not explicitly closed remain genuine; unchanged pages are not newly factually certified.

### P6-ESG-001 - Bounded semantic and editorial review

- **Finding ID:** `P6-ESG-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** All 138 human-facing encyclopedia pages
- **Claim/issue:** Phase 6 must assess semantic presentation under the ESG without weakening Phase 4 evidence, uncertainty, or applicability decisions.
- **ECV/ESG rule:** ECV 1 through 4, 10, 12 through 17, 19; ESG 1 through 15
- **Evidence inspected:** Canonical ESG; current ledger; Phase 4 factual audit and final-review queue; Phase 5 canonical ownership map; every human-facing page through deterministic checks and targeted terminology, heading, example, link, presentation, and editorial searches.
- **Evidence class:** META, RES
- **Applicability:** Human-facing encyclopedia at Phase 5 commit `bd8aee0e17d05fde6770ed38891d229df567b3cb`.
- **Finding:** The established evidence vocabulary and Phase 4 qualifications remain visible. No editorial issue required a new protocol interpretation, and no new issue met the `ASTRA-FINAL-REVIEW` threshold.
- **Required remediation:** Correct only clear semantic or editorial defects and preserve all factual guardrails.
- **Resolution:** Applied the bounded corrections recorded below; no factual value, applicability statement, evidence status, or canonical protocol conclusion changed.
- **Reviewer/model:** GPT-5.6 Sol, Medium reasoning (Phase 6)
- **Verification:** Changed passages compared with Phase 4 and Phase 5; deterministic checker and full Markdown link/structure validation rerun after edits.
- **Open evidence gap:** All Phase 3 and Phase 4 evidence gaps remain unchanged; this editorial pass supplies no new protocol evidence.

### P6-ESG-002 - Canonical `slot` notation and grammar

- **Finding ID:** `P6-ESG-002`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** device-model/README.md; device-model/configuration.md; device-model/modules.md; device-model/physical-devices.md; diagnostics/dim30-modules.md; guides/read-device-configuration.md; protocol/dimensions.md; reverse-engineering/methodology.md
- **Claim/issue:** Several passages used the literal implementation position as plain “slot” or retained the ungrammatical article “an” after Phase 2 replaced the obsolete term.
- **ECV/ESG rule:** ESG 2, 5
- **Evidence inspected:** Canonical Module/`slot` definitions; affected passages; repository searches for `an \`slot\`` and plain `slot` in the corrected canonical contexts.
- **Evidence class:** META
- **Applicability:** Editorial notation for numeric protocol/database `slot`; scenario-memory uses of ordinary “slot” are outside this finding.
- **Finding:** The affected passages clearly refer to the numeric `SLOT`, `first_slot`, or catalogue placement concept and therefore require code formatting. Ten article mismatches were objective grammar defects.
- **Required remediation:** Use `slot` for the literal numeric/index concept, retain Module for the logical entity, and use the article “a”.
- **Resolution:** Corrected the grammar and the exposed canonical labels/descriptions without changing Module/Object relationships or runtime claims.
- **Reviewer/model:** GPT-5.6 Sol, Medium reasoning (Phase 6)
- **Verification:** Targeted search returns no `an \`slot\`` occurrences; deterministic terminology checks pass.
- **Open evidence gap:** None for terminology; the underlying protocol relationships retain their existing evidence status.

### P6-ESG-003 - Punctuation-normalization regressions

- **Finding ID:** `P6-ESG-003`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** device-model/configuration.md; reverse-engineering/database-relationship-reconstruction.md; guides/troubleshoot-diagnostics.md
- **Claim/issue:** Three former parenthetical breaks had become joined compounds: “and-where available-the”, “relationship-not”, and “falsifiable-for example”.
- **ECV/ESG rule:** ESG 1; ESG editorial mechanics
- **Evidence inspected:** Exact affected sentences and repository search for the same joined-parenthetical patterns.
- **Evidence class:** META
- **Applicability:** Prose mechanics only.
- **Finding:** Each construction was grammatically malformed and impeded the intended qualification.
- **Required remediation:** Restore normal sentence or comma structure without changing the qualified claim.
- **Resolution:** Recast the three sentences with commas or a sentence boundary; their evidence and uncertainty content is unchanged.
- **Reviewer/model:** GPT-5.6 Sol, Medium reasoning (Phase 6)
- **Verification:** Targeted search returns no remaining instances of the identified joined-parenthetical forms.
- **Open evidence gap:** None.

### P6-ESG-004 - Review candidates retained without semantic churn

- **Finding ID:** `P6-ESG-004`
- **Status:** Verified
- **Severity:** Informational
- **Path:** project/review/phase-4-factual-audit.md; guides/read-device-configuration.md; guides/retrieve-actuator-group-memberships.md; guides/retrieve-configured-cen-buttons.md
- **Claim/issue:** The deterministic checker reports protocol-literal candidates in a historical audit report and repeated operational passages in Practical Guides.
- **ECV/ESG rule:** ECV 3; ESG 5, 13
- **Evidence inspected:** All 34 post-edit checker candidates and the Phase 4/5 records governing their status.
- **Evidence class:** META, RES
- **Applicability:** Historical review report and independently executable Practical Guides.
- **Finding:** Twenty-seven candidates occur only in the Phase 4 report and preserve its review record; seven are permitted guide repetitions needed for executable workflows. None is a human-reference regression or competing canonical definition.
- **Required remediation:** Retain the report history and operational guide context; continue linking guides to canonical owners.
- **Resolution:** No prose removed or weakened. Existing canonical links and Phase 4 qualifications remain in place.
- **Reviewer/model:** GPT-5.6 Sol, Medium reasoning (Phase 6)
- **Verification:** Final checker reports 34 review candidates with the same 27/7 disposition and zero objective failures.
- **Open evidence gap:** Guide workflows still lack the end-to-end experimental validation recorded in Phase 3; repetition does not close that gap.

### P7-EPI-001 - Deterministic contradiction and drift candidate audit

- **Finding ID:** `P7-EPI-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** All 138 human-facing encyclopedia pages; `project/review/checks/audit_epistemic_drift.py`
- **Claim/issue:** Repeated ranges, frames, evidence-status language, and multi-frame blocks require a reproducible candidate inventory before semantic comparison.
- **ECV/ESG rule:** ECV 1 through 4, 7, 9, 10, 12, 15 through 17, 19; ESG 3, 6, 8, 13, 15
- **Evidence inspected:** Complete human-page population; 306 range occurrences; 529 inline frame occurrences; lines combining observation with universal language; implementation-evidence promotion patterns; absence claims; all multi-frame candidates; Phase 4 findings and current canonical owners.
- **Evidence class:** META, RES
- **Applicability:** Human encyclopedia at Phase 6 commit `8d79c210046dc2a8d48dcfd45f501894ebde8c82`; candidate detection is lexical and does not decide protocol truth.
- **Finding:** The script found 106 unique range tokens, 55 repeated range tokens, 283 unique inline frames, 112 repeated exact frames, and 53 semantic candidates. Manual review found the observation/universal and absence candidates were explicit guardrails; repeated exact literals were context-consistent, explicitly contrasted, or permitted Guide copies. Eight unlabelled multi-frame blocks are compact reference forms rather than transcripts. The four Phase 4 evidence conflicts remain visible.
- **Required remediation:** Correct only established drift; retain context-specific literals and disputed values; rerun after remediation and preserve the candidate classifications.
- **Resolution:** Reusable candidate checker added. The capability/runtime and range findings below record the clear corrections; no ambiguous value was selected.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phases 7 and 8)
- **Verification:** Post-edit script completes across 138 pages; targeted searches cover `WHAT 17`, `DIMENSION 32`, `DIMENSION 38`, HMAC, ZigBee, evidence labels, universal terms, and source-absence language.
- **Open evidence gap:** Mechanical equality cannot establish semantic identity or conflict; the four Phase 4 final-review records require evidence adjudication.

### P7-EPI-002 - Registered management capability overstated as Device participation

- **Finding ID:** `P7-EPI-002`
- **Status:** Verified
- **Severity:** Substantive
- **Path:** `functional/open-db-coverage.md`; `functional/who-8-video-door-entry-telephony/README.md`; `functional/who-99-service-identification/README.md`
- **Claim/issue:** Three descriptions of implementation templates used wording that could elevate a database association into runtime support or proof.
- **ECV/ESG rule:** ECV 2, 4, 7, 10, 16, 19; ESG 3, 15
- **Evidence inspected:** Phase 4 `P4-FAC-004`; `OPEN.db` coverage descriptions for Lighting/Automation, Energy Management, Access Control, `WHO 8`, and `WHO 99`; related canonical applicability statements.
- **Evidence class:** REG, RES, META
- **Applicability:** MyHOME Suite 3.5.38 registered operation associations only; no installed Device behavior is newly claimed.
- **Finding:** A 65-record association establishes the management capability surface registered for a system in MyHOME Suite. It does not establish that every installed Device in that family supports every operation. A parameterized template establishes its database association, not a complete protocol vocabulary.
- **Required remediation:** State implementation capability and per-Device limits explicitly; replace proof language where it exceeds the database's authority.
- **Resolution:** Qualified the three managed-system descriptions and replaced two exposed proof phrasings. Functional semantics and stored frames are unchanged.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phases 7 and 8)
- **Verification:** Targeted review confirms every affected paragraph now separates registered implementation capability from runtime support and protocol completeness.
- **Open evidence gap:** Installed Device support still requires applicable observations or controlled experiments as recorded by `P1-GAP-005` and `P1-GAP-008`.

### P7-ESG-001 - Inline-code range notation drift

- **Finding ID:** `P7-ESG-001`
- **Status:** Verified
- **Severity:** Editorial
- **Path:** Device Model; Diagnostics; Protocol; selected Functional, Guide, Reverse Engineering, and Scenario Engine pages
- **Claim/issue:** Phase 2's plain-text detector did not see several inclusive domains whose endpoints were separately code-formatted with “to” or “through”.
- **ECV/ESG rule:** ESG 5, 6
- **Evidence inspected:** Repository search for code-formatted numeric endpoints joined by “to” or “through”; exact surrounding claims; Phase 4 values and applicability.
- **Evidence class:** META, RES
- **Applicability:** Unambiguous inclusive numeric domains only; relationship phrases and non-domain sequences are excluded.
- **Finding:** Fifteen exposed domain expressions used prose separators despite ESG 6. The values themselves agreed with their canonical definitions and required no factual change.
- **Required remediation:** Render the domains with `..` while preserving values, fixed widths, prefixes, units, and qualifications.
- **Resolution:** Corrected the exposed Device ID, `slot`, group, HMAC nibble, implementation, CEN, group-membership, temperature, and timed-action domains. Also corrected one residual “An `slot`” grammar defect.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phases 7 and 8)
- **Verification:** The targeted endpoint search now returns only relationship uses, one non-contiguous example sequence, and phrases where “through” describes resolution rather than a numeric domain; Phase 2 checker passes.
- **Open evidence gap:** None for notation; this finding does not validate the factual origin of each range beyond the established Phase 4 state.

### P8-REM-001 - Historical ledger queue reconciled

- **Finding ID:** `P8-REM-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** `project/review/ecv-esg-review-ledger.md`; canonical pages referenced by reconciled findings
- **Claim/issue:** Several Phase 1 through 3 records remained Open after later phases completed their remediation or accurately bounded the unavailable evidence.
- **ECV/ESG rule:** ECV 3, 6, 8, 19
- **Evidence inspected:** Every non-Verified Blocking, Substantive, and Editorial ledger record; Phase 3 coverage conclusions; Phase 4 authority; Phase 5 ownership changes; Phase 6 semantic review; current canonical representations.
- **Evidence class:** META, RES
- **Applicability:** Ledger state through Phase 8; historical claim text remains preserved.
- **Finding:** ZigBee integration and its coverage-map handoff are verified; diagnostics/programming, application runtime, scenario runtime, high-priority semantic questions, and ZigBee publication provenance are accurately represented accepted gaps; the Phase 3 contradiction umbrella is superseded by four specific Phase 4 records; both Phase 2 semantic candidates are verified.
- **Required remediation:** Update status, resolution, and verification fields without erasing original findings or treating evidence absence as a negative protocol conclusion.
- **Resolution:** Reconciled `P1-GAP-003`, `P1-GAP-005` through `007`, `P1-GAP-009`, `P2-AMB-001`, `P2-AMB-002`, `P3-COV-004`, `P3-PROV-003`, `P3-CON-001`, and the duplicate Phase 5 queue tracker.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phases 7 and 8)
- **Verification:** Final status/severity inventory contains no Open, Investigating, Remediation-ready, or Fixed Blocking/Substantive/Editorial item. Accepted gaps point to canonical qualifications and retain precise missing evidence.
- **Open evidence gap:** Accepted gaps remain open in the evidence, even though their documentation remediation is complete.

### P8-REV-001 - Final Astra queue normalized

- **Finding ID:** `P8-REV-001`
- **Status:** Verified
- **Severity:** Informational
- **Path:** `P4-FAC-002`; `P4-FAC-003`; `P4-FAC-005`; `P4-REV-001`; `project/review/phase-9-review-packet.md`
- **Claim/issue:** Tracking records must not inflate the final evidence-sensitive review queue or obscure the exact unresolved questions.
- **ECV/ESG rule:** ECV 1 through 4, 6 through 10, 19
- **Evidence inspected:** All ledger status values; Phase 4 report and findings; canonical pages for every disputed subject; Phase 5 tracking record.
- **Evidence class:** META, RES
- **Applicability:** Final independent-review handoff after Phase 8.
- **Finding:** The final queue contains exactly four substantive records. `P5-REV-001` is a verified queue-retention record, not a separate factual question.
- **Required remediation:** Keep only the four underlying records at `ASTRA-FINAL-REVIEW` and provide exact evidence pointers in the Phase 9 packet.
- **Resolution:** Queue normalized without deciding any disputed value or behavior.
- **Reviewer/model:** GPT-5.6 Sol, High reasoning (Phases 7 and 8)
- **Verification:** Exact ledger status count and packet rows both equal four; canonical qualifications remain present.
- **Open evidence gap:** The independent evidence specified by each of the four Phase 4 records.

## Finding record template

New findings must preserve all fields below. A field may say “None” or “Not yet established,” but must not be omitted.

```text
### <Finding ID> - <Short title>

- Finding ID:
- Status:
- Severity:
- Path:
- Claim/issue:
- ECV/ESG rule:
- Evidence inspected:
- Evidence class:
- Applicability:
- Finding:
- Required remediation:
- Resolution:
- Reviewer/model:
- Verification:
- Open evidence gap:
```

## Phase 1 exit state

Phase 1 is complete when the authoritative baseline, canonical ECV/ESG, complete human-facing page population, supporting pages, primary source artifacts, major dependencies, coverage matrix, and known inaccessible or unexamined evidence are all represented here. Completion of Phase 1 does not close any substantive factual gap and does not certify ECV or ESG compliance.
