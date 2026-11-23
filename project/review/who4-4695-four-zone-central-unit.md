# `WHO 4` Four-Zone Central Unit (`4695`) and Gateway Compatibility - Evidence Review

This review records the published specification boundary, static and deterministic P-code inspection of BTicino four-zone central-unit `4695` (`HC/HS/L/N/NT4695`, `AM5875`) Firmware `01.01.03` (`ThermorCentralUnit v01.01.03`), and 13-gateway `own-firmware-oracle` execution for `WHO 4` (Temperature Control) four-zone central-unit (`#0#C`), central-zone (`#Z`, `#Z#C`), and direct zone (`Z`) operations. It preserves the strict separation required by the [Encyclopedia Core Values](../encyclopedia-core-values.md): published specification pages are kept distinct from implementation-scoped Firmware evidence.

## Published Specification and Catalogue Baseline

The published `WHO 4` v2.0.0 specification (`ownkb:source:s000138`) documents `#0` for the 99-zone central unit and `#1..#99` for zones addressed through the central unit, without specifying `#0#C` or `#Z#C`. Separately, MyHOME_Suite 3.5.38 `OPEN.db` (`ownkb:source:s000125`) defines Virtual address rule `#0#[ZA][ZB]` and Advanced address rule `#0#[ZAZB]` (`01..99`) for the four-zone control-unit target class, and BTicino Technical Guide `U1809C` (`ownkb:source:s000319`, [`OWN-DEV-0017`](../../devices/definitions/own-dev-0017-flush-mounted-temperature-central-unit.md)) documents that `4695` manages four consecutive zones starting at `ZA`/`ZB` (including `ZA=2, ZB=1` managing zones `21..24`) and houses the Zone 1 temperature probe internally. Historical BTouch touchscreen client code emits `#0#C` for central-unit commands and `#Z#C` for controlled-zone writes ([`WHO 4` Addressing](../../functional/who-4-temperature-control/addressing.md#historical-central-unit-variants)).

## Inspected `4695` Central-Unit Firmware Artifact

Static inspection (`static_firmware_analysis`, `firmware_interface`) and deterministic Renesas M16C/60 P-code execution (`M16C/60:LE:16:default`) cover the vendor `ThermorCentralUnit v01.01.03` Firmware update archive (`LH4695_AM5875_010103.fwz`). Raw Flash/RAM offsets and disassembly instructions are withheld per publication hygiene; each finding is pinned to the full immutable artifact SHA-256:

| Artifact | Size (bytes) | SHA-256 | Role |
| --- | ---: | --- | --- |
| `LH4695_AM5875_010103.fwz` | `109864` | `b01630d5f4d4fb45ee3392279635cde4e3575778fe69afae505d71a7c211a3be` | Vendor `.fwz` archive (`[ARTICOLO]=LH4695`, `[ARTICOLO2]=AM5875`, `[FW_VER]=010103`) |
| `info.txt` | `188` | `6d71fe6e03f38ceaafc3f28e41a2fce5be774ed34c78413d518d8318a931c1b3` | Embedded package metadata (`[TYPE]=FILE MITSUBISHI`, `[EXT]=mot`) |
| `4695_010103.mot` | `350878` | `3a760549e6c9b376308e29a1a6b46f5bb8f57a1b6f2715fff2f063324588ed01` | Motorola S-Record image (`7638` `S2` 24-bit records, all checksums valid) |
| `flat_0E0000_0FFFFF.bin` | `131072` | `254e3daed3534a4bcbf31a42534f75c3a8148e4e65fdcbcd0ea73aa4c16c91e9` | Canonical `0xFF`-padded 128 KB M16C/60 Flash image |

## Inspected Gateway Firmware Binaries and `own-firmware-oracle` Suites

Thirteen gateway Firmware images and their `WHO 4` translators were inspected (`static_firmware_analysis`, `firmware_interface`) and executed in `OpenWebNet-HA/own-firmware-oracle` at revision `0819306b866e99e4472cfa5b6acebfff4f1d9047` (`oracle_version=3`, stateless `oracle/cases/thermo-four-zone-central.cases` with `81` steps and `suite_sha256` `fb5095d09c78753cd3909431989650e986cecce36f661356d50a2c6ceb960c0d`, plus closed-loop `oracle/plant_cases/plant-cu4695.seq` with `37` steps, `suite_sha256` `7c9c0e5fdbdd51b5ea416505f83082769120cb8183d050370055adf1369b4fc7`, and `oracle/plant/fixtures/cu4695.yaml` `plant_sha256` `cc56acd2db907083f1b54e6c2aa0b26823e358ff5ad923ac2559d39adb1b0dc9`):

| Generation | Gateway model | Firmware | Translator binary | Translator SHA-256 |
| --- | --- | --- | --- | --- |
| Generation A | `MH200` | `020102` | `bt_termo` | `33ddcc24da367192b303202314f0c9ec82bf9280da44045a2983a137a0c1d4f9` |
| Generation A | `H4684` | `020054` | `bt_termo` | `c21fceaaefd9e19601ecc3f959e88ebdb8f506e02b81d99dfcead502adbaa143` |
| Generation B | `MH200N` | `010108` | `bt_termo` | `fa2e45e707b1a6d6ce31d04a54490e1ec7453bd2932b44aba23fc5bfeeac2b4c` |
| Generation B | `F453AV` | `030014` | `bt_termo` | `45d4c4529876dd7e64bac2153382f138005838f186a26955c7c563ec6ec6a3e0` |
| Generation B | `F453` | `010100` | `bt_termo` | `b28d02b1ec8ac565bc23c6c621d2b1d4a791c67c8f2bc2c1924e671198f6590f` |
| Generation C | `F454` | `020051` | `bt_termo` | `d2c9f8e5f62d45e836f5b52780f8353d89cad57acd40540f6852b3be5461870f` |
| Generation C | `F459` | `020105` | `bt_termo` | `7925ff014a6708a4591fe6c7241ee004ae840589c9c97e86e0ad5c222f0c2a69` |
| Generation C | `F450` | `020010` | `bt_termo` | `963cf11bddd078a8e2ad86c8d98efd0136f1cf83c3c79792064eb834f087cd3d` |
| Generation C | `MH202` | `010024` | `coso` | `6865c2d1d441d25effa31275080ded70ad3538a8a49288e3002ffb196b066175` |
| Generation D | `MyHomeServer1` | `028206` | `bt_termo` | `ef2054ede288b166d5c8ea1e8951316b0172691f47f36181c2bb998caa1c45c6` |
| Generation D | `F461` | `020011` | `bt_termo` | `23958a97b4808421de65c13ab254bc76c0f68b10416e3c6f24b9adb108bcf29f` |
| Generation D | `F460` | `020012` | `bt_termo` | `8df7400eb9364f77a23c9ca170b2238586e95ecb12acc32591177cd7b1c7b0d5` |
| Generation D | `3488` | `030205` | `bt_termo` | `f755a29d1d6604b215d34925fcf23e9b270e6ad4cf86d840c0565db5ee1af25d` |

Pinned `own-firmware-oracle` result TSVs (`public_experiment`, `git_file` at revision `0819306b866e99e4472cfa5b6acebfff4f1d9047`):

| Source ID | Gateway | Firmware | Suite | Lines | Original Git blob | Original SHA-256 | Inspected path |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| `ownkb:source:s001236` | `3488` | `030205` | `thermo-four-zone-central` | `96` | `f1f989a00a2c9b681dca575ad3f6d53035331c87` | `2e87074243efa97cefa83bb656a8634fc8286ca99728125f17d5a7c3469d3c0d` | `results/3488/030205/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001237` | `F450` | `020010` | `thermo-four-zone-central` | `96` | `2e841ab16a748c93ab58f0522d512f153b3aec05` | `268532d27f5ef0918178766b14c505091cfda0e2b628f08af485e03401a8b2b3` | `results/F450/020010/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001238` | `F453` | `010100` | `thermo-four-zone-central` | `96` | `875f49dabaf44fc079e16dc3a308329cc684ae97` | `3426ae269b4ba51e2b5b11b488371c3c1b29b9058edd959bfd8fc9f855298357` | `results/F453/010100/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001239` | `F453AV` | `030014` | `thermo-four-zone-central` | `96` | `fde940d53f53c7422036d7b2912df3a6a6296871` | `5ac99895c22cc3746012ac66f258c284926ca1b32027fbe025411bc1263c5038` | `results/F453AV/030014/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001240` | `F454` | `020051` | `thermo-four-zone-central` | `96` | `f11c69377ba41f3854f5b6e775c3ed9d7b1be098` | `1e57f2225d97fb6af2e52e883b8f78e5ed67b5759799151d4af74d239154f66e` | `results/F454/020051/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001241` | `F454` | `020051` | `plant-cu4695` | `53` | `5817df3f62630f27f19318edacacf8ed833f17bd` | `691e53d1ca31614b34589cafb29419fb866a16c36f70236905a80e9a7d91462a` | `results/F454/020051/oracle/plant-cu4695/plant-cu4695.tsv` |
| `ownkb:source:s001242` | `F459` | `020105` | `thermo-four-zone-central` | `96` | `cf7310e6cae9584deb23dd4d3767a3e3f5db3c9e` | `d25c6ff5335b535dbea83452ed7996d7bbd9b45f8c2df7a16fe137af48e5c5a5` | `results/F459/020105/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001243` | `F460` | `020012` | `thermo-four-zone-central` | `96` | `82aa7f072baa5dbfbd8d5e3177654c372cbc6dff` | `b454166c5fa0c035d1b180ab216bfafc2fe7c8fde3ff19118fb438bf66dab8df` | `results/F460/020012/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001244` | `F461` | `020011` | `thermo-four-zone-central` | `96` | `7d1a49c7a84de1a2ff022ea0ec5408e86f4d2bd0` | `837ca3a6a04d36e4d1a13721bfdfb35f9826531d9f8e27ce510ad9a39df7f834` | `results/F461/020011/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001245` | `F461` | `020011` | `plant-cu4695` | `53` | `6f3d8bf25e72713eeddb263ac1cb7b7cc775f2ba` | `dcaa94a093ea85c7b873fa538b1bf5101524449772c90ec2aaf619aa13ebfd51` | `results/F461/020011/oracle/plant-cu4695/plant-cu4695.tsv` |
| `ownkb:source:s001246` | `H4684` | `020054` | `thermo-four-zone-central` | `96` | `8677a15977bb47682652e46a17971a34b0fc4e86` | `bf61b419340502b29f9fe8edde941960881861d95e373238422ba1fdc0384fea` | `results/H4684/020054/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001247` | `H4684` | `020054` | `plant-cu4695` | `53` | `cd89e35e7096e491f78731be5fbc58693f4ee10b` | `d1337f815934f35e7a2bb806329992e8180514ca80413804c1247bd2c2ea8831` | `results/H4684/020054/oracle/plant-cu4695/plant-cu4695.tsv` |
| `ownkb:source:s001248` | `MH200` | `020102` | `thermo-four-zone-central` | `96` | `4c5886d93792511c3a8f0f83bc73350ea9364de6` | `2cae97ab622a6cf17ed02fda5871238254928f1438834dba4ac3c43120e5954b` | `results/MH200/020102/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001249` | `MH200` | `020102` | `plant-cu4695` | `53` | `48d84ef253a81a2d6eb48964eb1eb907657a8a2a` | `5de451690b1622b4092098ae923f69ed6e63e28420978371df07cc2ed7ba1f74` | `results/MH200/020102/oracle/plant-cu4695/plant-cu4695.tsv` |
| `ownkb:source:s001250` | `MH200N` | `010108` | `thermo-four-zone-central` | `96` | `af66f6a4926e819ca775eb9882051126bdd7c05a` | `9c9950a201b6a131ef7217144caf5ddccd88573ff2aef51cf8e4754c9e4668e1` | `results/MH200N/010108/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001251` | `MH200N` | `010108` | `plant-cu4695` | `53` | `965e8071c59772cf8832a7e344f0cf7c5850b3ab` | `538aa0c6720d35c60c2ab4d69744bfd7f86ed9ee22df6345b90564b693ce0ba7` | `results/MH200N/010108/oracle/plant-cu4695/plant-cu4695.tsv` |
| `ownkb:source:s001252` | `MH202` | `010024` | `thermo-four-zone-central` | `96` | `186742ab40a6d9666acf0c08511da3cb07e75ec8` | `249346855b6772318242c8acfb991a47b4064f8e3a0adaf9bfd7773c24df3ecf` | `results/MH202/010024/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001253` | `MyHomeServer1` | `028206` | `thermo-four-zone-central` | `96` | `f85876dd42949435c8e8fbd6280834cd741b795f` | `be23dc9ddb2109086fcf405d4f4e6fe17d28a760fbce8bd17b0b21bdf3dc0f79` | `results/MyHomeServer1/028206/oracle/full/thermo-four-zone-central.tsv` |
| `ownkb:source:s001254` | `MyHomeServer1` | `028206` | `plant-cu4695` | `53` | `7bf0df2d7fdad24381cd417bea93dd44eb166314` | `f4b7190b610d502895f46051a7a8bfe0040f9d837b01dc202985dbfe4ac8ae06` | `results/MyHomeServer1/028206/oracle/plant-cu4695/plant-cu4695.tsv` |

## Addressing, Built-In Zone `C`, and `C2` Write Absence

1. **Base address `C = ZA * 10 + ZB` (`#0#1..#0#99`)**: `4695` Firmware `01.01.03` derives its base address `C = ZA * 10 + ZB` (`1..99`, encoded on the SCS bus as hexadecimal byte `<CU> = 0x01..0x63`, for example `0x01` for `#0#1` and `0x15` for `#0#21`) and manages the four consecutive zones `C..C+3` (`1..96` when all four zones fall within `1..99`). Broadcast central address `00` (`#0` and `#Z`) fails the unit's own-address check (`B1 == C`) and is ignored.
2. **Built-in master probe (`Z = C`) versus external slave probes (`C+1..C+3`)**: On incoming `$04` short telegrams, `4695` Firmware `01.01.03` handles `$04 99` status/dimension reads and `$04 95` configuration telegrams, and drops `$04 90`, `$04 91`, `$04 92`, and `$04 93` direct-zone setpoint and mode writes. Because Zone `C` is internal to `4695` with no external slave probe at `Z = C`, direct zone writes targeting `Z = C` (`*#4*C*#14*T*M##`, `*4*303*C##`) produce no state change or SCS reply on `4695`, whereas external slave probes at `C+1..C+3` accept `$04 90..93` on Generation C and D gateways and broadcast `$18 D2 <Z> 03 04 12 ...` (`DIMENSION 12`) and `$04 B7 <Z> 30 ...` (`WHAT`) updates.
3. **Unimplemented `B3=0x02, B4=0xC2` write path**: All 13 gateways encode `#Z` writes (`*#4*#Z*#14*T*M##`, `*4*303*#Z##`, `*4*311*#Z##`) with `B1=0x00, B3=0x02, B4=0xC2`, and Generation B, C, and D gateways encode `#Z#C` writes (`*#4*#Z#C*#14*T*M##`, `*4*303*#Z#C##`, `*4*311*#Z#C##`) and `*4*311*#0#C##` with `B1=<CU>, B3=0x02, B4=0xC2`. `4695` Firmware `01.01.03` implements only `B4=0xC1` and `B4=0xBA` under `B3=0x02`, dropping all `B4=0xC2` writes (`TX=[]`); `0xC2` is implemented solely as a read-only query under `B3=0x03` (`*#4*#Z#C##` -> `$18 D1 <CU> 03 03 C2 <Z> 00 00` -> `$18 D2 <CU> 03 04 C2 <Z> <mode> <val>`).
4. **Actuator `DIMENSION 20` `#0#1` specification collision versus gateway decoding**: Although published `WHO 4` v2.0.0 documentation (`ownkb:claim:c003280`) writes Master Pump Actuator `1` as `*#4*#0#1*20*V##` (colliding lexically with `#0#1`), Generation B, C, and D gateway translators decode incoming `B7 80 31 01` as `*#4*0#1*20*0##`, `B7 00 31 01` as `*#4*100*20*0##`, and `B7 00 30 01` as `*#4*#0*20*0##`, while outbound `*#4*#0#1*20##` on Generation C and D (`F454`, `F459`, `F450`, `MyHomeServer1`, `F461`, `F460`, `3488`) transmits `A9 01 30 10` (`*#4*1#1*20*0##`). `4695` Firmware `01.01.03` instead transmits actuator commands on `$04 BF` and `$04 BA`, which all 13 gateways leave untranslated (`silent`).
5. **Four-generation gateway matrix**:
   - **Generation A (`MH200 020102`, `H4684 020054`)**: Collapses outbound `#0#C` and `#Z#C` to `00` (dropped by `4695`), `NACK`s `*4*1*#0#1##`, `*4*0*#0#1##`, `*4*103*#0#1##`, `*4*203*#0#1##`, `*4*311*#0#1##`, and all direct `Z` writes, and strips `#C` on inbound `D2 <CU> 03 04 C0/C2` frames (`*4*WHAT*#0##`).
   - **Generation B (`MH200N 010108`, `F453AV 030014`, `F453 010100`)**: Preserves `#0#C` outbound and inbound, `NACK`s direct `Z` setpoint and `303`/`102`/`202`/`302` writes (`*#4*Z*#14*T*M##`, `*4*303*Z##`), and mis-translates `*4*1*1##` and `*4*0*1##` into central `#0#1` season commands (`$18 D1 01 03 02 C1 F0/F1 00 00`, while `NACK`ing `Z >= 2`). Because `4695` also drops `#Z` and `#Z#C` writes, individual slave zones behind Generation B gateways cannot be overridden separately via OpenWebNet.
   - **Generation C (`F454 020051`, `F459 020105`, `F450 020010`, `MH202 010024`)**: Preserves `#0#C` and translates direct `Z` writes (`$04 90..93 <Z> ...`), while rejecting `*#4*#0#C*14##`, `*#4*#0#C*12##`, and `*#4*#0#C*0##` with `NACK`.
   - **Generation D (`MyHomeServer1 028206`, `F461 020011`, `F460 020012`, `3488 030205`)**: Matches Generation C on `#0#C` and direct `Z` writes (requiring bus device TX-ACK for `ACK` on writes), and additionally forwards `*#4*#0#C*14##` as `$04 99 <CU> 30 0E` (local Zone `C` `DIMENSION 14` read).

## `WHAT` Commands, Season Transitions, and `C0` Status Flags on `#0#C`

In `4695` Firmware `01.01.03`, `$18 D1 <CU> 03 02 C1 <B5> <B6> <B7>` applies a season filter on `B5 & 0xF0` (`0x10` accepted only in Heating, `0x20` accepted only in Cooling, `0x00` accepted in both seasons, `0xF0`/`0xF1` routed to season selection) before dispatching `B5 & 0x0F`:

| `B5` (hex) | `B6` (hex) | OpenWebNet command (Gen B/C/D) | `4695` `01.01.03` action and `C0` report |
| --- | --- | --- | --- |
| `01` / `11` / `21` | `00..02` | `*4*3101..3103*#0#C##`, `*4*1101..1103*#0#C##`, `*4*2101..2103*#0#C##` | Selects weekly program `1..3` (subject to `11`/`21` season filter); broadcasts `C0 11/21 00..02 <flags>` (`*4*110P/210P*#0#C##`) |
| `01` | `FF` | `*4*3100*#0#C##` | Resumes stored active weekly program `1..3` in both seasons; broadcasts `C0 11/21 <prog> <flags>` |
| `02` / `12` / `22` | `0A..46` | `*#4*#0#C*#14*T*3/1/2##` | Sets manual setpoint `5.0..35.0 °C` (`B6 = T_celsius * 2 <= 0x46`, subject to `12`/`22` season filter; `35.5..40.0 °C` `0x47..0x50` dropped with `TX=[]`); broadcasts `C0 12/22 <B6> <flags>` (`*4*110#TTTT/210#TTTT*#0#C##`) |
| `03` / `13` / `23` | `00..0F`, `FF` | `*4*1201..3216*#0#C##`, `*4*3200*#0#C##` | Unimplemented (`TX=[]`); ignored by `4695` `01.01.03` |
| `04` / `14` / `24` | `00..02` | `*4*115#1101..315#3103*#0#C##` | Selects `4695` scenario `1..3` (subject to `14`/`24` season filter); broadcasts `C0 14/24 00..02 <flags>` (`*4*115#110S/215#210S*#0#C##`) |
| `05` / `15` / `25` | `01..FF`, `00` | `*4*13DDD#P..33DDD#P*#0#C##`, `*4*3000*#0#C##`, `*4*3000#P*#0#C##` | `B6 >= 01` with `B7 = 00..02` enters multi-day vacation (subject to `15`/`25` season filter) and broadcasts `C0 15/25 <days> <flags>` (`*4*13DDD/23DDD*#0#C##`); `B6 = 00` while in vacation exits back to weekly program `1..3` |
| `06` / `16` / `26` | `00` | `*4*303*#0#C##`, `*4*103*#0#C##`, `*4*203*#0#C##` | Enters `OFF` (`303` universal; `103` Heating-only; `203` Cooling-only; `103`/`203` `NACK` on Gen A); broadcasts `C0 16/26 00 <flags>` |
| `07` / `17` / `27` | `00` | `*4*302*#0#C##`, `*4*102*#0#C##`, `*4*202*#0#C##` | Enters Protection (`302` universal; `102` Heating-only; `202` Cooling-only); broadcasts `C0 17/27 00 <flags>` |
| `F0` / `F1` | `00` | `*4*1*#0#C##` / `*4*0*#0#C##` | Same season: immediate no-op (`TX=[]`, leaves `OFF` untouched). Cross-season: switches season and enters Protection (`C0 17/27 00 <flags>` -> `*4*102/202*#0#C##`) |

Status byte `B7` (`<flags>`) in `$18 D2 <CU> 03 04 C0 <B5> <B6> <B7>` carries six active status bits decoded identically across Generation B, C, and D gateways (`#0#C`) and Generation A (`#0`):

- `bit 0 = 0` / `1`: `*4*20*#0#C##` (remote control disabled) / `*4*21*#0#C##` (remote control enabled)
- `bit 1 = 1` (`0x02`): `*4*30*#0#C##` (system or probe failure)
- `bit 2 = 1` (`0x04`): `*4*31*#0#C##` (central-unit backup-battery fault from `4695` periodic 10-bit ADC load test)
- `bit 3 = 1` (`0x08`): `*4*22*#0#C##` (at least one probe in Local OFF)
- `bit 4 = 1` (`0x10`): `*4*23*#0#C##` (at least one probe in Local Protection)
- `bit 5 = 1` (`0x20`): `*4*24*#0#C##` (at least one probe in Local Manual offset)

## `DIMENSION 14` Reads and Zone Broadcast Asymmetry

1. **Central `DIMENSION 14` read (`*#4*#0#C*14##`)**: Rejected with `NACK` (`TX=[]`) on Generation A, B, and C gateways; stripped to `$04 99 <CU> 30 0E` (Zone `C` `DIMENSION 14` read -> `*#4*C*14*TTTT*3##`) on Generation D (`MyHomeServer1`, `F461`, `F460`, `3488`). Dimensionless `*#4*#0#C##` (`$04 99 <CU> 30 C0`) is the sole query that reads `4695` central `C0` state (`*4*110#TTTT*#0#C##` / `*4*210#TTTT*#0#C##` when in manual mode).
2. **Built-in Zone `C` versus slave `C+1..C+3` broadcasts**: On a `#0#C` mode or setpoint transition, `4695` Firmware `01.01.03` emits `$18 D2 <CU> 03 04 C0 ...` plus `$04 90/91 <C+1..C+3> 30 <T*2>` or `$04 93 <C+1..C+3> 30 <mode>` pushes to external slave zones, without emitting an immediate `$18 D2 <C> 03 04 12 ...` (`*#4*C*12*TTTT*3##`) report for built-in Zone `C`. External slave probes respond to `$04 90..93` with their own `DIMENSION 12` and `WHAT` broadcasts, whereas built-in Zone `C` reports `DIMENSION 0`, `12`, `13`, and `14` on periodic thermal measurement cycles or explicit `*#4*C##` / `*#4*C*0/12/13/14##` polls.

## Identity and Claim Review

Existing released document, section, chunk, claim, and source identities are preserved unchanged. Three new sections (`ownkb:section:d000068:s000008` in `functional/who-4-temperature-control/addressing.md`, `ownkb:section:d000070:s000007` in `functional/who-4-temperature-control/what.md`, and `ownkb:section:d000069:s000024` in `functional/who-4-temperature-control/dimensions.md`), three retrieval chunks (`ownkb:chunk:r007943..r007945`), three topic entities, new immutable firmware and `own-firmware-oracle` source records strictly above `ownkb:source:s001225` (reusing existing `ownkb:source:s001217..s001220` and `ownkb:source:s001223` where already registered), and implementation-scoped `observed` and `corroborated_interpretation` claims strictly above `ownkb:claim:c074200` are allocated in the lifecycle registry. H1 root-section `section_sha256` pins on `ownkb:section:d000068:s000001`, `ownkb:section:d000069:s000001`, and `ownkb:section:d000070:s000001` are updated solely for their appended child-section lists in the shared IR.
