# ECV/ESG Review Ledger

This ledger records the formal review of the human-facing OpenWebNet Encyclopedia against the canonical [Encyclopedia Core Values](../encyclopedia-core-values.md) (ECV) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md) (ESG).

It is a review artifact, not canonical protocol knowledge. Phase 1 establishes the inventory, canonical-placement map, evidence-corpus register, coverage matrix, and explicit evidence gaps. It does not adjudicate protocol claims or authorize speculative protocol changes.

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

The Phase 1 inventory contains 136 human-facing encyclopedia pages: the root page plus 135 pages across the nine subject areas. The baseline also contains three project-governance pages and seven source-provenance pages. These ten supporting pages are inventoried separately because they govern or describe the encyclopedia rather than form its protocol content.

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
- **Status:** Accepted evidence gap
- **Severity:** Substantive
- **Path:** `sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf`, `sources/openwebnet-public/pdf/WHO_6_L4686SDK.pdf`
- **Claim/issue:** Both PDFs are present and fingerprinted in the authoritative repository but are not materialized in the local review workspace.
- **ECV/ESG rule:** ECV 5, 6, 7, 8, 12, 20
- **Evidence inspected:** Manifest entries, authoritative Git tree entries, functional source-coverage page, prior review record
- **Evidence class:** META; PUB existence only
- **Applicability:** ZigBee-backed OpenWebNet and product-specific `WHO 6` coverage
- **Finding:** Their existence, size, and fingerprint are established; their contents were not freshly reviewed in Phase 1.
- **Required remediation:** Materialize and inspect both PDFs in a later evidence-review phase before certifying those subject areas.
- **Resolution:** Recorded as an explicit inspection boundary.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Baseline tree contains both blobs and manifest fingerprints; local baseline snapshot lacks both files.
- **Open evidence gap:** Page-level claims, diagrams, examples, caveats, and internal contradictions in these documents remain unexamined in this phase.

### P1-GAP-003 - ZigBee-backed OpenWebNet not integrated

- **Finding ID:** `P1-GAP-003`
- **Status:** Open
- **Severity:** Substantive
- **Path:** Protocol, Functional, Diagnostics, Programming, Device Model, and source-coverage sections
- **Claim/issue:** The baseline contains `OpenWebNet_Zigbee.pdf` but no canonical human-facing treatment of its OpenWebNet-visible differences.
- **ECV/ESG rule:** ECV 5, 6, 11, 12, 13, 14, 20; ESG 10, 13, 15
- **Evidence inspected:** Complete human-facing path inventory; repository-wide ZigBee term search; manifest and source coverage
- **Evidence class:** META, RES
- **Applicability:** OpenWebNet variants/transports, especially Lighting, Automation, addressing, Diagnostics, and Programming
- **Finding:** Current coverage cannot establish where SCS-specific behavior is being treated as universal or how ZigBee-backed systems affect the documented mechanisms.
- **Required remediation:** Later factual review must inspect the canonical ZigBee PDF, map only OpenWebNet-visible differences, scope SCS behavior, and leave underlying ZigBee internals outside the encyclopedia unless mediated by OpenWebNet.
- **Resolution:** Pending later phase; no speculative protocol edits made.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** No substantive ZigBee treatment appears in the 136-page human-facing baseline.
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
- **Status:** Open
- **Severity:** Substantive
- **Path:** `diagnostics/`, `programming/`, associated guides
- **Claim/issue:** Most MyHOME Suite Device interview and programming mechanisms are established from implementation data and private observations rather than a complete public protocol specification.
- **ECV/ESG rule:** ECV 2, 4, 5, 6, 7, 8, 10, 14, 17, 20; ESG 3, 15
- **Evidence inspected:** Diagnostic/programming page inventory, `OPEN.db` surface, catalogue surface, prior review, source policy
- **Evidence class:** REG, CAT, VAL, OBS-derived RES
- **Applicability:** Diagnostic families, configuration reading, and Device programming workflows
- **Finding:** Coverage exists but independent reproducibility and general applicability cannot yet be established across all Devices, firmware, gateways, diagnostic families, or transports.
- **Required remediation:** Claim-level deep review must tag evidence class/applicability, separate syntax from support and behavior, and preserve open fields.
- **Resolution:** Pending later factual review.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** No complete public diagnostic/programming specification is present; the pages themselves identify observation limits.
- **Open evidence gap:** Sanitized captures, controlled Device matrices, gateway/version matrices, abort/error paths, and transport variants.

### P1-GAP-006 - Application runtime and localization evidence incomplete

