# Three-module basic control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0007` | Project identity |
| Technical description | Three-module, six-button configurable SCS control for three independent loads/functions | Catalogue + official technical sheet |
| Catalogue item | `4` - “Basic control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `3` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `148` | Implementation evidence |
| Declared Modules | `3` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This Device exposes three independently addressed command Modules under a shared physical mode selector. The official `MQ00290-c-EN` technical sheet directly covers `067554`, `H4652/3`, `L4652/3`, and `AM5832/3`. The catalogue also maps `573975` and `687378` to the same technical item.

## Commercial identities


| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4652/3` | Established identity | Catalogue + official technical sheet |
| BTicino - LivingLight | `L4652/3` | Established identity | Catalogue + official technical sheet |
| BTicino - Matix | `AM5832/3` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067554` | Established catalogue identity | Catalogue + official technical sheet |
| Legrand - Arteor | `573975` | Shared technical item | Implementation evidence; product-document review pending |
| Legrand - Vela | `687378` | Shared technical item | Implementation evidence; product-document review pending |

The current Legrand web catalogue describes reference `067554` with “Arteor” wording while the canonical MyHOME Suite catalogue assigns that code to the Céliane line. Preserve this as a source/catalogue metadata difference until the historical commercial relationship is resolved.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00290-c-EN` | Technical sheet | 01/08/2013 | `067554`, `H4652/3`, `L4652/3`, `AM5832/3` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/21/3c/213cc3f253156d5ef9c7311ff6a1a5f9ae6c48405991341ded7f7b3a94517a85.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00290_c_EN.pdf) |
| `MQ00290-c-FR` | Technical sheet | revision date to verify | same family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/48/79/48794f03e6d3bc4b5e200f3ebf49de93f7d85f4c29714869914e11752b8cff2e.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00290-c-FR.pdf) |
| `T9807J` | Instruction sheet | revision to verify | L4652/3 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/3e/59/3e59e4fbc2a4cbfb4f70b85750d2d970f750e8ac81c79af99f91c332c7512cc5.pdf) | [Official source](https://dar.bticino.com/asset/Documents/T9807J.pdf) |
| `LE05420AA` | Instruction sheet | revision to verify | `067554` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/c5/f9/c5f96fb6a845ad7c7b2ffc5b41c232c446ed6e1d306585e133ca56f263fdaf17.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE05420AA.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Width | 3 flush-mounted modules | Publisher documentation cited in this section |
| Front controls | 6 pushbuttons with status LEDs | Publisher documentation cited in this section |
| SCS nominal supply | `27 Vdc` | Publisher documentation cited in this section |
| SCS operating supply | `18..27 Vdc` | Publisher documentation cited in this section |
| Current draw | `9 mA` | Publisher documentation cited in this section |
| Physical configurator positions | `A1`, `PL1`, `A2`, `PL2`, `A3`, `PL3`, `M` | Publisher documentation cited in this section |

The English technical sheet establishes:


The seven printed configurator positions independently support the expected ordinary addressed-form configurator count. An observed `DIMENSION 1` read is still required before recording `N_CONF = 7` as hardware-corroborated.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `4` | Canonical catalogue |
| Item model / `modobj` | `3` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `148` | `-1` | `-1` | `-1` | `3` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `148` | `401` | Automation control | catalogue firmware/Object relation |
| `148` | `404` | Scheduled scenario | catalogue firmware/Object relation |
| `148` | `406` | Scheduled scenario PLUS | catalogue firmware/Object relation |
| `148` | `400` | Light control | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `148` | `500` | catalogue candidate/template association |

### Reconciled topology notes


Firmware `148` declares three command Modules.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `400` | Light control | `1`, `2`, `3` | designated Object |
| `401` | Automation control | `1`, `2`, `3` | alternative |
| `404` | Scheduled scenario | `1`, `2`, `3` | alternative |
| `406` | Scheduled scenario PLUS | `1`, `2`, `3` | alternative |

Virgin Object `500`, **Automation double command virgin**, applies to all three slots and permits Objects `400`, `401`, `404`, `406`, and `407` (AUX control).

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `148` | Physical configuration | retained Device-specific configuration modality |
| `148` | Virtual Configuration | retained Device-specific configuration modality |
| `148` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration.

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `148` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `A1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `PL1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `A2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `PL2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `A3` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `PL3` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `148` | `M` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


| Field | Catalogue domain | Role |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1`, `A2`, `A3` | `0..9`, `GEN`, `GR`, `AMB`, `AUX` | address scope for each Module |
| `PL1`, `PL2`, `PL3` | `0..9` | point/function value for each Module |
| `M` | `0..9`, `CEN` | shared function selector |

