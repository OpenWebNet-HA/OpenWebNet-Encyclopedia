# Authentication

OpenWebNet authentication occurs after the client selects a connection session and before normal session traffic is accepted. It authenticates the client to the OpenWebNet server; it does **not** encrypt or integrity-protect subsequent functional traffic.

A gateway can also allow configured client IP addresses to connect without an OPEN password. A client must follow the server's response rather than assume that every connection enters a challenge.

## Authentication selection

The HMAC specification adds an optional algorithm-declaration frame sent by the server after session selection:

| Server frame | Authentication method |
| --- | --- |
| No `*98*Y##` declaration; legacy challenge follows | Legacy OPEN password algorithm |
| `*98*1##` | HMAC using SHA-1 |
| `*98*2##` | HMAC using SHA-256 |

A client that supports the declared method answers with `ACK`. If it answers `NACK`, the server closes the connection. If the client's address is in the configured open range, authentication can be skipped even when HMAC support exists.

`WHO 98` here is a connection-negotiation namespace, not an ordinary functional system.

## Legacy OPEN authentication

The introductory specification establishes that password-protected sessions can use the older OPEN challenge-response algorithm. In this mode the server sends an operations/challenge frame rather than an HMAC declaration, and the client computes the legacy password response.

The detailed transformation is historically documented outside the canonical files currently preserved in this repository. This reference therefore records the negotiation boundary without reproducing an unverified implementation from a third-party library.

An implementation should keep the legacy algorithm behind a dedicated compatibility interface and test it against a real gateway. It must not log the challenge, password, or computed response at normal verbosity.

## HMAC Simple Authentication Mode

The canonical HMAC specification defines client authentication using a pre-shared key derived from the OPEN password.

| Symbol | Meaning |
| --- | --- |
| `Ra` | Server-generated random value |
| `Rb` | Client-generated random value |
| `Kab` | Password-derived pre-shared key |
| `A` | Client identity string defined by the specification |
| `B` | Server identity string defined by the specification |

For SHA-1, the random values, key, and digests are 160 bits. For SHA-256, they are 256 bits. `Kab` is the SHA digest of the OPEN password using the negotiated digest family.

The exchange has three cryptographic steps:

1. The server sends `Ra`.
2. The client generates `Rb` and returns `Rb` with the client proof over `Ra`, `Rb`, the two role identities, and `Kab`.
3. The server returns its confirmation over `Ra`, `Rb`, and `Kab`.

The client must verify the server confirmation and then send `*#*1##` to finish the published handshake. A server confirmation is not itself permission to skip this final client acknowledgement. If authentication fails, the connection is closed. The specification calls for a 60-second authentication suspension after three failed handshakes within 60 seconds.

## Wire encoding

The HMAC document uses decimal characters for binary values because ordinary OpenWebNet tags do not contain hexadecimal letters. Each binary byte is split into two hexadecimal nibbles, and each nibble is encoded as a two-digit decimal number in `00..15`.

| Byte | Nibbles | OpenWebNet representation |
| --- | --- | --- |
| `0x01` | `0`, `1` | `0001` |
| `0x0A` | `0`, `A` | `0010` |
| `0xFF` | `F`, `F` | `1515` |

A 20-byte SHA-1 value therefore occupies 80 decimal characters on the wire; a 32-byte SHA-256 value occupies 128.

This transport representation is not the input representation used by the hash calculation. Implementations should keep functions for binary values, hash-input serialization, and OpenWebNet wire encoding separate.

## Proof calculation and source discrepancy

The document calls this scheme HMAC, but describes its proof operation as SHA-1 or SHA-256 over concatenated fields. It does not describe the standard keyed HMAC inner/outer-pad construction. Substituting a library's generic `HMAC(key, message)` operation is therefore not justified by the protocol name.

For the negotiated hash `H`, the published layout is:

~~~text
Kab = H(OPEN_PASSWORD)
client_proof = H(hex(Ra) || hex(Rb) || A || B || hex(Kab))
server_proof = H(hex(Ra) || hex(Rb) || hex(Kab))
~~~

Here `hex` means lowercase hexadecimal text with two characters per byte; `||` means concatenation without separators. This is the hash-input representation, not the decimal-nibble transport representation. The password is the permitted alphanumeric character string.

The identity constants need special care. The source pairs the client label `copen` with `736F70653E` and the server label `sopen` with `636F70653E`. Those hex strings decode to `sope>` and `cope>`, respectively, and do not match the accompanying labels. This reference preserves that discrepancy rather than inventing corrected constants. Interoperable implementations need an independently verified gateway transcript or implementation source to resolve it.

The published exchange, with transport-encoded binary values, is:

| Direction | Frame |
| --- | --- |
| Server → client | `*#Ra##` |
| Client → server | `*#Rb*CLIENT_PROOF##` |
| Server → client | `*#SERVER_PROOF##` |
| Client → server, after verification | `*#*1##` |

See the authentication specification's printed pages 2–3 and 7–8 for the proof layout and serialization. The unresolved identity-constant discrepancy prevents treating this page as a complete, independently verified implementation recipe.

## Password constraints and security boundary

The HMAC specification permits an OPEN password of up to 30 alphanumeric characters and leaves minimum-length policy to applications.

Neither legacy nor HMAC authentication makes the later connection confidential. Deployments should not expose TCP port `20000` to untrusted networks and should use an external protected transport or trusted network boundary where confidentiality and integrity are required.

Do not place passwords, derived keys, nonces, proofs, or complete authentication frames in logs.

## Implementation checklist

- Wait for the initial server `ACK`.
- Select the required session.
- Branch on open-range acceptance, an HMAC declaration, or a legacy challenge.
- Reject unsupported declarations instead of silently changing the digest.
- Generate `Rb` with a cryptographically secure random generator.
- Compare proofs without timing-dependent early exit where practical.
- Begin functional parsing only after authentication succeeds.

## Evidence basis

The HMAC algorithm, declaration frames, value encoding, password format, and failure behavior come from [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf), version 1.1. The connection position and open-range exception are corroborated by [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf).
