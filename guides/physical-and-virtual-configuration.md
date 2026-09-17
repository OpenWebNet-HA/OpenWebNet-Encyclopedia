# Physical and Virtual Configuration

## Goal

Determine whether a property or value can be represented with physical configurators, through MyHOME_Suite Virtual configuration, or both.

## Terminology

- **Physical configuration** uses configurators or jumpers on the Device.
- **Virtual configuration** covers configuration performed through MyHOME_Suite.
- **Virtual-configurator transfer** writes the software projection associated with `DIMENSION 4` and `5`.
- **Advanced Object programming** writes Objects, addresses, and indexed properties through `DIMENSION 30`, `32`, and `35`.

Advanced and Virtual are not opposites; advanced programming is a Virtual configuration mechanism.

## Procedure

1. Resolve the Device and firmware.
2. Confirm supported modes through `AS_FIRMWARE_CONFIG_MODE` and `EN_CONFIG_MODE`.
3. Enumerate firmware-scoped physical fields, normally `idx = -1`, excluding `AID`.
4. Resolve the effective address or indexed property.
5. Compare symbols, semantic types, domains, filters, symbol references, conversion rules, and `EN_PHY_TO_ADV_TRANS`.
6. Use product documentation or captures where symbols differ.
7. Establish physical and Virtual value domains independently.

## Classification

| Result | Meaning |
| --- | --- |
| direct counterpart | symbol and semantics match |
| mapped counterpart | corroborated mapping between different symbols |
| physically representable | value is inside the established physical domain |
| Virtual-only value | the property has a counterpart but this value exceeds its physical domain |
| Virtual-only property | no physical counterpart resolves |
| unresolved | evidence is insufficient |

A compatible value does not reveal which method produced the installed state. Diagnostic frames report effective configuration.

See [Physical-configurator counterparts](../device-model/configuration.md#physical-configurator-counterparts).
