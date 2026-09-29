# Flush-mounted two-relay actuator and free control

## Summary

| Field | Value |
| --- | --- |
| Device ID | `OWN-DEV-0003` |
| Technical description | Flush-mounted two-relay actuator and free control |
| Categories | Actuator, Command, Multifunction, Lighting, Automation |
| Documentation status | Partial |

Legrand 64391 is a combined Device: it contains actuator capability and independently configurable command/scenario capability in one Physical Device.

The canonical MyHOME Suite catalogue resolves SKU `64391` to shared item `1184`, “Flush mounted actuator and free control”, item model `107`, and firmware definition `157`.

## Commercial identities

| Brand | SKU / reference | Region / line | Relationship | Evidence |
| --- | --- | --- | --- | --- |
| Legrand | 64391 | Espace Evo | Established identity | Canonical catalogue and MyHOME Suite product/function documentation |

### Related catalogue records

Catalogue SKUs `64191` and `64192` share item `1184`, item model `107`, firmware `157`, and therefore the same firmware/Module/Object/configuration capability core.

That shared capability model is not, by itself, treated here as proof that `64191`, `64192`, and `64391` are fully synonymous commercial identities. Their exact product/line differences should be established from product documentation before merging them into one technical Device definition.

## Documentation

A canonical publisher-hosted PDF specifically for 64391 has not yet been archived. The following source leads are already useful.

| Document / source | Type | Revision / date | Language | Archived original | Source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite function documentation - lighting actuator modes | Vendor implementation documentation | MyHOME Suite 03.04-era web help | EN | External only | [BTicino MyHOME Suite documentation](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_attuatore_luci.html) |
| MyHOME Suite function documentation - automation actuator modes | Vendor implementation documentation | MyHOME Suite 03.04-era web help | EN | External only | [BTicino MyHOME Suite documentation](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/attuatore_automazione.html) |
| Arnould / BTicino Espace Evolution general catalogue | Historical product catalogue lead | Historical | FR | Pending verification | Secondary archival lead located; canonical publisher copy still sought |

The project should continue looking for the original Legrand/Arnould product sheet, installation sheet, and historical catalogue revisions.

## Identification

