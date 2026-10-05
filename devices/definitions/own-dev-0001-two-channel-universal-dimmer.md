# Two-channel universal dimmer

## Summary

The F418U2 is a DIN-mounted, two-channel SCS dimmer for dimmable LED, compact fluorescent and other documented lamp types. Its channels can operate separately or in parallel for a larger load, and local pushbuttons provide direct control.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0001` | Project identity |
| Technical description | Two-channel universal dimmer, 4 DIN modules | Catalogue + vendor documentation |
| Commercial identities | BTicino `F418U2`; Legrand `0 036 51` / catalogue `003651` | Catalogue + vendor documentation |
| Catalogue item | `2065` - “2x1,6A universal dimmer, 4DIN” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `77` | Implementation evidence |
| Catalogue brand / line | `BRAND = 5`; `LINE = 0` | Implementation evidence |
| Firmware definition | `1.0.5` (`EN_FIRMWARE 590`) | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Actuator, Lighting, Dimmer | Derived from capability model |

## Commercial identities

| Brand / range | SKU / reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F418U2` | Established commercial identity | Catalogue + vendor technical sheet |
| Legrand | `0 036 51` / `003651` | Equivalent commercial reference | Same vendor technical sheet + same catalogue item |

No preference between these references is implied by the Device ID.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F418U2` | `8005543534991` | [Archived original](https://archive.openwebnet-ha.org/sha256/97/8f/978fcfe56ced3126d6658112df49a6f63b77e6fa1cc205f2aaba7c94bfb2566b.pdf), `F418U2-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ01019_a_EN` - Universal dimmer 2x300W | Technical sheet | 20/09/2018 | Whole Device-specific document, PDF pp. 1-4; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/2d/b6/2db6bcdc199da839de2bff76bbcd7ef21afac85c8818dbd563c4dc226f66e58e.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ01019_a_EN.pdf) |
| `LE07383AB` | Instruction sheet | Printed `LE07383AB-01PC-17W18` | Whole Device-specific document, PDF pp. 1-2; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/3e/ee/3eeee15691e13bddc91c9980b95553414b0418488086893f99ca2fddca509aaf.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE07383AB.pdf) |
| `LE07383AC` | Instruction sheet | Printed revision AC; `21W40` imprint | Whole Device-specific document, PDF pp. 1-2; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/2c/e6/2ce6014a32c3752547d670f35bdbfdeac8c38fc56b0fd40798c33b207132134c.pdf) | [Official source](https://dar.bticino.com/asset/Documents/LE07383AC.pdf) |
| `LE07383AD` | Instruction sheet | 07/23 | Whole Device-specific document, PDF pp. 1-2; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/4d/2f4daed6f567b8fcc3250113603a57168b949f441eb121e7851b6f23625dfdbe.pdf) | [Official source](https://dar.bticino.com/asset/Documents/LE07383AD.pdf) |
| `ST-00001620-EN` | Technical sheet | 19/07/2023 | Whole Device-specific document, PDF pp. 1-4; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/10/7a/107a108bd89755bf0f2e93b861c8458d77f3fa994555126fc3f22c0f3979a004.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001620-EN.pdf) |
| `GUI-MHOME` | MyHOME installation guide | Publisher listing; see original imprint | Listing alias only; mapping of `GUI-MHOME` to the retained technical-guide binary is not established | - | [BTicino product page](https://www.bticino.com/products/bt-f418u2) |
| `F418U2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `F418U2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/97/8f/978fcfe56ced3126d6658112df49a6f63b77e6fa1cc205f2aaba7c94bfb2566b.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F418U2) |
| `MyHOME-Technical-Guide.pdf` | Multi-product MyHOME technical guide | Retained publisher guide; retrieved binary reused | F418U2: printed/PDF pp. 46, 56, 100. General role, wiring example and `230 Vac` catalogue matrix inspected; unrelated products not reviewed. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher source](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |

See the [Device Source Index](../../sources/devices/index.md) for archival status and provenance.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Width | 4 DIN modules | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| SCS supply | `18..27 Vdc` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| SCS absorption | max. `18 mA` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Mains supply | `110..127 Vac` or `220..240 Vac`, `50..60 Hz` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Device consumption | max. `5 W` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Operating temperature | `0..40 °C` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Channels | 2, with parallel operation supported by the product documentation | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Incandescent/halogen at `220..240 V`, separate channels | `2 × 300 W` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Incandescent/halogen at `220..240 V`, parallel channels | `600 W` | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Load families | dimmable LED, dimmable CFL, halogen, electronic transformers | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Local operation | local channel pushbuttons | `MQ01019_a_EN`, printed/PDF p. 1; 2018 scope |
| Later operating temperature | `5..40 °C` | `LE07383AD`, July 2023, PDF p. 2; earlier `MQ01019_a_EN` gives `0..40 °C` |
| Later load-table entries at `240 Vac` | `150 W` / `150 VA` | `LE07383AD`, PDF p. 2; keep the printed load-column context separate from the older per-channel ratings |
| Later load-table entries at `110 Vac` | `75 W` / `75 VA` | `LE07383AD`, PDF p. 2; not a timeless replacement for the 2018 matrix |
| Fuse | `T3.15H 250 V` time-lag fuse | `LE07383AD`, PDF p. 1 |
| Installation placement | No adjacent dimmers; no installation adjacent to a power supply | `LE07383AD`, PDF p. 2 |
| Load combination | Mixed loads prohibited | `LE07383AD`, PDF p. 2 |

| Property | Value | Evidence |
| --- | --- | --- |
| Incandescent/halogen at `110..127 V` | `2 × 150 W` separate; `300 W` parallel | `MQ01019_a_EN`, p. 1 |
| Dimmable LED/CFL and documented transformer loads at `220..240 V` | `2 × 300 VA` separate; `600 VA` parallel | `MQ01019_a_EN`, p. 1 |
| Same VA load classes at `110..127 V` | `2 × 150 VA` separate; `300 VA` parallel | `MQ01019_a_EN`, p. 1 |
| LED/CFL explanatory approximation | `300 VA` corresponds to about `200 W` for the most common lamps, according to this source | `MQ01019_a_EN`, p. 1; not a universal VA/W conversion |
| 2023 technical-sheet temperature and ratings | `0..40 °C`; `2 × 300 W / VA` high-voltage separate channels, `600 W / VA` parallel | `ST-00001620-EN`, pp. 1, 4 |
| Production-batch light-level change | From `23W16`, revised relationship between nominal level and brightness | `LE07383AD`, p. 2; product documentation, not a new observation |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2065` | Canonical catalogue |
| Item model / `modobj` | `77` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation (`id_system = 1`) | Canonical catalogue / retained definition |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `77` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These are software applicability associations, not an inventory of physical ports or proof of every functional service.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `590` | `1` | `0` | `5` | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

