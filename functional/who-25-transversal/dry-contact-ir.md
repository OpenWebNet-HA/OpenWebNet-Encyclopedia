# Dry Contact and IR

Dry-contact and IR functions are carried within the `WHO 25` namespace while remaining functionally distinct from CEN+.

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `31` | ON / IR detection |
| `32` | OFF / IR not detected or end of detection |

The parameter following `WHAT` distinguishes state reporting from a system event/action context:

| Parameter | Meaning |
| ---: | --- |
| `0` | State returned by a request |
| `1` | State associated with an event/action |

Command/event forms therefore include `*25*31#1*WHERE##` and `*25*32#1*WHERE##`. A state request uses `*#25*WHERE##`; the response uses `*25*VALUE#0*WHERE##`, where `VALUE` is `31` for ON / IR detection or `32` for OFF / no detection.

## `WHERE`

Two published address forms are established:

| `WHERE` | Application |
| --- | --- |
| `1..201` | Automation dry-contact interfaces configured using Virtual Configurator Software |
| `[1-9][1-9]` | Alarm dry-contact interfaces and IR devices configured using physical `Z` and `N` configurators |

The published device families include automation dry-contact interfaces such as 3477/F428 and alarm/IR interfaces such as 3480/F482 and IR detector families.

## Historical contact interpretation

BTicino `PPTStatDevice` tests at `TS10_1_0_23` interpret `31#0` and `31#1` as contact closed, and `32#0` and `32#1` as contact open, and emit `*#25*WHERE##` for status. The 2009 implementation history explicitly corrects an earlier reversed interpretation. This corroborates the contact branch of the published ON/OFF model; it does not invert or redefine IR detection. See [Transversal evidence](../../project/review/myopencommunity-integration.md#transversal-functions).

The client combines replies and events into one local boolean; its `DIM_STATUS` identifier is not a wire `DIMENSION`. It compares numeric addresses and forwards repeated decoded values. That matching behavior does not establish leading-zero normalization, routed contact support or a wider address domain.

BtExperience selects this `WHO 25` receiver for its Automation contact Objects, preserving the configured `WHERE`. Its displayed state starts locally as inactive and emits a change notification only when the boolean changes. The initial display therefore is not a confirmed contact reading, and the change-only notification policy does not redefine bus events. See [Contact-client evidence](../../project/review/myopencommunity-cen-history-review.md#contact-receipt-and-product-state).

## Gateway compatibility and hardware boundaries

**Published protocol.** The [dry-contact/IR specification](https://archive.openwebnet-ha.org/sha256/12/2d/122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927.pdf), version `1.0.0`, page 13, lists the following availability for dry-contact and IR state functions. Firmware marked “not stated” remains unspecified in that table.

| Gateway model | Firmware in source | Published dry-contact / IR support |
| --- | --- | --- |
| MH200 | Not stated | No |
| MH200N / 03565 | Not stated | Yes |
| F453AV | `1.0.19` | No |
| F453AV / 573992 | `2.1.7` | Yes |
| F453 | Not stated | Yes |
| F452V | Not stated | No |
| F452 | Not stated | No |

This source does not list MH202, F454 or MyHomeServer1. Their absence from this historical table is not a finding of incompatibility. Published dry-contact/IR availability does not establish the reply to every `WHO 25` request or support for the separate CEN+ and ScenarioPlus families. See [CEN+ gateway compatibility](cen-plus.md#gateway-compatibility-and-hardware-boundaries) for the CEN+ specification and the scoped replay observations; the replay comparison there covers CEN+ commands, not dry-contact state queries.

**Physical MH200 capture inspection.** The [2026-10-22 capture](../../evidence/cap-mh200-who25-boundary-20261022/manifest.json) records NACK on MH200 firmware 2.1.0 for literal status request `*#25*21##` after 19.576 ms, `*25*31#1*339##` after 39.486 ms, and `*25*32#1*33##` after 14.686 ms. No dry-contact/IR interface was installed or configured. These are literal probe results: `WHERE 339` is outside the published address forms above, and none of the replies alone establishes a valid configured Device response or a gateway-wide rejection rule. The WHAT meanings remain 31 for ON/detection and 32 for OFF/no detection. Incoming physical WHO 25 events and physical bus forwarding were not tested.

## Functional navigation

Dry contacts are indexed separately in [Functional Protocol](../README.md) so readers searching by function can reach this page directly while the canonical reference remains under `WHO 25`.
