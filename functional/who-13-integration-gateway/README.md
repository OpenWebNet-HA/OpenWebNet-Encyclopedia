# Overview

`WHO 13` is the OpenWebNet namespace for the external interface / gateway device itself. It exposes gateway-local information and management functions rather than the state of the SCS Devices reached through that gateway.

The published protocol defines a compact but important management interface: clock and calendar access, network identity, gateway model identification, software-version information, and uptime. Time, date, and combined date/time can also be written.

## Reference

| Subject | Page |
| --- | --- |
| Gateway capabilities and frame model | [`capabilities.md`](capabilities.md) |
| `DIMENSION` values, payloads, and access modes | [`dimensions.md`](dimensions.md) |

## Capability groups

| Capability | `DIMENSION` | Access |
| --- | ---: | --- |
| Time and time zone | `0` | Read / write |
| Date | `1` | Read / write |
| IP address | `10` | Read |
| Network mask | `11` | Read |
| MAC address | `12` | Read |
| Gateway model / device type | `15` | Read |
| OpenWebNet server firmware version | `16` | Read |
| Uptime | `19` | Read |
| Combined date and time | `22` | Read / write |
| Kernel version | `23` | Read |
| Distribution version | `24` | Read |

This makes `WHO 13` useful for gateway discovery and inventory, network identification, software/firmware reporting, clock synchronisation, and operational-health information such as uptime.

## Scope

`WHO 13` must not be conflated with the transport session used to connect to an IP gateway. TCP connection establishment, command/monitor sessions, authentication, HMAC, and generic `ACK` / `NACK` handling are common OpenWebNet transport concerns and are documented under [`../../protocol/`](../../protocol/).

It is also distinct from diagnostic `WHO 1013`. The latter belongs to the diagnostic namespace; the numeric relationship does not make diagnostic operations part of the functional `WHO 13` gateway-management vocabulary.

The published `WHO 13` specification calls this system the **External interface device**. The MyHOME_Suite `OPEN.db` definitions represent `WHO 13` as the Integration / Gateway functional system. These are complementary descriptions of the same functional namespace.