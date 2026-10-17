# Local Display

## Summary

Local Display is a compact touch interface for MyHOME. Its configured pages provide scenario, sound and temperature controls; later retained manuals also describe energy display and load management. Available controls depend on the configured applications and connected system.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0018` | Project identity |
| Technical description | Multifunction local display for scenarios, sound and temperature-control functions | Catalogue + product documentation |
| Catalogue item | `1147` - Local Display | Implementation evidence |
| Main catalogue system | Temperature control; also Automation | Implementation evidence |
| Item model / `modobj` | `64` | Implementation evidence |
| Firmware definition | `1.3 build 7` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connection | USB | Implementation evidence |
| Categories | User Interface, Multifunction, Thermoregulation, Scenarios | Capability model |

The Local Display is a multifunction wall user interface whose catalogue topology is selected by the firmware-level `FUN` parameter. The same Physical Device can expose scenario-control, sound-diffusion, or temperature-probe behavior. The catalogue therefore must be read as a conditional topology rather than as three simultaneous fixed functions.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4685` | Documented 4685-family identity | Catalogue + family documentation |
| BTicino - LivingLight | `L/N/NT4685` | Documented 4685-family identity | Catalogue + family documentation |
| Legrand - Arteor | `573916` | Established catalogue identity | Implementation evidence |
| Legrand - Arteor | `573917` | Established catalogue identity | Implementation evidence |
| Legrand - Céliane | `067281` | Established catalogue identity | Implementation evidence |
| Legrand - Céliane | `067282` | Established catalogue identity | Implementation evidence |

All six records share catalogue item `1147` and `modobj` 64. Direct variant-specific documentation remains desirable for the Legrand references.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U1063B` | Instruction sheet | No dated imprint established in inspected original | 4685 Local Display family instruction sheet | not archived in repository | [Official source](https://dar.bticino.com/asset/Documents/U1063B.pdf) |
| MyHOME catalogue `HPML0714` | Product catalogue | No dated imprint established in inspected original | Generic “Local display - Sound distribution” context on printed p. 5 / PDF p. 5; the `4685` family is not named | [Archived MyHOME catalogue](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | publisher source not currently retained |
| `O2189D_U_EN.pdf` | Manufacturer user manual | 10/14-01 PC | Local Display: PDF pp. 6–28 inspected for scenario/sound/temperature/energy/load operation. No build cutoff established. | [Archived original](https://archive.openwebnet-ha.org/sha256/06/55/06556aebd384e635cdc57be4eb608cc4ea280c25aeccf435f743df353d8a4524.pdf) | Publisher URL not retained in manifest |
| `O2189C_S_EN.pdf` | Manufacturer software manual | Revision C; dated imprint not established | Local Display: complete software manual inspected, PDF pp. 4–20; project limits, USB/bus connection and application settings. | [Archived original](https://archive.openwebnet-ha.org/sha256/09/21/0921999650dac001f3e2aa6736f2d4066c4d11599711df9d68c45c245b4282a7.pdf) | [Publisher source](https://dar.bticino.com/asset/Documents/O2189C_S_EN.pdf) |

The U1063B manufacturer endpoint was rechecked during this review: DAR returned HTTP 403 and the assets endpoint HTTP 404. The older external reference copy is an unretained discovery lead, not a retained original or accepted technical specification. The HPML0714 catalogue provides generic Local Display context without naming this cluster. The retained O2189 user/software manuals now supply direct manufacturer application/procedure evidence; their relationship to each historical hardware/firmware variant is not fully established.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| User interface | Touch display with text and icons | O2189D_U_EN, p. 6; its LCD note is source wording |
| Programming connection | USB–miniUSB; device must be connected to the bus for communication | O2189C_S_EN, p. 4 |
| Temperature arrangement | Configured local/slave probes; with 4/99-zone central unit or as standalone thermostat without one | O2189C_S_EN, pp. 13–14 |

Electrical ratings, external probe 3457 characteristics and historical serial connection from the unretained U1063B copy remain unverified leads under Evidence limits. The later manual’s LCD wording and the older OLED description do not establish a hardware revision boundary.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1147` | Implementation evidence |
| Main system | thermoregulation / Temperature control | Implementation evidence |
| Additional system | lighting_automation / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `64` in both mappings | Implementation evidence |
| Family | `1` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `64` | No | Canonical item/system relationship |
| Temperature control | `64` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `110` | `1` | `3` | `7` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

