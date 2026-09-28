"""Tests for the final generated-text hygiene publication gate."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HYGIENE = load("ownkb_text_hygiene", ROOT / "knowledge/tools/validate_text_hygiene.py")


class TextHygieneTests(unittest.TestCase):
    def test_known_implementation_leaks_are_rejected(self):
        bad = {
            "python AST repr": "{'text': 'Scope', 'inline': [{'type': 'text', 'text': 'Scope'}]}",
            "JSON AST repr": '{"text":"Scope","inline":[{"type":"text","text":"Scope"}]}',
            "JavaScript coercion": "value=[object Object]",
            "Python object repr": "<parser.Token object at 0x7FABC123>",
            "traceback": 'Traceback (most recent call last):\n  File "/tmp/tool.py", line 7, in run',
            "workspace path": "loaded from /workspace/projects/example/input.json",
            "temporary build path": "wrote /tmp/ownkb-check-ab12/first/knowledge/manifest.json",
        }
        for name, value in bad.items():
            with self.subTest(name=name):
                self.assertTrue(HYGIENE.text_violation_labels(value))

    def test_legitimate_protocol_and_code_shaped_text_is_accepted(self):
        safe = (
            "*#1*0##",
            "*1*1*11##",
            '{"WHO":1,"WHAT":0,"WHERE":"11"}',
            "{'WHO': 1, 'WHAT': 0, 'WHERE': 11}",
            "SELECT ObjectId, Val FROM Objects WHERE ObjectId = 406;",
            "736F70653E and 0x7F are public protocol-shaped examples.",
            "Use /etc/hosts only as an illustrative operating-system path.",
            "[label](https://example.invalid/) and inline-code notation remain ordinary Markdown.",
        )
        for value in safe:
            with self.subTest(value=value):
                self.assertEqual([], HYGIENE.text_violation_labels(value))

    def test_jsonl_diagnostic_identifies_record_and_field(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "claims.jsonl"
            path.write_text(
                json.dumps({
                    "id": "ownkb:claim:c999999",
                    "statement": "bad [object Object] text",
                    "context": {"description": "safe"},
                }) + "\n",
                encoding="utf-8",
            )
            violations = HYGIENE.scan_artifact(path, "knowledge/claims/claims.jsonl")
        self.assertEqual(1, len(violations))
        self.assertIn("record=ownkb:claim:c999999", violations[0])
        self.assertIn("$.statement", violations[0])

    def test_current_public_generated_surfaces_are_clean(self):
        manifest = json.loads((ROOT / "knowledge/manifest.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(HYGIENE.validate_generated_text(ROOT, manifest), 12)


if __name__ == "__main__":
    unittest.main()
