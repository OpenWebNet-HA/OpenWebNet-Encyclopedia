# Overview

The functional protocol reference documents ordinary OpenWebNet systems identified by `WHO`. Each system defines its own `WHAT` values, `WHERE` grammar, `DIMENSION` identifiers, parameters, and operation-specific behavior.

Common frame syntax is defined in [`../protocol/`](../protocol/). This section documents the semantics carried by those frames for each functional system.

## Systems

| System | `WHO` | Reference |
| --- | ---: | --- |
| Scenarios | `0` | [`scenarios/`](scenarios/) |
| Lighting | `1` | [`lighting/`](lighting/) |
| Automation | `2` | [`automation/`](automation/) |
| Load Management | `3` | [`load-management/`](load-management/) |
| Temperature Control | `4` | [`temperature-control/`](temperature-control/) |
| Alarms | `5` | [`alarms/`](alarms/) |
| Video Door Entry | `6`, `7`, `8` | [`video-door-entry/`](video-door-entry/) |
| Auxiliaries | `9` | [`auxiliaries/`](auxiliaries/) |
| CEN and CEN+ | `15`, `25` | [`cen/`](cen/) |
| Sound System | `16`, `22` | [`sound-system/`](sound-system/) |
| Energy Management | `18` | [`energy-management/`](energy-management/) |
| Access Control | `23` | [`access-control/`](access-control/) |

Additional functional systems will be added when their reference material is developed.

## Scope

`WHAT` and `DIMENSION` identifiers are documented within the system that defines them. `WHERE` is likewise interpreted according to the selected `WHO`; it is not a universal address type.

Diagnostic and configuration/programming operations are documented separately under `diagnostics/` and `programming/`.