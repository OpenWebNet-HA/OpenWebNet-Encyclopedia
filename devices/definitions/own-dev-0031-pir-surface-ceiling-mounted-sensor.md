# PIR surface ceiling-mounted sensor

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0031` | Project identity |
| Technical description | Ceiling-mounted PIR / daylight sensor with stand-alone and scenario-oriented roles | Catalogue + official documentation |
| Commercial identities | `BMSE1001`, `048833` | Catalogue |
| Catalogue item | `33` - “PIR surface ceiling mounted sensor” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `18` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `130` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Sensor, Presence, Daylight, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino | `BMSE1001` | Established identity | canonical commercial record `33`; Commercial identity of this Technical Device | Canonical catalogue |
| Legrand | `048833` | Established identity | canonical commercial record `1556`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `fiche technique 048833` | Technical sheet | `LG00295-a-FR` | printed pp. 464-467 / PDF pp. 1-4 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/96/b2/96b2d164e69405d1c7f3a1b52e3eea061ad02c1fee528c16f35971255406232f.pdf) | [Publisher PDF](https://assets.legrand.com/general/legrand-fr/pfat/gm/fiche%20technique%20048833.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Sensor technology | passive infrared (PIR) with ambient-light information for lighting control | `fiche technique 048833` |
| Mounting | surface ceiling mounted | `fiche technique 048833` |
| Reference installation height | `2.5 m` | `fiche technique 048833` |
| Maximum-sensitivity coverage diameter | approximately `6 m` | `fiche technique 048833` |
| Maximum-sensitivity coverage area | approximately `28 m²` | `fiche technique 048833` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `33` | Canonical catalogue |
| Technical item description | PIR surface ceiling mounted sensor | Canonical catalogue |
| Item family | `5` - Light / Motion detector | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `18` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `130` | `-1` | `-1` | `1` | `1` | `-1` |

Firmware 130 has wildcard version/revision/build applicability and one Module slot.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `130` | `276` | `119` | `119` | Stand alone presence sensor |
| `130` | `277` | `164` | `164` | Scenarios daylight sensor |
| `130` | `278` | `165` | `165` | Scenarios presence sensor |
| `130` | `279` | `166` | `166` | Stand alone daylight sensor |
| `130` | `280` | `168` | `168` | Stand alone daylight and presence sensor |
| `130` | `406` | `128` | `128` | Scenarios daylight and presence sensor |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `277` | `1` | `119` | candidate / non-fixed | Stand alone presence sensor |
| `278` | `1` | `164` | candidate / non-fixed | Scenarios daylight sensor |
| `279` | `1` | `165` | candidate / non-fixed | Scenarios presence sensor |
| `280` | `1` | `166` | candidate / non-fixed | Stand alone daylight sensor |
| `281` | `1` | `168` | candidate / non-fixed | Stand alone daylight and presence sensor |
| `587` | `1` | `128` | fixed | Scenarios daylight and presence sensor |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| `130` | `3` | `515` | `515` | Daylight and motion sensor virgin | `119`, `128`, `164`, `165`, `166`, `168` | `1` |

Slot `1` has six firmware candidate Objects: `119` Stand alone presence sensor, `164` Scenarios daylight sensor, `165` Scenarios presence sensor, `166` Stand alone daylight sensor, `168` Stand alone daylight and presence sensor, and `128` Scenarios daylight and presence sensor. Catalogue slot metadata marks Object `128` fixed and the other five non-fixed candidates. Shared Virgin Object families `515` / `516` are associated with these sensor Objects; candidate ordering is not an active-role selection rule.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `130` | `1` | `1` | Virtual Configuration |
| `130` | `2` | `2` | Advanced Configuration |
| `130` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1, 2 and 3. The official sheet explicitly documents both physical and virtual configuration.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` | `0` | area / environment configurator |
| `PL` | `0..9` | `0` | light-point configurator |
| `M` | `0..8` | `0` | operating / function mode |
| `S` | `0..4` | `0` | sensor sensitivity selector |
| `T` | `0..9` | `0` | time-delay selector |

The catalogue software domain is broader than the printed physical table: database `M` is `0..8` and `S` is `0..4`, while the 048833 sheet gives physical `M` as `0..4` and `S` as `0..3`. The sheet also forbids `A=0` together with `PL=0`. Both scopes are preserved.

## Object configuration surfaces