- **Finding ID:** `P1-GAP-006`
- **Status:** Open
- **Severity:** Substantive
- **Path:** `internals/`, `scenario-engine/`, `reverse-engineering/open-questions.md`
- **Claim/issue:** Stored databases and `OpenQuery.txt` do not preserve callers, selection precedence, caching/migration, localization resources, or full runtime control flow.
- **ECV/ESG rule:** ECV 1, 2, 4, 5, 6, 7, 8, 10, 16, 20; ESG 3, 15
- **Evidence inspected:** Implementation-boundary pages, open questions, support-file inventory, installer manifest record
- **Evidence class:** CAT, REG, SCN, VAL, SUP, RES
- **Applicability:** MyHOME Suite 3.5.38 implementation behavior only
- **Finding:** Database structure can establish stored capability and associations, but not the complete application algorithm or UI semantics.
- **Required remediation:** Later review must scope implementation claims and identify where APP evidence or legitimate runtime tracing is required.
- **Resolution:** Pending; no application behavior inferred from data presence alone.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Open questions and Internals pages explicitly identify these missing layers.
- **Open evidence gap:** Installer/application binary inspection, file-access traces, executed-query traces, localization resources, UI workflows, and persistence behavior.

### P1-GAP-007 - Scenario execution persistence and control flow unavailable

- **Finding ID:** `P1-GAP-007`
- **Status:** Open
- **Severity:** Substantive
- **Path:** `scenario-engine/`
- **Claim/issue:** ScenarioDevices files describe capabilities but do not establish complete user-authored graph storage or runtime execution.
- **ECV/ESG rule:** ECV 1, 2, 4, 5, 6, 7, 10, 16, 20; ESG 3, 15
- **Evidence inspected:** Both ScenarioDevices schemas and row surfaces; Scenario Engine open questions; Internals coverage
- **Evidence class:** SCN, RES
- **Applicability:** MyHOME Suite 3.5.38 Scenario Engine
- **Finding:** Capability templates, categories, and parameters can be inventoried, while graph persistence, branches, ordering, event matching, scheduling, retries, and error handling remain incompletely supported.
- **Required remediation:** Later factual review must prevent capability rows from being presented as complete runtime behavior and identify the missing APP/OBS evidence.
- **Resolution:** Pending.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Neither preserved ScenarioDevices database contains an evident complete scenario-instance graph model.
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
- **Status:** Open
- **Severity:** Substantive
- **Path:** `reverse-engineering/open-questions.md` and linked canonical pages
- **Claim/issue:** Known unresolved areas require targeted evidence rather than editorial completion.
- **ECV/ESG rule:** ECV 1, 2, 3, 4, 6, 8, 9, 10, 17, 20; ESG 3, 15
- **Evidence inspected:** Open Questions, Relationship Register, rejected relationships, prior review record
- **Evidence class:** RES, CAT, REG, SCN, OBS-derived RES
- **Applicability:** Individual questions as scoped in their canonical pages
- **Finding:** Highest-priority gaps include `DIMENSION 32.SYS`; `DIMENSION 4`/`5`; Object-specific `DIMENSION 310`; hardware/microcontroller version mapping; address-rule selection/rendering; firmware selection precedence; Object replacement; physical-to-advanced translation; catalogue-wide `N_CONF` equivalence; ScenarioDevices precedence; and application runtime/localization behavior.
- **Required remediation:** Carry each question into claim-level review and later evidence acquisition without reopening already established boundaries.
- **Resolution:** Consolidated into the coverage matrix; no semantic decision made.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** Each item is explicitly recorded in the baseline open-question pages.
- **Open evidence gap:** The discriminating observations listed in `reverse-engineering/open-questions.md`.

### P1-ESG-001 - Deterministic ESG review not yet performed

- **Finding ID:** `P1-ESG-001`
- **Status:** Open
- **Severity:** Editorial
- **Path:** All 136 human-facing pages
- **Claim/issue:** Phase 1 inventoried pages and dependencies but did not perform the later deterministic or semantic ESG pass.
- **ECV/ESG rule:** ESG 1-15 and Editorial Mechanics
- **Evidence inspected:** Page paths, H1 headings, local-link dependency graph, canonical ESG
- **Evidence class:** META
- **Applicability:** Fixed baseline human-facing documentation
- **Finding:** Page population and architecture are known; compliance with terminology, evidence vocabulary, code formatting, range/hex notation, transcript direction, hierarchy, recurring sections, link labels, presentation form, and example labelling remains to be tested systematically.
- **Required remediation:** Execute the dedicated ESG phases using this complete inventory; record defects as separate findings rather than silently editing protocol meaning.
- **Resolution:** Pending later phase.
- **Reviewer/model:** Codex, GPT-5
- **Verification:** No claim of complete ESG compliance is made by this phase.
- **Open evidence gap:** None; this is unperformed review work rather than unavailable external evidence.

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
