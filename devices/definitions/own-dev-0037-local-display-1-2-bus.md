# Local Display 1.2 inch bus

## Summary

Local Display 1.2 is a compact OLED touchscreen for configured MyHOME functions such as scenarios, temperature, sound, consumption and load management. Its software configuration can present one to four functions within a two-module wall device.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0037` | Project identity |
| Technical description | Two-module 1.2-inch OLED touch display for up to four MyHOME functions | Catalogue + `MQ00692-b-EN` |
| Commercial identities | `L/N/NT4891`, `HC/HS/HD4891`, `067271`, `067272`, `573716`, `573717` | Catalogue + official documentation |
| Catalogue item | `1657` | Implementation evidence |
| Main catalogue system | Local Display / multifunction user interface | Implementation evidence |
| Item model / `modobj` | `70` | Implementation evidence |
| Firmware definition | `11` / `1.0.1` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | User interface, Scenario, Sound, Temperature control, Energy management | Capability model |

The Local Display is one Physical Device with two catalogue Modules: a function-selected first Module and a fixed Local Display Module. The function selector exposes several protocol roles without turning the product into separate Devices.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4891` | established grouped identity | catalogue + `MQ00692-b-EN` |
| BTicino - Axolute | `HC/HS/HD4891` | established grouped identity | catalogue + `MQ00692-b-EN` |
| Legrand - Céliane | `067271` | established identity | catalogue + `MQ00692-b-EN` |
| Legrand - Céliane | `067272` | established identity | catalogue + `MQ00692-b-EN` |
| Legrand - Arteor | `573716` | established identity | catalogue + `MQ00692-b-EN` |
| Legrand - Arteor | `573717` | established identity | catalogue + `MQ00692-b-EN` |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00692-b-EN` | Technical sheet | revision b / 2014-04-17 | all six current catalogue identity groups; hardware, configuration and available functions | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/56/b856e489d0b6da84d20534a4aafdd61d540cc2d46b15edb0c9c47d0e12d59bc6.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00692_b_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | 1.2-inch OLED touch display | `MQ00692-b-EN` |
| Mounting | 2 flush-mounted modules | `MQ00692-b-EN` |
| BUS supply | `18..27 Vdc` | `MQ00692-b-EN` |
| Standby current | max `10 mA` at `27 Vdc` / max `15 mA` at `18 Vdc` | `MQ00692-b-EN` |
| Operating current | max `50 mA` at `27 Vdc` / max `70 mA` at `18 Vdc` | `MQ00692-b-EN` |
| Operating temperature | `5..35 °C` | `MQ00692-b-EN` |
| Local connections | SCS BUS, external temperature probe terminal and USB | `MQ00692-b-EN` |
| Software capacity | `1..4` configured functions | `MQ00692-b-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1657` | Implementation evidence |
| Main system | Local Display / multifunction user interface | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `70` | Implementation evidence |
| Catalogue buses | `1`, `11`, `12`, `16`, `19` | Implementation evidence |
| Commercial records | `6` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `11` | `1` | `0` | `1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `11` | `1` | `419` Sound diffusion control | Candidate alternative | `2382` | `419` | `1037` |
| `11` | `1` | `191` Local display as temperature control probe | Candidate alternative | `2384` | `460` | `1039` |
| `11` | `1` | `197` Energy load control actuator | Candidate alternative | `2385` | `468` | `1040` |
| `11` | `1` | `221` Slave probe | Candidate alternative | `2383` | `546` | `1038` |
| `11` | `1` | `433` Scenario module control - local display | Fixed/designated metadata | `2381` | `617` | `1036` |
| `11` | `2` | `108` Local Display | Fixed/designated metadata | `2387` | `618` | `1042` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The first slot is function-selected while Object `108` remains fixed at slot `2`. No Virgin Object relation is present for firmware `11`.

## Configuration modes

| Mode | Meaning | Evidence |
| --- | --- | --- |
| `4` | Product Programming | Implementation evidence + USB/software configuration in `MQ00692-b-EN` |

