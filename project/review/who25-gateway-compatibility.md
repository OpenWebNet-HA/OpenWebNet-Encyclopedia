# WHO 25 gateway compatibility evidence review

## Published specifications

The CEN/CEN+ specification version 1.0.0, SHA-256 `8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21`, page 24, was inspected for CEN+ availability and the separate CEN column. The dry-contact/IR specification version 1.0.0, SHA-256 `122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927`, page 13, was inspected independently for dry-contact/IR availability.

Both tables list MH200N and F453 as supporting their respective function, F453AV 1.0.19 as unsupported, F453AV / 573992 2.1.7 as supported, and MH200, F452V and F452 as unsupported. Firmware values absent from the source remain unspecified. The CEN/CEN+ table separately lists CEN support for MH200. These are published function-availability statements, not universal socket response or firmware implementation claims.

## Published oracle result inspection

Method: source inspection of published result TSVs at own-firmware-oracle revision `af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b`. No firmware was executed and no physical hardware was probed for this change. The existing recorded experiments are identified by their original image, executable and suite digests in the preserved headers.

Lines 18 and 19 record `*25*21#1*21##` and `*25*23#8*233##`, respectively. For both inputs, MH200N 010108, F454 020051 and MyHomeServer1 028206 record reply `nack` with verdict `out`; MH202 010024 records reply `ack` with verdict `silent`. The records declare the full harness, a simulated PIC responder and `settle_ms=300`; MH200N uses `reset=each`, and the other three use `reset=0`. The time field is preserved as a declared setting, not proof of a complete 300 ms observation.

| Gateway | Firmware | Original Git blob | Original SHA-256 | Preserved result |
| --- | --- | --- | --- | --- |
| MH200N | `010108` | `bd89265158fe1e3a28beac76a2a39ae8fe3c3c93` | `e11f9a28e6e3ca903af5cb839812816b69257b2c0ef8eb3145c98ba1d88ff135` | `project/review/fixtures/who25-gateway-compatibility/MH200N-010108.tsv` |
| F454 | `020051` | `4c590bc15fbb0250d26b59358325690c4b7931cc` | `c46b49618c6f62baa330f72053a5f80aaf69b6b2d1d4d476081a9b6c73b46cb5` | `project/review/fixtures/who25-gateway-compatibility/F454-020051.tsv` |
| MH202 | `010024` | `e777c742371bb16519a11bebb03086e2df7ce3ab` | `b21efb5cc3720f73c61a2055dbe4bdf620f1009f18068db5cc5bb937ffbe5fef` | `project/review/fixtures/who25-gateway-compatibility/MH202-010024.tsv` |
| MyHomeServer1 | `028206` | `a39d0d6b50ddb4f15f2596a658b8daee79416d43` | `e2bb2652ab49f0f793e65f346b98bd8fa7c56f5bc665d62851d0846de7c1436d` | `project/review/fixtures/who25-gateway-compatibility/MyHomeServer1-028206.tsv` |

The preserved files retain the original result bytes. Original immutable URLs are recorded in the Machine KB source registry and linked from the canonical CEN+ page. These results separate socket acknowledgement from recorded bus output. They neither establish physical execution nor imply namespace-wide acceptance/rejection, event forwarding, or status-query support.

## Missing physical bench evidence

No reviewed MH200 WHO 25 capture supports this change. Claims of immediate rejection on MH200 FW 2.1.0, rejection of every WHO 25 operation, or observed event suppression are omitted. The published lack of CEN+ and dry-contact/IR function availability remains documented. Historical ScenarioPlus documentation and its identities from current main are preserved; no MH200 ScenarioPlus runtime conclusion is added.

## Identity and claim review

Existing released section, chunk, claim and source identities from current main are retained. New gateway section identities avoid the historical ScenarioPlus/contact sections added since PR 49 was opened. New chunk, claim and artifact-source IDs are allocated above the current lifecycle inventory; artifact sources retain the numbered source-ID form used by registry consumers. The README gateway section is navigation only and is reviewed non-claim material; the two substantive compatibility sections have reviewed atomic claims. Existing CEN+ ACK statements are qualified as published sequences and cite the CEN/CEN+ specification rather than the dry-contact source entry. Affected source pins and context mappings are reviewed only within the edited WHO 25 pages.
