# Objects

An Object is the logical function exposed by or assigned to a Module. It defines what that Module does, not the identity of the Physical Device that contains it.

## Object identity

The catalogue represents Objects through Object identifiers and descriptions. This page will document:

- Object identity and catalogue naming
- the relationship between Modules and Objects
- fixed, selectable, and disabled Object assignments
- functional-system membership
- diagnostic and programming capabilities associated with an Object
- Object-specific configuration definitions

Database identifiers such as `EN_KEY_OBJECT.key_object` retain their database meaning. The documentation does not shorten Object to “KO”.

## Device and Object descriptions

The Device description identifies the physical product model. The Object description identifies an individual logical function such as a command, actuator, dimmer, sensor, or scenario function.

A Device can therefore have one standard Device description and several different Object descriptions. Object labels must not be used as substitute model names for the Device.

## Functional role

An Object can produce or consume functional OpenWebNet traffic under one or more applicable `WHO` namespaces. The functional namespace describes runtime behavior; it does not by itself determine the Physical Device class.

For example, a Light control Object on command-only hardware represents the actual command function of that hardware. It is not evidence that the Device contains a light actuator.

## Configuration relationship

Object identity selects the configuration vocabulary available to a Module. Configuration then supplies instance-specific values such as addresses, modes, delays, groups, presets, and other parameters.

The same Object type can appear in different Device models while retaining Object-level semantics and acquiring Device- or Module-specific constraints.
