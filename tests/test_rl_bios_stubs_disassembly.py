import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/rl-bios-stubs-disassembly-summary.json").read_text());self.assertEqual(s["release_count"],12);self.assertEqual(s["functions"],["RLUnCompVram","RLUnCompWram"])
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());v=e["functions"]["RLUnCompVram"];w=e["functions"]["RLUnCompWram"];self.assertEqual(v["software_interrupt"],0x15);self.assertEqual(w["software_interrupt"],0x14);self.assertEqual(w["rom_offset"]-v["rom_offset"],4);self.assertTrue(v["selected_by_verified_sdk_layout"]);self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/rl-bios-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
