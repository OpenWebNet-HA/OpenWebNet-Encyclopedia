# `WHO 4` `DIMENSION 19`, `DIMENSION 20`, and `#20` Output Codes - Evidence Review

This review records the published specification boundary, live sanitized plant capture evidence, and static gateway-firmware analysis for `WHO 4` (Temperature Control) actuator output codes on `DIMENSION 19` (`CV` / `HV`), `DIMENSION 20`, and `#20`. It preserves the strict separation required by the [Encyclopedia Core Values](../encyclopedia-core-values.md): published specification text is never retrofitted with undocumented firmware or observed plant values.

## Published Specification Baseline

The published specification (`ownkb:source:s000138`, OpenWebNet Temperature Control `WHO 4` v2.0.0) defines discrete output codes `0..8` on both `DIMENSION 19` (valves `CV` and `HV`) and `DIMENSION 20` (actuator status), and adds `9` (`fan-coil ON`) in the `DIMENSION 20` text while classifying `DIMENSION 20` as read-only in the functional table. See [dimensions.md](../../functional/who-4-temperature-control/dimensions.md#dimension-20---actuator-status).

The published PDF does not document discrete codes `10..22`, proportional codes `100..200`, `9` on `DIMENSION 19`, or `#20` dimension write frames.

## Live Sanitized Capture Inspection

One sanitized live capture (`public_capture`, `git_file` source) establishes how a live `MyHomeServer1` gateway running firmware `2.87.13` emits `#20` and `20` frames for fan-coil and non-fan-coil actuators:

| Source metadata | Value |
| --- | --- |
| Repository | `OpenWebNet-HA/MyHOME` |
| Commit | `3590d0fabce43f8bccc52c804d32749d0bbfe7a1` |
| Path | `tests/fixtures/traces/issue_908/myhome_trace_MyHomeServer1_fancoil_dim20_100_2026-11-14.json` |
| Git blob | `9b450640c11ed6194c20ff6cb5ee7020570dce25` |
| SHA-256 | `2ae9b60d22a30d5dc7a5e8eb91450637922935c699b0256503c122cb44b6a346` |
| Line count | `1729` |
| Gateway model / firmware | `MyHomeServer1` / `2.87.13` |

Verified `rx` frames in that capture:

| Line span | Frame | Semantic role in capture |
| --- | --- | --- |
| `1183..1194` | `*#4*1#3*#20*100##` | Spontaneous `#20` dimension write reporting `100` (`0%` proportional 0-10 V idle/OFF) for zone `1`, actuator `3` |
| `1195..1207` | `*#4*1#3*20*100##` | `DIMENSION 20` status reply reporting `100` for zone `1`, actuator `3`, 282.792 ms after its `#20` frame |
| `1208..1220` | `*#4*2#3*#20*100##` | Spontaneous `#20` dimension write reporting `100` for zone `2`, actuator `3` |
| `1221..1233` | `*#4*2#3*20*100##` | `DIMENSION 20` status reply reporting `100` 24.241 ms after line `1208..1220` |
| `1234..1246` | `*#4*2#3*20*100##` | Subsequent `DIMENSION 20` status reply reporting `100` for `2#3` |
| `1625..1636` | `*#4*2#1*#20*0##` | Spontaneous `#20` dimension write reporting `0` (`OFF`) for zone `2`, actuator `1` |
| `1637..1649` | `*#4*2#1*20*0##` | Paired `DIMENSION 20` status reply reporting `0` (`OFF`) for `2#1`, 17.264 ms after its `#20` frame |

The wider retained-payload audit below found no `14..16`, `101..200`, `10..13` or `17..22` in its examined non-synthetic datasets. This result is limited to the recorded inventory and revisions, not all live or bench captures. The `1#3` write/status interval is 282.792 ms and the `2#3` interval is 24.241 ms; 46.353 ms separates the `1#3` status from the next `2#3` write, which concerns a different actuator. The earlier ~45 ms assertion was incorrect; the source does not establish a universal response-time guarantee.

## Inspected Gateway Firmware Binaries

Static inspection (`static_firmware_analysis`, `firmware_interface`) covers seven extracted gateway binaries across five gateway platforms. Raw ELF addresses, code offsets, and disassembly instructions are withheld per publication hygiene; each finding is pinned to the full immutable binary SHA-256.

| Gateway model | Firmware version | Binary filename | SHA-256 |
| --- | --- | --- | --- |
| `MH200N` | `010108` | `bt_termo` | `fa2e45e707b1a6d6ce31d04a54490e1ec7453bd2932b44aba23fc5bfeeac2b4c` |
| `F454` | `020051` | `bt_termo` | `d2c9f8e5f62d45e836f5b52780f8353d89cad57acd40540f6852b3be5461870f` |
| `MH202` | `010024` | `libplug_thermo_tr.so` | `5e2da864f01b19f4f14dde76e11786234b36c97f4f6778966d6a32f597d1452b` |
| `MyHomeServer1` | `028206` | `bt_termo` | `ef2054ede288b166d5c8ea1e8951316b0172691f47f36181c2bb998caa1c45c6` |
| `MyHomeServer1` | `028206` | `bt_thermo_manager` | `f4bd0eb5af3c7e0fb18722eabfa3a87dcc1d79fb1a836479363eedff361e3c66` |
| `MyHomeServer1` | `028206` | `bt_thermo_central_unit` | `ab8fb396e52bbba43908b71328865b1abbb202c9f5925e0552efd8a57ee01911` |
| `F461` | `020011` | `bt_termo` | `23958a97b4808421de65c13ab254bc76c0f68b10416e3c6f24b9adb108bcf29f` |

## Discrete Output-Code Tables and Active-State Bitmasks

### Baseline 14-Entry Table (`0..13`) Across All Five Gateways

In `MH200N` (`010108`), `F454` (`020051`), `MH202` (`010024`), `MyHomeServer1` (`028206`), and `F461` (`020011`), the SCS-to-OpenWebNet discrete lookup table maps 14 SCS actuator byte values (`0..13`) on both `DIMENSION 19` (`CV` / `HV`) and `DIMENSION 20` (including code `9` on `DIMENSION 19` as well as `DIMENSION 20`):

| OpenWebNet code | SCS byte | Classification / status |
| --- | --- | --- |
| `0` | `'01'` | Published: OFF (valve / actuator OFF) |
| `1` | `'00'` | Published: ON (valve / actuator ON) |
| `2` | `'10'` | Published: Opened |
| `3` | `'11'` | Published: Closed |
| `4` | `'12'` | Published: Stop |
| `5` | `'20'` | Published: OFF - fan coil |
| `6` | `'21'` | Published: ON - speed 1 |
| `7` | `'22'` | Published: ON - speed 2 |
| `8` | `'23'` | Published: ON - speed 3 |
| `9` | `'2F'` | Published on `DIMENSION 20`: ON - fan coil; firmware emits on `DIMENSION 19` and `DIMENSION 20` in all five gateways |
| `10` | `'30'` | Firmware discrete slot; catalogue/actuator label unresolved |
| `11` | `'31'` | Firmware discrete slot; catalogue/actuator label unresolved |
| `12` | `'32'` | Firmware discrete slot; catalogue/actuator label unresolved |
| `13` | `'3F'` | Firmware discrete slot; catalogue/actuator label unresolved |

### Extended 23-Entry Table (`0..22`) on `MyHomeServer1` and `F461`

`MyHomeServer1` (`028206` `bt_termo`) and `F461` (`020011` `bt_termo`) expand the discrete lookup table to 23 entries (`0..22`) across `DIMENSION 19`, `DIMENSION 20`, and `#20`:

| OpenWebNet code | SCS byte | Classification / status |
| --- | --- | --- |
| `14` | `'24'` | Extended fan-coil OFF speed 1 (firmware-verified; inactive in `bt_thermo_manager`) |
| `15` | `'25'` | Extended fan-coil OFF speed 2 (firmware-verified; inactive in `bt_thermo_manager`) |
| `16` | `'26'` | Extended fan-coil OFF speed 3 (firmware-verified; inactive in `bt_thermo_manager`) |
| `17` | `'40'` | Firmware discrete slot; catalogue/actuator label unresolved (inactive in `bt_thermo_manager` and `bt_thermo_central_unit`) |
| `18` | `'41'` | Firmware discrete slot; catalogue/actuator label unresolved (active in `bt_thermo_manager`) |
| `19` | `'42'` | Firmware discrete slot; catalogue/actuator label unresolved (active in `bt_thermo_manager`) |
| `20` | `'43'` | Firmware discrete slot; catalogue/actuator label unresolved (active in `bt_thermo_manager`) |
| `21` | `'44'` | Firmware discrete slot; catalogue/actuator label unresolved (active in `bt_thermo_manager`) |
| `22` | `'45'` | Firmware discrete slot; catalogue/actuator label unresolved (active in `bt_thermo_manager`) |

### `MyHomeServer1` (`028206`) Active vs. Inactive Classification

Inside `MyHomeServer1` (`028206`):

- `bt_thermo_manager` classifies `{0, 3, 5, 13, 14, 15, 16, 17, 100}` as inactive and `{1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 101..200}` as active.
- `bt_thermo_central_unit` classifies `{0, 3, 5, 13, 17, 100}` as inactive (omitting `14..16` from its inactive set relative to `bt_thermo_manager`) and treats `101..200` as active (`1%..100%`).
- Code `4` (`Stop`) lies in the active set rather than the inactive mask in `bt_thermo_manager` (and is omitted from the inactive mask in `bt_thermo_central_unit`), which differs from client heuristics that collapse `Stop` to an idle HVAC action.

## Proportional `0-10 V` Output Codes (`100..200`)

Across gateways supporting proportional `0-10 V` actuator feedback, SCS bus bytes `0x80..0xE4` (encoding `0%..100%` as `0x80 + pct`) map to OpenWebNet output codes `100..200` (`100 + pct`). Gateway emission behavior varies across platforms:

| Gateway model | Firmware | Proportional `100..200` behavior |
| --- | --- | --- |
| `MH200N` | `010108` | Unsupported; drops SCS bytes `0x80..0xE4` |
| `F454` | `020051` | Emitted on `DIMENSION 20` only; dropped on `DIMENSION 19` |
| `MH202` | `010024` | Emitted on `DIMENSION 20` only; dropped on `DIMENSION 19` |
| `MyHomeServer1` | `028206` | Emitted on `DIMENSION 19` (`CV` / `HV`), `DIMENSION 20`, and `#20` |
| `F461` | `020011` | Emitted on `DIMENSION 19` (`CV` / `HV`), `DIMENSION 20`, and `#20` |

In `MyHomeServer1` (`028206`), `bt_thermo_manager` emits `*#4*Z#N*#20*200##` for `100%` and `*#4*Z#N*#20*100##` for `0%`, and compares proportional fan-coil speeds against `speed_pct + 100`. Both `bt_thermo_manager` and `bt_thermo_central_unit` classify `100` as inactive (`0%`) and `101..200` as active (`1%..100%`).

## Unresolved Catalogue Labels and Client Boundaries

1. **Unresolved discrete labels (`10..13`, `17..22`)**: Static firmware inspection recovers the SCS byte mapping and active/inactive polarity (`13` and `17` inactive; `10..12` and `18..22` active in `bt_thermo_manager`), but neither the published `WHO 4` PDF nor live captures identify the physical actuator states or catalogue names for `'30'..'32'`, `'3F'`, or `'40'..'45'`. These remain `unresolved`.
2. **Unmapped ranges (`23..99` and `> 200`) and empty-field `DIMENSION 19` emission (`*#4*1*19*0*##`)**: None of the five inspected gateway firmwares map `23..99` or values above `200` in the `DIMENSION 19` / `DIMENSION 20` / `#20` output tables. For an SCS byte outside both the discrete table and `0x80..0xE4` (such as `0x46`, `0x7F`, or `0xE5`), `DIMENSION 20` emits no frame on any of the five gateways, and `MH200N` (`010108`), `F454` (`020051`), and `MH202` (`010024`) abort translation and emit no frame on `DIMENSION 19`. In `MyHomeServer1` (`028206` `bt_termo`) and `F461` (`020011` `bt_termo`), however, the missed `CV` or `HV` table loop falls through with that side's string buffer left empty and still formats `*#4*WHERE*19*CV*HV##`, emitting a frame with an empty value field (for example `*#4*1*19*0*##` when `CV` maps to `0` and `HV` is `0x46`, `0x7F`, or `0xE5`). A reader of `DIMENSION 19` on `MyHomeServer1` or `F461` can therefore meet an empty value field when an out-of-table SCS byte arrives.
3. **Live-plant coverage gap (`14..16`, `101..200`, `10..13`, `17..22`)**: Only `100` (and `0`) among the non-published or extended codes have been observed in sanitized live captures (`MyHomeServer1` `2.87.13`). Extended fan-coil OFF codes `14..16` (present in `OpenWebNet-HA/MyHOME` only in the oracle-built fixture `issue_908/myhome_trace_oracle_myhomeserver1_extended_fancoil_off_14_16.json`), proportional active values `101..200`, and discrete codes `10..13` and `17..22` remain firmware-verified only, without retained live-plant capture confirmation.
4. **Protocol write classification**: The `WHO 4` v2.0.0 PDF classifies `DIMENSION 20` as read-only; observed `#20` write and `20` status pairs on `MyHomeServer1` (`2.87.13`) must not be generalized into universal `#20` commandability across gateways or actuators.


## Wider retained-capture corpus audit

A read-only audit on 21 November 2026 records the exact repository revisions, every selected path, Git blob, SHA-256, classification and payload counts in [the retained-corpus inventory](who4-output-capture-corpus-2026-11-21.json). The [audit helper](checks/audit_who4_output_capture_corpus.py) reproduces the inventory from clean checkouts at its pinned revisions; no raw log lines or device metadata are copied here.

| Retained material | Immutable revision | Examined scope | Result for `10..13`, `14..16`, `17..22`, `101..200` |
| --- | --- | --- | --- |
| `OpenWebNet-HA/MyHOME` `v2-phase1-architecture` | `a881a4be711e7b8f03f044505c3810cfffcad403` | 201 retained fixture/log files: 123 capture-labelled, 69 other retained fixture/log files, 9 synthetic/oracle files; metadata prose is excluded from parsed payloads, with a separate lexical cross-check | No occurrences in the 192 non-synthetic files (2,341 output-payload occurrences); synthetic/oracle expectations are counted separately |
| `OpenWebNet-HA/OWNd` | `d04e453ea99b2b5dcaf36b2bfccc073eda522c48` | `tests/test_f461_live_plant.py` `GATEWAY_FRAMES`, lines 32..68; subsequent unit assertions are not capture evidence | No occurrences in the 11 retained output payloads |

The audit also inventories 272 MyHOME and 91 OWNd unit/golden context files separately. Those expectations do contain extended/proportional examples and cannot establish physical observations. Counts are literal retained occurrences, not independent events; logs/exports can duplicate observations. Origins are those described by the retained sources, not a new physical certification. Here, the non-synthetic inventory means files not marked synthetic/oracle: it includes the 69 origin-uncertified fixture/log files and does not certify them as physical captures. The absence is also confirmed by the full-text range cross-check in each selected file, avoiding a conclusion based solely on one JSON shape.

The retained F461 `2.0.11` `GATEWAY_FRAMES` excerpt includes gateway-emitted `#20` frames with `0`, `1`, `5` and `8`. Thus the earlier open question about whether such frames occur outside MyHomeServer1 is already answered for this F461 capture. A separate question remains whether a particular gateway accepts a client-originated `#20` command; received gateway frames alone do not establish that capability.

The Oracle repository was also inspected at `3c1634b00f8b165d1f63ddd4289171a9826ff501`. Its `f461-bench` / `mh200-bench` files are virtual plant configurations and simulator case sequences, with emulator result TSVs. The repository README explicitly distinguishes these virtual traces from physical plant captures. The inventory records 922 Oracle input/result/context files separately; none is promoted to a new physical observation. This inspection did not identify the separately named raw bench-capture archive.

The separately mentioned `own-bench-captures` material was not available to this audit and is explicitly outside its claim. Deleted/history-only files, other branches/revisions, unretained traffic and future captures are also outside scope. No firmware binary was reanalysed or executed, and no hardware was operated. The existing static table evidence is reused for `c003276` with exact MyHomeServer1 `028206` / F461 `020011` scope; this is a provenance repair, not a claim of new disassembly.

Reproduce after checking out the two pinned revisions:

```sh
python3 -B project/review/checks/audit_who4_output_capture_corpus.py --myhome /path/to/MyHOME --ownd /path/to/OWNd --oracle /path/to/own-firmware-oracle --output /tmp/who4-corpus-audit.json
```
