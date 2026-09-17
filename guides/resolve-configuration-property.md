# Resolve a Configuration Property

## Goal

Map one `DIMENSION 35` tuple to the applicable `EN_CONF` definition and user-facing property.

## Inputs

- resolved Device item and firmware;
- internal `SLOT`;
- configured Object for that slot;
- `INDEX` and raw `VAL_PAR`;
- applicable Object/firmware association.

## Procedure

1. Collect Object-scoped definitions where `id_key_object` is the resolved internal Object ID and `id_firmware = 0`.
2. Collect firmware-scoped definitions where `id_key_object = 0` and `id_firmware` is resolved.
3. Form their union.
4. Select definitions whose `idx` equals the reported `INDEX`.
5. Use scope, symbol, semantic type, filters, conditions, UI evidence, and captures to eliminate incompatible matches.
6. Retain the selected `EN_CONF.id_conf` with the raw tuple.
7. Interpret `VAL_PAR` through the resolved data type, ranges, filters, and conversions.

The zero values are scope sentinels, not Object or firmware ID 0. `INDEX` is not globally unique.

## Resolution outcomes

| Outcome | Treatment |
| --- | --- |
| one compatible definition | decode the value |
| several compatible definitions | retain ambiguity |
| no definition | preserve raw tuple as unresolved |
| read-only/fixed definition | report it but do not infer writability |

## Expected result

A property record containing scope, `id_conf`, `idx`, symbol, description, data type, raw value, decoded value, and evidence path.

See [Configuration Programming](../programming/configuration-programming.md) and [Configuration](../device-model/configuration.md).
