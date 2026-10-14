import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PREFIX = "sapphire"
ASSET = "kyogre"
LABEL = "Kyogre"


class TitleLegendaryLoaderTests(unittest.TestCase):
    def setUp(self):
        self.asset_reports = sorted(
            (ROOT / "analysis").glob(f"{PREFIX}-*-title-{ASSET}.json")
        )
        self.manifest = json.loads(
            (ROOT / "manifests/title-legendary-loaders.json").read_text()
        )
        self.source = (ROOT / "src/title_legendary_loader.asm").read_text()

    def test_every_asset_has_one_runtime_load(self):
        self.assertEqual(len(self.asset_reports), 6)
        for asset_path in self.asset_reports:
            asset = json.loads(asset_path.read_text())
            load_path = asset_path.with_name(asset_path.stem + "-load.json")
            load = json.loads(load_path.read_text())
            self.assertEqual(load["source_sha256"], asset["rom_sha256"])
            self.assertEqual(load["asset"]["source_offset"], asset["source_offset"])
            self.assertEqual(load["asset"]["decompressed_length"], asset["decompressed_length"])
            self.assertEqual(len(load["pointer_locations"]), 1)
            self.assertEqual(len(load["thumb_references"]), 1)
            self.assertFalse(load["raw_bytes_published"])

    def test_loader_targets_title_vram_and_direct_call(self):
        for asset_path in self.asset_reports:
            load = json.loads(
                asset_path.with_name(asset_path.stem + "-load.json").read_text()
            )
            reference = load["thumb_references"][0]
            self.assertEqual(reference["destination_register"], 0)
            self.assertEqual(reference["destination"], 0x06008000)
            self.assertEqual(reference["loader_sequence_length"], 8)
            self.assertGreaterEqual(reference["call_target"], 0x08000000)
            self.assertLess(reference["call_target"], 0x0A000000)

    def test_semantic_source_records_asset_and_destination(self):
        self.assertIn(f"LoadTitleScreen{LABEL}Tiles::", self.source)
        self.assertIn("ldr r1, =$06008000", self.source)
        self.assertIn("bl LZ77UnCompVram", self.source)

    def test_manifest_hashes_outputs(self):
        self.assertFalse(self.manifest["raw_rom_bytes_included"])
        for output in self.manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()
