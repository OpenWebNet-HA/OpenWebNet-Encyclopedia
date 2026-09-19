# Addressing

`WHO 24` uses a structured sender/recipient `WHERE` rather than the `A`/`PL` grammar of `WHO 1`.

The complete `WHERE` contains both recipient and sender:

~~~text
RECIPIENT_ZONE#RECIPIENT_ENDPOINT#00#SENDER_ZONE#SENDER_ENDPOINT
~~~

The source writes an endpoint as `dev_type & sys_addr`. Its examples concatenate those values: `dev_type = 1` and `sys_addr = 1` become `11`; a Lighting Console (`99991`) at system address `1` becomes `999911`. The `&` is notation, **not a transmitted character**. The literal `#00#` separates recipient and sender within one `WHERE`; it is not a choice between two alternative whole-address forms.

For example, `*#24*1001#11#00#0#999911*#3*200##` writes maintained illuminance of 200 lux to zone 1 on BMNE500 system address 1, from a Lighting Console at system address 1.

Some source examples use bare special endpoint codes (`8`, `4`, or `99991`) without a separately recognizable system-address suffix. Preserve these explicitly illustrated special forms rather than requiring a suffix on every endpoint or guessing one.

## Lighting Management zone

| `LM_zone_num` | Meaning |
| --- | --- |
| `0` | No zones |
| `1000` | Every zone |
| `1000 + zone number` | Selected zone |

The zone encoding is therefore offset-based. A displayed zone number and its wire value are not necessarily identical.

## Device type

| `dev_type` | Meaning |
| ---: | --- |
| `1` | BMNE500 / 002645 |
| `99991` | Lighting Console |
| `9991` | Virtual Configurator |
| `4` | Broadcast |
| `8` | Unknown in the published table |

`dev_type 8` remains unknown. No device role is assigned without additional evidence.

## System address

`sys_addr` uses the published range `1..9`. It is a Lighting Management system-address component and must not be interpreted as an SCS `A` or `PL` configurator.

## Sender versus recipient

Represent recipient and sender as separate fields inside the decoded address. Replies reverse their communication roles; do not assume that the complete response `WHERE` equals the request `WHERE`. The source examples also vary the suffix on special endpoint codes, so preserve the raw endpoint alongside any decoded type/address.

This address grammar is one of the principal reasons `WHO 24` must remain separate from ordinary [`WHO 1`](../who-1-lighting/) Lighting.

## Evidence basis

The [Lighting Management Specification](../../sources/openwebnet-public/pdf/WHO_24.pdf), pages 4–5, gives the notation and concrete two-endpoint examples.
