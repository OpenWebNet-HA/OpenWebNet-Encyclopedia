# SCS/SCS interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0078` | Project identity |
| Technical description | SCS/SCS interface | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F422`, `003562` | Canonical commercial records |
| Catalogue item | `90` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `251` | Canonical inventory |
| Firmware definition | `-1.-1.-1`; `6.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Integration, SCS gateway, Bus separation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F422` | Established identity | canonical commercial record for item `90` |
| Legrand | `003562` | Established identity | canonical commercial record for item `90` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F422` | `8012199490854` | [Archived original](https://archive.openwebnet-ha.org/sha256/4d/9a/4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454.pdf), `F422-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00280-f-EN` | technical sheet | publisher technical sheet | `F422` SCS/SCS interface electrical data and six operating modes | [Archived original](https://archive.openwebnet-ha.org/sha256/16/dd/16ddee94af03d514235d5d4c0e781be9bea0a5973b7dfbbf8dfe8e195a731b6e.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00280_f_EN.pdf) |
| MyHOME Server compatibility table | compatibility documentation | current publisher support | Corroborates `F422` / `003562` pairing; PDF p. 7 | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/a4/d2a45bbcd72baa0b6e5536baccca8816cce3cdf94414e7b7144763003c1b1e6d.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00224AA_EN.pdf) |
| `F422-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `F422` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/4d/9a/4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F422) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `MQ00280-f-EN` |
| Current draw - IN side | `25 mA` | `MQ00280-f-EN` |
| Current draw - OUT side | `5 mA` | `MQ00280-f-EN` |
| Maximum dissipated power | `1 W` | `MQ00280-f-EN` |
| Width | `2 DIN modules` | `MQ00280-f-EN` |
| Interfaces | two SCS BUS domains | `MQ00280-f-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `90` | Canonical catalogue |
| Technical item | SCS/SCS interface | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `251` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `143` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |
| `722` | `6` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `143` | `1` | `74` Interface SCS / SCS Logic | Candidate alternative | `508` | `74` | `352` |
| `143` | `1` | `75` Interface SCS / SCS physical | Candidate alternative | `509` | `75` | `353` |
| `143` | `1` | `76` Interface SCS / SCS galvanic | Fixed/designated metadata | `510` | `76` | `354` |
| `143` | `1` | `77` Interface SCS / SCS burglar alarm | Candidate alternative | `511` | `77` | `355` |
| `143` | `1` | `78` Interface SCS / SCS public riser | Candidate alternative | `512` | `78` | `356` |
| `143` | `1` | `79` Interface SCS / SCS access control | Candidate alternative | `513` | `79` | `357` |
| `143` | `1` | `85` Interface SCS / SCS physical separation | Candidate alternative | `514` | `496` | `358` |
| `722` | `1` | `74` Interface SCS / SCS Logic | Candidate alternative | `2637` | `74` | `1247` |
| `722` | `1` | `75` Interface SCS / SCS physical | Candidate alternative | `2638` | `75` | `1248` |
| `722` | `1` | `76` Interface SCS / SCS galvanic | Fixed/designated metadata | `2639` | `76` | `1249` |
| `722` | `1` | `77` Interface SCS / SCS burglar alarm | Candidate alternative | `2640` | `77` | `1250` |
| `722` | `1` | `78` Interface SCS / SCS public riser | Candidate alternative | `2641` | `78` | `1251` |
| `722` | `1` | `85` Interface SCS / SCS physical separation | Candidate alternative | `2643` | `496` | `1253` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `143` | `525` Interface_SCS_SCS_virgin | `1` | `74`, `75`, `76`, `77`, `78`, `79`, `85` | `524` | `16` |
| `722` | `525` Interface_SCS_SCS_virgin | `1` | `74`, `75`, `76`, `77`, `78`, `79`, `85` | `524` | `60` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `143` | Advanced Configuration | supported configuration route for this Device family |
| `143` | Physical configuration | supported configuration route for this Device family |
| `143` | Virtual Configuration | supported configuration route for this Device family |
| `722` | Advanced Configuration | supported configuration route for this Device family |
| `722` | Physical configuration | supported configuration route for this Device family |
| `722` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `143` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `143` | `I1` | `0..9` | `0` | I1; Automation interface address 1 |
| `143` | `I2` | `0..9` | `0` | I2; Automation interface address 2 |
| `143` | `I3` | `0..9` | `0` | I3; Automation interface address 3 |
| `143` | `I4` | `0..9` | `0` | I4; Automation interface address 4 |
| `143` | `MOD` | `0..6` | `0` | MOD; Mode 0-6 |
| `722` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `722` | `I1` | `0..9` | `0` | I1; Automation interface address 1 |
| `722` | `I2` | `0..9` | `0` | I2; Automation interface address 2 |
| `722` | `I3` | `0..9` | `0` | I3; Automation interface address 3 |
| `722` | `I4` | `0..9` | `0` | I4; Automation interface address 4 |
| `722` | `MOD` | `0..4`; `6` | `0` | MOD |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `74` - Interface SCS / SCS Logic

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I3` | `0` | `0` | Automation interface address 3 |
| `I4` | `1..15` | `1` | Automation interface address 4 |


### Object `75` - Interface SCS / SCS physical

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I3` | `0..10` | `0` | Automation interface address 3 |
| `I4` | `0..15` | `1` | Automation interface address 4 |


