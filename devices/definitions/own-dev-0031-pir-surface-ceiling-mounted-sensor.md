# PIR surface ceiling-mounted sensor

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0031` | Project identity |
| Technical description | Ceiling-mounted PIR / daylight sensor with stand-alone and scenario-oriented roles | Catalogue + official documentation |
| Catalogue item / model | `33` / `modobj 18` | Implementation evidence |
| Firmware applicability | 130, wildcard -1.-1.-1, one slot | Implementation evidence |
| Commercial identities | BMSE1001; 048833 | Catalogue |
| Categories | Sensor, Presence, Daylight, Lighting | Capability model |

## Commercial identities

The canonical catalogue groups BTicino BMSE1001 and Legrand 048833 under technical item 33.

## Documentation

Official Legrand technical sheet 048833 directly covers BMSE1001 and documents physical and virtual configuration, the ceiling PIR coverage model and the A/PL/M/S/T configurators. The canonical catalogue is broader than the printed physical-configuration table, so discrepancies are retained below instead of normalized away.

## Physical and electrical characteristics

The publisher sheet describes a ceiling-mounted passive infrared detector. At 2.5 m installation height its maximum-sensitivity coverage is approximately 6 m diameter / 28 m². It is intended to combine occupancy and ambient-light information for lighting control.

## Identity

Catalogue item `33` maps to `modobj = 18`.

## Firmware and hardware

Firmware 130 has wildcard version/revision/build applicability and one Module slot.

## Module, Object, and Virgin Object model

Slot 1 has six firmware candidate Objects: 119 Stand alone presence sensor, 164 Scenarios daylight sensor, 165 Scenarios presence sensor, 166 Stand alone daylight sensor, 168 Stand alone daylight and presence sensor, and 128 Scenarios daylight and presence sensor. Catalogue slot metadata marks Object 128 fixed and the other five non-fixed candidates. Shared Virgin Object families 515/516 are associated with these sensor Objects; candidate ordering is not an active-role selection rule.

## Configuration modes

The catalogue declares configuration modes 1, 2 and 3. The official sheet explicitly documents both physical and virtual configuration.

## Firmware-scoped configuration

Firmware fields are A, PL, M, S, T and AID. The database describes M as 0..8, S as 0..4 and T as 0..9. The official 048833 sheet gives physical `A` 1..9, `PL` 1..9, `M` 0..4, `S` 0..3 and `T` 0..9, and explicitly forbids `A` value 0 with `PL` value 0. This is a source-scope tension, not a reason to widen the physical configurator domain.

## Object configuration surfaces

The selected sensor Object determines the larger configuration surface: presence timing and PIR settings, daylight setpoints/regulation, addressing modes, group/reference-actuator fields, or scenario detection settings as applicable.

## Conditions, filters, and conversions

The catalogue attaches many Object/Firmware filters to the sensor candidates, including daylight-group, sensitivity, loop type, functional mode, occupancy, retrigger, alert, detection-schema and daylight-value filters. Consumers must evaluate these filters for the resolved Object rather than flattening all sensor fields into one unconditional form.

## Diagnostic applicability

Use the standard Device identity, firmware, Object, address and configuration diagnostics in [Diagnostics](../../diagnostics/). `DIMENSION 30` is particularly important where one slot has multiple candidate Objects.

## Functional applicability

Depending on resolved Object/configuration, the Device participates in lighting automation as a presence sensor, daylight sensor, combined sensor or scenario-oriented sensor.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Resolve the active slot Object before exposing configuration. Keep the official physical A/PL/M/S/T limits distinct from the wider software/database domains.

## Source reconciliation

Database and official documentation agree on the BMSE1001/048833 ceiling sensor identity and on A/PL/M/S/T as the physical configuration family. The material discrepancy is S: the database domain reaches 4 while the official physical sheet prints 0..3; M is likewise broader in the database than the printed 0..4 physical table. Both scopes are preserved.

## Evidence limits and open work

- Archive the small publisher-original 048833 technical sheet in the Device source set.
- Hardware-corroborate the resolved Object for representative physical and virtual configurations.
- Preserve the S and M domain discrepancy until firmware/runtime evidence establishes the exact software-only cases.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [https://assets.legrand.com/general/legrand-fr/pfat/gm/fiche%20technique%20048833.pdf](https://assets.legrand.com/general/legrand-fr/pfat/gm/fiche%20technique%20048833.pdf)
