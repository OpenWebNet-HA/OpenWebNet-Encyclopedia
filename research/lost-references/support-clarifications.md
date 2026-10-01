# Official-support OpenWebNet clarifications

This note records statements relayed by Legrand community staff from internal support/MyHOME teams. They are secondary official-support evidence, not substitutes for publisher specifications.

## MH201 status feedback and session model

Legrand internal support clarified in 2026 that correct MH201 OpenWebNet communication requires both command and event sessions. The event session is specifically used to receive feedback to commands and status requests.

Internal support also recommends avoiding continuous polling of SCS objects: request status at communication startup, then monitor spontaneous status updates through the event session.

Source: `https://developer.legrand.com/forums/topic/mh201-openwebnet-status-feedback-not-returned-for-lighting-devices/`

## F460 and F461 OpenWebNet compatibility

Legrand internal support clarified:

- F460: Home + Control only, not OpenWebNet-compatible.
- F461: OpenWebNet-compatible, not for Home + Control use.
- MyHomeServer1 may coexist with F460 if used only as an OPEN gateway and not configured through Home + Project.

Source: `https://developer.legrand.com/forums/topic/information-on-myhome-server-f460-and-f461/`

## Lighting relay vs dimmer identification

Legrand support stated there is no direct OpenWebNet frame that declares whether a lighting object is a binary switch or dimmer.

Suggested probe:

`*#1*WHERE*1##`

If the object supports level control, it returns a DIMENSION 1 response containing a level; otherwise it returns normal ON/OFF status.

Source: `https://developer.legrand.com/forums/reply/12113/`

## WHO 4 DIMENSION 19 fan-coil values

The MyHOME team supplied missing DIMENSION 19 values:

- 14 - OFF speed 1
- 15 - OFF speed 2
- 16 - OFF speed 3

Source: `https://developer.legrand.com/forums/topic/openwebnet-thermoregulation-who4-dim19-clarifications/`

These statements should be cited as support clarifications and kept distinct from documented specification tables and physical-bus evidence.
