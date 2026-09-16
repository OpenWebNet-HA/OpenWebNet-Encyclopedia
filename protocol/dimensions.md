# Overview

A Dimension identifies a property that can be requested, reported, or, where supported, written through an OpenWebNet Dimension frame.

Dimension identifiers are scoped to `WHO`. The semantic identity of a Dimension is therefore `(WHO, DIMENSION)`.

## Frame forms

| Operation | Syntax |
| --- | --- |
| Request | `*#WHO*WHERE*DIMENSION##` |
| Response | `*#WHO*WHERE*DIMENSION*VALUE...##` |
| Write | `*#WHO*WHERE*#DIMENSION*VALUE...##` |

`VALUE...` represents the ordered values defined by the selected Dimension. A Dimension can have one value, several values, or a system-specific structured layout.

## Semantics

The numeric Dimension identifier alone is insufficient to determine meaning. A Dimension used by Lighting can have entirely different semantics from the same numeric identifier used by Sound or a diagnostic `WHO`.

Dimension reference tables therefore belong with their respective systems. This page defines only the common transport form.

## Read and write capability

The existence of a Dimension does not imply that it supports both read and write operations. Capability must be established for the specific `(WHO, DIMENSION)` pair. Implementations should model request, response, write, and asynchronous-report capabilities separately where the system distinguishes them.

## Values

Dimension values are transmitted as ordered `*`-separated fields. Their type, range, padding, enumeration, and interpretation are Dimension-specific. Implementations should preserve the field ordering defined by the corresponding reference rather than treating a response as an unordered set of values.

See [`frame-syntax.md`](frame-syntax.md) for the complete frame grammar and [`addressing.md`](addressing.md) for `WHERE`.