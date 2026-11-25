import hashlib, json, pathlib, unittest
ROOT = pathlib.Path(__file__).parents[1]
PROFILE, LENGTH, CALLS = "rs", 98, 6
class VBlankIntrTests(unittest.TestCase):
    def test_matrix(self):
        summary=json.loads((ROOT/"analysis/vblank-intr-disassembly-summary.json").read_text()); catalog=json.loads(next((ROOT/"analysis").glob("*-global-release-catalog.json")).read_text())
        self.assertEqual((summary["axis"],summary["profile"],summary["release_count"]),("Disassembly",PROFILE,len(catalog["releases"])))
        for release in summary["releases"]:
            evidence=json.loads((ROOT/release["evidence"]).read_text()); self.assertEqual(evidence["function"]["rom_code_range"]["length"],LENGTH); self.assertEqual(len(evidence["calls"]),CALLS); self.assertFalse(evidence["raw_rom_bytes_included"])
    def test_manifest(self):
        manifest=json.loads((ROOT/"manifests/vblank-intr-disassembly.json").read_text())
        for item in manifest["outputs"]: self.assertEqual(hashlib.sha256((ROOT/item["path"]).read_bytes()).hexdigest(),item["sha256"])
if __name__ == "__main__": unittest.main()
