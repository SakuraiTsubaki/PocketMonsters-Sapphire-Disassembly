import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/affine-copy-bios-stubs-disassembly-summary.json").read_text());self.assertEqual(s["release_count"],12);self.assertEqual(s["functions"],["BgAffineSet","CpuFastSet","ObjAffineSet"])
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());self.assertTrue(e["verified_layout"]["all_signatures_globally_unique"]);self.assertEqual(e["functions"]["BgAffineSet"]["software_interrupt"],0x0E);self.assertEqual(e["functions"]["CpuFastSet"]["software_interrupt"],0x0C);self.assertEqual(e["functions"]["ObjAffineSet"]["software_interrupt"],0x0F);self.assertTrue(all(v["signature_match_count"]==1 for v in e["functions"].values()));self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/affine-copy-bios-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
