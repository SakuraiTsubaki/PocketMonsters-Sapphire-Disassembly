import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class PikachuSpriteSetTests(unittest.TestCase):
    def test_all_releases_have_rendered_assets(self):
        summary = json.loads((ROOT / "analysis/pikachu-sprite-set-summary.json").read_text())
        catalog_path = next((ROOT / "analysis").glob("*-global-release-catalog.json"))
        catalog = json.loads(catalog_path.read_text())
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(summary["origin_reference"], catalog["releases"][0]["id"])
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(evidence["discovery"]["front_to_back_table_delta"], 0x14A0)
            self.assertEqual(evidence["discovery"]["back_to_palette_table_delta"], 0x0DC0)
            self.assertFalse(evidence["raw_rom_bytes_included"])
            for key in ("front", "back"):
                self.assertTrue((ROOT / release[key]).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertTrue((ROOT / release["palette"]).read_bytes().startswith(b"JASC-PAL\n0100\n16\n"))

    def test_manifest_hashes_every_output(self):
        manifest = json.loads((ROOT / "manifests/pikachu-sprite-set.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])


if __name__ == "__main__":
    unittest.main()

