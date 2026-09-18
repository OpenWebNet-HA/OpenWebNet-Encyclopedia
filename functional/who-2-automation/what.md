# `WHAT` Reference

`WHAT` in `WHO 2` expresses Automation movement commands. The published specification distinguishes base motor commands, advanced parameterized commands, and translated event reports.

## Base commands

| `WHAT` | Function | Frame |
| ---: | --- | --- |
| `0` | Stop | `*2*0*WHERE##` |
| `1` | Up | `*2*1*WHERE##` |
| `2` | Down | `*2*2*WHERE##` |

Collective commands can expand into events for the addressed scope and the individual affected Objects. Up/Down movement normally produces a later Stop event when the endpoint is reached.

## Advanced commands

| Leading `WHAT` | Function | Parameters |
| ---: | --- | --- |
| `10` | Advanced Stop | priority; set/clear selector |
| `11` | Advanced Up | optional step; priority; set/clear selector |
| `12` | Advanced Down | optional step; priority; set/clear selector |

The exact `#`-parameterized form is part of `WHAT`; parsing only the leading number loses the requested step and priority operation.

### Step

`1`–`99` requests the corresponding relative movement. An omitted/null value or `100` means movement to the endpoint for the selected direction.

### Priority

The priority payload contains a set/clear selector and Safety, High, and Medium flags. A zero flag leaves that priority unchanged. This is a bit-selection operation, not a single ordinal priority number.

## Command-translation reports - `WHAT 1000`

The published Automation flows use `1000#INNER_WHAT...` when reporting translated commands for point targets. Base operations can appear as:

~~~text
*2*1000#INNER_WHAT*WHERE##
~~~

Advanced reports preserve their parameters, for example the inner operation, priority, set/clear selector, and target `WHERE`. Some tables in the source omit `WHERE` in individual rows while later rows include it; parsers should accept only forms corroborated by the actual gateway/device family and preserve the raw frame when the source is inconsistent.

Do not mistake `1000` for a movement state. It is a wrapper around another Automation operation.

## State values are not commands

Values `10`–`14` also appear as `DIMENSION 10` shutter-state values: Stop, Up, Down, step-by-step Up, and step-by-step Down. That value table is local to the `DIMENSION` payload. In particular, `13` and `14` are not established ordinary command `WHAT` values.

## Evidence basis

The command table, step and priority model, collective event behavior, and translation frames come from [WHO 2 specification](../../sources/openwebnet-public/pdf/WHO_2.pdf). MyHOME Suite ScenarioDevices corroborates ordinary movement and absolute-position capability but does not redefine the published wire grammar.

See [`DIMENSION` Reference](dimensions.md), [Addressing](addressing.md), and the common [`WHAT` model](../../protocol/what.md).
