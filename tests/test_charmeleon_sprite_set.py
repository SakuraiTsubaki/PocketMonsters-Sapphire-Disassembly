import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_assets(self):
  s=json.loads((ROOT/"analysis/charmeleon-sprite-set-summary.json").read_text());self.assertEqual(s["release_count"],12);self.assertEqual(s["species"],{"id":5,"name":"charmeleon"})
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());self.assertEqual(e["target"]["sha256"],r["sha256"]);self.assertFalse(e["raw_rom_bytes_included"])
   for key in("front","back"):self.assertTrue((ROOT/r[key]).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
   self.assertTrue((ROOT/r["palette"]).read_bytes().startswith(b"JASC-PAL\n0100\n16\n"))
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/charmeleon-sprite-set.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()