### Parameter and package associations

No firmware parameter-file associations are stored for this item in the canonical snapshot.

No `AS_FW_PACKAGE` association is stored for these firmware definitions. This is a catalogue coverage statement, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `590` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `2592` | `8` | `1210` |
| `590` | `1` | `136` Double Dimmer actuator | Candidate alternative | `2591` | `631` | `1209` |
| `590` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `2593` | `8` | `1210` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `590` | `528` Dimmer actuator virgin | `1`, `2` | `8`, `136` | `532` | `55` |

The installed Module/Object projection is obtained through [`DIMENSION 30`](../../diagnostics/dim30-modules.md). The generic `SLOT`, `KEYO`, and `STATE` frame semantics remain canonical there.

## Configuration modes

| Firmware | Mode | Catalogue mode | Applicability |
| --- | --- | --- | --- |
| `590` | Physical configuration | `0` | Canonical catalogue association; not proof of installed state |
| `590` | Virtual Configuration | `1` | Canonical catalogue association; not proof of installed state |
| `590` | Advanced Configuration | `2` | Canonical catalogue association; not proof of installed state |

Product physical and software setup are distinct from the catalogue mode labels. A declared mode does not prove every reusable Object or programming operation is available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `590` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `590` | `A` | `0..9` | `0` | Area |
| `590` | `PL1` | `0..9` | `0` | Lighting point for channel 1 |
| `590` | `PL2` | `0..9` | `0` | Lighting point for channel 2 |
| `590` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | Modality |
| `590` | `G` | `0..9` | `0` | Group |
| `590` | `TY` | `0..3` | `0` | Load type |
| `590` | `MIN1` | `0..9` | `0` | Minimum level for channel 1 |
| `590` | `MIN2` | `0..9` | `0` | Minimum level for channel 2 |

