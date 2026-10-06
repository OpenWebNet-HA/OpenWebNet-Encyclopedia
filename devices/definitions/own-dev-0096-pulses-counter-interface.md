# Pulses counter interface

## Summary

3522 / 003554 is a compact SCS pulse-counter interface for compatible water, gas or heat meters with pulse outputs. It reports consumption and can retain hourly, daily and monthly history for one year when a system device supplies the date and time.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0096` | Project identity |
| Technical description | Pulses counter interface | Canonical catalogue |
| Commercial identities | `3522`, `003554` | Canonical commercial records |
| Catalogue item | `1031` | Canonical catalogue |
| Main catalogue system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `3` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | New energy saving and load control, Energy metering, Interface | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3522` | Established catalogue identity | canonical commercial record for item `1031` |
| Legrand | `003554` | Established catalogue identity | canonical commercial record for item `1031` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `3522-publisher-product-sheet.pdf` | product sheet | Publisher export retained 2026-10-03 | Whole exact 3522 export, PDF/printed p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/16/b6/16b671b522f2d6522fe4dd53e249e1600c3e53a0b6be107a1ab92a2b0624d601.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3522) |
| `MQ00359_b_EN.pdf` | technical / instruction manual | 11/12/2012; MQ00359-b-UK | Entire exact technical sheet, printed/PDF pp. 1–2; MQ00359-b-UK, 11/12/2012 | [Archived original](https://archive.openwebnet-ha.org/sha256/ed/1f/ed1fd00db6fa60bd146761506281b3b23892f1a2153219d8dcc34aebc04d1454.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00359_b_EN.pdf) |
| `BR-MyHOME-HPML0714.pdf` | Regional MyHOME catalogue | HPML0714; source-era issue | Only printed/PDF p. 34: old 03554 to 3522 cross-reference; unrelated leaves unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Publisher source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Construction | Basic concealed-box/board module, `40×40×23 mm` | MQ00359-b-UK, printed/PDF p. 1 |
| Power / temperature | `18..27 Vdc`; maximum standby `7.5 mA`; `0..40 °C` | Same source; export 27 V / 0.0075 A agrees with rating |
| Pulse input | Minimum pulse `50 ms`; at most 5 pulses/s; minimum period `200 ms` | Same source |
| Outputs / indicators | Optoisolated pulse-repetition output; green supply and red pulse indication | Same source; virtual-configuration button marked future application |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1031` | Canonical catalogue |
| Technical item | Pulses counter interface | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `3` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| New energy saving and load control | `3` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `1031` | `3522` | `1` | `5` | `BTicino_Undefined_Pulses counter interface` |
| `1893` | `003554` | `2` | `5` | Empty in source |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `1031` | `1` | `0` | `0` | Empty in source |
| `1893` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `200` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `200` | `1` | `204` Pulse output sensor interface | Fixed/designated metadata | `758` | `481` | `520` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `200` | Physical configuration | `0` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `200` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `200` | `A1` | `0..2` | `0` | A1; Energy Management A1 Address (0-2) |
| `200` | `A2` | `0..9` | `0` | A2; Energy Management A2 Address (0-9) |
| `200` | `A3` | `0..9` | `1` | A3; Energy Management A3 Address (0-9) |
| `200` | `G` | `0..4` | `0` | G; G - (0-4) |
| `200` | `M` | `0..3` | `0` | M; Mode (0-3) |
| `200` | `SM` | `0..3` | `0` | SM; Configurator SM Energy Mng (0-3) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `204` - Pulse output sensor interface

Catalogue Object key `481` maps to external Object `204`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A123` | `0..255` | `0` | Address; Energy Management A123 Address (0-255) |
| `G` | `0..4` | `0` | G; G - (0-4) |
| `M` | `0..3` | `0` | Modality; Mode (0-3) |
| `SM` | `0..3` | `0` | Divider; Configurator SM Energy Mng (0-3) |

### Device-specific interpretation

Official/default wildcard firmware `200` declares one Module with external Object `204` (catalogue key 481), and only Physical Configuration mode 0. There are no Virgin Objects or connection/parameter/package associations. Firmware A1=`0..2`, A2/A3=`0..9`, defaults 0/0/1; reusable A123=`0..255`, default 0. Empty condition `4158` links all 256 rule-520 branches, `A123=100`×A1+10×A2+A3; independent digit combinations `256..299` have no stored conversion branch. G/M/SM defaults are 0 with domains `0..4`/`0..3`/`0..3`; G filter `732` retains its full range. Manufacturer physical `M=1` gas, 2 heat, 3 water, 4 generic/future differs from catalogue `M=0..3`. No offset mapping is stored, and rule `520` addresses only A123. G and the virtual-configuration button are marked future applications by the exact sheet; do not turn their presence into enabled functionality or a Virtual Configuration catalogue mode.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `200` | `1` | `204` | `4158` | No textual predicate stored | `520` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `200` | `204` | `732` | `G` | `0..4` (entire reusable range retained) | `0` | G |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `1031` / `modobj = 3` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`204`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `204` Pulse output sensor interface | New energy saving and load control | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

The retained pulse-interface sheet establishes instantaneous-value calculation and hourly/daily/monthly counters with one-year memory. Archiving requires a source of current date/time on the system; without it, totalizers and instantaneous calculations continue but historical data is not archived. Partial data is saved on loss of power.

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Consumption history | Hourly/daily/monthly archive for one year requires a system date/time source, e.g. Touchscreen | MQ00359-b-UK, p. 1; without clock only total/instantaneous data continue |
| Power loss | Partial acquired data retained across loss of supply | Same source; installed retention not observed |
| Instantaneous value | Description refers both to averaging two pulses and to elapsed-time/multiplier calculation within one hour | Same source; no universal extra conversion formula inferred |
| Physical type / scale | `M=1` gas, 2 heat, 3 water, 4 generic/future; `SM=0/1/2/3` divides by 1/10/100/1000 | Same source, p. 2; G marked future application |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

MQ00359-b-UK, printed/PDF p. 2, uses A1/A2/A3 as hundreds/tens/units with maximum address 255. M selects the physical meter type and SM the pulse multiplier; `SM=0` is recommended, independently of the recorded software default. G and the configuration button are explicitly future applications. No local factory-reset, download or firmware-update procedure is supplied.

### Pulse-unit examples

The p. 2 table was visually checked because its merged cells are flattened by text extraction.

| Unit / meter pulse output | SM | Display resolution | Display full scale |
| --- | --- | --- | --- |
| Litres; one pulse per litre | 0 | 1 L/h | 254 L/h |
| Cubic metres; one pulse per 1000 litres | 0 | 1 m³/h | 254 m³/h |
| Cubic metres; one pulse per 100 litres | 1 | 1 m³/h | 254 m³/h |
| Cubic metres; one pulse per 10 litres | 2 | 1 m³/h | 254 m³/h |
| Cubic metres; one pulse per litre | 3 | 1 m³/h | 254 m³/h |

## Source reconciliation

The technical sheet filename MQ00359_b_EN prints MQ00359-b-UK dated 11/12/2012. The item’s M=`0..3` software enum differs from its physical M=`1..4` instructions; no stored offset conversion resolves them. The regional BR catalogue cross-reference (printed/PDF p. 34) maps old 03554 to 3522, while the canonical commercial record uses 003554. This padding difference is preserved, not rewritten as a different identity. 3522N is a separate technical item and supplies no borrowed specifications here.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- The physical/software M mapping and unspecified address-zero semantics remain unresolved; stored domains are retained unchanged.
- Linked later 3522N documentation is outside this exact product scope; no payload or runtime measurements are available.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0096)
