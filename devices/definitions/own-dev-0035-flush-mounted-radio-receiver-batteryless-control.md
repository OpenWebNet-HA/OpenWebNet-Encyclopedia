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
| BTicino / Axolute | `HC/HS/HD4575SB` | `40` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `L/N/NT4575SB` | `1841` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | 4575SB receiver sections; exact page locator pending | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | 4575SB electrical/radio data; exact page locator pending | [Archived PDF](../../sources/devices/documents/device-doc-radio-wired-interface-sound-guide/mh_diff-sonore2008.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |

Exact printed and 1-based PDF page locations remain an explicit reconciliation item until pinned.

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

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `218` | `-1` | `-1` | `4` | `1` | `0` |

Firmware 218 has wildcard version/revision/build applicability and four Module slots.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `218` | `608` | `400` | `400` | Light control |
| `218` | `609` | `403` | `403` | Scenario module control |
| `218` | `610` | `401` | `401` | Automation control |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1011` | `1` | `400` | fixed | Light control |
| `1015` | `1` | `403` | candidate / non-fixed | Scenario module control |
| `1019` | `1` | `401` | candidate / non-fixed | Automation control |
| `1012` | `2` | `400` | fixed | Light control |
| `1016` | `2` | `403` | candidate / non-fixed | Scenario module control |
| `1013` | `3` | `400` | fixed | Light control |
| `1017` | `3` | `403` | candidate / non-fixed | Scenario module control |
| `1020` | `3` | `401` | candidate / non-fixed | Automation control |
| `1014` | `4` | `400` | fixed | Light control |
| `1018` | `4` | `403` | candidate / non-fixed | Scenario module control |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

Object `400` Light control is fixed on slots `1`, `2`, `3` and `4`. Object `403` Scenario module control is a non-fixed candidate on all four slots. Object `401` Automation control is a non-fixed candidate on slots `1` and `3`. Shared Virgin Object families `500` / `501` / `502` cover the corresponding Light, Automation and Scenario control Objects.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `218` | `1` | `1` | Virtual Configuration |
| `218` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` | `0` | area / environment configurator |
| `PL1` | `0..9` | `0` | output 1 light-point configurator |
| `M1` | `0..8` / `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` | `0` | channel 1 operating mode |
| `PL2` | `0..9` | `0` | output 2 light-point configurator |
| `M2` | `0..8` / `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` | `0` | channel 2 operating mode |
| `SPE` | `0` / `1` / `6` | `0` | special-function selector |

`M1` / `M2` select the command behavior for the two control positions; `SPE` is the special-function selector. Slot/Object conditions further constrain which reusable control Object is active.

## Object configuration surfaces

### Object `400` - Light control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R` | target, group, installation-level or network addressing |
| Mode and behavior | `M` | operating mode and behavior selectors |
| Timing and levels | `HOURS`, `MINUTES`, `SECONDS`, `LEVEL`, `START_S`, `STOP_S`, `DIMMING_S`, `T_TIME` | timers, delays, levels and transition parameters |
| Object-specific | `INST_LEV`, `DEST_LEV`, `IN_AUX_CHANNEL` | additional reusable fields defined by this Object |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

### Object `403` - Scenario module control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | Scenario activation and modification / Scenario activation | `0` | Modality |
| `APL` | `A`: `0..10`; `PL`: `0..15` (catalogue-composed address) | `0` | Scenario module address |
| `INST_LEV` | private riser / local bus `1..15` / standard | `16` | Installation level |
| `DEST_LEV` | private riser / local bus `1..15` / all systems | `0` | Destination level |
| `SCE_BUTT_1` | `1..16` | `1` | Upper button scenario |
| `SCE_BUTT_2` | `1..16` | `2` | Lower button scenario |
| `DEL_BUTTON_1` | none / catalogue delay scale from seconds to minutes | `0` | Activation delay for upper button |
| `DEL_BUTTON_2` | none / catalogue delay scale from seconds to minutes | `0` | Activation delay for lower button |

**Firmware relationship.** The catalogue relation restricts `INST_LEV` to encoded value `8` (catalogue label `Level 4 #8`).

### Object `401` - Automation control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R` | target, group, installation-level or network addressing |
| Mode and behavior | `M` | operating mode and behavior selectors |
| Object-specific | `INST_LEV`, `DEST_LEV`, `IN_AUX_CHANNEL` | additional reusable fields defined by this Object |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `12` | Device/Firmware topology conditions |
| Object/Firmware filters | `1` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `1` | `401` | `4305` | `M1=SU_GIU;SPE<>6` | - |
| `1` | `401` | `4313` | `M1=SU_GIU_M;SPE<>6` | - |
| `1` | `403` | `4857` | `SPE=6` | - |
| `2` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `2` | `403` | `4899` | `SPE=7` | - |
| `3` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `3` | `401` | `4416` | `M2=SU_GIU;SPE<>6` | - |
| `3` | `401` | `4422` | `M2=SU_GIU_M;SPE<>6` | - |
| `3` | `403` | `4874` | `SPE=8` | - |
| `4` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `4` | `403` | `4877` | `SPE=9` | - |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `403` | `1109` | `INST_LEV` | Installation level | `0` | `8` - Level 4 #8 |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

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
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
