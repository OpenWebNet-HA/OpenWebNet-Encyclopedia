# Flush-mounted radio receiver for batteryless control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0035` | Project identity |
| Technical description | Four-slot SCS radio receiver for batteryless flat controls | Catalogue + official documentation |
| Commercial identities | `HC/HS/HD4575SB`, `L/N/NT4575SB` | Catalogue |
| Catalogue item | `40` - “Flush mounted radio receiver for HA/HB4572SB” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `19` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `218` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Categories | Radio interface, Lighting control, Automation control, Scenario control | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - Axolute | `HC/HS/HD4575SB` | Established identity | canonical commercial record `40`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - Axolute | `L/N/NT4575SB` | Established identity | canonical commercial record `1841`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | Batteryless control/4575SB receiver configuration: printed pp. 138-141 / PDF pp. 140-143; technical characteristics printed p. 172 / PDF p. 174 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | 4575SB sound-mode configuration: printed pp. 66-67 / PDF pp. 66-67 and 82; radio-interface technical data printed p. 99 / PDF p. 99 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `27 Vdc` | Publisher automation documentation |
| Mounting | 2 wiring-device modules | Publisher automation documentation |
| Radio frequency | `868 MHz` | `mh_diff-sonore2008.pdf` |
| Published current draw | `33 mA` for the documented `L/N/NT4575SB` variant | `mh_diff-sonore2008.pdf` |
| Radio role | receiver for the batteryless flat-control family | Publisher automation documentation |

Where package variants are not covered by the same electrical table, current/range figures remain explicitly source-revision and variant scoped.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `40` | Canonical catalogue |
| Technical item description | Flush mounted radio receiver for HA/HB4572SB | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `19` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `218` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `218` | `1` | `400` Light control | Fixed/designated metadata | `1011` | `400` | `608` |
| `218` | `1` | `401` Automation control | Candidate alternative | `1019` | `401` | `610` |
| `218` | `1` | `403` Scenario module control | Candidate alternative | `1015` | `403` | `609` |
| `218` | `2` | `400` Light control | Fixed/designated metadata | `1012` | `400` | `608` |
| `218` | `2` | `403` Scenario module control | Candidate alternative | `1016` | `403` | `609` |
| `218` | `3` | `400` Light control | Fixed/designated metadata | `1013` | `400` | `608` |
| `218` | `3` | `401` Automation control | Candidate alternative | `1020` | `401` | `610` |
| `218` | `3` | `403` Scenario module control | Candidate alternative | `1017` | `403` | `609` |
| `218` | `4` | `400` Light control | Fixed/designated metadata | `1014` | `400` | `608` |
| `218` | `4` | `403` Scenario module control | Candidate alternative | `1018` | `403` | `609` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

Object `400` Light control is fixed on slots `1`, `2`, `3` and `4`. Object `403` Scenario module control is a non-fixed candidate on all four slots. Object `401` Automation control is a non-fixed candidate on slots `1` and `3`. Shared Virgin Object families `500` / `501` / `502` cover the corresponding Light, Automation and Scenario control Objects.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `218` | `1` | `1` | Virtual Configuration |
| `218` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `218` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `218` | `A` | `0..9` | `0` | A; Environment |
| `218` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `218` | `M1` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M1; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `218` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `218` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M2; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `218` | `SPE` | `0..1`; `6` | `0` | SPE; Special function command control (0,1,6) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL1` | `0..9` | output 1 light-point configurator |
| `M1` | `0..8` / `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` | channel 1 operating mode |
| `PL2` | `0..9` | output 2 light-point configurator |
| `M2` | `0..8` / `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` | channel 2 operating mode |
| `SPE` | `0` / `1` / `6` | special-function selector |


`M1` / `M2` select the command behavior for the two control positions; `SPE` is the special-function selector. Slot/Object conditions further constrain which reusable control Object is active.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON`/`OFF` and dimming; `4` = Toggle `ON`/`OFF`; `5` = `ON`/`OFF`; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Light point of reference actuator; 0=no referent address |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0=no referent address |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129-134` |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129-134` |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129-134` |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129-132` |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `401` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `12` = Bistable control; `13` = Monostable control; `14` = Blades control and bistable | `12` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `403` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number | `0` | Destination level |
| `SCE_BUTT_1` | `1..16` | `1` | Upper button scenario |
| `SCE_BUTT_2` | `1..16` | `2` | Lower button scenario |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `43` = 43 s; `44` = 44 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `36` = 36 s; `37` = 37 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `69` = 9 min; `70` = 10 min | `0` | Activation delay for lower button |


### Product interpretation and source differences

**Object `400` - Light control - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

**Object `403` - Scenario module control - product interpretation.**

**Firmware relationship.** The catalogue relation restricts `INST_LEV` to encoded value `8` (catalogue label `Level 4 #8`).

**Object `401` - Automation control - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `218` | `1` | `400` | `4145` | No textual predicate stored | None |
| `218` | `1` | `401` | `4305` | `M1=SU_GIU;SPE<>6` | None |
| `218` | `1` | `401` | `4313` | `M1=SU_GIU_M;SPE<>6` | None |
| `218` | `1` | `403` | `4857` | `SPE=6` | None |
| `218` | `2` | `400` | `4145` | No textual predicate stored | None |
| `218` | `2` | `403` | `4899` | `SPE=7` | None |
| `218` | `3` | `400` | `4145` | No textual predicate stored | None |
| `218` | `3` | `401` | `4416` | `M2=SU_GIU;SPE<>6` | None |
| `218` | `3` | `401` | `4422` | `M2=SU_GIU_M;SPE<>6` | None |
| `218` | `3` | `403` | `4874` | `SPE=8` | None |
| `218` | `4` | `400` | `4145` | No textual predicate stored | None |
| `218` | `4` | `403` | `4877` | `SPE=9` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `218` | `403` | `1109` | `INST_LEV` | `8` = Local bus 8 | `16` | Installation level; reusable default `16` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 19` and the 4575SB receiver family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assuming wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate four fixed Light-control positions and resolve optional Automation/Scenario candidates | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured addresses for the active slot roles | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL1`, `M1`, `PL2`, `M2`, `SPE` and the Scenario installation-level restriction | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on Object and mode, the receiver can expose lighting, automation and scenario-control functions from paired batteryless radio controls.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Preserve slot-by-slot Object selection and the complete `M` / `SPE` mode set. Do not model the receiver as a single generic pushbutton or as four unconditional Light controls.

## Source reconciliation

Publisher documentation establishes the 4575SB batteryless-radio receiver family and SCS BUS role. The canonical database explains its richer software topology: four fixed Light-control slot positions with optional Automation and Scenario Objects, plus the firmware-level `PL` / `M` / `SPE` configuration.

## Evidence limits and open work

- Add sanitized pairing and button-action captures for representative 4572SB controls.
- Corroborate optional Automation/Scenario Object resolution by `DIMENSION 30` on hardware.
- Document the Installation level filter for Scenario module control in human-readable form.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
