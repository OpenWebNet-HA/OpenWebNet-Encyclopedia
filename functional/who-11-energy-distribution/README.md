# `WHO 11` - Energy Distribution

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 11` as Energy distribution.

## Protocol boundary

`WHO 11` is distinct from both [`WHO 3`](../who-3-load-management/) Load Management and [`WHO 18`](../who-18-energy-management/) Energy Management. These three namespaces occupy related electrical-energy domains but represent separate protocol systems.

`WHO 18` measurements such as active power, totalizers, actuator information and historical energy must not be exposed under `WHO 11` unless direct evidence establishes an equivalent operation. Likewise, `WHO 3` load-management states are not `WHO 11` values.

## Corpus status

The implementation data establishes the Energy distribution namespace but does not yet provide a complete supported `WHAT`, `WHERE`, or `DIMENSION` table. The canonical public PDF set used by this repository does not contain a dedicated `WHO 11` functional specification.

Implementations should therefore recognize the namespace, preserve unknown frames losslessly, and add field semantics only from direct implementation or wire evidence.