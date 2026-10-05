# Earlier-device EAN backfill review

Review date: `2026-10-05`.

Scope: `OWN-DEV-0001..OWN-DEV-0115`. This pass checks commercial EAN evidence; Device definitions and queue selection are unchanged.

## Incorporated evidence

The review adds **121 explicit SKU/EAN-13 relationships to 44 existing Device definitions**. Individual physical references have separate rows, including named members of grouped catalogue codes. All 121 codes pass the EAN-13 check digit calculation. Each row cites an exact manufacturer commercial record, with its archived original and page locator.

**109 new original manufacturer PDF exports** were uploaded, their archived SHA-256 fingerprints and sizes verified, and their manifest entries individually registered and pushed on `main` before incorporation. Twelve EAN relationships reuse already registered originals. The source index records every incorporated relationship.

The earlier catalogue contains 414 distinct written reference labels. Normalising manufacturer reference spacing and expanding explicit physical groups produces 473 reference spellings for this review. Legacy `_OLD` catalogue markers remain separate from later physical references and have no inferred EAN. No EAN is inferred from a neighbouring SKU or from a barcode prefix. The catalogue itself has no EAN field. A source-specific EAN does not establish that an installed Device has the same hardware or firmware revision as the current commercial record.

## Remaining archival action

A further **26 exact SKU/EAN relationships** were located in original Legrand product web pages. Their original response bytes are preserved in the local review checkpoint. These records have not been incorporated because the installed public archive uploader accepts PDF originals only; executing the proposed HTML uploader requires host administrator setup. The pages affected are marked below. Their catalogue identities remain established.

Other references have no exact EAN record established by the retained originals and the manufacturer catalogue searches in this pass. Manufacturer lookup failures, missing commercial fields and searches returning a different reference are not evidence that a product lacks an EAN.

## Device-by-device coverage

