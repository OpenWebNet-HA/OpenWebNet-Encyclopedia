# CEN+

CEN+ is carried within `WHO 25` and provides a virtual-object command/event model for short press, extended press and rotary-selector interactions. It is related to CEN under [`WHO 15`](../who-15-cen/) but uses a different field allocation and address space.

## `WHAT` reference

| `WHAT` | Meaning |
| ---: | --- |
| `21` | Short pressure, less than 0.5 seconds |
| `22` | Start of extended pressure, at least 0.5 seconds |
| `23` | Extended pressure / keep pressing |
| `24` | Release after an extended pressure |
| `25` | Rotary selector, slow clockwise rotation |
| `26` | Rotary selector, fast clockwise rotation |
| `27` | Rotary selector, slow counter-clockwise rotation |
| `28` | Rotary selector, fast counter-clockwise rotation |

Unlike `WHO 15`, the interaction type is encoded by `WHAT`; the virtual pushbutton number is carried as a parameter.

## Pushbutton parameter

The parameter attached to `WHAT` identifies the virtual pushbutton and has the range `0`–`31`.

The general form is `*25*WHAT#PUSHBUTTON*WHERE##`.

`PUSHBUTTON` and the Object embedded in `WHERE` are independent fields: the first identifies the control on the source Object, while the second identifies the configured CEN+ virtual Object.

## `WHERE` - virtual Object

CEN+ uses a virtual address formed from the prefix `2` and an Object value in the range `0`–`2047`.

Conceptually:

`WHERE = 2 + OBJECT`

Published examples include `21` for Object 1, `20` for Object 0, `2101` for Object 101, `22010` for Object 2010, and `22047` for Object 2047. The field is therefore a protocol composition, not a decimal arithmetic addition.

A decoder should remove/interpret the CEN+ prefix according to the `WHO 25` grammar rather than parse the complete field as a Lighting/Automation `A`/`PL` address.

## Short pressure - `WHAT 21`

Action frame: `*25*21#PUSHBUTTON*WHERE##`.

A short interaction is complete in one event. It represents a press and release occurring before the 0.5-second extended-pressure threshold; there is no separate short-release `WHAT` analogous to CEN `WHO 15` `#1`.

The accepted virtual action is acknowledged with `ACK`, and the corresponding CEN+ frame is visible on event connections.

## Start of extended pressure - `WHAT 22`

Action frame: `*25*22#PUSHBUTTON*WHERE##`.

This marks that the button has reached the extended-pressure threshold. It begins the long-interaction sequence and is distinct from the periodic continued-pressure event `WHAT 23`.

## Extended pressure - `WHAT 23`

Action frame: `*25*23#PUSHBUTTON*WHERE##`.

While a physical CEN+ button remains pressed, continued-pressure events can follow the initial `WHAT 22`. Multiple `WHAT 23` frames may therefore belong to one physical interaction.

## End of extended pressure - `WHAT 24`

Action frame: `*25*24#PUSHBUTTON*WHERE##`.

This marks release after an extended interaction and closes the sequence begun by `WHAT 22`.

A typical held-button event sequence is therefore:

`WHAT 22` → zero or more `WHAT 23` → `WHAT 24`.

The published examples show both sequences with repeated `23` frames and a sequence in which `22` is followed directly by `24` when release occurs before another continued-pressure interval is emitted.

## Rotary-selector events - `WHAT 25`–`28`

CEN+ also defines directional rotary interactions:

| Direction | Slow | Fast |
| --- | ---: | ---: |
| Clockwise | `25` | `26` |
| Counter-clockwise | `27` | `28` |

These operations use the same virtual Object/pushbutton addressing model. Their presence is an important difference from Basic/Evolved CEN under `WHO 15`.

## Action and event connections

CEN+ supports virtual actions and event reporting. For pushbutton interactions, a client sends the functional frame on an action connection and receives `ACK`; event-session clients receive the corresponding frame when the gateway reads the CEN+ event on the SCS bus.

The same event form can therefore represent an interaction originating from a physical CEN+ command or from a virtual action submitted through a gateway. The functional frame itself identifies the interaction, pushbutton and Object rather than its origin.

## CEN+ configuration model

The published CEN documentation states that CEN+ devices use Advanced Virtual Configuration and do not use a conventional SCS bus address for this function. The configured virtual Object becomes the OpenWebNet `WHERE`, while the button number is represented by the `WHAT` parameter.

This is materially different from Basic/Evolved CEN, where `WHO 15` `WHERE` can represent an `A`/`PL` source address and the button number itself occupies `WHAT`.

## Relationship to CEN

| Property | CEN - `WHO 15` | CEN+ - `WHO 25` |
| --- | --- | --- |
| Button number | `WHAT 00`–`31` | `WHAT` parameter `0`–`31` |
| Interaction phase | optional `WHAT` parameter `#1`–`#3` | `WHAT 21`–`24` |
| Source/target | `A`/`PL` and advanced CEN `WHERE` forms | virtual Object `0`–`2047` with prefix `2` |
| Rotary events | not defined in the published CEN table | `WHAT 25`–`28` |

The two systems should be modeled separately even when a physical command device is capable of both modes.

## Other `WHO 25` functions

`WHO 25` also carries dry-contact and IR functions using `WHAT 31` and `32`. Those operations use different parameters and `WHERE` grammars and are documented in [Dry Contact and IR](dry-contact-ir.md).