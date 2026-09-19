# Functional Source Coverage

The functional reference combines several evidence classes. They answer different questions and must not be treated as interchangeable.

| Evidence class | Establishes | Does not establish by itself |
| --- | --- | --- |
| Public `WHO` specification | Published wire grammar, values, ranges, and examples for that namespace | Device-specific support or later implementation extensions |
| `OWN_Intro_ENG.pdf` | Common syntax, sessions, and the contemporary namespace summary | Complete semantics for every listed `WHO` |
| `OPEN.db` | MyHOME Suite namespace identity, diagnostic-family mapping, address rules, and associated management templates | Complete ordinary functional vocabulary |
| ScenarioDevices databases | Functional actions exposed by the scenario engine and their concrete frames where present | Every legal command or a universal Device capability |
| `MHCatalogue.db` | Physical Device, firmware, Module, Object, and configuration applicability | A complete functional command registry |
| Observed traffic | Behavior of the captured Device/gateway/software version | Universal behavior outside the observed conditions |

## Public specification coverage

| `WHO` | Public source in the corpus | Coverage consequence |
| ---: | --- | --- |
| `0` | `WHO_0.pdf` | Dedicated scenario-module grammar |
| `1` | `WHO_1.pdf` | Dedicated Lighting grammar |
| `2` | `WHO_2.pdf` | Dedicated Automation grammar |
| `3` | `WHO_3.pdf` | Dedicated load-management grammar |
| `4` | `WHO_4.pdf` | Dedicated Temperature Control grammar |
| `5` | `WHO_5.pdf` | Dedicated Alarm grammar |
| `6` | `WHO_6_L4686SDK.pdf` | Product-specific SDK surface; not automatically a complete generic `WHO 6` specification |
| `7` | `WHO_7.pdf` | Dedicated Multimedia grammar |
| `13` | `WHO_13.pdf` | Gateway-management grammar; `OPEN.db` additionally establishes integration-interface use |
| `15`, `25` | `WHO_15-25.pdf` | CEN and CEN+ interaction grammar |
| `16` | `WHO_16.pdf` | Sound-system grammar |
| `17` | `WHO_17.pdf` | Scenario-management grammar |
| `18` | `WHO_18.pdf` | Energy Management grammar |
| `22` | `WHO_22.pdf` | Sound Diffusion / Multimedia grammar |
| `24` | `WHO_24.pdf` | Lighting Management grammar |
| `25` | `WHO_25.pdf` | Dry-contact and IR state functions |

The corpus contains no dedicated public functional specification for `WHO 8`, `9`, `10`, `11`, `12`, `14`, `19`, `23`, `26`, `27`, or `99`. Their pages must therefore distinguish namespace identity and narrow implementation evidence from a complete grammar.

The [ZigBee Interface Specification](../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0, is also relevant to Protocol, Diagnostics, Programming boundaries, and functional `WHO 1`, `2`, `4`, `13`, `18`, and `25`. It describes a particular Legrand serial interface, not a universal replacement for the SCS-oriented references. The [ZigBee Interface](../protocol/zigbee-interface.md) owns cross-cutting transport, addressing, acknowledgement, and applicability. Operation-level ZigBee references are integrated for [Lighting](who-1-lighting/zigbee-variant.md), [Automation](who-2-automation/zigbee-variant.md), [Temperature Control](who-4-temperature-control/zigbee-variant.md), [Network Management](who-13-integration-gateway/zigbee-network-management.md), [Energy Management](who-18-energy-management/zigbee-variant.md), and [Binding](who-25-transversal/zigbee-binding.md). These pages are source-bounded to the version 4.0 specification and do not establish universal product support. The source's publication status also requires the [Source Provenance Qualification](../sources/openwebnet-public/README.md). `WHO 1000 DIMENSION 81` discovery and the sections 5-6 product-inventory flows are reconciled in the [ZigBee Discovery and Inventory Reconciliation](../project/review/zigbee-discovery-inventory-reconciliation.md). The final source-to-documentation audit is recorded in the [ZigBee Final Source Completeness Certification](../project/review/zigbee-final-source-completeness-certification.md). See the [Phase 3 Source-Coverage Audit](../project/review/phase-3-source-coverage.md), [ZigBee Reconciliation Review](../project/review/zigbee-reconciliation.md), [ZigBee Functional Reconciliation](../project/review/zigbee-functional-reconciliation.md), and the Step 2 review for inspection scope, source conflicts, and rejected or unresolved claims.

## Implementation-only enrichment

Notable relationships established outside the public functional PDFs include:

- `WHO 14` lock/unlock frames from ScenarioDevices;
- target-dependent ScenarioDevices labeling of `WHO 1 / WHAT 17`;
- MyHOME Suite action templates for `WHO 4 DIMENSION 7`, local control, and fan-coil writes;
- `OPEN.db` management/address models for functional families `1/2`, `4`, `8`, `13`, `18`, `23`, and `27`;
- diagnostic-family assignments such as `1001`, `1004`, `1008`, `1013`, `1018`, `1023`, and `1027`.

These additions should be labelled as implementation evidence. A diagnostic-family association does not copy diagnostic `WHAT` or `DIMENSION` semantics into the functional namespace.

## Absence rules

- No public page means “not established by the current public corpus,” not “the function does not exist.”
- No `AS_OPEN_SYSTEM` association means `OPEN.db` does not supply a concrete operation for that system; it is not proof that the system has no functional frames.
- A generic parameterized template does not establish the meaning of each substituted value.
- A ScenarioDevices row with a null or symbolic `Frame` establishes application capability, not a wire mapping.

See [MyHOME Suite `OPEN.db` Coverage](open-db-coverage.md), [Cross-database functional coverage](cross-database-coverage.md), and [Evidence and Confidence](../reverse-engineering/evidence-and-confidence.md).
