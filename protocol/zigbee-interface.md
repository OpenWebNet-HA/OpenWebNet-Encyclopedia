# ZigBee OpenWebNet Interface

This page records the interface-specific boundary established by the supplied Legrand [ZigBee OpenWebNet Specification](../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0, 22 November 2016. It is specification evidence, not a tested interoperability claim. The document carries Confidential footers; its public-release provenance remains unresolved as recorded in the [Source-Coverage Audit](../project/review/phase-3-source-coverage.md).

## Transport and addressing

Section 2.3 specifies serial communication at 19200 baud, eight data bits, one stop bit, and no parity for the described interfaces. The same section says the USB interface can increase its baud rate up to 115200 baud, but it defines no OpenWebNet negotiation command, host-side selection procedure, or revision applicability for that higher rate. Treat 19200 baud as the documented base setting and 115200 baud as a source-stated optional USB capability, not a universal default. The TCP session selectors and authentication workflow documented elsewhere are not prerequisites established for this serial interface.

Section 3 retains the OpenWebNet delimiters and principal frame classes but defines its own `WHERE`:

| Form | Source meaning |
| --- | --- |
| `PRODUCT_DECIMAL` + `UNIT` + `#9` | Unicast; concatenate the decimal representation of the product's last four MAC-address bytes with the two-character unit, then append `#9` |
| `0#UNIT#9` | Broadcast to the selected unit; unit `00` selects all units |
| `#` transmission prefix | Multicast marked not implemented in this source revision |

These are symbolic forms, not observed installation identifiers. They are not SCS `A`/`PL` addresses. The suffix named `SYS` by this document is a `WHERE` family marker; it is not evidence for the numeric payload `SYS` in Suite `DIMENSION 32`. The four-byte address component does not by itself establish identity with the Suite diagnostic Physical Device ID namespace.

Section 3.3 limits broadcast sending to no more than one per second. It warns that exceeding this rate can saturate the ZigBee network and cause products to miss traffic during the following eight seconds. Preserve this interface-specific constraint; do not infer a protocol-wide throughput limit.

The source presents the abstract form `*WHO*WHAT*WHERE*WHEN##`, but section 3.5 explicitly states that `WHEN` is never used by this interface. Its operational command/status, request, parameterized `DIMENSION`, response/report, and write forms are instances of the canonical structures in [Frame Syntax](frame-syntax.md) and [`DIMENSION`](dimensions.md); ZigBee-specific `WHERE` parsing still follows the rules above.

Section 4 states that only products compatible with the source's ZigBee network 2.1 profile can be managed by this interface. This is an applicability limit of the documented interface revision, not evidence that all ZigBee products expose OpenWebNet.

## Acknowledgement behavior

Sections 3.6 through 3.9 define `ACK = *#*1##`, `NACK = *#*0##`, and `BUSY NACK = *#*6##`. For this interface the source says a BUSY NACK is followed by a NACK and instructs waiting 500 milliseconds before retrying the same frame. A receiver must retain that two-frame result rather than attributing the following NACK to a new command. This is not a generic retry rule for TCP gateways.

## Namespace and management boundaries

Section 3.1 lists `WHO 1`, `2`, `4`, `13`, `18`, `25`, and diagnostic `1000`. A shared `WHO` number does not establish identical operations, ranges, addressing, or support to the SCS-oriented references. The source's label "Diagnostic" for `WHO 1000` does not make its neighbor-table mechanism equivalent to the MyHOME Suite diagnostic families.

Canonical runtime semantics remain organized under the relevant functional namespace. The current owners are [`WHO 1`](../functional/who-1-lighting/), [`WHO 2`](../functional/who-2-automation/), [`WHO 4`](../functional/who-4-temperature-control/), [`WHO 13`](../functional/who-13-integration-gateway/), [`WHO 18`](../functional/who-18-energy-management/), and [`WHO 25`](../functional/who-25-transversal/). This interface page owns cross-cutting transport, addressing, acknowledgement behavior, discovery architecture, and applicability limits; it does not create a second set of functional command definitions.

| Mechanism | Evidence and limit |
| --- | --- |
| Neighbor discovery | Section 5.3 defines `WHO 1000 DIMENSION 81` as a router-neighbor traversal. Its detailed grammar and evidence limits are documented below. |
| Interface product inventory | Sections 5.4, 6, and 11 define `WHO 13` Scan and product-database operations. See [ZigBee Network Management](../functional/who-13-integration-gateway/zigbee-network-management.md). |
| Binding | Section 13 defines OpenWebNet-visible binding operations under `WHO 25`. See [ZigBee Binding](../functional/who-25-transversal/zigbee-binding.md); the SCS virtual-button grammar is not a complete account of this variant. |
| Firmware boundary | Version readout and boot-mode handoff are OpenWebNet-visible; a handoff is not evidence that the subsequent upload protocol is OpenWebNet. |

Detailed ZigBee semantics for `WHO 1`, `2`, `4`, `13`, `18`, and `25` are integrated under their canonical functional namespaces. The discovery architecture and `WHO 1000 DIMENSION 81` semantics are canonical on this page.

## Discovery and product inventory

ZigBee OpenWebNet version 4.0 exposes more than one way to learn about ZigBee products. The mechanisms are related by the installation they describe, but the source does not make their result sets interchangeable.

| Mechanism | What the source exposes | Persistence or reachability established |
| --- | --- | --- |
| `WHO 1000 DIMENSION 81` | neighbor information reported by the interface or an addressed ZigBee router | neighbor-table freshness, aging, and persistence are not defined |
| `WHO 13 WHAT 65` plus `DIMENSION 67`, `73`, and `66` | Scan plus the interface's stored product database and product-information queries | database persistence and stale-entry behavior are partly specified; current reachability is a separate question |
| MyHOME Suite diagnostic discovery | diagnostic-family enumeration and Physical Device interview, such as `WHO 1001 DIMENSION 13` | not established by this ZigBee interface specification |

The source describes two principal ZigBee product categories for this interface: `ZR` (ZigBee Router), described there as mains-powered, and `ZED` (ZigBee End Device), described there as battery-powered. These are source-defined ZigBee categories for the interface. They are not aliases for the encyclopedia's Physical Device, Module, Object, or catalogue entities.

### Neighbor discovery - `WHO 1000 DIMENSION 81`

**Evidence status:** specification evidence from section 5.3 of ZigBee OpenWebNet version 4.0. The source provides the complete illustrated exchange but does not provide a separate field-definition table for `DIMENSION 81`.

The documented first step queries the OpenWebNet ZigBee interface itself:

```text
Client -> ZigBee interface: *#1000**81##
ZigBee interface -> Client: *#1000**81#ROW*UNKNOWN*NEIGHBOR##
ZigBee interface -> Client: *#*1##
```

The response form is repeated once for each reported entry and a final `ACK` terminates the sequence. The symbolic fields above replace installation-derived identifiers from the source examples.

The documented second step queries each newly discovered router through the interface:

```text
Client -> ZigBee interface: *#1000*ROUTER00#9*81##
ZigBee interface -> Client: *#1000*ROUTER00#9*81#ROW*UNKNOWN*NEIGHBOR##
ZigBee interface -> Client: *#*1##
```

Here `ROUTER00#9` uses the source's ZigBee product-address form with Unit `00`. It selects the router whose neighbor information is being requested; it is not a MyHOME Suite Physical Device ID.

| Response element | Source-bounded interpretation |
| --- | --- |
| response `WHERE` | empty when the interface's own neighbors are returned; the addressed router `WHERE` when a router is queried |
| `ROW` | the example increments this field from zero for successive responses; the source does not name it or establish cursor, resume, persistence, or product-database-index semantics |
| `UNKNOWN` | an additional numeric response field whose meaning is not defined anywhere in the inspected source |
| `NEIGHBOR` | a returned ZigBee product-address component; the source uses a newly discovered router value to construct the next router-addressed request |
| final `ACK` | explicit end of that neighbor response sequence |

Calling the process recursive is a description of the client traversal, not terminology supplied by the specification. The source explicitly says that after querying the interface, the second step is to ask each newly discovered `ZR` for its neighbors, and it states that this sequence can obtain the products of the installation. The documented traversal therefore continues through newly discovered routers.

The documented procedure does not query `ZED` entries recursively. The source does not state that a `ZED` must reject `DIMENSION 81`; support for such a request is **Unknown**. No end-Device recursion should be inferred.

### Neighbor-table limits

The source calls the returned entries "known neighbors." It does not define neighbor-table freshness, aging, radio reachability criteria, or persistence. Therefore `DIMENSION 81` is established as a topology or neighbor-traversal mechanism, but it is **Unresolved** whether every returned entry is currently reachable at the instant of the query.

The source does not define a duplicate-elimination rule. In one router-addressed example, a returned neighbor identifier is equal to the queried router identifier. The source does not explain whether that is intended semantics, an example defect, or evidence about the unnamed fields. A client must not assume that `DIMENSION 81` yields a duplicate-free graph solely from this specification.

No `DIMENSION 81` maximum entry count, paging rule, request cursor, or numeric termination sentinel is specified. Completion is the final `ACK`. The interface-wide `NACK` and BUSY behavior described under [Acknowledgement behavior](#acknowledgement-behavior) remains applicable as general interface syntax, but section 5.3 assigns no `DIMENSION 81`-specific meaning to `NACK` or BUSY.

The product database's documented 175-product capacity does not establish a 175-entry limit for a neighbor response. These are separate mechanisms.

### Relationship to Scan and the product database

Section 5.4 presents `WHO 13 WHAT 65` Scan as another discovery sequence. Scan broadcasts over the ZigBee network so active routers and awake end Devices can answer. Approximately 13 seconds after an accepted Scan, the interface reports `DIMENSION 67`.

The detailed `WHO 13` definition makes an important distinction: the reported `DIMENSION 67` value is the number of products stored in the interface product database, not merely the number of active routers observed by that Scan. Indexed `DIMENSION 73` reads the stored product identifier and power category from that database, while `DIMENSION 66` can contact a product to retrieve Unit/end-point Device-ID information and can report that a stored product is unreachable.

These semantics are canonical in [ZigBee Network Management](../functional/who-13-integration-gateway/zigbee-network-management.md#scan-and-product-database). Neighbor discovery does not replace that inventory model, and product-database membership does not prove current reachability.

### Relationship to Suite diagnostics

The MyHOME Suite diagnostic workflows documented under [Diagnostics](../diagnostics/) use different management families, identifiers, enumeration operations, and Physical Device interview semantics. In particular, `WHO 1001 DIMENSION 13` Device-ID enumeration is not a renamed form of ZigBee `WHO 1000 DIMENSION 81`.

No inspected source establishes a mapping between ZigBee product identifiers, ZigBee product-database indexes, and MyHOME Suite Physical Device IDs. The three discovery/inventory surfaces must remain separate unless future evidence establishes a relationship.

## Preserved source conflicts

| Question | Conflicting source locations | Current conclusion |
| --- | --- | --- |
| Automation UP value | PDF page 11 labels a `WHAT 2` example UP; page 38 assigns UP to `1` and DOWN to `2` | Preserve the conflict; do not use the example to redefine Automation direction. Applicable interface evidence is required. |
| Energy reset value | PDF page 53 summary gives `0`; the detailed reset frame uses `75` | Unresolved for this variant. SCS `WHAT 75` is not independent confirmation of the ZigBee operation. |
| Energy Frequency/Energy mapping | PDF page 53 Frequency use case uses `DIMENSION 51`; pages 54-55 define `51` as Energy and `112` as Frequency | Preserve the conflict. The detailed table and definitions do not erase the contradictory use case. |

No private address from the source examples is reproduced here. Functional sections 8 through 13 have now received operation-level reconciliation for `WHO 1`, `2`, `4`, `13`, `18`, and `25`; their detailed evidence decisions are recorded in the [ZigBee Functional Reconciliation](../project/review/zigbee-functional-reconciliation.md) and the earlier [ZigBee Reconciliation Review](../project/review/zigbee-reconciliation.md). The `WHO 1000` discovery mechanism and sections 5 and 6 product-inventory flows are reconciled in [ZigBee Discovery and Inventory Reconciliation](../project/review/zigbee-discovery-inventory-reconciliation.md). The complete source-wide audit is recorded in the [ZigBee Final Source Completeness Certification](../project/review/zigbee-final-source-completeness-certification.md).
