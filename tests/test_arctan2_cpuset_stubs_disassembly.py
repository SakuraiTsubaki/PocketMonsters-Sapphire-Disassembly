import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/arctan2-cpuset-stubs-disassembly-summary.json").read_text());self.assertEqual(s["release_count"],12);self.assertEqual(s["functions"],["ArcTan2","CpuSet"])
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());a=e["functions"]["ArcTan2"];c=e["functions"]["CpuSet"];self.assertEqual(a["software_interrupt"],10);self.assertEqual(c["software_interrupt"],11);self.assertTrue(a["selected_by_verified_sdk_layout"]);self.assertTrue(c["selected_by_verified_sdk_layout"]);self.assertIn(c["lz77_vram_relative_offset"],(-8,-4));self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/arctan2-cpuset-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
