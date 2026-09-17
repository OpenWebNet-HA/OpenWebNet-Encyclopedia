# Overview

`WHO 3` defines the OpenWebNet Load Management system. It represents the older load-control domain: managed electrical loads, priority/disconnection behavior and associated load-management states.

## Reference

| Subject | Page |
| --- | --- |
| Functional model and protocol boundaries | [`protocol.md`](protocol.md) |

## Relationship to energy systems

Load Management must not be merged with [`WHO 18`](../who-18-energy-management/) Energy Management. `WHO 3` concerns load-control behavior, while `WHO 18` provides the later power, energy-totalizer, actuator, Stop&Go and historical-energy model. [`WHO 11`](../who-11-energy-distribution/) is another distinct namespace.

The MyHOME_Suite functional-system data retains Load Management as its own system, which is consistent with this protocol separation.

## Implementation rule

`WHAT`, `WHERE`, and any structured values are scoped to `WHO 3`. Similar concepts in `WHO 18` must not be substituted by numeric resemblance. Where the current integrated corpus does not establish a value precisely, it remains unspecified rather than inferred from the newer Energy Management protocol.

See [`../../protocol/`](../../protocol/) for common OpenWebNet frame syntax.