| Evidence | Value | Status | Source |
| --- | --- | --- | --- |
| Catalogue SKU | `64391` | Implementation evidence | [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192) |
| Catalogue item | `1184` | Implementation evidence | [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192) |
| Item description | `Flush mounted actuator and free control` | Implementation evidence | [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192) |
| `modobj` / item model | `107` | Implementation evidence | [DIMENSION 1 Device Identity](../../diagnostics/dim1-device-identity.md) |
| Firmware definition | `157` | Implementation evidence | [Firmware](../../device-model/firmware.md#firmware-example) |
| Installed `WHO 1001 DIMENSION 1` tuple | Not yet curated on this page | Incomplete | - |

`OBJECT_MODEL = 107` identifies the shared item/capability model, not SKU `64391` uniquely. Catalogue brand/line or other product evidence is required to narrow the marketed Device record.

## Firmware and hardware

Firmware `157` declares four `slot` positions and eleven slot/Object alternatives.

| `slot` | Designated Object | Additional Objects |
| ---: | --- | --- |
| `1` | Light actuator (`6`) | Automation actuator (`7`) |
| `2` | Light actuator (`6`) | - |
| `3` | Light control (`400`) | Automation control (`401`); Scheduled scenario (`404`); Scheduled scenario PLUS (`406`) |
| `4` | Light control (`400`) | Automation control (`401`); Scheduled scenario (`404`); Scheduled scenario PLUS (`406`) |

The Device therefore has four Modules. Eleven catalogue rows represent Object alternatives across those Modules, not eleven Modules.

## Functional profile

| Module / `slot` | Capability | Typical role | Functional system |
| ---: | --- | --- | --- |
| `1` | Light actuator or Automation actuator | Actuator | Lighting or Automation |
| `2` | Light actuator | Actuator | Lighting |
| `3` | Light control, Automation control, Scheduled scenario, or Scheduled scenario PLUS | Command / scenario | Configuration-dependent |
| `4` | Light control, Automation control, Scheduled scenario, or Scheduled scenario PLUS | Command / scenario | Configuration-dependent |

This is precisely why Device category is many-to-many: `64391` is simultaneously an actuator, a command Device, and a multifunction Device.

## Diagnostic observations

The canonical diagnostic model can expose the installed Module/Object projection through `DIMENSION 30`.

For this Device, the catalogue establishes the candidate Object set above. The active Object at each `slot` must still be derived from the installed configuration or diagnostic observation rather than assumed from the SKU alone.

A complete first-hand fingerprint for a known 64391 is not yet incorporated into this page.

## Addressing and memberships

Actuator and command Modules can have distinct functional addressing roles. Do not reduce the Physical Device to one OpenWebNet address.

Installed A/PL values, group memberships, scenario bindings, and other concrete configuration are local installation state.

## Configuration

### Configuration methods

Firmware `157` is associated with:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

### Physical configuration

The relevant firmware-scoped physical definitions are:

| Position | Legal physical domain |
| --- | --- |
| `A1` | `0..9` |
| `PL1` | `0..9` |
| `M1` | `0..8`; `9 = O/I`; `10 = OFF`; `12 = UP/DOWN`; `13 = UP/DOWN monostable`; `14 = CEN`; `15 = PUL` |
| `A2` | `0..9` |
| `PL2` | `0..9` |
| `M2` | Same stored domain as `M1` |

Firmware `157` also owns `AID` at `progressive = 0`; that is an ID field and is not one of the six physical configurator positions above.

### Condition-dependent topology

The selected Objects depend on configuration conditions.

For the representative physical configuration:

```text
M1=CEN
M2=O/I
```

the canonical catalogue branches resolve the four slots to:

| `slot` | Selected Object |
| ---: | --- |
| `1` | Light actuator (`6`) |
| `2` | Light actuator (`6`) |
| `3` | Light control (`400`) |
| `4` | Light control (`400`) |

This `[6, 6, 400, 400]` topology is an example produced by the generic resolver. It must not be stored as the unconditional topology of every 64391.

The catalogue also contains unreachable or textually irregular stored branches for this firmware. See [Catalogue Resolution](../../internals/catalogue-resolution.md#worked-example-firmware-157) before implementing configuration generation from these rules.

## Programming

The Device is a strong test case for future programming support because one physical configuration can select several Object roles across four Modules.

Programming logic must resolve:

1. the legal firmware-specific configuration domain;
2. the condition-selected Object for each Module;
3. applicable Object and firmware configuration definitions;
4. conversion rules;
5. the resulting OpenWebNet programming representation.

It must not hard-code `64391 -> four fixed Objects`.

## Observed behavior

No complete first-hand runtime capture tied to a known physical 64391 has yet been incorporated into this page.

The existing page is therefore intentionally stronger on catalogue/configuration evidence than on installed runtime evidence.

## Evidence

- **Implementation evidence** - canonical `MHCatalogue.db` establishes item `1184`, `modobj = 107`, firmware `157`, four Modules, Object alternatives, configuration domains, conditions, and conversion rules.
- **Implementation documentation** - MyHOME Suite function documentation explicitly includes 64391 among flush-mounted actuator/free-control products and exposes lighting, automation, scenario, and other command functions.
- **Observed behavior** - not yet sufficient for a complete 64391 fingerprint.

## Evidence limits

- Commercial equivalence with `64191` or `64192` is not yet asserted despite their shared capability core.
- A known-physical-64391 fingerprint is still needed.
- Original device-specific Legrand/Arnould PDFs remain to be located and archived.
- Catalogue condition data for firmware `157` contains unreachable and textually irregular branches; do not silently normalize them.
- The complete virtual/advanced configuration constraint set is not yet normalized into this page.

## Sources

- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192)
- [Firmware](../../device-model/firmware.md#firmware-example)
- [Modules](../../device-model/modules.md#combined-device-example)
- [Objects](../../device-model/objects.md#device-and-object-descriptions)
- [Catalogue Resolution](../../internals/catalogue-resolution.md#worked-example-firmware-157)
- [Device Sources](../../sources/devices/)

## Related material

- [Device Model](../../device-model/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
- [Lighting - WHO 1](../../functional/who-1-lighting/)
- [Automation - WHO 2](../../functional/who-2-automation/)
