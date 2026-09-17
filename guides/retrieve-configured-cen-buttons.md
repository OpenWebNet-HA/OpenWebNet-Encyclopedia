# Retrieve Configured CEN Buttons

## Goal

Answer the installer or application question: “Which CEN buttons are configured on this Physical Device?”

Starting only with a way to select the installed Device, this guide obtains the raw frames, resolves every Module and Object, identifies CEN-capable Objects, and returns each configured button with its CEN identifier and provenance.

## Prerequisites

- a Device selector: preferably its discovered 32-bit ID, otherwise a diagnostic address or local-interaction workflow;
- the applicable diagnostic `WHO`;
- access to `MHCatalogue.db` and applicable `rules.db3` data;
- the ability to establish the required session and send and receive frames as MyHOME_Suite does;
- raw frames retained in arrival order.

No previously captured interview or configuration response is assumed.

## 1. Interview the selected Device

Start one of these selection workflows:

| Selection method | Send |
| --- | --- |
| Device ID | `*[WHO]*10#[ID]*0##` |
| diagnostic address | `*#[WHO]*[WHERE]*0##` |
| local interaction | `*[WHO]*5*0##`, then perform the Device-side interaction |

A Device ID is represented as eight hexadecimal characters.

Collect the initial stream in arrival order. The frames needed by this guide are:

- `DIMENSION 1` for catalogue identity;
- `DIMENSION 2`, `3`, and `6` where reported, for firmware resolution;
- repeated `DIMENSION 30` records for the Module/Object layout;
- `DIMENSION 13` for the installed Device ID;
- applicable `DIMENSION 31` errors;
- Device `WHAT 4` as the normal interview terminator.

Use the applicable 15-second first-response window for ID/address selection or the 300-second local-interaction window, followed by the 20-second further-information window used by MyHOME_Suite. Record whether `WHAT 4`, abort, timeout, or transport closure ended collection.

## 2. Resolve the Device, Modules, and Objects

Resolve `DIMENSION 1` through the catalogue and use `EN_DEVICE.name` as the preferred Physical Device description. Retain candidate brands, collections, SKUs, and firmware when identity is not unique.

Parse every Module record:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

For each response:

1. use protocol `SLOT` as the Device-local internal-slot key;
2. if `STATE=1`, resolve `KEYO` against `EN_KEY_OBJECT.key_object`;
3. if `STATE=0`, resolve it against `EN_VIRGIN_OBJECT.virgin_key_object` and mark the Module unconfigured;
4. retain the configured Object's internal `id_key_object`;
5. attach any `DIMENSION 31` error without discarding a valid Module record.

This is a Device-wide question. Do not stop after the first scenario-related Module, and do not renumber internal slots to match MyHOME_Suite's visible Module numbering.

## 3. Identify CEN-capable Object properties

For every configured Module, load both applicable configuration scopes:

- Object-scoped `EN_CONF` rows using its `id_key_object` and `id_firmware = 0`;
- firmware-scoped rows using `id_key_object = 0` and the resolved firmware.

The zero is a “not applicable” sentinel on the unused ownership axis.

Identify definitions whose resolved semantics represent:

- the CEN or Scheduled scenario PLUS number;
- an upper, lower, or numbered button;
- any Object-specific component required to decode those values.

Use property identity and semantics, not matching numeric values or a global index list. CEN-capable Objects do not all expose the same properties.

## 4. Request the detailed configuration

After the complete Module/Object layout is known, send once:

`*#[WHO]*0*38#0##`

Collect the repeated responses during the MyHOME_Suite eight-second response window:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Join each response to a property through the resolved Module and `(SLOT, INDEX)`. Equal indices on different Modules remain separate values.

Retain applicable `DIMENSION 39` property errors. Keep any `DIMENSION 310` response outside the generic indexed-property model because it carries no `INDEX`.

