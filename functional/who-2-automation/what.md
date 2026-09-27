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

`1..99` requests the corresponding relative movement. An omitted/null value or `100` means movement to the endpoint for the selected direction.

### Priority

The priority payload contains a set/clear selector and Safety, High, and Medium flags. A zero flag leaves that priority unchanged. This is a bit-selection operation, not a single ordinal priority number.

### Parameter format

The published [`WHO 2` specification](../../sources/openwebnet-public/pdf/WHO_2.pdf) defines separate parameter structures for command sessions and event sessions:

**Published command session grammar** (client to server):
~~~text
*2*10#PRIORITY*WHERE##                 (Advanced Stop)
*2*11#STEP#PRIORITY*WHERE##            (Advanced Up)
*2*12#STEP#PRIORITY*WHERE##            (Advanced Down)
~~~

Where:
- `STEP`: `1..99` specifies a relative step percentage; `100` (or omitted/null) requests movement to the physical endpoint (full open or full close).
- `PRIORITY`: 3-digit bitfield (`p1 p2 p3`) representing Safety (`p1`), High (`p2`), and Medium (`p3`) priority levels (for example, `001` sets standard medium priority).

**Published event session grammar** (server to client):
In event sessions and status reports, the server appends a selector flag (`<shutterType>`):
~~~text
*2*10#PRIORITY#SELECTOR*WHERE##        (Advanced Stop event)
*2*11#STEP#PRIORITY#SELECTOR*WHERE##   (Advanced Up event)
*2*12#STEP#PRIORITY#SELECTOR*WHERE##   (Advanced Down event)
~~~

Where `SELECTOR`:
- `0`: Clear priority.
- `1`: Set priority.

Command-translation reports (`WHAT 1000`) for point targets wrap this event structure: `*2*1000#11#PRIORITY#SELECTOR*WHERE##`.

**Observed physical transmitter frames**:
Physical centralized transmitters broadcasting to the General scope (`WHERE = 0`) emit the event-style multi-parameter form with `SELECTOR = 1` (Set priority) directly onto the SCS bus:
- Up: `*2*11#100#001#1*0##`
- Down: `*2*12#100#001#1*0##`
- Stop: `*2*10#001#1*0##`

This on-wire behavior is corroborated by authentic bus monitor traces captured on a physical MyHomeServer1 gateway with an `LN4660M2` centralized controller ([public MyHomeServer1/LN4660M2 traces](https://github.com/OpenWebNet-HA/MyHOME/tree/198a848e73edd2a887b993b98beffa98f3f20e36/tests/fixtures/traces/issue_445), contributed by Francesco Montorsi on [MyHOME issue #445](https://github.com/OpenWebNet-HA/MyHOME/issues/445) and [#466 (comment 5853591733)](https://github.com/OpenWebNet-HA/MyHOME/issues/466#issuecomment-5853591733)).

### Physical transmitter STOP / PRESET behavior

Advanced physical shutter controls (such as `LN4660M2`, `H4660M2`, `AM5860M2`) feature a dual-function middle button:
- When shutters are **in motion**: pressing the button emits the Advanced Stop command (`*2*10#001#1*WHERE##`), stopping movement immediately across the addressed scope.
- When shutters are **stationary**: pressing the button triggers the **PRESET** function, recalling a pre-configured intermediate position stored within the actuators.

## Command-translation reports - `WHAT 1000`

The published Automation flows use `1000#INNER_WHAT...` when reporting translated commands for point targets. Base operations can appear as:

~~~text
*2*1000#INNER_WHAT*WHERE##
~~~

Advanced reports preserve their parameters, for example the inner operation, priority, set/clear selector, and target `WHERE`. Some tables in the source omit `WHERE` in individual rows while later rows include it; parsers should accept only forms corroborated by the actual gateway/device family and preserve the raw frame when the source is inconsistent.

Do not mistake `1000` for a movement state. It is a wrapper around another Automation operation.

## State values are not commands

Values `10..14` also appear as `DIMENSION 10` shutter-state values: Stop, Up, Down, step-by-step Up, and step-by-step Down. That value table is local to the `DIMENSION` payload. In particular, `13` and `14` are not established ordinary command `WHAT` values.

## Evidence basis

The command table, step and priority model, collective event behavior, and translation frames come from [`WHO 2` specification](../../sources/openwebnet-public/pdf/WHO_2.pdf). MyHOME Suite ScenarioDevices corroborates ordinary movement and absolute-position capability but does not redefine the published wire grammar.

See [`DIMENSION` Reference](dimensions.md), [Addressing](addressing.md), and the common [`WHAT` model](../../protocol/what.md).
