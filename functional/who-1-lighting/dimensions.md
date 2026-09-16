# `DIMENSION` Reference

Known Lighting `DIMENSION` identifiers include:

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Lighting level and transition speed |
| `2` | Temporization |
| `3` | Required-only-ON operation |
| `4` | 100-level status |
| `8` | Lamp working-time information |
| `9` | Lamp working-time information |

## Level and speed

MyHOME_Suite 3.5.38 uses the write form `*#1*WHERE*#1*LEVEL*SPEED##` for `DIMENSION 1`.

## Temporization

MyHOME_Suite 3.5.38 uses `*#1*WHERE*#2*HOURS*MINUTES*SECONDS##` for `DIMENSION 2`.

Read requests and responses follow the common `DIMENSION` frame classes documented in [`../../protocol/dimensions.md`](../../protocol/dimensions.md). Read and write support are capabilities of the target operation and must not be assumed solely from the existence of a `DIMENSION` identifier.