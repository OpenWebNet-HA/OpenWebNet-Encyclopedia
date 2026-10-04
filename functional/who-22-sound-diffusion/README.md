# `WHO 22` - Sound Diffusion

`WHO 22` is the later Sound Diffusion / Multimedia dialect. It uses structured source, speaker, area, and general addresses, with operation parameters embedded in `WHAT`.

## Core parameters

| Parameter | Published domain |
| --- | --- |
| Multimedia type | `1` voice; `2` right; `3` left; `4` stereo; `11` all sources |
| Source ID | `1..4` |
| Area / speaker point | `1..9` |
| Device state | `0` OFF; `1` ON |
| Frequency step | `1..15` |
| Modulation | `1` FM; `2` AM-LW; `3` AM-MW; `4` AM-SW |
| Stored station | `1..5` for F500; `1..15` for F500N |
| Track | `1..999` |
| Volume / volume step | absolute `0..31`; step `1..31` |
| Tone / balance value | `1..63` |
| 3D level | `0..10` |
| Loudness | `0` OFF; `1` ON |
| Preset | `2` normal, `3` dance, `4` pop, `5` rock, `6` classic, `7` techno, `8` party, `9` soft, `10` full bass, `11` full treble; `16..25` user defined |

The source describes frequency steps as `50`, `100`, … `750 Hz`; this appears unusually small for radio tuning. This reference preserves the published values without silently relabelling their unit.

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `0` / `1` | Turn source or speaker OFF / ON |
| `2` | Source turned on |
| `3` / `4` | Increase / decrease volume |
| `5` / `6` | Search/tune toward higher / lower frequencies |
| `9` / `10` | Next / previous station |
| `11` / `12` | Next / previous track |
| `22` | Sliding request |
| `31` / `32` | Start / stop RDS message reporting |
| `33` | Store tuned frequency as a station |
| `34` | Turn amplifier ON using Follow Me |
| `35` | Turn amplifier ON using a specified source |
| `36` / `37` | Increment / decrement low tones |
| `38` / `39` | Increment / decrement mid tones |
| `40` / `41` | Increment / decrement high tones |
| `42` / `43` | Move balance right / left |
| `55` / `56` | Next / previous preset |

Most commands are parameterized. For example, source power uses `WHAT#MULTIMEDIA_TYPE#AREA`, while the target source remains in `WHERE`. A decoder must retain the entire `WHAT` field.

### Frequency search

For `WHAT 5` and `6`, an empty step parameter requests automatic search; a supplied frequency-step value requests movement by that step. The flat `WHAT` table's wording for `6` is therefore incomplete by itself; the allowed-message flow establishes both modes.

## `WHERE`

| Target | `WHERE` form |
| --- | --- |
| Source | `2#SOURCE_ID` |
| Speaker | `3#AREA#POINT` |
| Speaker area | `4#AREA` |
| General | `5#SENDER_ADDRESS` |
| All sources | `6` |

These are tagged target classes, not decimal numbers with punctuation. Keep the structure intact.

## `DIMENSION`

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Volume |
| `2` | High tones |
| `3` | Medium tones |
| `4` | Low tones |
| `5` | Frequency |
| `6` | Track/station |
| `7` | Play status |
| `11` | Frequency and station |
| `12` | Device state |
| `17` | Balance |
| `18` | 3D |
| `19` | Preset |
| `20` | Loudness |

Absolute `DIMENSION` state complements relative `WHAT` operations. Prefer reported values for state caches instead of reconstructing state from increments.

### Payloads and concrete operations

| Dimension | Report payload following the dimension |
| --- | --- |
| `1` | `VOLUME` |
| `2`, `3`, `4` | `TONE_VALUE` |
| `5` | `MODULATION*FREQUENCY` |
| `6` | `STATION_OR_TRACK` |
| `11` | `MODULATION*FREQUENCY*STATION_OR_TRACK` |
| `12` | `DEVICE_STATE*MULTIMEDIA_TYPE` |
| `17` | `BALANCE` |
| `18` | `3D_LEVEL` |
| `19` | `PRESET` |
| `20` | `LOUDNESS` |

