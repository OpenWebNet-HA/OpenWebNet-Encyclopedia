# ZigBee Network Management

The Legrand ZigBee OpenWebNet specification version 4.0 defines an interface-specific `WHO 13` management surface for the ZigBee OpenWebNet interface. It manages the interface's ZigBee-network role, exposes product-database operations, and reports selected interface and radio Device properties.

This page documents only behavior represented through OpenWebNet. ZigBee radio commissioning, routing, security, and other radio-internal mechanisms are outside the encyclopedia boundary except where an OpenWebNet field exposes their result.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. The document carries Confidential footers, so its publication provenance remains qualified as recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The semantics below are **specification evidence** for this interface revision; they are not a claim of support by every ZigBee gateway, product, or firmware revision.

## `WHAT` reference

The ZigBee specification defines the following `WHO 13` command values:

| `WHAT` | Source action | Principal applicability |
| ---: | --- | --- |
| `12` | Boot mode | interface |
| `22` | Reset | interface |
| `30` | Create ZigBee network | interface |
| `31` | Close ZigBee network | interface and product-originated indication |
| `32` | Open ZigBee network | interface and product-originated indication |
| `33` | Join ZigBee network | interface and product-originated indication |
| `34` | Leave ZigBee network | interface or addressed product, plus product-originated indication |
| `60` | Keep connect / readiness | interface |
| `61` | Identify | addressed product |
| `65` | Scan | interface |
| `66` | Supervisor | interface command and product-originated indication |
| `67` | Supervisor remove | interface command and product-originated indication |

