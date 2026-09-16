# Protocol

`WHO 24` is the Lighting Management namespace. It is distinct from ordinary [`WHO 1`](../who-1-lighting/) Lighting and uses a specialized sender/recipient structure rather than simply reusing the `WHO 1` point-to-point command model.

The public corpus contains a dedicated `WHO 24` specification. `WHAT`, sender, recipient, and any additional parameters must therefore be decoded according to that system-specific grammar.

Applications should expose `WHO 24` as Lighting Management while cross-linking it with Lighting for functional navigation; the two protocol namespaces remain independent.