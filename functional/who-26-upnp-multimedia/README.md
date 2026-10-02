# `WHO 26` - UPnP Multimedia

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 26` as a UPnP multimedia command namespace.

## Protocol position

`WHO 26` belongs to the broader multimedia area but remains independent from camera/video [`WHO 7`](../who-7-multimedia-video/), Sound System [`WHO 16`](../who-16-sound-system/), and Sound Diffusion [`WHO 22`](../who-22-sound-diffusion/). Shared concepts such as media, source, playback, or navigation do not imply shared numeric encodings.

## Corpus status

The current implementation corpus establishes the namespace but does not yet support a complete system-specific `WHAT`, `WHERE`, or `DIMENSION` reference. No public dedicated `WHO 26` specification is present in the canonical PDF set used by this repository.

Parsers should therefore preserve `WHO 26` traffic losslessly and expose unknown fields as raw values. Semantics from `WHO 7`, `16`, or `22` must not be copied into this namespace without direct evidence.

## Historical OpenXml client

The BTicino touchscreen library at `TS10_1_0_23` implements a separate local OpenXml media service. Its [UTF-8 envelope and framing](../../protocol/stream-parsing.md#separate-multimedia-xml-transport) are distinct from numeric OpenWebNet frames. The following XML tags are verified in its serializers and response tests; they do not establish corresponding numeric `WHAT` values or support by external gateways.

| XML request | Arguments | Response tag and decoded content |
| --- | --- | --- |
| `RW26C1` | None | `AW26C1`: `server/name` list |
| `RW26C2` | `id` | `AW26C2`: selected `current_server`, directory `status_browse`, or selected track's `DIDL-Lite` metadata |
| `CW26C7` | None | `AW26C7`: parent-directory browsing result |
| `CW26C10` / `CW26C11` | None | `AW26C10` / `AW26C11`: next / previous track metadata |
| `RW26C15` | `rank`, `delta` | `AW26C15`: `total`, `rank`, directory names and track records |
| `CW26C16` | `server`, slash-joined `path` | `AW26C16`: navigation-context result |

Selection uses the same `id` argument for a server, directory or file. Tested browsing outcomes include `browse_okay`, `empty_directory`, `already_at_root` and `no_such_directory`, depending on the operation. Track records contain a resource URL and, for audio, title, artist, album and duration. XML error text is mapped into local application errors; those enum numbers are not wire return codes.

See [OpenXml service evidence](../../project/review/myopencommunity-coverage-audit.md#openxml-media-vocabulary).
