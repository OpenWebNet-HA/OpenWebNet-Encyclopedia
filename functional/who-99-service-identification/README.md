# `WHO 99` - Session and Service Identification

`99` appears in two related but differently evidenced roles:

1. the public connection workflow uses `*99*X##` to select an OpenWebNet session;
2. MyHOME Suite `OPEN.db` names functional namespace `WHO 99` **Service Identification**.

These facts must be preserved without inventing a broader functional vocabulary.

## Published session selectors

| Frame | Session |
| --- | --- |
| `*99*9##` | Commands/actions |
| `*99*1##` | Events |
| `*99*0##` | Programmed scenario |

These frames occur during connection setup after the server greeting. They omit the normal `WHERE` field and are parsed by the session state machine, not by an ordinary three-field functional dispatcher.

See [Connection and Sessions](../../protocol/sessions.md) for the complete workflow.

## `OPEN.db` namespace evidence

`OPEN.db.EN_SYSTEM` contains a `WHO 99` row labelled Service Identification. It has no direct `AS_OPEN_SYSTEM` association to an `EN_OPEN` operation in this database revision.

The database therefore establishes the namespace label, but **does not** establish an additional service-identification `WHAT` table or prove that every `*99*X##` value is valid. The published selectors above are the concrete operations supported by the current source corpus.

## Distinctions

`WHO 99` session selection is not:

- gateway authentication (`WHO 98` declarations and challenge-response);
- a diagnostic Device interview;
- catalogue identity resolution;
- functional `WHO 8`'s parameterized service-identification association in `OPEN.db`.

Implementations should represent the raw numeric namespace while dispatching the published selector frames according to connection state.

## Evidence basis

The selector frames and order come from [`OWN_Intro_ENG.pdf`](../../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). The Service Identification label and absence of an associated concrete operation come from `OPEN.db`; see [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md).
