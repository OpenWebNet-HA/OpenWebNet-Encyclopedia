# Diagram Assets

This directory contains repository-native diagrams used by the documentation.

SVG is the canonical format. Diagrams must be self-contained, contain no external resources or scripts, and remain readable when rendered by GitHub. Relationship connectors must use dedicated whitespace or routing gutters and must not cross entity bodies.

## Installed diagram files

| Filename | Intended page | Purpose | SHA-256 of generated file |
| --- | --- | --- | --- |
| `catalogue-capability.svg` | `internals/catalogue-resolution.md` | Device, item, firmware, Object, slot, build, and system relationships | `6a2dc26de76f51eb42e8c45a92b9fb792af97db91ff1666cb33a4e0a77c8ef8a` |
| `configuration-validation.svg` | `internals/validation-layers.md` | polymorphic configuration ownership and validation layers | `dd7bb3655d9fab72419b20bb025433826b81ddbd5ceb845b0a8202bccfb9ee84` |
| `openwebnet-registry.svg` | `internals/openwebnet-registry-and-state-machines.md` | `OPEN.db` systems, frames, parameters, sequences, and timeouts | `56c8d7a94899f77c6b72fafaadceb95ea5e977b42fcf65e299787176f3620146` |
| `scenario-capability.svg` | `internals/scenario-capability-loading.md` | ScenarioDevices declared hierarchy and revision boundary | `49b55d4d03b9bb0aba68cfb659e6bcee1fbf93f5247e024d8acf7d3dd4e0a00f` |
| `cross-database-correlation.svg` | `reverse-engineering/cross-database-correlation.md` | staged semantic correlation across traffic and independent source models | `2da0a1098f3ef62912403730b786c794099fb8c65b28b558b9bd8bf34409f90f` |

The uploaded SVG content matches the recorded hashes and is referenced from the intended documentation pages. PNG renderings are review artifacts and are not canonical repository assets.
