# Addressing

Temperature Control uses a zone/probe-oriented `WHERE` grammar rather than the `A`/`PL` grammar used by Lighting and Automation. Leading zeroes are significant because they distinguish address classes.

## Published functional `WHERE` forms

| Scope | Form | Meaning |
| --- | --- | --- |
| General probes | `0` | All probes |
| Master probe | `1..99` | Master probe of zone `1..99` |
| All probes in zone | `001..099` | Master and slave probes belonging to the selected zone |
| Individual probe | `PZZ` | Probe `P` (`1..8`) of zone `ZZ` (`01..99`) |
| Central unit | `#0` | Temperature Control central unit |
| Zone via central unit | `#1..#99` | Selected zone controlled through the central unit |

Examples of individual-probe encoding include `101` for probe 1 of zone 1, `801` for probe 8 of zone 1, and `899` for probe 8 of zone 99.

The forms `1` and `001` are therefore not equivalent: `1` selects the master probe of zone 1, whereas `001` selects all probes belonging to zone 1.

## MyHOME_Suite address rules

The MyHOME_Suite `OPEN.db` address-rule definitions represent Temperature Control through several operation-specific forms:

| Form | Purpose |
| --- | --- |
| `[ZA][ZB]` | Temperature Control zone |
| `[ZAZB]` | Advanced zone form |
| `#0#[ZA][ZB]` | Four-zone central-unit form |
| `[ZA][ZB]#[N]` | Temperature Control actuator instance |

These implementation forms complement the public functional grammar. The selected operation determines which rule is valid; clients must not normalize all Temperature Control `WHERE` values to one integer zone identifier.

The physical `ZA`/`ZB` positions identify the zone; actuator `N` and probe Slave numbering have separate roles. A numeric plug in a probe's `SLA` socket is distinct from the lettered `SLA` plug in `MOD`. See [Temperature Control configurators](../../device-model/configurators.md#temperature-control) for the manufacturer-defined count, numbering and product scopes.

## Actuator addressing

Actuator-oriented `DIMENSION` operations can append an actuator selector to the zone address. This is distinct from addressing a probe in the same zone and is used by operations such as actuator state reported by read-only `DIMENSION 20`. The public forms are `Z#N` for actuator `N` (`1..9`) in zone `Z` (`0..99`), `Z#0` for all actuators of a zone, and `0#0` for all actuators. Split control uses the additional prefix `3#Z#N` under `DIMENSION 22`.

## Central-unit addressing

A leading `#` identifies central-unit scope in the published functional grammar. `#0` addresses the central unit itself; `#N` addresses zone `N` through the central unit. Central-unit commands include zone mode changes, setpoint changes, program/scenario selection, and holiday operations.

## Historical central-unit variants

The BTouch source distinguishes 3550 (99-zone) and 4695 (four-zone) central units. The mature four-zone probe implementation composes a probe/zone address with a central selector, such as `23#1`, and writes a controlled setpoint through `#23#1`. These application variants must remain distinct from ordinary `#N` central-zone addressing.

The touchscreen Configuration parser selects the following command targets, with `Z` the configured zone and `C` the configured four-zone central selector:

| Operation | 99-zone Configuration | Four-zone Configuration |
| --- | --- | --- |
| Central-unit command | `#0` | `#0#C` |
| Controlled zone command / setpoint write | `#Z` | `#Z#C` |
| Fan-coil `DIMENSION 11` request / write | `Z` | `Z` |