A one-Module `DIMENSION 38` form exists, but the canonical `DiagKO` sequence uses the all-Module request above. The source also uses reset terminology for `DIMENSION 38`; preserve that ambiguity and exercise caution with unfamiliar Devices.

## 5. Decode a two-button Scheduled scenario PLUS Object

The catalogue defines one two-button “Scheduled scenario PLUS” Object with this Object-scoped property set:

| `INDEX` | Symbol | Meaning |
| ---: | --- | --- |
| 0 | `PPT_CEN_LOW` | low component of the Scheduled scenario PLUS/CEN number |
| 1 | `PPT_CEN_HIG` | high component of the Scheduled scenario PLUS/CEN number |
| 2 | `BUTTON_1` | upper button |
| 3 | `BUTTON_2` | lower button |

Suppose the detailed read yields:

| `SLOT` | low | high | upper button | lower button |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 33 | 0 | 5 | 6 |
| 4 | 33 | 0 | 7 | 8 |

The user-facing result is:

- CEN 33, Module internal slot 3: upper button 5; lower button 6;
- CEN 33, Module internal slot 4: upper button 7; lower button 8.

Retain the four raw `DIMENSION 35` tuples behind each Module result.

## 6. Combine and validate the values

For each selected property:

1. load `EN_CONF_RANGE`;
2. apply applicable `EN_FILTER`, `EN_FILTER_RANGE`, conditions, conversion rules, and `rules.db3` dependencies;
3. retain the selected `EN_CONF.id_conf`, raw `VAL_PAR`, and decoded value;
4. flag values outside the effective domain rather than discarding them.

The `LOW` and `HIG` names and catalogue ranges strongly indicate byte components. Where the combination rule has been independently established for the applicable Device family, decode them as:

`CEN = LOW + 256 × HIG`

Otherwise, show both raw components and mark the combined number as an evidence-backed inference. Do not silently promote the formula to a universal protocol rule.

CEN virtual addresses occupy the range `0` through `2047`; the effective Object, filter, and rule constraints still apply.

## 7. Handle Object variants and missing evidence

Do not apply the four indices above to every CEN-capable Object.

For example:

- another “Scheduled scenario PLUS” Object variant exposes only one `BUTTON_1`;
- “Scheduled scenario” and “Scenario module control” Objects use other symbols and layouts;
- a property absent from the resolved Object definition is not the same as a property reported as zero;
- a defined property with no response is “not reported,” not automatically unconfigured.

Also:

- if the interview does not terminate normally, return the partial result with its completion status;
- if Device, firmware, Object, or property resolution remains ambiguous, retain all compatible candidates;
- if a value violates its effective domain, preserve it with a warning;
- if no configured Object exposes CEN-button properties, return an empty list with the successful interview and resolution evidence.

## 8. Build the result

Return one entry per applicable Module:

| Field | Purpose |
| --- | --- |
| Device ID | identifies the installed Physical Device |
| Device | preferred `EN_DEVICE.name` |
| internal slot | preserves the protocol Module key |
| Object | identifies the configured Module function |
| CEN number | decoded identifier, or raw low/high components |
| buttons | Object-defined button names and decoded values |
| raw properties | exact `INDEX` and `VAL_PAR` tuples |
| status | resolved, inferred, ambiguous, not reported, or error |
| provenance | selected `id_key_object` and `id_conf` records |

## Expected result

```text
Device ID: 007B269D
Device: <resolved EN_DEVICE.name>
CEN Modules:
  - internal slot 3
    Object: Scheduled scenario PLUS
    CEN: 33
    upper button: 5
    lower button: 6
  - internal slot 4
    Object: Scheduled scenario PLUS
    CEN: 33
    upper button: 7
    lower button: 8
Interview status: complete
Resolution status: resolved
```

See [Device Discovery](../diagnostics/device-discovery.md), [Device Interview](../diagnostics/device-interview.md), [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 35`](../diagnostics/dim35-configuration.md), [Configuration](../device-model/configuration.md), and [Configuration Reading](../diagnostics/configuration-reading.md).
