# Phase 9 Review Packet

## 1. Unresolved `ASTRA-FINAL-REVIEW` items with evidence pointers

| Ledger item | Residual question | Evidence pointers | Independent evidence required |
| --- | --- | --- | --- |
| [`P4-FAC-002`](ecv-esg-review-ledger.md#p4-fac-002---lighting-what-17-duration-remains-contradictory) | Lighting `WHAT 17`: 30 seconds versus 30 minutes | [canonical command treatment](../../functional/who-1-lighting/what.md#target-dependent-myhome-suite-label-for-what-17); [cross-database qualification](../../functional/cross-database-coverage.md#who-1-target-dependent-interpretation); [`WHO_1.pdf`](../../sources/openwebnet-public/pdf/WHO_1.pdf) summary and section 3.1.9; ScenarioDevices door-lock template | Target-scoped timing experiment and independently applicable authoritative clarification |
| [`P4-FAC-003`](ecv-esg-review-ledger.md#p4-fac-003---address-namespaces-and-pl0-interpretation-cannot-be-collapsed) | `DIMENSION 32.SYS`, `ADDR` conversion, historical `PL=0`, and Automation routing combinations | [`DIMENSION 32` treatment](../../diagnostics/dim32-addressing.md); [common addressing boundary](../../protocol/addressing.md); [write gate](../../programming/address-programming.md); [open questions](../../reverse-engineering/open-questions.md) | Raw tuples with exact Object/Firmware context, discriminating non-Lighting responses, and an applicable encoder or consumer with controlled operation evidence |
| [`P4-FAC-005`](ecv-esg-review-ledger.md#p4-fac-005---detailed-read-guides-omit-dimension-38-effect-ambiguity) | `DIMENSION 38` retrieval role versus reset/select effect | [canonical detailed-read sequence](../../diagnostics/dim35-configuration.md#reading-detailed-parameters); [Guide applicability gate](../../guides/read-device-configuration.md); Phase 4's seven qualified call sites | Restore-safe before/after experiments or applicable implementation evidence defining effects, scope, and repetition behavior |
| [`P4-REV-001`](ecv-esg-review-ledger.md#p4-rev-001---independent-adjudication-of-source-contradictions) | HMAC identity constants; ZigBee UP/reset conflicts; retained `WHO 7`, `18`, `22`, and `24` source discrepancies | [authentication limitation](../../protocol/authentication.md); [ZigBee conflict table](../../protocol/zigbee-interface.md#preserved-source-conflicts); [Phase 4 audit](phase-4-factual-audit.md#unresolved-evidence-and-final-review); affected functional pages listed in the ledger record | Working authentication vectors, exact product/interface tests, and source-location-specific adjudication under the applicable variant |

## 2. High-risk pages materially changed in Phase 4

| Risk surface | Pages to sample |
| --- | --- |
| Common grammar, correlation, and variant applicability | [Frame Syntax](../../protocol/frame-syntax.md), [Acknowledgements](../../protocol/acknowledgements.md), [Addressing](../../protocol/addressing.md), [ZigBee Interface](../../protocol/zigbee-interface.md) |
| Diagnostic address and detailed-read safety | [`DIMENSION 32`: Addressing](../../diagnostics/dim32-addressing.md), [`DIMENSION 35`: Configuration Parameters](../../diagnostics/dim35-configuration.md) |
| Programming prerequisites and effects | [Address Programming](../../programming/address-programming.md), [Configuration Programming](../../programming/configuration-programming.md), [Session Lifecycle](../../programming/session-lifecycle.md), [Programming Validation](../../programming/validation.md) |
| Functional conflicts and product scope | [Lighting `WHAT`](../../functional/who-1-lighting/what.md), [`WHO 6` L4686SDK](../../functional/who-6-basic-video-door-entry/), [Energy Management](../../functional/who-18-energy-management/), [Cross-database Functional Coverage](../../functional/cross-database-coverage.md) |
| Capability versus runtime behavior | [Scenario Categories and Matching](../../scenario-engine/categories-and-matching.md), [Scenario Execution Model](../../scenario-engine/execution-model.md), [Device Configuration](../../device-model/configuration.md) |

## 3. Resolved contradictions worth independently sampling

| Resolution | Sampling target |
| --- | --- |
| Replies need not repeat a request selector or address; exceptions remain system-scoped. | [Frame Syntax](../../protocol/frame-syntax.md), [Addressing](../../protocol/addressing.md) |
| `WHO 18` historical commands are the enumeration `57`, `58`, `59`, `510`, not an inclusive range. | [Energy Management Commands](../../functional/who-18-energy-management/what.md) |
| `DIMENSION 1.N_CONF` is the physical-configurator-position count; it is not an Object, Virgin Object, Firmware class, or generic Device class. | [Device Identity](../../diagnostics/dim1-device-identity.md), [Physical Devices](../../device-model/physical-devices.md) |
| Absence of a physical counterpart does not establish advanced-only support. | [Configuration](../../device-model/configuration.md), [`DIMENSION 35`](../../diagnostics/dim35-configuration.md) |
| Catalogue rows, registered management operations, and ScenarioDevices templates establish capability or implementation structure, not installed runtime support. | [MyHOME Suite `OPEN.db` Coverage](../../functional/open-db-coverage.md), [Scenario Execution Model](../../scenario-engine/execution-model.md) |
| `DIMENSION 38` Guide copies retain the canonical applicability and effect gate. | [canonical treatment](../../diagnostics/dim35-configuration.md#reading-detailed-parameters), [Program a Device](../../guides/program-device.md), [Verify Programming](../../guides/verify-programming.md) |
| L4686SDK send operations, receive-only notifications, broadcast sentinel `4100`, and acknowledgement meaning remain separate. | [`WHO 6` Basic Video Door Entry](../../functional/who-6-basic-video-door-entry/) |

## 4. Genuinely inaccessible or unresolved source areas

| Source area | State after Phase 8 |
| --- | --- |
| Sanitized primary captures and controlled Device/Firmware/gateway/transport experiments | Unavailable; private captures are intentionally excluded, and derived observations cannot be comprehensively replayed. |
| MyHOME Suite executable behavior | Application binaries/resources, query consumers, loader traces, UI traces, localization bundles, caching/migration behavior, and scenario persistence fixtures are unavailable. |
| Product hardware documentation | Original diagram editions and exact pages supporting physical-configurator and product-layout correlations are unavailable. |
| Published functional specifications | No dedicated stored public specification exists for `WHO 8`, `9`, `10`, `11`, `12`, `14`, `19`, `23`, `26`, `27`, or `99`; narrow implementation evidence does not replace one. |
| Detailed public-source inspection | Portions of the ZigBee and product-specific flows/diagrams remain unexamined; HMAC and retained functional contradictions lack independent adjudication. |
| ZigBee publication provenance | The document is fingerprinted and technically inspectable, but its acquisition/public-release chain remains unresolved because of its Confidential footers. |
| Runtime selection and encoding | Firmware-selection precedence, address-rule consumer behavior, `DIMENSION 310`, physical-to-advanced translation coverage, and scenario matching/loading remain unresolved where their canonical pages state so. |

## 5. Final ledger counts and deterministic-check results

| Measure | Final result |
| --- | ---: |
| Ledger findings | `60` |
| `Verified` | `44` |
| `Accepted evidence gap` | `10` |
| `Superseded` | `1` |
| `ASTRA-FINAL-REVIEW` | `4` |
| Remaining Open/Investigating/Remediation-ready/Fixed Blocking, Substantive, or Editorial findings | `0` |
| Phase 2 human pages | `138` |
| Phase 2 supporting pages | `15` |
| Phase 2 objective failures | `0` |
| Phase 2 review candidates | `34` |
| Markdown files checked for local links, fragments, headings, tables, and fences | `154` |
| Markdown link/structure failures | `0` |
| Drift-audit semantic candidates after classification | `51` |
