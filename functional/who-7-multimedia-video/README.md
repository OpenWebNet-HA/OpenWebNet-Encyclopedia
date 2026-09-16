# Overview

`WHO 7` defines the published Multimedia System functions used to control camera/video resources associated with the Video Door Entry catalogue. It is a control namespace for video reception, resource release, camera image adjustment and display selection.

## Established `WHAT` families

| `WHAT` | Function |
| ---: | --- |
| `0` | Receive video |
| `9` | Free audio/video resources |
| `120` / `121` | Zoom in / zoom out |
| `130` / `131` | Move zoom centre on the X axis |
| `140` / `141` | Move zoom centre on the Y axis |
| `150` / `151` | Increase / decrease luminosity |
| `160` / `161` | Increase / decrease contrast |
| `170` / `171` | Increase / decrease colour |
| `180` / `181` | Increase / decrease image quality |
| `31x`, `32x`, `33x`, … | Select/display DIAL positions defined by the multimedia specification |

The paired adjustment values represent relative operations. A decoder should retain the exact `WHAT` rather than collapsing each pair into an unsigned generic adjustment.

## Resource model

Video operations interact with shared audio/video resources. `WHAT 0` requests video reception while `WHAT 9` releases the associated resources. Resource lifetime is therefore part of correct client behavior; image-adjustment commands should be interpreted in the context of the selected/active video resource.

## Camera adjustment

Zoom, X/Y positioning, luminosity, contrast, colour and image-quality operations form independent control axes. The X/Y operations move the central portion of the image used for zooming; they are not absolute pixel coordinates.

## Display selection

The `3xx` family selects display DIAL entries. The decimal structure carries row/position information defined by the published multimedia grammar. Implementations should parse the family structurally rather than treating every `3xx` value as an unrelated command.

`WHO 7` remains distinct from Basic Video Door Entry [`WHO 6`](../who-6-basic-video-door-entry/), Video Door Entry/Telephony [`WHO 8`](../who-8-video-door-entry-telephony/), and the sound namespaces [`WHO 16`](../who-16-sound-system/) and [`WHO 22`](../who-22-sound-diffusion/).