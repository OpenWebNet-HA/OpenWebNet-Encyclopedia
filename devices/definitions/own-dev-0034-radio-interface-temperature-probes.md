# Radio interface for temperature probes

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0034` | Project identity |
| Technical description | Two-channel radio receiving interface for wireless temperature probes | Catalogue + official documentation |
| Catalogue item / model | `39` / `modobj 23` | Implementation evidence |
| Firmware applicability | 239, wildcard -1.-1.-1, two slots | Implementation evidence |
| Commercial identities | HC/HS/HD4577; L/N/NT4577 | Catalogue |
| Categories | Radio interface, Temperature control, Sensor bridge | Capability model |

## Commercial identities

The canonical catalogue groups Axolute HC/HS/HD4577 and Living/Light/Light Tech L/N/NT4577 under technical item 39.

## Documentation

Current BTicino product documentation identifies the 4577 family as the receiving radio interface for wireless temperature probe 3455, powered from the 27 Vdc BUS and occupying two modules. A current English technical sheet is published as MQ00183-c-EN.

## Physical and electrical characteristics

Current publisher data for the Livinglight form gives 27 Vdc supply, 33 mA input current, 868 MHz radio and a two-module flush-mounted enclosure.

## Identity

Catalogue item `39` maps to `modobj = 23`.

## Firmware and hardware

Firmware 239 has wildcard version/revision/build applicability and two Module slots.

## Module, Object, and Virgin Object model

Slots 1 and 2 are both fixed Object 124, Radio interface for sensors (measurer T). This is a two-slot instance of the same temperature-sensor-interface Object.

## Configuration modes

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

Firmware fields are A, PL1/N1, M1, A2/-, PL2/N2, M2 and AID. For each channel, `M` value 0 means not configured, `M` value 1 temperature sensor and `M` value 6 lighting sensor. The reusable Object 124 exposes A, PL_N and M.

## Object configuration surfaces

Each fixed slot uses the temperature-sensor radio-interface Object. The firmware's paired PL/N and M fields distinguish the two configured channels; they must not be flattened into a single probe address.

## Conditions, filters, and conversions

No Object/Firmware filter rows were returned for Object 124 under firmware 239. The unusual `M` value 6 lighting-sensor option is implementation evidence and should remain visible rather than being erased by the product's temperature-oriented commercial name.

## Diagnostic applicability

Use the standard Device identity, firmware, Object, address and configuration diagnostics in [Diagnostics](../../diagnostics/). `DIMENSION 30` is particularly important where one slot has multiple candidate Objects.

## Functional applicability

Thermoregulation is the main catalogue system for the Device; the item is also associated with lighting/automation. The configured channel mode determines whether a slot represents temperature or lighting-sensor use.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Program and validate both channel positions independently. Preserve `M` values 0/1/6 semantics and the dual-system applicability.

## Source reconciliation

Official product documentation corroborates the 4577/3455 radio-temperature role, 27 Vdc BUS supply and two-module form. The database adds two fixed Object slots and explicitly permits `M` value 6 lighting-sensor mode, which broadens the implementation model beyond the product headline.

## Evidence limits and open work

- Archive MQ00183-c-EN and the applicable instruction sheet in the Device source set.
- Hardware-corroborate both slot identities and `M` value 6 behavior.
- Capture representative radio-probe traffic without retaining private installation identifiers.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [https://www.bticino.com/products/bt-l4577](https://www.bticino.com/products/bt-l4577)
- [https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-L4577](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-L4577)
