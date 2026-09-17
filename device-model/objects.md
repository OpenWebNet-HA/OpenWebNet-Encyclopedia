# Objects

An Object is the logical function exposed by or assigned to a Module. It defines what that Module does, not the identity of the Physical Device containing it.

## Catalogue identity

`MHCatalogue.db.EN_KEY_OBJECT` contains 158 Object definitions.

| Column | Role |
| --- | --- |
| `id_key_object` | Internal database key |
| `key_object` | External/catalogue Object number |
| `descr` | Object description |
| `slots` | Object-level slot metadata stored as text |
| `visible` | Catalogue/UI visibility |
| `id_family` | Object-family reference |

The two Object identifiers serve different purposes:

- `id_key_object` joins catalogue tables;
- `key_object` is the Object number exposed in the wider MyHOME_Suite model and correlated with diagnostic `KEYO`.

Documentation uses **Object**, not “KO”, except when quoting database column names or source descriptions.

## Device and Object descriptions

The Device and Object answer different questions:

| Question | Source |
| --- | --- |
| What physical product is installed? | `EN_DEVICE.name` |
| What shared product/capability item does it use? | `EN_ITEM.descr` |
| What logical function does one Module expose? | `EN_KEY_OBJECT.descr` |

A Device can therefore have one standard Device description and several Object descriptions.

For example, `64391` is catalogued as “Flush mounted actuator and free control”. Its Modules can expose Objects including:

- `6`: Light actuator;
- `7`: Automation actuator;
- `400`: Light control;
- `401`: Automation control;
- `404`: Scheduled scenario;
- `406`: Scheduled scenario PLUS.

None of those individual Object descriptions is a complete Device-model name.

## Firmware and slot availability

Objects become available to a Device through:

`EN_FIRMWARE` → `AS_OBJECT_FIRMWARE` → `EN_SLOTS`

The canonical database contains:

- 827 firmware/Object associations;
- 1,725 slot/Object placements.

A reusable Object can appear in many firmware definitions and at many slots. The same Object semantics can therefore be shared by different product models.

## Object-system associations

`AS_OBJECT_SYSTEM` associates an Object with a catalogue system. The canonical database contains 251 such rows.

This is a catalogue relationship. `MHCatalogue.db.EN_SYSTEM.id_system` is not the same identifier space as:

- functional OpenWebNet `WHO`;
- diagnostic `WHO`;
- `OPEN.db.EN_SYSTEM.id_system`;
- ScenarioDevices `FamilyId`;
- ScenarioDevices `ObjectId`.

A functional-system mapping can be made when the Object’s semantics, functional frame, or another explicit association establishes it. Numeric equality alone is not evidence.

## Diagnostic Object identity

`OPEN.db` defines:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

`KEYO` is described as the “device object model” and has range `1`–`65535`. In the catalogue, `EN_KEY_OBJECT.key_object` supplies the corresponding Object number.

This mapping is structurally and behaviorally supported, but there is no foreign key between the two databases. A decoder should retain both the raw `KEYO` value and the resolved catalogue Object record.

## Object roles

Objects can represent several roles:

| Role | Examples |
| --- | --- |
| Command | Light control, Automation control, AUX control |
| Actuator | Light actuator, Automation actuator, Dimmer actuator |
| Sensor | Daylight sensor, motion/presence sensor |
| State/input | Contact state |
| Scenario | Scheduled scenario, Scheduled scenario PLUS |
| Interface | Bus or system integration Objects |
| Temperature Control | Thermostat, probe, relay, fan-coil functions |
| Energy/access/hotel | Domain-specific functions represented by catalogue systems |

These roles describe logical function. They do not prove that every Device exposing the Object contains identical hardware.

## Command and Device Objects

`AS_KO_CMD_KO_DEV` records explicit command-Object to Device-Object pairings:

| Column | Role |
| --- | --- |
| `key_object_cmd` | Command Object number |
| `key_object_cmd_desc` | Command Object description |
| `key_object_dev` | Device/actuator Object number |
| `key_object_dev_desc` | Device/actuator Object description |

