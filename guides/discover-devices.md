# Discover Devices

## Goal

Build a deduplicated inventory of installed Devices for one diagnostic `WHO` without inventing candidate product identities.

## Prerequisites

- an authenticated OpenWebNet connection;
- the diagnostic `WHO` for the target system;
- per-pass timeout handling;
- a collector that preserves raw frames.

## Inputs

| Input | Purpose |
| --- | --- |
| diagnostic `WHO` | selects the management family |
| discovery scope | all, configured, or unconfigured Devices |
| retry policy | distinguishes silence from a completed pass |

## Procedure: discovery by Device ID

1. Send `*[WHO]*12*0##` to release prior enumeration state.
2. Send `*#[WHO]*0*13##`.
3. Collect `*#[WHO]*[WHERE]*13*[ID]##` responses during the four-second Suite discovery window.
4. For every new ID, send `*[WHO]*11#[ID]*0##` to suppress it during the active enumeration.
5. Repeat the same request.
6. Treat a complete pass with no new response as the capture-supported end condition.
7. Send `*[WHO]*12*0##` again to release scan state.

Use `*#[WHO]*0*13#1##` or `*#[WHO]*0*13#0##` only when the configured/unconfigured filter is intentionally required. Those frames exist in `OPEN.db` but are not the ordinary `ScanAID` member.

## Inventory record

For every response retain:

- raw ID field;
- normalized eight-character hexadecimal display;
- response `WHERE`;
- diagnostic `WHO`;
- first and last observation times;
- scan pass;
- duplicate count.

Deduplicate by the full 32-bit Device ID, not by `WHERE`. The Device ID is an installed-instance identifier, not a SKU, catalogue key, Object number, or functional address.

## Alternative discovery

Use [Address Discovery](../diagnostics/address-discovery.md) when ID enumeration is unavailable or a known diagnostic address must be probed. Use local-button discovery to select one physically accessible Device when neither ID nor address is sufficient. Local interaction is a selection workflow outside the payload and uses a longer first-response window.

## Validation gates

- Do not declare the bus empty from one silent request.
- Do not merge Devices because their `WHERE` values match.
- Do not decode every `WHERE` as `A`/`PL`.
- Do not leave Devices suppressed; always release scan state.

## Expected result

A Device inventory keyed by normalized 32-bit ID, with raw response evidence and no catalogue identity claimed yet.

See [Device Discovery](../diagnostics/device-discovery.md) and [Diagnostic Architecture](../diagnostics/architecture.md).