The catalogue declares Product Programming only and a USB programming connection. That is materially different from many configurable command Devices: the Local Display topology is selected through product-level configuration rather than represented as a generic Virgin Object.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `110` | `114` | BTicino (key `1`) | `0` | external software | `TiLocalDisplay_0200` |
| `110` | `187` | Unspecified (key `0`) | `0` | external software | `TiLocalDisplay_0102` |
| `110` | `259` | Legrand (key `2`) | `2` | external software | `LocalDisplayConfig_0102` |
| `110` | `260` | BTicino (key `1`) | `3` | external software | `TiLocalDisplay_0102` |
| `110` | `261` | BTicino (key `1`) | `1` | external software | `TiLocalDisplay_0102` |
| `110` | `262` | Legrand (key `2`) | `4` | external software | `LocalDisplayConfig_0102` |

All 6 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `110` | `1` | `413` Scenario module control | Fixed/designated metadata | `1199` | `413` | `647` |
| `110` | `1` | `419` Sound diffusion control | Candidate alternative | `1203` | `419` | `648` |
| `110` | `1` | `191` Local display as temperature control probe | Candidate alternative | `1195` | `460` | `646` |
| `110` | `2` | `413` Scenario module control | Candidate alternative | `1200` | `413` | `647` |
| `110` | `2` | `419` Sound diffusion control | Fixed/designated metadata | `1204` | `419` | `648` |
| `110` | `2` | `191` Local display as temperature control probe | Candidate alternative | `1196` | `460` | `646` |
| `110` | `3` | `413` Scenario module control | Candidate alternative | `1201` | `413` | `647` |
| `110` | `3` | `419` Sound diffusion control | Candidate alternative | `1205` | `419` | `648` |
| `110` | `3` | `191` Local display as temperature control probe | Fixed/designated metadata | `1197` | `460` | `646` |
| `110` | `4` | `413` Scenario module control | Candidate alternative | `1202` | `413` | `647` |
| `110` | `4` | `419` Sound diffusion control | Candidate alternative | `1206` | `419` | `648` |
| `110` | `4` | `191` Local display as temperature control probe | Fixed/designated metadata | `1198` | `460` | `646` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

Three reusable Objects are mapped across the four catalogue slots:
There is no Virgin Object. Conditions `FUN=1`, `FUN=2`, `FUN=3` and `FUN=4` are explicit catalogue predicates. `FUN=3` and `FUN=4` intentionally select the same reusable Object in the current source; this dossier does not invent a distinction not represented by that source.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `110` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `110` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `110` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `110` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `110` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `110` | `M` | `0`; `3..8` | `0` | M; Mode (None,3,4,5,6,7,8) |
| `110` | `FUN` | `0..4` | `0` | FUN; Configurator FUN |

The database labels `M=0` and `FUN=0` as None. Numeric M values `3..8` and `FUN` values `1..4` are preserved as raw catalogue values unless a product document supplies stronger names.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `413` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

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

### Device-specific interpretation

Catalogue `FUN=3` and `FUN=4` select the same external probe Object `191` (internal key 460). This is a stored relationship, not evidence of identical product wiring or firmware behavior. Later software supports energy functions not separately represented by the 1.3.7 Object inventory.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `110` | `1` | `413` | `4912` | `FUN=1` | None |
| `110` | `1` | `419` | `4913` | `FUN=2` | None |
| `110` | `1` | `191` | `4190` | `FUN=3` | `1000` |
| `110` | `1` | `191` | `4191` | `FUN=4` | `1000` |
| `110` | `2` | `413` | `4912` | `FUN=1` | None |
| `110` | `2` | `419` | `4913` | `FUN=2` | None |
| `110` | `2` | `191` | `4190` | `FUN=3` | `1000` |
| `110` | `2` | `191` | `4191` | `FUN=4` | `1000` |
| `110` | `3` | `413` | `4912` | `FUN=1` | None |
| `110` | `3` | `419` | `4913` | `FUN=2` | None |
| `110` | `3` | `191` | `4190` | `FUN=3` | `1000` |
| `110` | `3` | `191` | `4191` | `FUN=4` | `1000` |
| `110` | `4` | `413` | `4912` | `FUN=1` | None |
| `110` | `4` | `419` | `4913` | `FUN=2` | None |
| `110` | `4` | `191` | `4190` | `FUN=3` | `1000` |
| `110` | `4` | `191` | `4191` | `FUN=4` | `1000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1000` | `ZA=0; ZB=1..9` | `ZAZB=01..09` | Rule `1000` through branch `1001` |
| `1000` | `ZA=1..9; ZB=0..9` | `ZAZB=10..99` | Rule `1000` through branches `1002..1010` |
| `1000` | `ZA=0; ZB=0` | No `00` mapping stored | Do not widen the conversion from the reusable Object domain |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Product interpretation and source differences

| Selector | Object | Applicability |
| --- | --- | --- |
| `FUN=1` | `413` | scenario module control |
| `FUN=2` | `419` | sound diffusion control |
| `FUN=3` | `191` | temperature-control probe role |
| `FUN=4` | `191` | temperature-control probe role; product documentation distinguishes role context |

