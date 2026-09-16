# CEN+

CEN+ functions are carried within the `WHO 25` namespace. They are distinct from the CEN event family under [`WHO 15`](../who-15-cen/).

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `21` | Short press, less than 0.5 seconds |
| `22` | Start of extended press, at least 0.5 seconds |
| `23` | Extended press |
| `24` | Release after an extended press |
| `25` | Rotary selector, slow clockwise rotation |
| `26` | Rotary selector, fast clockwise rotation |
| `27` | Rotary selector, slow counter-clockwise rotation |
| `28` | Rotary selector, fast counter-clockwise rotation |

## Pushbutton parameter

The parameter following `WHAT` identifies the virtual pushbutton and has the published range `0`–`31`. Event frames therefore follow `*25*WHAT#pushbutton*WHERE##`.

## Addressing

CEN+ uses a virtual address rather than physical A/PL addressing. The published object range is `0`–`2047`, represented by a `WHERE` composed from the CEN+ address prefix and Object value.

A decoder should therefore resolve `WHO 25` and the CEN+ operation before interpreting `WHERE`; it must not be parsed as a Lighting/Automation point-to-point address.

## Relationship to other `WHO 25` functions

`WHO 25` also carries dry-contact and IR functions. Sharing the same `WHO` does not make those operations CEN+; they are documented separately in [`dry-contact-ir.md`](dry-contact-ir.md).