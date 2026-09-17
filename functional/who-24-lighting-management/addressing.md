# Addressing

`WHO 24` uses a structured sender/recipient `WHERE` rather than the `A`/`PL` grammar of `WHO 1`.

| Direction/role | Published form |
| --- | --- |
| Recipient | `LM_zone_num#dev_type&sys_addr` |
| Sender | `#00#LM_zone_num#dev_type&sys_addr` |

The separators are structural. Parsers should preserve the three components rather than flattening the expression into a number.

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

`sys_addr` uses the published range `1`–`9`. It is a Lighting Management system-address component and must not be interpreted as an SCS `A` or `PL` configurator.

## Sender versus recipient

The `#00#` sender prefix changes the semantic role of the address. Sender and recipient forms should therefore be represented separately in an implementation even when their zone, device-type and system-address components match.

This address grammar is one of the principal reasons `WHO 24` must remain separate from ordinary [`WHO 1`](../who-1-lighting/) Lighting.