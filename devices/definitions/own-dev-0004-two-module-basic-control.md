# Two-module basic control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0004` | Project identity |
| Technical description | Two-module, two-channel configurable SCS control | Catalogue + official technical sheet |
| Catalogue item | `281` - “Basic control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `2` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `145` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This technical definition covers the shared catalogue capability core used by 19 commercial Device records. The official `MQ00286-d-EN` technical sheet directly covers four of those references - `067552`, `H4652/2`, `L4652/2`, and `AM5832/2`. The remaining catalogue records are retained as commercial identities associated with item `281`, but their packaging, range, and exact commercial equivalence still require product-document review.

## Commercial identities


### Directly documented references

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `H4652/2` | Established identity | Catalogue + `MQ00286-d-EN` |
| BTicino L/N/NT | `L4652/2` | Established identity | Catalogue + `MQ00286-d-EN` |
| BTicino Matix | `AM5832/2` | Established identity | Catalogue + `MQ00286-d-EN` |
| Legrand Céliane | `067552` | Established identity | Catalogue + `MQ00286-d-EN` |

### Additional commercial records sharing item 281

| Brand / line | References | Status |
| --- | --- | --- |
| Arnould Espace Evolution | `64160`, `64161`, `64360` | Shared technical item; individual product-document review pending |
| Legrand Arteor | `571848`, `573974` | Shared technical item; individual product-document review pending |
| Legrand Matix | `078473` | Shared technical item; individual product-document review pending |
| Legrand Mosaic | `078462`, `078463`, `078471`, `079171`, `079173`, `079262`, `079263` | Shared technical item; individual product-document review pending |
| Legrand, catalogue line undefined | `067241` | Shared technical item; product-line/document review pending |
| Legrand Vela | `687377` | Shared technical item; individual product-document review pending |

Sharing one `EN_ITEM` establishes a common catalogue capability core. It does not by itself prove that every commercial package is physically identical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00286-d-EN` - Basic control for 2 independent loads | Technical sheet | 20/01/2014 | `067552`, `H4652/2`, `L4652/2`, `AM5832/2` | [Archived original](../../sources/devices/documents/device-doc-basic-control-mq00286-d-en/MQ00286-d-EN.pdf) | [Official PDF](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00286-d-en.pdf) |

Additional language revisions and product-range-specific sheets should be collected rather than treating this one document as exhaustive.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Controls | 4 buttons | Official technical sheet |
| Indicators | two-colour LEDs with local brightness/off adjustment | Official technical sheet |
| SCS nominal supply | `27 Vdc` | Official technical sheet |
| SCS operating supply | `18..27 Vdc` | Official technical sheet |
| Maximum LED-brightness current | `6 mA` for `H4652/2`; `8.5 mA` for `L4652/2`, `AM5832/2`, `067552` | Official technical sheet |
| Physical configurator positions | `A1`, `PL1`, `M1`, `A2`, `PL2`, `M2` | Official technical sheet |

The official technical sheet establishes the following for its four named references:


The six documented physical configurator positions are consistent with the ordinary diagnostic interpretation of `N_CONF`, but an observed `DIMENSION 1` value for known hardware is still needed before recording `N_CONF = 6` as corroborated behavior.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `281` | Canonical catalogue |
| Item model / `modobj` | `2` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `145` | `-1` | `-1` | `-1` | `2` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `145` | `400` | Light control | catalogue firmware/Object relation |
| `145` | `401` | Automation control | catalogue firmware/Object relation |
| `145` | `404` | Scheduled scenario | catalogue firmware/Object relation |
| `145` | `406` | Scheduled scenario PLUS | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `145` | `500` | catalogue candidate/template association |

### Reconciled topology notes


Firmware `145` exposes two configurable Modules.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `400` | Light control | `1`, `2` | designated Object |
| `401` | Automation control | `1`, `2` | alternative |
| `404` | Scheduled scenario | `1`, `2` | alternative |
| `406` | Scheduled scenario PLUS | `1`, `2` | alternative |

Virgin Object `500`, **Automation double command virgin**, applies to slots `1` and `2` and permits Objects `400`, `401`, `404`, `406`, and `407` (AUX control).

Installed Object selection belongs to [`DIMENSION 30`](../../diagnostics/dim30-modules.md); generic frame syntax is not repeated here.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `145` | Physical configuration | retained Device-specific configuration modality |
| `145` | Virtual Configuration | retained Device-specific configuration modality |
| `145` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares all three modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration. It also documents Lighting Management configuration modes such as Plug&go, Push&Learn, and Project&Download for the named product variants.

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `145` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `145` | `A1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `145` | `PL1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `145` | `M1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `145` | `A2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `145` | `PL2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `145` | `M2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


The complete firmware-scoped configuration surface is:

| Field | Domain | Meaning / document correlation |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1`, `A2` | `0..9`, `GEN=12`, `GR=13`, `AMB=14`, `AUX=15` | channel address scope |
| `PL1`, `PL2` | `0..9` | physical point / function value |
| `M1`, `M2` | `0..8`, `O/I=9`, `OFF=10`, `ON=11`, `UP/DOWN=12`, `UP/DOWN monostable=13`, `CEN=14`, `PUL=15` | channel mode |