Gateway-directed commands use an empty `WHERE`, for example `*13*30*##` for Create and `*13*65*##` for Scan. Product-directed or product-originated frames use the [ZigBee `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing), which is distinct from SCS `A`/`PL` addressing.

### Boot mode and reset

`WHAT 12` requests boot mode. The specification describes an OpenWebNet `ACK` or `NACK` followed, on success, by an ASCII boot-mode acknowledgement and states that subsequent communication no longer uses ordinary OpenWebNet frames. The OpenWebNet encyclopedia therefore stops at that handoff; the subsequent bootloader protocol is not established as OpenWebNet.

`WHAT 22` resets the interface. The source says the interface returns `ACK` before reset when the request is accepted.

## Network lifecycle

`WHAT 30` creates a ZigBee network. The source use case states that a successful Create leaves the network created and open.

`WHAT 31` closes an existing network, while `WHAT 32` opens it. The specification also defines addressed, server-originated `WHAT 31` and `WHAT 32` frames as product indications that a ZigBee product closed or opened the network.

`WHAT 33` requests that the interface join an existing network. The detailed `WHAT` definition also assigns addressed, server-originated `WHAT 33` frames to product join indications.

`WHAT 34` requests that the interface leave its network. The detailed definition additionally allows `*13*34*WHERE#9##` to request that an addressed product leave, and uses the same addressed form as a product-originated leave indication.

### Source inconsistencies

The source contains two material inconsistencies that must not be silently normalized:

- The `WHO 13` Join use case shows `*13*33*##` followed by `ACK` and then an addressed `WHAT 32` frame, while the detailed `WHAT` table assigns addressed product join indications to `WHAT 33`. The current corpus does not establish whether the use-case frame is a documentation error or represents an additional event.
- The detailed Leave table describes both the `ACK` and `NACK` cases with wording equivalent to "has not left." The preceding Leave use case states that `ACK` accompanies a successful leave. The reference therefore treats the duplicated negative wording as a source defect rather than evidence that successful Leave has inverted acknowledgement semantics.

## Readiness and identification

`WHAT 60` is the interface readiness operation. `*13*60*##` returns `ACK` when the interface is ready and `NACK` when it is not.

`WHAT 61` identifies an addressed product. The source specifies a ZigBee `WHERE` with Unit `00` and says the product's green LED blinks slowly for five minutes. `ACK` indicates that the identify command was sent; `NACK` indicates that it was not. A BUSY result follows the interface-specific BUSY/NACK handling documented under [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior).

## Supervisor mode

`WHAT 66` sends the supervisor command. The specification describes this as a broadcast to active products that enables reporting of subsequent state changes to the OpenWebNet interface. A newly joined product requires the supervisor command to be sent again before that product participates in this mode.

`WHAT 67` is the complementary Supervisor Remove operation. The source calls it the default mode and says it prevents receipt of product state changes enabled through Supervisor.

The source recommends only one OpenWebNet interface with supervisor mode enabled in a ZigBee network for normal operation because multiple supervisors reduce radio-network performance. This is an interface-specific ZigBee constraint, not a generic OpenWebNet session rule.

## Scan and product database

The interface maintains an internal product database. Section 6 says the database can contain up to 175 products and is managed automatically by the interface. The database is a stored inventory, not a statement that every stored product is currently reachable.

### Database population and persistence

When the interface is present as products join a network, the source says each new joining product fills the product database. The section 6.1.1 use case shows the stored product count increasing as both routers and end Devices join.

When the interface itself joins an existing ZigBee network, section 6.1.2 says it initially does not know the existing products. The OpenWebNet user sends Scan to learn active products. Products that are not active during that process, particularly sleeping battery end Devices, require later activity described by the source before they can be added. Section 6.1.3 likewise states that a product which joins while the interface is powered off is not known to the interface at that time; its use case shows later Scan or product activity as ways the stored population can be updated.

The source explicitly says that the number of products in the database does not change across an interface power cycle. Section 6.1.4 also states that a product which leaves the ZigBee network while the interface is powered off remains in the database. The source defines no OpenWebNet command in the inspected discovery/inventory material for deleting that stale entry, no aging interval, and no automatic stale-entry pruning rule.

These rules establish that database membership and current reachability are distinct states.

### Scan

`WHAT 65` initiates a scan with `*13*65*##`. The specification says the interface broadcasts over the ZigBee network and active routers plus awake end Devices can answer. The command returns `ACK` when sent. The documented flow then reports `DIMENSION 67` approximately 13 seconds later.

The detailed Scan definition explicitly warns that the resulting count is the number of products stored in the interface product database, not simply the number of active routers seen during that scan. A Scan can therefore contribute newly active products to the stored database without turning `DIMENSION 67` into a count of only the current responders.

## `DIMENSION` reference

The ZigBee specification defines this `WHO 13` `DIMENSION` set:

| `DIMENSION` | Source property | Applicability |
| ---: | --- | --- |
| `12` | MAC / IEEE address | interface |
| `16` | Firmware version | interface or addressed product |
| `17` | Hardware version | interface or addressed product |
| `26` | Implemented `WHO` values | interface or addressed product |
| `66` | Product information | product-database entry or addressed product |
| `67` | Number of products | interface product database |
| `71` | ZigBee channel | interface |
| `72` | Battery information | applicable battery product |
| `73` | Device MAC address by index | product-database entry |

This table is variant-specific. It must not be supplemented with SCS/TCP `WHO 13` dimensions merely because the namespace number is shared.

### `DIMENSION 12` - Interface IEEE address

The request is `*#13**12##`. The source returns the interface IEEE address as eight decimal values followed by `ACK`.

This property is protocol knowledge, but real installation identifiers are not. Documentation and tests should use symbolic or synthetic values rather than retaining a real interface address.

### `DIMENSION 16` and `17` - Firmware and hardware versions

`DIMENSION 16` reports three firmware components: version, release, and build. `DIMENSION 17` reports major, minor, and release hardware-version components.

Both can address the interface with an empty `WHERE` or a ZigBee product with the product-level Unit form described by the source. Availability for one target does not establish support by every product.

### `DIMENSION 26` - Implemented `WHO` values

`DIMENSION 26` reports the functional `WHO` values implemented by the selected target. The returned list is capability evidence for that target; it does not establish that every operation of every reported namespace is supported.

### `DIMENSION 66` - Product information

Product information can be requested either by a zero-based product-database index or by an addressed product:

- by index: `*#13**66#INDEX##`;
- by product: `*#13*WHERE#9*66##`, using product-level Unit `00`.

Responses use `DIMENSION 66` and identify product Units/endpoints with an index and a numeric Device-ID/type value. The specification provides a value registry for scenario, Lighting, Automation, interface, and video product types.

The source says this operation may take up to 30 seconds when a product is not reachable, for example when a battery-powered Device is sleeping. It defines a response value of `0` for an unreachable product and terminates the reported Unit sequence with `ACK`.

The published parameter separator is `#INDEX`. The exploratory ZigBee branch recorded an alternate `*INDEX` form as an implementation compatibility claim, but that form is not established by this specification and is not part of the canonical grammar.

### `DIMENSION 67` - Product count

`*#13**67##` requests the number of products in the interface product database. The response is `*#13**67*VALUE##` followed by `ACK`.

The source uses "products discovered" in parts of the detailed description while explicitly stating that the value comes from the interface product database. The database interpretation is therefore retained as the stronger local qualification.

### `DIMENSION 71` - ZigBee channel

`*#13**71##` requests the ZigBee network channel. The published range is `11..26`. This page records the OpenWebNet-visible value only; ZigBee RF channel-selection mechanics are outside scope.

### `DIMENSION 72` - Battery information

Battery information is a server-originated frame of the form `*#13*WHERE#9*72*VALUE##`. The source defines:

| `VALUE` | Source label |
| ---: | --- |
| `0` | `CRITICAL` |
| `1` | `POWER_VALUE_33` |
| `2` | `POWER_VALUE_66` |
| `3` | `POWER_VALUE_100` |

The frame can carry a Unit-specific `WHERE`. That addressing does not by itself prove that each Unit has an independent battery.

### `DIMENSION 73` - Product identifier by index

`*#13**73#INDEX##` requests the ZigBee product identifier associated with a zero-based product-database index. The response uses `*#13*WHERE#9*73#INDEX*VALUE##` with Unit `00` and classifies the stored product as:

| `VALUE` | Source meaning |
| ---: | --- |
| `0` | unknown |
| `1` | mains-powered Device |
| `2` | battery-powered Device |

The detailed use case says this operation asks the interface database for the product identifier and does not send a ZigBee frame to reach the product. This makes `DIMENSION 73` a local stored-inventory lookup rather than a reachability test.

The same use-case paragraph also repeats a statement that the "product information command" could take 30 seconds when a product is unreachable. That warning conflicts with the immediately following statement that this indexed lookup does not contact the product. The 30-second reachability warning is therefore retained for `DIMENSION 66`, where it is independently defined, and is not promoted as established `DIMENSION 73` timing.

The source labels `DIMENSION 73` "Device MAC address by index," but the returned `WHERE` is the ZigBee OpenWebNet product identifier form derived from the product address model, not the eight-value interface IEEE address returned by `DIMENSION 12`.

## Discovery relationship and source conflicts

The specification exposes several distinct discovery mechanisms:

1. [`WHO 1000 DIMENSION 81` neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) traverses neighbor information reported by the interface and newly discovered routers.
2. `WHO 13 WHAT 65` scans the ZigBee network and later reports the product-database count through `DIMENSION 67`.
3. `DIMENSION 73` resolves a product-database index locally to its stored ZigBee product identifier and power type.
4. `DIMENSION 66` queries Units/endpoints and numeric Device-ID/type information for an indexed or addressed product and can expose that a stored product is unreachable.

The source does not define one contradiction-free canonical sequence combining all four. Section 5.4 shows Scan followed by `DIMENSION 67` and then indexed `DIMENSION 73` requests, but its explanatory prose under those `DIMENSION 73` exchanges says that the product supplies endpoints and Device IDs. The detailed definitions later assign endpoint/Device-ID information to `DIMENSION 66` and define `DIMENSION 73` as index-to-product-identifier/power-type lookup.

Section 5.2 also shows a product-join discovery frame with command/status content but a leading `*#13` form. The detailed `WHO 13` Product Joins use case and `WHAT 33` definition use the command/status form `*13*33*WHERE#9##`. The leading `#` in section 5.2 is therefore preserved as a source inconsistency rather than promoted as an alternate join grammar.

The `DIMENSION 73` use-case paragraph contains a separate copied-looking reachability warning while also stating that the operation is a local database lookup which sends no ZigBee frame. The encyclopedia preserves that contradiction and does not assign the `DIMENSION 66` 30-second reachability behavior to `DIMENSION 73`.

The encyclopedia therefore preserves the primitives and these source inconsistencies rather than replacing them with an inferred canonical workflow.

## Evidence limits

No inspected source establishes that the MyHOME Suite diagnostic Device-interview model - including diagnostic `WHO 1001` and `DIMENSION 30`, `32`, or `35` - applies to this ZigBee interface.

The specification also does not establish the exploratory branch's firmware-version threshold for binding, alternate `DIMENSION 66` separator syntax, or old-firmware ACK workarounds. Those remain implementation claims requiring separate provenance before they can become canonical compatibility notes.

See [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for transport, addressing, acknowledgement behavior, and cross-namespace applicability.
