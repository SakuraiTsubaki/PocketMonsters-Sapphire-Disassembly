import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
EXPECTED_PROFILE = "rs"
EXPECTED_ACCESS = "direct"
EXPECTED_READ_LENGTH = 148


class KeyInputDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_evidence(self):
        summary = json.loads((ROOT / "analysis/key-input-disassembly-summary.json").read_text())
        catalog = json.loads(next((ROOT / "analysis").glob("*-global-release-catalog.json")).read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["family_profile"], EXPECTED_PROFILE)
        self.assertEqual(summary["save_options_access"], EXPECTED_ACCESS)
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["origin_reference"], catalog["releases"][0]["id"])
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(evidence["functions"][0]["rom_code_range"]["length"], 28)
            self.assertEqual(evidence["functions"][1]["rom_code_range"]["length"],
                             EXPECTED_READ_LENGTH)
            self.assertEqual(evidence["verified_layout"]["init_to_read_delta"], 40)
            self.assertFalse(evidence["raw_rom_bytes_included"])
            self.assertTrue(all(item["control_flow"]["raw_halfwords_omitted"]
                                for item in evidence["functions"]))

    def test_manifest_and_semantic_source(self):
        manifest = json.loads((ROOT / "manifests/key-input-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        source = (ROOT / "src/key_input.s").read_text()
        for token in ("InitKeys:", "ReadKeys:", "gSaveBlock2", "0x04000130"):
            self.assertIn(token, source)
        self.assertNotIn(".hword", source)


if __name__ == "__main__":
    unittest.main()