### Object `119` - Stand alone presence sensor

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R`, `MAIN_GROUP` | target, group, installation-level or network addressing |
| Mode and behavior | `FUNC_MODE` | operating mode and behavior selectors |
| Timing and levels | `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Sensing / regulation | `PIR`, `US`, `INITIAL_OCCUPANCY`, `MAINTAIN_OCCUPANCY`, `RETRIGGER`, `ALERT`, `ENABLE_LOAD_CONTROL` | sensor, occupancy and daylight/regulation parameters |
| Group membership | `G1`, `G2` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `US`, `ALERT`, `INITIAL_OCCUPANCY`, `MAINTAIN_OCCUPANCY`, `RETRIGGER`. The catalogue relation restricts `FUNC_MODE`: `2`. Catalogue irregularity: `GD` (filter `78`) is not present in this reusable Object schema; `TYPE_LOOP` (filter `81`) is not present in this reusable Object schema; `INITIAL_OCC` (filter `84`) is not present in this reusable Object schema; `MAINTAIN_OCC` (filter `85`) is not present in this reusable Object schema; `RE-TRIGGER` (filter `86`) is not present in this reusable Object schema.

### Object `164` - Scenarios daylight sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

### Object `165` - Scenarios presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | PIR only / US only / PIR and US / PIR or US | `4` | Detection scheme |
| `PIR` | Low / Medium / High / Maximum | `3` | PIR sensitivity |
| `US` | Low / Medium / High / Maximum | `2` | US sensitivity |

**Firmware relationship.** The catalogue relation explicitly exposes `US`. The catalogue relation restricts `SCHEMA` to US only (`2`), PIR and US (`3`), or PIR or US (`4`).

### Object `166` - Stand alone daylight sensor

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R`, `GD` | target, group, installation-level or network addressing |
| Mode and behavior | `FUNC_MODE` | operating mode and behavior selectors |
| Sensing / regulation | `TYPE_LOOP`, `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`, `LIGHTING_REGULATION`, `DAYLIGHT_FACTOR`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_LEVEL` | sensor, occupancy and daylight/regulation parameters |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_LOOP`, `DAYLIGHT_FACTOR`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_LEVEL`, `GD`.

