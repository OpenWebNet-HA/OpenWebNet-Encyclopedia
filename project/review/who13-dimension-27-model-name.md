# WHO 13 DIMENSION 27 model-name evidence review

## Physical gateway capture inspection

Method: source inspection of two read-only physical gateway capture fixtures committed in `OpenWebNet-HA/MyHOME` at revision `eca7e51091ef75a2c10b74d0305fc9a8708624e4`. Both fixtures were sanitized prior to publication in `OpenWebNet-HA/MyHOME`; no physical hardware was operated during this documentation integration.

| Gateway | Firmware | Original Git blob | Original SHA-256 | Line count | Inspected range | Inspected path |
| --- | --- | --- | --- | ---: | --- | --- |
| F461 | `2.0.11` | `9f3ceb3c0fdcb84bad6de94e4c31d013d5911e4f` | `b4f08c1503c360c5341fc0788de80d884d9993082126f95c896f36ca2e4e4755` | `9954` | `6358..6411` | `tests/fixtures/traces/f461_live_2026-10-23/myhome_trace_F461_live_2026-10-23.json` |
| MyHomeServer1 | `3.87.13` | `0600ad6420ae493d87b563332c03f6bf08115bae` | `9c6b0a3d1a248991ca857901ceea12c0b422229eb6e0f4bf305d31cdd2b995fe` | `6840` | `1300..1353` | `tests/fixtures/traces/myhomeserver1_live_2026-10-24/myhome_trace_MyHomeServer1_live_2026-10-24.json` |

Verified exchange records:

- `F461` Firmware `2.0.11` (`WHO 13` `DIMENSION 15 = 200`, diagnostic `WHO 1013` `DIMENSION 1` `OBJECT_MODEL = 134`, `lines 6358..6411`, `run1_oracle_replay_readonly` / `plant_reads`): command-session `tx` `*#13**27##` received command-session `rx` `*#13**27*70#52#54#49##` followed by command-session `rx` `*#*1##` (`ACK`) and event-session `rx` `*#13**27*70#52#54#49##`. Decimal ASCII codes `70, 52, 54, 49` decode to `"F461"`.
- `MyHomeServer1` Firmware `3.87.13` (`WHO 13` `DIMENSION 15 = 200`, diagnostic `WHO 1013` `DIMENSION 1` `OBJECT_MODEL = 67`, `lines 1300..1353`, `run1_identify` / `identify`): command-session `tx` `*#13**27##` received command-session `rx` `*#13**27*77#121#72#111#109#101#83#101#114#118#101#114#49##` followed by command-session `rx` `*#*1##` (`ACK`) and event-session `rx` `*#13**27*77#121#72#111#109#101#83#101#114#118#101#114#49##`. Decimal ASCII codes `77, 121, 72, 111, 109, 101, 83, 101, 114, 118, 101, 114, 49` decode to `"MyHomeServer1"`.

Scope limits: these two physical captures establish populated read responses on those two hardware units and Firmware revisions only. They do not establish write support (`*#13**#27*...##`), non-ASCII encodings, maximum string length, or whether user configuration can alter the returned string.

## Published oracle v3 result inspection

Method: source inspection of published `who13-identification` result TSVs at `OpenWebNet-HA/own-firmware-oracle` revision `836843800a25def1d14f40aa82d09dd0bf901db0` (`suite_sha256=718a8e0e59e9a6d7b0bdd4ebe78edac87200d1bb4d82ed57b8422b15ddad188c`, `oracle_version=3`, full simulated-PIC harness, `reset=each` on `F450 020010` and `reset=0` on the other 11 targets, declared `settle_ms=3000`, reproduced across two consecutive passes via `tools/suite_plan.py`). These observations describe executed gateway Firmware in the QEMU user-mode jail with factory/staged configuration files; they do not establish physical hardware supervisor behavior or plant-provisioned descriptor values.

Line `25` of each 25-line TSV records the `down *#13**27##` step:

