import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1];PROFILE,MODE,LENGTH="rs","bios-call",22
class Tests(unittest.TestCase):
 def test_matrix(self):
  s=json.loads((ROOT/"analysis/wait-for-vblank-disassembly-summary.json").read_text());c=json.loads(next((ROOT/"analysis").glob("*-global-release-catalog.json")).read_text());self.assertEqual((s["axis"],s["profile"],s["release_count"]),("Disassembly",PROFILE,len(c["releases"])))
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());self.assertEqual((e["wait"]["mode"],e["function"]["rom_code_range"]["length"],e["state"]["intrCheck_offset"]),(MODE,LENGTH,28));self.assertIsNotNone(e["wait"]["call"])
 def test_manifest(self):
  for x in json.loads((ROOT/"manifests/wait-for-vblank-disassembly.json").read_text())["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