The official sheet also documents physical configurator use. Catalogue mode `4` describes the implementation programming association; it does not erase the physical configuration surface printed on the product.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `11` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `11` | `A` | `0..9` | `0` | A; Environment |
| `11` | `PL` | `0..9` | `0` | PL; Light Point |
| `11` | `MOD` | `0..4` | `0` | MOD; Mode 0-4 |
| `11` | `FUN` | `0..4` | `0` | FUN; Configurator FUN |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | catalogue address field corresponding to the first zone/address configurator position |
| `PL` | `0..9` | catalogue address field corresponding to the second zone/address configurator position |
| `MOD` | `0..4` | mode selector |
| `FUN` | stored enum `0..4` | function selector; slot conditions also reference `FUN=5` |


The rear product labelling uses `ZA/ZB`, `MOD` and `FUN`, while firmware `11` names the two address fields `A` and `PL`. This naming difference is preserved. More importantly, the stored `FUN` enumeration stops at `4` while catalogue slot condition `4931` selects Object `197` with `FUN=5`.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `419` - Sound diffusion control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON`/`OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |


### Object `191` - Local display as temperature control probe

Catalogue Object key `460` maps to external Object `191`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `SLA` | `0..8` | `0` | Slave number |
| `COLD` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `WARM` | `0` = Disable; `1` = Enable | `0` | Winter modality; Winter mode |
| `ZAZB_CENTRAL` | `1..99` | `01` | Control unit address |


### Object `197` - Energy load control actuator

