import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class AgbMainDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_structural_profiles(self):
        summary = json.loads((ROOT / "analysis/agb-main-disassembly-summary.json").read_text())
        catalog = json.loads(next((ROOT / "analysis").glob("*-global-release-catalog.json")).read_text())
        profile = json.loads((ROOT / "analysis/agb-main-disassembly-profile.json").read_text())
        variants = {item["id"]: item for item in profile["variants"]}
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            variant = variants[release["profile_variant"]]
            self.assertEqual(evidence["axis"], "Disassembly")
            self.assertEqual(evidence["entry_chain"]["thumb_transition_target"],
                             evidence["function"]["address"])
            self.assertFalse(evidence["control_flow"]["return_observed"])
            self.assertEqual(len(evidence["direct_calls"]),
                             variant["signature"]["call_count"])
            self.assertLess(evidence["function"]["loop_back_edge"]["target"],
                            evidence["function"]["loop_back_edge"]["source"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_and_source(self):
        manifest = json.loads((ROOT / "manifests/agb-main-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        source = (ROOT / "src/agb_main.s").read_text()
        self.assertIn("AgbMain:", source)
        self.assertNotIn(".hword", source)


if __name__ == "__main__":
    unittest.main()

