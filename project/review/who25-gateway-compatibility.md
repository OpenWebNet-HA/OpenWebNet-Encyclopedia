# WHO 25 gateway compatibility evidence review

## Published specifications

The CEN/CEN+ specification version 1.0.0, SHA-256 `8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21`, page 24, was inspected for CEN+ availability and the separate CEN column. The dry-contact/IR specification version 1.0.0, SHA-256 `122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927`, page 13, was inspected independently for dry-contact/IR availability.

Both tables list MH200N and F453 as supporting their respective function, F453AV 1.0.19 as unsupported, F453AV / 573992 2.1.7 as supported, and MH200, F452V and F452 as unsupported. Firmware values absent from the source remain unspecified. The CEN/CEN+ table separately lists CEN support for MH200. These are published function-availability statements, not universal socket response or firmware implementation claims.

## Historical oracle v1 result inspection

Method: source inspection of published result TSVs at own-firmware-oracle revision `af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b`. No firmware was executed and no physical hardware was probed for this change. The existing recorded experiments are identified by their original image, executable and suite digests in the preserved headers.

Lines 18 and 19 record `*25*21#1*21##` and `*25*23#8*233##`, respectively. For both inputs, MH200N 010108, F454 020051 and MyHomeServer1 028206 record reply `nack` with verdict `out`; MH202 010024 records reply `ack` with verdict `silent`. The records declare the full harness, a simulated PIC responder and `settle_ms=300`; MH200N uses `reset=each`, and the other three use `reset=0`. The time field is preserved as a declared setting, not proof of a complete 300 ms observation.

| Gateway | Firmware | Original Git blob | Original SHA-256 | Preserved result |
| --- | --- | --- | --- | --- |
| MH200N | `010108` | `bd89265158fe1e3a28beac76a2a39ae8fe3c3c93` | `e11f9a28e6e3ca903af5cb839812816b69257b2c0ef8eb3145c98ba1d88ff135` | `project/review/fixtures/who25-gateway-compatibility/MH200N-010108.tsv` |
| F454 | `020051` | `4c590bc15fbb0250d26b59358325690c4b7931cc` | `c46b49618c6f62baa330f72053a5f80aaf69b6b2d1d4d476081a9b6c73b46cb5` | `project/review/fixtures/who25-gateway-compatibility/F454-020051.tsv` |
| MH202 | `010024` | `e777c742371bb16519a11bebb03086e2df7ce3ab` | `b21efb5cc3720f73c61a2055dbe4bdf620f1009f18068db5cc5bb937ffbe5fef` | `project/review/fixtures/who25-gateway-compatibility/MH202-010024.tsv` |
| MyHomeServer1 | `028206` | `a39d0d6b50ddb4f15f2596a658b8daee79416d43` | `e2bb2652ab49f0f793e65f346b98bd8fa7c56f5bc665d62851d0846de7c1436d` | `project/review/fixtures/who25-gateway-compatibility/MyHomeServer1-028206.tsv` |

The preserved files retain the original result bytes. Original immutable URLs are recorded in the Machine KB source registry and linked from the canonical CEN+ page. These results separate socket acknowledgement from recorded bus output. They neither establish physical execution nor imply namespace-wide acceptance/rejection, event forwarding, or status-query support.

## Withdrawn physical capture

The contributor withdrew the 2026-10-17 physical-capture details because the underlying recording was not retained. Its 5–6 ms timing and event-window assertions are unsubstantiated and support no claims in this change. This withdrawal does not invalidate the separately pinned oracle v1 files, which remain historical harness records. The replacement capture below is the sole physical source used here.

## Identity and claim review

Existing released section, chunk, claim and source identities from current main are retained. New gateway section identities avoid the historical ScenarioPlus/contact sections added since PR 49 was opened. New chunk, claim and artifact-source IDs are allocated above the current lifecycle inventory; artifact sources retain the numbered source-ID form used by registry consumers. The README gateway section is navigation only and is reviewed non-claim material; the two substantive compatibility sections have reviewed atomic claims. Existing CEN+ ACK statements are qualified as published sequences and cite the CEN/CEN+ specification rather than the dry-contact source entry. Affected source pins and context mappings are reviewed only within the edited WHO 25 pages.

## Published oracle result inspection

The current comparison uses revision `8a61bbeb1d26354241debac84a7310142e5ab3a5` and six independently fingerprint-checked WHO 25 TSVs. Each observation remains limited to the two CEN+ inputs on lines 18 and 19. All six headers declare oracle version 3, the full simulated-PIC harness, reset 0 and settle_ms 3000. We inspected the published artifacts; no firmware was executed here. MH200 020102 records NACK/silent; MH200N 010108, F453 010100, F454 020051 and MH202 010024 record ACK/out with bus bytes; MyHomeServer1 028206 records NACK/out with bus bytes. The two MH200 firmware versions in this review are distinct: emulator 2.1.2 and physical capture 2.1.0.

