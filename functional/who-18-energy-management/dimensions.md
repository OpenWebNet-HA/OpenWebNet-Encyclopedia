# `DIMENSION` Reference

`WHO 18` relies heavily on `DIMENSION` operations for instantaneous measurements, accumulated energy, actuator state and control, Stop&Go functions, and historical data. The identifier must always be interpreted together with the `WHO 18` `WHERE` class and its operation-specific parameters.

| `DIMENSION` | Function family |
| ---: | --- |
| `51`–`54` | Energy totalizers and partial totalizers |
| `71`–`73` | Energy-management actuator information/control |
| `113` | Instantaneous active power |
| `250`–`263` | Stop&Go functions |
| `511`–`514` | Historical energy data |

## Active power — `DIMENSION 113`

`DIMENSION 113` is used to read instantaneous active power from supported energy-measurement devices. A typical request follows `*#18*WHERE*113##`. The returned value is a measurement, not an accumulated totalizer, and should be stored separately from the `51`–`54` family.

## Energy totalizers — `DIMENSION 51`–`54`

The totalizer family exposes accumulated energy at different scopes or periods. Some operations are parameterized by a period such as month/day; clients must preserve those parameters because the `DIMENSION` number alone does not identify the requested historical interval.

The MyHOME/OpenWebNet implementation ecosystem uses this family for devices such as F521-class energy meters. Periodic and partial values are therefore part of the same `WHO 18` measurement model but are not interchangeable with instantaneous power.

## Actuator information — `DIMENSION 71`–`73`

The `71`–`73` family represents energy-management actuator information/control. Actuator `WHERE` forms can themselves be parameterized; for example, supported implementations use requests of the form `*#18*7n#0*71##` for actuator information.

Returned payloads are tuples rather than single Boolean states. Consumers must preserve the complete tuple and interpret it according to the specific `DIMENSION` definition instead of reducing the response to an ON/OFF value.

## Stop&Go — `DIMENSION 250`–`263`

The Stop&Go range is a dedicated functional family inside `WHO 18`. Its identifiers represent device state, configuration and control operations associated with Stop&Go devices. These values are not energy measurements despite sharing the Energy Management namespace.

## Historical data — `DIMENSION 511`–`514`

The `511`–`514` family carries historical energy information. Requests can include period-selection parameters. Implementations should model the period and returned measurement as structured data rather than attempting to infer a timestamp solely from the numeric `DIMENSION`.

## Discovery is not implicit

The functional `WHO 18` vocabulary does not establish a general broadcast inventory operation equivalent to Lighting general-status enumeration. Known implementations commonly address energy devices by their `WHO 18` `WHERE` ranges and query supported positions individually. Device discovery/configuration should therefore remain distinct from ordinary energy measurement traffic unless a specific device family defines otherwise.

`WHO 18` is separate from the older [`WHO 3`](../who-3-load-management/) Load Management system. Their `WHAT`, `WHERE`, and `DIMENSION` namespaces must not be merged.