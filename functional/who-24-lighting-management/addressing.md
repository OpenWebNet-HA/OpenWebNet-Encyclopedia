# Addressing

`WHO 24` uses a sender/recipient structure.

The published recipient form is `LM_zone_num#dev_type&sys_addr`; the sender form is `#00#LM_zone_num#dev_type&sys_addr`.

## Components

| Component | Known values |
| --- | --- |
| `LM_zone_num` | `0` no zones; `1000 + zone number` selected zone; `1000` every zone |
| `dev_type` | `1` BMNE500/002645; `99991` Lighting Console; `9991` Virtual Configurator; `4` broadcast; `8` unknown |
| `sys_addr` | `1`–`9` |

The published value `8` for `dev_type` is explicitly unidentified and remains documented as unknown rather than assigned an inferred device role.