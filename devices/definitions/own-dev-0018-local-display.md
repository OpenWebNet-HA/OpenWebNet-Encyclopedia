# Local Display

## Summary

Local Display is a compact OLED touch interface for MyHOME. Its selected configuration assigns it to scenario control, sound diffusion or temperature regulation, so its displayed controls follow the role chosen for the installation.

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
| Legrand - Arteor | `573916` | Shared technical item | Implementation evidence |
| Legrand - Arteor | `573917` | Shared technical item | Implementation evidence |
| Legrand - Céliane | `067281` | Shared technical item | Implementation evidence |
| Legrand - Céliane | `067282` | Shared technical item | Implementation evidence |

All six records share catalogue item `1147` and `modobj` 64. Direct variant-specific documentation remains desirable for the Legrand references.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U1063B` | Instruction sheet | revision/date not yet pinned | 4685 Local Display family instruction sheet | not archived in repository | [Official source](https://dar.bticino.com/asset/Documents/U1063B.pdf) |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | Generic “Local display - Sound distribution” context on printed p. 5 / PDF p. 5; the `4685` family is not named | [Archived MyHOME catalogue](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | publisher source not currently retained |

The former official `U1063B` publisher URL currently returns an access/error response and the current Legrand document CDN does not expose that filename. An external reference copy of the same `U1063B` revision has therefore been used only to recover Device facts. The older MyHOME catalogue provides only generic Local Display / sound-distribution context and does not identify the `4685` family or corroborate its complete role set. The external copy is not archived or represented as an official original; byte-for-byte publisher evidence is still required.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| User interface | OLED touch display | `U1063B` reference copy |
| Connections | BUS/SCS, serial programming connector and external-probe connector | `U1063B` reference copy |
| Supported external probe | `3457` | `U1063B` reference copy |
| External probe characteristic | `10 kΩ` at `25 °C`, `BETA = 3435` | `U1063B` reference copy |
| Maximum probe connection length | `10 m` | `U1063B` reference copy |
| SCS supply | `18..27 Vdc` | `U1063B` reference copy |
| Maximum standby consumption | approximately `20 mA` | `U1063B` reference copy |
| Maximum operating consumption | approximately `60 mA` | `U1063B` reference copy |
| Operating temperature | `5..35 °C` | `U1063B` reference copy |

These values remain provisional until the exact official `U1063B` bytes are archived; they do not override the canonical implementation topology.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1147` | Implementation evidence |
| Main system | thermoregulation / Temperature control | Implementation evidence |
| Additional system | lighting_automation / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `64` in both mappings | Implementation evidence |
| Family | `1` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `110` | `1` | `3` | `7` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

The catalogue declares Product Programming only and a USB programming connection. That is materially different from many configurable command Devices: the Local Display topology is selected through product-level configuration rather than represented as a generic Virgin Object.

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

| Mode / modality | Evidence |
| --- | --- |
| Product Programming | implementation evidence |
| USB programming connection | implementation evidence |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `110` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `110` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `110` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `110` | `M` | `0`; `3..8` | `0` | M; Mode (None,3,4,5,6,7,8) |
| `110` | `FUN` | `0..4` | `0` | FUN; Configurator FUN |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `ZA` | `0..9` | first thermoregulation zone digit |
| `ZB` | `0..9` | second thermoregulation zone digit |
| `M` | `0`, `3`, `4`, `5`, `6`, `7`, `8` | product mode configurator domain |
| `FUN` | `0`, `1`, `2`, `3`, `4` | function selector that controls Object applicability |


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


### Additional Device-specific interpretation

| Object | Role | Principal configuration |
| --- | --- | --- |
| `191` | Local display as temperature-control probe | `ZAZB`, `SLA`, `COLD`, `WARM`, `ZAZB_CENTRAL` |
| `413` | Scenario module control | modality, scenario address, levels, contact type, scenario, delay |
| `419` | Sound diffusion control | modality, addressing, area/audio point, follow-me, source, channel |

#### Object `191` - Local display as temperature control probe

The reusable probe exposes `ZAZB` zone, `SLA` slave number, `COLD` summer enable, `WARM` winter enable, and `ZAZB_CENTRAL` control-unit address. This is the configuration surface used when `FUN` selects the temperature-control role.

#### Object `413` - Scenario module control

The scenario role exposes modality, scenario-module address, installation/destination levels, contact type, scenario number and activation delay. The reusable scenario address spans the standard `A` / `PL` combinations represented by the catalogue; scenario number is `1..16` and contact type can be normally open or normally closed.

#### Object `419` - Sound diffusion control

The sound role exposes modality (including `VOL` / `ON_OFF`), addressing type, area, audio point, follow-me, source/sub-source, contact type and channel. These are reusable Object domains and should not be interpreted as proof that every field is visible in every product-programming screen.

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

Period product material describes an OLED local touch display used as a compact MyHOME interface. Its relevant systems include scenario control, sound diffusion and temperature regulation. The implementation database adds the exact conditional Object topology and the programming/configuration fields needed to represent those roles deterministically.

Depending on `FUN`, the Device participates in scenario, sound-diffusion or temperature-control behavior. Generic frame syntax remains canonical under Functional Protocol. This page records the Device-specific applicability and the conditional topology.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

The catalogue presents this Device as product-programmed over USB. Configuration tooling should preserve `FUN` as a topology selector: changing it can change which reusable Object model is applicable, not merely a value inside one unchanged Object.

## Source reconciliation

The `U1063B` Local Display documentation clarifies the conditional roles represented by `FUN`:

- `FUN=1` is the scenario-oriented display role;
- `FUN=2` is the sound-diffusion display/control role;
- `FUN=3` uses the Local Display with an external temperature probe;
- `FUN=4` associates the Local Display with a thermoregulation probe/zone role rather than merely duplicating `FUN=3`.

The same documentation describes a short display wake/active interval after user interaction, product programming through the documented local programming connection, and use with external probe reference `3457` in the applicable temperature role. It also supplies the external-probe and electrical/temperature data recorded above.

Because the publisher endpoint for `U1063B` still prevents repository archival in this environment, these meanings are recorded as document-derived findings pending byte-for-byte archival verification. The earlier open question about the distinction between `FUN=3` and `FUN=4` is therefore narrowed to verification/correlation with the catalogue topology rather than basic semantic naming.

## Evidence limits and open work

- Obtain sanitized fingerprints for at least one BTicino 4685 and one Legrand commercial variant.
- Archive the official `U1063B` revision when the publisher endpoint permits automated retrieval.
- Find direct official sheets for `573916`/`573917` and `067281`/`067282`.
- Establish vendor-facing names for `M=3..8` and verify the documented `FUN=3` / `FUN=4` distinction against an archived `U1063B` original and real hardware.
- Check whether firmware later than catalogue `1.3.7` changes role selection or slot anchoring.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
