# `WHO 7` - Multimedia System

`WHO 7` controls cameras from the Video Door Entry catalogue: video-resource acquisition/release, image adjustment, and display DIAL selection.

## `WHAT` values

| `WHAT` | Function |
| ---: | --- |
| `0` | Receive video |
| `9` | Release audio/video resources |
| `120` / `121` | Zoom in / out |
| `130` / `131` | Increase / decrease zoom-centre X coordinate |
| `140` / `141` | Increase / decrease zoom-centre Y coordinate |
| `150` / `151` | Increase / decrease luminosity |
| `160` / `161` | Increase / decrease contrast |
| `170` / `171` | Increase / decrease colour |
| `180` / `181` | Increase / decrease image quality |
| `311`–`344` | Select DIAL row `1`–`4`, position `1`–`4` |

The adjustment operations are relative. The `3RC` family is structural: `R` selects DIAL row and `C` selects position, both `1`–`4`.

## Camera addressing

The published `WHERE` table lists cameras `4000`–`4099`, with the final two digits identifying camera `00`–`99`.

Individual command-flow tables state `WHERE=[4000-5000]`, which conflicts with the explicit address table. This documentation treats `4000`–`4099` as the established enumerated range and records the broader command-note range as a source inconsistency, not as proof that every value through `5000` is a camera.

## Frame shape

The dedicated specification prints command/event frames with a trailing empty tag:

~~~text
*7*WHAT*WHERE*##
~~~

It also prints resource release as `*7*9**##`, with no camera address. An implementation targeting this dialect should preserve the empty field rather than normalizing blindly to the common three-tag form.

The gateway answers commands with `ACK` or `NACK`. Adjustment and DIAL operations are meaningful only in the context of an acquired/active video resource.

## Resource lifecycle

1. Request video with `WHAT 0` for the selected camera.
2. Apply zoom, position, image, or DIAL operations as supported.
3. Release audio/video resources with `WHAT 9`.

`WHAT 9` is resource management, not a camera OFF state.

## Namespace boundary

`WHO 7` remains distinct from Basic Video Door Entry [`WHO 6`](../who-6-basic-video-door-entry/), Video Door Entry/Telephony [`WHO 8`](../who-8-video-door-entry-telephony/), and sound [`WHO 16`](../who-16-sound-system/) / [`WHO 22`](../who-22-sound-diffusion/).

## Evidence basis

Values, addresses, trailing-empty-tag frames, and command sequences come from [`WHO_7.pdf`](../../sources/openwebnet-public/pdf/WHO_7.pdf). The source's address-range discrepancy is retained explicitly.
