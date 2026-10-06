# Stop&Go Btest

## Summary

Stop&Go Btest F80/SGB adds periodic residual-current-device testing to the legacy automatic reclosure kit. It retains fault checks and local indications, and its test activation has a specific six-hour timing relationship that differs from newer Stop&Go generations.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0092` | Project identity |
| Technical description | Stop&Go Btest | Canonical catalogue |
| Commercial identities | `F80/SGB` | Canonical commercial records |
| Catalogue item | `914` | Canonical catalogue |
| Main catalogue system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `1` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | New energy saving and load control, Energy/load control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F80/SGB` | Established catalogue identity | canonical commercial record for item `914` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `F4269H.pdf` | technical / instruction manual | 10W04 / revision H | Entire applicable kit instructions, PDF pp. 1–4; unnumbered panels 1–9b and technical legend p. 4; 10W04 | [Archived original](https://archive.openwebnet-ha.org/sha256/16/d6/16d6f331c180eb1fc0afbc2042f7e6aa1c0e967207e88cc3c3e8fab421254e23.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/F4269H.pdf) |
| `F80SCS-product-sheet.pdf` | Accessory product export · IT | Retrieved 2026-10-06 | Whole one-page export: optional Stop&Go fault/intervention display on Touchscreen; accessory dimensions not adopted for the kit | [Archived original](https://archive.openwebnet-ha.org/sha256/7f/71/7f7110949fc1b80058368b6455a100ff738ce5b2125213ec8ac41e82b2393262.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F80SCS) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Kit construction | Motor 2 DIN modules plus control unit 1 DIN module | F4269H, PDF p. 4; physical width differs from one logical Module |
| Supply / operating conditions | `230 Vac`, `85..110%` nominal; `50 Hz`; `−5..60 °C`; flexible conductors up to `1.5 mm²` | F4269H, PDF p. 4 |
| Motor / control rating | Motor: 4000 operations and maximum actuation rating `14 VA`; control: `1 VA` | F4269H, PDF p. 4; not an observed standby-total measurement |
| Fault-check thresholds | Earth resistance: non-operating `225 kΩ` / operating `375 kΩ`; short-circuit resistance: non-operating `0.75 Ω` / operating `1.25 Ω` | F4269H, PDF p. 4; intervening bands do not have one stated exact trip threshold |
| Contacts / interfaces | Motor 12/13 fault relay; remote closure L input; separate control-unit sensing terminals; optional F80SCS / F80CMD expansion | F4269H, PDF p. 4; expansion does not establish a built-in SCS port |
| Btest applicability / test current | Only `30 mA` residual-current devices; test current `27.3..39.1 mA` | F4269H, PDF p. 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `914` | Canonical catalogue |
| Technical item | Stop&Go Btest | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `1` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| New energy saving and load control | `1` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `914` | `F80/SGB` | `1` | `5` | `BTicino_Undefined_Stop&Go Btest` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `914` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `227` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `227` | `1` | `176` Stop&Go Btest | Fixed/designated metadata | `1176` | `176` | `632` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `227` | Physical configuration | `0` | Canonical firmware/mode association |
| `227` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `227` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `227` | `A1` | `0..1` | `0` | A1; Energy Management A1 Address (0-1) |
| `227` | `A2` | `0..9` | `0` | A2; Energy Management A2 Address (0-9) |
| `227` | `A3` | `0..9` | `1` | A3; Energy Management A3 Address (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `176` - Stop&Go Btest

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A123` | `0..127` | `0` | Address; Energy Management A123 Address (0-127) |

### Device-specific interpretation

Official/default wildcard firmware `227` declares one Module with Object `176`. There are no Virgin Objects or stored Object filters. Empty condition `4158` links rule `520` but supplies no activation predicate. Firmware A1 is `0..1`, A2/A3 `0..9`, defaults `0/0/1`; reusable A123 is `0..127`, default `0`. All 256 conversion branches are retained: A123 = 100 × A1 + 10 × A2 + A3 for outputs 0..255. Inputs for outputs `128..199` fit the independent firmware digits but exceed the reusable Object domain; `200..255` also require `A1=2` outside the firmware domain. No narrower default, precedence or wider effective domain is inferred. Periodic physical Btest operation is not a programmable timer inferred from this narrow reusable address schema.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `227` | `1` | `176` | `4158` | No textual predicate stored | `520` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `520` | `A1=0; A2=0; A3=0` | `A123` = `0` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=1` | `A123` = `1` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=2` | `A123` = `2` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=3` | `A123` = `3` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=4` | `A123` = `4` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=5` | `A123` = `5` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=6` | `A123` = `6` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=7` | `A123` = `7` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=8` | `A123` = `8` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=9` | `A123` = `9` | `520` → `521` → `522` |
| `520` | `A1=0; A2=1; A3=0` | `A123` = `10` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=1` | `A123` = `11` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=2` | `A123` = `12` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=3` | `A123` = `13` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=4` | `A123` = `14` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=5` | `A123` = `15` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=6` | `A123` = `16` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=7` | `A123` = `17` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=8` | `A123` = `18` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=9` | `A123` = `19` | `520` → `521` → `523` |
| `520` | `A1=0; A2=2; A3=0` | `A123` = `20` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=1` | `A123` = `21` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=2` | `A123` = `22` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=3` | `A123` = `23` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=4` | `A123` = `24` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=5` | `A123` = `25` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=6` | `A123` = `26` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=7` | `A123` = `27` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=8` | `A123` = `28` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=9` | `A123` = `29` | `520` → `521` → `524` |
| `520` | `A1=0; A2=3; A3=0` | `A123` = `30` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=1` | `A123` = `31` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=2` | `A123` = `32` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=3` | `A123` = `33` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=4` | `A123` = `34` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=5` | `A123` = `35` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=6` | `A123` = `36` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=7` | `A123` = `37` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=8` | `A123` = `38` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=9` | `A123` = `39` | `520` → `521` → `525` |
| `520` | `A1=0; A2=4; A3=0` | `A123` = `40` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=1` | `A123` = `41` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=2` | `A123` = `42` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=3` | `A123` = `43` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=4` | `A123` = `44` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=5` | `A123` = `45` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=6` | `A123` = `46` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=7` | `A123` = `47` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=8` | `A123` = `48` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=9` | `A123` = `49` | `520` → `521` → `526` |
| `520` | `A1=0; A2=5; A3=0` | `A123` = `50` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=1` | `A123` = `51` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=2` | `A123` = `52` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=3` | `A123` = `53` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=4` | `A123` = `54` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=5` | `A123` = `55` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=6` | `A123` = `56` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=7` | `A123` = `57` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=8` | `A123` = `58` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=9` | `A123` = `59` | `520` → `521` → `527` |
| `520` | `A1=0; A2=6; A3=0` | `A123` = `60` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=1` | `A123` = `61` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=2` | `A123` = `62` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=3` | `A123` = `63` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=4` | `A123` = `64` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=5` | `A123` = `65` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=6` | `A123` = `66` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=7` | `A123` = `67` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=8` | `A123` = `68` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=9` | `A123` = `69` | `520` → `521` → `528` |
| `520` | `A1=0; A2=7; A3=0` | `A123` = `70` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=1` | `A123` = `71` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=2` | `A123` = `72` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=3` | `A123` = `73` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=4` | `A123` = `74` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=5` | `A123` = `75` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=6` | `A123` = `76` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=7` | `A123` = `77` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=8` | `A123` = `78` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=9` | `A123` = `79` | `520` → `521` → `529` |
| `520` | `A1=0; A2=8; A3=0` | `A123` = `80` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=1` | `A123` = `81` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=2` | `A123` = `82` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=3` | `A123` = `83` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=4` | `A123` = `84` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=5` | `A123` = `85` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=6` | `A123` = `86` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=7` | `A123` = `87` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=8` | `A123` = `88` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=9` | `A123` = `89` | `520` → `521` → `530` |
| `520` | `A1=0; A2=9; A3=0` | `A123` = `90` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=1` | `A123` = `91` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=2` | `A123` = `92` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=3` | `A123` = `93` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=4` | `A123` = `94` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=5` | `A123` = `95` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=6` | `A123` = `96` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=7` | `A123` = `97` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=8` | `A123` = `98` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=9` | `A123` = `99` | `520` → `521` → `531` |
| `520` | `A1=1; A2=0; A3=0` | `A123` = `100` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=1` | `A123` = `101` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=2` | `A123` = `102` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=3` | `A123` = `103` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=4` | `A123` = `104` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=5` | `A123` = `105` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=6` | `A123` = `106` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=7` | `A123` = `107` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=8` | `A123` = `108` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=9` | `A123` = `109` | `520` → `532` → `533` |
| `520` | `A1=1; A2=1; A3=0` | `A123` = `110` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=1` | `A123` = `111` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=2` | `A123` = `112` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=3` | `A123` = `113` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=4` | `A123` = `114` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=5` | `A123` = `115` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=6` | `A123` = `116` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=7` | `A123` = `117` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=8` | `A123` = `118` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=9` | `A123` = `119` | `520` → `532` → `534` |
| `520` | `A1=1; A2=2; A3=0` | `A123` = `120` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=1` | `A123` = `121` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=2` | `A123` = `122` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=3` | `A123` = `123` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=4` | `A123` = `124` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=5` | `A123` = `125` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=6` | `A123` = `126` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=7` | `A123` = `127` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=8` | `A123` = `128` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=9` | `A123` = `129` | `520` → `532` → `535` |
| `520` | `A1=1; A2=3; A3=0` | `A123` = `130` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=1` | `A123` = `131` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=2` | `A123` = `132` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=3` | `A123` = `133` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=4` | `A123` = `134` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=5` | `A123` = `135` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=6` | `A123` = `136` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=7` | `A123` = `137` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=8` | `A123` = `138` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=9` | `A123` = `139` | `520` → `532` → `536` |
| `520` | `A1=1; A2=4; A3=0` | `A123` = `140` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=1` | `A123` = `141` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=2` | `A123` = `142` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=3` | `A123` = `143` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=4` | `A123` = `144` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=5` | `A123` = `145` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=6` | `A123` = `146` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=7` | `A123` = `147` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=8` | `A123` = `148` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=9` | `A123` = `149` | `520` → `532` → `537` |
| `520` | `A1=1; A2=5; A3=0` | `A123` = `150` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=1` | `A123` = `151` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=2` | `A123` = `152` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=3` | `A123` = `153` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=4` | `A123` = `154` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=5` | `A123` = `155` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=6` | `A123` = `156` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=7` | `A123` = `157` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=8` | `A123` = `158` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=9` | `A123` = `159` | `520` → `532` → `538` |
| `520` | `A1=1; A2=6; A3=0` | `A123` = `160` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=1` | `A123` = `161` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=2` | `A123` = `162` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=3` | `A123` = `163` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=4` | `A123` = `164` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=5` | `A123` = `165` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=6` | `A123` = `166` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=7` | `A123` = `167` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=8` | `A123` = `168` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=9` | `A123` = `169` | `520` → `532` → `539` |
| `520` | `A1=1; A2=7; A3=0` | `A123` = `170` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=1` | `A123` = `171` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=2` | `A123` = `172` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=3` | `A123` = `173` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=4` | `A123` = `174` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=5` | `A123` = `175` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=6` | `A123` = `176` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=7` | `A123` = `177` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=8` | `A123` = `178` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=9` | `A123` = `179` | `520` → `532` → `540` |
| `520` | `A1=1; A2=8; A3=0` | `A123` = `180` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=1` | `A123` = `181` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=2` | `A123` = `182` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=3` | `A123` = `183` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=4` | `A123` = `184` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=5` | `A123` = `185` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=6` | `A123` = `186` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=7` | `A123` = `187` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=8` | `A123` = `188` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=9` | `A123` = `189` | `520` → `532` → `541` |
| `520` | `A1=1; A2=9; A3=0` | `A123` = `190` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=1` | `A123` = `191` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=2` | `A123` = `192` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=3` | `A123` = `193` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=4` | `A123` = `194` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=5` | `A123` = `195` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=6` | `A123` = `196` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=7` | `A123` = `197` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=8` | `A123` = `198` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=9` | `A123` = `199` | `520` → `532` → `542` |
| `520` | `A1=2; A2=0; A3=0` | `A123` = `200` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=1` | `A123` = `201` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=2` | `A123` = `202` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=3` | `A123` = `203` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=4` | `A123` = `204` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=5` | `A123` = `205` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=6` | `A123` = `206` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=7` | `A123` = `207` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=8` | `A123` = `208` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=9` | `A123` = `209` | `520` → `543` → `544` |
| `520` | `A1=2; A2=1; A3=0` | `A123` = `210` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=1` | `A123` = `211` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=2` | `A123` = `212` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=3` | `A123` = `213` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=4` | `A123` = `214` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=5` | `A123` = `215` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=6` | `A123` = `216` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=7` | `A123` = `217` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=8` | `A123` = `218` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=9` | `A123` = `219` | `520` → `543` → `545` |
| `520` | `A1=2; A2=2; A3=0` | `A123` = `220` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=1` | `A123` = `221` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=2` | `A123` = `222` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=3` | `A123` = `223` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=4` | `A123` = `224` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=5` | `A123` = `225` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=6` | `A123` = `226` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=7` | `A123` = `227` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=8` | `A123` = `228` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=9` | `A123` = `229` | `520` → `543` → `546` |
| `520` | `A1=2; A2=3; A3=0` | `A123` = `230` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=1` | `A123` = `231` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=2` | `A123` = `232` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=3` | `A123` = `233` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=4` | `A123` = `234` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=5` | `A123` = `235` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=6` | `A123` = `236` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=7` | `A123` = `237` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=8` | `A123` = `238` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=9` | `A123` = `239` | `520` → `543` → `547` |
| `520` | `A1=2; A2=4; A3=0` | `A123` = `240` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=1` | `A123` = `241` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=2` | `A123` = `242` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=3` | `A123` = `243` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=4` | `A123` = `244` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=5` | `A123` = `245` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=6` | `A123` = `246` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=7` | `A123` = `247` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=8` | `A123` = `248` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=9` | `A123` = `249` | `520` → `543` → `548` |
| `520` | `A1=2; A2=5; A3=0` | `A123` = `250` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=1` | `A123` = `251` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=2` | `A123` = `252` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=3` | `A123` = `253` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=4` | `A123` = `254` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=5` | `A123` = `255` | `520` → `543` → `549` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `914` / `modobj = 1` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`176`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `176` Stop&Go Btest | New energy saving and load control | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Supply restoration | Initial powering does not automatically reclose the coupled protective device | F4269H, PDF p. 2, panel 8a |
| Pre-reclosure check | Short-circuit and earth-fault checks inhibit restoration when a fault is detected | F4269H, PDF pp. 3–4 |
| Indications | Upper LED: short circuit; lower: earth fault. Green/green: healthy closed state; one red: corresponding fault; both red: both faults; yellow: resolved fault indication; alternating red: blocked state | F4269H, PDF pp. 3–4; combine LED state with breaker state and buzzer |
| Other status | Upper flashing green: reclosure disabled; both LEDs off: mains absence or device fault; buzzer accompanies documented fault/block states | F4269H, PDF p. 3 |
| SCS supervision | F80SCS accessory supports Touchscreen display of Stop&Go intervention following a fault | F80SCS product export, PDF p. 1; no complete OpenWebNet command/control API established |
| Periodic Btest | 56-day interval; first activation six hours before the desired test time | F4269H, PDF p. 2, panel 9b |
| Btest indications | Lower flashing green: testing disabled; both flashing yellow with buzzer and closed breaker: documented RCD fault | F4269H, PDF p. 3; separate from yellow resolved-fault indication |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

F4269H (10W04), PDF pp. 1–4, describes coupling and enabling the legacy kit; the protective device must be closed during coupling, and the kit is powered after coupling. Panel 8a enables reclosure with P held for more than 2 seconds after closed-state setup. The transparent isolating slider disables automatic operation in OFF. The diagrams and compatibility list cover the specifically listed protective-device families (including G722/G723/G724/G725, G8130/G8230/G823, F82+G2 and F810N/F820/F81/F82/F881); compatibility is not assumed for every breaker.

### Connector scope

F4269H, PDF p. 4, supplies this terminal legend; it is a source locator, not an installation substitute.

| Assembly | Source terminals / purpose |
| --- | --- |
| Motor, upper | 1 L remote closure; 2 L1; 3 unused; 4 N input; 5 unused; 6 L control output; 7 unused; 8 N output |
| Motor, lower | 12/13 fault-indication relay (05/06 in schematic) |
| Control, upper | 1 L1 closure; 2 L; 3 unused; 4 N |
| Control, lower | 5 downstream PE; 6 unused; 7 SC1; 8 SC2; 9 downstream L; 10 unused; 11 downstream N |

These physical P-button/terminal procedures are independent of the catalogue address fields and its configuration-mode identifiers. No manufacturer programming project, reset-to-factory workflow, firmware package or full SCS functional command vocabulary is supplied by these kit instructions.

### Btest setup

Panel 8b holds P for more than 8 seconds; panel 9b requires first activation six hours before the desired recurring test time. The source gives a 56-day period. PDF p. 3 describes P-button deactivation/reactivation using the lower green LED (flashing then fixed), and calls for replacement after its indicated RCD test failure. These are the legacy F80/SGB instructions, not the eight-hour timing of newer F80SGB product material.

## Source reconciliation

F4269H explicitly covers F80/SG and F80/SGB, with different activation and Btest scopes. Its four PDF pages are not printed as four numbered manual pages: panel locators and PDF page numbers are used. Physical three-module kit width must not be confused with the one-Module catalogue topology. F80SCS evidence concerns optional fault-intervention display; it does not prove the base kit itself implements the complete SCS command surface. Historical TT/TN application statements are source claims, not current universal installation rules.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- Dedicated later-generation F80SGB and F80SGPN downloads encountered during discovery are not exact revision evidence for this slash-coded legacy kit. Their two-module construction/eight-hour test timing are not adopted.
- F4268H maintenance instructions remain unexamined; firmware-update and complete SCS command procedures are not established.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0092)
