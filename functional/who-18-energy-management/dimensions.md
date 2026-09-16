# `DIMENSION` Reference

Energy Management relies heavily on `DIMENSION` operations. Known identifiers include:

| `DIMENSION` | Meaning |
| ---: | --- |
| `51`–`54` | Energy totalizers |
| `71`–`73` | Energy-management actuator information/control |
| `113` | Active power |
| `250`–`263` | Stop&Go functions |
| `511`–`514` | Historical energy data |

The value tuple and units are defined by each `DIMENSION`; the identifier alone is not sufficient to determine the number or interpretation of returned values.

`WHO 18` is separate from the older [`WHO 3`](../who-3-load-management/) Load Management system. Implementations should not merge their `WHAT`, `WHERE`, or `DIMENSION` namespaces.