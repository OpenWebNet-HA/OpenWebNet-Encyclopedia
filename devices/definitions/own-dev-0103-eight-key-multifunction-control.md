# Eight-key multifunction control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0103` | Project identity |
| Technical description | Eight backlit keys with learned, scenario, paired lighting/shutter and `CEN` control modes | Published technical sheets; canonical catalogue |
| Commercial identities | `H4652`, `LN4652`, `067592` | Three catalogue records and both technical-sheet headers |
| Catalogue item | `1678` | Canonical MyHOME Suite `3.5.38` catalogue |
| Main catalogue system | Automation | Main item/system association |
| Item model / `modobj` | `49` | Main item/system association |
| Firmware definition | `1.0.1` | Canonical catalogue; not an observed installed release |
| Declared Modules | `9` | Canonical firmware metadata |
| Categories | Commands, Scenarios, User interfaces, Multifunction devices | Source-derived roles |

The catalogue title “8 scenarios control” covers a broader multifunction command surface. Eight keys correspond to command slots `1..8`; slot `9` is User interface settings. Physical mounting occupies two wiring-device modules, independently of this protocol topology.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4652` | Established commercial variant | Item `1678`; `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| BTicino - LivingLight | `LN4652` | Established commercial variant | Item `1678`; `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Legrand - Céliane | `067592` | Established commercial variant | Item `1678`; `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |

