# Configuration Programming

Configuration programming writes indexed Object or firmware properties after the Device, firmware, internal slot, and target Object have been resolved.

## Write frame

`*#[WHO]*0*#35#[INDEX]#[SLOT]*[VAL_PAR]##`

| Field | `OPEN.db` range | Meaning |
| --- | ---: | --- |
| `INDEX` | `0`–`255` | configuration index |
| `SLOT` | `1`–`255` | Device-local internal slot |
| `VAL_PAR` | `0`–`65535` | encoded value |

`INDEX` correlates with `EN_CONF.idx` but is not globally unique.

## Resolving a property

1. Resolve the installed Device and firmware.
2. Resolve `SLOT` and the target Object selected earlier in the transfer.
3. Find Object-scoped definitions with the Object's `id_key_object` and `id_firmware = 0`.
4. Find applicable firmware-scoped definitions with `id_key_object = 0` and the resolved firmware.
5. Select definitions whose `idx` equals `INDEX`.
6. Apply filters, conditions, conversions, and value encoding.
7. Retain the resolved `EN_CONF.id_conf` with the transmitted tuple.

Do not require one `EN_CONF` row to contain both a valid Object and firmware key; the scopes are mutually exclusive in the canonical catalogue.

### Object and firmware scopes

`EN_CONF` uses `0` as a “not applicable” sentinel on the unused ownership axis:

| Scope | `id_key_object` | `id_firmware` |
| --- | --- | --- |
| Object property | resolved Object ID | `0` |
| Firmware property | `0` | resolved firmware ID |

The zero values do not identify Object 0 or firmware 0. They take the place of `NULL` and distinguish which entity owns the definition. Applicable definitions must therefore be collected as the union of the two scopes:

```sql
WHERE (id_key_object = :object_id AND id_firmware = 0)
   OR (id_key_object = 0 AND id_firmware = :firmware_id)
```

A query requiring both resolved IDs in the same row would miss the canonical definitions. Resolve the scope before interpreting `idx`, because an index is not globally unique.

## Transfer behavior

Parameter writes are optional and repeatable within `ConfKO`. `NACK` transitions the canonical sequence to Warning rather than Error.

The Device can report:

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

`OPEN.db` classifies this as error-and-information because a Device can leave some parameters unmanaged without stopping the whole configuration. The sequence maps it to Warning. Preserve each warning by `SLOT` and `INDEX`; do not discard the rest of the accepted configuration.

## Value forms

Depending on the resolved definition, `VAL_PAR` can encode:

- an enumeration;
- a numeric range;
- a padded value;
- a boolean;
- a fixed value;
- a user-supplied value;
- a value requiring a conversion rule.

The transport maximum does not override `EN_CONF_RANGE`, `EN_FILTER_RANGE`, or linked-property rules.

## Physical counterparts

An indexed property can correspond to a physical configurator position even when the symbols differ. For example, firmware `192` uses physical `TYPE` and `PRE` positions while shutter actuator Object `218` uses indexed `SHUTTER_TYPE` and `PRESET_NUMBER` properties.

A physical counterpart does not prove that the installed value was physically configured, and physical and advanced encodings need not use the same range.

See [Configuration](../device-model/configuration.md), [Programming Validation](validation.md), and diagnostic [`DIMENSION 35`](../diagnostics/dim35-configuration.md).

## Special parameters

Diagnostic `DIMENSION 310` carries an Object-specific value without `INDEX`. `OPEN.db` provides no corresponding generic programming write in `ConfKO`. Do not force it into `DIMENSION 35` programming without Object-specific evidence.
