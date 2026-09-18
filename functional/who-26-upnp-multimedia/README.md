# `WHO 26` — UPnP Multimedia

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 26` as a UPnP multimedia command namespace.

## Protocol position

`WHO 26` belongs to the broader multimedia area but remains independent from camera/video [`WHO 7`](../who-7-multimedia-video/), Sound System [`WHO 16`](../who-16-sound-system/), and Sound Diffusion [`WHO 22`](../who-22-sound-diffusion/). Shared concepts such as media, source, playback, or navigation do not imply shared numeric encodings.

## Corpus status

The current implementation corpus establishes the namespace but does not yet support a complete system-specific `WHAT`, `WHERE`, or `DIMENSION` reference. No public dedicated `WHO 26` specification is present in the canonical PDF set used by this repository.

Parsers should therefore preserve `WHO 26` traffic losslessly and expose unknown fields as raw values. Semantics from `WHO 7`, `16`, or `22` must not be copied into this namespace without direct evidence.

This page intentionally records the strongest established model rather than filling the missing vocabulary by analogy.