The catalogue LN record uses the grouping `L/N/NT`; the publisher markets `LN4652` as LivingLight. Label sheets `3541`, `3542`, `067595` and `067596` are accessories, not additional Device identities.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00778_a_EN.pdf` | English technical sheet | `MM00778-a-EN`, `02/12/2013` | All three identities; specifications/interfaces printed p. 1 / PDF p. 1; learning and F420 scenario procedures printed p. 2 / PDF p. 2; deletion, paired/`CEN` modes, LEDs and Ethernet diagram printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/19/85/1985866f3b45dfdb083ce1150d8fcce44c6e6384cb05898732eb1b1692868608.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00778_a_EN.pdf) |
| `MM00778-a-FR.pdf` | French technical sheet | `MM00778-a-FR`, `02/12/2013` | All three identities; specifications/interfaces printed p. 1 / PDF p. 1; learning and F420 scenario procedures printed p. 2 / PDF p. 2; deletion, paired/`CEN` modes, LEDs and Ethernet diagram printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/fb/1a/fb1a47e3c4a6f25602b1c8271b72614f57df0e7bc48d9cdf35ccb4e9b5b32555.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00778-a-FR.pdf) |
| `LE06019AA.pdf` | Illustrated label installation sheet | `LE06019AA-02PC-13W21` | All three identities; label removal, replacement, printing and cutting; no printed pagination / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/8b/0e8b53454dad7420f6cfb97c7fcd5d4792cec49629ba2c75207aa577ac85343c.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/LE06019AA.pdf) |
| `H4652-publisher-product-sheet.pdf` | Publisher product-sheet export | `DATASHEET`, `03.10.2026` (export date) | `H4652` only; identity/product characteristics printed p. 1 / PDF p. 1; technical attributes printed pp. 2-3 / PDF pp. 2-3; download inventory printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/b5/57/b557bf645d57e9ea72d167ec4b23c4e5ea7c2ed814e6a056f051f32c1e99c1cb.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-H4652&include_technical=1) |
| `LN4652-publisher-product-sheet.pdf` | Publisher product-sheet export | `DATASHEET`, `03.10.2026` (export date) | `LN4652` only; identity/product characteristics printed p. 1 / PDF p. 1; technical attributes printed pp. 2-3 / PDF pp. 2-3; download inventory printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/a6/e9/a6e9eb147e099cf713ebddb91471594664a3782386ef335efa8767e3692687b3.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-LN4652&include_technical=1) |
| `MM00778_a_IT.pdf` | Italian technical sheet | `MM00778-a-IT`, `02/12/2013` | All three identities; specifications printed p. 1 / PDF p. 1; learning/F420 printed p. 2 / PDF p. 2; paired/`CEN`, LED and software configuration printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/05/ad05d7c531374863da1cd8a217be237ee00df442859528ee7fe657d27b5c7d3a.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00778_a_IT.pdf) |
| `cm220600_0982.pdf` | French commercial catalogue extract | `CM220600`; no full publication date printed | H4652/LN4652 command block, label accessories, separate thermostat and infrastructure products; printed p. 982 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/cc/9d/cc9d0f49992d060e11b7692ab13867434c287ec02d881de3ed1049abbeafa340.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-fr/pc/cm220600_0982.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1678`; complete commercial, firmware, Module/Object and configuration records | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | Two flush-mounted wiring-device modules | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| SCS BUS supply | `18..27 Vdc` | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Rear interfaces | SCS BUS terminals and physical configurator socket | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Current, LEDs off | `5 mA` | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Current, LEDs at full brightness | `20 mA` | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Operating temperature | `0..40 °C` | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Front controls | Eight backlit keys; replaceable icon/label area | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Rear programming key | Learning and scenario programming/deletion | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Physical configurator positions | `A`, `PL`, `M`, `LED` | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Symbol sheet accessories | `3541` / `067595`: black A5 sheets; `3542` / `067596`: white A5 sheets | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1; `LE06019AA`, PDF p. 1 |
| Published standards | `EN 60669-2-1`, `EN 50491-5-1`, `EN 50428` | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Current online rated current | H4652 `20 mA`; LN4652 `21 mA`, each at `27 Vdc` | SKU-scoped product-sheet exports `03.10.2026`, printed pp. 1-3 / PDF pp. 1-3; different from LED-specific sheet figures |
| H4652 / LN4652 online dimensions | `45 x 45 x 24 mm`; box depth minimum `55 mm`; `IP20` | Both product-sheet exports `03.10.2026`, printed pp. 1-3 / PDF pp. 1-3 |
| H4652 / LN4652 online storage / terminals | `-10..70 °C`; terminal capacity `0.34..2.5 mm²`, flexible or rigid wire | Both product-sheet exports `03.10.2026`, printed pp. 1-3 / PDF pp. 1-3 |
| H4652 / LN4652 online construction | Plastic / thermoplastic, glossy untreated finish, transparent; catalogue RAL-like values H4652 `9011`, LN4652 `9006` | SKU-scoped product-sheet attributes, printed p. 2 / PDF p. 2; no Céliane extension |
| H4652 / LN4652 online interface attributes | Eight actuation points/buttons; LED and label area; no display, room-temperature controller, IR sensor, RF bus or bidirectional RF | Product-sheet inventory, printed pp. 2-3 / PDF pp. 2-3; ecosystem voice/internet fields reconciled below |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1678` | Canonical catalogue |
| Technical item description | 8 scenarios control | Canonical catalogue |
| Item family | Control (`1`) | Catalogue family association |
| Main system | Automation; system key `1` | `AS_ITEM_SYSTEM.main` association; not a functional WHO number |
| Item model / `modobj` | `49` | Main item/system mapping |
| Brand / line keys | BTicino brand key `1`, Axolute line key `2`, LivingLight line key `4`; Legrand brand key `2`, Céliane line key `13` | Commercial database keys; different from software parameter model namespaces |
| Commercial records | `3`; record IDs `1733`, `2155`, `2156` | Three shared-item catalogue variants |
| Gateway metadata | None of the three records is marked as a gateway | Commercial metadata; an MH201 software route is an external system connection |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `122` | `1` | `0` | `1` | `9` | Catalogue default | Official |

Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.


Hardware revision, microcontroller and installed firmware are unknown. The firmware table records source applicability, not an observed Physical Device.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `122` | `1` | `410` Light control | Fixed/designated metadata | `2307` | `410` | `985` |
| `122` | `1` | `411` Automation control | Candidate alternative | `1400` | `411` | `739` |
| `122` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `1408` | `412` | `740` |
| `122` | `1` | `413` Scenario module control | Candidate alternative | `1416` | `413` | `741` |
| `122` | `1` | `414` Scheduled scenario | Candidate alternative | `1424` | `414` | `742` |
| `122` | `1` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1432` | `415` | `743` |
| `122` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `1440` | `416` | `744` |
| `122` | `1` | `417` `AUX` control | Candidate alternative | `1448` | `417` | `745` |
| `122` | `1` | `418` Open lock control | Candidate alternative | `1456` | `418` | `746` |
| `122` | `1` | `419` Sound diffusion control | Candidate alternative | `1464` | `419` | `747` |
| `122` | `1` | `421` Cyclic autoswitch control | Candidate alternative | `1472` | `421` | `748` |
| `122` | `1` | `426` Staircase light control | Candidate alternative | `1480` | `426` | `749` |
| `122` | `1` | `427` Floor call control | Candidate alternative | `1488` | `427` | `750` |
| `122` | `1` | `462` Open lock command on session | Candidate alternative | `1496` | `489` | `751` |
| `122` | `2` | `410` Light control | Fixed/designated metadata | `2308` | `410` | `985` |
| `122` | `2` | `411` Automation control | Candidate alternative | `1401` | `411` | `739` |
| `122` | `2` | `412` Lock/unlock actuator control | Candidate alternative | `1409` | `412` | `740` |
| `122` | `2` | `413` Scenario module control | Candidate alternative | `1417` | `413` | `741` |
| `122` | `2` | `414` Scheduled scenario | Candidate alternative | `1425` | `414` | `742` |
| `122` | `2` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1433` | `415` | `743` |
| `122` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `1441` | `416` | `744` |
| `122` | `2` | `417` `AUX` control | Candidate alternative | `1449` | `417` | `745` |
| `122` | `2` | `418` Open lock control | Candidate alternative | `1457` | `418` | `746` |
| `122` | `2` | `419` Sound diffusion control | Candidate alternative | `1465` | `419` | `747` |
| `122` | `2` | `421` Cyclic autoswitch control | Candidate alternative | `1473` | `421` | `748` |
| `122` | `2` | `426` Staircase light control | Candidate alternative | `1481` | `426` | `749` |
| `122` | `2` | `427` Floor call control | Candidate alternative | `1489` | `427` | `750` |
| `122` | `2` | `462` Open lock command on session | Candidate alternative | `1497` | `489` | `751` |
| `122` | `3` | `410` Light control | Fixed/designated metadata | `2309` | `410` | `985` |
| `122` | `3` | `411` Automation control | Candidate alternative | `1402` | `411` | `739` |
| `122` | `3` | `412` Lock/unlock actuator control | Candidate alternative | `1410` | `412` | `740` |
| `122` | `3` | `413` Scenario module control | Candidate alternative | `1418` | `413` | `741` |
| `122` | `3` | `414` Scheduled scenario | Candidate alternative | `1426` | `414` | `742` |
| `122` | `3` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1434` | `415` | `743` |
| `122` | `3` | `416` Scheduled scenario PLUS | Candidate alternative | `1442` | `416` | `744` |
| `122` | `3` | `417` `AUX` control | Candidate alternative | `1450` | `417` | `745` |
| `122` | `3` | `418` Open lock control | Candidate alternative | `1458` | `418` | `746` |
| `122` | `3` | `419` Sound diffusion control | Candidate alternative | `1466` | `419` | `747` |
| `122` | `3` | `421` Cyclic autoswitch control | Candidate alternative | `1474` | `421` | `748` |
| `122` | `3` | `426` Staircase light control | Candidate alternative | `1482` | `426` | `749` |
| `122` | `3` | `427` Floor call control | Candidate alternative | `1490` | `427` | `750` |
| `122` | `3` | `462` Open lock command on session | Candidate alternative | `1498` | `489` | `751` |
| `122` | `4` | `410` Light control | Fixed/designated metadata | `2310` | `410` | `985` |
| `122` | `4` | `411` Automation control | Candidate alternative | `1403` | `411` | `739` |
| `122` | `4` | `412` Lock/unlock actuator control | Candidate alternative | `1411` | `412` | `740` |
| `122` | `4` | `413` Scenario module control | Candidate alternative | `1419` | `413` | `741` |
| `122` | `4` | `414` Scheduled scenario | Candidate alternative | `1427` | `414` | `742` |
| `122` | `4` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1435` | `415` | `743` |
| `122` | `4` | `416` Scheduled scenario PLUS | Candidate alternative | `1443` | `416` | `744` |
| `122` | `4` | `417` `AUX` control | Candidate alternative | `1451` | `417` | `745` |
| `122` | `4` | `418` Open lock control | Candidate alternative | `1459` | `418` | `746` |
| `122` | `4` | `419` Sound diffusion control | Candidate alternative | `1467` | `419` | `747` |
| `122` | `4` | `421` Cyclic autoswitch control | Candidate alternative | `1475` | `421` | `748` |
| `122` | `4` | `426` Staircase light control | Candidate alternative | `1483` | `426` | `749` |
| `122` | `4` | `427` Floor call control | Candidate alternative | `1491` | `427` | `750` |
| `122` | `4` | `462` Open lock command on session | Candidate alternative | `1499` | `489` | `751` |
| `122` | `5` | `410` Light control | Fixed/designated metadata | `2311` | `410` | `985` |
| `122` | `5` | `411` Automation control | Candidate alternative | `1404` | `411` | `739` |
| `122` | `5` | `412` Lock/unlock actuator control | Candidate alternative | `1412` | `412` | `740` |
| `122` | `5` | `413` Scenario module control | Candidate alternative | `1420` | `413` | `741` |
| `122` | `5` | `414` Scheduled scenario | Candidate alternative | `1428` | `414` | `742` |
| `122` | `5` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1436` | `415` | `743` |
| `122` | `5` | `416` Scheduled scenario PLUS | Candidate alternative | `1444` | `416` | `744` |
| `122` | `5` | `417` `AUX` control | Candidate alternative | `1452` | `417` | `745` |
| `122` | `5` | `418` Open lock control | Candidate alternative | `1460` | `418` | `746` |
| `122` | `5` | `419` Sound diffusion control | Candidate alternative | `1468` | `419` | `747` |
| `122` | `5` | `421` Cyclic autoswitch control | Candidate alternative | `1476` | `421` | `748` |
| `122` | `5` | `426` Staircase light control | Candidate alternative | `1484` | `426` | `749` |
| `122` | `5` | `427` Floor call control | Candidate alternative | `1492` | `427` | `750` |
| `122` | `5` | `462` Open lock command on session | Candidate alternative | `1500` | `489` | `751` |
| `122` | `6` | `410` Light control | Fixed/designated metadata | `2312` | `410` | `985` |
| `122` | `6` | `411` Automation control | Candidate alternative | `1405` | `411` | `739` |
| `122` | `6` | `412` Lock/unlock actuator control | Candidate alternative | `1413` | `412` | `740` |
| `122` | `6` | `413` Scenario module control | Candidate alternative | `1421` | `413` | `741` |
| `122` | `6` | `414` Scheduled scenario | Candidate alternative | `1429` | `414` | `742` |
| `122` | `6` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1437` | `415` | `743` |
| `122` | `6` | `416` Scheduled scenario PLUS | Candidate alternative | `1445` | `416` | `744` |
| `122` | `6` | `417` `AUX` control | Candidate alternative | `1453` | `417` | `745` |
| `122` | `6` | `418` Open lock control | Candidate alternative | `1461` | `418` | `746` |
| `122` | `6` | `419` Sound diffusion control | Candidate alternative | `1469` | `419` | `747` |
| `122` | `6` | `421` Cyclic autoswitch control | Candidate alternative | `1477` | `421` | `748` |
| `122` | `6` | `426` Staircase light control | Candidate alternative | `1485` | `426` | `749` |
| `122` | `6` | `427` Floor call control | Candidate alternative | `1493` | `427` | `750` |
| `122` | `6` | `462` Open lock command on session | Candidate alternative | `1501` | `489` | `751` |
| `122` | `7` | `410` Light control | Fixed/designated metadata | `2313` | `410` | `985` |
| `122` | `7` | `411` Automation control | Candidate alternative | `1406` | `411` | `739` |
| `122` | `7` | `412` Lock/unlock actuator control | Candidate alternative | `1414` | `412` | `740` |
| `122` | `7` | `413` Scenario module control | Candidate alternative | `1422` | `413` | `741` |
| `122` | `7` | `414` Scheduled scenario | Candidate alternative | `1430` | `414` | `742` |
| `122` | `7` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1438` | `415` | `743` |
| `122` | `7` | `416` Scheduled scenario PLUS | Candidate alternative | `1446` | `416` | `744` |
| `122` | `7` | `417` `AUX` control | Candidate alternative | `1454` | `417` | `745` |
| `122` | `7` | `418` Open lock control | Candidate alternative | `1462` | `418` | `746` |
| `122` | `7` | `419` Sound diffusion control | Candidate alternative | `1470` | `419` | `747` |
| `122` | `7` | `421` Cyclic autoswitch control | Candidate alternative | `1478` | `421` | `748` |
| `122` | `7` | `426` Staircase light control | Candidate alternative | `1486` | `426` | `749` |
| `122` | `7` | `427` Floor call control | Candidate alternative | `1494` | `427` | `750` |
| `122` | `7` | `462` Open lock command on session | Candidate alternative | `1502` | `489` | `751` |
| `122` | `8` | `410` Light control | Fixed/designated metadata | `2314` | `410` | `985` |
| `122` | `8` | `411` Automation control | Candidate alternative | `1407` | `411` | `739` |
| `122` | `8` | `412` Lock/unlock actuator control | Candidate alternative | `1415` | `412` | `740` |
| `122` | `8` | `413` Scenario module control | Candidate alternative | `1423` | `413` | `741` |
| `122` | `8` | `414` Scheduled scenario | Candidate alternative | `1431` | `414` | `742` |
| `122` | `8` | `415` Scenario PLUS Lighting Management | Candidate alternative | `1439` | `415` | `743` |
| `122` | `8` | `416` Scheduled scenario PLUS | Candidate alternative | `1447` | `416` | `744` |
| `122` | `8` | `417` `AUX` control | Candidate alternative | `1455` | `417` | `745` |
| `122` | `8` | `418` Open lock control | Candidate alternative | `1463` | `418` | `746` |
| `122` | `8` | `419` Sound diffusion control | Candidate alternative | `1471` | `419` | `747` |
| `122` | `8` | `421` Cyclic autoswitch control | Candidate alternative | `1479` | `421` | `748` |
| `122` | `8` | `426` Staircase light control | Candidate alternative | `1487` | `426` | `749` |
| `122` | `8` | `427` Floor call control | Candidate alternative | `1495` | `427` | `750` |
| `122` | `8` | `462` Open lock command on session | Candidate alternative | `1503` | `489` | `751` |
| `122` | `9` | `130` User interface settings | Fixed/designated metadata | `1504` | `480` | `752` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `122` | `521` Soft-Touch command virgin | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `46` |

