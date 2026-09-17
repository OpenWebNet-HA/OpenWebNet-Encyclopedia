# Device Selection

Programming must identify the intended installed Physical Device before applying Module or Object changes.

## Planned coverage

- selection by Device ID;
- selection by diagnostic or functional address;
- local-interaction selection where implemented;
- unconfigured Device selection;
- configured Device selection;
- identifier encoding and range;
- ambiguity and collision handling;
- selection errors and timeouts.

The Device ID, diagnostic `WHERE`, functional Module address, catalogue Device row, and Object number remain separate namespaces.

Selection procedures will link to [Device Discovery](../diagnostics/device-discovery.md) and [Address Discovery](../diagnostics/address-discovery.md) without duplicating their enumeration rules.
