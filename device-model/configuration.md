# Configuration

Configuration is the set of instance-specific values applied to an Object on a Module. It turns a supported logical function into an operational function within an installation.

## Configuration layers

The configuration model will distinguish:

| Layer | Purpose |
| --- | --- |
| Object selection | Chooses the function exposed by a configurable Module |
| Addressing | Assigns the functional target, such as point-to-point `A`/`PL`, group, environment, CEN, zone, or another system-specific address |
| Operating mode | Selects an Object-specific behavior or modality |
| Parameters | Supplies delays, levels, button assignments, sensitivity, load type, presets, and other Object-specific values |
| Associations | Links the Object to groups, scenarios, related Modules, or other supported entities |
| State and constraints | Records enabled state, fixed values, ranges, defaults, and read-only behavior |

Not every Object uses every layer.

## Catalogue representation

This page will document how configuration definitions and values are represented in the MyHOME_Suite catalogue, including:

- configuration keys and their ordering
- Object-to-configuration relationships
- value types, ranges, enumerations, and defaults
- dependencies that reveal or constrain other fields
- fixed and read-only values
- repeated values such as groups or preset positions

Database field names such as `EN_CONF.idx` and `EN_CONF.id_key_object` are treated as implementation identifiers until their precise relationships are established.

## Protocol representation

Diagnostic operations read the current Object assignment and configuration state. Programming operations write supported values and manage the configuration lifecycle.

A protocol field is not equated with a catalogue column solely because the values resemble one another. Mappings require consistent structural and behavioral evidence.

## Addressing

Configuration addresses are scoped to the functional system of the Object. `A`/`PL` applies to the SCS address families that define it; other systems use their own address grammars.

The Physical Device address used for discovery or interview can differ from the configured functional addresses of its Modules. Any rule connecting a Device-level address to a particular Module will be documented only where verified.

## Constraints and unresolved values

The reference will preserve the difference between:

- values selectable by the user
- values fixed by the Device model
- values calculated or compiled by MyHOME_Suite
- values reported by the Device
- fields whose meaning remains unknown

Unknown diagnostic fields remain unknown until corroborating evidence establishes their semantics.