### Object `168` - Stand alone daylight and presence sensor

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R`, `MAIN_GROUP`, `GD` | target, group, installation-level or network addressing |
| Mode and behavior | `FUNC_MODE` | operating mode and behavior selectors |
| Timing and levels | `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Sensing / regulation | `TYPE_LOOP`, `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`, `PIR`, `US`, `INITIAL_OCC`, `MAINTAIN_OCC`, `RE-TRIGGER`, `ALERT`, `LOAD_CONTROL`, `LIGHTING_REGULATION`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_FACTOR`, `DAYLIGHT_LEVEL` | sensor, occupancy and daylight/regulation parameters |
| Group membership | `G1`, `G2` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `GD`, `US`, `TYPE_LOOP`, `NATURAL_LIGHT_FACTOR`, `INITIAL_OCC`, `MAINTAIN_OCC`, `RE-TRIGGER`, `ALERT`, `DAYLIGHT_FACTOR`, `DAYLIGHT_LEVEL`, `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`. The catalogue relation restricts `FUNC_MODE`: `2`.

### Object `128` - Scenarios daylight and presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | PIR only / US only / PIR and US / PIR or US | `4` | Detection scheme |
| `PIR` | Low / Medium / High / Maximum | `3` | PIR sensitivity |
| `US` | Low / Medium / High / Maximum | `2` | US sensitivity |

**Firmware relationship.** The catalogue relation explicitly exposes `US`. The catalogue relation restricts `SCHEMA` to US only (`2`), PIR and US (`3`), or PIR or US (`4`).

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `9` | Device/Firmware topology conditions |
| Object/Firmware filters | `35` | Conditional Object configuration exposure |
| Referenced conversion rules | `1` | `6` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `128` | `4478` | `M=2` | `6` |
| `1` | `166` | `4462` | `M=1` | `6` |
| `1` | `166` | `4506` | `M=4` | `6` |
| `1` | `166` | `4546` | `M=7` | `6` |
| `1` | `166` | `4559` | `M=8` | `6` |
| `1` | `168` | `4441` | `M=0` | `6` |
| `1` | `168` | `4492` | `M=3` | `6` |
| `1` | `168` | `4520` | `M=5` | `6` |
| `1` | `168` | `4533` | `M=6` | `6` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `119` | `78` | `GD` | Daylight Sensor group | `1` | - |
| `119` | `79` | `US` | US sensitivity | `1` | - |
| `119` | `81` | `TYPE_LOOP` | Type loop | `1` | - |
| `119` | `83` | `FUNC_MODE` | Functional mode | `0` | `2` |
| `119` | `84` | `INITIAL_OCC` | Initial occupancy | `1` | - |
| `119` | `85` | `MAINTAIN_OCC` | Mantain occupancy | `1` | - |
| `119` | `86` | `RE-TRIGGER` | Re-trigger | `1` | - |
| `119` | `87` | `ALERT` | Alert | `1` | - |
| `119` | `2353` | `INITIAL_OCCUPANCY` | Initial occupancy | `1` | - |
| `119` | `2354` | `MAINTAIN_OCCUPANCY` | Mantain occupancy | `1` | - |
| `119` | `2355` | `RETRIGGER` | Re-trigger | `1` | - |
| `119` | `2356` | `ALERT` | Alert | `1` | - |
| `119` | `2357` | `US` | US sensitivity | `1` | - |
| `128` | `351` | `US` | US sensitivity | `1` | - |
| `128` | `352` | `SCHEMA` | Detection Schema | `0` | `2` - US only<br>`3` - PIR and US<br>`4` - PIR or US |
| `165` | `88` | `US` | US sensitivity | `1` | - |
| `165` | `89` | `SCHEMA` | Detection Schema | `0` | `2` - US only<br>`3` - PIR and US<br>`4` - PIR or US |
| `166` | `92` | `TYPE_LOOP` | Type loop | `1` | - |
| `166` | `2100` | `DAYLIGHT_FACTOR` | Daylight factor | `1` | - |
| `166` | `2115` | `NATURAL_LIGHT_FACTOR` | Natural light factor | `1` | - |
| `166` | `2130` | `DAYLIGHT_LEVEL` | Daylight level | `1` | - |
| `166` | `2358` | `GD` | Daylight sensor group | `1` | - |
| `168` | `96` | `GD` | Daylight Sensor group | `1` | - |
| `168` | `97` | `US` | US sensitivity | `1` | - |
| `168` | `99` | `TYPE_LOOP` | Type loop | `1` | - |
| `168` | `100` | `NATURAL_LIGHT_FACTOR` | natula light | `1` | - |
| `168` | `103` | `FUNC_MODE` | Functional mode | `0` | `2` |
| `168` | `104` | `INITIAL_OCC` | Initial occupancy | `1` | - |
| `168` | `105` | `MAINTAIN_OCC` | Mantain occupancy | `1` | - |
| `168` | `106` | `RE-TRIGGER` | Re-trigger | `1` | - |
| `168` | `107` | `ALERT` | Alert | `1` | - |
| `168` | `2146` | `DAYLIGHT_FACTOR` | Daylight factor | `1` | - |
| `168` | `2361` | `DAYLIGHT_LEVEL` | Daylight level | `1` | - |
| `168` | `2444` | `DAYLIGHT_SETPOINT` | Daylight setpoint (Lux) | `0` | - |
| `168` | `2456` | `PROVISION_OF_LIGHT` | Provision of light (Lux) | `0` | - |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 18`, `BMSE1001` / `048833` and installed identity fields | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assuming wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | identify which of the six candidate sensor Objects is active in the single Module position | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the address appropriate to the resolved sensor/scenario role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | correlate physical `A` / `PL` / `M` / `S` / `T` with role-specific presence/daylight configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on resolved Object/configuration, the Device participates in lighting automation as a presence sensor, daylight sensor, combined sensor or scenario-oriented sensor.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Resolve the active slot Object before exposing configuration. Keep the official physical `A` / `PL` / `M` / `S` / `T` limits distinct from the wider software/database domains.

## Source reconciliation

Database and official documentation agree on the BMSE1001/048833 ceiling sensor identity and on `A` / `PL` / `M` / `S` / `T` as the physical configuration family. The material discrepancy is `S`: the database domain reaches 4 while the official physical sheet prints `0..3`; `M` is likewise broader in the database than the printed `0..4` physical table. Both scopes are preserved.

## Evidence limits and open work

- Hardware-corroborate the resolved Object for representative physical and virtual configurations.
- Preserve the `S` and `M` domain discrepancy until firmware/runtime evidence establishes the exact software-only cases.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [fiche technique 048833](https://archive.openwebnet-ha.org/sha256/96/b2/96b2d164e69405d1c7f3a1b52e3eea061ad02c1fee528c16f35971255406232f.pdf)
