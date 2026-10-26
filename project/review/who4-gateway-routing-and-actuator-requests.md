# WHO 4 gateway routing and actuator-request evidence review

## Published oracle v3 result inspection

Method: source inspection of published `thermo-zone-requests` result TSVs at `own-firmware-oracle` revision `de87a34e251b677a299917c98fcfcea3b409bf34` (`oracle_version=3`, full simulated-PIC harness, `reset=each` on `F450 020010` and `reset=0` on the other 11 targets, declared `settle_ms=3000`). These observations describe executed gateway Firmware under a simulated PIC responder; they do not establish physical SCS bus behavior or uninspected Firmware revisions. The declared `settle_ms=3000` setting is a harness ceiling rather than proof of an entire three-second observation window.

Lines `16..38` of each 38-line TSV record 23 `WHO 4` Temperature Control requests: 13 local main-bus baseline queries (`*#4*#0*20##`, `*#4*0#0*20##`, `*#4*0*60##`, `*#4*2##`, `*#4*2#0*20##`, `*#4*2#1*20##`, `*#4*2#2*20##`, `*#4*2*0##`, `*#4*2*12##`, `*#4*2*14##`, `*#4*2*19##`, `*#4*2*20##`, `*#4*2*60##` on lines `16..20`, `23..24`, and `33..38`), one dimensionless local actuator status request (`*#4*2#1##` on line `21`), and nine `#4#INTERFACE`-qualified local-bus requests (`*#4*2#1#4#01*20##` on line `22`, and `*#4*2#4#01##`, `*#4*2#4#01*0##`, `*#4*2#4#01*11##`, `*#4*2#4#01*19##`, `*#4*2#4#01*20##`, `*#4*2#4#01*60##`, `*#4*2#4#12##`, `*#4*2#4#12*20##` on lines `25..32`).

| Gateway | Firmware | Original Git blob | Original SHA-256 | Inspected path |
| --- | --- | --- | --- | --- |
| F450 | `020010` | `c414bb186aeb71fa61e49d4a0fb8fe1226077605` | `ac10333e710b3295fbedd8aa0f4f012fd79ebfe27f607bad3e1a8ddf10c1870b` | `results/F450/020010/oracle/full/thermo-zone-requests.tsv` |
| F453 | `010100` | `2827fff8b48f34f153ecbce3949b79baabf2220b` | `9f4ed27a6f36e21ff5a8a52e923d03113e3f55d03533f44b0a1aac8460038d52` | `results/F453/010100/oracle/full/thermo-zone-requests.tsv` |
| F453AV | `030014` | `b5ac86aac8f1a545a126b350ad7172dd4f54e576` | `612f25d06a8cdb5710e137b3c852d9cf471cda3bf9589e2205b569db8fd3334e` | `results/F453AV/030014/oracle/full/thermo-zone-requests.tsv` |
| F454 | `020051` | `54cec97a1d2aca49f7dd7d3e9033c245610fb4c3` | `f45a9d533ab022493e1bcc69e5fc18d737b61f82dc23f49f88a60060a62cf560` | `results/F454/020051/oracle/full/thermo-zone-requests.tsv` |
| F459 | `020105` | `4bdc1059fc94021551b5e8ede92bd5a43681c968` | `75a272845860b585a775f565993f2f81a57140451dfa29070565abe9ec0d50a6` | `results/F459/020105/oracle/full/thermo-zone-requests.tsv` |
| F460 | `020012` | `5f34bab71a12c754399c05e5a5816bca3af88fcd` | `dfa5b2eea75a174f38bfc2ba978783f4cc596a86a0b95415de5ad45b858b063e` | `results/F460/020012/oracle/full/thermo-zone-requests.tsv` |
| F461 | `020011` | `6bf67a9337c2dd1d90d15a1658344cc51b8b3c98` | `0503018e39b8ca1d87821c9b2157eca1cf5aa00289e0b7c9a99227bd7cdb0b93` | `results/F461/020011/oracle/full/thermo-zone-requests.tsv` |
| H4684 | `020054` | `c8fd81458e5996e083d572f736e5565cb46e8565` | `a3c23b54c4939b0166c659f9bb5c281530b98948d0cb7ae3c58f5083b4a67366` | `results/H4684/020054/oracle/full/thermo-zone-requests.tsv` |
| MH200 | `020102` | `b804696f468d457c64f59166faa7c9730e089c0b` | `642ac9ffa70f6edfeba571a1ed4c2fc94cecf25efdb533d4d7666fc17f4c9ad5` | `results/MH200/020102/oracle/full/thermo-zone-requests.tsv` |
| MH200N | `010108` | `9bf2ddc9f18f98a56949701c85356bf7fc5089a9` | `cd4664998b17b0e6cf126fd34552256f25b360da6d9ccce47ea1d917968d4655` | `results/MH200N/010108/oracle/full/thermo-zone-requests.tsv` |
| MH202 | `010024` | `9628cb70b34c17c6e7e5d160eec1ab6c591de1b0` | `f7cf21d4e23ac82f34fb78fa6e0f03c898adff7789576e8b1ac12a6fa14dd752` | `results/MH202/010024/oracle/full/thermo-zone-requests.tsv` |
| MyHomeServer1 | `028206` | `50d83c3570e801d0688a788078fb4755deb48d4a` | `5347e72a10dfb51561fec0aacca773b16828943fc96f40d8ee7f7cc5144d3270` | `results/MyHomeServer1/028206/oracle/full/thermo-zone-requests.tsv` |

