# `WHO 13` - Integration and Gateway Functions

`WHO 13` covers Integration / Gateway functions. The namespace has three source-scoped roles that must remain distinct:

1. the published SCS/TCP OpenWebNet External interface device API, which exposes gateway-local clock, network identity, model, software-version, and uptime information;
2. the MyHOME_Suite `OPEN.db` Integration Functions model, which associates `WHO 13` with F422 interface modes and diagnostic family `WHO 1013`;
3. the ZigBee OpenWebNet interface, which defines a separate `WHO 13` network-management, product-database, and product-property surface.

These roles share the numeric namespace but do not automatically share `WHERE` grammar, `WHAT` values, `DIMENSION` sets, transport behavior, or Device support.

## Reference

| Subject | Page |
| --- | --- |
| SCS/TCP gateway capabilities and frame model | [Gateway Capabilities](capabilities.md) |
| SCS/TCP `DIMENSION` values, payloads, and access modes | [`DIMENSION` Reference](dimensions.md) |
| ZigBee network management, product inventory, and properties | [ZigBee Network Management](zigbee-network-management.md) |
| Cross-namespace MyHOME_Suite `OPEN.db` evidence | [MyHOME_Suite `OPEN.db` Coverage](../open-db-coverage.md) |

## SCS/TCP gateway capability groups

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

This surface supports gateway discovery and inventory, network identification, software/firmware reporting, clock synchronisation, and operational-health information such as uptime.

## Integration-interface model in `OPEN.db`

The MyHOME_Suite `EN_SYSTEM` row `id_system = 26` names the system **Integration Functions**, assigns functional `WHO 13`, diagnostic `WHO 1013`, and marks it as managed.

`OPEN.db` does not associate ordinary `EN_OPEN` command templates directly with this system, so the database does not provide an additional functional `WHAT` or `DIMENSION` table. It does, however, associate two concrete `EN_ADDRESS_RULE` definitions with the system:

| F422 interface mode | Virtual `WHERE` form | Advanced form |
| --- | --- | --- |
| Burglar alarm interface | `[I4]` | `[I4]` |
| Galvanic separation / New physical separation | `[I4]` | `[I4]` |

This is significant: the implementation model treats `WHO 13` as more than a set of IP-gateway information registers. It is also the Integration Functions namespace used by MyHOME_Suite for F422 interface configurations. The database establishes the interface modes and address grammar, but it does not by itself establish additional command semantics for those modes.

## Scope

`WHO 13` must not be conflated with the transport session used to connect to an IP gateway. TCP connection establishment, command/monitor sessions, authentication, HMAC, and generic `ACK` / `NACK` handling are common OpenWebNet transport concerns and are documented under [Protocol](../../protocol/).

It is also distinct from diagnostic `WHO 1013`. The latter is the diagnostic family assigned by MyHOME_Suite to the Integration Functions system; the numeric relationship does not make diagnostic operations part of the functional `WHO 13` vocabulary.

The published SCS/TCP `WHO 13` specification calls this system the **External interface device**. The MyHOME_Suite `OPEN.db` definitions call it **Integration Functions**. The ZigBee specification defines a third, interface-specific management role documented in [ZigBee Network Management](zigbee-network-management.md). These views remain separate where their wire grammars or applicability differ.