The fan-coil target is passed separately from the composed central-zone address. These are [verified client mappings](../../project/review/myopencommunity-hvac-history-review.md#configuration-and-address-selection), not a universal address rewrite for every `WHO 4` operation. Basic IR air-conditioning actions use the separate [`WHO 0` scenario namespace](../who-0-scenarios/README.md#historical-touchscreen-behavior).

For the four-zone case where probe and central share an address, the source describes a missing setpoint-change notification after entering manual mode. The client schedules a setpoint read after 10 seconds if the report has not arrived. The affected Firmware revisions are not named. This workaround is implementation evidence, not a deadline or a defect established for every 4695. Older external-probe code describes addresses `x00` with `x = 1..9`; that historical rule does not override the exact test addresses used by the later [external-temperature operation](dimensions.md#historical-external-probe-dimension-15).

See [Temperature Control evidence](../../project/review/myopencommunity-integration.md#temperature-control).

See [`WHAT` Reference](what.md) for central-unit commands, [`DIMENSION` Reference](dimensions.md) for operation-specific payloads, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.

## Gateway firmware routing and actuator-request boundaries

**Local-bus `#4#INTERFACE` qualification.** In the pinned `own-firmware-oracle` `thermo-zone-requests` v3 suite at revision `de87a34e251b677a299917c98fcfcea3b409bf34` (`oracle_version=3`, full simulated-PIC harness, `reset=each` on `F450 020010` and `reset=0` on the other 11 targets, declared `settle_ms=3000`), none of the 12 emulated gateway Firmwares emits an interface-routed `$06EC` or `$06E4` SCS bus telegram on any of the nine `#4#INTERFACE`-qualified `WHO 4` status or dimension requests (`*#4*2#4#01##`, `*#4*2#4#12##`, `*#4*2#4#01*0##`, `*#4*2#4#01*11##`, `*#4*2#4#01*19##`, `*#4*2#4#01*20##`, `*#4*2#4#12*20##`, `*#4*2#1#4#01*20##`, `*#4*2#4#01*60##`):

| Gateway model | Firmware | `#4#INTERFACE` `WHO 4` request behavior | Dimensionless `*#4*2#1##` behavior | Original result |
| --- | --- | --- | --- | --- |
| F450 | `020010` | Truncates `*20` at `#` to local zone `2` (`$04A9023010`, `NACK` / `out`); `NACK` / `silent` on others | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F450/020010/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| F453 | `010100` | `NACK` / `silent` on all nine `#4#INTERFACE` requests | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F453/010100/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| F453AV | `030014` | `NACK` / `silent` on all nine `#4#INTERFACE` requests | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F453AV/030014/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| F454 | `020051` | Truncates `*20` at `#` to local zone `2` (`$04A9023010`, `NACK` / `out`); `NACK` / `silent` on others | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F454/020051/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| F459 | `020105` | Truncates `*20` and `*60` at `#` to local zone `2`; `NACK` / `silent` on others | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F459/020105/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| F460 | `020012` | Truncates `*20` and `*60` at `#` to local zone `2`; `NACK` / `silent` on others | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F460/020012/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| F461 | `020011` | Truncates `*20` and `*60` at `#` to local zone `2`; `NACK` / `silent` on others | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/F461/020011/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| H4684 | `020054` | Truncates status, `*0`, and `*19` at `#` to local zone `2`; `NACK` / `silent` on others | Truncates at `#` to local zone `2` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/H4684/020054/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| MH200 | `020102` | Truncates status, `*0`, and `*19` at `#` to local zone `2`; `NACK` / `silent` on others | Truncates at `#` to local zone `2` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/MH200/020102/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| MH200N | `010108` | `NACK` / `silent` on all nine `#4#INTERFACE` requests | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/MH200N/010108/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| MH202 | `010024` | Parses trailing `#4#01` on `*20` as local `Z=4, N=1` (`$0499843110`); `crash` on `*#4*2#4#01##`; `NACK` / `silent` on `#4#12` and others | `NACK` / `crash` (`coso` daemon exit) | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/MH202/010024/oracle/full/thermo-zone-requests.tsv#L21-L32) |
| MyHomeServer1 | `028206` | Truncates `*20` and `*60` at `#` to local zone `2`; `NACK` / `silent` on others | `NACK` / `silent` | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/de87a34e251b677a299917c98fcfcea3b409bf34/results/MyHomeServer1/028206/oracle/full/thermo-zone-requests.tsv#L21-L32) |

Recorded `out` verdicts on `#4#INTERFACE`-qualified `WHO 4` requests must therefore not be interpreted as local-bus interface forwarding: on `F450`, `F454`, `F459`, `F460`, `F461`, `H4684`, `MH200`, and `MyHomeServer1`, the recorded SCS bus bytes query local main-bus zone `2`, while on `MH202` Firmware `010024` both `*#4*2#4#01*20##` and `*#4*2#1#4#01*20##` read the trailing `#4` and `#01` tokens as local zone `4` actuator `1` (`$0499843110`) and reject `*#4*2#4#12*20##` (`NACK` / `silent`). Clients should withhold outbound `#4#INTERFACE`-qualified `WHO 4` status and dimension polls unless gateway support is explicitly established, while continuing to parse `#4#INTERFACE`-qualified `WHO 4` event frames received from the bus.

**Dimensionless actuator status requests.** Dimensionless `*#4*Z#N##` status requests are not supported across the 12 inspected Firmwares: nine return `NACK` with `silent`, `H4684` Firmware `020054` and `MH200` Firmware `020102` truncate `2#1` at `#` to poll local zone `2`, and `MH202` Firmware `010024` terminates its `coso` translator process (`reply=nack`, `verdict=crash`) on both `*#4*2#1##` and misparsed `*#4*2#4#01##` (while rejecting `*#4*2#4#12##` with `NACK` / `silent`). Clients querying actuator state must request `DIMENSION 20` (`*#4*Z#N*20##` or `*#4*#0*20##`; zone-level `*#4*Z*20##` is dropped on six of the 12 inspected Firmwares) rather than sending dimensionless `*#4*Z#N##`. These observations come from inspected emulator artifacts and do not establish physical SCS bus behavior or uninspected Firmware versions; see [WHO 4 gateway routing and actuator-request review](../../project/review/who4-gateway-routing-and-actuator-requests.md).
