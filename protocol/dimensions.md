# Overview

A `DIMENSION` identifies a property that can be requested, reported, or, where supported, written through an OpenWebNet `DIMENSION` frame.

`DIMENSION` identifiers are scoped to `WHO`. The semantic identity of a `DIMENSION` is therefore `(WHO, DIMENSION)`.

## Frame forms

| Operation | Syntax |
| --- | --- |
| Request | `*#WHO*WHERE*DIMENSION##` |
| Response | `*#WHO*WHERE*DIMENSION*VALUE...##` |
| Write | `*#WHO*WHERE*#DIMENSION*VALUE...##` |

`VALUE...` represents the ordered values defined by the selected `DIMENSION`. A `DIMENSION` can have one value, several values, or a system-specific structured layout.

## Semantics

The numeric `DIMENSION` identifier alone is insufficient to determine meaning. A `DIMENSION` used by Lighting can have entirely different semantics from the same numeric identifier used by Sound or a diagnostic `WHO`.

`DIMENSION` reference tables therefore belong with their respective systems. This page defines only the common transport form.

## Read and write capability

The existence of a `DIMENSION` does not imply that it supports both read and write operations. Capability must be established for the specific `(WHO, DIMENSION)` pair. Implementations should model request, response, write, and asynchronous-report capabilities separately where the system distinguishes them.

## Values

`DIMENSION` values are transmitted as ordered `*`-separated fields. Their type, range, padding, enumeration, and interpretation are `DIMENSION`-specific. Implementations should preserve the field ordering defined by the corresponding reference rather than treating a response as an unordered set of values.

See [`frame-syntax.md`](frame-syntax.md) for the complete frame grammar and [`addressing.md`](addressing.md) for `WHERE`.