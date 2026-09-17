# Virgin Objects

A Virgin Object is a catalogue-level definition used before a Module has its final Object assignment. It constrains the Object choices available for that Module.

## Role in the model

Virgin Objects sit between Module capability and configured Object identity:

1. the Physical Device exposes a Module
2. the Module is associated with a Virgin Object definition
3. the Virgin Object permits one or more concrete Objects
4. configuration selects or instantiates the applicable Object and its parameters

This relationship expresses allowed transformations. It does not mean that the Virgin Object and the configured Object share the same identifier.

## Catalogue relationships

This page will document:

- Virgin Object identifiers and descriptions
- the one-to-many relationship between a Virgin Object and permitted Objects
- how Device and Module records select a Virgin Object
- whether an Object choice is fixed, optional, or unavailable
- constraints inherited by the final configuration

The exact catalogue tables and joins will be added after the relevant relationships have been verified against the canonical database.

## Interpretation rules

A permitted relationship establishes catalogue compatibility, not observed runtime use. A Module can support several Objects while one Device instance uses only one of them.

Names, numeric identifiers, Module positions, and diagnostic values remain independent unless the catalogue schema or protocol behavior explicitly connects them.