All eight command slots have the same fourteen associated external Objects; slot `9` holds only Object `130`. Object `410` has fixed/designated metadata on command slots, while the thirteen alternatives are candidate relationships. Virgin Object `521` is associated with slots `1..8`, not slot `9`. Database key `489` in this page identifies external Object `462`; it is unrelated to external Object `489` in the adjacent DND/MUR control dossier.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `122` | Virtual Configuration | `1` | Catalogue association `1` |
| `122` | Advanced Configuration | `2` | Catalogue association `2` |
| `122` | Physical configuration | `0` | Catalogue association `3` |
| `122` | Product Programming | `3` | Catalogue association `4` |

Both technical sheets document physical configurators and MyHOME Suite software configuration. The software route uses the PC Ethernet network and external MH201 scenario module; the control/indicator itself remains on SCS BUS. No connection association is stored for this firmware in `AS_CONNECTION_FIRMWARE`; this absence does not invalidate the published Ethernet route. Product Programming is additionally registered for firmware `122`; the source does not equate its mode number with a runtime protocol frame.

| Parameter scope | Registered paths | Evidence / boundary |
| --- | --- | --- |
| BTicino brand model `1`, line models `1` and `3` | `xml/SDC/sdc.xml`; `1678_1.0_BT/xml/SVM/svm.xml`, `1678_1.0_BT/xml/Extra/extra.xml`, `1678_1.0_BT/xml/DIRECTOR/director.xml`, `1678_1.0_BT/xml/Protocol/protocol.xml` | Catalogue parameter associations; referenced payloads not examined |
| Legrand brand model `2`, line model `4` | `xml/SDC/sdc.xml`; `1678_1.0_LG/xml/SVM/svm.xml`, `1678_1.0_LG/xml/Extra/extra.xml`, `1678_1.0_LG/xml/DIRECTOR/director.xml`, `1678_1.0_LG/xml/Protocol/protocol.xml` | Parameter model codes are separate from commercial line keys |

