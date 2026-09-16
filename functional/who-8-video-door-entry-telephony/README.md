# Overview

`WHO 8` identifies the OpenWebNet Video Door Entry / Telephony system.

## Corpus status

The current integrated corpus establishes the namespace and its functional domain but does not yet support a complete authoritative `WHAT`, `WHERE`, and `DIMENSION` table at the level available for the dedicated `WHO 7` multimedia specification. Unsupported values therefore remain unspecified.

## Relationship to adjacent systems

[`WHO 6`](../who-6-basic-video-door-entry/) covers Basic Video Door Entry, while [`WHO 7`](../who-7-multimedia-video/) contains the published camera/video multimedia control vocabulary. `WHO 8` remains a separate namespace for Video Door Entry/telephony functions. Related function does not imply compatible numeric fields.

Parsers should dispatch on `WHO` before interpreting subsequent fields and must not reuse `WHO 7` camera commands or address semantics under `WHO 8` without direct evidence.

See [`../../protocol/`](../../protocol/) for common frame syntax.