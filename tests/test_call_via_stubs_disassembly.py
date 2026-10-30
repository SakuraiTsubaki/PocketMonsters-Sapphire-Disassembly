import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/call-via-stubs-summary.json").read_text());self.assertEqual(s["release_count"],12);self.assertEqual(s["function_count"],15)
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());self.assertEqual(e["verified_layout"]["function_count"],15);self.assertTrue(e["verified_layout"]["word_aligned"]);self.assertEqual(e["verified_layout"]["vblank_end_to_suite_delta"],2);self.assertGreaterEqual(e["verified_layout"]["suite_signature_match_count"],1);self.assertTrue(e["verified_layout"]["selected_by_verified_adjacency"]);self.assertEqual(e["functions"]["_call_via_r0"]["branch_exchange_register"],"r0");self.assertEqual(e["functions"]["_call_via_lr"]["branch_exchange_register"],"lr");self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/call-via-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