## Firmware-scoped configuration

Domains and defaults below are catalogue evidence. `AID` is an eight-character mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `122` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `122` | `A` | `0..9`; `14` = `CEN` | `0` | A; Enviroment (0-9 `GEN`,`GR`,`AMB`) |
| `122` | `PL` | `0..9` | `0` | PL; Lighting point (0-9) |
| `122` | `M` | `0..2`; `6`; `9` = `O/I`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN` | `0` | M; Mode physical configurator (0-2,6,`O/I`,SU_GIU,SU_GIU_M,`CEN`) |
| `122` | `LED` | `0..9`; `10` = `OFF`; `11` = `ON` | `0` | LED; User interface settings configurator (0-9, `OFF`, `ON`) |

### Published physical modes

| Configurator / mode | Published applicability | Evidence |
| --- | --- | --- |
| `A`, `PL` | An A/PL address is required in every mode; source physical point address uses `A=0..9`, with F420 `PL=1..9` | `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1; `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=0` | Cyclic self-learning; an existing or otherwise unused A/PL address may be used | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=6` | Non-cyclic learning; learned `ON` assigns left `ON`/increase and right `OFF`/decrease; a learned single function leaves paired key unused or preserves its previous function | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=1`, `M=2` | F420 scenario recall/program/delete; same A/PL as F420; key `k=1..8` recalls scenario `k` for `M=1` or `k+8` for `M=2`; two controls reach sixteen scenarios | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=0/I` (catalogue `9`) | Four horizontal pairs; left `ON`/right `OFF`; individual point short press switches, long press adjusts; room/group controls switch only | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| `M=↑↓` (catalogue `12`) | Four shutter pairs, full travel after press | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| `M=↑↓M` (catalogue `13`) | Four shutter pairs, movement only while held | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| Paired addressing | First pair uses configured A/PL, next three use consecutive points; `AMB`/`GR` in A selects consecutive rooms/groups starting with PL | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| `M=CEN` (catalogue `14`) | Dedicated scenario-programmer software associates keys; unique A/PL required; `A=0, PL=0` forbidden | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |

### Published LED configurator mapping

| Physical LED token | Brightness | Catalogue value |
| --- | --- | --- |
| `0` | `30 %` | `0` |
| `1` | `10 %` | `1` |
| `2` | `15 %` | `2` |
| `3` | `20 %` | `3` |
| `4` | `25 %` | `4` |
| `5` | `30 %` | `5` |
| `6` | `40 %` | `6` |
| `7` | `50 %` | `7` |
| `8` | `60 %` | `8` |
| `9` | `80 %` | `9` |
| `OFF` | Off | `10` |
| `ON` | `100 %` | `11` |


This table is printed on technical-sheet p. 3 / PDF p. 3 in both languages. The default physical token `0` is `30 %`; these tokens are not Object `130` level numbers.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `410` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON`/`OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON`/`OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129`, 131 |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |


