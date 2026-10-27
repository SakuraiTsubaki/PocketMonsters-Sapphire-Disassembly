import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.summary = json.loads(
            (ROOT / "analysis/entry-bootstrap-disassembly-summary.json").read_text()
        )

    def test_all_bootstraps_enter_thumb_without_raw_words(self):
        for release in self.summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]["bootstrap"]).read_text())
            cfg = json.loads((ROOT / release["evidence"]["thumb_cfg"]).read_text())
            with self.subTest(release=release["id"]):
                self.assertEqual(evidence["transition"]["target_state"], "thumb")
                self.assertEqual(
                    evidence["transition"]["target_address"],
                    cfg["function"]["address"],
                )
                self.assertFalse(
                    evidence["bootstrap"]["rom_code_range"]["raw_bytes_published"]
                )
                text = json.dumps(evidence).lower()
                for forbidden in ('"instructions"', '"word":', "bytes_le", "raw_target"):
                    self.assertNotIn(forbidden, text)

    def test_source_and_manifest(self):
        source = (ROOT / "src/rom_bootstrap.s").read_text()
        self.assertIn("bx r1", source)
        self.assertNotIn(".word", source)
        manifest = json.loads((ROOT / "manifests/bootstrap.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()
