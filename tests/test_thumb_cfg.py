import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class ThumbCfgTests(unittest.TestCase):
    def setUp(self):
        self.summary = json.loads(
            (ROOT / "analysis/entry-bootstrap-disassembly-summary.json").read_text()
        )

    def test_compact_cfgs_are_nonreturning_and_raw_free(self):
        for release in self.summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]["thumb_cfg"]).read_text())
            with self.subTest(release=release["id"]):
                self.assertTrue(evidence["function"]["nonreturning"])
                self.assertEqual(evidence["control_flow"]["return_count"], 0)
                edge = evidence["control_flow"]["loop_back_edge"]
                self.assertLess(int(edge["target"], 16), int(edge["source"], 16))
                self.assertFalse(
                    evidence["function"]["rom_code_range"]["raw_bytes_published"]
                )
                text = json.dumps(evidence).lower()
                for forbidden in ('"instructions"', '"halfword":', "bytes_le", "raw_hex"):
                    self.assertNotIn(forbidden, text)

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/thumb-cfg.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()
