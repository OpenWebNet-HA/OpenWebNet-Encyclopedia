# `DIMENSION` Reference

`WHO 13` uses `DIMENSION` frames to expose properties of the external interface / gateway. The published specification explicitly identifies whether each property is readable or writable.

| `DIMENSION` | Property | Access | Payload |
| ---: | --- | --- | --- |
| `0` | Time | R/W | `H*M*S*T` |
| `1` | Date | R/W | `W*D*M*Y` |
| `10` | IP address | R | `IP1*IP2*IP3*IP4` |
| `11` | Netmask | R | `MASK1*MASK2*MASK3*MASK4` |
| `12` | MAC address | R | `MAC1*MAC2*MAC3*MAC4*MAC5*MAC6` |
| `15` | Device type / model | R | `MODEL` |
| `16` | Firmware version | R | `V*R*B` |
| `19` | Uptime | R | `D*H*M*S` |
| `22` | Date and time | R/W | `H*M*S*T*W*D*M*Y` |
| `23` | Kernel version | R | `V*R*B` |
| `24` | Distribution version | R | `V*R*B` |

## Read form

The request uses the normal `DIMENSION` form with the gateway `WHERE` field empty:

`*#13**DIMENSION##`

The gateway returns the same `DIMENSION` followed by its values:

`*#13**DIMENSION*VALUE1*...*VALUEn##`

The published command-session examples show the response followed by `ACK`. The same value frame can also be emitted to a monitor session.

## Write form

Writable properties use the `#DIMENSION` form:

`*#13**#DIMENSION*VALUE1*...*VALUEn##`

The published writable set is limited to `DIMENSION 0`, `1`, and `22`.

## `DIMENSION 0` — Time

Payload: `H*M*S*T`.

| Field | Meaning | Encoding |
| --- | --- | --- |
| `H` | Hour | two digits, `00`–`23` |
| `M` | Minute | two digits, `00`–`59` |
| `S` | Second | two digits, `00`–`59` |
| `T` | Time zone | three digits, sign + hour offset |

For `T`, the first digit encodes the sign: `0` for a positive offset and `1` for a negative offset. The remaining two digits encode the hour offset. The published examples therefore interpret `001` as GMT+1 and `102` as GMT-2.

Read: `*#13**0##`.

Write: `*#13**#0*H*M*S*T##`.

## `DIMENSION 1` — Date

Payload: `W*D*M*Y`.

| Field | Meaning | Encoding |
| --- | --- | --- |
| `W` | Day of week | `00` Sunday through `06` Saturday |
| `D` | Day | `01`–`31` |
| `M` | Month | `01`–`12` |
| `Y` | Year | four digits |

Read: `*#13**1##`.

Write: `*#13**#1*W*D*M*Y##`.

## `DIMENSION 10` — IP address

Payload: four decimal octets: `IP1*IP2*IP3*IP4`.

A gateway at `192.168.10.1`, for example, reports the values as `192*168*10*1` rather than as a dotted string.

## `DIMENSION 11` — Netmask

Payload: four decimal octets: `MASK1*MASK2*MASK3*MASK4`.

A netmask of `255.255.255.0` is therefore represented as `255*255*255*0`.

## `DIMENSION 12` — MAC address

Payload: six values: `MAC1*MAC2*MAC3*MAC4*MAC5*MAC6`.

The published specification requires the six octets to be carried as decimal values, not hexadecimal text. A parser should therefore preserve the numeric octets and format a conventional hexadecimal MAC address only at the presentation layer.

## `DIMENSION 15` — Device type

The published model table defines these values:

| `MODEL` | Gateway model |
| ---: | --- |
| `2` | MHServer |
| `4` | MH200 |
| `6` | F452 |
| `7` | F452V |
| `11` | MHServer2 |
| `13` | H4684 |

This table describes the models defined by the published specification. It should not be treated as an exhaustive list of every later OpenWebNet gateway implementation.

## `DIMENSION 16` — Firmware version

Payload: `V*R*B`, where `V` is version, `R` release, and `B` build. The specification describes this as the version of the device software implementing the OpenWebNet server.

## `DIMENSION 19` — Uptime

Payload: `D*H*M*S`, representing elapsed time since the last gateway start-up.

| Field | Meaning | Published encoding |
| --- | --- | --- |
| `D` | Days | two digits, `00`–`31` |
| `H` | Hours | two digits, `00`–`23` |
| `M` | Minutes | two digits, `00`–`59` |
| `S` | Seconds | two digits, `00`–`59` |

## `DIMENSION 22` — Date and time

Payload: `H*M*S*T*W*D*M*Y`. It combines the complete payloads of `DIMENSION 0` and `DIMENSION 1` and is both readable and writable.

Read: `*#13**22##`.

Write: `*#13**#22*H*M*S*T*W*D*M*Y##`.

For clock synchronisation, this combined operation avoids separate time and date transactions.

## `DIMENSION 23` — Kernel version

Payload: `V*R*B`, with version, release, and build components.

This is distinct from `DIMENSION 16`: `16` identifies the OpenWebNet server/device firmware, while `23` reports the underlying kernel version.

## `DIMENSION 24` — Distribution version

Payload: `V*R*B`, with version, release, and build components.

Together, `DIMENSION 16`, `23`, and `24` expose three distinct software layers: gateway/OpenWebNet firmware, kernel, and operating-system distribution.