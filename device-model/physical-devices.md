# Physical Devices

A Physical Device is one installed hardware product instance. It is the root of the Device → Module → Object → Configuration hierarchy.

## Identity

This page will document the identifiers and attributes used to recognize a Physical Device, including:

- Device ID and its protocol representation
- catalogue model and product code
- brand and product line
- firmware and hardware identity where established
- diagnostic family and supported management operations

A Device ID identifies the physical instance. A model or product code identifies the product design. These identifiers are not interchangeable.

## Catalogue representation

The catalogue model will distinguish:

- the Device record and its standard MyHOME_Suite-facing description
- the relation between a Device and its item/system definition
- model, brand, and product-line identifiers
- the ordered set of Modules exposed by the Device
- capabilities that apply to the whole Device rather than to one Object

When identifying a scanned Device, the preferred standard description is the Device description resolved from the catalogue. Object descriptions identify individual functions and must not replace the Device description.

## Device classes

Physical form and functional composition are separate properties. The reference will cover at least these recurring compositions:

1. actuator-only Devices
2. dimmer-only Devices
3. command-only Devices
4. combined actuator and independently configurable command Devices
5. actuators with hard-linked local commands

These classes describe hardware composition. They do not assign undocumented meanings to diagnostic identity fields.

## Protocol relationships

Diagnostic discovery identifies the Physical Device before its Modules and Objects are interviewed. Functional OpenWebNet traffic ordinarily addresses configured functions rather than the Device as a catalogue entity.

The exact mapping between Device identity responses, catalogue records, and Module enumeration is documented only where supported by the source data or captured protocol behavior.
