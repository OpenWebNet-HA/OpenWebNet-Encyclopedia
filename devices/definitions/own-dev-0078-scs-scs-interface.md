# SCS/SCS interface

## Summary

`F422` / `003562` connects SCS bus sections and systems through separate IN and OUT terminals. Its configured role determines whether it extends a bus, separates address spaces, links burglar-alarm or sound functions, supervises public-riser alarms, or learns device placement for physical separation.

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
| `MQ00280-f-EN` | technical sheet | MQ00280-f-EN;2015-03-18 | Printed/PDF pp. 1–10;complete exactF422 ratings,six published roles,installation/address-learning and combined-mode diagrams | [Archived original](https://archive.openwebnet-ha.org/sha256/16/dd/16ddee94af03d514235d5d4c0e781be9bea0a5973b7dfbbf8dfe8e195a731b6e.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00280_f_EN.pdf) |
| F460/F461 installation/configuration compatibility table | compatibility documentation | RA00224AA;retained publisher revision | PDF p. 7: `F422` / `003562` pairing and direct association from batch `12W20`; distinct `F422 A` row for all batches | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/a4/d2a45bbcd72baa0b6e5536baccca8816cce3cdf94414e7b7144763003c1b1e6d.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00224AA_EN.pdf) |
| `F422-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1;exact-reference EAN and complete technical export attributes examined;linked downloads/prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/4d/9a/4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F422) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply/current | `27 Vdc` SCS, `18..27 Vdc` operating; IN25 mA, OUT5 mA; `1 W` maximum dissipation | MQ00280-f-EN, p. 1 |
| Construction | Two DIN modules; IN/OUT bus terminals, configurator socket, LED and C button | MQ00280-f-EN, p. 1 |
| LED states | Steady: supply/configuration correct; off: bus absent; flashing: configuration missing/incorrect | MQ00280-f-EN, p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `90` | Canonical catalogue |
| Technical item | SCS/SCS interface | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `251` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `151` | Yes | Canonical item/system relationship |
| Video door entry system | `69` | No | Canonical item/system relationship |
| Integration function | `251` | No | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `90` | `F422` | `1` | `5` | `BTicino_Undefined_SCS-SCS gateway` |
| `1592` | `003562` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `143` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |
| `722` | `6` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

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

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `143` | Physical configuration | `0` | Canonical firmware/mode association |
| `143` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `722` | Physical configuration | `0` | Canonical firmware/mode association |
| `722` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `722` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

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

| Surface | Fields | Meaning |
| --- | --- | --- |
| Operation, timing and presentation | `I4`, `ADDRESSES_MANAGED_1`, `ADDRESSES_MANAGED_2`, `ADDRESSES_MANAGED_3`, `ADDRESSES_MANAGED_4`, `ADDRESSES_MANAGED_5`, `ADDRESSES_MANAGED_6`, `ADDRESSES_MANAGED_7`, `ADDRESSES_MANAGED_8`, `ADDRESSES_MANAGED_9`, `ADDRESSES_MANAGED_10`, `ADDRESSES_MANAGED_11`, `ADDRESSES_MANAGED_12`, `ADDRESSES_MANAGED_13`, `ADDRESSES_MANAGED_14`, `ADDRESSES_MANAGED_15`, `ADDRESSES_MANAGED_16`, `ADDRESSES_MANAGED_17`, `ADDRESSES_MANAGED_18`, `ADDRESSES_MANAGED_19`, `ADDRESSES_MANAGED_20`, `ADDRESSES_MANAGED_22`, `CENTRAL_AUTOMATION_MANAGED`, `CENTRAL_ANTINTRUSION_MANAGED` | Reusable schema; apply the Device and firmware restrictions below. |

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

### Device-specific interpretation

Keep firmware `143` (-1/-1/-1, default) and `722` (6.0.0, non-default), both Official, separate. `MOD=5/access-system` Object `79` has a direct relation and condition only for firmware `143`; firmware `722` restricts MOD to `0..4` and 6 and omits that direct Object/condition, although Virgin `525` (internal key `524`) still admits Object `79` for both. This firmware-specific Virgin-only membership does not establish access-mode reachability for 722. MOD 2/1/4/3/6 select Objects 74/75/77/78/85; fixed Object `76` has no `MOD=0` predicate. All relation filters belong only to 143 and exclude reusable defaults: I4 `10..15` or `10..239`, and physical expansion I3 0 or 10. Do not inherit them into 722 or reinterpret manufacturer decimal configurators as these software values. Object `85` (internal key `496`) records address bitmaps `1..20` and 22, omits 21 (addresses `161..168`), and gives bitmap 22 f0..f6 for `169..175` without an f7 meaning. ADDRESSES_MANAGED_16 has the source description “address managed17”. Bitmap flags map 0 to IN and 1 to OUT; automation/antintrusion controls use separate flags. No conversion branch is recorded to explain encodings or repair omitted addresses.

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

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| MOD1 physical expansion | Up to 4 interfaces in series/5 individually powered sections; no parallel interfaces; separation address partitions lower IN/higher OUT addresses; does not increase 175 actuator address limit | MQ00280-f-EN, pp. 1–2 |
| MOD2 logical expansion | Local OUT systems connect to IN automation riser; up to 9 interfaces/10 systems; point-to-point stays within its system, group/general cross from riser; extended controls required for cross-system points | MQ00280-f-EN, p. 3 |
| MOD3 public riser | Common-area burglar/technical alarm display via 346310; up to 9 auxiliary channels on IN; use free video-handset address | MQ00280-f-EN, p. 4 |
| MOD4 burglar interface | Alarm bus on OUT, automation/video/sound on IN; only 1 alarm interface, no alarm-bus physical extension or automation actuators within alarm system | MQ00280-f-EN, p. 5 |
| Unconfigured MOD:galvanic separation | Separate supplies, automation on IN and other function on OUT; no multiple automation systems sharing same sound bus; no consumed automation address | MQ00280-f-EN, p. 5 |
| MOD6 physical separation | Up to 4 interfaces; each system separately powered; addresses may overlap across sides; interfaces have distinct addresses; point/room/group/general cross without the MOD1 address partition | MQ00280-f-EN, pp. 6–7 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Select role before assigning interfaces and power sections. MOD1 needs I1/I2 absent, I3/I4 `1..9` and no device sharing the separation address; place web/scenario programmer on lowest-address section. MOD2 needs I1..I3 absent, I4 `1..9`; place programmer/webserver on IN riser. MOD4/galvanic use I1..I3 absent, I4 1..9. MOD6 leaves I1/I2 absent and uses I3 `0..9`, I4 `1..9`; configure a unique interface address (physical, Virtual Configurator or button procedure), then acquire connected-device addresses only after all interface/actuator addresses are configured. The button address sequence is short press, short press to start and steady LED on completion; address acquisition uses at least 2 s. Cascades require a system between one OUT and another IN, not two OUT links; memory module goes after the final OUT. Evidence: MQ00280-f-EN pp. 1–7; combined-role diagrams pp. 8–10.

## Source reconciliation

The F460/F461 manual PDF p. 7 lists `F422`/003562 direct association from production batch 12W20 onward and separately lists `F422 A` for all batches; `F422 A` is not added to this canonical item.

The exact `F422` sheet revision f dated 18 March 2015 and the compatibility table PDF p. 7 establish `F422`/003562 scope. The technical sheet opens with “physical configuration only” and calls the C button future use in its legend, but later documents Virtual Configurator and button/self-configuration for MOD6; the latter route is retained with its specific scope. Its logical-expansion prose alternates 175 addresses with 81 in the installation rules, and example diagrams use `01..99` or `01..175`; physical/software addressing scopes and the unresolved 81/175 wording are distinguished. The MOD6 installation text gives addresses 01–99 while the configurator table restricts I4 to 1–9; that table excludes the decade addresses, so the broad range does not establish that every integer is assignable. MOD6’s example mentions Automation/Temperature Control but labels the second system Energy management; do not silently relabel the printed diagram. No access-system MOD5 is documented in this 2015 sheet, although it remains in catalogue 143. Firmware 722 has no such direct candidate. Manufacturer decimal configurators and catalogue filters/bitmaps are not assumed interchangeable.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- MOD5/access technical procedure is not covered by the retained 2015 sheet. The conflicting 81/175 wording, opening-only configuration claim, button legend and incomplete address bitmaps remain source limits.
- Virtual Configurator/self-configuration manual, 346310 switchboard sheet, linked DWG/environmental profile and installed behavior are unexamined. Catalogue LAN bus association does not establish an Ethernet connector on `F422`.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F422-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F422` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/4d/9a/4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F422); SHA-256 `4d9a1c46645f5c1e6d2dad84c789efb9bb5f27bca830339f9b03bedfc0735454`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0078)