The detailed flows additionally show RDS text under dimension `10` and equalizer reports under `21#1`, `21#2`, and `21#3`. The equalizer selectors carry bands `1..3`, `4..6`, and `7..8` respectively, separated by `*`. The published source does not supply a complete RDS text encoding or band-value domain; the historical RDS decoding evidence below establishes a narrower implementation format.

Examples with unambiguous separators in the detailed flows include:

| Operation | Frame |
| --- | --- |
| Increase speaker volume | `*22*3#VOLUME_STEP*3#AREA#POINT##` |
| Decrease speaker volume | `*22*4#VOLUME_STEP*3#AREA#POINT##` |
| Follow Me | `*22*34#MULTIMEDIA_TYPE#AREA*3#AREA#POINT##` |
| Select source and turn on speaker | `*22*35#4#AREA#SOURCE_ID*3#AREA#POINT##` |
| Store tuned station | `*22*33#STATION*2#SOURCE_ID##` |
| Request source frequency | `*#22*5#2#SOURCE_ID*5##` |
| Request speaker volume | `*#22*3#AREA#POINT*1##` |
| Set speaker balance | `*#22*3#AREA#POINT*#17*BALANCE##` |
| Set speaker preset | `*#22*3#AREA#POINT*#19*PRESET##` |
| Set speaker loudness | `*#22*3#AREA#POINT*#20*LOUDNESS##` |

Source dimension requests use the general-source form `5#2#SOURCE_ID` in these flows; some responses instead use `2#SOURCE_ID`. Retain the reported address rather than requiring textual equality with the request. Status requests receive an action-session ACK while the specified state reports appear on the event session; dimension reads have their own response flows.

### Published inconsistencies

The detailed specification is not uniformly reliable as a copy-and-send frame catalogue. Speaker power examples omit separators that appear in the address table; speaker writes for dimensions `1..4` join the dimension marker to `WHERE` without the normal `*`; preset commands `55`/`56` contain an early `##`; and some tone-response dimension numbers disagree with the requested tone. RDS commands `31`/`32` are printed without a normal `WHERE` field. The source also shows `WHAT 21` source notifications outside its summary table.

Preserve these as source discrepancies. The tested forms below resolve speaker volume writes, preset commands, power-control emissions, and RDS syntax for the historical touchscreen implementation. Other tone-response discrepancies and the meaning of the published `WHAT 21` notification remain unresolved. Occasional trailing empty fields in volume reports should be preserved by the parser. The compact tables above do not assert support for every read/write combination.

## Historical touchscreen syntax and extensions

Exact BTicino tests at `TS10_1_0_23` resolve several malformed published examples for that implementation:

| Operation | Tested emission |
| --- | --- |
| Speaker OFF | `*22*0#4#AREA*3#AREA#POINT##` |
| Speaker ON using Follow Me | `*22*34#4#AREA*3#AREA#POINT##` |
| Absolute volume | `*#22*3#AREA#POINT*#1*VOLUME##` |
| Next / previous preset | `*22*55*3#AREA#POINT##` / `*22*56*3#AREA#POINT##` |
| RDS start / stop | `*22*31*2#SOURCE##` / `*22*32*2#SOURCE##` |
| Automatic tuning up / down | `*22*5*2#SOURCE##` / `*22*6*2#SOURCE##` |
| Manual tuning up / down | `*22*5#STEP*2#SOURCE##` / `*22*6#STEP*2#SOURCE##` |
| Select source for one area | `*22*35#4#AREA#SOURCE*3#AREA#0##` |
| Select stored station | `*#22*2#SOURCE*#6*STATION##` |
| Virtual amplifier state report | `*#22*5#3#AREA#POINT*12*STATE*3##` |
| Virtual amplifier volume report | `*#22*5#3#AREA#POINT*1*VOLUME##` |

