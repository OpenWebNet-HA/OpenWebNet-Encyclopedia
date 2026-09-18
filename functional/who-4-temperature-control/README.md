# `WHO 4` — Temperature Control

`WHO 4` defines the OpenWebNet Temperature Control system. It covers zones and probes, central-unit operating modes, measured and target temperatures, local offsets, fan-coil speed, valve and actuator state, holiday operation, and split-unit control.

Unlike Lighting and Automation, Temperature Control uses a zone/probe-oriented `WHERE` grammar. Functional traffic can address master probes, all probes in a zone, individual slave probes, the central unit, zones through the central unit, and actuator instances.

The published OpenWebNet specification defines the functional state and command model. The MyHOME_Suite `OPEN.db` definitions complement it with implemented address rules and command templates, while the MyHOME_Suite catalogue and rule data describe the configuration capabilities of physical Temperature Control Objects. Diagnostic traffic uses the separate diagnostic namespace `WHO 1004` and is documented under [`../../diagnostics/`](../../diagnostics/).

## Reference

| Subject | Page |
| --- | --- |
| Operating modes and commands | [`what.md`](what.md) |
| Zones, probes, central unit and actuator `WHERE` forms | [`addressing.md`](addressing.md) |
| Temperature, status and control `DIMENSION` operations | [`dimensions.md`](dimensions.md) |

## Temperature representation

Temperature values are encoded as fixed-width decimal fields whose resolution depends on the operation. Measured/status temperatures commonly use 0.1 °C resolution, while setpoint-writing operations use the range and step defined by that operation. The frame definition must therefore determine how a temperature field is decoded; temperature-looking values are not globally interchangeable.

See [`../../protocol/`](../../protocol/) for common OpenWebNet frame classes and [`../../device-model/`](../../device-model/) for the Device → Module → Object → Configuration model.