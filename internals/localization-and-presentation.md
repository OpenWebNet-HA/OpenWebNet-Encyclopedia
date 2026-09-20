# Localization and Presentation

MyHOME Suite presentation combines stored catalogue text, resource keys, implementation metadata, and runtime/UI decisions. A protocol decoder should preserve those layers rather than collapsing them into one label.

## Label classes

| Concept | Preferred source | Notes |
| --- | --- | --- |
| Physical Device description | `EN_DEVICE.name` | standard MyHOME Suite-facing product description |
| Product code/SKU | `EN_DEVICE.code` | product identity, not a language key |
| Shared item description | `EN_ITEM.descr` | shared capability item, not necessarily a unique marketed product |
| Object description | `EN_KEY_OBJECT.descr` | logical function of one Module |
| Virgin Object description | `EN_VIRGIN_OBJECT.descr` | configurable role represented for a disabled Module in `DIMENSION 30` |
| Configuration label | `EN_CONF.descr`, `descr_ext`, and related metadata | property presentation in catalogue context |
| Scenario capability name | ScenarioDevices `Name` fields | commonly a localization/resource key, not final display text |
| Protocol operation label | `OPEN.db.EN_OPEN.open_label` | implementation operation label, not a public protocol name |

One Physical Device can have one standard Device description and several Module/Object descriptions. Displaying an Object description as the Device name loses the product-level identity.

## Resource keys

ScenarioDevices keys encode structure such as functional family, role, Object, and Command. They are useful stable evidence within a source revision, but their translated strings are not stored in the four capability tables.

A presentation layer should retain the source database and revision, raw resource key, resolved localized label if available, locale, fallback label, and unresolved-key status.

Do not compare capabilities solely through translated strings. Translation can change while the underlying resource key remains the same, and one key can occur in multiple category paths.

## UI numbering and `slot` positions

MyHOME Suite can hide `slot` positions or renumber visible Modules. The presentation layer must keep the protocol `SLOT`, catalogue placement, UI-visible Module number or name, and hidden/absent state as separate fields.

Never rewrite the Device-local `slot` to match the UI.

## Visibility and editability

Catalogue metadata such as `visible`, `hidden`, `read_only`, `fixed_ko`, and conditions contributes to UI behavior, but no one flag is a complete presentation rule.

A fixed Object can still expose editable configuration. A hidden property can participate in conversions. An Object alternative can exist in the catalogue but be suppressed by a `slot` condition. A `slot` can exist while being absent from a particular UI view.

Use observed UI behavior as presentation evidence and catalogue structures as capability evidence. Do not infer wire encoding from a label or widget alone.

## Terminology normalization

Repository prose uses **Physical Device**, **Module**, **`slot`**, **Object**, **Configuration**, and **Virtual configuration**. Database names such as `KEYO`, `ko slot`, and `id_key_object` are retained when quoting fields, but do not replace reader-facing terminology.

## Unknown localization mechanism

The corpus establishes stored text and resource-key usage but does not preserve the complete resource bundle or application code that resolves every key. It therefore does not establish fallback locale order, missing-key behavior, runtime culture selection, or formatting rules for composed labels.

Document raw keys whenever the final localized string cannot be reproduced.
