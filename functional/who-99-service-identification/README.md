# Overview

The MyHOME_Suite `OPEN.db` protocol definitions represent `WHO 99` as Service Identification.

## Protocol role

Service Identification is a protocol service rather than an ordinary automation function such as Lighting, Automation or Thermoregulation. It remains under `functional/` because it occupies a known non-diagnostic `WHO` namespace and is carried using ordinary OpenWebNet functional framing.

The implementation data establishes a service-identification operation in the MyHOME_Suite protocol catalogue. This should be modeled separately from gateway authentication, connection/session selection and diagnostic device identification.

## Distinctions

| Mechanism | Purpose |
| --- | --- |
| `WHO 99` | Functional service identification namespace |
| Gateway authentication/session | Establishes access to the OpenWebNet gateway |
| Diagnostic `DIMENSION 1` / `13` etc. | Identifies/interviews physical Devices in diagnostic families |

A service-identification frame must therefore not be interpreted as a Device catalogue identity or diagnostic Device ID solely because all three mechanisms involve “identification”.

## Corpus status

The current corpus establishes the namespace and service operation but does not justify a broader inferred `WHAT` vocabulary. Unknown values remain unspecified. Session-level behavior is cross-referenced under [`../../protocol/`](../../protocol/), while physical Device identification belongs under [`../../diagnostics/`](../../diagnostics/).