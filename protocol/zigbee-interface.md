# ZigBee OpenWebNet Interface

This page records the interface-specific boundary established by the supplied Legrand [ZigBee OpenWebNet Specification](../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0, 22 November 2016. It is specification evidence, not a tested interoperability claim. The document carries Confidential footers; its public-release provenance remains unresolved as recorded in the [Source-Coverage Audit](../project/review/phase-3-source-coverage.md).

## Transport and addressing

Section 2.3 specifies serial communication at 19200 baud, eight data bits, one stop bit, and no parity for the described interfaces. The TCP session selectors and authentication workflow documented elsewhere are not prerequisites established for this serial interface.

Section 3 retains the OpenWebNet delimiters and principal frame classes but defines its own `WHERE`:

| Form | Source meaning |
| --- | --- |
| `PRODUCT_DECIMAL` + `UNIT` + `#9` | Unicast; concatenate the decimal representation of the product's last four MAC-address bytes with the two-character unit, then append `#9` |
| `0#UNIT#9` | Broadcast to the selected unit; unit `00` selects all units |
| `#` transmission prefix | Multicast marked not implemented in this source revision |

These are symbolic forms, not observed installation identifiers. They are not SCS `A`/`PL` addresses. The suffix named `SYS` by this document is a `WHERE` family marker; it is not evidence for the numeric payload `SYS` in Suite `DIMENSION 32`. The four-byte address component does not by itself establish identity with the Suite diagnostic Physical Device ID namespace.

Section 3.3 limits broadcast sending to no more than one per second. Preserve this interface-specific constraint; do not infer a protocol-wide throughput limit.

## Acknowledgement behavior

Sections 3.6 through 3.9 define `ACK = *#*1##`, `NACK = *#*0##`, and `BUSY NACK = *#*6##`. For this interface the source says a BUSY NACK is followed by a NACK and instructs waiting 500 milliseconds before retrying the same frame. A receiver must retain that two-frame result rather than attributing the following NACK to a new command. This is not a generic retry rule for TCP gateways.

## Namespace and management boundaries

Section 3.1 lists `WHO 1`, `2`, `4`, `13`, `18`, `25`, and diagnostic `1000`. A shared `WHO` number does not establish identical operations, ranges, addressing, or support to the SCS-oriented references.

| Mechanism | Evidence and limit |
| --- | --- |
| Neighbor discovery | Section 5.3 uses `WHO 1000 DIMENSION 81`, including interface request `*#1000**81##`, indexed responses and final ACK. This is not Suite `DIMENSION 13` ID enumeration. |
| Interface/network management | Section 11 specifies `WHO 13` operations and firmware/hardware/product queries. These do not establish Suite interview or programming parity. |
| CEN+ binding | Section 13 includes OpenWebNet-visible binding operations under `WHO 25`; the SCS virtual-button grammar is not a complete account of this variant. |
| Firmware boundary | Version readout and boot-mode handoff are OpenWebNet-visible; a handoff is not evidence that the subsequent upload protocol is OpenWebNet. |

The complete detailed variant reference remains an integration backlog. This page establishes applicability and prevents reuse of incompatible SCS assumptions; it does not certify all listed operations or their full flows.

## Preserved source conflicts

| Question | Conflicting source locations | Current conclusion |
| --- | --- | --- |
| Automation UP value | PDF page 11 labels a `WHAT 2` example UP; page 38 assigns UP to `1` and DOWN to `2` | Preserve the conflict; do not use the example to redefine Automation direction. Applicable interface evidence is required. |
| Energy reset value | PDF page 53 summary gives `0`; the detailed reset frame uses `75` | Unresolved for this variant. SCS `WHAT 75` is not independent confirmation of the ZigBee operation. |

No private address from the source examples is reproduced here. Relevant inspected portions are sections 2.3, 3, 5.3 and the Phase 3 register for sections 11 through 13. Unexamined flows and Device behavior remain explicitly outside this assessment.
