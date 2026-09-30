# Flush-mounted radio receiver for batteryless control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0035` | Project identity |
| Technical description | Four-slot SCS radio receiver for batteryless flat controls | Catalogue + official documentation |
| Catalogue item / model | `40` / `modobj 19` | Implementation evidence |
| Firmware applicability | 218, wildcard -1.-1.-1, four slots | Implementation evidence |
| Commercial identities | HC/HS/HD4575SB; L/N/NT4575SB | Catalogue |
| Categories | Radio interface, Lighting control, Automation control, Scenario control | Capability model |

## Commercial identities

The canonical catalogue groups Axolute HC/HS/HD4575SB and Living/Light/Light Tech L/N/NT4575SB under technical item 40.

## Documentation

The already archived official MyHOME Automation guide identifies the 4575SB family as the radio receiving interface for batteryless flat controls such as HA/HB4572SB or L4572SB, supplied from the 27 Vdc BUS and occupying two wiring-device modules.

## Physical and electrical characteristics

Official automation documentation describes a 27 Vdc BUS-powered two-module receiver. Historical technical material specifies 868 MHz radio operation; exact range and current figures remain source-revision scoped.

## Identity

Catalogue item `40` maps to `modobj = 19`.

## Firmware and hardware

Firmware 218 has wildcard version/revision/build applicability and four Module slots.

## Module, Object, and Virgin Object model

Object 400 Light control is fixed on slots 1,2,3,4. Object 403 Scenario module control is a non-fixed candidate on all four slots. Object 401 Automation control is a non-fixed candidate on slots 1 and 3. Shared Virgin Object families 500/501/502 cover the corresponding Light, Automation and Scenario control Objects.

## Configuration modes

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

Firmware fields are A, PL1, M1, PL2, M2, SPE and AID. M1/M2 accept 0..8 plus O/I, OFF, ON, SU_GIU, SU_GIU_M, CEN and PUL; SPE accepts 0,1,6.

## Object configuration surfaces

The resolved Object determines whether a radio control surface acts as Lighting control, Automation control or Scenario module control. The four firmware slots do not imply four identical user controls without Object resolution.

## Conditions, filters, and conversions

The Scenario module relation carries an Installation level filter. The Light/Automation/Scenario Objects also have their own conditional fields and shared Virgin-object reachability; resolve topology before exposing those surfaces.

## Diagnostic applicability

Use the standard Device identity, firmware, Object, address and configuration diagnostics in [Diagnostics](../../diagnostics/). `DIMENSION 30` is particularly important where one slot has multiple candidate Objects.

## Functional applicability

Depending on Object and mode, the receiver can expose lighting, automation and scenario-control functions from paired batteryless radio controls.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Preserve slot-by-slot Object selection and the complete M/SPE mode set. Do not model the receiver as a single generic pushbutton or as four unconditional Light controls.

## Source reconciliation

Publisher documentation establishes the 4575SB batteryless-radio receiver family and SCS BUS role. The canonical database explains its richer software topology: four fixed Light-control slot positions with optional Automation and Scenario Objects, plus the firmware-level PL/M/SPE configuration.

## Evidence limits and open work

- Add sanitized pairing and button-action captures for representative 4572SB controls.
- Corroborate optional Automation/Scenario Object resolution by DIM30 on hardware.
- Document the Installation level filter for Scenario module control in human-readable form.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf)
