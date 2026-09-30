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
| Declared Modules | 3 | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This Device exposes three independently addressed command Modules under a shared physical mode selector. The official `MQ00290-c-EN` technical sheet directly covers `067554`, `H4652/3`, `L4652/3`, and `AM5832/3`. The catalogue also maps `573975` and `687378` to the same technical item.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `H4652/3` | Established identity | Catalogue + official technical sheet |
| BTicino L/N/NT | `L4652/3` | Established identity | Catalogue + official technical sheet |
| BTicino Matix | `AM5832/3` | Established identity | Catalogue + official technical sheet |
| Legrand Céliane | `067554` | Established catalogue identity | Catalogue + official technical sheet |
| Legrand Arteor | `573975` | Shared technical item | Implementation evidence; product-document review pending |
| Legrand Vela | `687378` | Shared technical item | Implementation evidence; product-document review pending |

The current Legrand web catalogue describes reference `067554` with “Arteor” wording while the canonical MyHOME Suite catalogue assigns that code to the Céliane line. Preserve this as a source/catalogue metadata difference until the historical commercial relationship is resolved.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher URL |
| --- | --- | --- | --- | --- | --- |
| `MQ00290-c-EN` | Technical sheet | 01/08/2013 | `067554`, `H4652/3`, `L4652/3`, `AM5832/3` | [Archived PDF](../../sources/devices/documents/device-doc-basic-control-3-mq00290-c-en/MQ00290_c_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00290_c_EN.pdf) |
| `MQ00290-c-FR` | Technical sheet | revision date to verify | same family | [Archived PDF](../../sources/devices/documents/device-doc-basic-control-3-mq00290-c-fr/MQ00290-c-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00290-c-FR.pdf) |
| `T9807J` | Instruction sheet | revision to verify | L4652/3 family | [Archived PDF](../../sources/devices/documents/device-doc-basic-control-3-t9807j/T9807J.pdf) | [Official source](https://dar.bticino.com/asset/Documents/T9807J.pdf) |
| `LE05420AA` | Instruction sheet | revision to verify | `067554` | [Archived PDF](../../sources/devices/documents/device-doc-basic-control-3-le05420aa/LE05420AA.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE05420AA.pdf) |

## Physical characteristics

The English technical sheet establishes:

| Property | Value |
| --- | --- |
| Width | 3 flush-mounted modules |
| Front controls | 6 pushbuttons with status LEDs |
| SCS nominal supply | `27 Vdc` |
| SCS operating supply | `18..27 Vdc` |
| Current draw | `9 mA` |
| Physical configurator positions | `A1`, `PL1`, `A2`, `PL2`, `A3`, `PL3`, `M` |

The seven printed configurator positions independently support the expected ordinary addressed-form configurator count. An observed `DIMENSION 1` read is still required before recording `N_CONF = 7` as hardware-corroborated.

## Identity and firmware

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `4` | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `3` | Implementation evidence |
| System | Lighting / Automation | Implementation evidence |
| Firmware | `148` | Implementation evidence |
| Firmware applicability | `-1.-1.-1` | Implementation evidence |
| Firmware slots | `3` | Implementation evidence |

Brand/line values depend on the commercial record. `modobj = 3` identifies the shared technical core rather than one printed SKU.

## Module and Object model

Firmware `148` declares three command Modules.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `400` | Light control | `1`, `2`, `3` | designated Object |
| `401` | Automation control | `1`, `2`, `3` | alternative |
| `404` | Scheduled scenario | `1`, `2`, `3` | alternative |
| `406` | Scheduled scenario PLUS | `1`, `2`, `3` | alternative |

Virgin Object `500`, **Automation double command virgin**, applies to all three slots and permits Objects `400`, `401`, `404`, `406`, and `407` (AUX control).

## Configuration modes

The catalogue declares:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration.

## Firmware-scoped configuration

| Field | Catalogue domain | Role |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1`, `A2`, `A3` | `0..9`, `GEN`, `GR`, `AMB`, `AUX` | address scope for each Module |
| `PL1`, `PL2`, `PL3` | `0..9` | point/function value for each Module |
| `M` | `0..9`, `CEN` | shared function selector |

The published sheet documents virtual point-to-point room `0..10`, light point `0..15`, group `1..255`, room, group, and general command forms. The physical form uses the three A/PL pairs and the shared `M` position.

## Condition-selected Object topology

The catalogue uses the shared `M` value to select a different Object pattern across the three slots.

| `M` family | Slot 1 | Slot 2 | Slot 3 | Published interpretation |
| --- | --- | --- | --- | --- |
| no configurator / default | Light control | Light control | Light control | cyclic lighting control |
| `1`, `4` | Light control | Light control | Automation control | mixed lighting + automation cover/function layout |
| `2`, `5` | Light control | Automation control | Automation control | mixed layout |
| `3`, `6` | Automation control | Automation control | Automation control | automation layout |
| `7`, `8`, `9` | Light control | Light control | Light control | lighting ON/OFF / dimming-related layouts |
| `CEN` | Scheduled scenario | Scheduled scenario | Scheduled scenario | six scenario keys for MH200N-style scenario control |
| implementation-only `FAKE` | Scheduled scenario PLUS | Scheduled scenario PLUS | Scheduled scenario PLUS | PLUS scenario projection |

The slot condition rows use conversion rules `31`, `32`, and `33`, one per Module. Generic conversion semantics remain canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md).

The official sheet independently documents lighting control, automation control, programmed scenario activation, and PLUS programmed scenario activation.

## Addressing and function detail

Each of the three Modules has its own address pair:

- control 1: `A1/PL1`;
- control 2: `A2/PL2`;
- control 3: `A3/PL3`.

For physical configuration, the front button pairs correspond left-to-right to those three controls. Virtual configuration supports richer room/group/general addressing and reference-address behavior.

The generic command frame grammar belongs to [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Reusable Object configuration surfaces

The selected Objects reuse the canonical command parameter models:

- Light control `400`: command mode, point/area/group/general address, installation/destination level, reference address, timed and dimming values;
- Automation control `401`: bistable/monostable/blades control and the same address-scope families;
- Scheduled scenario `404`: scenario button numbering and related address fields;
- Scheduled scenario PLUS `406`: PLUS scenario-number/button fields;
- AUX control `407`: AUX command and channel fields when reached through the Virgin Object.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 3`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | obtain actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Object for each of the three command Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine the three Module addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Programming

Programming must preserve three independent Module addresses while applying the one shared physical `M` selector to the Device topology. Do not flatten the Device into one command address.

See [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Corroboration status and open work

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
