# MyHOMEServer1 3.87.13 BNLD Trigger Serialization

The numeric `BNLD` trigger's selected serializer emits a signed threshold and passes the same JSON result back to its raw constructor before compilation. This gives a source-level value contract for the [numeric trigger](myhomeserver1-3.87.13-event-trigger.md#bnld-numeric-trigger) in [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), distinct from the `BNLD` condition serializer and a universal JSON round trip.

## Actual trigger method and selected value

The final raw `BnldTrigger` virtual table identifies its own serializer, which receives raw object and JSON destination separately and calls its trigger-base helper. The condition's differently selected serializer is not substituted for it.

Exact raw status `-1` selects an unconditional signed `level` assignment request. That arm has no local comparison suppressing zero, `-1` or another threshold word. The base begins with a fresh null-value construction and normally adds only ID, type, enabled and optional operator; under ordinary member/provider behavior it contributes no status member to preempt numeric reparse.

These are emission requests, not proof of accepted arbitrary numeric inputs or physical meanings. [Trigger-serializer evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-trigger-serialization/README.md) preserves the actual virtual identity, base call and selected fields.

## Same-result reparse and its limit

The initializer supplies the same JSON destination first to the raw virtual method and then to the trigger constructor. On the absent-status route, that constructor initializes status and level to `-1`, reads `level` with `asInt`, stores the word and retains status `-1`. The selected positive-value conditional store writes `-1` again, not status `0`.

With matching signed-integer construction/readback and valid fresh-member/copy/provider behavior, this path can retain the constructor-reachable threshold/status pair before compiled copying. It does not preserve every original member-presence distinction or establish malformed/other-type input, exceptional values, effective binding or configured admission.

The trigger caller's ID, configured-status, record-`on` and integer-value guards remain those of the [numeric-trigger reference](myhomeserver1-3.87.13-event-trigger.md#bnld-numeric-trigger). Crossing/deduplication, threshold domain, units and physical behavior remain unresolved.

## Candidate signed-integer provider source contract

The exact packaged `libjsoncpp.so.1.9.5` candidate has its own signed-integer path. `Value(int)` initializes type `1` and stores the `32`-bit argument with a sign-extended high word. `type()` reads its stored type byte. The selected type-`1` `asInt` route calls `isInt`, then loads the low word on its nonzero normal branch.

The examined `isInt` arithmetic adjusts the stored `64`-bit pair by `0x80000000` and tests whether the adjusted high word is zero. A constructor-produced sign-extended signed `32`-bit representation satisfies that test, so the selected getter returns its original argument word. This is source algebra, without an executed integer fixture.

[Signed-provider evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-integer-provider/README.md) retains the original provider identity, dispatch and arithmetic. Binding, valid unchanged objects, ABI/delegate returns and JSON member/map/move/assignment operations remain premises. The separately observed [double-helper cases](myhomeserver1-3.87.13-serialization.md#isolated-original-scalar-constructor-and-readback) do not prove integer or full serializer execution. Other type/error branches, complete lifetime and physical semantics remain unresolved.
