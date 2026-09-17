# Cross-database functional coverage

The MyHOME_Suite databases describe different layers of the same implementation. They should be correlated, but their identifiers must not be joined merely because they have the same numeric value.

- `OPEN.db` describes protocol systems, address grammars, management operations, parameters, sequences, diagnostics, and programming workflows.
- `MHCatalogue.db` describes physical Devices and the Device → Module → Object → Configuration capability model.
- `ScenarioDevices-program-files.sqlite` and `ScenarioDevices-programdata.sqlite` describe the scenario engine's functional Objects, actions, triggers, conditions, command templates, and parameter constraints.
- `rules.db3` contains additional validation/dependency data and is not a general `WHO` registry.

This page records the useful intersections without inventing database relationships that are not present.

## `MHCatalogue.db` system layer

`MHCatalogue.db.EN_SYSTEM` is a catalogue namespace, not the same identifier space as `OPEN.db.EN_SYSTEM`. Its rows nevertheless establish which broad functional systems the catalogue can assign to physical items through `AS_ITEM_SYSTEM`.

| Catalogue system | `EN_SYSTEM.id_system` | `sys_modobj` | Catalogue items | Catalogue Devices | Functional relationship |
| --- | ---: | ---: | ---: | ---: | --- |
| Automation | `1` | `1` | `113` | `338` | Lighting / Automation Objects and Devices |
| Temperature control | `2` | `3` | `17` | `57` | `WHO 4` device capability |
| Burglar alarm system | `3` | `4` | `7` | `10` | `WHO 5` device capability |
| Video door entry system | `4` | `6` | `20` | `39` | Video-door-entry families |
| Sound system | `5` | `8` | `1` | `2` | Sound / multimedia capability |
| Auxiliary | `6` | `9` | `0` | `0` | Auxiliary namespace represented, no directly assigned catalogue item in this dataset |
| Energy management functions | `7` | `17` | `0` | `0` | Legacy/load-management capability namespace |
| Access control | `8` | `7` | `9` | `15` | `WHO 23` device capability |
| New energy saving and load control | `20` | `2` | `13` | `29` | Energy/load-control Devices |
| Integration function | `26` | `15` | `43` | `83` | Integration-capable Devices |
| Hospital signaling system | `29` | `5` | `0` | `0` | Nurse Call / signalling capability namespace |

The catalogue also defines interface-only systems for Automation, burglar alarm, multimedia, Access Control, eight-wire Video Door Entry, and other bus levels. These rows are useful when interpreting interface Devices, but they do not independently assign an OpenWebNet `WHO`.

`sys_modobj` is a catalogue model value. It is not a functional or diagnostic `WHO` and must not be used as one.

## ScenarioDevices functional command layer

The two ScenarioDevices databases provide a complementary view that `OPEN.db` largely does not: concrete functional operations usable by the MyHOME_Suite scenario engine.

The program-files database contains 29 Object-system rows, 44 DeviceObjects, 157 Commands, and 42 Parameters. The program-data copy contains 27 Object-system rows, 42 DeviceObjects, 151 Commands, and 40 Parameters. Their common functional command model is substantially the same; the program-files copy additionally contains the Virtual Key Card trigger family and two Temperature Control action records.

### Explicit OpenWebNet frame families

Where ScenarioDevices supplies both `ChiOpen` and `Frame`, the following functional namespaces are explicit:

| `WHO` | Scenario-engine capability | Examples established by the database |
| ---: | --- | --- |
| `0` | Scenario-module action | `*0*N*WHERE##` |
| `1` | Lighting and Lighting-like actions | OFF/ON, timed ON, 100-level dimming, controlled socket, fan, automation door lock |
| `2` | Automation | UP/DOWN/STOP, absolute position, advanced movement, step-by-step movement |
| `4` | Temperature Control | MyHOME_Suite `DIMENSION 7` operating-mode/setpoint actions plus local-control and fan-coil writes |
| `14` | Special commands | actuator lock and unlock |

This is implementation evidence for commands that MyHOME_Suite can place in scenarios. It is not evidence that the scenario engine enumerates every valid functional command for those WHOs.

### `WHO 14` semantics recovered

ScenarioDevices resolves the previously ambiguous `WHO 14` operations through the Object and command names attached to the frames:

| ScenarioDevices command | Frame | Meaning |
| --- | --- | --- |
| `miniScenarioSuite.specialCommands.actionLockUnlockActuator.lock` | `*14*0*WHERE##` | Lock actuator |
| `miniScenarioSuite.specialCommands.actionLockUnlockActuator.unlock` | `*14*1*WHERE##` | Unlock actuator |

This is direct MyHOME_Suite implementation evidence for `WHAT 0` and `WHAT 1` in the actuator lock/unlock Object context.

### `WHO 1` target-dependent interpretation

