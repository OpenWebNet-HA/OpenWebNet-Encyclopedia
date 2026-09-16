# Addressing

Temperature Control uses its own zone-oriented `WHERE` grammar rather than the A/PL grammar used by Lighting and Automation.

The MyHOME_Suite 3.5.38 `OPEN.db` address-rule definitions include:

| Form | Purpose |
| --- | --- |
| `[ZA][ZB]` | Temperature-control zone |
| `[ZAZB]` | Advanced zone form |
| `#0#[ZA][ZB]` | Four-zone central-unit form |
| `[ZA][ZB]#[N]` | Temperature-control actuator form |

The selected `WHO 4` operation determines which address form is valid. See [`../../protocol/addressing.md`](../../protocol/addressing.md) for the common address-rule model.