The application maps amplifier-area configuration `#A` to `WHERE = 4#A`, and general amplifier configuration `0` to `5#3#0#0`. Tests also recognize `*22*0#4#15*5#1#1##` as a special general-OFF notification. That recognition does not establish an arbitrary sender-address domain.

The virtual amplifier publishes its own cached state and volume in the two report forms above, including during initialization with OFF and volume `0`. Its volume controls generate local requests; they do not by themselves confirm playback or a physical amplifier's state. Area/general controllers containing that virtual amplifier dispatch power and relative-volume operations to both the bus and the local amplifier.

The radio client interprets its cached frequency in hundredths of MHz: `9800` is 98.00 MHz, and a manual step changes it by `5` (50 kHz). It wraps above 108.00 MHz to 87.50 MHz and below 87.50 MHz to 108.00 MHz. With an unknown cached frequency, manual tuning sends nothing; automatic search still sends `WHAT 5` / `6`. BtExperience schedules a frequency read after manual tuning and waits for a report after automatic search. These are client policies; they do not resolve the published step-unit discrepancy or establish every tuner's band limits.

### Source activity and RDS

The library requests active areas with `*#22*2#SOURCE*13##`. A tested response at `5#2#SOURCE` carries sixteen flags for area indices `0..15`, replacing that source's cached area set; its matching `WHAT 2#4#AREA` notifications add an active area. An OFF state report clears the set. Selecting another source for a cached area removes that area from the previous source. In monochannel mode its `WHAT 2` notifications use area `0`. BtExperience exposes only indices `0..8` and emits an activity change when its area set crosses between empty and nonempty. These are internal state-model choices, not revised published area domains.

The tested source-selection method with no area supplied sends eight commands, one for each area `1..8`, using the selection form above. Supplying literal area `0` instead sends one command for area `0`. Application-wide selection and an explicit zero-area request are therefore distinct; neither establishes a universal broadcast form.

`DIMENSION 10` carries decimal character codes. The tested report `*#22*2#SOURCE*10*104*101*108*108*111*33##` decodes to `hello!`; no fixed eight-character limit is established by that test. The client starts RDS for its first subscriber and delays stopping after the last subscriber by 100 ms, allowing a new subscriber to cancel the pending stop. It re-requests RDS after a stop report only while updates remain enabled. This is subscription policy, not a mandatory protocol response or Device timing rule.

### Local volume and display scales

The historical touchscreen implementation distinguishes local audio settings `L = 0..8` from amplifier volume `V = 0..31`:

| Conversion | Implementation behavior |
| --- | --- |
| Local setting to amplifier volume | Round `L * 31 / 8` to the nearest integer |
| Amplifier volume to local setting | Round `V * 8 / 31` to the nearest integer |
| BtExperience percentage setting `P` to amplifier volume | Integer truncation of `P * 31 / 100` |
| Amplifier volume to BtExperience percentage setting | Integer truncation of `V * 100 / 31` |
| TS10 volume icon | Integer truncation of `V * 8 / 31`, giving indices `0..8` |
| TS3.5 volume icon | Indices `1..9` for bands `0..3`, `4..7`, `8..11`, `12..14`, `15..17`, `18..20`, `21..23`, `24..27`, `28..31`, respectively |

