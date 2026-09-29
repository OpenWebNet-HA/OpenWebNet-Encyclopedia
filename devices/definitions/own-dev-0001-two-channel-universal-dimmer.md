# Two-channel universal dimmer

## Summary

| Field | Value |
| --- | --- |
| Device ID | `OWN-DEV-0001` |
| Technical description | Two-channel universal dimmer |
| Categories | Actuator, Lighting |
| Documentation status | Partial |

BTicino F418U2 is a four-DIN-module, two-channel universal dimmer for the MyHOME SCS bus. The canonical catalogue resolves it to item `2065`, described as “2x1,6A universal dimmer, 4DIN”, with firmware definition `590` and two dimmer Modules.

## Commercial identities

| Brand | SKU / reference | Region / line | Relationship | Evidence |
| --- | --- | --- | --- | --- |
| BTicino | F418U2 | MyHOME | Established identity | Vendor documentation and canonical catalogue |

No cross-brand synonym is asserted on this page yet.

## Documentation

The source archive is not yet populated for this Device. The following official documents have been identified for archival import.

| Document | Type | Revision / date | Language | Archived original | Source |
| --- | --- | --- | --- | --- | --- |
| F418U2 installation instructions `LE07383AD` | Installation instructions | 07/23 | Multilingual | Pending | [BTicino PDF](https://dar.bticino.com/asset/Documents/LE07383AD.pdf) |
| Universal dimmer 2x300W `MQ01019_a_EN` | Technical sheet | Published vendor copy | EN | Pending | [BTicino PDF](https://dar.bticino.com/asset/Documents/MQ01019_a_EN.pdf) |
| F418U2 product page | Product catalogue | Current vendor page | EN | Not applicable | [BTicino product page](https://www.bticino.com/products/bt-f418u2) |

Once archived under [Device Sources](../../sources/devices/), these links should prefer the retained byte-for-byte originals while preserving the vendor URLs as provenance.

## Identification

| Evidence | Value | Status | Source |
| --- | --- | --- | --- |
| Catalogue item | `2065` | Implementation evidence | [Physical Devices](../../device-model/physical-devices.md#f418u2) |
| Catalogue description | `2x1,6A universal dimmer, 4DIN` | Implementation evidence | [Physical Devices](../../device-model/physical-devices.md#f418u2) |
| Firmware definition | `590` | Implementation evidence | [Physical Devices](../../device-model/physical-devices.md#f418u2) |
| `WHO 1001` / `DIMENSION 1` identity | Not yet curated on this page | Incomplete | - |
| Installed firmware versions | Not yet curated on this page | Incomplete | - |

The page deliberately does not infer an installed firmware version from the catalogue firmware-definition ID.

## Firmware and hardware

Firmware definition `590` declares two `slot` positions. The Device is therefore modelled as two dimmer Modules, not as one Device with a single logical address.

Virgin Object `528`, “Dimmer actuator virgin”, is placed at both slots and permits two concrete Object choices. The exact active Object on an installed Device must be established from configuration or diagnostic evidence.

## Functional profile

| Function / Object | Role | `WHO` | Module / `slot` | Notes |
| --- | --- | --- | --- | --- |
| Dimming actuator | Actuator | `WHO 1` Lighting | `1` | One dimmer channel |
| Dimming actuator | Actuator | `WHO 1` Lighting | `2` | One dimmer channel |

Vendor documentation states that the two channels can manage dimmable LED/CFL, halogen, and electronic-transformer loads. Configuration can be performed through MyHOME Suite or physical configurators.

## Diagnostic observations

The F418U2 is useful because first-hand traces already establish Device-specific runtime behavior beyond static catalogue capability.

| Surface | Observation | Status | Evidence |
| --- | --- | --- | --- |
| Functional `DIMENSION 1` | Fine dimming level plus a trailing secondary value is readable and writable on observed paths | Observed behavior | [WHO 1 DIMENSION reference](../../functional/who-1-lighting/dimensions.md) |
| Functional `DIMENSION 4` | Distinct fine-level state surface observed through MH202 and F454 | Observed behavior | [WHO 1 DIMENSION reference](../../functional/who-1-lighting/dimensions.md) |
| `DIMENSION 4` through MH200 | Explicit requests produced no response in the preserved public trace | Observed behavior, path-specific | [WHO 1 DIMENSION reference](../../functional/who-1-lighting/dimensions.md) |

At `LEVEL100 = 130`, controlled observation showed `DIMENSION 1` and `DIMENSION 4` carrying different trailing values. They must therefore not be collapsed into one state field merely because both include the same fine-grained level.

## Addressing and memberships

The Device exposes two dimmer Modules. Installed addresses and group memberships are installation state and do not belong in this product definition.

Product-specific limits on group membership are not yet curated on this page.

## Configuration

### Configuration methods

- Physical configurators - documented by the vendor.
- MyHOME Suite / virtual configuration - documented by the vendor and catalogue implementation.

The full Device-specific parameter and constraint model remains to be curated.

### Physical configuration

The installation instructions expose physical configurator sockets. Exact position names and all allowed values still need to be transcribed from authoritative Device documentation into this page.

### Virtual configuration

The canonical catalogue contains the firmware-specific configuration model for firmware `590`. It has not yet been normalized here into a complete parameter/constraint table.

## Programming

Use the canonical [Programming](../../programming/) workflows. Device-specific programming constraints remain incomplete here.

## Observed behavior

A public MH200/F418U2 trace and controlled observations through MH202 and F454 establish that gateway behavior can materially affect the functional dimmer surfaces exposed for the same Device.

This is a Device-path capability distinction, not evidence that the F418U2 itself changes protocol semantics between installations.

## Evidence

- **Implementation evidence** - `MHCatalogue.db` establishes item `2065`, firmware definition `590`, and the two-slot capability model.
- **Published/vendor documentation** - current BTicino product and installation documents establish the physical product, two-channel dimmer role, load classes, and configuration methods.
- **Observed behavior** - preserved and controlled runtime observations establish F418U2-specific `WHO 1` dimmer behavior across several gateway paths.

## Evidence limits

- The complete `WHO 1001` identity tuple is not yet curated into this page.
- The complete firmware-version applicability matrix is not yet curated.
- Physical and virtual configuration constraints remain incomplete.
- Gateway-dependent `DIMENSION 4` behavior is intentionally preserved as a bounded observation rather than generalized.

## Sources

- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Sources](../../sources/devices/)
- [Physical Devices](../../device-model/physical-devices.md#f418u2)
- [Virgin Objects](../../device-model/virgin-objects.md#dimmer-actuator-virgin)
- [WHO 1 DIMENSION reference](../../functional/who-1-lighting/dimensions.md)

## Related material

- [Device Model](../../device-model/)
- [Lighting - WHO 1](../../functional/who-1-lighting/)
- [Programming](../../programming/)
- [Open Questions](../../reverse-engineering/open-questions.md)
