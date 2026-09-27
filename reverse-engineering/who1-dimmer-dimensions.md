# WHO 1 Dimmer `DIMENSION 1` and `4` Observations

This page records the evidence path behind the functional WHO 1 reference for dimmer `DIMENSION 1` and `DIMENSION 4`. It separates published semantics, captured runtime behavior, tester-reported behavior, and remaining interpretation.

The raw captures are private because they contain installation-specific topology. The exchanges below use `WHERE` placeholders while preserving the relevant frame structure.

## Evidence set

| Evidence | Scope | Fingerprint / status |
| --- | --- | --- |
| F418U2 through F454 | same installed F418U2 channel; F454 firmware 2.0; 27 September 2026 | SHA-256 `6e73dd5ea8f6b63ff01d7ba7200d72a3821fc4c0bb74acff54be86a6cebd2e8b` |
| F418U2 through MH202 | same installed F418U2 channel; MH202 firmware 1.0; 27 September 2026 | SHA-256 `96c7e7b19e995cd5f5ad1c658901337e6ba1ae18f349bf602df57fa0533c564e` |
| F414 through MH200 | F414 classic modular dimmer; MH200 firmware 2.1.0; 26 September 2026 | SHA-256 `6a0e4dc6c6c2caa3c1fbbf004d6c177cf7c0ee77dacc0d1508d3caebad20975d` |
| F414 DIM4 request result | same tester/session family as the F414 capture | tester reported timeout after about two seconds followed by `NACK`; raw DIM4 exchange not present in the preserved capture |

The two F418U2 captures provide a controlled gateway comparison because the actuator and installed channel are the same while the gateway changes.

## Published boundary

The WHO 1 specification defines:

- `DIMENSION 1` as level plus transition speed, with the documented `LEVEL100 + SPEED` form;
- `DIMENSION 4` as 100-level dimmer status with ON/OFF speed.

The specification does not provide the same detailed payload and flow definition for `DIMENSION 4` that it provides for `DIMENSION 1`. Runtime observations must therefore remain scoped to the tested Device and gateway combinations.

## F418U2: distinct secondary state

At the same fine brightness level, the actuator emitted different secondary values:

~~~text
DIMENSION 1 report: *#1*<WHERE>*1*130*5##
DIMENSION 4 report: *#1*<WHERE>*4*130*2##
~~~

This establishes for the tested F418U2 that the two secondary values are not interchangeable representations of one state field.

It does **not** by itself establish:

- the physical-time unit or scale of the `DIMENSION 4` value `2`;
- that `DIMENSION 1` speed applies only to intermediate-level transitions;
- the full behavioral boundary of the published term `ON/OFFspeed`.

Those remain interpretation questions.

## Gateway-dependent read behavior

### MH202

When the F418U2 was OFF:

~~~text
TX *#1*<WHERE>*1##
RX *#1*<WHERE>*1*100*0##

TX *#1*<WHERE>*4##
RX *#1*<WHERE>*4*100*0##
~~~

At `LEVEL100 = 130`, direct reads similarly preserved the requested dimension and returned a trailing `0` in the sampled state:

~~~text
TX *#1*<WHERE>*1##
RX *#1*<WHERE>*1*130*0##

TX *#1*<WHERE>*4##
RX *#1*<WHERE>*4*130*0##
~~~

State-changing traffic later exposed nonzero actuator reports such as `DIMENSION 1 ...*130*5##` and `DIMENSION 4 ...*130*2##`.

### F454

When the same F418U2 was OFF, the F454 answered a `DIMENSION 1` request using `DIMENSION 4`:

~~~text
TX *#1*<WHERE>*1##
RX *#1*<WHERE>*4*100*2##
~~~

An explicit `DIMENSION 4` request at the same state also returned `DIMENSION 4 ...*100*2##`.

At `LEVEL100 = 130`, the F454 direct reads returned the nonzero state values observed in that capture:

~~~text
DIMENSION 1 -> *#1*<WHERE>*1*130*5##
DIMENSION 4 -> *#1*<WHERE>*4*130*2##
~~~

