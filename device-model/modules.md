# Modules

A Module is a firmware-exposed logical container within a Physical Device. A Device can expose one or more Modules.

## Terminology

**Module** is the preferred term for the logical units presented by a Device in MyHOME_Suite and by the diagnostic protocol.

**Internal slot** refers specifically to the numeric slot or index used in protocol frames or catalogue structures. An internal slot is an implementation locator; the Module is the logical entity located through it.

A user-interface position or label is not assumed to equal the protocol slot number unless the mapping is established.

## Module inventory

This page will document:

- how a Device declares its Module count and ordered Module list
- how internal slots identify Modules during diagnostic operations
- enabled, disabled, absent, and fixed-function Module states
- the distinction between hardware-backed and purely logical Modules
- Module capabilities that determine which Objects may be assigned

## Fixed and configurable Modules

A Module can expose a fixed Object, offer a constrained choice of Objects, or remain unavailable in a particular Device variant. These states must be derived from catalogue relationships and protocol behavior rather than from position alone.

Combined Devices may expose actuator Modules and independently configurable command Modules in the same Physical Device. Conversely, a local button that is hard-linked to an actuator does not necessarily constitute a separately configurable Module.

## Protocol representation

Diagnostic Module-list operations establish the Modules exposed by a Device and their internal slot identifiers. Object-specific diagnostic operations then describe the function and configuration associated with a selected Module.

The numeric fields used by Module-list responses will remain explicitly unknown where their semantics have not been established.