For example, amplifier volume `3` becomes local setting `1` but TS10 icon `0`. The conversion loses precision; icon indices and local settings are not interchangeable with the transmitted value or a calibrated loudness percentage. These are application/build choices, not a Firmware-wide volume rule. See [Volume conversion evidence](../../project/review/myopencommunity-remaining-source-review.md#volume-conversion-evidence).

The separately tested BtExperience percentage API sends volume `19` for `62%` and displays `38%` for reported volume `12`. Its integer conversions are not exact inverses. Earlier application versions used raw amplifier values; this change does not identify a Firmware generation.

### Historical alarm-clock control

The archived touchscreen alarm clocks are local controllers using ordinary source, station, volume and amplifier operations. Their scheduling is separate from the sound protocol; see [Touchscreen alarm-clock scheduling](../../scenario-engine/execution-model.md#historical-touchscreen-alarm-clock-scheduling).

| Controller / operation | Implementation behavior |
| --- | --- |
| Earlier `libqtdevices` helper startup | Select source for area `0`, select a nonzero station if the source is a radio, then process selected amplifiers in address order. In multichannel mode, select that source once per selected area `1..8` before setting volume and issuing Follow Me |
| Earlier helper initial volume | Use each stored amplifier value below `10`; start higher targets at `8`. Negative stored values exclude amplifiers. These are alarm settings, not revised volume domains |
| BtExperience startup at `TS10_1_0_23` | Starting the timer sends no sound command. The first 3-second tick selects the source through the amplifier controller, writes volume `0`, then activates the amplifier; the exact single-amplifier test selects its area |
| BtExperience volume ramp | Tick `t` proposes integer `t * 100 / 31` percent, writing only while this is at most the configured percentage. The amplifier's percentage conversion truncates again: the tested `25%` target sends levels `0..7`, then no further increase in the tested sequence |
| BtExperience snooze / automatic expiry | Snooze sends amplifier OFF and waits 5 minutes before restarting the ramp. The final sound tick sends OFF and stops the timers; the nominal ringing interval is 2 minutes |
| BtExperience explicit Stop | Stops ringing and snooze timers without an amplifier OFF command. The popup's Stop action calls this method; snooze and expiry have separate OFF behavior |

The alarm controllers do not inspect acknowledgements or confirm physical playback. The earlier helper's stop operation turns off selected amplifiers; the compared controllers do not restore the preceding source or volume. BtExperience's “ringing” flag describes an active timer.

For a local media source, a negative first-content callback switches the running alarm to beep mode and sends amplifier OFF. That callback describes content selection or availability, not verified playback failure. Reliable fallback for every USB/SD search or failed network stream is not established. See [Alarm-clock control evidence](../../project/review/myopencommunity-alarm-clock-history-review.md).

### Tone, balance, and presets

| Wire value | Touchscreen interpretation |
| --- | --- |
| High/low tone, dimensions `2` / `4` | integer `raw / 3 - 10`; tests include `0 -> -10`, `30 -> 0`, `60 -> 10` |
| Balance, dimension `17` | leading `0` means left, otherwise right; remaining digits divided by 3 give magnitude |
| Preset `2..11` | built-in application indices `0..9` |
| Preset `16..25` | custom application indices `10..19` |

Balance is textual: tests distinguish `030` (left 10) from `115` (right 5). Preserve leading zeroes. Invalid preset gaps `12..15` are ignored by the tested decoder. These conversions describe the power-amplifier UI, not revised published domains or units for every sound Device.

Relative balance direction remains unresolved between sources: exact client tests emit `42#1` from the method labelled left and `43#1` from right, reversing the published `WHAT` labels above. The method names and their historical correction do not independently establish physical direction.

### Virtual-amplifier temporary-off events

The historical virtual amplifier treats `*22*0#4#AREA*6##` and `*22*22#4#AREA*5#3#AREA#POINT##` as temporary-off events. Its tests show that the second form is matched by area rather than the final point: multichannel mode ignores another area's event, while monochannel mode accepts it. The class describes a one-second local interruption without changing its persistent ON/OFF state. This is touchscreen amplifier behavior, not a universal mute duration or a complete domain for `WHAT 22`.

### Local multimedia initialization

The virtual-source writer emits a private setup form at `WHERE = 7`, `DIMENSION = #15`:

`*#22*7*#15*SOURCE*AREA*POINT*9*9**MATRIX_INPUT*IS_SOURCE*IS_GATEWAY*IS_AMPLIFIER*READS_SCS##`

Empty source configuration becomes `0`; absent amplifier area/point remain empty. `MATRIX_INPUT` is the source address only in multichannel source mode. Flags reflect the writer's local configuration, with `IS_GATEWAY = 1` and `READS_SCS` set when a source or amplifier is configured. The two `9` fields and the empty field after them remain semantically unresolved.

Exact tested examples are `*#22*7*#15*3***9*9**3*1*1*0*1##` for multichannel source 3 and `*#22*7*#15*0*2*8*9*9***0*1*1*1##` for amplifier 28. This establishes product initialization traffic, not a general readable multimedia property. Earlier source emitted a different payload layout.

The virtual source's next/previous methods deliver local playback requests instead of sending bus frames. Its receiver accepts `WHAT 9` / `10` addressed to that source; the area-addressed delegate additionally accepts `WHAT 9` where the source is active. These method names do not redefine the published station/track command families. Source activation requests (`WHAT 1`) remain distinct from source-activity notifications (`WHAT 2`). BtExperience pauses local playback when no area remains active. This local player integration does not establish numeric [`WHO 26` UPnP Multimedia](../who-26-upnp-multimedia/) syntax.

See [Sound Diffusion evidence](../../project/review/myopencommunity-integration.md#sound-dialects-and-matrix-state).

## Source and speaker semantics

Source commands and reports use source addresses; volume/tone/balance operations generally apply to speaker endpoints or areas. `WHAT 35` carries routing intent by selecting a source while turning an amplifier on. Follow Me (`WHAT 34`) is a separate operation and should not be normalized to ordinary ON.

The same namespace includes tuner, media-track, presets, RDS, and equalization. Interpretation depends on the selected source and target class.

## Relationship to `WHO 16`

[`WHO 16`](../who-16-sound-system/) represents a different sound dialect. Similar terms do not imply compatible numeric values, address forms, or parameter layouts.

One MH200N was observed reporting every sound event in both dialects. In those captures the `WHO 22` frame states as separate fields what `WHO 16` packs into one address:

| `WHO 16` | `WHO 22` counterpart | `WHO 22` fields |
| --- | --- | --- |
| `*16*3*11##` | `*#22*3#1#1*12*1*4##` | speaker area 1, point 1; state ON, stereo |
| `*16*3*12##` | `*#22*3#1#2*12*1*4##` | speaker area 1, point 2 |
| `*#16*11*1*17##` | `*#22*3#1#1*1*17##` | volume 17, same `0..31` scale |
| `*16*3*101##` | `*#22*2#1*12*1*4##` | source 1 active |
| `*16*3*112##` | `*22*2#4#1*5#2#2##` | area 1 selecting source 2 |
| `*#16*101*8*…##` | `*#22*5#2#1*10*…##` | RDS text, `DIMENSION 8` against `DIMENSION 10` |

This is **established for that Device** and was used to corroborate the `WHO 16` amplifier and routing addressing. It does not establish a general translation between the dialects: the value ranges, `WHAT` numbering and dimension indices differ, an MH200 on another plant emitted no `WHO 22` frames, and these captures cannot show whether the second dialect originates in the gateway or in another bus device. The claim record is in [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md).

## Evidence basis

Parameters, identifiers, and allowed-message distinctions come from [`WHO 22` specification](https://archive.openwebnet-ha.org/sha256/13/8d/138d9031cd6d70693fa10f6ec05b344fd4efc5fc80c0ffaf9d5dca36d0d26cf0.pdf). Where its summary table and detailed flow differ, this page records the more specific flow and notes the discrepancy.

The tested client forms, source caches, local feedback, tuning and display conversions are traced in [Sound implementation review](../../project/review/myopencommunity-sound-history-review.md). Retained software revisions do not identify deployed Firmware generations.

See the [functional overview](../) for navigation by `WHO` and by function, and [Protocol](../../protocol/) for common frame and session syntax.
