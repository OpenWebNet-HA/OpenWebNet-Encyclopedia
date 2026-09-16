# Overview

`WHERE` identifies the destination or source of an OpenWebNet operation. Its grammar is defined by the selected `WHO`; OpenWebNet does not use one universal address representation for every system.

## Address scope

A `WHERE` value can represent a physical or logical endpoint, a group, an area, a general destination, or another system-specific recipient. The available forms depend on the system.

For example, Lighting and Automation use addressing forms based on SCS address concepts such as `A` and `PL`, while Thermoregulation uses zone-oriented fields such as `ZA` and `ZB`. Other systems define additional recipient structures.

Consequently, a parser must resolve `WHO` before interpreting `WHERE`.

## Address rules in MyHOME Suite

The canonical MyHOME Suite 3.5.38 `OPEN.db` represents address grammars in `EN_ADDRESS_RULE` and associates them with systems through `AS_SYSTEM_ADDRESS_RULE`. Rules include virtual and advanced forms and can define additional Level 2 or Level 4 addressing.

The database can be inspected with:

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

The same relationship is used by the canonical `OpenQuery.txt` support file.

## Parsing rule

Implementations should treat `WHERE` as a system-specific grammar rather than coercing it into a single numeric type. A suitable parser first identifies `WHO`, selects the applicable address rule, and then parses the `WHERE` field according to that rule.

See [`frame-syntax.md`](frame-syntax.md) for the enclosing frame forms.