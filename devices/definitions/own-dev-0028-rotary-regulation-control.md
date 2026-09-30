# Rotary regulation control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0028` | Project identity |
| Technical description | Flush-mounted rotary SCS control | Catalogue + implementation evidence |
| Catalogue item / model | `25` / `modobj 11` | Implementation evidence |
| Firmware applicability | firmware `213`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `HC/HS/HD4563`, `L/N/NT4563` | Catalogue |
| Categories | Control, Lighting/Automation command | Capability model |

## Commercial identities

The canonical catalogue groups Axolute `HC/HS/HD4563` and Living/Light/Light Tech `L/N/NT4563` under item `25`.

## Documentation

The commercial identity and configuration topology are established from the canonical MyHOME Suite catalogue. The archived system automation material provides family context, but a dedicated publisher technical sheet for the 4563 family has not yet been recovered.

## Identity

Catalogue item `25` maps to Automation `modobj = 11`.

## Firmware and hardware

Firmware `213` is wildcard `-1.-1.-1` with one Module.

## Module, Object, and Virgin Object model

The Module resolves to Object `451`, **Knob control**, a one-slot Object associated with Automation and the relevant command-control collections. No Virgin Object is declared for this firmware.

## Configuration modes

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

The firmware exposes `A`, `PL`, `M`, `LIV1`, `LIV2`, `SPE`, `I` and `AID`. The catalogue describes `M` as command mode with `O/I`, `OFF`, `ON`, `PUL`, `SU_GIU` and `SU_GIU_M` alternatives. `LIV1` and `LIV2` are level configurators; `SPE` selects a special command function; `I` is an additional configurator.

## Object configuration surfaces

Object `451` mirrors the firmware's address, command-mode, level and special-function controls. These fields describe one rotary-control Module, not multiple independent channels.

## Conditions, filters, and conversions

The technical inventory records no Device-specific conditions, filters or conversions.

## Diagnostic applicability

Use standard Device identity, firmware, Object, address and configuration diagnostics.

## Functional applicability

The selected command mode determines the functional command emitted. The dossier therefore does not collapse the Device to a single lighting action without first resolving configuration.

## Observed behavior and corroboration

No sanitized hardware fingerprint or first-hand command trace is currently retained for this exact family.

## Programming

Preserve the complete `M/LIV1/LIV2/SPE/I` configuration rather than translating the rotary control to a simple on/off command.

## Source reconciliation

The database is internally consistent: both commercial identities share firmware `213`, one Knob control Object and the same eight configuration fields. Dedicated publisher documentation remains a discovery gap, so physical interaction details beyond the database model are not inferred.

## Evidence limits and open work

- Locate and archive a publisher-original 4563-family technical sheet.
- Add a sanitized hardware fingerprint and first-hand command traces.
- Establish human-readable semantics for each `LIV1/LIV2/SPE/I` combination.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