The published sheet documents virtual point-to-point room `0..10`, light point `0..15`, group `1..255`, room, group, and general command forms. The physical form uses the three A/PL pairs and the shared `M` position.

## Object configuration surfaces

### Object `400` - Light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STOP_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DIMMING_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `T_TIME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `401` - Automation control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_DELAY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `406` - Scheduled scenario PLUS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PPT_CEN_HIG` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes

The selected Objects reuse these canonical command parameter models:

| Object | Principal configuration surface |
| --- | --- |
| `400` Light control | command mode; point/area/group/general address; installation/destination level; reference address; timed and dimming values |
| `401` Automation control | bistable/monostable/blades control; point/area/group/general address; installation/destination level |
| `404` Scheduled scenario | scenario button numbering; related address fields |
| `406` Scheduled scenario PLUS | PLUS scenario-number and button fields |
| `407` AUX control | AUX command and channel fields when reached through the Virgin Object |

These are reusable Object definitions; Device reachability remains governed by the firmware conditions, filters, and conversion rules documented below.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `298`, `299`, `300`, `301`, `304`, `562`, `563`, `564`, `565`, `566`, `567`, `568`, `569`, `570`, `571`, `572`, `1702` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | `4464`, `4465`, `4466`, `4467`, `4468`, `4469`, `4470`, `4471`, `4472`, `4473`, `4474`, `4475`, `4479`, `4480`, `4481`, `4482`, `4483`, `4484`, `4485`, `4486`, `4487`, `4488`, `4489`, `4490`, `4493`, `4494`, `4495`, `4496`, `4497`, `4498`, `4499`, `4500`, `4501`, `4502`, `4503`, `4504`, `4507`, `4508`, `4509`, `4510`, `4511`, `4512`, `4513`, `4514`, `4515`, `4516`, `4517`, `4518`, `4521`, `4522`, `4523`, `4524`, `4525`, `4526`, `4527`, `4528`, `4529`, `4530`, `4531`, `4532`, `4534`, `4535`, `4536`, `4537`, `4538`, `4539`, `4540`, `4541`, `4542`, `4543`, `4544`, `4545`, `4547`, `4548`, `4549`, `4550`, `4551`, `4552`, `4553`, `4554`, `4555`, `4556`, `4557`, `4558`, `4560`, `4561`, `4562`, `4563`, `4564`, `4565`, `4566`, `4567`, `4568`, `4569`, `4570`, `4571`, `4572`, `4573`, `4574`, `4575`, `4576`, `4577`, `4578`, `4579`, `4580`, `4581`, `4582`, `4583`, `4587`, `4588`, `4589`, `4594` | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `4` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`400`, `401`, `404`, `406`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 3`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | obtain actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Object for each of the three command Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine the three Module addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Functional applicability follows the resolved firmware/Object topology and the documented product roles above.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


Programming must preserve three independent Module addresses while applying the one shared physical `M` selector to the Device topology. Do not flatten the Device into one command address.

See [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The archived `MQ00290` and installation sheets add Device-specific behavior to the three independent command Modules:

- the shared physical `M` selector changes the function family of all three A/PL pairs and therefore cannot be interpreted independently per Module;
- physical and virtual configuration cover point-to-point, room, group and general lighting scopes, programmed scenarios, CEN/CEN PLUS behavior and automation control;
- software configuration can associate return-of-load status with a reference actuator address for non-point-to-point commands;
- CEN-only use has product-level constraints on address positions that are not used by the CEN function;
- the published PLUS scenario representation uses the wider software scenario domain rather than only the physical selector values;
- LED/mechanical behavior remains a commercial/package concern and should not be inferred solely from the shared item.

The current source set is reconciled for the core product family; direct documentation for `573975` and `687378` remains outstanding.

## Evidence limits and open work


- Locate product-specific documentation for `573975` and `687378`.
- Resolve the Céliane/Arteor wording discrepancy for reference `067554`.
- Add a sanitized hardware fingerprint to corroborate `modobj`, firmware, expected configurator count, Module Objects, addresses, and configuration.
- Verify whether all package/finish variants expose identical LED and mechanical behavior.
- Continue archival discovery for older technical-sheet revisions and language variants.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