### Object `411` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (`UP/DOWN`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `412` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `413` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0` = `A=0` `PL=0`; `1` = `A=0` `PL=1`; `2` = `A=0` `PL=2`; `3` = `A=0` `PL=3`; `4` = `A=0` `PL=4`; `5` = `A=0` `PL=5`; `6` = `A=0` `PL=6`; `7` = `A=0` `PL=7`; `8` = `A=0` `PL=8`; `9` = `A=0` `PL=9`; `10` = `A=0` `PL=10`; `11` = `A=0` `PL=11`; `12` = `A=0` `PL=12`; `13` = `A=0` `PL=13`; `14` = `A=0` `PL=14`; `15` = `A=0` `PL=15`; `16` = `A=1` `PL=0`; `17` = `A=1` `PL=1`; `18` = `A=1` `PL=2`; `19` = `A=1` `PL=3`; `20` = `A=1` `PL=4`; `21` = `A=1` `PL=5`; `22` = `A=1` `PL=6`; `23` = `A=1` `PL=7`; `24` = `A=1` `PL=8`; `25` = `A=1` `PL=9`; `26` = `A=1` `PL=10`; `27` = `A=1` `PL=11`; `28` = `A=1` `PL=12`; `29` = `A=1` `PL=13`; `30` = `A=1` `PL=14`; `31` = `A=1` `PL=15`; `32` = `A=2` `PL=0`; `33` = `A=2` `PL=1`; `34` = `A=2` `PL=2`; `35` = `A=2` `PL=3`; `36` = `A=2` `PL=4`; `37` = `A=2` `PL=5`; `38` = `A=2` `PL=6`; `39` = `A=2` `PL=7`; `40` = `A=2` `PL=8`; `41` = `A=2` `PL=9`; `42` = `A=2` `PL=10`; `43` = `A=2` `PL=11`; `44` = `A=2` `PL=12`; `45` = `A=2` `PL=13`; `46` = `A=2` `PL=14`; `47` = `A=2` `PL=15`; `48` = `A=3` `PL=0`; `49` = `A=3` `PL=1`; `50` = `A=3` `PL=2`; `51` = `A=3` `PL=3`; `52` = `A=3` `PL=4`; `53` = `A=3` `PL=5`; `54` = `A=3` `PL=6`; `55` = `A=3` `PL=7`; `56` = `A=3` `PL=8`; `57` = `A=3` `PL=9`; `58` = `A=3` `PL=10`; `59` = `A=3` `PL=11`; `60` = `A=3` `PL=12`; `61` = `A=3` `PL=13`; `62` = `A=3` `PL=14`; `63` = `A=3` `PL=15`; `64` = `A=4` `PL=0`; `65` = `A=4` `PL=1`; `66` = `A=4` `PL=2`; `67` = `A=4` `PL=3`; `68` = `A=4` `PL=4`; `69` = `A=4` `PL=5`; `70` = `A=4` `PL=6`; `71` = `A=4` `PL=7`; `72` = `A=4` `PL=8`; `73` = `A=4` `PL=9`; `74` = `A=4` `PL=10`; `75` = `A=4` `PL=11`; `76` = `A=4` `PL=12`; `77` = `A=4` `PL=13`; `78` = `A=4` `PL=14`; `79` = `A=4` `PL=15`; `80` = `A=5` `PL=0`; `81` = `A=5` `PL=1`; `82` = `A=5` `PL=2`; `83` = `A=5` `PL=3`; `84` = `A=5` `PL=4`; `85` = `A=5` `PL=5`; `86` = `A=5` `PL=6`; `87` = `A=5` `PL=7`; `88` = `A=5` `PL=8`; `89` = `A=5` `PL=9`; `90` = `A=5` `PL=10`; `91` = `A=5` `PL=11`; `92` = `A=5` `PL=12`; `93` = `A=5` `PL=13`; `94` = `A=5` `PL=14`; `95` = `A=5` `PL=15`; `96` = `A=6` `PL=0`; `97` = `A=6` `PL=1`; `98` = `A=6` `PL=2`; `99` = `A=6` `PL=3`; `100` = `A=6` `PL=4`; `101` = `A=6` `PL=5`; `102` = `A=6` `PL=6`; `103` = `A=6` `PL=7`; `104` = `A=6` `PL=8`; `105` = `A=6` `PL=9`; `106` = `A=6` `PL=10`; `107` = `A=6` `PL=11`; `108` = `A=6` `PL=12`; `109` = `A=6` `PL=13`; `110` = `A=6` `PL=14`; `111` = `A=6` `PL=15`; `112` = `A=7` `PL=0`; `113` = `A=7` `PL=1`; `114` = `A=7` `PL=2`; `115` = `A=7` `PL=3`; `116` = `A=7` `PL=4`; `117` = `A=7` `PL=5`; `118` = `A=7` `PL=6`; `119` = `A=7` `PL=7`; `120` = `A=7` `PL=8`; `121` = `A=7` `PL=9`; `122` = `A=7` `PL=10`; `123` = `A=7` `PL=11`; `124` = `A=7` `PL=12`; `125` = `A=7` `PL=13`; `126` = `A=7` `PL=14`; `127` = `A=7` `PL=15`; `128` = `A=8` `PL=0`; `129` = `A=8` `PL=1`; `130` = `A=8` `PL=2`; `131` = `A=8` `PL=3`; `132` = `A=8` `PL=4`; `133` = `A=8` `PL=5`; `134` = `A=8` `PL=6`; `135` = `A=8` `PL=7`; `136` = `A=8` `PL=8`; `137` = `A=8` `PL=9`; `138` = `A=8` `PL=10`; `139` = `A=8` `PL=11`; `140` = `A=8` `PL=12`; `141` = `A=8` `PL=13`; `142` = `A=8` `PL=14`; `143` = `A=8` `PL=15`; `144` = `A=9` `PL=0`; `145` = `A=9` `PL=1`; `146` = `A=9` `PL=2`; `147` = `A=9` `PL=3`; `148` = `A=9` `PL=4`; `149` = `A=9` `PL=5`; `150` = `A=9` `PL=6`; `151` = `A=9` `PL=7`; `152` = `A=9` `PL=8`; `153` = `A=9` `PL=9`; `154` = `A=9` `PL=10`; `155` = `A=9` `PL=11`; `156` = `A=9` `PL=12`; `157` = `A=9` `PL=13`; `158` = `A=9` `PL=14`; `159` = `A=9` `PL=15`; `160` = `A=10` `PL=0`; `161` = `A=10` `PL=1`; `162` = `A=10` `PL=2`; `163` = `A=10` `PL=3`; `164` = `A=10` `PL=4`; `165` = `A=10` `PL=5`; `166` = `A=10` `PL=6`; `167` = `A=10` `PL=7`; `168` = `A=10` `PL=8`; `169` = `A=10` `PL=9`; `170` = `A=10` `PL=10`; `171` = `A=10` `PL=11`; `172` = `A=10` `PL=12`; `173` = `A=10` `PL=13`; `174` = `A=10` `PL=14`; `175` = `A=10` `PL=15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |


