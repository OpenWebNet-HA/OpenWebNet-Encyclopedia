# `DIMENSION` Reference

`WHO 24` uses `DIMENSION` operations for Lighting Management configuration and runtime state. Reads use the ordinary `DIMENSION` form; writable properties use `#DIMENSION`.

| `DIMENSION` | Meaning | Value domain |
| ---: | --- | --- |
| `1` | Switch ON | Switching configuration |
| `2` | Maximum lux | Illuminance threshold |
| `3` | Maintained level | Maintained lighting level |
| `4` | Automatic switch ON | Automatic-on configuration |
| `5` | Switch ON delay | Time/delay |
| `6` | Automatic switch OFF | Automatic-off configuration |
| `7` | Switch OFF delay | Time/delay |
| `8` | Delay timer | Time/delay |
| `9` | Stand-by timer | Time/delay |
| `10` | Stand-by value | Stand-by level/value |
| `11` | OFF value | Off-state level/value |
| `12` | Slave offset (GAP) value | Slave offset |
| `17` | State | Automatic / Manual / Stop |
| `18` | Centralised lux value | Illuminance |

## Maintained level

The published write form is `*#24*WHERE*#3*Maint_lev##`. `Maint_lev` is the value associated specifically with `DIMENSION 3`; it should not be normalized as a `WHO 1` dimmer command.

## Timers and delays

`DIMENSION 5`, `7`, `8`, and `9` represent distinct timing properties: switch-on delay, switch-off delay, general delay timer, and stand-by timer. Their similar data type does not make them interchangeable.

## Stand-by and OFF values

`DIMENSION 10` and `11` configure values associated with stand-by and OFF behavior. They are separate from the enable/disable decisions represented by the automatic switching dimensions.

## Slave offset

`DIMENSION 12` carries the slave-offset/GAP value. Whether slave offset is enabled is controlled separately through parameterized `WHAT 2#[0-1]`; implementations should store both properties.

## Runtime state

`DIMENSION 17` is an enumerated operating-state value: Automatic, Manual, or Stop. `DIMENSION 18` carries centralised lux. These runtime values should remain distinct from configuration thresholds such as maximum lux (`DIMENSION 2`).

Capability support is device-specific. The namespace-level table defines available operations but does not imply that every Lighting Management endpoint accepts every write.