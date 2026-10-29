import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class InitMapMusicDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_maps(self):
        summary = json.loads((ROOT / "analysis/init-map-music-disassembly-summary.json").read_text())
        catalogs = list((ROOT / "analysis").glob("*-global-release-catalog.json"))
        self.assertEqual(len(catalogs), 1)
        catalog = json.loads(catalogs[0].read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["origin_reference"], catalog["releases"][0]["id"])
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            behavior = evidence["verified_behavior"]
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 16)
            self.assertEqual(evidence["function"]["calls"][0]["name"], "ResetMapMusic")
            self.assertEqual(behavior["instruction_form"], "clear-iwram-byte-then-call")
            self.assertTrue(behavior["gDisableMusic_address"].startswith("0x030"))
            self.assertEqual(behavior["gDisableMusic_value"], 0)
            self.assertEqual(behavior["reset_map_music_relative_offset"], 0x10C)
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/init-map-music-disassembly.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            actual = hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest()
            self.assertEqual(actual, output["sha256"])

    def test_source_preserves_map_music_initialization(self):
        source = (ROOT / "src/init_map_music.s").read_text()
        for token in ("InitMapMusic:", "gDisableMusic", "movs r0, #0",
                      "strb r0, [r1]", "bl ResetMapMusic"):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()

