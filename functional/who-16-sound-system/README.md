# `WHO 16` — Sound System

`WHO 16` defines the original OpenWebNet Sound System namespace. It combines amplifier and source control with tuner, RDS, volume, tone, balance and media-navigation functions.

## Reference

| Subject | Page |
| --- | --- |
| `WHAT`, `WHERE`, `DIMENSION`, command families and target model | [`reference.md`](reference.md) |

The protocol distinguishes amplifier targets from source targets and provides both relative operations (`WHAT` families such as volume/frequency/track increments) and absolute or structured information through `DIMENSION` operations.

Several `WHAT` ranges encode a magnitude directly in the command number. Implementations should parse those families structurally rather than maintaining hundreds of unrelated constants.

Sound Diffusion also exists under the distinct [`WHO 22`](../who-22-sound-diffusion/) namespace. Although the two systems share concepts such as source, volume and frequency, their wire grammars are different and numeric values must not be translated between them by position alone.