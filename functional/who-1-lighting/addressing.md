# Addressing

`WHO 1` uses the SCS Lighting `A`/`PL` addressing model. `WHERE` can select an individual light point, an environment, a group, the complete Lighting system, or a point reached through an interface/extended address form.

The same broad address family is shared with Automation, but `WHERE` remains scoped to the selected `WHO`: a Lighting address identifies Lighting Objects and must be interpreted using the Lighting operation in which it occurs.

## Address scopes

| Scope | `WHERE` form | Role |
| --- | --- | --- |
| General | `0` | Addresses the complete Lighting system |
| Environment / area | `A` | Addresses the Lighting Objects belonging to an environment |
| Point to point | `APL` | Addresses an individual `A`/`PL` light point |
| Group | `#GR` | Addresses the Lighting Objects belonging to a group |
| Riser / level 3 | `0#3`, `A#3`, `#G#3`, or `APL#3` | Routes the corresponding scope on the riser/backbone level |
| Local bus / level 4 | `0#4#Int`, `A#4#Int`, `#G#4#Int`, or `APL#4#Int` | Routes the corresponding scope through local-bus interface `Int` |

The canonical [`A`/`PL` grammar](../../protocol/addressing.md#lighting-and-automation-apl-grammar) defines the shared base ranges and the less-common forms that differ between Lighting and Automation. Advanced forms are modeled as a base target plus a routing qualifier: `#3` for the riser/backbone level or `#4#Int` for a local bus. The published `WHO 1` material establishes these qualifiers for General, Area, Group, and point targets. `Int` is the routing-interface address; for Lighting it is `01`–`09` or `11`–`15`. Leading zeroes and `#` markers are significant; a `WHERE` must be parsed as protocol syntax before numeric conversion.

## MyHOME_Suite address rules

The MyHOME_Suite `OPEN.db` definitions distinguish Lighting/Automation address rules rather than representing `WHERE` as one untyped integer. Relevant rules include point-to-point `[A][PL]`, environment `[A]`, and advanced forms. This confirms that the syntactic shape of the address participates in its meaning.

The same database contains system-to-address-rule associations, so an encoder or parser should select the rule from the system/operation context instead of inferring the address class solely from the number of digits.

## Scope and event reporting

Commands sent to a collective scope can result in state/event reporting for the individual Lighting Objects affected by the operation. Clients should therefore be prepared for a general, environment, or group command to be followed by point-specific state traffic rather than expecting only a frame that repeats the original collective `WHERE`.

This behavior is especially relevant when maintaining a live Lighting state model: the command target describes the requested scope, while subsequent events describe the resulting state of Objects within that scope.

See [`WHAT` Reference](what.md) for Lighting commands, [`DIMENSION` Reference](dimensions.md) for structured Lighting values, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.