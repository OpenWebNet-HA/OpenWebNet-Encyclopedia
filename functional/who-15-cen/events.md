# CEN Events

`WHO 15` carries Basic and Evolved CEN button interactions. A CEN frame identifies the button through `WHAT`, the command source through `WHERE`, and — for Evolved CEN phases — the interaction phase through a parameter attached to `WHAT`.

CEN frames can originate from physical SCS commands configured in CEN mode or can be injected virtually by a client through an OpenWebNet/SCS gateway. Event-session clients receive the corresponding bus event.

## Interaction model

Basic CEN reports the initial pressure. Evolved CEN adds release and hold information, allowing a receiver to distinguish a short press from an extended interaction.

| Interaction | Frame form |
| --- | --- |
| Pressure | `*15*BUTTON*WHERE##` |
| Release after short pressure | `*15*BUTTON#1*WHERE##` |
| Release after extended pressure | `*15*BUTTON#2*WHERE##` |
| Extended pressure | `*15*BUTTON#3*WHERE##` |

## Button `WHAT`

The button identifier occupies the range `00`–`31`. The leading zero is significant in the published examples and should be preserved when representing the canonical frame text.

| `WHAT` | Meaning |
| --- | --- |
| `00`–`31` | CEN button number |

The button number is not the physical address of the command device. Device/source addressing is carried separately by `WHERE`.

## `WHAT` parameters

| Parameter | Meaning |
| ---: | --- |
| none | Initial pressure |
| `#1` | Release after short pressure |
| `#2` | Release after extended pressure |
| `#3` | Extended pressure / keep pressing |

An extended pressure begins after the button has been held for approximately 0.5 seconds. The published behavior then emits an extended-pressure frame every approximately 0.5 seconds while the button remains pressed, followed by `#2` when it is released.

This makes CEN a small interaction state machine rather than four unrelated events.

## Short interaction sequence

A short press produces:

`*15*BUTTON*WHERE##` → `*15*BUTTON#1*WHERE##`

The first frame marks pressure; the second identifies release before the extended-pressure threshold.

## Extended interaction sequence

A held button produces:

`*15*BUTTON*WHERE##` → one or more `*15*BUTTON#3*WHERE##` → `*15*BUTTON#2*WHERE##`

Receivers should tolerate repeated `#3` frames for one physical hold. They represent continued pressure, not separate button activations.

## `WHERE` addressing

The published CEN address table includes normal A/PL and advanced/local-bus forms.

| Form | Meaning |
| --- | --- |
| `[1-9][1-9]` | Normal area/light-point A/PL |
| `[00][01-15]` | Zone 0, advanced A/PL |
| `[10][01-15]` | Zone 10, advanced A/PL |
| `[01-09][10-15]` | Light point 10–15, advanced A/PL |
| `WHERE#3` | Private riser bus parameter |
| `WHERE#4#[01-15]` | Local bus selected by interface `I4` |

The address must be parsed according to the CEN grammar. Values such as `0001`, `22`, and local-bus forms are source addresses, not CEN+ virtual Objects.

## Action connection

A client can generate a virtual CEN interaction by writing the same functional frames on an action connection. The gateway returns `ACK` when it accepts the frame for transmission.

Published virtual operations are:

| Operation | Action frame |
| --- | --- |
| Pressure | `*15*BUTTON*WHERE##` |
| Short release | `*15*BUTTON#1*WHERE##` |
| Release after extended pressure | `*15*BUTTON#2*WHERE##` |
| Extended pressure | `*15*BUTTON#3*WHERE##` |

A corresponding frame is then visible to event-session clients when the CEN frame is read on the SCS bus.

## Event connection

Event frames can originate from either a physical CEN-configured command or a virtual CEN operation sent by an OpenWebNet client. The wire form does not encode that origin distinction; consumers observing an event connection receive the CEN interaction itself.

The published examples demonstrate normal, advanced and local-bus addresses, including `*15*01*0001##`, `*15*02*22##`, `*15*06*36#4#01##`, and their release/extended variants. These examples establish that the `#4#I4` suffix belongs to `WHERE`, while the `#1`/`#2`/`#3` suffix belongs to `WHAT`.

## Device configuration modes

The CEN specification distinguishes how a physical command obtains its source identity:

| Configuration | Bus address behavior |
| --- | --- |
| Advanced Virtual Configuration | CEN device does not use a conventional address on the SCS bus; configured Object/address is mapped to `WHERE` |
| Basic Virtual Configuration | Device uses an SCS bus address |
| Physical configurators | Device uses an SCS bus address |

This configuration distinction affects the source represented by `WHERE`; it does not change the CEN button interaction vocabulary.

## CEN versus CEN+

CEN+ is carried under [`WHO 25`](../who-25-transversal/cen-plus.md) and uses a different event model: `WHAT 21`–`24` encode the interaction phase while the pushbutton number becomes a `WHAT` parameter and `WHERE` identifies a virtual Object. Rotary-selector events are also defined there.

A parser must therefore select `WHO 15` or `WHO 25` before interpreting the numeric fields. CEN and CEN+ are related command systems but are not alternate encodings of one universal `WHAT` table.