| Device | References considered | EAN rows incorporated | Review result |
| --- | ---: | ---: | --- |
| [OWN-DEV-0001](../../devices/definitions/own-dev-0001-two-channel-universal-dimmer.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0002](../../devices/definitions/own-dev-0002-audio-video-web-server-gateway.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0003](../../devices/definitions/own-dev-0003-flush-mounted-actuator-free-control.md) | 9 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0004](../../devices/definitions/own-dev-0004-two-module-basic-control.md) | 19 | 3 | EANs added for 3 reference(s); 3 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0005](../../devices/definitions/own-dev-0005-two-module-special-control.md) | 13 | 3 | EANs added for 3 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0006](../../devices/definitions/own-dev-0006-two-module-zero-crossing-actuator-control.md) | 7 | 3 | EANs added for 3 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0007](../../devices/definitions/own-dev-0007-three-module-basic-control.md) | 6 | 3 | EANs added for 3 reference(s) |
| [OWN-DEV-0008](../../devices/definitions/own-dev-0008-flush-mounted-one-relay-actuator.md) | 6 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0009](../../devices/definitions/own-dev-0009-four-zone-touch-multifunction-control.md) | 15 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0010](../../devices/definitions/own-dev-0010-pir-us-daylight-presence-sensor.md) | 16 | 10 | EANs added for 10 reference(s); 2 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0011](../../devices/definitions/own-dev-0011-scenario-control.md) | 14 | 6 | EANs added for 6 reference(s); 2 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0012](../../devices/definitions/own-dev-0012-four-channel-ir-receiver.md) | 12 | 6 | EANs added for 6 reference(s) |
| [OWN-DEV-0013](../../devices/definitions/own-dev-0013-video-display.md) | 8 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0014](../../devices/definitions/own-dev-0014-extended-control.md) | 8 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0015](../../devices/definitions/own-dev-0015-myhome-screen-3-5.md) | 8 | 1 | EANs added for 1 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0016](../../devices/definitions/own-dev-0016-pir-flush-mounted-sensor.md) | 12 | 8 | EANs added for 8 reference(s); 2 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0017](../../devices/definitions/own-dev-0017-flush-mounted-temperature-central-unit.md) | 10 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0018](../../devices/definitions/own-dev-0018-local-display.md) | 10 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0019](../../devices/definitions/own-dev-0019-three-module-touch-control.md) | 7 | 3 | EANs added for 3 reference(s) |
| [OWN-DEV-0020](../../devices/definitions/own-dev-0020-load-control-panel.md) | 10 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0021](../../devices/definitions/own-dev-0021-one-relay-din-actuator-16-a.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0022](../../devices/definitions/own-dev-0022-two-relay-din-actuator-10-a.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0023](../../devices/definitions/own-dev-0023-four-relay-din-actuator.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0024](../../devices/definitions/own-dev-0024-two-module-soft-touch-control.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0025](../../devices/definitions/own-dev-0025-din-dimmer-1000-w.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0026](../../devices/definitions/own-dev-0026-four-scenario-control-unit.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0027](../../devices/definitions/own-dev-0027-flush-mounted-dimmer.md) | 4 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0028](../../devices/definitions/own-dev-0028-rotary-regulation-control.md) | 6 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0029](../../devices/definitions/own-dev-0029-radio-receiver-interface.md) | 9 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0030](../../devices/definitions/own-dev-0030-ballast-din-dimmer-1-10-v.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0031](../../devices/definitions/own-dev-0031-pir-surface-ceiling-mounted-sensor.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0032](../../devices/definitions/own-dev-0032-transmitting-radio-interface.md) | 6 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0033](../../devices/definitions/own-dev-0033-light-manager-control-unit.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0034](../../devices/definitions/own-dev-0034-radio-interface-temperature-probes.md) | 6 | 6 | EANs added for 6 reference(s) |
| [OWN-DEV-0035](../../devices/definitions/own-dev-0035-flush-mounted-radio-receiver-batteryless-control.md) | 6 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0036](../../devices/definitions/own-dev-0036-key-card-switch.md) | 6 | 2 | EANs added for 2 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0037](../../devices/definitions/own-dev-0037-local-display-1-2-bus.md) | 10 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0038](../../devices/definitions/own-dev-0038-probe-with-regulation.md) | 10 | 7 | EANs added for 7 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0039](../../devices/definitions/own-dev-0039-key-card-switch-rfid.md) | 6 | 2 | EANs added for 2 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0040](../../devices/definitions/own-dev-0040-fan-coil-probe.md) | 9 | 6 | EANs added for 6 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0041](../../devices/definitions/own-dev-0041-basic-temperature-probe.md) | 9 | 6 | EANs added for 6 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0042](../../devices/definitions/own-dev-0042-temperature-control-central-unit.md) | 4 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0043](../../devices/definitions/own-dev-0043-special-functions-control.md) | 4 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0044](../../devices/definitions/own-dev-0044-shutter-control-bus.md) | 4 | 3 | EANs added for 3 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0045](../../devices/definitions/own-dev-0045-shutter-actuator-bus.md) | 4 | 3 | EANs added for 3 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0046](../../devices/definitions/own-dev-0046-display-thermostat-2-modules.md) | 4 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0047](../../devices/definitions/own-dev-0047-myhome-screen-10.md) | 4 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0048](../../devices/definitions/own-dev-0048-energy-display-2-modules.md) | 4 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0049](../../devices/definitions/own-dev-0049-myhome-screen-10-capacitive.md) | 4 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0050](../../devices/definitions/own-dev-0050-classe-300x.md) | 4 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0051](../../devices/definitions/own-dev-0051-pir-ceiling-mounted-sensor.md) | 2 | 1 | EANs added for 1 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0052](../../devices/definitions/own-dev-0052-ballast-din-dimmer-0-10-v.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0053](../../devices/definitions/own-dev-0053-ultrasonic-ceiling-sensor-ir-port.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0054](../../devices/definitions/own-dev-0054-pir-us-ceiling-mounted-sensor.md) | 2 | 1 | EANs added for 1 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0055](../../devices/definitions/own-dev-0055-pir-us-wall-mounted-sensor.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0056](../../devices/definitions/own-dev-0056-pir-wall-mounted-sensor-straight-range.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0057](../../devices/definitions/own-dev-0057-pir-wall-mounted-sensor-short-range.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0058](../../devices/definitions/own-dev-0058-pir-wall-mounted-sensor-dual-range.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0059](../../devices/definitions/own-dev-0059-basic-actuator.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0060](../../devices/definitions/own-dev-0060-basic-control-actuator.md) | 1 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0061](../../devices/definitions/own-dev-0061-pir-wall-mounted-sensor-long-range.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0062](../../devices/definitions/own-dev-0062-daylight-sensor-room-controller-rj45.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0063](../../devices/definitions/own-dev-0063-occupancy-sensor-ir-zigbee.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0064](../../devices/definitions/own-dev-0064-room-controller-2-output-16-a.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass; 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0065](../../devices/definitions/own-dev-0065-memory-module.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0066](../../devices/definitions/own-dev-0066-scenario-module.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0067](../../devices/definitions/own-dev-0067-four-relay-din-actuator-16-a.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0068](../../devices/definitions/own-dev-0068-one-module-one-relay-actuator.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0069](../../devices/definitions/own-dev-0069-scs-dali-gateway.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0070](../../devices/definitions/own-dev-0070-din-contacts-interface.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0071](../../devices/definitions/own-dev-0071-module-contacts-interface.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0072](../../devices/definitions/own-dev-0072-basic-contacts-interface.md) | 3 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0073](../../devices/definitions/own-dev-0073-din-dimmer-1000-va.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0074](../../devices/definitions/own-dev-0074-din-dimmer-2x400-va.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0075](../../devices/definitions/own-dev-0075-room-controller-4-output-0-10-v.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass; 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0076](../../devices/definitions/own-dev-0076-room-controller-2-universal-dimming-outputs.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0077](../../devices/definitions/own-dev-0077-multi-application-room-controller.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass; 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0078](../../devices/definitions/own-dev-0078-scs-scs-interface.md) | 2 | 1 | EANs added for 1 reference(s) |
| [OWN-DEV-0079](../../devices/definitions/own-dev-0079-room-controller-2-output-0-10-v.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass; 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0080](../../devices/definitions/own-dev-0080-scenario-programmer.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0081](../../devices/definitions/own-dev-0081-1-relay-din-actuator-16-a-100-240-v.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0082](../../devices/definitions/own-dev-0082-room-controller-1-output-16-amps.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0083](../../devices/definitions/own-dev-0083-2-relay-din-actuator-16-a-100-240-v.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0084](../../devices/definitions/own-dev-0084-ip55-pir-wall-mounted-sensor.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0085](../../devices/definitions/own-dev-0085-burglar-alarm-central-unit-with-communicator.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0086](../../devices/definitions/own-dev-0086-polyx-alarm.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0087](../../devices/definitions/own-dev-0087-gsm-burglar-alarm-central-unit.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0088](../../devices/definitions/own-dev-0088-flush-mounted-alarm-central-unit.md) | 6 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0089](../../devices/definitions/own-dev-0089-webserver-audio-video-din.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0090](../../devices/definitions/own-dev-0090-enhanced-webserver.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0091](../../devices/definitions/own-dev-0091-stop-go.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0092](../../devices/definitions/own-dev-0092-stop-go-btest.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0093](../../devices/definitions/own-dev-0093-stop-go-plus.md) | 1 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0094](../../devices/definitions/own-dev-0094-touch-control.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0095](../../devices/definitions/own-dev-0095-burglar-alarm-central-unit-with-communicator.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0096](../../devices/definitions/own-dev-0096-pulses-counter-interface.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0097](../../devices/definitions/own-dev-0097-video-station.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0098](../../devices/definitions/own-dev-0098-shutter-flush-mounted-actuator.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0099](../../devices/definitions/own-dev-0099-flush-mounted-leading-dimmer-300-va.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0100](../../devices/definitions/own-dev-0100-stereo-control.md) | 2 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0101](../../devices/definitions/own-dev-0101-eight-output-din-actuator-16-a.md) | 2 | 1 | EANs added for 1 reference(s); 1 exact web record(s) awaiting original HTML archival |
| [OWN-DEV-0102](../../devices/definitions/own-dev-0102-multimedia-touch-screen.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0103](../../devices/definitions/own-dev-0103-eight-key-multifunction-control.md) | 3 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0104](../../devices/definitions/own-dev-0104-do-not-disturb-make-up-room-control.md) | 3 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0105](../../devices/definitions/own-dev-0105-do-not-disturb-make-up-room-indicator.md) | 3 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0106](../../devices/definitions/own-dev-0106-rfid-reader-and-outside-door-indicator.md) | 3 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0107](../../devices/definitions/own-dev-0107-legrand-multimedia-touch-screen.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0108](../../devices/definitions/own-dev-0108-classe-300-v13e-v13m.md) | 3 | 2 | EANs added for 2 reference(s) |
| [OWN-DEV-0109](../../devices/definitions/own-dev-0109-living-now-thermostat-with-display.md) | 3 | 3 | EANs added for 3 reference(s) |
| [OWN-DEV-0110](../../devices/definitions/own-dev-0110-two-module-myhome-unified-control.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0111](../../devices/definitions/own-dev-0111-three-module-myhome-unified-control.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0112](../../devices/definitions/own-dev-0112-myhome-lighting-command-actuator.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0113](../../devices/definitions/own-dev-0113-myhome-shutter-command-actuator.md) | 3 | 0 | No archived exact SKU/EAN pair established in this pass |
| [OWN-DEV-0114](../../devices/definitions/own-dev-0114-living-now-light-digital-control.md) | 3 | 3 | EANs added for 3 reference(s) |
| [OWN-DEV-0115](../../devices/definitions/own-dev-0115-living-now-full-digital-control.md) | 3 | 3 | EANs added for 3 reference(s) |