This table can establish that a command Object is intended to control a particular class of Device Object. It does not make the two Objects identical.

## Object families and collections

Additional catalogue relationships include:

- `EN_OBJECT_ITEM_FAMILY`: Object/item family vocabulary;
- `AS_OBJECT_COLLECTION`: Object membership in collections;
- `AS_OBJECT_FUNCTION`: special-function associations;
- `AS_ICON_KO`: Object icons, subtypes, and modifiability metadata;
- `AS_OBJECT_VIRGIN_OBJECT`: Objects permitted by a Virgin Object;
- `RIF_MH_OBJECT`: installation/project Object instances with addresses and collection membership.

`RIF_MH_OBJECT` describes project-instance data structures, whereas `EN_KEY_OBJECT` describes reusable catalogue Object types.

## Functional OpenWebNet projection

Functional `WHO` documentation describes runtime frames emitted or consumed by configured Objects. It does not define the product hierarchy.

Examples:

- Light control and Light actuator Objects participate in Lighting traffic under `WHO 1`.
- Automation control and Automation actuator Objects participate in Automation traffic under `WHO 2`.
- Scenario Objects can participate in `WHO 0`, `WHO 15`, `WHO 17`, or `WHO 25`, depending on the function.
- Temperature Control Objects use `WHO 4`.

An Object label is not enough to manufacture a frame mapping. The mapping must be supported by the public protocol, an exact frame template, catalogue association, or observed traffic.

## ScenarioDevices evidence

The two ScenarioDevices databases describe scenario-engine capabilities through their own `ObjectSystems`, `DeviceObjects`, `Commands`, and `Parameters` tables.

They contain:

| Database | Object systems | DeviceObjects | Commands | Parameters |
| --- | ---: | ---: | ---: | ---: |
| Program Files copy | 29 | 44 | 157 | 42 |
| ProgramData copy | 27 | 42 | 151 | 40 |

These Object IDs are not `MHCatalogue.db.EN_KEY_OBJECT.key_object`. ScenarioDevices contributes:

- user-facing action/trigger/condition semantics;
- exact functional frames where `Commands.Frame` is populated;
- parameter limits for scenario commands.

It does not determine which Physical Device or internal slot exposes a catalogue Object.

See [cross-database functional coverage](../functional/cross-database-coverage.md) for the supported intersections.

## Object-scoped configuration

An Object can own reusable configuration definitions. In `EN_CONF`, Object-scoped rows use:

- an `id_key_object` resolving to `EN_KEY_OBJECT`;
- `id_firmware = 0`.

The canonical database contains 1,420 Object-scoped configuration rows. Firmware-scoped configuration uses the complementary pattern described in [`configuration.md`](configuration.md).

## Light-control-only Devices

The observed Devices `00C44420`, `00C443B9`, `00C4442E`, `00C44456`, `00C4445F`, and `00C4446E` expose Light control functionality without light-actuator hardware.

For these Devices, a Light control Object is their actual command hardware function. It must not be described as an alternate configuration of a light actuator merely because actuator and command Objects participate in the same functional `WHO`.

## Object `406`

Object `406` is catalogued as “Scheduled scenario PLUS”. On products such as `64360` and the command Modules of `64391`, it is one of the Object choices offered at a Module.

Its catalogue presence establishes that the Module can expose that logical function. Its complete runtime and programming behavior must be documented from the relevant scenario protocol and observed traffic, not inferred from the Object number alone.

## Source boundaries

| Source | Object evidence |
| --- | --- |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Object identity, families, firmware/slot availability, configuration, Virgin Object mappings |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | Diagnostic `KEYO`, system/address, and parameter frames |
| [ScenarioDevices databases](../sources/myhome-suite/3.5.38/databases/) | Scenario-engine capability names and functional command templates |
| [public OpenWebNet documents](../sources/openwebnet-public/) | Published functional semantics |
| Observed traffic | Actual Object identity and runtime behavior |
| MyHOME_Suite UI | Displayed Function type and editability |

When sources disagree or use different identifier spaces, retain the source-specific values and document the correlation explicitly.
