import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
RELEASES = ("en-rev1", "en-rev2", "de-rev1", "fr-rev1", "it-rev1", "es-rev1")


class TitleKyogreRevisionTests(unittest.TestCase):
    def test_all_later_revisions_match_asset_and_loader(self):
        manifest = json.loads((ROOT / "manifests/title-kyogre-revisions.json").read_text())
        self.assertEqual(manifest["releases"], list(RELEASES))
        for release in RELEASES:
            asset = json.loads((ROOT / "analysis" / f"sapphire-{release}-title-kyogre.json").read_text())
            load = json.loads((ROOT / "analysis" / f"sapphire-{release}-title-kyogre-load.json").read_text())
            self.assertEqual(asset["decompressed_sha256"], manifest["decoded_sha256"])
            self.assertEqual(asset["compressed_sha256"], manifest["compressed_sha256"])
            self.assertEqual(asset["png_sha256"], manifest["png_sha256"])
            self.assertEqual(load["source_sha256"], asset["rom_sha256"])
            self.assertEqual(load["asset"]["source_offset"], asset["source_offset"])
            self.assertEqual(len(load["pointer_locations"]), 1)
            self.assertEqual(len(load["thumb_references"]), 1)
            self.assertEqual(load["thumb_references"][0]["destination"], 0x06008000)

    def test_manifest_outputs_are_hash_locked(self):
        manifest = json.loads((ROOT / "manifests/title-kyogre-revisions.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()
