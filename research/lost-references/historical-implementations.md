# Historical OpenWebNet implementation lineage

This note records historical implementation sources that preserve protocol behavior but are not substitutes for publisher specifications.

## Flavio Crisciani / early Java connector lineage

An older OpenWebNet Java connector attributed to Flavio Crisciani survives in historical openHAB source forks under `com.myhome.fcrisciani`.

Preserved behavior includes:

- command session request `*99*0##`;
- monitor session request `*99*1##`;
- default OpenWebNet TCP port 20000;
- separate command and monitor sockets;
- synchronous command exchange and persistent monitor sessions.

An early openHAB binding explicitly credits both Mauro Cicolella's Freedomotic implementation and Flavio Crisciani's connector.

## Freedomotic OpenWebNet lineage

Freedomotic's OpenWebNet implementation preserves the same session model and several system initialization/status requests:

- Lighting: `*#1*0##`
- Automation: `*#2*0##`
- Burglar alarm: `*#5##`
- Power management: `*#3##`

The recovered Freedomotic plugin build dated 2016-01-30 defaults to `127.0.0.1:20000`, matching period reports of testing against the MyOpen VDK2 simulator.

Artifact SHA-256: `28ed89f68b32eddb00df4d5463a98cc7dab451876e64c2380ddf5d7261788980`.

## openwebnet4j

`mvalla/openwebnet4j` independently preserves the WHO 9 auxiliary WHAT table:

- 0 OFF
- 1 ON
- 2 TOGGLE
- 3 STOP
- 4 UP
- 5 DOWN
- 6 ENABLED
- 7 DISABLED
- 8 RESET_GEN
- 9 RESET_BI
- 10 RESET_TRI

It also implements `*9*1*WHERE##`, `*9*0*WHERE##`, and status request `*#9*WHERE##`.

These implementations corroborate historical behavior. Claims sourced from them must remain implementation evidence unless separately supported by a publisher document or observed traffic.
