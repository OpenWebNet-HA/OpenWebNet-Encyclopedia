# Addressing

`WHO 1` uses the SCS Lighting `A`/`PL` addressing model. `WHERE` can select an individual light point, an environment, a group, the complete Lighting system, or a point reached through an interface/extended address form.

The same broad address family is shared with Automation, but `WHERE` remains scoped to the selected `WHO`: a Lighting address identifies Lighting Objects and must be interpreted using the Lighting operation in which it occurs.

## Address scopes

| Scope | Role |
| --- | --- |
| General | Addresses the complete Lighting system |
| Environment | Addresses the Lighting Objects belonging to an environment |
| Point to point | Addresses an individual `A`/`PL` light point |
| Group | Addresses the Lighting Objects belonging to a group |
| Extended / local bus | Reaches a point through the applicable interface or advanced address rule |

The published Lighting grammar preserves significant leading zeroes in extended `A`/`PL` forms. A `WHERE` should therefore be parsed as protocol syntax before any numeric conversion.

## MyHOME_Suite address rules

The MyHOME_Suite `OPEN.db` definitions distinguish Lighting/Automation address rules rather than representing `WHERE` as one untyped integer. Relevant rules include point-to-point `[A][PL]`, environment `[A]`, and advanced forms. This confirms that the syntactic shape of the address participates in its meaning.

The same database contains system-to-address-rule associations, so an encoder or parser should select the rule from the system/operation context instead of inferring the address class solely from the number of digits.

## Scope and event reporting

Commands sent to a collective scope can result in state/event reporting for the individual Lighting Objects affected by the operation. Clients should therefore be prepared for a general, environment, or group command to be followed by point-specific state traffic rather than expecting only a frame that repeats the original collective `WHERE`.

This behavior is especially relevant when maintaining a live Lighting state model: the command target describes the requested scope, while subsequent events describe the resulting state of Objects within that scope.

See [`what.md`](what.md) for Lighting commands, [`dimensions.md`](dimensions.md) for structured Lighting values, and [`../../protocol/addressing.md`](../../protocol/addressing.md) for the common system-scoped addressing model.