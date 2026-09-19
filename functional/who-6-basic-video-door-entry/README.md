# `WHO 6` - Basic Video Door Entry

`WHO 6` identifies the Basic Video Door Entry system in the known OpenWebNet namespace catalogue.

## Corpus status

The corpus includes the [L4686SDK Specification](../../sources/openwebnet-public/pdf/WHO_6_L4686SDK.pdf), version 1.0.0 dated 11 February 2009. Its eight pages contain `WHO 6` command/address tables and send/receive flows for cameras, calls, locks, and stair lighting. This is product-specific published evidence, not merely a namespace record and not a complete generic Video Door Entry specification.

The current page does not yet integrate that product-specific grammar. Phase 4 must review its applicability and internal discrepancies before adding the detailed reference. Values from adjacent Video Door Entry systems must not be substituted for the available L4686SDK evidence.

## Protocol boundary

`WHO 6`, [`WHO 7`](../who-7-multimedia-video/), and [`WHO 8`](../who-8-video-door-entry-telephony/) are related by application domain but are independent protocol namespaces. A camera/video operation documented for `WHO 7`, for example, is not automatically valid under `WHO 6`.

Future values should be added only when supported by the MyHOME_Suite implementation corpus, a canonical specification, or observed wire behavior. Common frame syntax remains defined under [Protocol](../../protocol/).