### Published and reconciled details

These are the complete firmware-scoped configuration fields stored for firmware `590`, excluding only database bookkeeping columns.

| Field | Catalogue domain | Product-document interpretation | Evidence |
| --- | --- | --- | --- |
| `AID` | Device ID field | not a physical configurator | Implementation evidence |
| `A` | `0..9` | physical `A=1..9`; virtual room `0..10` | Catalogue + vendor PDF |
| `PL1` | `0..9` | physical `PL1=1..9`; virtual `0..15` | Catalogue + vendor PDF |
| `PL2` | `0..9` | physical `PL2=0..9`; virtual `0..15` | Catalogue + vendor PDF |
| `M` | `0,1,2,3,4,11=SLA,15=PUL` | Master, delayed `OFF` modes, Slave, Master `PUL` | Catalogue + vendor PDF |
| `G` | `0..9` | physical `0..9`; virtual group `0..255` | Catalogue + vendor PDF |
| `TY` | `0..3` | per-channel leading/trailing-edge load selection | Catalogue + vendor PDF |
| `MIN1` | `0..9` | channel 1 minimum level selector | Catalogue + vendor PDF |
| `MIN2` | `0..9` | channel 2 minimum level selector | Catalogue + vendor PDF |

The catalogue includes `0` in the stored physical ranges for `A` and `PL1`, while the 2018 technical sheet prints `A=1..9` and `PL1=1..9`. Preserve this as a source-level difference rather than silently reconciling the domains.

### Physical mode `M`

| Stored value | Vendor label / effect | Evidence |
| ---: | --- | --- |
| `0` | Master | Catalogue + vendor PDF |
| `1` | Master: corresponding Slave switch-off delayed by 1 minute | Vendor PDF |
| `2` | Master: corresponding Slave switch-off delayed by 2 minutes | Vendor PDF |
| `3` | Master: corresponding Slave switch-off delayed by 3 minutes | Vendor PDF |
| `4` | Master: corresponding Slave switch-off delayed by 4 minutes | Vendor PDF |
| `11` / `SLA` | Slave | Catalogue + vendor PDF |
| `15` / `PUL` | Master `PUL` | Catalogue + vendor PDF |

The 2018 sheet specifies software `Delay OFF = 0..255 seconds`, versus physical `M=1..4` presets in minutes. On OFF, the Master switches off immediately and its corresponding Slave remains on for the configured delay; the note allows point-to-point or group control. Group addressing is not configurable in Slave mode.

### Physical load selector `TY`

| `TY` | Channel 1 | Channel 2 | Evidence |
| ---: | --- | --- | --- |
| `0` | leading edge | leading edge | Vendor PDF |
| `1` | trailing edge | trailing edge | Vendor PDF |
| `2` | leading edge | trailing edge | Vendor PDF |
| `3` | trailing edge | leading edge | Vendor PDF |

### Physical minimum-level selectors

| Selector value | Minimum level | Evidence |
| ---: | ---: | --- |
| `0` | default, 10% in the 2018 sheet | Vendor PDF |
| `1` | 1% | Vendor PDF |
| `2` | 5% | Vendor PDF |
| `3` | 10% | Vendor PDF |
| `4` | 15% | Vendor PDF |
| `5` | 20% | Vendor PDF |
| `6` | 25% | Vendor PDF |
| `7` | 30% | Vendor PDF |
| `8` | 35% | Vendor PDF |
| `9` | 40% | Vendor PDF |

The 2018 sheet requires `MIN2=0` when `PL2=0` or `PL2=PL1`. Channel 2 load type is separately selectable only outside parallel mode. Its `TY=2/3` note says “parallel mode” but prints `PL2≠PL1`, conflicting with the equal-address parallel diagram; that condition is unresolved and must not become an implementation rule.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

