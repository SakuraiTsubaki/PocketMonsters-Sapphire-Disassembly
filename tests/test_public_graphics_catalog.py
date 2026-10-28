import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class PublicGraphicsCatalogTests(unittest.TestCase):
    def test_every_graphics_file_is_cataloged_with_provenance(self):
        catalog = json.loads((ROOT / "analysis/public-graphics-catalog.json").read_text())
        expected = sorted(path.relative_to(ROOT).as_posix() for path in (ROOT / "graphics").rglob("*")
                          if path.is_file() and path.suffix.lower() in (".png", ".json", ".pal"))
        actual = sorted(item["path"] for item in catalog["assets"])
        self.assertEqual(actual, expected)
        self.assertEqual(catalog["asset_count"], len(expected))
        self.assertFalse(catalog["raw_rom_bytes_included"])
        for item in catalog["assets"]:
            path = ROOT / item["path"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item["sha256"])
            self.assertTrue(item["provenance"])
            if item["format"] == "PNG":
                self.assertGreater(item["png"]["width"], 0)
                self.assertGreater(item["png"]["height"], 0)
            elif item["format"] == "JASC-PAL":
                self.assertGreater(item["palette"]["color_count"], 0)

    def test_manifest_and_preview(self):
        manifest = json.loads((ROOT / "manifests/public-graphics-catalog.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        preview = (ROOT / "ASSETS.md").read_text()
        self.assertIn("public graphics", preview.lower())
        self.assertIn("<img src=", preview)
        self.assertIn("Palette", preview)


if __name__ == "__main__":
    unittest.main()

