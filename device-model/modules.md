# Modules

A Module is a firmware-exposed logical container within a Physical Device. A Device can expose one or more Modules, each located by an internal slot.

## Terminology

**Module** is the preferred term for the logical units presented by a Device in MyHOME_Suite and by the diagnostic protocol.

**Internal slot** refers specifically to the numeric position used in catalogue structures and diagnostic frames. The internal slot locates the Module; it is not the Module’s functional address.

The following must remain distinct:

| Term | Meaning |
| --- | --- |
| Physical Device | Installed hardware product |
| Module | Firmware-exposed logical container |
| Internal slot | Numeric position locating a Module |
| Object | Logical function assigned to a Module |
| UI position | User-facing order or label, which may differ from the internal slot |
| Functional address | Address configured on an Object |

## Firmware-declared Module count

`EN_FIRMWARE.slots` declares the number of internal slots for a firmware definition.

This is the closest catalogue representation of the Module count, but it is not the number of rows in `EN_SLOTS`. The latter records Object alternatives and can contain several rows for one internal slot.

Examples:

| Firmware | Declared slots | Slot/Object rows | Interpretation |
| ---: | ---: | ---: | --- |
| `157` | `4` | `10` | four Modules with multiple Object alternatives |
| `145` | `2` | `8` | two command Modules, four Object alternatives per slot |
| `590` | `2` | `3` | two dimmer Modules; one slot carries an additional combined alternative |
| `194` | `1` | `1` | one fixed Light actuator Module |

## Catalogue slot representation

The primary path is:

`EN_FIRMWARE` → `AS_OBJECT_FIRMWARE` → `EN_SLOTS`

### `AS_OBJECT_FIRMWARE`

This association states that a firmware supports an Object:

| Column | Role |
| --- | --- |
| `id_object_firmware` | Association identifier |
| `id_firmware` | Firmware definition |
| `id_key_object` | Supported Object |

### `EN_SLOTS`

This table places a firmware/Object association at an internal slot:

| Column | Role |
| --- | --- |
| `id_slot` | Slot-assignment record |
| `first_slot` | Internal slot at which the Object association starts |
| `fixed_ko` | Marks the designated/fixed Object association in the catalogue data |
| `id_object_firmware` | Firmware/Object association |

All 1,725 slot records resolve to an `AS_OBJECT_FIRMWARE` association in the canonical database.

`first_slot` ranges from `1` through `17` in this source revision. That is observed catalogue coverage, not a universal protocol limit; `OPEN.db` permits diagnostic `[SLOT]` values from `1` through `255`.

## Object alternatives at a Module

A Module can expose:

- one Object only;
- one designated Object plus alternatives;
- a Virgin Object template that permits a set of Objects;
- a fixed Object whose configuration is still editable;
- no user-visible Object in a particular Device/UI context.

`fixed_ko` must not be translated mechanically into “Function type not user modifiable”. The visible behavior can also depend on Virgin Object associations, conditions, filters, and product-specific UI rules.

### Combined Device example

Firmware `157`, used by `64391`, `64191`, and `64192`, shows why Object alternatives cannot be counted as Modules:

| Slot | Designated Object | Additional Objects |
| ---: | --- | --- |
| `1` | Light actuator | Automation actuator |
| `2` | Light actuator | — |
| `3` | Light control | Automation control; Scheduled scenario; Scheduled scenario PLUS |
| `4` | Light control | Automation control; Scheduled scenario; Scheduled scenario PLUS |

The Physical Device therefore has four Modules, not ten.

## Diagnostic Module enumeration

`OPEN.db` defines the Module/Object response:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

| Field | Database description | Range |
| --- | --- | ---: |
| `SLOT` | “ko slot” | `1`–`255` |
| `KEYO` | “device object model” | `1`–`65535` |
| `STATE` | “configured or not configured” | `0`–`1` |

This response exposes the Device’s current Module/Object state:

- `SLOT` locates the Module;
- `KEYO` identifies the current Object;
- `STATE` reports a binary configuration state.

The catalogue association between `EN_KEY_OBJECT.key_object` and `KEYO` is supported by matching Object identity and observed behavior. It is not a cross-database foreign key.

### Address response

`OPEN.db` defines:

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

This reports a system and address for the Object at an internal slot. It does not redefine the Module itself as an address.

### Configuration response

`OPEN.db` defines:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Here `SLOT` selects the Module whose configuration property is being reported. `INDEX` selects the configuration property and `VAL_PAR` carries its value.

## Enabled, disabled, absent, and fixed

These states are distinct:

| State | Meaning |
| --- | --- |
| Present and configured | Module exists and has a configured Object |
| Present and unconfigured | Module exists but has not received a final configuration |
| Disabled | Module exists but its Object is disabled by configuration |
| Absent from UI | MyHOME_Suite does not present the internal slot in that context |
| Fixed-function | Catalogue/UI does not allow selection of another Object |
| Alternative Object | Firmware supports another Object at the same internal slot |

A captured `STATE` value alone does not establish all these UI distinctions.

For example, Device `007B269D` was observed with internal slot `1` disabled, internal slot `2` absent from the UI, and internal slots `3` and `4` displayed under shifted UI numbering. This demonstrates that UI position and internal slot cannot be assumed identical.

## Hardware-backed and logical Modules

A Module can correspond directly to hardware, such as:

- a relay output;
- a dimmer output;
- a pushbutton pair;
- a dry-contact input;
- a sensor;
- an IR scenario channel.

It can also represent a logical capability exposed by firmware. The catalogue establishes availability but does not always describe the physical implementation.

Command-only Devices such as `64360` expose Light control Objects as their actual hardware function. Those Objects are not alternate configurations of a hidden actuator.

## Repeated Modules

Some firmware definitions expose repeated Modules with the same Object vocabulary. Repetition does not make the Modules interchangeable at runtime: each internal slot can have its own Object selection, address, groups, and parameters.

The IP55 PIR sensor observed as Device `08CF44BF` illustrates a large Module set: one sensor Module plus optional IR scenario-control Modules across later slots. The catalogue’s maximum observed `first_slot` of `17` is consistent with this class of Device.

## Conditions attached to slots

`AS_SLOT_CONDITION` associates `EN_SLOTS.id_slot` with `EN_CONDITION.id_condition`. The canonical database contains 1,000 such associations.

Conditions can restrict whether a slot/Object association is applicable. `EN_CONDITION` references `EN_CONV_RULE`, which expresses configuration-dependent logic. Therefore, the raw existence of an `EN_SLOTS` row establishes catalogue capability, not unconditional availability in every configuration.

## Source boundaries

- [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) establishes declared slots, Object alternatives, and slot conditions.
- [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) establishes the `DIMENSION 30`, `32`, and `35` wire structures.
- Observed traffic establishes the actual Modules reported by a Device.
- MyHOME_Suite UI behavior establishes visibility, display order, labels, and editability.

Where these layers differ, document the difference instead of forcing them into one slot numbering scheme.
