# `WHO 6` - Basic Video Door Entry

`WHO 6` identifies the Basic Video Door Entry system in the known OpenWebNet namespace catalogue.

## Corpus status

The corpus includes the [L4686SDK Specification](../../sources/openwebnet-public/pdf/WHO_6_L4686SDK.pdf), version 1.0.0 dated 11 February 2009. Its eight pages contain `WHO 6` command/address tables and send/receive flows for cameras, calls, locks, and stair lighting. This is product-specific published evidence, not merely a namespace record and not a complete generic Video Door Entry specification.

The reference below preserves the source's product scope. Values from adjacent Video Door Entry systems must not be substituted for the L4686SDK evidence.

## L4686SDK reference

The command table and sections 1 and 2 establish these forms. Placeholders are symbolic, not captures.

| Operation | Published form | Applicability |
| --- | --- | --- |
| Camera ON | `*6*0*WHERE##` | `WHERE = 4000..4095`; riser form appends `#2` to `WHERE` |
| Camera OFF | `*6*9##` | No `WHERE` field in the published form |
| Stair light OFF / ON | `*6*11*WHERE##` / `*6*12*WHERE##` | L4686SDK address |
| Open lock | `*6*10*WHERE##` | `WHERE = 4000..4095`; riser form appends `#2` |
| Camera cycling | `*6*18*WHERE##` | `WHERE = 4000..4095`; source requires a preceding Camera ON; riser form appends `#2` |
| Incoming apartment call | `*6*6*WHERE##` | Receive section: `WHERE = 0..3999` |
| Incoming broadcast call | `*6*6*4100##` | Receive section; special value outside the endpoint range |
| Open lock with external unit in conversation | `*6*22*WHERE##` | Receive section: `WHERE = 4000..4095`; not evidence of a send operation |

For sending, the source describes ACK as confirmation that a frame was sent on the SCS bus, NACK as not sent, and `*#*x##` as an error-type form. It does not enumerate the `x` codes or establish the final physical effect. These are product-specific acknowledgement semantics.

## Source limits

The address table labels `4001` as endpoint 2 even though the adjacent entries suggest a different arithmetic correspondence. Preserve `4000..4095` as the stated wire range; do not infer an endpoint-number conversion from this inconsistent label.

Several response/receive rows print arrows inconsistent with their section headings and descriptions. The table above reports the sending/receiving section roles, not a repaired observed transcript. Exact direction and error-code behavior require product evidence. Camera OFF's short form and broadcast-call sentinel must not be normalized into the ordinary three-field command grammar.

## Protocol boundary

`WHO 6`, [`WHO 7`](../who-7-multimedia-video/), and [`WHO 8`](../who-8-video-door-entry-telephony/) are related by application domain but are independent protocol namespaces. A camera/video operation documented for `WHO 7`, for example, is not automatically valid under `WHO 6`.

Future values should be added only when supported by the MyHOME_Suite implementation corpus, a canonical specification, or observed wire behavior. Common frame syntax remains defined under [Protocol](../../protocol/).
