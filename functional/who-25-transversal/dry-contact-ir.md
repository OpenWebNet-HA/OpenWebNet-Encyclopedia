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

## Gateway compatibility and hardware boundaries

Support for `WHO 25` dry-contact and IR operations follows the general `WHO 25` gateway boundary:

| Gateway model | `WHO 13 MODEL` | `WHO 25` dry contact / IR support | Behavior | Reference |
| --- | --- | :---: | --- | --- |
| MH200N (03565) | `200` | Supported | `ACK` / state response | Legrand WHO 25 v1.0.0, p. 13 |
| MH202 | `200` | Supported | `ACK` / state response | Legrand WHO 25 v1.0.0, p. 13 |
| F454 | `200` | Supported | `ACK` / state response | Legrand WHO 25 v1.0.0, p. 13 |
| MH200 (1st gen) | `4` | Unsupported | `NACK` (`*#*0##`) | Legrand WHO 25 v1.0.0, p. 13; empirical bench probe |

The legacy MH200 (Model 4) does not process `WHO 25` dry-contact status requests (`*#25*WHERE##`) or events; all `WHO 25` requests return `NACK` (`*#*0##`).

## Functional navigation

Dry contacts are indexed separately in [Functional Protocol](../README.md) so readers searching by function can reach this page directly while the canonical reference remains under `WHO 25`.