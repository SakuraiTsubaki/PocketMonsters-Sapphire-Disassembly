import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/sqrt-vblank-stubs-summary.json").read_text());self.assertEqual(s["release_count"],12)
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());self.assertTrue(e["verified_layout"]["adjacent"]);self.assertEqual(e["verified_layout"]["reset_suite_to_sqrt_delta"],28);self.assertEqual(e["functions"]["Sqrt"]["software_interrupt"],8);self.assertEqual(e["functions"]["VBlankIntrWait"]["software_interrupt"],5);self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/sqrt-vblank-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