### Object `414` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `415` - Scenario PLUS Lighting Management

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON`/`OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |


### Object `416` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `417` - `AUX` control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |


### Object `418` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |


### Object `419` - Sound diffusion control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON`/`OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |


### Object `421` - Cyclic autoswitch control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


### Object `426` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `130` - User interface settings

Catalogue Object key `480` maps to external Object `130`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `STATE_OF_UNUSED_BUTTON` | `0` = `ON`; `1` = `OFF` | `1` | State of unused button; Default depends on device |
| `STATE_UPDATE` | `0` = No; `1` = Yes | `1` | Feedback update; Default depends on device |
| `LED_LEVEL` | `0..10` | `6` | LED intensity level; Default, minimum level (0), maximum level (10) and distribution of intermediate levels depend on device |
| `LED_FADE` | `0..10` | `5` | LED fading; Default, minimum level (0), maximum level (10) and distribution of intermediate levels depend on device |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 | `1` | Backlight intensity stand by level |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `BACKLIGHT_DELAY` | `0..255` | `15` | Delay time (seconds); Time en second to light off the backlight |
| `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable | `1` | Proximity Activation |
| `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase | `2` | Signboard activation type |


### Object `462` - Open lock command on session

Catalogue Object key `489` maps to external Object `462`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

### Reconciled Object notes

| Surface | Device-specific interpretation | Evidence / limit |
| --- | --- | --- |
| Command Objects `410..419`, `421`, `426`, `427`, `462` | Selectable command roles for slots `1..8`; target address, group, action, timing and scenario domains remain separate per Object | Reusable tables above; apply the 25 firmware/Object filter associations below |
| UI Object `130` | Unused-button state, feedback, intensity/fade, standby light, delay, proximity and signboard fields are reusable configuration evidence | Several descriptions explicitly make defaults/distribution Device-dependent; proximity field does not establish a physical sensor |
| Physical LED versus UI levels | Physical token `0` yields `30 %`; Object `LED_LEVEL` has stored default `6` | No conversion associates physical percentages with Object values; preserve separate defaults |
| Learning versus Object selection | Publisher learning procedures associate commands; catalogue alternatives expose reusable capability | No stored predicate chooses one active Object; no inferred selection precedence |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `122` | `410` | `1699` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `411` | `1538` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `412` | `1546` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `413` | `1554` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `414` | `1569` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `414` | `1570` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Modality |
| `122` | `415` | `1578` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `416` | `1593` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `416` | `1594` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Modality |
| `122` | `417` | `1602` | `TYPE_CONTACT` | No legal values specified in source (entire reusable range retained) | `0` | Contact type |
| `122` | `419` | `1610` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `122` | `419` | `3008` | `SUB_SOURCE` | `0..255` (entire reusable range retained) | `0` | Sub source |
| `122` | `419` | `3009` | `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video (entire reusable range retained) | `3` | Channel (BB-Stereo) |
| `122` | `426` | `4109` | `N1` | `100..255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `122` | `427` | `1625` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `122` | `427` | `1626` | `TO_ALL` | `1` = General | `1` | Type of call |
| `122` | `427` | `1906` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `122` | `130` | `1627` | `STATE_UPDATE` | `0` = No; `1` = Yes (entire reusable range retained) | `1` | Feedback update |
| `122` | `130` | `1628` | `LED_FADE` | `0..10` (entire reusable range retained) | `5` | LED fading |
| `122` | `130` | `1629` | `STATE_OF_UNUSED_BUTTON` | `0` = `ON`; `1` = `OFF` (entire reusable range retained) | `1` | State of unused button |
| `122` | `130` | `3116` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | Backlight intensity stand by level |
| `122` | `130` | `3123` | `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Proximity Activation |
| `122` | `130` | `3130` | `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase (entire reusable range retained) | `2` | Signboard activation type |
| `122` | `130` | `3138` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `122` | `130` | `3161` | `BACKLIGHT_DELAY` | `0..255` (entire reusable range retained) | `15` | Delay time (seconds) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule or selection predicate is associated with these placements. Validate the firmware domain and the selected Object/Firmware filters separately; empty selection metadata does not establish an active Object. Generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Compare discovered model and system with catalogue main model `49` in Automation; this is a source-derived identification target, not a verified response | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Corroborate installed firmware before relating observations to catalogue `1.0.1`; no hardware fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Corroborate hardware revision separately from firmware; no verified response retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Corroborate microcontroller revision if this managed Device supports the query; no verified response retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Discover active Objects and Modules: command slots `1..8` may expose the associated command Objects; slot `9` is Object `130`; Virgin Object `521` is a catalogue candidate. Do not report database relation IDs as KEYO | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Read applicable active Object addressing; resolve each command target and Device A/PL separately; device address encoding requires actual discovery context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Read/compare the selected Object configuration against its reusable domain/default and firmware context; default is not installed state | [Configuration](../../diagnostics/dim35-configuration.md) |