| Gateway | Firmware | Original Git blob | Original SHA-256 | Line `25` outcome (`reply` / `verdict` / `output`) | Inspected path |
| --- | --- | --- | --- | --- | --- |
| F450 | `020010` | `d3a50275544b474e76e8ad239ecdad3110a16ce5` | `2239fd97b91ed5006d523fccbff6ecb5768e6c53974a8d0647fbd611c5441395` | `ack` / `out` / `own:*#13**27*72#79#83#84##` | `results/F450/020010/oracle/full/who13-identification.tsv` |
| F453 | `010100` | `41d4d01960e905de399b6ef3baa68dbf8e78dbae` | `e2c92c9ad8991bc6bafd06448c4f145b1f4a2c3bbb9732fcd125d1a8e8f4d831` | `ack` / `out` / `own:*#13**27*66#84#87#69#66##` | `results/F453/010100/oracle/full/who13-identification.tsv` |
| F453AV | `030014` | `5fe14b1081e40d257428a66174f35ff9128e6e15` | `0b599630330776d0035601ecb70bd634da7316ec64e86817a2435e4f91888213` | `ack` / `out` / `own:*#13**27*66#84#87#69#66##` | `results/F453AV/030014/oracle/full/who13-identification.tsv` |
| F454 | `020051` | `6f01642e401a9a7deb67fce949657c58e21b41c0` | `2c6135496f05323387fd3843196619a587b127dc4f17280142e409e667e00338` | `ack` / `out` / `own:*#13**27*72#79#83#84##` | `results/F454/020051/oracle/full/who13-identification.tsv` |
| F459 | `020105` | `059d2d7b4bff6366f27b271b984abcc35fd1ccd3` | `5587b31eec5a7e012e01f81a0cfb4c1dfd0c20074c28f1c1e7cad1e52221baf5` | `ack` / `out` / `own:*#13**27*72#79#83#84##` | `results/F459/020105/oracle/full/who13-identification.tsv` |
| F460 | `020012` | `8a78f3fe80e5d755c24887228886eb1818344827` | `c93d45a7d519abcf9d9dd333d10b58c41852c3b993a8e79397fb04831e3ef80b` | `ack` / `out` / `own:*#13**27*72#79#83#84##` | `results/F460/020012/oracle/full/who13-identification.tsv` |
| F461 | `020011` | `1f5c583226702348dc55aebe5d21ec015e47328a` | `5d2840cbb2d90282fdcb8e028d7160fba82747cc3eac2dc714641e153ef19248` | `ack` / `out` / `own:*#13**27*72#79#83#84##` | `results/F461/020011/oracle/full/who13-identification.tsv` |
| H4684 | `020054` | `076d478c18ee0b8e38fc30eb3503b1da0642b1b3` | `0c8f7ae997985492d4cab2574b15de8af2817b01136f13e01dfc67a1783ef8e6` | `nack` / `silent` / `-` | `results/H4684/020054/oracle/full/who13-identification.tsv` |
| MH200 | `020102` | `7c290875e2d8da0703de387f61b8a29b3ba29b3b` | `593055301e49ca5b130b6f656e67b2a8f2ee191eee37d940756812b763411d1a` | `-` / `out` / `own:*#13**27*#*#*1##` | `results/MH200/020102/oracle/full/who13-identification.tsv` |
| MH200N | `010108` | `3c400a995ec080620698ee2b8a168abd1585fb19` | `656c3e406862096c834a77599ff7984b657f483e9d886247c8b86def46824a85` | `-` / `out` / `own:*#13**27*#*#*1##` | `results/MH200N/010108/oracle/full/who13-identification.tsv` |
| MH202 | `010024` | `164665451ef97d6d9b6847db7c28b27090664daf` | `f15bc5a46c16588c9f27a9542d2a074f722a293849b07820551be6cfc24b8478` | `ack` / `out` / `own:*#13**27*72#79#83#84##` | `results/MH202/010024/oracle/full/who13-identification.tsv` |
| MyHomeServer1 | `028206` | `31a5a067aab5436bd3991d613ed92e761452ecfe` | `d0337e5dcebd4915d4a20793240be41e41048f2511af721a4bf5d8382f9d3e8d` | `-` / `out` / `own:*#13**27*#*#*1##` | `results/MyHomeServer1/028206/oracle/full/who13-identification.tsv` |

Key cross-target observations:

- Six Firmwares (`F450 020010`, `F454 020051`, `F459 020105`, `F460 020012`, `F461 020011`, and `MH202 010024`) emit `own:*#13**27*72#79#83#84##` (`"HOST"`, decimal ASCII `72, 79, 83, 84`) followed by `ack` when unpopulated in the jail; `F453 010100` and `F453AV 030014` emit `own:*#13**27*66#84#87#69#66##` (`"BTWEB"`, decimal ASCII `66, 84, 87, 69, 66`) followed by `ack`.
- `H4684 020054` refuses `*#13**27##` cleanly with `reply=nack` and `verdict=silent` (unlike `DIMENSION 10`, `11`, and `12`, which record `verdict=crash` on `H4684 020054` and `MH200 020102`).
- `MH200 020102`, `MH200N 010108`, and `MyHomeServer1 028206` (whose staged configuration has an empty descriptor string) emit `own:*#13**27*#*#*1##` (`reply=-`, `verdict=out`), concatenating an unterminated `*#13**27*#` directly with `*#*1##` so no separate `ACK` frame follows on a `##`-delimited stream.

## Identity and claim review

Existing released document, section, chunk, claim, and source identities are preserved unchanged. One new section (`ownkb:section:d000036:s000018` in `functional/who-13-integration-gateway/dimensions.md`), one retrieval chunk (`ownkb:chunk:r007941`), one topic entity (`ownkb:entity:topic:d000036-s000018`), two pinned `OpenWebNet-HA/MyHOME` physical capture source records (`ownkb:source:s001202` and `ownkb:source:s001203`), 12 pinned `own-firmware-oracle` source records (`ownkb:source:s001204` through `ownkb:source:s001215`), and 16 scoped claims (`ownkb:claim:c074171` through `ownkb:claim:c074186`) are allocated strictly above both `main` and open `PR #52`. H1 root-section `section_sha256` pins on `ownkb:section:d000036:s000001` (`ownkb:claim:c001646` through `ownkb:claim:c001685`) are updated solely for the appended child-section list in the shared IR.
