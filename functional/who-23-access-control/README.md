# Overview

`WHO 23` identifies the OpenWebNet Access Control system.

## Protocol boundary

Access Control is a dedicated `WHO` namespace with its own addressing and functional semantics. It must not be interpreted using the A/PL grammar of Lighting/Automation or the zone/sensor grammar of Burglar Alarm merely because those systems may participate in the same installation.

## Corpus status

The current integrated corpus establishes the Access Control namespace and its use as a distinct functional/diagnostic domain, but does not yet provide enough supported ordinary functional traffic for a complete `WHAT`, `WHERE`, and `DIMENSION` table. Unsupported values remain unspecified.

Diagnostic Access Control traffic belongs to its diagnostic family (including the established `WHO 1023` domain) rather than to functional `WHO 23`. The numeric relationship between functional and diagnostic families does not make their frames interchangeable.

Implementations should retain undecoded `WHO 23` frames losslessly and add semantics only when supported by the implementation corpus, canonical specifications, or captures. See [`../../diagnostics/`](../../diagnostics/) for diagnostic protocol structure.