Catalogue Object key `468` maps to external Object `197`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase; Local Address of device |
| `P` | `1..63` | `1` | Priority; Local Address of device |
| `LOAD_TYPE` | `0` = Single phase; `1` = Three phases | `0` | Load type |
| `STATE_ON_ENABLE` | `0` = Previous status; `1` = `OFF` | `0` | Status of load upon central unit enabling |
| `VOLTAGE_TYPE` | `0` = AC; `1` = DC | `0` | AC or DC voltage |
| `AC_RATED_VOLTAGE` | `0` = Automatic detection; `1` = 1 V; `2` = 2 V; `3` = 3 V; `4` = 4 V; `5` = 5 V; `6` = 6 V; `7` = 7 V; `8` = 8 V; `9` = 9 V; `10` = 10 V; `11` = 11 V; `12` = 12 V; `13` = 13 V; `14` = 14 V; `15` = 15 V; `16` = 16 V; `17` = 17 V; `18` = 18 V; `19` = 19 V; `20` = 20 V; `21` = 21 V; `22` = 22 V; `23` = 23 V; `24` = 24 V; `25` = 25 V; `26` = 26 V; `27` = 27 V; `28` = 28 V; `29` = 29 V; `30` = 30 V; `31` = 31 V; `32` = 32 V; `33` = 33 V; `34` = 34 V; `35` = 35 V; `36` = 36 V; `37` = 37 V; `38` = 38 V; `39` = 39 V; `40` = 40 V; `41` = 41 V; `42` = 42 V; `43` = 43 V; `44` = 44 V; `45` = 45 V; `46` = 46 V; `47` = 47 V; `48` = 48 V; `49` = 49 V; `50` = 50 V; `51` = 51 V; `52` = 52 V; `53` = 53 V; `54` = 54 V; `55` = 55 V; `56` = 56 V; `57` = 57 V; `58` = 58 V; `59` = 59 V; `60` = 60 V; `61` = 61 V; `62` = 62 V; `63` = 63 V; `64` = 64 V; `65` = 65 V; `66` = 66 V; `67` = 67 V; `68` = 68 V; `69` = 69 V; `70` = 70 V; `71` = 71 V; `72` = 72 V; `73` = 73 V; `74` = 74 V; `75` = 75 V; `76` = 76 V; `77` = 77 V; `78` = 78 V; `79` = 79 V; `80` = 80 V; `81` = 81 V; `82` = 82 V; `83` = 83 V; `84` = 84 V; `85` = 85 V; `86` = 86 V; `87` = 87 V; `88` = 88 V; `89` = 89 V; `90` = 90 V; `91` = 91 V; `92` = 92 V; `93` = 93 V; `94` = 94 V; `95` = 95 V; `96` = 96 V; `97` = 97 V; `98` = 98 V; `99` = 99 V; `100` = 100 V; `101` = 101 V; `102` = 102 V; `103` = 103 V; `104` = 104 V; `105` = 105 V; `106` = 106 V; `107` = 107 V; `108` = 108 V; `109` = 109 V; `110` = 110 V; `111` = 111 V; `112` = 112 V; `113` = 113 V; `114` = 114 V; `115` = 115 V; `116` = 116 V; `117` = 117 V; `118` = 118 V; `119` = 119 V; `120` = 120 V; `121` = 121 V; `122` = 122 V; `123` = 123 V; `124` = 124 V; `125` = 125 V; `126` = 126 V; `127` = 127 V; `128` = 128 V; `129` = 129 V; `130` = 130 V; `131` = 131 V; `132` = 132 V; `133` = 133 V; `134` = 134 V; `135` = 135 V; `136` = 136 V; `137` = 137 V; `138` = 138 V; `139` = 139 V; `140` = 140 V; `141` = 141 V; `142` = 142 V; `143` = 143 V; `144` = 144 V; `145` = 145 V; `146` = 146 V; `147` = 147 V; `148` = 148 V; `149` = 149 V; `150` = 150 V; `151` = 151 V; `152` = 152 V; `153` = 153 V; `154` = 154 V; `155` = 155 V; `156` = 156 V; `157` = 157 V; `158` = 158 V; `159` = 159 V; `160` = 160 V; `161` = 161 V; `162` = 162 V; `163` = 163 V; `164` = 164 V; `165` = 165 V; `166` = 166 V; `167` = 167 V; `168` = 168 V; `169` = 169 V; `170` = 170 V; `171` = 171 V; `172` = 172 V; `173` = 173 V; `174` = 174 V; `175` = 175 V; `176` = 176 V; `177` = 177 V; `178` = 178 V; `179` = 179 V; `180` = 180 V; `181` = 181 V; `182` = 182 V; `183` = 183 V; `184` = 184 V; `185` = 185 V; `186` = 186 V; `187` = 187 V; `188` = 188 V; `189` = 189 V; `190` = 190 V; `191` = 191 V; `192` = 192 V; `193` = 193 V; `194` = 194 V; `195` = 195 V; `196` = 196 V; `197` = 197 V; `198` = 198 V; `199` = 199 V; `200` = 200 V; `201` = 201 V; `202` = 202 V; `203` = 203 V; `204` = 204 V; `205` = 205 V; `206` = 206 V; `207` = 207 V; `208` = 208 V; `209` = 209 V; `210` = 210 V; `211` = 211 V; `212` = 212 V; `213` = 213 V; `214` = 214 V; `215` = 215 V; `216` = 216 V; `217` = 217 V; `218` = 218 V; `219` = 219 V; `220` = 220 V; `221` = 221 V; `222` = 222 V; `223` = 223 V; `224` = 224 V; `225` = 225 V; `226` = 226 V; `227` = 227 V; `228` = 228 V; `229` = 229 V; `230` = 230 V; `231` = 231 V; `232` = 232 V; `233` = 233 V; `234` = 234 V; `235` = 235 V; `236` = 236 V; `237` = 237 V; `238` = 238 V; `239` = 239 V; `240` = 240 V; `241` = 241 V; `242` = 242 V; `243` = 243 V; `244` = 244 V; `245` = 245 V; `246` = 246 V; `247` = 247 V; `248` = 248 V; `249` = 249 V; `250` = 250 V; `251` = 251 V; `252` = 252 V; `253` = 253 V; `254` = 254 V; `255` = 255 V | `0` | AC voltage |
| `POWER_FACTOR` | `0..100` | `0` | Power factor (%) |
| `IDIFF_LOW_THR` | `0..30` | `5` | Low threshold value for differential current diagnostic (mA) |
| `IDIFF_HIGH_THR` | `0..30` | `15` | High threshold value for differential current diagnostic (mA) |
| `STANDBY_THRESHOLD` | `0..255` | `50` | Stand-by power threshold for energy management actuators (W) |
| `DC_RATED_VOLTAGE` | `1..255` | `24` | DC voltage (V) |
| `WITH_SENSOR` | `1` = Yes | `1` | With sensor |


### Object `221` - Slave probe