## Recorded bus-payload comparison for `#4#INTERFACE` requests

Across all 12 inspected TSVs, zero `#4#INTERFACE`-qualified `WHO 4` rows (`line 22` and `lines 25..32`) contain an interface-routed `$06EC` (`30 36 45 43`) or `$06E4` (`30 36 45 34`) SCS bus telegram:

- `F453 010100`, `F453AV 030014`, and `MH200N 010108` record `reply=nack` and `verdict=silent` on all nine `#4#INTERFACE` rows (`line 22` and `lines 25..32`).
- Every one of the 12 Firmwares records `reply=nack` and `verdict=silent` on `*#4*2#4#01*11##` (`line 27`).
- `H4684 020054` and `MH200 020102` emit identical local-zone-`2` SCS telegrams on `#4#INTERFACE` status, `DIMENSION 0`, and `DIMENSION 19` requests as on unqualified `WHERE 2`: `$0499023000\r`, `$0499023012\r`, `$049902300E\r`, and `$049902300D\r` on `*#4*2#4#01##` (`line 25`) and `*#4*2#4#12##` (`line 31`, matching `*#4*2##` on `line 19`); `$0499023000\r` on `*#4*2#4#01*0##` (`line 26`, matching `*#4*2*0##` on `line 33`); and `$0499023013\r` on `*#4*2#4#01*19##` (`line 28`, matching `*#4*2*19##` on `line 36`). Both record `reply=nack` and `verdict=silent` on `*#4*2#1#4#01*20##` (`line 22`), `*#4*2#4#01*20##` (`line 29`), `*#4*2#4#01*60##` (`line 30`), and `*#4*2#4#12*20##` (`line 32`).
- `F450 020010`, `F454 020051`, `F459 020105`, `F460 020012`, `F461 020011`, and `MyHomeServer1 028206` emit the exact local-zone-`2` `DIMENSION 20` SCS telegram (`$04A9023010\r`, or `$004A9023010\r` on `F460` and `F461`) on `*#4*2#1#4#01*20##` (`line 22`), `*#4*2#4#01*20##` (`line 29`), and `*#4*2#4#12*20##` (`line 32`), matching unqualified `*#4*2*20##` (`line 37`, with `reply=nack` and `verdict=out` on `F450` and `F454`, and `reply=ack` and `verdict=out` on `F459`, `F460`, `F461`, and `MyHomeServer1`). `F459 020105`, `F460 020012`, `F461 020011`, and `MyHomeServer1 028206` likewise emit the local-zone-`2` `DIMENSION 60` SCS telegram (`$06D102030308000000\r`, or `$006D102030308000000\r` on `F460` and `F461`) on `*#4*2#4#01*60##` (`line 30`), matching unqualified `*#4*2*60##` (`line 38`).
- `MH202 010024` records `$0499843110\r` (`24 30 34 39 39 38 34 33 31 31 30 0d` - local zone `4`, actuator `1`, `DIMENSION 20`, matching the `$0499823110\r` encoding of `*#4*2#1*20##` on `line 23` with zone `4` in place of zone `2`) on both `*#4*2#1#4#01*20##` (`line 22`) and `*#4*2#4#01*20##` (`line 29`), whereas `*#4*2#4#12*20##` (`line 32`) records `reply=nack` and `verdict=silent`.

## Dimensionless actuator status requests and `MH202 010024` daemon exit

Line `21` (`*#4*2#1##`), line `25` (`*#4*2#4#01##`), and line `31` (`*#4*2#4#12##`) isolate dimensionless actuator status behavior across the 12 Firmwares:

- Nine Firmwares (`F450 020010`, `F453 010100`, `F453AV 030014`, `F454 020051`, `F459 020105`, `F460 020012`, `F461 020011`, `MH200N 010108`, and `MyHomeServer1 028206`) record `reply=nack` and `verdict=silent` on `*#4*2#1##`, `*#4*2#4#01##`, and `*#4*2#4#12##`.
- `H4684 020054` and `MH200 020102` emit the four local-zone-`2` status telegrams (`$0499023000\r`, `$0499023012\r`, `$049902300E\r`, `$049902300D\r`) on `*#4*2#1##`, identical to `*#4*2##` (`line 19`).
- `MH202 010024` records `reply=nack` and `verdict=crash` (process exit on `SIGSEGV`) on both `*#4*2#1##` (`line 21`) and `*#4*2#4#01##` (`line 25`), while `*#4*2#4#12##` (`line 31`) records `reply=nack` and `verdict=silent`. By contrast, `*#4*2#1*20##` (`line 23`) records `reply=ack` and `verdict=out` (`$0499823110\r`) on `MH202 010024`.

## Identity and claim review

Existing released document, section, chunk, claim, and source identities are preserved unchanged. Two new sections (`ownkb:section:d000068:s000007` in `functional/who-4-temperature-control/addressing.md` and `ownkb:section:d000104:s000016` in `protocol/addressing.md`), two retrieval chunks, two topic entities, 12 pinned `own-firmware-oracle` source records (`ownkb:source:s001190` through `ownkb:source:s001201`), and scoped `observed` implementation claims are allocated strictly above the existing ID lifecycle inventory. H1 root-section `section_sha256` pins on `ownkb:section:d000068:s000001` and `ownkb:section:d000104:s000001` are updated solely for the appended child-section list in the shared IR.
