# ScenarioSuite Database and Script Generator

The original ScenarioSuite assemblies provide a concrete implementation chain from selected [MH202 editor database](scenario-suite-database.md) rules to command strings, a script line list, `.spt` file-writer calls and `info.xml` construction. This source evidence narrows the earlier gap between catalogue declarations and the MH202 scenario scheduler. It does not constitute an executed compiler or an installed scenario.

## Source and applicability

The exact files are recovered MyHOME Suite `3.5.38` installer members under `default/targetDir/`. They accompany package `1902_1.0_LGG`; database version `1.0.53` and MH202 Firmware `1.0.24` remain separate applicability scopes.

| Assembly | Selected role |
| --- | --- |
| `Bticino.ScenarioSuite.Core.dll` | Rule materialization, field resolution, command/script construction and writers |
| `Bticino.ScenarioSuite.DataManager.dll` | SQL query construction and dataset population |
| `Bticino.ScenarioSuite.Class.dll` | Field-object initialization and property storage |

The [source evidence](../project/review/firmware-analysis/next-investigations-2026-10-31/) retains exact installer-member hashes, method identities, raw code, reviews and analysis method. These findings come from static assembly inspection and read-only database analysis; the vendor CLR/compiler and generated scripts were not executed.

## Rule selection and command construction

DataManager `GetOPENRuleCompile`, takes object, optional command, area and output-dataset parameters. Its original area switch selects the following compile-rule column:

| Editor area | Selected column |
| ---: | --- |
| 3 | `TRIGGER_START_AREA` |
| 4 | `COND_OK_AREA` |
| 5 | `ACT_AREA` |
| 6 | `TRIGGER_STOP_AREA` |
| 7 | `TRIGGER_ENABLE` |
| 8 | `TRIGGER_DISABLE` |
| 9 | `PANIC_KEY` |

The selected query filters `ANA_OPEN_RULE_COMPILE` by object, nonzero selected flag and supplied command. This establishes one actual consumer of those flags. Upstream editor object permissions and association filtering remain separate: an alarm row with `ACT_AREA=1` does not establish that the MH202 editor offers alarm arming actions.

The DataManager's ordinary return `1` can accompany no added table when Fill's stored count is not positive. Core `GetOPENRuleCompile`, selects a default rule on its positive-manager/missing-named-table path; manager return `0` instead selects local `-3`. Thus a missing flagged row is not by itself a universal compiler failure verdict.

Core's row materializer copies the selected flags and all ten `OPEN_FIELD` values. It sets separate `COND_KO_AREA` and `ACT_ELSE_AREA` properties directly to `0`. The default rule orders `ID_CHI`, `ID_COSA`, `ID_DOVE`, whereas selected Counter/Boolean rows order `#ID_CHI`, `ID_DOVE`, `ID_COSA`; these are not interchangeable templates.

`cCompiler.MakeOpenCommand`, calls the actual parameter resolver and rule consumer, substitutes selected WHO/WHAT/WHERE fields, retains literal rule content and constructs the selected leading-`*`/trailing-`##` command. It stores that string in `cCommandSupport.MakeOpen`. No specific Counter or alarm command was executed through this compiler.

Evidence: [generator report](../project/review/firmware-analysis/next-investigations-2026-10-31/mh202-generator-report.txt), [independent source review](../project/review/firmware-analysis/next-investigations-2026-10-31/mh202-generator-source-review.txt).

## Counter text-field namespace

Equal `ID_KIND` numbers in `ANA_RANGE` and `ANA_TEXT` do not establish the same field definition.

Core `AddAuxFieldWhat`, switches on GraphicType−1 : graphic1 selects combo values, graphic2 range values and graphic3 text values. The text path passes the same auxiliary definition's IdKind to `GetTextFieldValues` ; DataManager's actual query selects `ANA_TEXT.ID_KIND`.

| Database field | Graphic type / kind | Actual selected text row |
| --- | --- | --- |
| 29 CountValue | 3 / 2 | `CountValue`, literal `[0-32000]` |
| 31 IfCountValue | 3 / 2 | Same text row `2` |
| 30 ValueStep | 3 / 3 | `ValueStep`, literal `[0-32000]` |

The source strips the bracket delimiters, splits on `-` and converts the two components. This is a range-description parser, without proof that the literal is evaluated as a .NET regular expression or that every editor input is constrained by it.

The selected text branch constructs a new `cAux_Field`; its original constructor initializes multiplier `1`. That branch does not copy the multiplier `10` from `ANA_RANGE.ID_KIND = 2`. The selected graphic `3` / conversion `0` compiler path multiplies the stored value by the object's multiplier before string substitution, under ordinary unchanged-property/provider premises. Saved-project mutation and complete UI enforcement remain unexecuted.

The temperature/time-labelled range rows remain database facts; the actual graphic-type dispatcher excludes the earlier proposed connection from those rows to these Counter text fields. They supply no Counter temperature/time units. The current text declarations corroborate the selected firmware `0..32000` guards without establishing automatic propagation between WHO `17` slots and named interpreter variables.

Evidence: [query and field-consumer report](../project/review/firmware-analysis/next-investigations-2026-10-31/mh202-database-consumers-report.v3.txt), [independent source review](../project/review/firmware-analysis/next-investigations-2026-10-31/mh202-database-consumers-source-review.txt). The source record preserves the superseded range-row interpretation and its correction.

## Status rules and script writers

The status-rule manager separately selects object/command rows without an area flag. Its Core consumer copies request/reply dimensions, function, parameter and custom-valuation properties. Selected Counter row `65` contains `EXTRACTVALUE`, reply dimension `6` and parameter string `1`.

`CompileScenario`, calls the actual status consumer and transfers those properties into its support state. Its original format is `{0} {1}=EXTRACTVALUE({2},{3},"{4}",{5}%,{6})`; argument construction reads ReplyDimension and ReplyPar. This establishes declaration-to-template use, without determining reply-parameter indexing or evaluating a real reply.

`cCore.CompileAll`, constructs the selected pathname `OutputFolder/ID.spt/ID.spt` and passes it to `CompileScenario`. The latter constructs `StreamWriter(FileSPT,false)` , requests `WriteLine` for its line list and closes the writer. Error/action-count branches can instead remove output or request an `.err` file.

CompileAll separately constructs XML rooted `script`, creator data, panic/scenario entries, name `ID.spt`, numeric id, description and scen_name, then requests `XmlDocument.Save` on `OutputFolder/info.xml`. These are actual writer call sites, rather than substring matches or observed output files.

Header/control construction includes `$NOMESCRIPT`, `$RESTART` with SI/NO, BEGIN, END, IIF, GOTO, OWRITE, SLEEP and SLEEPRANDOM. Selected repeat handling constructs a GOTO using a stored BEGIN label. The [MH202 generated-script consumers](../reverse-engineering/firmware-analysis/mh202-1.0.24-generated-scenarios.md) compare bounded original producer/consumer paths without claiming a complete naturally generated/executed scenario.

## Remaining evidence needed

Method ownership, selected database filtering, field-kind dispatch and writer requests are established static implementation evidence. A genuine configured project and controlled generated export are still needed for exact emitted bytes, complete compiler/error behavior and deployment compatibility. Full UI permission precedence, EXTRACTVALUE evaluation/indexing, complete Start/OnlyIf/action execution, Stop/panic/restart recovery, active providers and Physical Device behavior remain open.
