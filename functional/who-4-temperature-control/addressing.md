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

**Dimensionless actuator status requests.** For the literal `*#4*2#1##` probe, nine of the 12 inspected firmware images return `NACK` with `silent`, `H4684` Firmware `020054` and `MH200` Firmware `020102` emit the local-zone-`2` status queries, and `MH202` Firmware `010024` records `reply=nack` and `verdict=crash` (also on `*#4*2#4#01##`). These results do not test every dimensionless `Z#N` address.

**Client guidance for the inspected implementations.** The recorded cases support preferring verified `DIMENSION 20` queries over the tested dimensionless actuator poll, and withholding outbound `#4#INTERFACE`-qualified `WHO 4` polls until support has been established for the intended gateway and address. The suite includes literal `*#4*2#1*20##` and `*#4*#0*20##` queries; the latter is an observed implementation form rather than a universal published address grammar. See the [actuator-status reference](dimensions.md#dimension-20---actuator-status) for the published `Z#N`, `Z#0` and `0#0` forms. This is client guidance derived from the named firmware versions and harness cases above, not a protocol-wide support guarantee. Physical bus forwarding, incoming events and uninspected versions remain untested; see the [evidence review](../../project/review/who4-gateway-routing-and-actuator-requests.md#client-guidance-interpretation).

## Four-zone central-unit (`#0#C`) addressing and gateway compatibility

Inspection and sanitized M16C/60 P-code execution of BTicino four-zone central-unit `4695` (`HC/HS/L/N/NT4695`, `AM5875`) Firmware `01.01.03` (`ThermorCentralUnit v01.01.03`, `LH4695_AM5875_010103.fwz`), paired with 13 gateway Firmwares, establish the SCS bus addressing boundaries for `#0#C`, `#Z#C`, `#Z`, and direct zone `Z` operations ([four-zone central-unit evidence review](../../project/review/who4-4695-four-zone-central-unit.md)). The 19 `own-firmware-oracle` gateway TSVs execute gateway Firmware against synthetic bus inputs or clean-room Python controller/probe models, while original `4695` controller execution is recorded separately in the [execution scope and retained `4695` P-code record](../../project/review/who4-4695-four-zone-central-unit.md#execution-scope-and-retained-4695-p-code-record).

**Base address and four-zone block.** In `4695` Firmware `01.01.03`, the configured `ZA` and `ZB` configurators set the unit's base zone number `C = ZA * 10 + ZB` (`1..99`, exposed on OpenWebNet as `#0#1..#0#99`; `1..96` when managing four consecutive zones `C..C+3`). On the SCS bus, `#0#C` status requests use `$04 99 <CU> 30 C0` (`*#4*#0#C##`, answered with `$18 D2 <CU> 03 04 C0 <B5> <B6> <B7>`), and `#0#C` commands use `$18 D1 <CU> 03 02 C1 <B5> <B6> <B7>` where `<CU>` is the two-digit hexadecimal byte representation of `C` (`01..63`, for example `01` for `#0#1` and `15` for `#0#21` at `ZA=2, ZB=1`).

**Built-in master probe (`Z = C`) versus external slave probes (`C+1..C+3`).** Zone `C` is the `4695` unit's internal built-in master probe, while zones `C+1..C+3` are external SCS slave probes. On incoming `$04` zone telegrams, `4695` Firmware `01.01.03` processes `$04 99` status and dimension reads (`DIMENSION 0`, `DIMENSION 12`, `DIMENSION 13`, and `DIMENSION 14`) and `$04 95` configuration telegrams, and ignores direct-zone write opcodes `$04 90`, `$04 91`, `$04 92`, and `$04 93` (produced by `*#4*Z*#14*T*M##` and `*4*WHAT*Z##`). Because no external slave probe occupies `Z = C`, direct zone writes targeting `Z = C` (for example `*#4*1*#14*0180*3##` or `*4*303*1##` on a `#0#1` unit) receive gateway `ACK` when transmitted as `$04 92 01 30 24` or `$04 93 01 30 0F` on Generation C and D gateways, yet leave `4695` Zone `C` state unchanged with zero SCS reply frames. External slave probes at `C+1..C+3` accept `$04 90..93` directly off the SCS bus and emit `$18 D2 <Z> 03 04 12 ...` (`DIMENSION 12`) and `$04 B7 <Z> 30 ...` (`WHAT`) broadcasts, which `4695` Firmware `01.01.03` ingests for its slave-zone state table.

**Absence of `#Z` and `#Z#C` central-zone writes (`B3=0x02, B4=0xC2`) on `4695` `01.01.03`.** Gateways encode 99-zone central-zone writes (`*#4*#Z*#14*T*M##`, `*4*303*#Z##`, `*4*311*#Z##`) as `$18 D1 00 03 02 C2 <Z> <B6> <B7>`, and Generation B, C, and D gateways encode four-zone `#Z#C` writes (`*#4*#Z#C*#14*T*M##`, `*4*303*#Z#C##`, `*4*311*#Z#C##`) as `$18 D1 <CU> 03 02 C2 <Z> <B6> <B7>` (and `*4*311*#0#C##` as `$18 D1 <CU> 03 02 C2 00 00 00`). In `4695` Firmware `01.01.03`, central address `00` (`#0` and `#Z`) fails the unit's own-address check (`B1 == C`), and the `$18` write dispatcher (`B3=0x02`) implements only `B4=0xC1` (central-unit commands) and `B4=0xBA`, ignoring `B4=0xC2` with zero SCS reply frames. Sub-command `0xC2` is implemented in `4695` Firmware `01.01.03` only as a read-only zone-configuration query under `B3=0x03` (`$18 D1 <CU> 03 03 C2 <Z> 00 00` from `*#4*#Z#C##`, answered with `$18 D2 <CU> 03 04 C2 <Z> <mode> <val>`). Historical touchscreen `#Z#C` write emission therefore reflects client-side framing rather than a write path supported by `4695` Firmware `01.01.03`.

**Actuator `DIMENSION 20` `#0#1` specification collision versus gateway decoding.** Although the published `WHO 4` v2.0.0 specification writes Master Pump Actuator `1` as `*#4*#0#1*20*V##` (creating a grammar collision with four-zone central-unit `WHERE = #0#1`), Generation B, C (`F454` `020051`, `F459` `020105`, `F450` `020010`, `MH202` `010024`), and D (`MyHomeServer1` `028206`, `F461` `020011`, `F460` `020012`, `3488` `030205`) gateway translators decode incoming `B7 80 31 01` as `*#4*0#1*20*0##`, `B7 00 31 01` as `*#4*100*20*0##`, and `B7 00 30 01` as `*#4*#0*20*0##`, while outbound `*#4*#0#1*20##` on Generation C and D (`F454`, `F459`, `F450`, `MyHomeServer1`, `F461`, `F460`, `3488`) transmits `A9 01 30 10` to query Zone `1` actuator `1#1` (`*#4*1#1*20*0##`). `MH202` `010024` is excluded from this outbound list: the retained `*#4*#0#1*20##` case returns `NACK` with no bus output. `4695` Firmware `01.01.03` drives its own actuators through `$04 BF` and `$04 BA` bus telegrams, which all 13 inspected gateways leave untranslated on the OpenWebNet socket.

**Four-generation gateway compatibility across 13 Firmwares.** Across the 13 inspected gateway Firmwares, `#0#C`, `#Z#C`, and direct `Z` translations partition into four distinct implementation generations:

| Generation | Inspected gateway Firmwares | Outbound `#0#C` (`*#4*#0#C##`, `*4*WHAT*#0#C##`, `*#4*#0#C*#14*T*M##`) | Inbound `#0#C` (`$18 D2 <CU> 03 04 C0 ...`) | Outbound `#Z#C` writes | Outbound direct `Z` writes (`*#4*Z*#14*T*M##`, `*4*303*Z##`) |
| --- | --- | --- | --- | --- | --- |
| Generation A | `MH200` `020102`, `H4684` `020054` | Collapses `#0#C` to `00` (`$04 99 00 30 C0`, `$18 D1 00 ...`; `NACK` on `1`, `0`, `103`, `203`, `311`); ignored by `4695` `01.01.03` | Strips `#C`, emitting `*4*WHAT*#0##` | Collapses `#Z#C` to `00` `C2`; ignored by `4695` `01.01.03` | `NACK` / `silent` (`*4*1*Z##` and `*4*0*Z##` also `NACK`) |
| Generation B | `MH200N` `010108`, `F453AV` `030014`, `F453` `010100` | Preserves `<CU>` (`01..63` hex for `1..99`); accepted by `4695` `01.01.03` | Preserves `*4*WHAT*#0#C##` | `ACK` / emits `$18 D1 <CU> 03 02 C2 ...`; ignored by `4695` `01.01.03` | `NACK` / `silent` on setpoint and `303`; `*4*1*1##` and `*4*0*1##` `ACK` and mis-emit `#0#1` season `$18 D1 01 03 02 C1 F0/F1 00` (`Z >= 2` `NACK`) |
| Generation C | `F454` `020051`, `F459` `020105`, `F450` `020010`, `MH202` `010024` | Preserves `<CU>` (`01..63` hex for `1..99`); accepted by `4695` `01.01.03` | Preserves `*4*WHAT*#0#C##` | `ACK` / emits `$18 D1 <CU> 03 02 C2 ...`; ignored by `4695` `01.01.03` | `ACK` / emits `$04 90..93 <Z> ...`; accepted by external slaves `C+1..C+3`, ignored by `4695` built-in Zone `C` |
| Generation D | `MyHomeServer1` `028206`, `F461` `020011`, `F460` `020012`, `3488` `030205` | Preserves `<CU>` (`01..63` hex for `1..99`); accepted by `4695` `01.01.03` | Preserves `*4*WHAT*#0#C##` | `out` (`NACK` without device TX-ACK) / emits `$18 D1 <CU> 03 02 C2 ...`; ignored by `4695` `01.01.03` | `ACK` (with slave TX-ACK) / emits `$04 90..93 <Z> ...`; accepted by external slaves `C+1..C+3`, ignored by `4695` built-in Zone `C` |
