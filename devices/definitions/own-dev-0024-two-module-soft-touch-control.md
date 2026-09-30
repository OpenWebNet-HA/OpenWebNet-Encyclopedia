# Two-module Soft Touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0024` | Project identity |
| Technical description | Two-module capacitive Soft Touch SCS command with configurable function and UI settings | Catalogue + official documentation |
| Catalogue item / model | `12` / `modobj 8` | Implementation evidence |
| Firmware applicability | firmware `149`, `-1.-1.-1`, two slots | Implementation evidence |
| Commercial identities | `HC/HS4653/2`, `HD4653M2` | Catalogue |
| Categories | Command, Lighting, Automation, Scenario, Sound, Access | Capability model |

## Commercial identities

`HC4653/2`, `HS4653/2`, and `HD4653M2` belong to the shared item. Direct documentation is strongest for the HC/HS family; HD remains a direct-documentation follow-up.

## Documentation

The archived official MyHOME automation guide and Legrand automation catalogue cover Soft Touch operation and functions. Historical product documentation states that two- and three-module Soft Touch variants differ mechanically while sharing configuration and operating methods.

## Physical and electrical characteristics

Published data gives SCS nominal `27 Vdc`, operating `18..27 Vdc`, maximum consumption `18 mA`, operating temperature `5..35 °C`, and a two-module flush-mounted form for HC/HS4653/2. LED intensity is adjustable.

## Identity

Catalogue item `12` maps to Automation `modobj = 8`.

## Firmware and hardware

Firmware `149` is wildcard `-1.-1.-1` and declares two slots.

## Module, Object, and Virgin Object model

Slot `1` is the configurable command surface. Direct candidates are Objects `410`, `411`, `412`, `413`, `414`, `415`, `416`, `418`, `419`, `426`, and `427`. Virgin Object `521`, Soft-Touch command virgin, additionally permits AUX `417`, cyclic autoswitch `421`, and Open-lock-on-session `462`. Slot `2` is fixed Object `130`, User interface settings. It is not a second command channel.

## Configuration modes

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

`A` supports `0..9`, `GEN`, `GR`, `AMB`, `AUX`; `PL` is `0..9`; `M` supports `0..9`, `OFF`, `ON`, `CEN`, `PUL`; `M2` is `0..9`; `SPE` supports default and `0,1,2,3,4,6,7,8,9`; `INT` supports default, `0`, `1`, `OFF`; `AID` is the identity field.

## Object configuration surfaces

The active slot-1 Object determines the functional configuration surface. Object `130` carries UI settings and must remain separate from the command Object.

## Conditions, filters, and conversions

No slot-condition or conversion rows are recorded for firmware `149`; function selection is represented by configuration and the Virgin Object.

## Diagnostic applicability

Use `DIMENSION 30` to distinguish the active command Object from fixed UI Object `130`; `DIMENSION 1`, `2`, `32`, and `35` provide identity, firmware, address and configuration.

## Functional applicability

Depending on configuration, the control participates in lighting, automation, scenarios, sound diffusion and access/door-entry command functions.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Treat the Device as one configurable command surface plus one UI-settings Module, not two independent commands.

## Source reconciliation

Official documentation establishes touch operation, adjustable LED intensity, actuator/scenario use and sound-system ON/OFF/volume use. The database expands the same command surface to the full Virgin-Object candidate set and explicitly separates UI settings into slot `2`.

## Evidence limits and open work

- Archive a dedicated Soft Touch technical sheet with explicit `HD4653M2` coverage.
- Publish the exact physical `M/M2/SPE/INT` function matrix.
- Hardware-corroborate active Object and UI-settings behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