The same Object for `FUN=3` and `FUN=4` is intentional in the current implementation source and must not be split without evidence.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 64 and commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | confirm installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | observe which conditional Modules are exposed | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect addresses for the selected role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | correlate `FUN` / `M` and role-specific configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

A hardware fingerprint is especially valuable here because `DIMENSION 30` can test whether runtime exposure follows the source-level `FUN` conditions exactly.

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Scenario | Four displayed scenario keys; enabled module required for learning; 3-second icon hold to program, 30-second inactivity exit, 10-second hold to delete | O2189D_U_EN, pp. 8–10 |
| Sound / alarm clock | Amplifier On/Off/volume, up to four sources, station/track controls; sound or beep alarm clock | Same source, pp. 12–15 |
| Temperature with central unit | 4-zone local offset −3..+3 °C; 99-zone temporary setpoint in 0.5 °C steps; fan-coil auto/speeds `1..3`, protection/Off/automatic | Same source, pp. 16–18 |
| Standalone thermostat | Without central unit, local manual/protection/Off with summer/winter choice | Same source, p. 19; software pp. 13–14 |
| Energy display | Up to ten displayed items, consumption/production, cumulative period data, tariff evaluation and two alarm thresholds | User pp. 8, 20–24; software p. 19 |
| Load management | Up to twenty displayed loads, shed-state display and forcing; consumption requires advanced actuators | User pp. 8, 25–26; software p. 12 |

These functions are manual-scoped. Energy and programmed-scenario UI elements in later manuals do not establish new Objects in the stored firmware-110 model.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

The retained software manual specifies USB–miniUSB with bus power for configuration transfer, firmware update and Device Info. Projects provide a local address and standby timeout; up to four functions can be included (pp. 4–9). Its application settings distinguish load central-unit address, load priority `1..255` and Basic/Advanced interface; zone address, local/slave probes, 4/99-zone central-unit association or thermostat actuators/pumps; amplifier A/PF and source list; F420 scenario number or CEN/CEN PLUS button/address; energy meter address `1..255`, production/consumption, two thresholds and DataLogger presence (pp. 12–20). These UI ranges are not replacements for firmware-110 fields/restrictions.

Catalogue FUN conditions determine its stored Object projection. `FUN=3` and `FUN=4` both reference external Object `191`; no new distinct protocol Object is invented from the UI. The unretained older instruction copy’s serial connector and exact FUN wiring interpretation require original/revision confirmation. For scenario learning the module must itself permit programming; deleting a displayed scenario and erasing a module’s entire memory are distinct operations.

## Source reconciliation

O2189D’s October 2014 user manual and O2189C’s software manual document a broader Local Display interface than the original page’s three-role synopsis. The software sets a maximum of four functions, agreeing with the user introduction; the user p. 8 also says “four or five” while listing five available categories. This internal wording is preserved without adopting five simultaneous functions. Load priority and meter addresses reach 255 in the software manual, while other load products have narrower ranges; those Device-specific namespaces remain separate.

The 1.3.7 catalogue supplies four conditional slots and no Virgin Object; its temperature Object is external 191, internal key 460. It lacks separate energy/load/CEN PLUS Objects despite their later manual UI descriptions. No source establishes a firmware cutoff, an automatic topology upgrade or physical equivalence across all variants. U1063B’s alleged `FUN=3` external-probe/`FUN=4` probe-role distinction remains a provisional discovery finding requiring retained evidence, not a resolved installed behavior. Later USB/bus documentation does not establish that the historical serial wording was false.

## Evidence limits and open work

- Obtain sanitized fingerprints for at least one BTicino 4685 and one Legrand commercial variant.
- Archive the official `U1063B` revision when the publisher endpoint permits automated retrieval.
- Find direct official sheets for `573916`/`573917` and `067281`/`067282`.
- Establish vendor-facing names for `M=3..8` and verify the documented `FUN=3` / `FUN=4` distinction against an archived `U1063B` original and real hardware.
- Check whether firmware later than catalogue `1.3.7` changes role selection or slot anchoring.
- The unretained U1063B copy previously supplied OLED, BUS/serial/probe connectors, probe 3457 (10 kΩ at 25 °C, BETA 3435), 10 m probe cable, `18..27` Vdc, approximately 20 mA standby/60 mA operation and `5..35` °C. These values are preserved here as unverified leads, not accepted ratings. Obtain the publisher bytes or a retained exact technical source before using them.
- Establish O2189 feature-to-firmware applicability and resolve the four/five simultaneous-function wording, old OLED/later LCD note and serial/USB source scopes.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0011-0020-2026-10-05.md#own-dev-0018)
