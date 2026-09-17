# Retrieve Configured CEN Buttons

## Goal

Answer the installer or application question: “Which CEN buttons are configured on this Physical Device?”

The result should cover every applicable Module on the Device and associate each configured button with its CEN identifier, Object, internal slot, and raw configuration evidence.

## Prerequisites

- an inventory entry from [Discover and Identify Devices](discover-devices.md);
- the Device interview and Module/Object model described in [Read and Present a Device Configuration](read-device-configuration.md);
- access to `MHCatalogue.db` and applicable `rules.db3` data;
- the ability to send and receive diagnostic frames as MyHOME_Suite does.

## 1. Build the complete Module list

Run the Device interview using the installed Device ID, diagnostic address, or local-interaction workflow described in [Read and Present a Device Configuration](read-device-configuration.md).

Process every `DIMENSION 30` response:

1. retain the Device-local internal `SLOT`;
2. resolve configured `KEYO` values against `EN_KEY_OBJECT.key_object`;
3. retain each resolved Object's internal `id_key_object`;
4. preserve unconfigured and unresolved Modules.

This is a Device-wide question. Do not stop after finding the first scenario-related Module.

## 2. Identify CEN-capable Object properties

For every configured Module, load the Object-scoped `EN_CONF` definitions using its `id_key_object` and `id_firmware = 0`.

Identify definitions whose resolved semantics represent:

- the CEN or Scheduled scenario PLUS number;
- an upper, lower, or numbered button;
- any Object-specific component required to decode those values.

Use property identity and semantics, not matching numeric values or a global index list. CEN-capable Objects do not all expose the same properties.

## 3. Request the detailed configuration

Send the canonical all-Module detailed-read request once:

`*#[WHO]*0*38#0##`

Collect the repeated responses during the MyHOME_Suite eight-second response window:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Join each response to a property through the resolved Module and `(SLOT, INDEX)`. Equal indices on different Modules remain separate values.

## 4. Decode a two-button Scheduled scenario PLUS Object

The catalogue defines one two-button “Scheduled scenario PLUS” Object with this Object-scoped property set:

| `INDEX` | Symbol | Meaning |
| ---: | --- | --- |
| 0 | `PPT_CEN_LOW` | low component of the Scheduled scenario PLUS/CEN number |
| 1 | `PPT_CEN_HIG` | high component of the Scheduled scenario PLUS/CEN number |
| 2 | `BUTTON_1` | upper button |
| 3 | `BUTTON_2` | lower button |

Suppose the detailed read yields these normalized values:

| `SLOT` | low | high | upper button | lower button |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 33 | 0 | 5 | 6 |
| 4 | 33 | 0 | 7 | 8 |

The user-facing result is:

- CEN 33, Module internal slot 3: upper button 5; lower button 6;
- CEN 33, Module internal slot 4: upper button 7; lower button 8.

Retain the four raw `DIMENSION 35` tuples behind each Module result.

## 5. Combine the CEN-number components cautiously

The `LOW` and `HIG` property names and catalogue ranges strongly indicate byte components. Where the combination rule has been independently established for the applicable Device family, decode them as:

`CEN = LOW + 256 × HIG`

Otherwise, present both raw components and mark the combined number as an evidence-backed inference. Do not silently promote the formula to a universal protocol rule.

CEN virtual addresses occupy the range `0` through `2047`; the effective Object, filter, and rule constraints still need to be applied.

## 6. Handle Object variants

Do not apply the four indices above to every CEN-capable Object.

For example:

- another “Scheduled scenario PLUS” Object variant exposes only one `BUTTON_1`;
- “Scheduled scenario” and “Scenario module control” Objects use other symbols and layouts;
- a property absent from the resolved Object definition is not the same as a property reported as zero;
- a defined property with no response is “not reported,” not automatically unconfigured.

The resolved Object's `EN_CONF` rows determine which button fields exist and how their values should be interpreted.

## 7. Build the result

Return one entry per applicable Module, including:

| Field | Purpose |
| --- | --- |
| Device ID | identifies the installed Physical Device |
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
Resolution status: resolved
```

See [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 35`](../diagnostics/dim35-configuration.md), [Configuration](../device-model/configuration.md), and [Configuration Reading](../diagnostics/configuration-reading.md).
