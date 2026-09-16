# CEN+

CEN+ functions are carried within the `WHO 25` namespace. They provide virtual pushbutton and rotary-selector interactions over a virtual Object address space and are distinct from the CEN family under [`WHO 15`](../who-15-cen/).

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `21` | Short pressure, less than 0.5 seconds |
| `22` | Start of extended pressure, at least 0.5 seconds |
| `23` | Extended pressure |
| `24` | Release after an extended pressure |
| `25` | Rotary selector, slow clockwise rotation |
| `26` | Rotary selector, fast clockwise rotation |
| `27` | Rotary selector, slow counter-clockwise rotation |
| `28` | Rotary selector, fast counter-clockwise rotation |

The values form two related groups: `21`–`24` describe pushbutton interaction phases, while `25`–`28` describe rotary direction and speed.

## Pushbutton parameter

The parameter following `WHAT` identifies the virtual pushbutton and has the published range `0`–`31`. Event frames therefore follow `*25*WHAT#PUSHBUTTON*WHERE##`.

The pushbutton number and `WHERE` identify different parts of the event and must remain separate in an implementation. The former identifies the control within the virtual Object; the latter identifies the CEN+ Object itself.

## Press sequence

A short interaction is represented by `WHAT 21`. An extended interaction progresses through start (`22`), extended (`23`), and release (`24`) phases. Consumers implementing gestures should retain these protocol phases rather than collapsing them into a Boolean state.

## Rotary interaction

Rotary events encode both direction and speed directly in `WHAT`:

| Direction | Slow | Fast |
| --- | ---: | ---: |
| Clockwise | `25` | `26` |
| Counter-clockwise | `27` | `28` |

This is event semantics; it does not imply a Lighting level change until another component maps the CEN+ event to a Lighting or Automation action.

## Addressing

CEN+ uses a virtual address rather than physical A/PL addressing. The published Object range is `0`–`2047`. This matches the virtual-address range established by our MyHOME_Suite/device analysis.

A decoder must resolve `WHO 25` and the CEN+ operation before interpreting `WHERE`; the address must not be parsed as a Lighting/Automation point-to-point address.

## Action and event use

The published `WHO 15/25` specification distinguishes action connections, which can inject virtual interactions, from event connections, which report interactions. This means the same CEN+ vocabulary can participate in generated actions and observed events while connection role determines direction and use.

## Relationship to other `WHO 25` functions

`WHO 25` also carries dry-contact and IR functions. Sharing the same `WHO` does not make those operations CEN+; they are documented separately in [`dry-contact-ir.md`](dry-contact-ir.md).