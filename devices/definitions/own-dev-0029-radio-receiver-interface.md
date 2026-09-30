# Radio receiver interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0029` | Project identity |
| Technical description | Flush-mounted 868 MHz radio-to-SCS receiving interface | Catalogue + official technical documentation |
| Catalogue item / model | `28` / `modobj 20` | Implementation evidence |
| Firmware applicability | firmware `214`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `HC/HS/HD4575`, `L/N/NT4575`, `L/N/NT4575N` | Catalogue |
| Categories | Radio interface, Control bridge | Capability model |

## Commercial identities

The canonical catalogue groups the Axolute and Living/Light/Light Tech 4575 receiver references under technical item `28`.

## Documentation

An official Legrand/BTicino technical guide for the radio-wired interface is archived in Device Sources. It explicitly covers `HC/HS4575` and `L/N/NT4575N`; the catalogue additionally groups `HD4575` and `L/N/NT4575` with the same technical item.

## Physical and electrical characteristics

The official guide specifies 27 Vdc BUS supply, 868 MHz reception, 2 mA consumption for `L/N/NT4575N` and `HC/HS4575`, two wiring-device modules, and +5 °C to +35 °C operating temperature. It identifies a status LED, programming micro-button, physical configurator positions and the SCS BUS connector.

## Identity

Catalogue item `28` maps to Automation `modobj = 20`.

## Firmware and hardware

Firmware `214` is wildcard `-1.-1.-1` and declares one Module.

## Module, Object, and Virgin Object model

The single Module resolves to Object `27`, **Radio receiver**. No Virgin Object is declared for this firmware.

## Configuration modes

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

The firmware exposes `A`, `PL`, `M` and `AID`. Its `M` description permits `0`, `1`, `6`, `7`, `8` and `CEN`. The reusable Object uses the corresponding `MOD` concept.

## Object configuration surfaces

Object `27` represents the radio receiver as one SCS endpoint. Radio transmitters paired to it are not additional Device Modules in this catalogue model.

## Conditions, filters, and conversions

The technical inventory records no Device-specific conditions, filters or conversions.

## Diagnostic applicability

Use standard Device identity, firmware, Object, address and configuration diagnostics.

## Functional applicability

The official documentation shows that the receiver can translate radio controls into SCS functions. A sound-system guide specifically documents amplifier on/off, volume, source selection and radio-station/track changes when appropriately configured. Other configured modes must be interpreted from their own functional context.

## Observed behavior and corroboration

No sanitized first-hand capture for this exact receiver is currently retained.

## Programming

Preserve the configured `M/MOD` role, including `CEN`, rather than assuming all received radio commands are ordinary lighting commands.

## Source reconciliation

The canonical database and publisher technical guide agree on a one-Module radio receiver with physical configurators and SCS BUS connection. The official guide directly covers two of the catalogue's reference forms; the remaining grouped references are catalogue-correlated and should not be represented as separately documented variants.

## Evidence limits and open work

- Add sanitized hardware and pairing traces.
- Recover dedicated documentation for the catalogue-only `HD4575` and `L/N/NT4575` forms if distinct publisher sheets exist.
- Map each `M/MOD` value to verified emitted OpenWebNet behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
