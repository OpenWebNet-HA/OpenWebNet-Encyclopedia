# Clock-script evidence and protocol scope

The packaged F453AV `3.0.14` and MH200N `1.1.8` clock scripts establish local operating-system helper selection, but no OpenWebNet-visible clock command, scene-timing rule or scheduling contract. Their detailed script branches belong to the [supporting component evidence](../../project/review/firmware-analysis/sequential-legacy-clock-2026-11-02/source/REPORT.txt).

A selected startup script conditionally requests a compiled date after a parsed local flag equals one. A hardware-clock command in that script is a comment. A separate wrapper has view-specific branch differences, with its natural caller and actual command/clock outcomes unresolved. These facts do not identify a CPU, prove a hardware fault or establish clock synchronization.

The encyclopedia's relevant product context remains the [F453AV webserver](../../devices/definitions/own-dev-0089-webserver-audio-video-din.md) and [MH200N scenario programmer](../../devices/definitions/own-dev-0131-mh200n-scenario-programmer.md). The [scenario engine](../../scenario-engine/README.md) documents protocol-facing scenario behavior. No relationship between these component scripts and an OpenWebNet scenario result is established by the retained evidence.
