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

## Functional navigation

Dry contacts are indexed separately in [Functional Protocol](../README.md) so readers searching by function can reach this page directly while the canonical reference remains under `WHO 25`.