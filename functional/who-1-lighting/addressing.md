# Addressing

Lighting uses the A/PL addressing family represented by the common OpenWebNet `WHERE` field.

The MyHOME Suite 3.5.38 address-rule database distinguishes several Lighting/Automation forms, including point-to-point `[A][PL]`, environment `[A]`, and advanced variants using the corresponding extended syntax. Address interpretation is therefore determined by the selected address rule rather than by treating every numeric `WHERE` as a point-to-point address.

See [`../../protocol/addressing.md`](../../protocol/addressing.md) for the common address-rule model.