### Object `136` - Double Dimmer actuator

Catalogue Object key `631` maps to external Object `136`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

### Applicability interpretation

Objects `8` and `136` have identical reusable field surfaces in this snapshot. `TYPE_LOAD` includes technologies beyond the F418U2 product sheets; membership in that enum does not establish support on this dimmer.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `590` | `1` | `8` | `4149` | No textual predicate stored | `3` |
| `590` | `1` | `136` | `4960` | `PL1=PL2` | `550` |
| `590` | `2` | `8` | `4149` | No textual predicate stored | `3` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `590` | `8` | `2214` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `590` | `8` | `2215` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `590` | `8` | `2216` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `590` | `8` | `2217` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `590` | `8` | `2218` | `MIN_LEVEL` | `1..100` (entire reusable range retained) | `1` | Minimum level |
| `590` | `8` | `2219` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `590` | `8` | `2220` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of load |
| `590` | `136` | `2205` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `590` | `136` | `2206` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `590` | `136` | `2207` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `590` | `136` | `2208` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `590` | `136` | `2209` | `MIN_LEVEL` | `1..100` (entire reusable range retained) | `1` | Minimum level |
| `590` | `136` | `2210` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of load |
| `590` | `136` | `2211` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `3` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `3` |
| `3` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `3` |
| `3` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `3` |
| `550` | `M1=0` | `M` = `0` | `550` |
| `550` | `M1=1` | `M` = `1`; `T_TIME ` = `1` | `550` |
| `550` | `M1=2` | `M` = `1`; `T_TIME ` = `2` | `550` |
| `550` | `M1=3` | `M` = `1`; `T_TIME ` = `3` | `550` |
| `550` | `M1=4` | `M` = `1`; `T_TIME ` = `4` | `550` |
| `550` | `M1=5` | `M` = `1`; `T_TIME ` = `5` | `550` |
| `550` | `M1=6` | `M` = `1`; `T_TIME ` = `6` | `550` |
| `550` | `M1=7` | `M` = `1`; `T_TIME ` = `7` | `550` |
| `550` | `M1=8` | `M` = `1`; `T_TIME ` = `8` | `550` |
| `550` | `M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` |
| `550` | `M1=O/I` | `M` = `9` | `550` |
| `550` | `M1=OFF` | `M` = `10` | `550` |
| `550` | `M1=ON` | `M` = `11` | `550` |
| `550` | `M1=PUL` | `M` = `15` | `550` |
| `550` | `M1=SU_GIU` | `M` = `12` | `550` |
| `550` | `M1=SU_GIU_M` | `M` = `13` | `550` |
| `550` | `A1=1` | `A` = `1` | `550` |
| `550` | `A1=2` | `A` = `2` | `550` |
| `550` | `A1=3` | `A` = `3` | `550` |
| `550` | `A1=4` | `A` = `4` | `550` |
| `550` | `A1=5` | `A` = `5` | `550` |
| `550` | `A1=6` | `A` = `6` | `550` |
| `550` | `A1=7` | `A` = `7` | `550` |
| `550` | `A1=8` | `A` = `8` | `550` |
| `550` | `A1=9` | `A` = `9` | `550` |
| `550` | `PL1=1` | `PL` = `1` | `550` |
| `550` | `PL1=1; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `550` → `1` |
| `550` | `PL1=1; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `550` → `1` |
| `550` | `PL1=2` | `PL` = `2` | `550` |
| `550` | `PL1=2; M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `550` → `2` |
| `550` | `PL1=2; M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `550` → `2` |
| `550` | `PL1=2; M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `550` → `2` |
| `550` | `PL1=2; M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `550` → `2` |
| `550` | `PL1=2; M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `550` → `2` |
| `550` | `PL1=2; M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `550` → `2` |
| `550` | `PL1=2; M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `550` → `2` |
| `550` | `PL1=2; M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `550` → `2` |
| `550` | `PL1=2; M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `550` → `2` |
| `550` | `PL1=2; M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `550` → `2` |
| `550` | `PL1=3` | `PL` = `3` | `550` |
| `550` | `PL1=3; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `550` → `3` |
| `550` | `PL1=3; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `550` → `3` |
| `550` | `PL1=4` | `PL` = `4` | `550` |
| `550` | `PL1=4; M1=0` | `M` = `0` | `550` → `4` |
| `550` | `PL1=4; M1=1` | `M` = `1`; `T_TIME ` = `1` | `550` → `4` |
| `550` | `PL1=4; M1=2` | `M` = `1`; `T_TIME ` = `2` | `550` → `4` |
| `550` | `PL1=4; M1=3` | `M` = `1`; `T_TIME ` = `3` | `550` → `4` |
| `550` | `PL1=4; M1=4` | `M` = `1`; `T_TIME ` = `4` | `550` → `4` |
| `550` | `PL1=4; M1=5` | `M` = `1`; `T_TIME ` = `5` | `550` → `4` |
| `550` | `PL1=4; M1=6` | `M` = `1`; `T_TIME ` = `6` | `550` → `4` |
| `550` | `PL1=4; M1=7` | `M` = `1`; `T_TIME ` = `7` | `550` → `4` |
| `550` | `PL1=4; M1=8` | `M` = `1`; `T_TIME ` = `8` | `550` → `4` |
| `550` | `PL1=4; M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` → `4` |
| `550` | `PL1=4; M1=O/I` | `M` = `9` | `550` → `4` |
| `550` | `PL1=4; M1=OFF` | `M` = `10` | `550` → `4` |
| `550` | `PL1=4; M1=ON` | `M` = `11` | `550` → `4` |
| `550` | `PL1=4; M1=PUL` | `M` = `15` | `550` → `4` |
| `550` | `PL1=4; M1=SU_GIU` | `M` = `12` | `550` → `4` |
| `550` | `PL1=4; M1=SU_GIU_M` | `M` = `13` | `550` → `4` |
| `550` | `PL1=4; M2=0` | `M` = `0` | `550` → `4` |
| `550` | `PL1=4; M2=1` | `M` = `1`; `T_TIME ` = `1` | `550` → `4` |
| `550` | `PL1=4; M2=2` | `M` = `1`; `T_TIME ` = `2` | `550` → `4` |
| `550` | `PL1=4; M2=3` | `M` = `1`; `T_TIME ` = `3` | `550` → `4` |
| `550` | `PL1=4; M2=4` | `M` = `1`; `T_TIME ` = `4` | `550` → `4` |
| `550` | `PL1=4; M2=5` | `M` = `1`; `T_TIME ` = `5` | `550` → `4` |
| `550` | `PL1=4; M2=6` | `M` = `1`; `T_TIME ` = `6` | `550` → `4` |
| `550` | `PL1=4; M2=7` | `M` = `1`; `T_TIME ` = `7` | `550` → `4` |
| `550` | `PL1=4; M2=8` | `M` = `1`; `T_TIME ` = `8` | `550` → `4` |
| `550` | `PL1=4; M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` → `4` |
| `550` | `PL1=4; M2=O/I` | `M` = `9` | `550` → `4` |
| `550` | `PL1=4; M2=OFF` | `M` = `10` | `550` → `4` |
| `550` | `PL1=4; M2=ON` | `M` = `11` | `550` → `4` |
| `550` | `PL1=4; M2=PUL` | `M` = `15` | `550` → `4` |
| `550` | `PL1=4; M2=SU_GIU` | `M` = `12` | `550` → `4` |
| `550` | `PL1=4; M2=SU_GIU_M` | `M` = `13` | `550` → `4` |
| `550` | `PL1=5` | `PL` = `5` | `550` |
| `550` | `PL1=5; M1=0` | `M` = `0` | `550` → `5` |
| `550` | `PL1=5; M1=O/I` | `M` = `9` | `550` → `5` |
| `550` | `PL1=5; M1=OFF` | `M` = `10` | `550` → `5` |
| `550` | `PL1=5; M1=ON` | `M` = `11` | `550` → `5` |
| `550` | `PL1=5; M1=PUL` | `M` = `15` | `550` → `5` |
| `550` | `PL1=5; M1=SU_GIU` | `M` = `12` | `550` → `5` |
| `550` | `PL1=5; M1=SU_GIU_M` | `M` = `13` | `550` → `5` |
| `550` | `PL1=5; M2=0` | `M` = `0` | `550` → `5` |
| `550` | `PL1=5; M2=O/I` | `M` = `9` | `550` → `5` |
| `550` | `PL1=5; M2=OFF` | `M` = `10` | `550` → `5` |
| `550` | `PL1=5; M2=ON` | `M` = `11` | `550` → `5` |
| `550` | `PL1=5; M2=PUL` | `M` = `15` | `550` → `5` |
| `550` | `PL1=5; M2=SU_GIU` | `M` = `12` | `550` → `5` |
| `550` | `PL1=5; M2=SU_GIU_M` | `M` = `13` | `550` → `5` |
| `550` | `PL1=5; PL1=0` | `OUT_AUX_CHANNEL` = `0` | `550` → `5` |
| `550` | `PL1=5; PL1=1` | `OUT_AUX_CHANNEL` = `1` | `550` → `5` |
| `550` | `PL1=5; PL1=2` | `OUT_AUX_CHANNEL` = `2` | `550` → `5` |
| `550` | `PL1=5; PL1=3` | `OUT_AUX_CHANNEL` = `3` | `550` → `5` |
| `550` | `PL1=5; PL1=4` | `OUT_AUX_CHANNEL` = `4` | `550` → `5` |
| `550` | `PL1=5; PL1=5` | `OUT_AUX_CHANNEL` = `5` | `550` → `5` |
| `550` | `PL1=5; PL1=6` | `OUT_AUX_CHANNEL` = `6` | `550` → `5` |
| `550` | `PL1=5; PL1=7` | `OUT_AUX_CHANNEL` = `7` | `550` → `5` |
| `550` | `PL1=5; PL1=8` | `OUT_AUX_CHANNEL` = `8` | `550` → `5` |
| `550` | `PL1=5; PL1=9` | `OUT_AUX_CHANNEL` = `9` | `550` → `5` |
| `550` | `PL1=5; PL2=0` | `OUT_AUX_CHANNEL` = `0` | `550` → `5` |
| `550` | `PL1=5; PL2=1` | `OUT_AUX_CHANNEL` = `1` | `550` → `5` |
| `550` | `PL1=5; PL2=2` | `OUT_AUX_CHANNEL` = `2` | `550` → `5` |
| `550` | `PL1=5; PL2=3` | `OUT_AUX_CHANNEL` = `3` | `550` → `5` |
| `550` | `PL1=5; PL2=4` | `OUT_AUX_CHANNEL` = `4` | `550` → `5` |
| `550` | `PL1=5; PL2=5` | `OUT_AUX_CHANNEL` = `5` | `550` → `5` |
| `550` | `PL1=5; PL2=6` | `OUT_AUX_CHANNEL` = `6` | `550` → `5` |
| `550` | `PL1=5; PL2=7` | `OUT_AUX_CHANNEL` = `7` | `550` → `5` |
| `550` | `PL1=5; PL2=8` | `OUT_AUX_CHANNEL` = `8` | `550` → `5` |
| `550` | `PL1=5; PL2=9` | `OUT_AUX_CHANNEL` = `9` | `550` → `5` |
| `550` | `PL1=6` | `PL` = `6` | `550` |
| `550` | `PL1=6; M=3` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=4` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=5` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=6; M=6` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=7` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=6; M=8` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; S=0` | `PIR` = `0` | `550` → `6` |
| `550` | `PL1=6; S=1` | `PIR` = `1` | `550` → `6` |
| `550` | `PL1=6; S=2` | `PIR` = `2` | `550` → `6` |
| `550` | `PL1=6; S=3` | `PIR` = `3` | `550` → `6` |
| `550` | `PL1=6; T=0` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=1` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `30` | `550` → `6` |
| `550` | `PL1=6; T=2` | `HOURS` = `0`; `MINUTES` = `1`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=3` | `HOURS` = `0`; `MINUTES` = `2`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=4` | `HOURS` = `0`; `MINUTES` = `5`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=5` | `HOURS` = `0`; `MINUTES` = `10`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=6` | `HOURS` = `0`; `MINUTES` = `15`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=7` | `HOURS` = `0`; `MINUTES` = `20`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=8` | `HOURS` = `0`; `MINUTES` = `30`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=9` | `HOURS` = `0`; `MINUTES` = `40`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; M=0` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1` | `550` → `6` |
| `550` | `PL1=6; M=1` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=7` | `PL` = `7` | `550` |
| `550` | `PL1=7` | Referenced conversion rule absent from source | `550` → `7` |
| `550` | `PL1=8` | `PL` = `8` | `550` |
| `550` | `PL1=8` | Referenced conversion rule absent from source | `550` → `8` |
| `550` | `PL1=9` | `PL` = `9` | `550` |
| `550` | `PL1=9; M=0` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `550` → `9` |
| `550` | `PL1=9; M=1` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `550` → `9` |
| `550` | `PL1=9; M=2` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `25` | `550` → `9` |
| `550` | `PL1=9; M=3` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `550` → `9` |
| `550` | `PL1=9; M=PUL` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `20` | `550` → `9` |
| `550` | `PL1=9; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `550` → `9` |
| `550` | `M2=0` | `M` = `0` | `550` |
| `550` | `M2=1` | `M` = `1`; `T_TIME ` = `1` | `550` |
| `550` | `M2=2` | `M` = `1`; `T_TIME ` = `2` | `550` |
| `550` | `M2=3` | `M` = `1`; `T_TIME ` = `3` | `550` |
| `550` | `M2=4` | `M` = `1`; `T_TIME ` = `4` | `550` |
| `550` | `M2=5` | `M` = `1`; `T_TIME ` = `5` | `550` |
| `550` | `M2=6` | `M` = `1`; `T_TIME ` = `6` | `550` |
| `550` | `M2=7` | `M` = `1`; `T_TIME ` = `7` | `550` |
| `550` | `M2=8` | `M` = `1`; `T_TIME ` = `8` | `550` |
| `550` | `M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` |
| `550` | `M2=O/I` | `M` = `9` | `550` |
| `550` | `M2=OFF` | `M` = `10` | `550` |
| `550` | `M2=ON` | `M` = `11` | `550` |
| `550` | `M2=PUL` | `M` = `15` | `550` |
| `550` | `M2=SU_GIU` | `M` = `12` | `550` |
| `550` | `M2=SU_GIU_M` | `M` = `13` | `550` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