The evidence therefore rejects a universal client rule that a `DIMENSION 1` request must receive a `DIMENSION 1` response.

## `DIMENSION 4` write behavior

### MH202/F418U2 positive-level write

A positive `DIMENSION 4` write succeeded:

~~~text
TX *#1*<WHERE>*#4*130*0##
...
RX *#1*<WHERE>*4*130*2##
~~~

The same capture also includes a `DIMENSION 4` write with `LEVEL100 = 100`; its subsequent state is ambiguous and does not establish that the write form is a reliable substitute for an ordinary OFF command.

### F454/F418U2 positive-level write

The equivalent positive write:

~~~text
TX *#1*<WHERE>*#4*130*0##
~~~

did not produce the expected level/status transition in the sampled F454 run. A following `DIMENSION 1` write to the same fine level did produce the expected `DIMENSION 1` report.

This is meaningful negative evidence because the connection remained healthy and the immediately following alternative write succeeded. It remains scoped to the tested F454 firmware and state; it is not yet a universal rejection rule.

## Classic F414 boundary

The F414/MH200 capture establishes that a classic dimmer supports `DIMENSION 1` read and write:

~~~text
TX *#1*<WHERE>*1##
RX *#1*<WHERE>*1*200*2##

TX *#1*<WHERE>*#1*150*0##
RX *#1*<WHERE>*1*150*5##
~~~

The same capture also shows fine `LEVEL100` values after coarse `WHAT` commands, including values not equal to the nominal decimal percentage.

A companion tester report states that:

~~~text
*#1*<WHERE>*4##
~~~

received no DIM4 response, timed out after about two seconds, and ended in `NACK`. Because that exchange is not present in the preserved capture, classify it as a reported observation pending a directly preserved trace. It supports, but does not yet independently establish, that DIM4 is unavailable on the tested F414.

## Current conclusions

| Claim | Confidence and scope |
| --- | --- |
| F414 and F418U2 can use WHO 1 `DIMENSION 1` for fine level state/control | Established in the preserved captures for the tested Device/gateway combinations |
| F418U2 `DIMENSION 1` and `DIMENSION 4` expose distinct secondary values at the same `LEVEL100` | Established for the tested F418U2 |
| F418U2 DIM4 reads work through both MH202 and F454 | Established in the two preserved captures |
| F418U2 positive DIM4 write works through MH202 | Established in the preserved MH202 capture |
| F454 can answer an OFF-state DIM1 request with DIM4 | Established for the tested F454/F418U2 combination |
| F454 universally rejects DIM4 writes | Not established; one controlled negative observation |
| F414 does not support DIM4 | Supported by tester report, but raw DIM4 exchange still needed for capture-established status |
| DIM4 trailing values have a known physical-time mapping | Unknown |
| MH202 DIM4 trailing `0` has the same formal meaning as DIM1 `SPEED = 0` | Unknown |

## Implementation consequences

A robust WHO 1 implementation should:

- preserve `DIMENSION 1` and `DIMENSION 4` as distinct state surfaces;
- tolerate a response dimension that differs from the requested dimension when gateway-specific evidence permits it;
- treat DIM4 read/write support as Device- and gateway-dependent capability rather than a universal dimmer property;
- avoid interpreting DIM4 trailing values with the published DIM1 `SPEED` table unless independent evidence establishes that mapping.

## Remaining experiments

The highest-value follow-up observations are:

1. preserve a raw F414/MH200 DIM4 request through timeout/NACK;
2. repeat the F454 positive DIM4 write to distinguish systematic gateway behavior from state-dependent failure;
3. vary a known ON/OFF fade setting on an F418U2 while holding level and DIM1 speed constant, then compare DIM4;
4. test DIM1 and DIM4 across additional classic and modern gateways to determine whether the observed query behavior clusters by model, firmware, or gateway family.

See the canonical [WHO 1 DIMENSION Reference](../functional/who-1-lighting/dimensions.md) for the operational result.