### Object `76` - Interface SCS / SCS galvanic

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I4` | `0..239` | `1` | Address |


### Object `77` - Interface SCS / SCS burglar alarm

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I4` | `0..15` | `0` | Address |


### Object `78` - Interface SCS / SCS public riser

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I1I2I3I4` | `0..3999` | `0` | Internal unit address |


### Object `79` - Interface SCS / SCS access control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I1` | `0` | `0` | Automation interface address 1 |
| `I2` | `0` | `0` | Automation interface address 2 |
| `I3` | `0` | `0` | Automation interface address 3 |
| `I4` | `0..15` | `1` | Automation interface address 4 |


### Object `85` - Interface SCS / SCS physical separation

Catalogue Object key `496` maps to external Object `85`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `I4` | `0..239` | `0` | Address |
| `ADDRESSES_MANAGED_1` | `0..255` | `0` | Address managed 1; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 01........f7=address 08 |
| `ADDRESSES_MANAGED_2` | `0..255` | `0` | Address managed 2; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 09........f7=address 16 |
| `ADDRESSES_MANAGED_3` | `0..255` | `0` | Address managed 3; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 17........f7=address 24 |
| `ADDRESSES_MANAGED_4` | `0..255` | `0` | Address managed 4; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 25........f7=address 32 |
| `ADDRESSES_MANAGED_5` | `0..255` | `0` | Address managed 5; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 33........f7=address 40 |
| `ADDRESSES_MANAGED_6` | `0..255` | `0` | Address managed 6; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 41........f7=address 48 |
| `ADDRESSES_MANAGED_7` | `0..255` | `0` | Address managed 7; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 49........f7=address 56 |
| `ADDRESSES_MANAGED_8` | `0..255` | `0` | Address managed 8; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 57........f7=address 64 |
| `ADDRESSES_MANAGED_9` | `0..255` | `0` | Address managed 9; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 65........f7=address 72 |
| `ADDRESSES_MANAGED_10` | `0..255` | `0` | Address managed 10; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 73........f7=address 80 |
| `ADDRESSES_MANAGED_11` | `0..255` | `0` | Address managed 11; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 81........f7=address 88 |
| `ADDRESSES_MANAGED_12` | `0..255` | `0` | Address managed 12; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 89........f7=address 96 |
| `ADDRESSES_MANAGED_13` | `0..255` | `0` | Address managed 13; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 97........f7=address 104 |
| `ADDRESSES_MANAGED_14` | `0..255` | `0` | Address managed 14; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 105........f7=address 112 |
| `ADDRESSES_MANAGED_15` | `0..255` | `0` | Address managed 15; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 113........f7=address 120 |
| `ADDRESSES_MANAGED_16` | `0..255` | `0` | Address managed 17; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 121........f7=address 128 |
| `ADDRESSES_MANAGED_17` | `0..255` | `0` | Address managed 17; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 129........f7=address 136 |
| `ADDRESSES_MANAGED_18` | `0..255` | `0` | Address managed 18; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 137........f7=address 144 |
| `ADDRESSES_MANAGED_19` | `0..255` | `0` | Address managed 19; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 145........f7=address 152 |
| `ADDRESSES_MANAGED_20` | `0..255` | `0` | Address managed 20; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 153........f7=address 160 |
| `ADDRESSES_MANAGED_22` | `0..255` | `0` | Address managed 22; fx=0 device installed in IN side, fx=1 device installed in OUT side. Addresses managed values=f7f6f5f4f3f2f1f0 f0=address 169........f6=address 175 |
| `CENTRAL_AUTOMATION_MANAGED` | `0` = Managed on IN side; `1` = Managed on OUT side | `0` | Control unit automation managed; 0x00 managed on IN side, 0x01 managed on OUT side |
| `CENTRAL_ANTINTRUSION_MANAGED` | `0` = Managed on IN side; `1` = Managed on OUT side | `0` | Control unit burglar alarm managed; 0x00 managed on IN side, 0x01 managed on OUT side |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `143` | `1` | `74` | `4698` | `MOD=2` | None |
| `143` | `1` | `75` | `4697` | `MOD=1` | None |
| `143` | `1` | `77` | `4700` | `MOD=4` | None |
| `143` | `1` | `78` | `4699` | `MOD=3` | None |
| `143` | `1` | `79` | `4895` | `MOD=5` | None |
| `143` | `1` | `85` | `4896` | `MOD=6` | None |
| `722` | `1` | `74` | `4698` | `MOD=2` | None |
| `722` | `1` | `75` | `4697` | `MOD=1` | None |
| `722` | `1` | `77` | `4700` | `MOD=4` | None |
| `722` | `1` | `78` | `4699` | `MOD=3` | None |
| `722` | `1` | `85` | `4896` | `MOD=6` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `143` | `74` | `2972` | `I4` | `10`; `11`; `12`; `13`; `14`; `15` | `1` | Automation interface address 4; reusable default `1` is outside this subset; filter supplies no replacement default |
| `143` | `75` | `2968` | `I3` | `0`; `10` | `0` | Automation interface address 3 |
| `143` | `75` | `2970` | `I4` | `0`; `10`; `11`; `12`; `13`; `14`; `15` | `1` | Automation interface address 4; reusable default `1` is outside this subset; filter supplies no replacement default |
| `143` | `76` | `2965` | `I4` | `10`; `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `11`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `12`; `120`; `121`; `122`; `123`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80`; `81`; `82`; `83`; `84`; `85`; `86`; `87`; `88`; `89`; `90`; `91`; `92`; `93`; `94`; `95`; `96`; `97`; `98`; `99`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239` | `1` | Automation interface address 4; reusable default `1` is outside this subset; filter supplies no replacement default |
| `143` | `77` | `2974` | `I4` | `10`; `11`; `12`; `13`; `14`; `15` | `0` | Automation interface address 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `143` | `79` | `2976` | `I4` | `10`; `11`; `12`; `13`; `14`; `15` | `1` | Automation interface address 4; reusable default `1` is outside this subset; filter supplies no replacement default |
| `143` | `85` | `2980` | `I4` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80`; `81`; `82`; `83`; `84`; `85`; `86`; `87`; `88`; `89`; `90`; `91`; `92`; `93`; `94`; `95`; `96`; `97`; `98`; `99`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239` | `0` | Automation interface address 4; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `90` / `modobj = 251` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`74`, `75`, `76`, `77`, `78`, `79`, `85`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

SCS/SCS interface used for physical or logical expansion, system-to-system interfacing, riser separation, galvanic separation and physical separation. The catalogue retains both wildcard firmware applicability and a concrete `6.0.0` firmware surface, with one Object difference between them.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The dedicated technical sheet documents `F422`, while current publisher compatibility documentation explicitly pairs Legrand `003562` with BTicino `F422`; commercial reconciliation is therefore established across both references.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F422-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F422` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/4d/9a/4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F422); SHA-256 `4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454`.
