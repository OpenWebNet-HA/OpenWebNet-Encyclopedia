# Gateway Capabilities

This page describes the SCS/TCP external-interface `WHO 13` property surface. In that published interface model the target is the gateway itself and the property frames use an empty `WHERE` field.

The ZigBee OpenWebNet interface defines a different `WHO 13` management surface with additional `WHAT` values, a different `DIMENSION` set, and both empty and product-addressed `WHERE` forms. See [ZigBee Network Management](zigbee-network-management.md). Neither variant should be used to fill gaps in the other by numeric analogy.

## Functional model

The namespace provides five main capability groups.

| Group | Operations |
| --- | --- |
| Clock and calendar | Read/write time, read/write date, read/write combined date and time, including time-zone information |
| Network identity | Read IPv4 address, network mask, and MAC address |
| Hardware/product identity | Read gateway model / device type |
| Software identity | Read OpenWebNet firmware, kernel, and distribution versions |
| Runtime state | Read elapsed uptime since the last start-up |

The detailed payload definitions are documented in [`DIMENSION` Reference](dimensions.md).

## Command-session behavior

A property request is sent in a command session as:

`*#13**DIMENSION##`

The gateway answers with:

`*#13**DIMENSION*VALUE1*...*VALUEn##`

and the published examples show an `ACK` after the returned value.

For writable properties, the client sends:

`*#13**#DIMENSION*VALUE1*...*VALUEn##`

and the gateway returns `ACK` when the operation is accepted.

This follows the common OpenWebNet `DIMENSION` read/write distinction, but the available `DIMENSION` numbers and their payload schemas are specific to `WHO 13`.

## Monitor-session behavior

The published specification also shows the gateway value frames on a monitor session. A client may therefore encounter frames such as time, network identity, model, version, or uptime reports as server-originated monitor traffic rather than only as direct command-session replies.

A decoder should consequently treat a `WHO 13` value frame as a gateway property report independently of which session delivered it. Request/reply correlation belongs to the session layer.

## Clock management

Three related properties exist:

- `DIMENSION 0` - time plus time zone;
- `DIMENSION 1` - day of week and calendar date;
- `DIMENSION 22` - complete date and time in one payload.

All three are writable. `DIMENSION 22` carries time and calendar components in one frame. This avoids two separate submissions, but the specification does not establish transactional atomicity inside the gateway.

The protocol's time-zone encoding is an hour-offset representation rather than a named time-zone database identifier. Implementations should not infer daylight-saving rules from it; it carries the offset represented by the gateway.

## Network identity

`DIMENSION 10`, `11`, and `12` report the gateway's IP address, netmask, and MAC address respectively.

The payload is structured numerically: IPv4 and netmask values are four decimal octets, while the MAC address is six decimal octets. These fields should be parsed as component tuples rather than as arbitrary strings.

The published `WHO 13` interface exposes these properties as read-only. It therefore supports network identification, not IP configuration.

## Product identification

`DIMENSION 15` reports a numeric model identifier. The published table maps values to several historical external-interface products including MHServer, MH200, F452, F452V, MHServer2, and H4684.

This is a gateway model code, not a MyHOME Device Object ID and not the diagnostic object model returned by diagnostic `DIMENSION 1`. Implementations should keep those identifier spaces separate.

Because later gateways exist beyond the models listed in the original specification, an unknown numeric `MODEL` value should be retained as an unknown `WHO 13` model code rather than rejected.

## Software stack identification

Three independent version properties are defined:

| `DIMENSION` | Layer |
| ---: | --- |
| `16` | Device/OpenWebNet server firmware |
| `23` | Kernel |
| `24` | Distribution |

Each uses a three-component `V*R*B` payload for version, release, and build. Keeping these values separate is important: they describe different layers of the gateway software stack and should not be collapsed into a single firmware string.

## Uptime

`DIMENSION 19` reports elapsed days, hours, minutes, and seconds since the last gateway start-up. It provides a simple runtime-health signal and can be used to detect that a gateway has restarted between observations.

The published format is an elapsed-time tuple, not a boot timestamp. Deriving a boot time from it requires combining the value with an independently known current time and therefore belongs to application logic rather than the protocol representation.

## Relationship to transport and diagnostics

A gateway performs several roles that must remain separate in an implementation:

| Role | Namespace / layer |
| --- | --- |
| TCP connection and OpenWebNet session establishment | Protocol/session layer |
| Authentication and HMAC | Protocol/session layer |
| Generic `ACK` / `NACK` | Protocol/session layer |
| Gateway-local properties and clock management | Functional `WHO 13` |
| Gateway/device diagnostic operations | Diagnostic families such as `WHO 1013` |
| Functional traffic forwarded to the field bus | The corresponding functional `WHO` (`1`, `2`, `4`, etc.) |

`WHO 13` therefore describes the gateway as a manageable OpenWebNet endpoint; it does not replace the common gateway transport protocol and does not subsume the diagnostic protocol.