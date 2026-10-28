import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class CheckFlashMemoryDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/check-flash-memory-disassembly-summary.json").read_text())
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
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 38)
            self.assertEqual([item["name"] for item in evidence["function"]["calls"]],
                             ["IdentifyFlash", "InitFlashTimer"])
            self.assertEqual(evidence["control_flow"]["instruction_halfwords"], 17)
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/check-flash-memory-disassembly.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])

    def test_source_has_both_flash_paths(self):
        source = (ROOT / "src/check_flash_memory.s").read_text()
        for token in ("CheckForFlashMemory:", "bl IdentifyFlash", "bl InitFlashTimer",
                      "movs r0, #1", "movs r0, #0", "gFlashMemoryPresent"):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()

