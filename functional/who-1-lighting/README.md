# Overview

`WHO 1` defines the OpenWebNet Lighting system. It covers switching, dimming, timed and blinking operations, status reporting, and lighting-specific `DIMENSION` operations.

## Reference

| Subject | Page |
| --- | --- |
| Commands and states | [`what.md`](what.md) |
| `WHERE` forms | [`addressing.md`](addressing.md) |
| `DIMENSION` operations | [`dimensions.md`](dimensions.md) |

Ordinary command/status frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`. `DIMENSION` operations use the common frame classes defined in [`../../protocol/dimensions.md`](../../protocol/dimensions.md).

Lighting Management is a distinct protocol namespace under [`WHO 24`](../who-24-lighting-management/).