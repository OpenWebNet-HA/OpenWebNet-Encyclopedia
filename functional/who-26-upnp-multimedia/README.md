# `WHO 26` - UPnP Multimedia

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 26` as a UPnP multimedia command namespace.

## Protocol position

`WHO 26` belongs to the broader multimedia area but remains independent from camera/video [`WHO 7`](../who-7-multimedia-video/), Sound System [`WHO 16`](../who-16-sound-system/), and Sound Diffusion [`WHO 22`](../who-22-sound-diffusion/). Shared concepts such as media, source, playback, or navigation do not imply shared numeric encodings.

## Corpus status

The current implementation corpus establishes the namespace but does not yet support a complete system-specific `WHAT`, `WHERE`, or `DIMENSION` reference. No public dedicated `WHO 26` specification is present in the canonical PDF set used by this repository.

Parsers should therefore preserve `WHO 26` traffic losslessly and expose unknown fields as raw values. Semantics from `WHO 7`, `16`, or `22` must not be copied into this namespace without direct evidence.

## Historical OpenXml client

The BTicino touchscreen library at `TS10_1_0_23` implements a separate local OpenXml media service. Its [UTF-8 envelope and framing](../../protocol/stream-parsing.md#separate-multimedia-xml-transport) are distinct from numeric OpenWebNet frames. The following XML tags are verified in its serializers and response tests; they do not establish corresponding numeric `WHAT` values or support by external gateways.

| XML request | Arguments | Response tag and decoded content |
| --- | --- | --- |
| `RW26C1` | None | `AW26C1`: `server/name` list |
| `RW26C2` | `id` | `AW26C2`: selected `current_server`, directory `status_browse`, or selected track's `DIDL-Lite` metadata |
| `CW26C7` | None | `AW26C7`: parent-directory browsing result |
| `CW26C10` / `CW26C11` | None | `AW26C10` / `AW26C11`: next / previous track metadata |
| `RW26C15` | `rank`, `delta` | `AW26C15`: `total`, `rank`, directory names and track records |
| `CW26C16` | `server`, slash-joined `path` | `AW26C16`: navigation-context result |

Selection uses the same `id` argument for a server, directory or file. Tested browsing outcomes include `browse_okay`, `empty_directory`, `already_at_root` and `no_such_directory`, depending on the operation. Track records contain a resource URL and, for audio, title, artist, album and duration. XML error text is mapped into local application errors; those enum numbers are not wire return codes.

See [OpenXml service evidence](../../project/review/myopencommunity-coverage-audit.md#openxml-media-vocabulary).

### Local playlist integration

BtExperience at revision `b88cdac9665d28494f19d6a5d759acf8d5f00ad9`, and libqtcommon at `825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2`, share an OpenXml device between browsing and playlist control. Selecting a playlist entry sends its name to the service; the player updates the current URL when a track-selection response arrives. Next/previous adjusts the local index before the service response, so that index alone does not confirm successful selection.

The list manager emits a local server-down signal for track-selection or invalid-response server-down errors. Its error handler does not clear the current track or stop playback, and the reviewed BtExperience playlist does not connect that signal to termination or alarm fallback. Earlier touchscreen pages did consume it for page-state handling. These are implementation differences, not universal server-failure behavior.

The UPnP source object supplies explicit selection playback but inherits a false first-content result rather than discovering an initial track automatically. See [Historical local playback](../who-22-sound-diffusion/#historical-local-playback) and [Playback backend evidence](../../project/review/myopencommunity-playback-history-review.md). No numeric `WHO 26` encoding or physical playback result follows from these client paths.

### Browser state and recovery

The same pinned libqtcommon browser and BtExperience paged model maintain local navigation state separately from service responses.

| Operation / result | Implementation behavior |
| --- | --- |
| Enter a server or directory | Append its name before sending selection; a failure does not roll back that context |
| Set navigation context | Change the local level before the response; success installs the pending context, while failure reports a generic error without restoring the previous level |
| Return from a server to the server list | Set level to zero and request servers, retaining the old context until a separate reset clears it |
| Browser reset | Clear level, rank and current context; retain pending context and queued commands. A later directory response can still increment the level |
| Selection error | Browsing failure emits directory-change error, empty content emits empty-directory, and other failures emit generic error |
| Parent-navigation error | Server-down emits generic error without changing level. Other errors at level one return locally to root and trim context; deeper errors emit directory-change error |
| Model loading | Directory-change error clears the base model's loading flag; list-retrieval error clears the paged model's flag. Empty-directory and generic-error signals have no equivalent connection in these model constructors |
| Paged reply admission | Ignore replies for an inactive model or with a local answered ordinal at or below the recorded discard boundary; this discards results without cancelling commands |

Root server lists are cached locally. Service pages use one-based `rank` and a four-entry request size. Type filtering occurs after decoding, while `total` remains the service's unfiltered count. The paged model requests the next rank using the number of accepted entries. With a positive remaining count and an all-filtered page, it can repeatedly request the same rank; the archived mock tests do not exercise that service/filter combination.

The shared OpenXml device queues commands while disconnected or while a session ID is outstanding. Queued dispatch waits for the welcome state; ACK return code `200` clears SID and PID and dispatches the next command. Session cleanup leaves the queue intact, and the device's reset method is unimplemented. Answered ordinals are local bookkeeping copied from the last sent command, not response identifiers verified against the service. Earlier libraries used different queue and stale-result handling. None of these policies establishes automatic recovery or a deployed gateway contract. See [Discovery and browser lifecycle evidence](../../project/review/myopencommunity-async-browser-review.md) and [XML transport](../../protocol/stream-parsing.md#separate-multimedia-xml-transport).
