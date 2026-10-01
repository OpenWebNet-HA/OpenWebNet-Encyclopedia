# Door-entry protocol recovery

This note tracks recoverable OpenWebNet-specific evidence for the poorly preserved door-entry families. It deliberately separates legacy WHO 6 material from modern WHO 8 traffic.

## WHO 6 - legacy video door-entry

The original community document is known by the historical title `OpenWebNet_Community_DoorEntry` / `WHO_6.pdf`, version 1.0.0 (2006), but its original bytes have not yet been recovered.

Independent implementations preserve a consistent command subset:

| Function | Frame template | Evidence |
| --- | --- | --- |
| Indoor camera ON | `*6*0*WHERE##` | legacy openHAB VDES binding |
| Riser camera ON | `*6*0*WHERE#2##` | legacy openHAB VDES binding |
| Camera OFF | `*6*9##` | legacy openHAB VDES binding |
| Staircase light ON | `*6*12*WHERE##` | legacy openHAB VDES binding |
| Staircase light OFF | `*6*11*WHERE##` | legacy openHAB VDES binding |
| Door lock activation | `*6*10*WHERE##` | legacy openHAB VDES binding |
| Riser door lock activation | `*6*10*WHERE#2##` | legacy openHAB VDES binding |
| Door lock activation by numeric door id | `*6*10*<4000+doorId>##` | `michnovka/openwebnet-php` |

Implementation sources:

- `lolarchives/Zoo`, `addons/binding/org.openhab.binding.openwebnetvdes/.../DeviceFeatureType.java`
- `michnovka/openwebnet-php`, `src/OpenWebNetDoorLock.php`

These implementations corroborate the lost WHO 6 family but do not replace the missing original specification.

## WHO 8 - newer door-entry / intercom signaling

No public standalone WHO 8 specification has been recovered. Period community discussion explicitly describes WHO 8 as undocumented publicly while noting that old MyOpen forum material existed.

Multiple independent modern implementations and live-device captures converge on the following behavior:

- Unlock/actuator press: `*8*19*WHERE##`.
- Unlock/actuator release: `*8*20*WHERE##`.
- Exterior call/session start frames begin `*8*1#1#4#...`.
- Interior self-view/session start frames begin `*8*1#5#4#...`.
- Ring notification uses `*8*9#1#4*...` for exterior origin.
- Answer/two-way session uses `WHAT=2`.
- Hang-up/end uses `WHAT=3`.
- Audio/call phase is also exposed through dimension/status family `*#8**35*V*0*0##`.

Corroborating implementation sources:

- `fquinto/bticinoClasse300x`, especially `bticino_bridge/pkg/openwebnet/command.go`, `pkg/bticino/constants.go`, and multicast handlers.
- `r0bb10/BTicino-GO-Companion`, `internal/openwebnet/frames.go`.
- `jorgeavlobo/bticino-classe100x-ha`, `docs/PROTOCOL.md`.

These are implementation and observed-device evidence. WHERE values and composite fields are installation/device dependent and must not be generalized beyond the evidence.

## Recovery status

- WHO 6 original/community PDF: identified, original bytes still missing.
- WHO 8 public specification: not identified; old forum material remains the likely historical source.
- MyOpen OWN index confirms additional historical document IDs, including `35509` in the December 2011 batch. Its page capture still needs recovery from an alternate mirror or filename.
- VDK package remains unrecovered. Period sources independently confirm the MyOpen-distributed Virtual Development Kit, localhost OpenWebNet endpoint `127.0.0.1:20000`, and an `own-manifest` configuration file.
