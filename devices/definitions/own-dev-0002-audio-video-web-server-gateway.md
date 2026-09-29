# Audio/video web server and OpenWebNet gateway

## Summary

| Field | Value |
| --- | --- |
| Device ID | `OWN-DEV-0002` |
| Technical description | Audio/video web server and OpenWebNet gateway |
| Categories | Gateway, Interface |
| Documentation status | Partial |

BTicino F454 is a six-DIN-module MyHOME audio/video web server that can operate as an integration gateway. Vendor documentation states that it replaced F453 and F453AV.

## Commercial identities

| Brand | SKU / reference | Region / line | Relationship | Evidence |
| --- | --- | --- | --- | --- |
| BTicino | F454 | MyHOME | Established identity | Vendor documentation, catalogue resolution, and first-hand gateway capture |

F453 and F453AV are predecessor products, not synonyms, and are not folded into this Device definition.

## Documentation

The source archive is not yet populated for this Device. The vendor still exposes an unusually rich historical document set, making F454 a good test case for the archival workflow.

| Document | Type | Revision / date | Language | Archived original | Source |
| --- | --- | --- | --- | --- | --- |
| `MQ00519-c-EN` | Technical sheet | Vendor copy | EN | Pending | [BTicino/Legrand product documentation](https://www.legrand.rw/en/catalog/products/myhome-audiovideo-web-server-for-the-remote-control-of-the-system-using-web-pages-or-the-my-home-portal-f454) |
| `O1755J_U_EN` | User manual | Historical vendor copy | EN | Pending | [BTicino PDF](https://dar.bticino.com/asset/Documents/O1755J_U_EN.pdf) |
| `O1755H_S_EN` | Software manual | Historical vendor copy | EN | Pending | [BTicino PDF](https://dar.bticino.it/asset/Documents/O1755H_S_EN.pdf) |
| F454 firmware version history | Firmware documentation | Historical vendor copy | - | Pending | [Vendor product archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |
| F454 firmware `02.00.51` | Firmware package | Historical vendor copy | - | Pending | [Vendor product archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |

The existence of a vendor firmware package does not establish the firmware installed on any particular F454.

## Identification

The F454 exercises the gateway-specific identity path and is therefore materially different from an ordinary addressed Device.

| Evidence | Value | Status | Source |
| --- | --- | --- | --- |
| `WHO 13 DIMENSION 15.MODEL` | `200` | Observed behavior | [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md#8-worked-case-f454) |
| `WHO 1013 DIMENSION 1.OBJECT_MODEL` | `51` | Observed behavior / catalogue-facing identity | [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md#8-worked-case-f454) |
| Gateway `N_CONF` | `15` | Observed, semantics unresolved | [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md#8-worked-case-f454) |
| `BRAND` | `5` | Observed behavior | [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md#8-worked-case-f454) |
| `LINE` | `0` | Observed behavior | [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md#8-worked-case-f454) |

The complete observed gateway identity frame is:

```text
Client -> Gateway: *#1013**1##
Gateway -> Client: *#1013**1*51*15*5*0##
```

In the Integration Functions catalogue context, `OBJECT_MODEL = 51`, `BRAND = 5`, and `LINE = 0` resolve the observed case to F454.

`WHO 13 DIMENSION 15 = 200` is not a unique Device discriminator: an observed MH202 returns the same functional model code.

## Firmware and hardware

Vendor archives expose F454 firmware `02.00.51` and a version-history document. These establish vendor-supported firmware material, not the firmware installed on every F454.

The Device-specific hardware-version matrix is not yet curated.

## Functional profile

| Function | Role | `WHO` | Notes |
| --- | --- | --- | --- |
| Integration gateway | Gateway / interface | `WHO 13` | Gateway information and integration functions |
| Diagnostic identity | Gateway diagnostics | `WHO 1013` | Catalogue-facing identity layer |
| SCS/TCP bridge | Gateway | Multiple functional systems | Carries OpenWebNet interactions for the plant |

The F454 should not be represented as a normal addressed multi-Module actuator merely because it is a Physical Device in the broader model.

## Diagnostic observations

| Dimension / surface | Observation | Status | Evidence |
| --- | --- | --- | --- |
| `WHO 13 DIMENSION 15` | Returns `200` in the observed F454 | Observed behavior | [Gateway DIMENSION reference](../../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) |
| `WHO 1013 DIMENSION 1` | Returns `51*15*5*0` | Observed behavior | [Gateway identification guide](../../guides/identify-openwebnet-gateway.md#8-worked-case-f454) |
| `WHO 13 DIMENSION 40` | Returns `4*0` in first-hand F454 observation | Observed extension, semantics unknown | [Gateway DIMENSION reference](../../functional/who-13-integration-gateway/dimensions.md#observed-implementation-extension-dimension-40) |

Gateway `N_CONF = 15` must not be interpreted as fifteen physical configurator positions. Its exact gateway semantics remain unresolved.

## Addressing and memberships

Not applicable in the same sense as an addressed actuator Module. Network addressing and installed gateway identity are installation state and are intentionally outside this product definition.

## Configuration

The F454 has a substantial software/network configuration surface documented by its software, installer, and user manuals. A normalized Device-Library configuration model has not yet been curated from those documents.

## Programming

Gateway configuration must remain separate from OpenWebNet Device/Object programming semantics unless a specific programming operation is established.

## Observed behavior

The observed F454 has also served as a gateway for controlled F418U2 experiments. Those observations show gateway-dependent handling of some functional dimmer requests; they are evidence about the F454/F418U2 path and must not be generalized to all target Devices.

## Evidence

- **Published protocol** - classic `WHO 13` defines the historical gateway information surface.
- **Implementation evidence** - MyHOME Suite defines the `WHO 1013` Integration Functions diagnostic identity path and catalogue correlation.
- **Observed behavior** - a first-hand F454 capture establishes `DIMENSION 15 = 200`, the gateway identity tuple `51*15*5*0`, and readable `DIMENSION 40 = 4*0`.
- **Vendor documentation** - product, user, software, installer, firmware, and technical documents establish the marketed F454 product and configuration surface.

## Evidence limits

- `N_CONF = 15` semantics remain unresolved.
- `WHO 13 DIMENSION 40` semantics remain unresolved.
- `DIMENSION 15 = 200` is not unique to F454.
- The complete hardware-revision and firmware-applicability matrix is not yet curated.
- The extensive vendor documentation has been identified but not yet archived under `sources/devices/`.

## Sources

- [Device Sources](../../sources/devices/)
- [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md)
- [Gateway DIMENSION reference](../../functional/who-13-integration-gateway/dimensions.md)
- [DIMENSION 1 Device Identity](../../diagnostics/dim1-device-identity.md)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)

## Related material

- [WHO 13 - Integration Gateway](../../functional/who-13-integration-gateway/)
- [Diagnostics](../../diagnostics/)
- [Open Questions](../../reverse-engineering/open-questions.md#who-13-gateway-properties)
