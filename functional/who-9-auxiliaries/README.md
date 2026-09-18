# `WHO 9` - Auxiliaries

`WHO 9` defines the OpenWebNet Auxiliaries system. Auxiliary channels provide general-purpose binary/event functions that can also appear as references from other systems, including the published `WHO 5` Alarm addressing model.

## Namespace semantics

`WHAT`, `WHERE`, and any structured values are scoped to `WHO 9`. An auxiliary number is not an Automation `A`/`PL` address and should not be normalized as one.

The Alarm specification's references to AUX targets demonstrate cross-system use of auxiliary channels, but do not make `WHO 9` part of the Alarm namespace. Integrations should preserve the originating `WHO` when correlating such events.

## Corpus status

The current integrated corpus establishes the Auxiliaries namespace and its use by MyHOME_Suite, but does not justify a complete independent `WHAT`/`DIMENSION` table beyond supported implementation evidence. Unknown values remain unspecified rather than inferred from generic binary-control behavior.

See [Protocol](../../protocol/) for common frame syntax and [`WHO 5` - Alarm](../who-5-alarm/) for Alarm-side AUX references.