# CEN+

CEN+ functions are carried within the `WHO 25` namespace. They are distinct from the CEN button-event family under [`WHO 15`](../who-15-cen/).

## `WHAT`

The established CEN+ command/event range is `WHAT` `21` through `28`. The individual values represent CEN+ event forms and remain interpreted within `WHO 25`.

## Addressing

CEN+ uses a virtual address space rather than physical A/PL addressing. Established CEN virtual addresses range from `0` through `2047`.

A decoder should therefore resolve `WHO 25` and the selected CEN+ operation before interpreting `WHERE`; the value must not be parsed as a Lighting/Automation point-to-point address.

## Relationship to other `WHO 25` functions

`WHO 25` also carries dry-contact and IR functions. Sharing the same `WHO` does not make those operations CEN+; they are documented separately in [`dry-contact-ir.md`](dry-contact-ir.md).