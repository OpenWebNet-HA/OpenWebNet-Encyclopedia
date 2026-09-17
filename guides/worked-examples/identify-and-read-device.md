# Identify and Read a Device

## Goal

Demonstrate the evidence chain from one discovered 32-bit Device ID to a structured installed-state record.

## Example outline

1. Enumerate one diagnostic family.
2. Normalize the returned Device ID to eight hexadecimal characters.
3. Interview that exact ID.
4. Resolve `DIMENSION 1` to item and candidate Device records.
5. Select the preferred `EN_DEVICE.name` description.
6. Build Modules from `DIMENSION 30` using `STATE` to choose the Object or Virgin Object namespace.
7. Attach `DIMENSION 32` by internal slot.
8. Resolve `DIMENSION 35` only after Object and firmware context exists.
9. Record optional omissions and the terminal condition.

## Evidence table

| Stage | Raw evidence | Resolved result | Status |
| --- | --- | --- | --- |
| discovery | to be supplied | Device instance | pending |
| identity | to be supplied | item and candidate SKU set | pending |
| Modules | to be supplied | Object/Virgin Object per slot | pending |
| addresses | to be supplied | system-specific decoded tuples | pending |
| parameters | to be supplied | context-resolved properties | pending |

This first draft intentionally contains no invented capture. A captured Device can be inserted later without changing the procedure.
