import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
EXPECTED_PROFILE = "rs"
EXPECTED_STORAGE = "direct"
EXPECTED_LENGTHS = [22, 26, 8, 84, 22]


class PlayTimeCounterDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_cluster(self):
        summary = json.loads((ROOT / "analysis/play-time-counter-disassembly-summary.json").read_text())
        catalog = json.loads(next((ROOT / "analysis").glob("*-global-release-catalog.json")).read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["profile"], EXPECTED_PROFILE)
        self.assertEqual(summary["storage_profile"], EXPECTED_STORAGE)
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual([item["rom_code_range"]["length"]
                              for item in evidence["functions"]], EXPECTED_LENGTHS)
            self.assertEqual(evidence["verified_behavior"]["thresholds"]["maximum_hours"], 999)
            self.assertTrue(all(item["control_flow"]["raw_halfwords_omitted"]
                                for item in evidence["functions"]))
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_and_source(self):
        manifest = json.loads((ROOT / "manifests/play-time-counter-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        source = (ROOT / "src/play_time_counter.s").read_text()
        for token in ("PlayTimeCounter_Reset:", "PlayTimeCounter_Update:", "gSaveBlock2"):
            self.assertIn(token, source)
        self.assertNotIn(".hword", source)


if __name__ == "__main__":
    unittest.main()
