import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]
EXPECTED_FORM = "rs-base"
EXPECTED_LENGTH = 22
EXPECTED_POINTERS = []


class InitMainCallbacksDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/init-main-callbacks-disassembly-summary.json").read_text())
        catalogs = list((ROOT / "analysis").glob("*-global-release-catalog.json"))
        self.assertEqual(len(catalogs), 1)
        catalog = json.loads(catalogs[0].read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["origin_reference"], catalog["releases"][0]["id"])
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], EXPECTED_LENGTH)
            self.assertEqual(evidence["function"]["calls"][0]["name"], "SetMainCallback2")
            self.assertEqual(evidence["verified_behavior"]["instruction_form"], EXPECTED_FORM)
            self.assertEqual(evidence["verified_behavior"]["initialized_pointers"], EXPECTED_POINTERS)
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/init-main-callbacks-disassembly.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])

    def test_source_preserves_callback_initialization(self):
        source = (ROOT / "src/init_main_callbacks.s").read_text()
        for token in ("InitMainCallbacks:", "gMain", "Copyright", "bl SetMainCallback2"):
            self.assertIn(token, source)
        for token in EXPECTED_POINTERS:
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()

