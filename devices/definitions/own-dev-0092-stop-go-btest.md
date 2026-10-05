# Stop&Go Btest

## Summary

Stop&Go Btest is the separately catalogued Btest member of the Stop&Go protection-control family, integrated through MyHOME energy management. The family supports supervision and reset control; the Btest variant's specific test and recovery behaviour remains a product-documentation gap.

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
| `F4269H.pdf` | technical / instruction manual | 10W04 / revision H | Whole product document, PDF pp. 1-4; printed p. 1 for one-page catalogue exports | [Archived original](https://archive.openwebnet-ha.org/sha256/16/d6/16d6f331c180eb1fc0afbc2042f7e6aa1c0e967207e88cc3c3e8fab421254e23.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/F4269H.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product description | `Stop&Go Btest` | Catalogue item description; not a complete product specification |
| Additional electrical/mechanical characteristics | Properties not established beyond the source-scoped facts on this page | Direct product-source reconciliation remains open |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `914` | Canonical catalogue |
| Technical item | Stop&Go Btest | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `1` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `227` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `227` | Physical configuration | supported configuration route for this Device family |
| `227` | Virtual Configuration | supported configuration route for this Device family |

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

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Virtual Configuration, Physical configuration for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has one declared Module; do not treat candidate Object rows as additional channels.

The retained sources establish only the Device-specific procedures described below; reset, transfer or update details not covered by those sources remain open work. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

The retained `F4269H` installation sheet explicitly covers `F80/SG` and `F80/SGB`. It requires association with the protective device before energizing Stop&Go and distinguishes fault indicators, the local button and isolation controls. Its physical installation/activation procedure is product commissioning evidence; it is not an OpenWebNet firmware-update sequence.

## Source reconciliation

The canonical MyHOME Suite `3.5.38` catalogue establishes the commercial-to-item association, firmware definitions, Module placements, reusable configuration values and relationship-specific conditions/filters recorded above. Publisher evidence is retained as listed in Documentation; its Device-specific coverage is bounded below. Catalogue descriptions and Object names therefore remain implementation evidence; electrical limits, commissioning procedures and runtime behavior cannot be borrowed from sibling products.

The corrected tables distinguish external Object/Virgin Object numbers from database keys, firmware status from wildcard applicability and actual Module slots from slot row IDs. Remaining source acquisition and runtime checks are listed below.

## Evidence limits and open work

- Locate and archive dedicated publisher documentation for the exact commercial references where available.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
