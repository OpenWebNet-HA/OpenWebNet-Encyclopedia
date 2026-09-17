# Programming Validation

Every requested Object, address, and configuration value must be validated in its complete Device, firmware, slot, and Object context before transmission.

## Validation order

1. Resolve the Device item and firmware.
2. Resolve the target internal slot.
3. Resolve the current Virgin Object or configured Object.
4. Establish whether the requested Object or property is available.
5. Resolve the applicable `EN_CONF` definition.
6. Apply `EN_CONF_RANGE`.
7. Apply `EN_FILTER` and `EN_FILTER_RANGE`.
8. Apply slot conditions and conversion rules.
9. Apply relevant `rules.db3` dependencies.
10. Enforce read-only, fixed, hidden, and visibility metadata where applicable.
11. Validate the system-specific address grammar or physical representation.
12. Encode the accepted value for the programming frame.

## Outcomes

| Outcome | Meaning |
| --- | --- |
| Valid | accepted directly in the resolved context |
| Valid after conversion | requires an established encoding or conversion rule |
| Conditionally valid | depends on another property or selected Object |
| Advanced-only | valid in advanced configuration but not physically representable |
| Read-only or fixed | reported or derived but not writable |
| Invalid | excluded by an applicable rule |
| Unresolved | required context or mapping is missing |

Numeric range membership alone is insufficient when filters, conditions, conversions, or linked properties apply.