These are candidate corroboration surfaces of the managed Device model. Catalogue associations do not prove that every operation succeeds on this firmware/transport. Automation diagnostics use `WHO 1001` in the canonical system context.

## Functional applicability

| Function family | Device applicability | Canonical reference |
| --- | --- | --- |
| Lighting | Object `410`, or learned/paired commands with matching targets | [`WHO 1`](../../functional/who-1-lighting/) |
| Shutter automation / actuator locking | Objects `411` / `412`; full-travel or monostable behavior depends on mode and target | [`WHO 2`](../../functional/who-2-automation/) |
| Scenario module / scheduler | Objects `413`, `414`; physical F420 or configured external programmer; `CEN` unique A/PL requirement | [`WHO 0`](../../functional/who-0-scenarios/); [`WHO 17`](../../functional/who-17-scenario-management/) |
| PLUS / Lighting Management | Objects `415`, `416`; reusable catalogue alternatives, not a claim every physical configurator selects them | [`WHO 25`](../../functional/who-25-transversal/); [`WHO 24`](../../functional/who-24-lighting-management/) |
| Auxiliaries | Object `417`, target `AUX` control | [`WHO 9`](../../functional/who-9-auxiliaries/) |
| Video door entry | Objects `418`, `421`, `426`, `427`, `462`: lock, cyclic selection, staircase light, floor call and session lock roles | [`WHO 6`](../../functional/who-6-basic-video-door-entry/); exact selected target/system matters |
| Sound diffusion | Object `419`; learned sound commands and appropriate installed sound system | [`WHO 22`](../../functional/who-22-sound-diffusion/) |
| User interface | Object `130`, slot `9`; reusable LED/standby/UI settings | Catalogue surface; does not create an additional externally exposed functional command family |

## Observed behavior and corroboration

No sanitized hardware fingerprint, protocol capture or commissioning experiment is retained for this exact technical item. Source diagrams, room number `127`, switch states and example addresses are publisher illustrations, not observed project installations.

## Programming

MyHOME Suite software configuration uses PC Ethernet through MH201 to the SCS system; it offers more options than physical configuration. The technical sheets do not define a complete transfer wizard, erase scope, firmware-update package or recovery procedure. Validate the active Object and its complete configuration before applying changes; absence of slot predicates does not supply a selection algorithm.

### Published learning and scenario workflow

| Operation | Published procedure / timing | Evidence |
| --- | --- | --- |
| Learn or replace a key | Press/release rear programming key: slow LED flash; within `20 s` press target key: rapid flash; operate target control/actuator: slow flash; repeat per key; short rear-key press or `20 s` timeout exits | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Delete one learned key | Enter learning; within `20 s` hold target key `4 s`; LEDs at full power `4 s`; repeat as needed; short rear-key press or `20 s` timeout exits | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Delete all learned keys | Enter learning with short rear-key press; hold rear key again `10 s`; LEDs on about `4 s` confirm deletion | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Non-cyclic learning | `M=6` automatically pairs `ON`/increase left and `OFF`/decrease right for learned lighting commands; single-function pair counterpart remains unused or retains prior assignment | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Program or replace F420 scenario | Enable F420 learning (green LED; red disables); short control rear-key press gives slow `1 s` on / `1 s` off; select scenario key within `20 s`; rapid flash; establish target states; press control programming key to finish; repeat; press F420 learning key or wait `20 s` to end (red LED) | `MM00778-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Delete one F420 scenario | Enable F420 learning; enter control programming; within `20 s` hold scenario key `4 s`; rapid flash `4 s`; repeat; short rear-key press or `20 s` timeout exits | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| Erase F420 memory | Enable F420 programming, hold its own `DEL` key `10 s`; separate from deleting all learned commands on the control | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| Paired control / `CEN` | Paired modes need no additional learning or F420; `CEN` is associated in programmer software and needs unique nonzero A/PL | `MM00778-a-EN` / French counterpart, printed p. 3 / PDF p. 3 |
| Customize labels | Release front, remove original card, insert black/white replacement and refit; custom A5 card printed then cut using the illustrated sequence; label tool is in MyHOME Suite | `LE06019AA`, no printed pagination / PDF p. 1; `MM00778-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |

## Source reconciliation

