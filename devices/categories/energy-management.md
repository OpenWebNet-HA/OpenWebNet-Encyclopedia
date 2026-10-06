# Energy Management

| Device ID | Commercial identity | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0020](../definitions/own-dev-0020-load-control-panel.md) | 6-record 4673/load-panel cluster | Load Control Panel bus | Four load-status / override positions with priority and phase configuration |
| [OWN-DEV-0091](../definitions/own-dev-0091-stop-go.md) | `F80/SG` | Stop&Go | Fault-checked legacy reclosure; separate SCS accessory scope |
| [OWN-DEV-0092](../definitions/own-dev-0092-stop-go-btest.md) | `F80/SGB` | Stop&Go Btest | Legacy reclosure plus 56-day Btest; six-hour activation timing |
| [OWN-DEV-0093](../definitions/own-dev-0093-stop-go-plus.md) | `F80/SGP` | Stop&Go Plus | Fault monitoring; 30-minute recovery and 24-hour automatic-restoration limit |
| [OWN-DEV-0096](../definitions/own-dev-0096-pulses-counter-interface.md) | `3522`, `003554` | Pulses counter interface | SCS pulse accounting; clock-dependent history and physical multiplier matrix |
| [OWN-DEV-0120](../definitions/own-dev-0120-three-input-electricity-meter.md) | `F520`, `003555` | Three-input electricity meter | Three toroid inputs, stored energy history and distinct firmware/address scopes |
| [OWN-DEV-0121](../definitions/own-dev-0121-load-management-central-unit.md) | `F521`, `003557` | Load management central unit | Central load priority management and stored energy history |
| [OWN-DEV-0122](../definitions/own-dev-0122-load-actuator-current-sensor.md) | `F522`, `003558` | Load actuator with current sensor | One measured relay, local totalizers and optional residual-current sensor |
| [OWN-DEV-0123](../definitions/own-dev-0123-load-management-automation-actuator.md) | `F523`, `003559` | Load management and automation actuator | One unmetered relay combining load shedding and automation |
| [OWN-DEV-0124](../definitions/own-dev-0124-flush-mounted-load-management-actuator.md) | `HC/HS/HD4672N`, `L/N/NT4672N` | Flush-mounted load management actuator | Two-module flush relay with separate shedding indicator |
| [OWN-DEV-0134](../definitions/own-dev-0134-energy-data-logger.md) | `F524`, `003566` | Energy data logger | Catalogue role inventory; exact published specifications and evidence limits scoped in the dossier |
| [OWN-DEV-0150](../definitions/own-dev-0150-pulse-counter-interface.md) | `003576`, `3522N` | Pulse counter interface | Catalogue role inventory; exact published specifications and evidence limits scoped in the dossier |
