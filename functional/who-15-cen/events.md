# CEN Events

`WHO 15` carries CEN command/button interactions. The protocol represents the logical CEN button together with the phase of the user interaction, allowing a receiver to distinguish a press from the corresponding release and extended-pressure sequence.

CEN+ is a separate family under [`WHO 25`](../who-25-transversal/cen-plus.md). CEN and CEN+ must not be collapsed into a single event vocabulary.

## Button identifiers

Published CEN button identifiers occupy `00`–`31`. The button number identifies the logical CEN command point; it is not a Lighting/Automation A/PL address.

## Interaction phases

The CEN protocol distinguishes four interaction phases:

| Phase | Meaning |
| --- | --- |
| Pressure | Initial button activation |
| Release after short pressure | Button released before an extended pressure is established |
| Release after extended pressure | Button released after an extended interaction |
| Extended pressure | Continued/extended activation |

These phases are represented through the parameterized CEN `WHAT` form. An implementation must preserve both the button identifier and the interaction parameter rather than normalizing the event to a simple pressed/released Boolean.

## Action and event connections

The published specification describes both action-connection and event-connection use. Action traffic can generate virtual pressure/release interactions, while event traffic reports the corresponding physical/logical CEN interaction. The same conceptual phases therefore occur in both directions, but direction and connection role remain part of the interpretation.

## State-machine handling

Extended interaction is a sequence rather than an isolated value. A consumer interested in gestures should retain the progression from pressure through extended pressure to release. A short interaction instead terminates with the short-release phase.

Applications should not synthesize an extended interaction merely from elapsed local time when the protocol supplies explicit phase events.

## Relationship to CEN+

`WHO 25` CEN+ uses a different `WHAT` vocabulary and a virtual Object address range up to `2047`. It additionally defines rotary-selector operations. See [`../who-25-transversal/cen-plus.md`](../who-25-transversal/cen-plus.md).