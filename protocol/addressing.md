# Overview

OpenWebNet addressing is system-specific. `WHERE` identifies the destination or source of a frame, but its grammar depends on the selected `WHO` and must not be interpreted as a single universal address type.

## Address interpretation

A parser should resolve `WHO` before interpreting `WHERE`. Different systems can use different address layouts, ranges, hierarchy levels, and advanced-address forms.

For example, Lighting and Automation use address structures based on `A`/`PL` and related environment or group forms, while Thermoregulation uses its own zone-oriented grammar.

## MyHOME Suite address rules

MyHOME Suite 3.5.38 stores protocol address grammars in `OPEN.db`. `EN_ADDRESS_RULE` defines individual rules and `AS_SYSTEM_ADDRESS_RULE` associates them with systems.

The following query lists the configured address rules by system:

```sql
SELECT
    sar.id_system,
    ar.id_address_rule,
    ar.address_rule_virt,
    ar.address_rule_adv,
    ar.level_2_rule,
    ar.level_4_rule,
    ar.validity_rule,
    ar.object_device_family,
    ar.offset_adv
FROM AS_SYSTEM_ADDRESS_RULE AS sar
JOIN EN_ADDRESS_RULE AS ar
    ON ar.id_address_rule = sar.id_address_rule
ORDER BY sar.id_system, ar.id_address_rule;
```

These rules demonstrate that address syntax is part of the selected system rather than a property of the frame transport itself.

## Advanced addressing

Some address forms use `#`-qualified syntax. The role of `#` is determined by the address grammar of the selected `WHO`; it should not be interpreted independently of that grammar.

## Implementation guidance

An implementation should model an address as a system-specific structure rather than storing only an undifferentiated `WHERE` string. The raw field should still be retained when exact frame reproduction or diagnostics are required.

See [`frame-syntax.md`](frame-syntax.md) for frame structure, [`what.md`](what.md) for `WHAT`, and [`dimensions.md`](dimensions.md) for `DIMENSION` operations.