The official sheet uses physical `A=1..9` and `PL=1..9` for ordinary point-to-point addressing, while the database stores `0` in the firmware-level domains. Preserve that source-level distinction.

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


The Objects reachable from the Device expose these reusable configuration families:

| Object | Principal configuration surface |
| ---: | --- |
| `400` Light control | mode; point/area/group/general address; installation/destination level; reference address; timed and dimmer parameters; AUX input |
| `401` Automation control | bistable/monostable/blades mode; point/area/group/general address; installation/destination level; reference address; AUX input |
| `404` Scheduled scenario | `A`, `PL`, upper/lower button `0..31`, AUX input, restart delay |
| `406` Scheduled scenario PLUS | scenario number split across low/high fields; upper/lower button `0..31` |
| `407` AUX control | toggle/ON/OFF/PUL/automation/reset/enable-disable modes; AUX output channel `1..15`; AUX input `0..15` |

These are reusable Object definitions. A value appearing in a reusable Object enum is not automatically a physically reachable configuration of this Device; firmware conditions and conversion rules remain authoritative for reachability.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `263`, `264`, `265`, `266`, `267`, `268`, `269`, `270`, `271`, `272`, `273`, `277`, `278`, `279`, `281`, `1701` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | `4165`, `4167`, `4169`, `4171`, `4173`, `4175`, `4192`, `4233`, `4234`, `4236`, `4237`, `4254`, `4269`, `4270`, `4271`, `4274`, `4275`, `4277`, `4278`, `4281`, `4282`, `4284`, `4285`, `4286`, `4287`, `4289`, `4290`, `4293`, `4294`, `4296`, `4297`, `4300`, `4301`, `4303`, `4304`, `4308`, `4309`, `4311`, `4312`, `4314`, `4315`, `4316`, `4318`, `4319`, `4389`, `4390`, `4391`, `4392`, `4394`, `4395`, `4396`, `4397`, `4399`, `4400`, `4401`, `4402`, `4404`, `4405`, `4406`, `4407`, `4409`, `4410`, `4411`, `4412`, `4414`, `4415`, `4417`, `4418`, `4420`, `4421` | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `281` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`400`, `401`, `404`, `406`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 2`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, and physical Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Objects on the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


For the four references named by `MQ00286-d-EN`, the sheet documents:

- point-to-point, room, group, and general lighting addressing;
- lighting cyclic, ON, OFF, pushbutton, timed-ON, and dimming functions;
- automation bistable, monostable, and lath/blade control;
- programmed scenario buttons `0..31`;
- PLUS scenario number `1..2047` and button number `0..31` through virtual configuration;
- Lighting Management virtual functions including dual light, CEN, CEN PLUS, and AUX control.

The exact generic functional frame grammar remains canonical under [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


A programmer should resolve each Module independently from the physical/virtual configuration, then apply the selected Object configuration and conversion rules. Generic write/read-back mechanics remain in [Programming](../../programming/).

## Source reconciliation


`MQ00286-d-EN` has been reconciled beyond the high-level Object list:

- physical and virtual configuration both support point-to-point, room, group and general lighting control, but the published physical ranges and the reusable Object ranges are not identical;
- the Device supports timed-ON and dimming variants in addition to simple cyclic/ON/OFF/pushbutton behavior;
- load-status feedback for room/group/general commands is tied to a reference actuator address in software configuration rather than being implied by the command address alone;
- CEN-only use has a product-level configuration constraint: secondary address positions that are not part of the CEN function must remain unconfigured rather than being treated as independent command channels;
- local LED behavior and brightness adjustment are part of the Device user interface and remain distinct from the OpenWebNet command Modules.

The archived technical sheet has therefore been reconciled into both the physical configuration model and the reusable Object model; remaining incompleteness concerns other commercial variants and hardware corroboration.

## Evidence limits and open work


- Archive and hash `MQ00286-d-EN`, its language variants, and older/newer revisions.
- Locate authoritative product documents for the other 15 commercial records sharing item `281`.
- Capture a sanitized fingerprint from known hardware to corroborate `modobj`, `N_CONF`, firmware, Module/Object projection, addressing, and configuration.
- Establish which commercial variants differ only in finish/package and which have material hardware differences.
- Preserve any disagreement between product documentation and the catalogue rather than normalizing it away.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
