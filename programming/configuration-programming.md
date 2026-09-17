# Configuration Programming

Configuration programming writes Object- or firmware-scoped properties after the target Device, internal slot, and Object have been resolved.

## Planned coverage

- programming frame structure;
- configuration index resolution through `EN_CONF.idx`;
- Object-scoped and firmware-scoped definitions;
- value encoding and conversion;
- repeated parameter writes;
- read-only and fixed values;
- physical-configurator counterparts;
- parameter errors;
- special Object parameters outside the ordinary indexed model.

`INDEX` is not globally unique. It must be interpreted with the resolved Device, firmware, internal slot, and Object.

See [Validation](validation.md) for the checks required before transmission and [`DIMENSION 35`](../diagnostics/dim35-configuration.md) for diagnostic read-back.
