# `DIMENSION`

A `DIMENSION` identifies a property, query, or structured operation within an OpenWebNet `WHO`. It can be requested, reported asynchronously, returned in a response, or-where explicitly supported-written.

The complete identity is not always just `(WHO, DIMENSION)`. A `DIMENSION` selector can contain `#`-separated parameters:

~~~text
DIMENSION#PARAMETER#PARAMETER
~~~

These parameters select a particular instance, sub-property, internal slot, priority context, or operation variant. The `*`-separated fields following the selector are the ordered payload values:

~~~text
DIMENSION#PARAMETER#PARAMETER*VALUE*VALUE
~~~

Implementations must preserve this boundary. Selector parameters and payload values are not interchangeable.

## General frame forms

| Operation | Flat selector | Parameterized selector |
| --- | --- | --- |
| Request | `*#WHO*WHERE*DIMENSION##` | `*#WHO*WHERE*DIMENSION#P1#P2##` |
| Response/report | `*#WHO*WHERE*DIMENSION*V1*V2##` | `*#WHO*WHERE*DIMENSION#P1#P2*V1*V2##` |
| Write | `*#WHO*WHERE*#DIMENSION*V1*V2##` | `*#WHO*WHERE*#DIMENSION#P1#P2*V1*V2##` |

`P1`, `P2`, `V1`, and `V2` are notation, not literal wire values. A particular `DIMENSION` can define zero, one, or several selector parameters and zero, one, or several payload values.

The actual arity and meaning are defined by the selected `WHO` and `DIMENSION`. The table describes the reusable structural pattern, not permission to append arbitrary parameters.

## Three different uses of `#`

The same character participates in several layers:

| Position | Example | Meaning |
| --- | --- | --- |
| Before `WHO` | `*#WHO...` | Selects the request/`DIMENSION` frame family |
| Before a writable selector | `*#WHO*WHERE*#DIMENSION...` | Marks a `DIMENSION` write |
| Inside the selector | `DIMENSION#P1#P2` | Separates parameters belonging to that selector |

The leading write marker and selector parameters can occur together:

~~~text
#DIMENSION#P1#P2
~~~

This is one major `*`-delimited field. It is not a series of independent frame fields.

## Selector parameters versus payload values

Consider the abstract response:

~~~text
*#WHO*WHERE*32#7*SYSTEM*ADDRESS##
~~~

Here:

- `32` is the `DIMENSION` identifier;
- `7` is a selector parameter, for example an internal slot;
- `SYSTEM` and `ADDRESS` are payload values.

The equivalent structured representation is:

~~~text
selector = {
  dimension: "32",
  parameters: ["7"]
}
values = ["SYSTEM", "ADDRESS"]
~~~

It would be incorrect to parse the field as `DIMENSION=32`, then treat `7`, `SYSTEM`, and `ADDRESS` as three equivalent values. It would also be incorrect to describe `SYSTEM` and `ADDRESS` as `#`-separated simply because the selector is parameterized: payload values remain separated by `*`.

## Concrete patterns

### Flat selector with multiple values

Lighting temporization uses a flat `DIMENSION 2` selector and three payload values:

~~~text
*#1*WHERE*#2*HOURS*MINUTES*SECONDS##
~~~

`HOURS`, `MINUTES`, and `SECONDS` are values; none is part of the selector.

### Parameterized write selector

Advanced Automation absolute positioning uses a parameter attached to the writable selector:

~~~text
*#2*WHERE*#11#SHUTTER_PRIORITY*SHUTTER_LEVEL##
~~~

`SHUTTER_PRIORITY` belongs to the `DIMENSION 11` selector. `SHUTTER_LEVEL` is the payload value.

### Parameterized diagnostic selector

Diagnostic operations use selectors such as `32#SLOT`, where `SLOT` identifies the Device-local internal slot. The following `SYS` and `ADDR` fields are ordinary `*`-separated payload values:

~~~text
*#DIAGNOSTIC_WHO*DEVICE*32#SLOT*SYS*ADDR##
~~~

This distinction is essential when correlating a response with a Device Module: the internal slot is addressing the property instance, while `SYS` and `ADDR` describe its configured functional address.

## Requests, responses, and reports

A request supplies the selector but normally no payload:

~~~text
*#WHO*WHERE*DIMENSION#P1##
~~~

A response ordinarily repeats enough context to identify the reported property and appends its values:

~~~text
*#WHO*WHERE*DIMENSION#P1*V1*V2##
~~~

The same response-shaped frame can appear asynchronously on an events session. Direction and session state therefore distinguish a solicited response from an unsolicited report; syntax alone may not.

A collective request can produce multiple response frames followed by `ACK`. Do not assume one request yields one value frame. If the sequence terminates in `NACK`, the common protocol permits the preceding provisional results to be treated as invalid.

## Writes

A write prefixes the complete selector with `#`:

~~~text
*#WHO*WHERE*#DIMENSION#P1*V1##
~~~

The write marker does not remove the selector's own parameters. A parser can represent this cleanly as:

~~~text
operation = "write"
dimension = "DIMENSION"
selector_parameters = ["P1"]
values = ["V1"]
~~~

The existence of a readable or reportable `DIMENSION` does not imply write support. Read, report, and write capability must be established separately for the exact selector and target Object.

## Arity and typing

Neither parameter count nor value count is globally fixed. The available public specification establishes no protocol-wide maximum count for selector parameters or payload values, and it does not specify a universal maximum frame length. This absence of a common limit does not make the arity unrestricted for a particular operation: the exact `(WHO, DIMENSION, operation)` definition determines which counts are valid.

System-specific definitions can impose:

- exact or variable selector-parameter counts;
- exact or variable payload counts;
- decimal ranges or enumerations;
- fixed-width strings and significant leading zeroes;
- encoded temperatures, times, masks, identifiers, or text;
- relationships between selector parameters and the number or meaning of values.

Keep raw fields as strings until the applicable `(WHO, DIMENSION)` grammar is known. Premature integer conversion can destroy leading zeroes, empty values, fixed-width identifiers, and encoded structure.

## Semantic identity

For a flat property, `(WHO, DIMENSION)` can be sufficient to select the value grammar. For a parameterized property, use at least:

~~~text
(WHO, DIMENSION, SELECTOR_PARAMETERS)
~~~

Interpretation can additionally depend on `WHERE`, direction, session, Device firmware, Module/Object capability, and whether the frame is a request, response, report, or write.

Equal numeric `DIMENSION` identifiers in different `WHO` namespaces do not imply equal meaning. Equal selectors on different Device Objects do not prove equal support or value ranges.

## Parser model

A practical parser should:

1. identify the `DIMENSION` frame family from `*#WHO`;
2. split only the major `*`-delimited fields, preserving empty fields;
3. detect and remove the leading write marker from the selector field;
4. split the remaining selector field on `#` into the identifier and selector parameters;
5. retain the following major fields as ordered payload values;
6. resolve the system-specific grammar before converting types;
7. validate operation direction and target capability separately.

Do not globally split the entire frame on both `*` and `#`; doing so erases the difference between selector parameters, payload values, and parameterized `WHERE` or `WHAT` fields.

## Evidence basis

Flat request, response, and write forms come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). Parameterized selectors are established by the dedicated functional specifications and the MyHOME Suite diagnostic/programming templates, including advanced Automation `DIMENSION 11` and diagnostic slot-qualified selectors.

See [Frame Syntax](frame-syntax.md), [Stream Parsing](stream-parsing.md), [Addressing](addressing.md), the relevant functional `WHO` page, and the [Diagnostic `DIMENSION` Reference](../diagnostics/dimension-reference.md).
