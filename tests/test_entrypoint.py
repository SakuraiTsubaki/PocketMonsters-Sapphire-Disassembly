import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class EntrypointTests(unittest.TestCase):
    def setUp(self):
        self.summary = json.loads(
            (ROOT / "analysis/entry-bootstrap-disassembly-summary.json").read_text()
        )

    def test_all_release_entries_round_trip_without_raw_words(self):
        self.assertGreater(self.summary["release_count"], 0)
        self.assertEqual(self.summary["releases"][0]["language"], "Japanese")
        for release in self.summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]["entrypoint"]).read_text())
            with self.subTest(release=release["id"]):
                self.assertEqual(evidence["entry"]["address"], "0x08000000")
                self.assertEqual(evidence["entry"]["state"], "arm")
                self.assertTrue(evidence["entry"]["round_trip_verified"])
                self.assertFalse(evidence["entry"]["rom_code_range"]["raw_bytes_published"])
                text = json.dumps(evidence).lower()
                for forbidden in ("instruction_word", "instruction_bytes", "bytes_le", '"word":'):
                    self.assertNotIn(forbidden, text)

    def test_source_and_manifest(self):
        source = (ROOT / "src/rom_entry.s").read_text()
        self.assertIn("b rom_bootstrap", source)
        self.assertNotIn(".word", source)
        manifest = json.loads((ROOT / "manifests/entrypoint.json").read_text())
        self.assertEqual(manifest["release_count"], self.summary["release_count"])
        for output in manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()
