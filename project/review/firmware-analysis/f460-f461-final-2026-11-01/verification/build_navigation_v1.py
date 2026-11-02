#!/usr/bin/env python3
"""Exclusive documentary navigation. Never imports or runs firmware/old collectors.

After the parent announces run15's saved EVIDENCE_INDEX: --capture, then default
generation. --check only reads exact current immutable inputs and captured copies.
The first script copy must exist before capture. No generated overwrite mode.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'work/f460-f461-comparison').is_dir())
BASE = Path('work/f460-f461-comparison')
NAMES = ['2026-11-01', '2026-11-01-depth'] + [f'2026-11-01-run{i:02}' for i in range(3, 16)]
TOPICS = [
    'Package and first-pass provenance', 'First selected compiled/source routes',
    'Sleep callable / translation callback dispatch', 'Catalogue reader / field owner',
    'Constructor selection / local translator output', 'Trigger schema / address prefix',
    'Scene receiver / pure identity getter', 'Update manifest / daemon configuration',
    'Condition pointer / platform selector', 'Action polling / contextual address suffix',
    'Provided-receiver control / configuration selection', 'Update record / deferred clock request',
    'Working-profile request / deadline producer gap', 'Numeric condition / module admission',
    'Numeric serialization / module removal request',
]
OUTPUTS = ['CATALOGUE.json', 'CATALOGUE.md', 'INPUTS.json', 'HISTORICAL_REFERENCES.json',
           'SAVED_CHECKS.json', 'VERSION_NAVIGATION.json', 'REPORT.md', 'OUTPUT_MANIFEST.json']


def sha(b):
    return hashlib.sha256(b).hexdigest()


def encode(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + '\n').encode()


def read(path):
    p = ROOT / path
    assert not Path(path).is_absolute() and '..' not in Path(path).parts, path
    assert p.is_file() and not p.is_symlink(), path
    assert ROOT in p.resolve().parents, path
    return p.read_bytes()


def exclusive(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as f:
        f.write(data)


def identity(path, data):
    return {'path': str(path), 'bytes': len(data), 'sha256': sha(data)}


def capture():
    assert not (HERE / 'CAPTURE.json').exists(), 'Capture already exists'
    assert not (HERE / 'source-inputs').exists(), 'Input directory already exists'
    first = HERE / 'first-script/build_navigation_v1.py'
    assert first.read_bytes() == Path(__file__).read_bytes(), 'Freeze exact script first'
    for n in NAMES:
        assert (ROOT / BASE / n / 'EVIDENCE_INDEX.json').is_file(), 'Checkpoint not saved: ' + n
    pins, checkpoints, historical = {}, [], {}

    def pin(path, expected=None, size=None):
        path = str(path)
        b = read(path)
        if expected is not None:
            assert sha(b) == expected, ('Identity mismatch', path)
        if size is not None:
            assert len(b) == size, ('Size mismatch', path)
        obj = identity(path, b)
        obj['copy'] = 'source-inputs/' + obj['sha256'] + '.bin'
        pins[path] = obj
        return obj

    for n, topic in zip(NAMES, TOPICS):
        d = BASE / n
        state_name = 'RESEARCH_STATE.v2.json' if n.endswith('run15') else 'RESEARCH_STATE.json'
        index_name = 'EVIDENCE_INDEX.v2.json' if n.endswith('run15') else 'EVIDENCE_INDEX.json'
        sp, vp, ip = [d / x for x in [state_name, 'IDENTITY_VALIDATION.json', index_name]]
        for p in (sp, vp, ip):
            pin(p)
        state, validation, index = [json.loads(read(p)) for p in (sp, vp, ip)]
        assert validation['status'] == 'PASS', n
        indexmap = {r['path']: r for r in index['files']}
        assert len(indexmap) == len(index['files']), 'Duplicate index paths'

        def indexed(path):
            path = str(path)
            row = indexmap[path]
            return pin(path, row['sha256'], row['bytes'])

        checks = []
        for name in ['SOURCE_CHECKS.json', 'FINAL_CHECKS.json']:
            checks.append(indexed(d / name))
        state_history = []
        if n.endswith('run15'):
            for name in ['RESEARCH_STATE.json', 'EVIDENCE_INDEX.json', 'STATE_CORRECTION.v2.json']:
                state_history.append(indexed(d / name))
        reviews = []
        for name, expected in state['reviews'].items():
            filename = name if name.endswith('.md') else name + '.md'
            obj = indexed(d / 'reviews' / filename)
            assert obj['sha256'] == expected
            reviews.append(obj)
        packets = state.get('packets')
        if packets is None:
            packets = [
                {'product': 'F460', 'root': 'work/f460-firmware/2.0.12/research/2026-11-01/first-pass', 'report': 'REPORT.md'},
                {'product': 'F461', 'root': 'work/f461-firmware/2.0.11/research/2026-11-01', 'report': 'REPORT.v2.md'},
            ]
        packet_rows = []
        for packet in packets:
            pr = Path(packet['root'])
            rp = pr / packet['report']
            report = indexed(rp)
            if 'report_sha256' in packet:
                assert report['sha256'] == packet['report_sha256']
            controls = []
            for path, row in sorted(indexmap.items()):
                p = Path(path)
                if not p.is_relative_to(pr):
                    continue
                rel = p.relative_to(pr)
                top = len(rel.parts) == 1
                special = re.search(r'(HISTORY|REFINEMENT|FAILURE|DB_SCOPE|OUTPUT_MANIFEST)', p.name, re.I)
                if p.name == 'INDEX.json' or (top and (p.name.startswith(('REPORT', 'collect_')) or special)):
                    controls.append(indexed(path))
            packet_rows.append({'reported_packet': packet, 'report': report, 'control_pins': controls})
        for row in validation.get('historical_reference_substitutions', []):
            key = (row['current_reference'], row['sha256'])
            actual = pin(row['retained_prior'], row['sha256'])
            record = historical.setdefault(key, {**row, 'retained_pin': actual, 'saved_in': []})
            assert record['retained_prior'] == row['retained_prior'], 'Ambiguous retained mapping'
            record['saved_in'].append(n)
        # These are identities of saved candidate indexes, not a fresh check of every member.
        candidates = []
        for path in sorted(indexmap):
            p = Path(path)
            if p.is_relative_to(d) and p.name == 'INDEX.json' and ('review-candidate' in path or '/integration/' in path):
                candidates.append(indexed(path))
        checkpoints.append({
            'checkpoint': n, 'topic': topic, 'state': pins[str(sp)], 'validation': pins[str(vp)],
            'evidence_index': pins[str(ip)], 'saved_index_member_count': len(index['files']),
            'checks': checks, 'reviews': reviews, 'packets': packet_rows, 'candidate_index_pins': candidates,
            'state_history': state_history,
        })
    # A read-time capture is made before output generation, with no earlier-time provenance claim.
    captured = {'scope': 'Selected immutable documentary inputs only; no original payloads or old collector execution',
                'generator': identity(str(Path(__file__).relative_to(ROOT)), Path(__file__).read_bytes()),
                'captured_UTC': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'checkpoints': checkpoints, 'historical_mappings': sorted(historical.values(), key=lambda r: (r['current_reference'], r['sha256'])),
                'inputs': sorted(pins.values(), key=lambda r: r['path'])}
    (HERE / 'source-inputs').mkdir()
    for row in captured['inputs']:
        dest = HERE / row['copy']
        if not dest.exists():
            exclusive(dest, read(row['path']))
    exclusive(HERE / 'CAPTURE.json', encode(captured))
    print(json.dumps({'captured_inputs': len(pins), 'checkpoints': len(checkpoints), 'historical_mappings': len(historical)}))


def build():
    capbytes = (HERE / 'CAPTURE.json').read_bytes()
    cap = json.loads(capbytes)
    script = Path(__file__).read_bytes()
    assert sha(script) == cap['generator']['sha256'] and len(script) == cap['generator']['bytes']
    assert (HERE / 'first-script/build_navigation_v1.py').read_bytes() == script
    data = {}
    for row in cap['inputs']:
        b = (HERE / row['copy']).read_bytes()
        assert len(b) == row['bytes'] and sha(b) == row['sha256'], row['copy']
        current = read(row['path'])
        assert current == b, ('Immutable input changed', row['path'])
        data[row['path']] = b
    rows, checks, versions = [], [], []
    for c in cap['checkpoints']:
        s = json.loads(data[c['state']['path']])
        v = json.loads(data[c['validation']['path']])
        reports = []
        for packet in c['packets']:
            r = packet['report']
            lines = data[r['path']].decode().splitlines()
            heading = next((i + 1, x) for i, x in enumerate(lines) if x.startswith('# '))
            va = next(((i + 1, x) for i, x in enumerate(lines) if re.search(r'0x[0-9a-fA-F]{3,}', x)), None)
            reports.append({'product': packet['reported_packet']['product'], 'identity': r,
                            'heading': {'line': heading[0], 'exact_text': heading[1]},
                            'first_VA_line': None if va is None else {'line': va[0], 'exact_text': va[1]}})
            versions.append({'checkpoint': c['checkpoint'], 'reported_packet': packet['reported_packet'],
                             'authoritative_report': r, 'version_history_and_control_pins': packet['control_pins'],
                             'scope': 'Saved report/version identities; collector scripts are read as data, never executed. A report-only refinement does not alter the older collector binding.'})
        rows.append({'checkpoint': c['checkpoint'], 'topic': c['topic'], 'saved_status': s['status'],
                     'saved_UTC': s.get('saved_UTC'), 'saved_scope': s.get('scope'), 'reports': reports,
                     'state': c['state'], 'evidence_index': c['evidence_index'], 'validation': c['validation'],
                     'reviews': c['reviews'], 'saved_index_member_count': c['saved_index_member_count'],
                     'candidate_index_pins': c['candidate_index_pins'], 'state_history': c['state_history']})
        checks.append({'checkpoint': c['checkpoint'], 'validation_identity': c['validation'],
                       'saved_status': v['status'], 'saved_completed_UTC': v.get('completed_UTC'),
                       'saved_scope': v.get('scope'), 'check_identities': c['checks'],
                       'saved_old_MHS_ledger': s.get('old_MHS_saved_totals'),
                       'saved_history_limit': s.get('history', s.get('prior_intermediate_history_limit', s.get('preservation'))),
                       'scope': 'Previously saved checks/status only; none rerun by this catalogue.'})
    assert len(rows) == 15 and sum(len(r['reports']) for r in rows) == 30
    latest = checks[-1]['saved_old_MHS_ledger']
    assert latest['original_code_hook_visits'] == 340 and latest['total_hooks'] == 360
    assert latest['C_primitives'] == 0 and latest['definition_redirects'] == 12 and latest['EXIT'] == 8
    assert 340 + 0 + 12 + 8 == 360 and latest['guard_stops'] == 0
    catalogue = {'scope': 'Navigation and documentary hash verification, not semantic reaudit, replay, coverage percentage or support table',
                 'checkpoints': rows, 'checkpoint_count': len(rows), 'source_report_count': 30,
                 'new_original_native_provider_model_fixture_SQL_or_target_execution': 0}
    inputobj = {'capture': identity(str((HERE / 'CAPTURE.json').relative_to(ROOT)), capbytes),
                'captured_UTC': cap['captured_UTC'], 'inputs': cap['inputs'],
                'policy': 'Every selected current immutable input and its exact pre-generation copy must agree. Historical logical references are resolved only to the explicitly pinned retained path, never to a changed current page.'}
    md = ['# F460/F461 completed-checkpoint navigation', '',
          'These 15 rows locate saved checkpoints and 30 source reports. Row counts are not firmware coverage or capability counts. Report excerpts are exact navigation locators, not newly verified firmware claims.', '',
          '| Checkpoint | Bounded topic | F460 source report | F461 source report |', '|---|---|---|---|']
    for r in rows:
        links = [f"[{x['identity']['path'].split('/')[-1]}]({ROOT / x['identity']['path']}) (line {x['heading']['line']})" for x in r['reports']]
        md.append(f"| {r['checkpoint']} | {r['topic']} | {links[0]} | {links[1]} |")
    md += ['', 'Exact sizes, hashes, headings and first VA-bearing report lines are in CATALOGUE.json. The links use the absolute workspace paths captured for this local dossier.', '',
           'VERSION_NAVIGATION.json retains the authoritative report name separately from canonical collector/first-copy identities. In particular run08 F460 uses report v3 over collector v2; run10 F460 first-candidate/REPORT.md is the v2 report alias; run13 and run15 F461 have report-only v2 refinements over retained v1 collector bindings.', '']
    report = f'''# Final F460/F461 navigation verification

This catalogue freezes **15 completed checkpoints** (baseline, depth, run03–run15), **30 authoritative source-report locators**, and **{len(cap['inputs'])} selected documentary input identities**. It verifies hashes and exact captured bytes. It does not repeat semantic source reviews, run any source collector, parse firmware/database payloads, execute a native helper, or claim a coverage percentage.

The checkpoint state, evidence index, saved identity validation, source checks, final checks and reviews are individually pinned. Saved evidence-index member counts are navigation metadata; this batch does **not** independently verify every indexed member or recursively replay earlier protection checks. Candidate and history index files are byte-pinned, without certifying every member named by those indexes. The catalogue author also authored F461 packets and F460 peer reviews; this identity check is not another independent semantic review of those claims.

Inputs were captured at **{cap['captured_UTC']}**, before catalogue generation. CAPTURE.json records exact source/copy pairs; INPUTS.json pins that capture. Current immutable source bytes and pre-generation copies must both match on --check. Mutable public pages are not fresh direct inputs: **{len(cap['historical_mappings'])} explicit historical mappings** resolve logical reference paths to already retained exact versions. Later page edits do not silently substitute new bytes.

Versions and failures remain documentary evidence. VERSION_NAVIGATION.json pins available report, collector, manifest, refinement/failure/history and first-copy-index identities selected from each saved checkpoint index. No absent draft, failed run, or earlier timestamp is invented. Saved MH202 run18/run21 missing intermediate histories remain unverified. A refined report need not be the report reproduced by an older canonical collector; those identities remain separate. Run10 F460's first-copy REPORT.md alias maps v2, while its root REPORT.md retains v1. Run08 F460's opaque helper return is an X0 value, not an established pointer type. Run15 uses RESEARCH_STATE.v2.json and EVIDENCE_INDEX.v2.json (214 saved members); its original 205-member index/state and STATE_CORRECTION.v2.json remain separately pinned. The correction concerns saved coordination metadata, not source/results or a fresh current-branch assertion. No completed-claim promotion is added here.

All F460/F461 original/native/provider/model/fixture/target execution additions in this verification are **0**. The separate inherited MyHOMEServer1 saved corpus remains **1 corpus, 8 entries, 340 original visits, 0 C primitives, 12 redirects, 8 EXIT, 0 guard stops, 360 hooks**, plus **4 data-relocation setups**. Arithmetic 340+0+12+8=360 is checked as saved metadata, not replayed. Old F454/MH202 ledgers and full Device/source gates remain separate and unchanged.

Reproduce with `python3 -B build_navigation_v1.py --check` from this directory. --check reads only and refuses any byte mismatch. Initial generation is exclusive and refuses existing outputs; source capture and the exact first script copy precede generation. The first-candidate index is computed before opening its own index file, so it does not circularly hash itself.

Read CATALOGUE.md for the short navigation table, CATALOGUE.json for exact report lines/pins, SAVED_CHECKS.json for historical check identities/scope, HISTORICAL_REFERENCES.json for explicit retained-version mappings, and VERSION_NAVIGATION.json for report/collector/history distinctions. These records do not establish installed configuration, natural invocation, successful delivery, elapsed timing, lifetime safety, public protocol support, physical effects, or a complete product implementation.
'''
    out = {'CATALOGUE.json': encode(catalogue), 'CATALOGUE.md': ('\n'.join(md)).encode(),
           'INPUTS.json': encode(inputobj), 'HISTORICAL_REFERENCES.json': encode({'scope': 'Explicit saved mappings; current logical reference bytes are not read as replacement evidence', 'mappings': cap['historical_mappings']}),
           'SAVED_CHECKS.json': encode({'scope': 'Historical saved results only, no rerun', 'checks': checks}),
           'VERSION_NAVIGATION.json': encode({'packets': versions}), 'REPORT.md': report.encode()}
    out['OUTPUT_MANIFEST.json'] = encode({'scope': 'Generated members excluding this manifest itself',
                                         'files': [identity(n, b) for n, b in sorted(out.items())]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--capture', action='store_true')
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    assert not (args.capture and args.check)
    if args.capture:
        capture()
        return
    if not args.check:
        assert not any((HERE / n).exists() for n in OUTPUTS), 'Refusing output overwrite'
        assert not (HERE / 'first-candidate-v1').exists(), 'First candidate already exists'
    out = build()
    if args.check:
        for n, b in out.items():
            assert (HERE / n).read_bytes() == b, ('Output differs', n)
        snapshot = json.loads((HERE / 'first-candidate-v1/INDEX.json').read_text())
        for row in snapshot['files']:
            b = (HERE / 'first-candidate-v1' / row['copy']).read_bytes()
            assert len(b) == row['bytes'] and sha(b) == row['sha256']
        print(json.dumps({'status': 'PASS', 'checkpoints': 15, 'reports': 30, 'outputs': len(out), 'new_firmware_execution': 0}))
        return
    for n, b in out.items():
        exclusive(HERE / n, b)
    first = HERE / 'first-candidate-v1'
    first.mkdir()
    copydata = {**out, 'build_navigation_v1.py': Path(__file__).read_bytes(), 'CAPTURE.json': (HERE / 'CAPTURE.json').read_bytes()}
    index = {'scope': 'Exact first generated bytes; index itself excluded',
             'files': [{'copy': n, 'bytes': len(b), 'sha256': sha(b)} for n, b in sorted(copydata.items())]}
    for n, b in copydata.items():
        exclusive(first / n, b)
    exclusive(first / 'INDEX.json', encode(index))
    print(json.dumps({'status': 'GENERATED', 'checkpoints': 15, 'reports': 30, 'outputs': len(out), 'first_copies': len(copydata)}))


if __name__ == '__main__':
    main()