| Gateway | Firmware | Original Git blob | Original SHA-256 | Preserved result |
| --- | --- | --- | --- | --- |
| MH200 | `020102` | `169ebf04e8934fb29b93ff585f96ef7271150f34` | `8895d1c545f80ae4c0177a6cc2ea135d7112b11983cc8875119f38a21100ba5e` | `project/review/fixtures/who25-gateway-compatibility/oracle-v3/MH200-020102.tsv` |
| MH200N | `010108` | `22568253f2f90aeb352f421ff3f52a55b88dafee` | `1dfd7a802bb2a763276187bc13649d7071deefb492f9a9f7a070957feef30148` | `project/review/fixtures/who25-gateway-compatibility/oracle-v3/MH200N-010108.tsv` |
| F453 | `010100` | `d4a3f0b4c77762f9301d5c04db34ef90bb481b8e` | `ac9d494099c530c5a8500d4cb74db6400add3ffe9f6862dadea0fdaccb01a6df` | `project/review/fixtures/who25-gateway-compatibility/oracle-v3/F453-010100.tsv` |
| F454 | `020051` | `dd9eebd6b5bb4792ef3f561fbebf44d1a7904d55` | `f6669f98ab5297be2ae36566138d360c1d0e5f2aa3e71fad493f5f248bd70ba1` | `project/review/fixtures/who25-gateway-compatibility/oracle-v3/F454-020051.tsv` |
| MH202 | `010024` | `c1e437f88708d28b9840720a759d829cd58f2020` | `53e76991e2324d02f101a1b66da692a450f5d0ba3274de76642debe0ab462fab` | `project/review/fixtures/who25-gateway-compatibility/oracle-v3/MH202-010024.tsv` |
| MyHomeServer1 | `028206` | `febe9c37b4358d61474d916b3e62c9f059dfe818` | `a444bf040cf2af9bd887a66251de4c90730e1d61f6940e767e2cea5e0643522f` | `project/review/fixtures/who25-gateway-compatibility/oracle-v3/MyHomeServer1-028206.tsv` |

The upstream responder acknowledgement and CPU-idle changes are published harness corrections, not new claims about physical gateway execution. The earlier v1 assertion records and sources retain their identities and are explicitly historical. The new v3 observations use new claim/source identities. The MH200 translator-registration explanation remains an inference from the published findings and results; the hashed private stack_open.xml contents were not inspected for this change. No direct static-analysis claim is added.

## Replacement physical capture inspection

The contributor's [replacement capture](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/pull/49#issuecomment-6336963459) includes four files whose declared byte lengths and SHA-256 values were independently checked. Its three-file package passes the repository evidence validator; its 47 normalized records match the 47 run-phase records of the 57-record raw timeline, including their session labels and rebased relative times. The original public raw-session-log.jsonl hash is `2300d334629ad0dc0f61377e0e91e1b22e11359eaf1279c3fa39dba44faacb28`. The separately posted [withdrawal](https://github.com/OpenWebNet-HA/OpenWebNet-Encyclopedia/pull/49#issuecomment-6336110877) is explicit provenance, not evidence for a physical claim.

The retained repository package is a derived privacy projection, not a byte-identical original. It removes authentication and all clock query/broadcast data, replaces the original installation/bus/gateway labels, retains the capture date without its wall-clock time, and substitutes synthetic WHERE 99 for the live lighting positive control. It preserves all eight WHO 25 command/reply pairs unchanged and retains fractional relative times plus session labels in session-log.jsonl. The projection manifest records every original fingerprint, omitted source sequence and retained-to-original line mapping without publishing the original installed address. No original capture file is copied into sources/ or published as a repository fixture.

Source inspection is the examination method, with public_capture provenance and observed status. We did not operate physical hardware or a firmware emulator. The physical finding is limited to the recorded MH200 2.1.0 setup, with no WHO 25 transmitter/interface configured. The two-second windows are declared by the contributor recipe; the raw log has no explicit final observation-end marker. The recorded absence of WHO 25 event frames does not establish rejection of incoming hardware events or absence of physical bus forwarding.

| Literal probe | Recorded NACK latency (ms) |
| --- | ---: |
| `*25*21#1*21##` | 57.430 |
| `*25*11#0*11##` | 25.392 |
| `*#25*21##` | 19.576 |
| `*25*11#121*10##` | 23.398 |
| `*25*12*131##` | 34.942 |
| `*25*23#8*233##` | 24.200 |
| `*25*31#1*339##` | 39.486 |
| `*25*32#1*33##` | 14.686 |

The WHAT 31/32 labels preserve the published ON/OFF meanings. The CEN+ virtual Objects are 1 for WHERE 21 and 33 for WHERE 233. The dry-contact WHERE 339 probe is outside the published address forms, and the remaining unconfigured probes establish only literal socket responses, not valid-target or capability tests. No unsupported namespace-wide, immediate-NACK, event-suppression or all-firmware assertion is added.
