# Protocol

`WHO 24` defines Lighting Management through a Programmer Gateway. It is distinct from ordinary [`WHO 1`](../who-1-lighting/) Lighting: the namespace models management devices, zones, profiles and control parameters rather than SCS A/PL light points.

## Frame model

`WHO 24` uses the common OpenWebNet frame delimiters but gives `WHERE` a specialized sender/recipient grammar. The target can encode a Lighting Management zone, device type and system address. Sender frames add the `#00#` prefix documented in [`addressing.md`](addressing.md).

`WHAT` operations are parameterized forms rather than a flat scalar table. `DIMENSION` operations carry configuration/state values such as maintained level, timers, stand-by/off values, operating state and centralised lux.

## Read and write operations

Structured values use the normal OpenWebNet `DIMENSION` distinction: reads use `DIMENSION`, while writes use `#DIMENSION`. For example, maintained-level writing follows `*#24*WHERE*#3*Maint_lev##`; a corresponding read uses the non-`#` form.

A client should preserve the value schema of each `DIMENSION`. Lux, level, timers, state and slave-offset values are different domains even though they occupy the same frame position.

## Profiles

The `WHAT 1#PROFILE_ID` family identifies a profile operation. The profile identifier is part of `WHAT` syntax and must not be moved into `WHERE` or treated as a `DIMENSION` value.

## Slave offset

`WHAT 2#[0-1]` controls slave-offset enable/disable behavior, while `DIMENSION 12` carries the slave-offset/GAP value. The enable state and the configured offset are therefore separate protocol properties.

## State and lux

`DIMENSION 17` reports the Lighting Management operating state (Automatic / Manual / Stop). `DIMENSION 18` carries the centralised lux value. These are management-system properties and are not aliases of `WHO 1` dimmer state or level.

See [`what.md`](what.md), [`addressing.md`](addressing.md), and [`dimensions.md`](dimensions.md) for the system-specific grammar.