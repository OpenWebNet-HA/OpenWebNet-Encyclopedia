# `WHO 22` — Sound Diffusion

`WHO 22` defines the later Multimedia / Sound Diffusion namespace. It provides explicit source, speaker, area and general addressing together with power, routing, tuner, track, RDS, tone, balance, preset and loudness functions.

## Reference

| Subject | Page |
| --- | --- |
| `WHAT`, structured `WHERE`, `DIMENSION` and functional behavior | [`reference.md`](reference.md) |

The target class is encoded in `WHERE`: a source, individual speaker, speaker area and general target use different forms. This makes address parsing part of operation semantics rather than a generic integer conversion.

Relative commands such as volume/tone increments coexist with absolute or structured `DIMENSION` state. State-tracking implementations should prefer reported absolute values where available rather than reconstructing them only from command history.

`WHO 22` is distinct from the earlier [`WHO 16`](../who-16-sound-system/) Sound System dialect. The [functional overview](../) groups them together for navigation without merging their protocol namespaces.