The Device-specific knowledge above projects through the general diagnostic model:

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model `77`, brand `5`, line `0`; obtain installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | obtain installed firmware version | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | obtain hardware version when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | obtain microcontroller version when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 13` | obtain physical Device ID | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate the two installed Modules and active Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain configured Module addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | obtain configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

The table documents applicability and Device-specific expectations. Frame grammar and generic field semantics belong to the linked reference pages.
## Functional applicability

F418U2 is a `WHO 1` Lighting dimmer. General commands, addressing, and dimension grammar are documented under [Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

First-hand evidence already adds several Device-specific observations:

- `DIMENSION 1` and functional `DIMENSION 4` are distinct state surfaces on the tested F418U2 even when they report the same `LEVEL100`;
- at `LEVEL100 = 130`, observed trailing values differed between those two dimensions;
- through MH202, explicit reads of both dimensions were observed;
- through F454, an `OFF`-state `DIMENSION 1` request was observed to return a `DIMENSION 4` frame;
- through an MH200 running firmware 2.1.0, the preserved public trace shows working `DIMENSION 1` reads/writes while explicit `DIMENSION 4` requests received no response in the captured windows.

These observations corroborate runtime behavior but do not change the canonical generic frame definitions. See [`WHO 1` Dimensions](../../functional/who-1-lighting/dimensions.md) and the [Open Questions](../../reverse-engineering/open-questions.md).

## Programming

F418U2 programming should use the canonical [Programming](../../programming/) workflow. The Device-specific data required by a validator is captured above:

- two-slot firmware topology;
- allowed Object alternatives;
- physical configuration fields and domains;
- reusable Object parameter domains;
- product-document constraints on channel configuration, loads, and minimum levels.

Generic `DIMENSION` write syntax and validation sequencing belong in [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation

Known F418U2 product documentation and runtime research have been reconciled as follows:

- the local channel pushbuttons are Device controls, not additional OpenWebNet Modules; their status/fault indication belongs to the product-level behavior of the two dimmer channels;
- vendor documentation distinguishes normal status from load/fault and configuration indications on the front LEDs and documents a Device-level two-channel setup path in the MyHOME Server tooling;
- group configuration is not a legal physical interpretation of Slave operation, and the second channel inherits product constraints from the selected channel/load arrangement rather than being an unconstrained duplicate;
- later instruction material warns against mixing incompatible load technologies and keeps minimum-level/load-type behavior revision-scoped;
- the runtime `DIMENSION 4` evidence remains Device-specific and unresolved in four places: the exact `ON/OFFspeed` encoding, whether the observed F454 positive write failure is systematic, whether MH200 non-response is gateway/firmware-wide or interaction-specific, and whether the reported F414/MH200 timeout followed by `NACK` can be reproduced from a preserved raw exchange.

The five exact-product PDFs are retained separately. `LE07383AB` (`17W18`) and `LE07383AC` (`21W40`) print `200..240 Vac` / `110..127 Vac` load-table rows with `1..300 W/VA` / `1..150 W/VA`; their wiring pictures supply the channel context. The 2018 technical sheet instead uses `220..240 Vac`. These source intervals are not silently made identical.

`ST-00001620-EN` is dated 19 July 2023 and still states `0..40 °C` and the `300`-per-channel / `600`-parallel matrix. The July 2023 `LE07383AD` prints `5..40 °C` and `150 W/VA` at `240 Vac`, `75 W/VA` at `110 Vac`. The AD table does not establish that these entries mean “per channel”; the earlier page wording was too strong. The simultaneous 2023 disagreement remains unresolved, so no single replacement load rating or production-batch hardware explanation is inferred. Its explicit `23W16` light-level change is a separate documented fact.

The already retained MyHOME technical guide corroborates the product role and a `230 Vac` catalogue matrix. It does not resolve the AD load conflict or prove that the product-listing alias `GUI-MHOME` names this exact binary. Unrelated guide products are outside this review scope.

The `TY` note and catalogue-versus-physical address-domain differences remain explicit. Runtime claims above remain scoped to the preserved gateway paths, rather than inferred from these product revisions.

## Evidence limits and open work

- Establish the exact `GUI-MHOME` listing-to-binary relationship; the separately retained technical guide is reviewed only at its F418U2 locations.
- Add a sanitized fingerprint capture from a known physical F418U2 so installed identity, firmware, hardware, Module/Object state, addresses, and configuration can be tied to one evidence record.
- Resolve the source-level `A` / `PL1` physical-domain difference between catalogue data and the 2018 technical sheet.
- Preserve production-batch-specific behavior from later instruction sheets as revision-scoped product evidence rather than generalizing it backwards.
- Resolve the contemporaneous 2023 rating/temperature conflict and the contradictory `TY=2/3` condition without guessing hardware applicability. The stored firmware filters are fully recorded; their physical reachability remains unobserved.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Physical Devices](../../device-model/physical-devices.md#f418u2)
- [Firmware](../../device-model/firmware.md)
- [Virgin Objects](../../device-model/virgin-objects.md#dimmer-actuator-virgin)
- [`WHO 1` Dimensions](../../functional/who-1-lighting/dimensions.md)

- `F418U2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F418U2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/97/8f/978fcfe56ced3126d6658112df49a6f63b77e6fa1cc205f2aaba7c94bfb2566b.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F418U2); SHA-256 `978fcfe56ced3126d6658112df49a6f63b77e6fa1cc205f2aaba7c94bfb2566b`.

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0001-0010-2026-10-05.md#own-dev-0001)
