"""Prepare an explicitly pinned public catalogue appendix, never arbitrary inventories.

Only the accepted page's exact link activates this supplement. Numeric keys and
hexadecimal bounds are validated before rendering; free text from the JSON never
enters preparation. The result still passes the shared privacy gate and parser.
"""
import hashlib
import json
import re
from pathlib import Path

APPENDIX = 'devices/inventory/touch-screen-package-unicode-ranges.json'
LINK = '../inventory/touch-screen-package-unicode-ranges.json'
SCOPE = 'Canonical package character sets for items 1340 and 1809; not installed firmware or examined package payloads'


def supplement_text(root: Path, source_path: str, text: str) -> str:
    pins = root / 'knowledge/inputs/device-supplements.json'
    if not pins.exists():
        return text
    rules = json.loads(pins.read_text())
    if set(rules) != {'version', 'documents'} or rules['version'] != 1:
        raise ValueError('invalid Device supplement registry')
    rule = rules['documents'].get(source_path)
    if rule is None:
        return text
    if (not source_path.startswith('devices/definitions/own-dev-')
            or set(rule) != {'path', 'sha256', 'catalogue_sha256'}
            or rule['path'] != APPENDIX or f']({LINK})' not in text):
        raise ValueError('Device supplement must match the exact accepted public appendix link')
    candidate = (root / APPENDIX).resolve()
    if root.resolve() not in candidate.parents:
        raise ValueError('Device supplement escapes source root')
    raw = candidate.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != rule['sha256']:
        raise ValueError('Device supplement fingerprint changed; explicit review required')
    value = json.loads(raw)
    if (set(value) != {'source_sha256', 'scope', 'sets', 'ranges'}
            or value['scope'] != SCOPE or value['source_sha256'] != rule['catalogue_sha256']
            or not re.fullmatch('[a-f0-9]{64}', value['source_sha256'])):
        raise ValueError('invalid public catalogue appendix provenance')
    sets = value['sets']
    if sets != [{'id_unicode_set': k, 'notes': name} for k, name in enumerate(['GL1', 'GL21', 'GL31', 'GL42', 'GL51'], 1)]:
        raise ValueError('public package character-set metadata changed')
    seen = set()
    for row in value['ranges']:
        if (set(row) != {'id_unicode_set', 'id_unicode_range', 'Min', 'Max'}
                or type(row['id_unicode_set']) is not int or row['id_unicode_set'] not in range(1, 6)
                or type(row['id_unicode_range']) is not int or row['id_unicode_range'] <= 0
                or any(not isinstance(row[k], str) or not re.fullmatch('[0-9A-F]{4,6}', row[k]) for k in ['Min', 'Max'])
                or not 0 <= int(row['Min'], 16) <= int(row['Max'], 16) <= 0x10FFFF):
            raise ValueError('invalid public package character-range association')
        key = (row['id_unicode_set'], row['id_unicode_range'])
        if key in seen:
            raise ValueError('duplicate public package character-range association')
        seen.add(key)
    if len(seen) != 4534:
        raise ValueError('incomplete public package character-range inventory')
    output = ['\n## Canonical package character ranges (prepared supplement)\n',
              f'Prepared supplement from [{APPENDIX}]({LINK}); appendix SHA-256 `{digest}`; catalogue SHA-256 `{value["source_sha256"]}`. These are the accepted page\'s linked public package character-set associations for items `1340` and `1809`. They do not establish firmware identity/network field character domains, installed glyph support, or examined package payloads. The supplementary sections below are deterministic preparation of that JSON appendix; their row provenance is the named appendix, rather than additional lines in the Device Markdown file.\n']
    rows = value['ranges']
    for start in range(0, len(rows), 100):
        output += [f'### Package range associations {start + 1:04d} through {min(start + 100, len(rows)):04d}\n',
                   '| Unicode set | Range key | Minimum hexadecimal | Maximum hexadecimal |\n| --- | --- | --- | --- |']
        output += [f'| `{r["id_unicode_set"]}` | `{r["id_unicode_range"]}` | `{r["Min"]}` | `{r["Max"]}` |' for r in rows[start:start + 100]]
        output.append('')
    return text + '\n'.join(output) + '\n'
