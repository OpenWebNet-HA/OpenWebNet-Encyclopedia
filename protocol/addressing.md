# Addressing

OpenWebNet addressing is system-specific. `WHERE` identifies the destination or source of a frame, but its grammar depends on the selected `WHO` and must not be interpreted as a single universal address type.

## Address interpretation

A parser must resolve `WHO` before interpreting `WHERE`. Different systems can use different address layouts, ranges, hierarchy levels, and advanced-address forms.

Lighting (`WHO 1`) and Automation (`WHO 2`) share the SCS `A`/`PL` address family. In that family the textual shape of `WHERE` distinguishes an individual point from an environment, group, general scope, or local-bus target. Leading zeroes can therefore be significant.

Other systems, such as Thermoregulation, use different grammars and must not be decoded with the `A`/`PL` rules below.

## Lighting and Automation A/PL grammar

| Scope | `WHERE` syntax | Valid values |
| --- | --- | --- |
| General | `0` | complete system selected by `WHO` |
| Environment / area | `A` | `00`, `1`–`9`, or `100` |
| Point to point | `APL` | valid combinations listed below |
| Group | `#GR` | `GR = 1`–`255` |
| Local bus | `APL#4#INTERFACE` | valid `APL`; `INTERFACE = [0-1][1-9]` |

The labels *environment* and *area* refer to the same collective `A` level in different source/UI contexts. The meaning remains scoped to the selected functional `WHO`.

### Point-to-point A/PL

A point address is the concatenation of its `A` and `PL` representations; it is not an arbitrary decimal integer. The allowed `PL` form depends on `A`:

| `A` representation | Valid `PL` | Examples |
| --- | --- | --- |
| `1`–`9` | `1`–`9` | `11`, `56`, `99` |
| `00` | `01`–`15` | `0001`, `0015` |
| `10` | `01`–`15` | `1001`, `1015` |
| `01`–`09` | `10`–`15` | `0110`, `0915` |

Thus `56` is the point `A=5, PL=6`, whereas `0015` is `A=00, PL=15`. Converting the field to an integer before applying the grammar can destroy information required to parse it correctly.

### Collective addresses

`WHERE=0` is the general address and targets the complete functional system selected by `WHO`.

An environment/area address contains only the `A` component. Valid forms are `1`–`9` plus the extended forms `00` and `100`. It must not be reconstructed by numerically shortening a point address.

A group address is explicitly marked by `#`: `#1` through `#255`. The prefix is part of the protocol syntax, so a group must not be represented as the bare decimal group number.

### Local-bus address

A local-bus target extends a valid point address:

~~~text
APL#4#INTERFACE
~~~

`INTERFACE` has the form `[0-1][1-9]`. The `#4#` component is structural syntax, not part of the numeric `A`/`PL` value.

## Parsing rules

An implementation should preserve the raw `WHERE` string and classify it using the grammar for the selected `WHO`. Resolve the functional system first, recognize structural markers such as `#` before numeric conversion, preserve leading zeroes, validate the complete syntactic form and its ranges, and only then expose structured components such as `A`, `PL`, group, or interface.

A syntactically valid address is not necessarily applicable to every Device or Object. Device capabilities, system rules, and operation-specific restrictions can further constrain which addresses are meaningful.

## MyHOME Suite address rules

MyHOME Suite 3.5.38 stores protocol address grammars in `OPEN.db`. `EN_ADDRESS_RULE` defines individual rules and `AS_SYSTEM_ADDRESS_RULE` associates them with systems.

~~~sql
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
~~~

These rules demonstrate that address syntax is part of the selected system rather than a property of the frame transport itself. They can also add Object/Device-family validity conditions beyond the generic grammar documented above.

## Advanced addressing

Some systems use additional `#`-qualified or prefixed forms. The role of those components is determined by the address grammar of the selected `WHO`; they must not be generalized from the Lighting/Automation syntax.

See the relevant functional `WHO` addressing page for system-specific applicability, and [Frame Syntax](frame-syntax.md) for the position of `WHERE` in OpenWebNet frames.
