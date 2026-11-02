import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/lz77-bios-stubs-disassembly-summary.json").read_text());self.assertEqual(s["release_count"],12);self.assertEqual(s["functions"],["LZ77UnCompVram","LZ77UnCompWram"])
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());v=e["verified_layout"];self.assertTrue(v["adjacent"]);self.assertEqual(v["suite_length"],8);self.assertEqual(v["vram_to_wram_delta"],4);self.assertEqual(v["suite_signature_match_count"],1);self.assertEqual(e["functions"]["LZ77UnCompVram"]["software_interrupt"],0x12);self.assertEqual(e["functions"]["LZ77UnCompWram"]["software_interrupt"],0x11);self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/lz77-bios-stubs-disassembly.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