ScenarioDevices contains a notable overlap with the published Lighting vocabulary. The command `miniScenarioSuite.automation.actionAutomationDoorLock.on` emits `*1*17*WHERE##`. In the published Lighting table, ordinary `WHAT 17` is the 30-second timed-ON command.

The databases therefore show that the same wire frame can be presented by MyHOME_Suite as an **Automation Door Lock ON** action when the selected Object is a door-lock capability. A decoder should not discard the published `WHO 1` meaning; instead, higher-level UI semantics can depend on the target Object while the wire-level `WHAT` remains `17`.

This is an example of why `WHO` + `WHAT` alone is not always sufficient for a user-facing capability label.

### `WHO 4` implementation-only action surface

ScenarioDevices provides exact MyHOME_Suite action templates using `DIMENSION 7`:

| Mode | Heat | Cool | Auto | Generic |
| --- | --- | --- | --- | --- |
| Comfort | `*#4*ZAZB*#7*1*3*##` | `*#4*ZAZB*#7*2*3*##` | `*#4*ZAZB*#7*3*3*##` | `*#4*ZAZB*#7*0*3*##` |
| Eco | `*#4*ZAZB*#7*1*4*##` | `*#4*ZAZB*#7*2*4*##` | `*#4*ZAZB*#7*3*4*##` | `*#4*ZAZB*#7*0*4*##` |
| Protection | `*#4*ZAZB*#7*1*2*##` | `*#4*ZAZB*#7*2*2*##` | `*#4*ZAZB*#7*3*2*##` | `*#4*ZAZB*#7*0*2*##` |
| Setpoint | `*#4*ZAZB*#7*1*1*c1c2c3c4##` | `*#4*ZAZB*#7*2*1*c1c2c3c4##` | `*#4*ZAZB*#7*3*1*c1c2c3c4##` | `*#4*ZAZB*#7*0*1*c1c2c3c4##` |

It also defines OFF as `*#4*ZAZB*#7*0*5*##`, local control as `*#4*ZAZB*#5*val##`, and fan-coil speed as `*#4*ZAZB*#11*val##`.

These are MyHOME_Suite implementation templates. They complement, rather than replace, the public `WHO 4` functional `DIMENSION` table.

## Scenario capabilities without explicit OpenWebNet frames

ScenarioDevices also defines Alarm, Auxiliaries, hotel-room, scheduled-scenario, time, and Virtual Key Card trigger/condition/action capabilities for which the `Frame` column is null or contains a symbolic internal expression rather than a complete OpenWebNet frame.

Those rows establish application-level capabilities, but they do not justify manufacturing a `WHO`, `WHAT`, or `DIMENSION` mapping. They should be used as semantic leads only when another source establishes the wire representation.

## How the three databases complement each other

A useful implementation interpretation is:

| Question | Strongest database evidence |
| --- | --- |
| Which protocol system / diagnostic family does MyHOME_Suite know? | `OPEN.db.EN_SYSTEM` |
| Which `WHERE` grammar does the implementation construct? | `OPEN.db.EN_ADDRESS_RULE` and association tables |
| Which management/configuration frame does it send? | `OPEN.db.EN_OPEN` and `AS_OPEN_*` |
| Which physical Devices support a functional system? | `MHCatalogue.db.EN_DEVICE` → `EN_ITEM` → `AS_ITEM_SYSTEM` |
| Which Modules and Objects can a Device expose? | `MHCatalogue.db` firmware/slot/Object tables |
| Which configuration properties and ranges exist? | `MHCatalogue.db.EN_CONF`, ranges, filters, and firmware associations |
| Which functional actions can the scenario engine emit? | ScenarioDevices `Commands.Frame` / `ChiOpen` |
| Which action parameters are constrained? | ScenarioDevices `Parameters` |

The databases therefore describe **different projections of the implementation**, not redundant copies of one protocol catalogue.

## Cross-reference rule

Do not numerically join `OPEN.db.EN_SYSTEM.id_system`, `MHCatalogue.db.EN_SYSTEM.id_system`, ScenarioDevices `FamilyId`, ScenarioDevices `ObjectId`, or `MHCatalogue.db.EN_KEY_OBJECT.key_object`. These are independent identifier spaces.

A cross-database relationship should be asserted only when one of the following establishes it:

1. an explicit database relationship;
2. an exact OpenWebNet frame containing the `WHO`;
3. matching implementation semantics corroborated by the protocol specification or observed traffic;
4. a Device/Object mapping already established through the MyHOME_Suite catalogue model.

This keeps implementation-derived enrichment useful without turning coincidental numeric equality into protocol semantics.

See [`open-db-coverage.md`](open-db-coverage.md) for the complete `OPEN.db` namespace/management matrix and [`../device-model/`](../device-model/) for the catalogue Device → Module → Object → Configuration model.