# Overview

`WHO 25` contains several transversal OpenWebNet functions. The `WHO` namespace is the canonical location even though the functions use different `WHAT`, parameter, and `WHERE` grammars.

## Functions

| Function | Reference | Established range |
| --- | --- | --- |
| CEN+ | [`cen-plus.md`](cen-plus.md) | `WHAT 21`–`28`, virtual pushbutton `0`–`31`, virtual Object `0`–`2047` |
| Dry contact / IR | [`dry-contact-ir.md`](dry-contact-ir.md) | `WHAT 31`–`32`, state/event parameter `0`/`1` |

The [functional overview](../) also links these pages from their corresponding functional areas. A parser must select the `WHO 25` function before interpreting its parameters or `WHERE`.