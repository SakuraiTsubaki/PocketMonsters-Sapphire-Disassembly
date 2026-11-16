import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
EXPECTED_PROFILE = "rs"


class ClearPokemonCrySongsDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_behavior(self):
        summary = json.loads((ROOT / "analysis/clear-pokemon-cry-songs-disassembly-summary.json").read_text())
        catalog = json.loads(next((ROOT / "analysis").glob("*-global-release-catalog.json")).read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["profile"], EXPECTED_PROFILE)
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["cleared_byte_count"], 104)
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(evidence["function"]["rom_code_range"]["length"], 26)
            self.assertEqual(evidence["function"]["call"]["name"], "CpuSet")
            self.assertEqual(evidence["verified_behavior"]["halfword_count"], 52)
            self.assertTrue(evidence["control_flow"]["raw_halfwords_omitted"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_and_source(self):
        manifest = json.loads((ROOT / "manifests/clear-pokemon-cry-songs-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        source = (ROOT / "src/clear_pokemon_cry_songs.s").read_text()
        for token in ("ClearPokemonCrySongs:", "gPokemonCrySongs", "bl CpuSet"):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()
