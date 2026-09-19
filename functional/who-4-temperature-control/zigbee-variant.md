# ZigBee Variant

The ZigBee OpenWebNet version 4.0 specification defines a deliberately narrow `WHO 4` Temperature Control surface for the Legrand serial ZigBee interface. In the inspected section, `WHO 4` is used to receive temperature reports from a ZigBee probe. It does not define the broad SCS zone, central-unit, actuator, setpoint, program, or split-control model documented elsewhere in this namespace.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**.

## Documented surface

The ZigBee `WHO 4` section contains no `WHAT` entries. Its `DIMENSION` table defines only:

| `DIMENSION` | ZigBee specification meaning | Direction established by the section |
| ---: | --- | --- |
| `0` | Temperature level | server to client |

The report form is:

`*#4*WHERE#9*0*LEVEL##`

`WHERE` uses the [ZigBee product-and-Unit address family](../../protocol/zigbee-interface.md#transport-and-addressing), not the SCS Temperature Control zone/probe grammar.

The section defines no `WHO 4` request frame for this value. A client-side measured-temperature request such as the one documented for SCS must therefore not be inferred for this ZigBee interface from the shared `DIMENSION 0` identifier.

## Temperature encoding

`LEVEL` is four digits `C1C2C3C4`:

| Field | Meaning |
| --- | --- |
| `C1` | sign: `0` positive, `1` negative |
| `C2C3` | whole-temperature tens and units |
| `C4` | decimal digit in 0.1 °C steps |

The source examples demonstrate both positive and negative values. It does not state a complete valid temperature range beyond this field structure, so the encyclopedia does not infer one from the number of available digits.

This encoding is materially different from the SCS-oriented `DIMENSION 0` representation documented in [`DIMENSION` Reference](dimensions.md). The two payloads must be selected by interface variant rather than decoded through one shared temperature rule.

## Prior procedure

The source states that the probe must previously have completed a source-named "PnL" procedure with the OpenWebNet interface and points to the `WHO 25` use cases.

This establishes a prerequisite in the source's ZigBee workflow but does not establish the underlying ZigBee radio procedure as OpenWebNet. See [ZigBee Binding](../who-25-transversal/zigbee-binding.md) for the OpenWebNet-visible `WHO 25` lifecycle.

## Evidence limits

The absence of other `WHAT` and `DIMENSION` values from this ZigBee section means that version 4.0 does not establish them for this interface. It is not a universal statement that no ZigBee Temperature Control implementation can expose additional OpenWebNet operations.

In particular, the SCS central-unit modes, zone commands, `DIMENSION 11..31`, actuator addressing, and split-control operations must not be transferred to this variant by namespace equality.

See [Temperature Control](README.md) for the broader SCS-oriented namespace and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport and addressing.
