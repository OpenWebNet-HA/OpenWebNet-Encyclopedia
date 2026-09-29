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
| Declared Modules | 2 | Implementation evidence |
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

| Document | Type | Revision / date | Coverage | Status | Source |
| --- | --- | --- | --- | --- | --- |
| `MQ00286-d-EN` - Basic control for 2 independent loads | Technical sheet | 20/01/2014 | `067552`, `H4652/2`, `L4652/2`, `AM5832/2` | Official source identified; archival copy pending | [Official PDF](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00286-d-en.pdf) |

Additional language revisions and product-range-specific sheets should be collected rather than treating this one document as exhaustive.

## Physical characteristics

The official technical sheet establishes the following for its four named references:

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Controls | 4 buttons | Official technical sheet |
| Indicators | two-colour LEDs with local brightness/off adjustment | Official technical sheet |
| SCS nominal supply | `27 Vdc` | Official technical sheet |
| SCS operating supply | `18..27 Vdc` | Official technical sheet |
| Maximum LED-brightness current | `6 mA` for `H4652/2`; `8.5 mA` for `L4652/2`, `AM5832/2`, `067552` | Official technical sheet |
| Physical configurator positions | `A1`, `PL1`, `M1`, `A2`, `PL2`, `M2` | Official technical sheet |

The six documented physical configurator positions are consistent with the ordinary diagnostic interpretation of `N_CONF`, but an observed `DIMENSION 1` value for known hardware is still needed before recording `N_CONF = 6` as corroborated behavior.

## Identity and firmware

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `281` | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `2` | Implementation evidence |
| System | Lighting / Automation | Implementation evidence |
| Firmware | `145` | Implementation evidence |
| Firmware version | `-1.-1.-1` | Implementation evidence |
| Firmware slots | `2` | Implementation evidence |

The `-1` firmware components are wildcard/unspecified applicability in the catalogue, not a physical firmware version.

Brand and line values vary across the 19 commercial records. Therefore `modobj = 2` identifies the shared technical item, while `BRAND` and `LINE` are needed to resolve a particular commercial record. See [`DIMENSION 1` Device Identity](../../diagnostics/dim1-device-identity.md).

## Module and Object model

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

The catalogue declares all three modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration. It also documents Lighting Management configuration modes such as Plug&go, Push&Learn, and Project&Download for the named product variants.

## Firmware-scoped configuration

The complete firmware-scoped configuration surface is:

| Field | Domain | Meaning / document correlation |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1`, `A2` | `0..9`, `GEN=12`, `GR=13`, `AMB=14`, `AUX=15` | channel address scope |
| `PL1`, `PL2` | `0..9` | physical point / function value |
| `M1`, `M2` | `0..8`, `O/I=9`, `OFF=10`, `ON=11`, `UP/DOWN=12`, `UP/DOWN monostable=13`, `CEN=14`, `PUL=15` | channel mode |

The official sheet uses physical `A=1..9` and `PL=1..9` for ordinary point-to-point addressing, while the database stores `0` in the firmware-level domains. Preserve that source-level distinction.

## Device-specific function selection

The catalogue condition matrix selects Objects from the physical configuration.

| Configuration family | Selected Object | Notes |
| --- | --- | --- |
| ordinary, `O/I`, `OFF`, `ON`, `PUL` modes | `400` Light control | address-scope conversion depends on `A1/A2` |
| `UP/DOWN`, `UP/DOWN monostable` | `401` Automation control | per channel |
| `CEN` | `404` Scheduled scenario | per channel; cross-channel CEN rules also exist |
| stored `FAKE` branch | `406` Scheduled scenario PLUS | implementation-only selector; not in physical `M` enum |

The condition set uses conversion rules `4`, `17`, `18`, `93`, `94`, `95`, `96`, and `97`. Generic rule evaluation belongs in [Catalogue Resolution](../../internals/catalogue-resolution.md).

The official sheet corroborates the same high-level capability set: lighting control, automation control, programmed scenarios, and PLUS programmed scenarios.

## Reusable Object configuration surfaces

The Objects reachable from the Device expose these reusable configuration families:

| Object | Principal configuration surface |
| ---: | --- |
| `400` Light control | mode; point/area/group/general address; installation/destination level; reference address; timed and dimmer parameters; AUX input |
| `401` Automation control | bistable/monostable/blades mode; point/area/group/general address; installation/destination level; reference address; AUX input |
| `404` Scheduled scenario | `A`, `PL`, upper/lower button `0..31`, AUX input, restart delay |
| `406` Scheduled scenario PLUS | scenario number split across low/high fields; upper/lower button `0..31` |
| `407` AUX control | toggle/ON/OFF/PUL/automation/reset/enable-disable modes; AUX output channel `1..15`; AUX input `0..15` |

These are reusable Object definitions. A value appearing in a reusable Object enum is not automatically a physically reachable configuration of this Device; firmware conditions and conversion rules remain authoritative for reachability.

## Published function details

For the four references named by `MQ00286-d-EN`, the sheet documents:

- point-to-point, room, group, and general lighting addressing;
- lighting cyclic, ON, OFF, pushbutton, timed-ON, and dimming functions;
- automation bistable, monostable, and lath/blade control;
- programmed scenario buttons `0..31`;
- PLUS scenario number `1..2047` and button number `0..31` through virtual configuration;
- Lighting Management virtual functions including dual light, CEN, CEN PLUS, and AUX control.

The exact generic functional frame grammar remains canonical under [WHO 1 - Lighting](../../functional/who-1-lighting/) and [WHO 2 - Automation](../../functional/who-2-automation/).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 2`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, and physical Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Objects on the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Programming

A programmer should resolve each Module independently from the physical/virtual configuration, then apply the selected Object configuration and conversion rules. Generic write/read-back mechanics remain in [Programming](../../programming/).

## Corroboration status and open work

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
