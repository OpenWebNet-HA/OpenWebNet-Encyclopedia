# `WHO 12` - Messages

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 12` as Messages.

## Corpus status

The functional namespace is directly established, but the currently integrated evidence does not support a complete authoritative `WHAT`, `WHERE`, or `DIMENSION` reference. No dedicated `WHO 12` PDF is present in the canonical public corpus used by this repository.

## Interpretation rule

The generic name “Messages” is not sufficient to infer payload encoding, recipient addressing, text representation, notification type, or acknowledgement behavior. Those semantics remain unknown until supported by implementation definitions or captured traffic.

OpenWebNet parsers should still recognize `WHO 12` and retain its fields losslessly. This permits later decoding while keeping unknown protocol values distinct from generic `ACK`/`NACK` frames and from application messages transported outside this `WHO` namespace.

Common frame/session concepts remain documented under [`../../protocol/`](../../protocol/).