Catalogue Object key `546` maps to external Object `221`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `SLA` | `1..9` | `1` | Slave number |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `EXTERNAL_SENSOR_TYPE` | `0` = BTicino 3457; `1` = Vantage 8051 | `0` | External temperature sensor type |
| `RISC` | `0` = Disable; `1` = Enable | `1` | Winter modality; Winter mode |
| `COND` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `ZAZB_CENTRALE` | `00..99` | `01` | Temperature Control unit address |


### Object `433` - Scenario module control - local display

Catalogue Object key `617` maps to external Object `433`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `SCE_BUTT_1` | `1..16` | `1` | Button 1 |
| `SCE_BUTT_2` | `1..16` | `2` | Button 2 |
| `SCE_BUTT_3` | `1..16` | `3` | Button 3 |
| `SCE_BUTT_4` | `1..16` | `4` | Button 4 |


### Object `108` - Local Display

Catalogue Object key `618` maps to external Object `108`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDRESS` | `0..95` | `0` | Address |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `11` | `1` | `419` | `4913` | `FUN=2` | None |
| `11` | `1` | `191` | `4930` | `FUN=4` | None |
| `11` | `1` | `197` | `4931` | `FUN=5` | None |
| `11` | `1` | `221` | `4929` | `FUN=3` | None |
| `11` | `1` | `433` | `4912` | `FUN=1` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `11` | `221` | `3755` | `EXTERNAL_SENSOR_TYPE` | `0` = BTicino 3457; `1` = Vantage 8051 (entire reusable range retained) | `0` | External temperature sensor type |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Product interpretation and source differences

| Condition ID | Slot | Predicate | Selected Object | Meaning |
| --- | --- | --- | --- | --- |
| `4912` | `1` | `FUN=1` | `433` | scenario function |
| `4913` | `1` | `FUN=2` | `419` | sound diffusion function |
| `4929` | `1` | `FUN=3` | `221` | slave temperature probe |
| `4930` | `1` | `FUN=4` | `191` | local display temperature-control probe |
| `4931` | `1` | `FUN=5` | `197` | energy/load-control function |

| Filter ID | Object | Field | Meaning |
| --- | --- | --- | --- |
| `3755` | `221` | `EXTERNAL_SENSOR_TYPE` | External temperature sensor type |

The `FUN=5` condition lies outside the stored firmware `FUN` enum `0..4`. It is retained as a catalogue inconsistency and must not be “corrected” by guessing whether the condition or enum is stale.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 70` and product identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | corroborate firmware `1.0.1` | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | identify the function-selected slot-1 Object and fixed Object `108` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | observe the address context for the selected function | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configured `A`/`PL`/`MOD`/`FUN` and software/physical configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The publisher lists scenario control, temperature control, sound system, consumption display, load management and software-only advanced scenario functions. The active OpenWebNet-facing first Module depends on `FUN`; Object `108` represents the Local Display itself as the second Module.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained. Runtime testing is especially useful here because `FUN=5` is present in topology conditions but absent from the stored firmware enum.

## Programming

The USB interface supports configuration, firmware-related operations and character/icon resources. Programming software must resolve the function-selected Object before presenting Object-specific settings and must preserve the `A`/`PL` versus printed `ZA/ZB` naming boundary.

## Source reconciliation

`MQ00692-b-EN` corroborates all six commercial identity groups, the two-module hardware, 1.2-inch display, electrical limits, USB/external-probe connections and the product-level function set. The catalogue adds the two-Module topology and exact reusable Object surfaces.

Two implementation tensions remain explicit: the database names the physical address fields `A`/`PL` while the product labels them `ZA/ZB`, and `EN_CONF_RANGE` lists `FUN=0..4` while slot condition `4931` requires `FUN=5`.

## Evidence limits and open work

- Hardware-corroborate `DIMENSION 30` for each available `FUN` role.
- Determine whether `FUN=5` is accepted by firmware `1.0.1` despite its absence from the stored firmware enum.
- Correlate the catalogue `A`/`PL` field names with the printed `ZA/ZB` positions through a real configuration read.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MQ00692-b-EN` archived original](https://archive.openwebnet-ha.org/sha256/b8/56/b856e489d0b6da84d20534a4aafdd61d540cc2d46b15edb0c9c47d0e12d59bc6.pdf)
