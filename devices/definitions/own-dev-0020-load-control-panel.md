# Load Control Panel bus

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0020` | Project identity |
| Technical description | Four-channel SCS load-control status and override panel | Catalogue + official technical sheet |
| Catalogue item | 1465 - Load Control Panel bus | Implementation evidence |
| Main catalogue system | New energy saving / load control | Implementation evidence |
| Item model / `modobj` | `10` | Implementation evidence |
| Firmware definition | wildcard `-1.-1` | Implementation evidence |
| Declared slots | `4` | Implementation evidence |
| Configuration modes | Virtual, Advanced, Physical | Implementation evidence |
| Object | 492 - Load control actuator visualization | Implementation evidence |
| Categories | Energy Management, User Interface | Product and capability model |

The load-control panel is a four-button SCS user interface for loads managed by the load-control system. It displays load state and permits a user override / re-enable action. The catalogue represents each of the four positions with the same fixed visualization Object and derives per-position priority from the product configurators.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC/HS/HD4673` | Documented commercial identity | Catalogue + MQ00709 technical sheet |
| BTicino L/N/NT | `L/N/NT4673` | Documented commercial identity | Catalogue + MQ00709 technical sheet |
| Legrand Arteor | `573985` | Documented commercial identity | Catalogue + MQ00709 technical sheet |
| Legrand Arteor | `573991` | Documented commercial identity | Catalogue + MQ00709 technical sheet |
| Legrand Céliane | `067206` | Documented commercial identity | Catalogue + MQ00709 technical sheet |
| Legrand Céliane | `067207` | Documented commercial identity | Catalogue + MQ00709 technical sheet |

The technical sheet names the corresponding 4673, `067206`/`067207` and `573985`/`573991` families, giving unusually strong commercial corroboration for the current six-record catalogue cluster.

## Documentation

| Document | Coverage | Status |
| --- | --- | --- |
| `MQ00709_c_EN` | Four-channel load-control panel family | [Archived original](../../sources/devices/documents/device-doc-load-control-mq00709-c-en/MQ00709_c_EN.pdf) |
| MyHOME catalogue HPML0714 | Load-control system context | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) |

## Physical and functional characteristics

MQ00709 documents a two-module device with four buttons and four red LEDs connected to the SCS bus. It displays the state of loads controlled by the load-control system and allows operation to be forced independently of the central unit; the documented temporary re-enable behavior is four hours. The sheet specifies SCS `18..27` Vdc, maximum `7 mA`, and an operating range of `0..40` °C for the covered family.

These product-level facts complement the catalogue topology below: the four OpenWebNet Modules represent the four panel positions, not four different Object types.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1465` | Implementation evidence |
| main system | New energy saving / load control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `10` | Implementation evidence |
| family | catalogue energy-management family | Implementation evidence |

## Firmware and Module model

Firmware id 232 uses wildcard version/revision `-1.-1` and declares four slots. All four slots are fixed instances of Object `492`, Load control actuator visualization.

| Slot | Object | Relationship |
| ---: | ---: | --- |
| `1` | `492` | fixed |
| `2` | `492` | fixed |
| `3` | `492` | fixed |
| `4` | `492` | fixed |

There is no Virgin Object.

## Configuration modes

The catalogue declares Virtual Configuration, Advanced Configuration and Physical configuration. The technical sheet documents physical configurators and MyHOME_Suite configuration. It also defines a self-learning setup selected by `M=1` with the priority configurators cleared.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | Device identity |
| `P1AB` | `0..6` | 0 | shared priority/configurator field for positions A/B |
| `P2A` | `0..9` or `OFF` | 0 | position A sub-priority / disable selector |
| `P2B` | `0..9` or `OFF` | 0 | position B sub-priority / disable selector |
| `P1CD` | `0..6` | 0 | shared priority/configurator field for positions C/D |
| `P2C` | `0..9` or `OFF` | 0 | position C sub-priority / disable selector |
| `P2D` | `0..9` or `OFF` | 0 | position D sub-priority / disable selector |
| `M` | 0 Normal / 1 Self learning | 0 | operating/configuration mode |

`OFF` is represented by catalogue value 10 in the P2 fields. The dossier keeps both the encoded value and the human label distinct.

## Slot applicability conditions

The current catalogue uses explicit conditions for normal mode:

| Slot | Normal-mode condition using shared P1 | Fallback normal-mode condition | Conversion reference |
| ---: | --- | --- | ---: |
| 1 / A | `M=0`; P1ab<>0; P2a<>`OFF` | `M=0`; P1ab=0; P2a<>`OFF`; P2a<>0 | 421 |
| 2 / B | `M=0`; P1ab<>0; P2b<>`OFF` | `M=0`; P1ab=0; P2b<>`OFF`; P2b<>0 | 431 |
| 3 / C | `M=0`; P1cd<>0; P2c<>`OFF` | `M=0`; P1cd=0; P2c<>`OFF`; P2c<>0 | 441 |
| 4 / D | `M=0`; P1cd<>0; P2d<>`OFF` | `M=0`; P1cd=0; P2d<>`OFF`; P2d<>0 | 451 |

All four slots also carry the self-learning condition:

`M=1`; P1ab=0; P2a=0; P2b=0; P1cd=0; P2c=0; P2d=0

The slot-condition rows reference conversion identifiers 421, 431, 441 and 451, but no matching rows were found in `EN_CONV_RULE` in the canonical catalogue copy. The references are therefore preserved as unresolved implementation evidence; this definition does not fabricate the missing arithmetic.

## Reusable Object configuration

Object `492` exposes:

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | 1 | load-control priority represented by the Module |
| `PHASE` | 0 Single/undefined, 1 Phase 1/R, 2 Phase 2/S, 3 Phase 3/T | 0 | electrical phase association |

The source-level `PRIORITY` domain is wider than the physical `P1` / `P2` configurator digits. The missing conversion records are therefore material: a consumer should use an already resolved Object value when available and must not guess how `P1` / `P2` compose into 0..63.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 10 / commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the four fixed visualization Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect per-position load-control addressing if exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `PRIORITY`, `PHASE` and product configurators where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The panel belongs to load / energy management. Product documentation establishes status visualization and user override behavior; the catalogue establishes the four fixed OpenWebNet visualization Objects and their parameter domains. Generic energy-management protocol semantics remain canonical under Functional Protocol.

## Programming and self learning

Normal physical configuration uses `P1AB` / `P1CD` plus the per-position P2 configurators. `M=1` selects self-learning only when all `P1` / `P2` fields are zero, exactly matching the explicit catalogue condition. Virtual and Advanced configuration are also declared. Software should represent self-learning as a product-level configuration mode, not as a fifth Module.

## Evidence limits and open work

- Obtain a sanitized four-slot DIM30/DIM35 fingerprint from a known panel.
- Recover or independently establish the missing conversion logic referenced as 421/431/441/451.
- Verify how `PRIORITY` `0..63` maps to physical `P1` / `P2` values before implementing a converter.
- Correlate wildcard firmware applicability with observed firmware versions.
- Check whether phase configuration is surfaced consistently across all six commercial identities.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
