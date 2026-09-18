# Rejected Relationships

Rejected interpretations are retained because they are easy to rediscover from names or coincident integers.

## Database relationships

| Proposed relationship | Reason rejected |
| --- | --- |
| `EN_DEVICE.code → EN_LANGUAGE.code` | Device code contains product codes/SKUs; name similarity is accidental |
| `MHCatalogue.EN_SYSTEM.id_system = OPEN.EN_SYSTEM.id_system` | independent registries with only partial numeric coincidence |
| ScenarioDevices `ObjectId = EN_KEY_OBJECT.key_object` | no declared or complete semantic mapping; namespaces serve different models |
| ScenarioDevices `FamilyId = functional WHO` | family IDs are local editor groupings and values do not encode `WHO` |
| diagnostic Device `ID = EN_DEVICE.id_device` | installed 32-bit instance identifier versus catalogue row key |
| diagnostic `SLOT = EN_SLOTS.id_slot` | Device-local position versus association-row primary key |
| `EN_FIRMWARE.slots = count(EN_SLOTS rows)` | one internal slot can contain several Object alternatives |

## Protocol interpretations

| Proposed interpretation | Reason rejected or constrained |
| --- | --- |
| `DIMENSION 1.N_CONF` is an Object or Virgin Object | `N_CONF` is the number of physical configurator positions; it is a count, not an Object namespace |
| `DIMENSION 32.SYS` is automatically a functional `WHO` | system grouping and candidate values differ; no direct evidence |
| diagnostic outer `WHERE` always equals slot `1` address | observed correlation is not a universal rule |
| every Module returns `DIMENSION 32` | observed command-only layouts and optional response behavior contradict universality |
| actuators use only `DIMENSION 32`; commands use only `35` | a Module can expose address, indexed parameters, both, or neither |
| `DIMENSION 310` is an ordinary `EN_CONF.idx` value | the frame has no index and lacks generic parameter metadata |
| an `ACK` proves effective configuration | acknowledgement, accepted transfer, and diagnostic verification are distinct |

## Configuration errors

| Shortcut | Why unsafe |
| --- | --- |
| validate only against `OPEN.db` field range | transport capacity can be broader than catalogue capability |
| treat `id_key_object = 0` or `id_firmware = 0` as broken references | zero is the `EN_CONF` ownership discriminator |
| use global `EN_CONF.idx` lookup | index meaning depends on Object/firmware and slot context |
| treat a visible UI field as writable | visibility and editability are separate |
| treat a physical counterpart as proof of active physical configuration | diagnostics reports effective values, not necessarily the configuration method |

## Reconsideration rule

A rejected relationship can be reopened when new evidence directly addresses the reason for rejection. Record the new source and test it against the full dataset; do not silently remove the earlier counterexample.
