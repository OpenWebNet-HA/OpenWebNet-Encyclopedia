# `WHO 19` — Interface

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 19` as Interface.

## Evidence boundary

The implementation corpus establishes the namespace, but the currently integrated evidence does not support a complete authoritative `WHAT`, `WHERE`, or `DIMENSION` vocabulary. This is a meaningful protocol result: `WHO 19` is known to exist, while the semantics of unsupported numeric fields remain unknown.

## Implementation guidance

Generic parsers should retain `WHO 19` frames losslessly even when a field is not yet decoded. Unknown `WHAT`, `WHERE`, parameters, and `DIMENSION` values should be represented as raw protocol values rather than mapped to nearby functional systems.

In particular, the name Interface does not establish that `WHO 19` uses the F422 advanced-address rules or any other specific interface-device grammar. Such a mapping requires direct implementation or wire evidence.

Future additions should distinguish direct MyHOME_Suite definitions from inferred behavior according to the repository provenance rules.