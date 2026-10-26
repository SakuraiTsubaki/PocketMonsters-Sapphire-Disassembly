import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]


class SeedRngWithRtcDisassemblyTests(unittest.TestCase):
    def test_all_catalog_releases(self):
        catalog_name = next((ROOT / "analysis").glob("*-global-release-catalog.json"))
        catalog = json.loads(catalog_name.read_text(encoding="utf-8"))
        summary = json.loads((ROOT / "analysis/seed-rng-with-rtc-disassembly-summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["axis"], "disassembly")
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        for release in catalog["releases"]:
            release_id = release["id"]
            mapping = json.loads((ROOT / f"analysis/{release_id}-seed-rng-with-rtc-map.json").read_text(encoding="utf-8"))
            cfg = json.loads((ROOT / f"analysis/{release_id}-seed-rng-with-rtc-cfg.json").read_text(encoding="utf-8"))
            self.assertEqual(mapping["axis"], "disassembly")
            self.assertEqual(mapping["target"]["sha256"], release["sha256"])
            self.assertEqual([call["name"] for call in mapping["calls"]], ["RtcGetMinuteCount", "SeedRng"])
            self.assertEqual(mapping["function"]["rom_code_range"]["length"], 24)
            self.assertEqual(mapping["literal_pool"]["value"], "0x0000FFFF")
            self.assertNotIn("halfword", cfg["instructions"][0])
            self.assertFalse(mapping["raw_rom_bytes_included"])

    def test_source_and_manifest(self):
        source = (ROOT / "src/seed_rng_with_rtc.s").read_text(encoding="utf-8")
        self.assertIn(".thumb_func", source)
        self.assertIn(".LSeedMask", source)
        manifest = json.loads((ROOT / "manifests/seed-rng-with-rtc-disassembly.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["axis"], "disassembly")
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()

