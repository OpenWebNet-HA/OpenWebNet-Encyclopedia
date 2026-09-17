# Validate a Configuration Value

## Goal

Decide whether one intended semantic value is writable for the resolved Device, firmware, Module, and Object, and derive its wire encoding.

## Acquire the current state

Validation requires the installed context, not only the proposed value.

1. If the Device is not yet identified, execute [Discover and Identify Devices](discover-devices.md).
2. Start a fresh interview with `*[WHO]*10#[ID]*0##`, or the documented address/local alternative.
3. Collect identity, firmware, `DIMENSION 30`, and `DIMENSION 32` responses through Device `WHAT 4` or a classified timeout.
4. After resolving the Module/Object layout, send `*#[WHO]*0*38#0##`.
5. Collect the resulting repeated `DIMENSION 35` values and any `DIMENSION 310` response during the detailed-read window.
6. Transform those raw frames using [Read and Present a Device Configuration](read-device-configuration.md).

Do not validate against a stale or partially identified configuration without marking that limitation.

## Procedure

1. Take the resolved installed Device and firmware from the freshly acquired configuration model.
2. Resolve the internal slot and current Object or Virgin Object.
3. Prove that the target Object survives the Virgin Object, firmware, and slot intersections.
4. Resolve the Object- and firmware-scoped `EN_CONF` property.
5. Evaluate `read_only`, `visible`, `hidden`, fixed-value, and conditional metadata.
6. Build the base domain from `EN_CONF_RANGE`.
7. Apply the applicable `EN_FILTER` and `EN_FILTER_RANGE` for the resolved `AS_OBJECT_FIRMWARE` context.
8. Evaluate slot conditions, `EN_CONDITION`, `EN_CONV_RULE`, and `CONF_SYMBOL_REF`.
9. Apply `rules.db3` dependencies for the supported Temperature Control Objects.
10. Revalidate the converted value against the effective domain.
11. Confirm the result fits the `OPEN.db` transport field.
12. Record the expected diagnostic read-back.

## Required result

Validation returns evidence rather than a Boolean:

- status and reason;
- resolved identifiers;
- base and filtered domains;
- condition and conversion path;
- dependencies;
- semantic input and encoded value;
- physical-representation classification;
- expected read-back.

Fail closed when the property, domain, condition, or encoding is ambiguous.

## Common mistakes

- treating `0–65535` as the allowed value set;
- resolving `INDEX` without Object/firmware context;
- merging filters from unrelated firmware associations;
- assuming a hidden value is invalid;
- assuming a physical counterpart uses the same range;
- validating only the changed property when linked rules depend on others.

See [Programming Validation](../programming/validation.md) for the complete fourteen-milestone resolver.
