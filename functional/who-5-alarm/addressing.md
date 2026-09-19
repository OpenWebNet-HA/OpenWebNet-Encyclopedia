# Addressing

Published `WHO 5` `WHERE` values include:

| `WHERE` | Meaning |
| --- | --- |
| `1` | Control panel |
| `#0..#8` | Central zone `0..8` |
| `#1..#9` | Auxiliary `1..9` (`WHO 9` relationship in the published table) |
| `01..0n` | Input-zone device |
| `11..1n` | Zone 1 sensor |
| `81..8n` | Zone 8 sensor |
| `#12` | Zone C / AUX C |
| `#15` | Zone F / AUX F |

Zone `0` is used for inputs and the three internal sirens in the published model. Alarm addressing is therefore its own `WHO 5` grammar and must not be parsed as Lighting/Automation A/PL.
