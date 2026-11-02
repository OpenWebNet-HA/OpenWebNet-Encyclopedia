# `WHO 9` - Auxiliaries

`WHO 9` defines the OpenWebNet Auxiliaries system. Auxiliary channels provide general-purpose binary/event functions that can also appear as references from other systems, including the published `WHO 5` Alarm addressing model.

## Namespace semantics

`WHAT`, `WHERE`, and any structured values are scoped to `WHO 9`. An auxiliary number is not an Automation `A`/`PL` address and should not be normalized as one.

The Alarm specification's references to AUX targets demonstrate cross-system use of auxiliary channels, but do not make `WHO 9` part of the Alarm namespace. Integrations should preserve the originating `WHO` when correlating such events.

## Corpus status

The current integrated corpus establishes the Auxiliaries namespace and its use by MyHOME_Suite, but does not justify a complete independent `WHAT`/`DIMENSION` table beyond supported implementation evidence. Unknown values remain unspecified rather than inferred from generic binary-control behavior.

The historical BTicino touchscreen library and exact tests at `TS10_1_0_23` establish the following narrower status model:

| Operation | Implemented form | Client interpretation |
| --- | --- | --- |
| Request auxiliary status | `*#9*WHERE##` | Sent during device initialization |
| Receive ON indication | `*9*1*WHERE##` | Boolean true |
| Receive OFF indication | `*9*0*WHERE##` | Boolean false |

The decoder requires a command/event frame and an exact match of the complete configured `WHERE`; other `WHAT` values yield no status update. Its `DIM_STATUS` identifier is a local library value, not a wire `DIMENSION`. This evidence does not establish an auxiliary-address range, a dimension read/write vocabulary, or a physical response/acknowledgement sequence.

The library forwards repeated ON/OFF reports. Its scenario-condition consumer applies a separate policy: the first matching report can trigger, while repeated matches are suppressed until a nonmatching report arrives. See [historical touchscreen condition evaluation](../../scenario-engine/execution-model.md#historical-touchscreen-condition-evaluation) for initialization and condition-change behavior.

Alarm auxiliary-source configuration selects the separate `WHO 5` technical-alarm path; its source-number limits do not define the `WHO 9` address domain. Sound-source entries labelled AUX instead use the [`WHO 16`](../who-16-sound-system/) / [`WHO 22`](../who-22-sound-diffusion/) sound dialects. See [auxiliary implementation evidence](../../project/review/myopencommunity-auxiliary-history-review.md) for the scoped tests and historical corrections.

The physical `AUX` plug, the numeric channel in an `AUX` socket and an analogue audio connector marked AUX have distinct roles. Manufacturer-defined configuration examples are maintained in [SCS Configurator Labels](../../device-model/configurators.md#positions-and-functions); neither a shared label nor a product's channel range establishes one universal auxiliary wire grammar.

See [Protocol](../../protocol/) for common frame syntax and [`WHO 5` - Alarm](../who-5-alarm/) for Alarm-side AUX references.

## MH202 implementation evidence

MH2021.0.24 packages auxiliary translation and state-machine plugins with criterion `9`. In one explicitly supplied postparsed ordinary case, `WHAT 3`, `WHERE 5` and parsed kind `1` produce internal bytes `B0 00 9B 50`, represented as ASCII `B0009B50`. A separately supplied reverse input through the selected opcode path constructs candidate `*9*3*5##`. These are static source/format results, not serial captures, native parser acceptance or a causal physical exchange. No physical meaning is assigned to `WHAT 3`.

The selected application handler has unsigned numeric guards `WHERE <=15` and `WHAT <=10`; the standalone translation body does not apply the same WHERE guard. These are separate local contracts, not a universal address or command-support table. Forward output copies the source ID but does not initialize status offset `52` in the inspected allocation/helper stores; reverse output copies status and ID from its separately supplied input. A local ACK request is distinct from physical completion. See the [auxiliary translation report](../../project/review/firmware-analysis/mh202-1.0.24/run19-coso-report.txt) and [independent source review](../../project/review/firmware-analysis/mh202-1.0.24/run19-coso-review.txt). The historical touchscreen decoder's `WHAT 0/1` Boolean interpretation above remains scoped to that implementation.

A later [original parser and copy-helper test](../../reverse-engineering/firmware-analysis/mh202-1.0.24-record-and-script-lifecycle.md#auxiliary-field-records-use-a-command-directed-copy) constructs an actual kind1 object from supplied `*9*3*5##` and copies its fields into a distinct command-directed envelope. Helper selector4 controls output metadata, not parsed kind4 or ACK semantics. This supplements the selected grammar evidence under explicit private models; it does not execute the internal-body translation or a physical transaction.
