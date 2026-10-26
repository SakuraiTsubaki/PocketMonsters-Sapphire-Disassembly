import hashlib
import json
import math
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
COUNT = 1


class PaletteSwatchTests(unittest.TestCase):
    def test_catalog_and_pngs(self):
        catalog = json.loads((ROOT / "analysis/palette-swatch-catalog.json").read_text())
        self.assertEqual((catalog["palette_count"], len(catalog["palettes"])), (COUNT, COUNT))
        self.assertGreaterEqual(sum(item["origin_reference"] for item in catalog["palettes"]), 1)
        for item in catalog["palettes"]:
            source = ROOT / item["source"]
            png = (ROOT / item["png"]).read_bytes()
            evidence = json.loads((ROOT / item["evidence"]).read_text())
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), item["source_sha256"])
            self.assertEqual(hashlib.sha256(png).hexdigest(), item["png_sha256"])
            self.assertEqual(struct.unpack(">II", png[16:24]), (min(16, item["color_count"]) * 16, math.ceil(item["color_count"] / 16) * 16))
            self.assertTrue(evidence["source"]["provenance_manifests"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest(self):
        manifest = json.loads((ROOT / "manifests/palette-swatches.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()
