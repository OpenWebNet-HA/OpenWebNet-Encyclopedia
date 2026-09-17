# Programming Validation

Programming values must be validated against the complete Device, firmware, internal-slot, and Object context before frames are transmitted. Protocol field ranges only establish storage capacity.

## Validation pipeline

### 1. Resolve the target

Resolve:

- management `WHO`;
- installed Device ID or selection address;
- item and firmware;
- internal slot;
- current configured Object or Virgin Object;
- target Object.

Do not join independent identifiers by numeric equality.

### 2. Validate Object availability

Require the target Object to be:

- permitted by the current Virgin Object where the Module is configurable;
- associated with the resolved firmware through `AS_OBJECT_FIRMWARE`;
- placed at the target internal slot through `EN_SLOTS`;
- compatible with fixed-Object and slot-condition metadata.

### 3. Resolve configuration definitions

Collect the applicable Object-scoped and firmware-scoped `EN_CONF` rows. Use `idx` only after scope has been resolved.

Apply `read_only`, `visible`, and `hidden` metadata. A value can be reportable while not writable.

### 4. Establish the base value domain

`EN_CONF_RANGE` can define:

- named discrete values;
- numeric minimum and maximum;
- step;
- digit width;
- default;
- display order.

A missing range row is not evidence that every transport value is allowed.

### 5. Apply Object/firmware filters

`EN_FILTER` binds a configuration definition to an `AS_OBJECT_FIRMWARE` context. `EN_FILTER_RANGE` narrows the available range for that context.

Use `whole_range` and associated filter ranges as represented; do not merge filters from unrelated firmware/Object associations.

### 6. Apply slot conditions and conversions

`AS_SLOT_CONDITION` attaches conditions to catalogue slot records. `EN_CONDITION` selects conversion-rule logic. `EN_CONV_RULE` can compare item and Object configuration symbols, values, unconditional branches, and jumps.

`CONF_SYMBOL_REF` supplies explicit item-to-Object symbol correspondence for a system and slot. It is supporting mapping evidence, not a global replacement for context-sensitive rules.

### 7. Apply additional rules

`rules.db3` adds linked-parameter constraints for selected Temperature Control Objects. It is not a general `WHO` or Object registry and should be consulted only after the Object and index have been resolved.

### 8. Validate address and physical representation

For `DIMENSION 32` writes, apply the selected `OPEN.db` address rule and its fixed structure, levels, validity conditions, object/device family, and advanced offset.

Where a property has a physical-configurator counterpart, distinguish:

- representable physically;
- valid only through advanced/virtual configuration;
- effective value whose active configuration method is unknown.

### 9. Encode the wire value

Only after semantic validation should the value be converted into `KEYO`, `SYS`/`ADDR`, `INDEX`/`VAL_PAR`, or virtual configurator positions.

Retain the raw intended value, resolved catalogue definition, conversion path, and encoded value for verification.

## Validation result

| Result | Meaning |
| --- | --- |
| Valid | directly allowed in the resolved context |
| Valid after conversion | permitted after an established conversion |
| Conditionally valid | depends on another selected value or Object |
| Advanced-only | valid but not physically representable |
| Read-only/fixed | part of effective state but not writable |
| Invalid | excluded by an applicable capability or rule |
| Ambiguous | more than one definition remains |
| Unresolved | required context or mapping is absent |

An implementation should fail closed for programming when semantic resolution is ambiguous. Preserving an unknown value is appropriate for diagnostics; transmitting an unvalidated interpretation can alter Device state.

## Source priority

Use the canonical implementation databases for exact programming support and constraints. Public protocol documents supply shared syntax and functional meaning. Product manuals can establish physical configurator layouts. Captures and UI behavior corroborate runtime sequencing and presentation but must not override explicit database constraints without documenting the discrepancy.