The English and French technical sheets have the same `a`, `02/12/2013` revision and agree on the Device-specific specifications, modes, procedures and scope described above. Their three-reference headers independently support the catalogue cluster. General vendor/contact text and certification marks remain in the originals; listed standards are publisher declarations, not a new certification audit. Physical wiring-device module count is independent of protocol Module count. Catalogue status/default metadata and published operating descriptions are not observations of installed firmware or behavior.

| Source issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Title and capability | Catalogue “8 scenarios control” is narrower than the documented multifunction modes; preserve title as metadata without suppressing command alternatives | Item `1678`; both sheets pp. 1-3 |
| Address selector | Firmware A domain includes value `14` labelled `CEN`, while its description mentions `GEN`/`GR`/`AMB`; physical sheet uses `AMB`/`GR` in A and `CEN` in M. No conversion or selection predicate resolves this | Firmware A/M domains; both sheets p. 3 |
| Scenario-programmer naming | English introduction/matching name MH200N/MH201 but its final requirement says MH200/MH201. The French and Italian counterparts consistently name MH200N/MH201, supporting a translation omission; no MH200/MH200N hardware equivalence inferred | Both sheets pp. 1, 3 |
| Current rating | Dated common sheet says LEDs-off `5 mA`, full LEDs `20 mA`; live H4652 says rated/standby `20 mA`, live LN4652 rated `21 mA`. Distinct conditions/variants preserved; reason for 21 mA unresolved | Both sheets p. 1; retained product-sheet exports |
| Accessory colours | Both sheets and LE06019AA identify 3541/067595 black and 3542/067596 white; retained French catalogue CM220600 p. 982 reverses the labels: 3541 white, 3542 black. No product/revision explanation resolves the conflict; retain both source-scoped inventories | Sheets p. 1; LE06019AA; known `cm220600_0982.pdf` |
| Restricted command targets | Object `426` N1 permits only `100..255` while reusable default `0` is outside the subset. Object `427` TO_ALL permits only `1` (General), while the reusable domain is broader; do not invent replacement defaults | Filters `4109`, `1626` |
| Reusable source irregularities | Object `417` TYPE_CONTACT has default `0` but no legal values specified; Object `419` CHANNEL assigns the same Left and video label to `9` and `11`. No guessed correction | Reusable Objects `417`, `419`; corresponding filters retain the source ranges |
| UI capability | Reusable Object `130` proximity/signboard settings and default LED level do not establish a sensor, map to physical LED percentages or prove firmware acceptance | Object `130`; filters retain the affected reusable ranges, with no conversion to physical percentages |
| Voice / network catalogue attributes | Live H/LN product pages mark voice command, internet-box connectivity and interoperability, while connected-object is No and the device uses SCS. No onboard microphone, IP endpoint or standalone voice service inferred | Retained product sheets, printed pp. 2-3 / PDF pp. 2-3 |

The illustrated instruction revision `LE06019AA-02PC-13W21` has been incorporated for label handling. Black/white stock and custom print/cut sequences supplement the technical-sheet accessory inventory.

Italian `MM00778-a-IT` revision a independently agrees on all three references, specifications, legal physical modes, complete LED mapping and programming timings. Its final `CEN` requirement retains the MH200N name. French `CM220600`, printed p. 982 / PDF p. 1, confirms Axolute and LivingLight identities, point/group/general lighting and shutter/scenario roles, label customization, and the requirement for the appropriate plate/support (Axolute catalogue pp. 692-693; LivingLight pp. 704-706). Its photographed `LNA4802ACS` brushed-steel plate is an accessory. The reversed A5 stock colours remain unresolved. Separate thermostat, controller, PMS and supervision-software blocks do not specify additional capabilities of this eight-key control.

The initial dossier used live product-page attributes without retaining a file. This revision replaces those evidence entries with original manufacturer PDF exports, downloaded through the publisher’s product-sheet endpoint with technical characteristics included, uploaded and registered on `main` before incorporation. These preserve the cited ratings, dimensions, material/interface attributes and their discrepancies. Their `03.10.2026` date identifies the export, not an installed release. General bus-classification, commercial image and download-list attributes establish no additional runtime commands; the PDF’s existing document references are recorded as discovery provenance. The earlier HTML response was not archived, and no earlier byte identity is reconstructed.

## Evidence limits and open work

- Resolve 3541/3542 accessory colours: three 2013 technical-sheet languages and LE06019AA say black/white, while the retained French commercial catalogue p. 982 says white/black.
- Resolve the `A=14/CEN` selector, `AMB`/`GR` encoding, MH200 versus MH200N wording and SKU/current-condition discrepancies with exact software or hardware evidence.
- Inspect registered product-parameter XML payloads and establish accepted Object selection, UI level mapping, proximity/signboard applicability and serialization.
- Corroborate all nine Modules, active command Objects, Virgin Object `521`, learning/deletion timing and published `CEN` address restrictions with sanitized captures.
- Retained exact-product source reconciliation is scoped to the listed revisions; current commercial catalogues/translations and future revisions can extend it. Current catalogue facts are now backed by retained original publisher product-sheet exports dated `03.10.2026`.

## Sources

Catalogue tables were read from the registered `MHCatalogue.db` original, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. `EN_ITEM`, `EN_DEVICE`, firmware/system associations, `EN_SLOTS`, Object/Virgin relationships, `EN_CONF`/`EN_CONF_RANGE`, slot conditions, filters, conversions and configuration-mode associations define the implementation scope. Exact archived PDF revisions and publisher URLs are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue metadata and retained fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
- [H4652 official catalogue](https://www.bticino.com/products/bt-h4652)
- [LN4652 official catalogue](https://www.bticino.com/products/bt-ln4652)
- [Retained Italian technical-sheet publisher source](https://dar.bticino.com/asset/Documents/MM00778_a_IT.pdf)
- [Retained French catalogue-page publisher source](https://assets.legrand.com/general/legrand-fr/pc/cm220600_0982.pdf)
