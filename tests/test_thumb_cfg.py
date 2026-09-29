from __future__ import annotations
import hashlib,json,re,struct,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ThumbCfgTests(unittest.TestCase):
 def test_reachable_source_bytes(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-rev0-thumb-cfg.json").read_text());s=(ROOT/"src"/"thumb_entry_reachable.s").read_text();values=[int(v,16) for v in re.findall(r"\.hword 0x([0-9a-f]+)",s)];raw=b"".join(struct.pack("<H",v) for v in values);self.assertEqual((len(values),len(r["edges"]),len(r["calls"])),(107,18,21));self.assertEqual(hashlib.sha256(raw).hexdigest(),r["canonical_instruction_bytes_sha256"]);self.assertEqual([struct.pack("<H",v).hex() for v in values],[i["bytes_le"] for i in r["instructions"]]);self.assertFalse(r["return_observed"])
 def test_manifest_hashes(self):
  m=json.loads((ROOT/"manifests"/"thumb-cfg.json").read_text());self.assertTrue(all(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest()==o["sha256"] for o in m["outputs"]))
if __name__=="__main__":unittest.main()

