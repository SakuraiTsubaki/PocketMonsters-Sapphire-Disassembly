from __future__ import annotations
import hashlib,json,re,struct,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RomBootstrapTests(unittest.TestCase):
 def test_source_matches_instruction_bytes(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-rev0-bootstrap.json").read_text());s=(ROOT/"src"/"rom_bootstrap.s").read_text();words=[int(v,16) for v in re.findall(r"\.word 0x([0-9a-f]+)",s)];raw=b"".join(struct.pack("<I",v) for v in words);self.assertEqual(len(words),12);self.assertEqual(hashlib.sha256(raw).hexdigest(),r["instruction_bytes_sha256"]);self.assertEqual([struct.pack("<I",v).hex() for v in words],[i["bytes_le"] for i in r["instructions"]])
 def test_thumb_transition(self):
  t=json.loads((ROOT/"analysis"/"sapphire-jp-rev0-bootstrap.json").read_text())["transition"];self.assertEqual((t["instruction_address"],t["literal_address"],t["raw_target"],t["target_address"],t["target_state"]),(0x080000FC,0x08000244,0x0800024D,0x0800024C,"thumb"))
 def test_manifest_hashes(self):
  m=json.loads((ROOT/"manifests"/"bootstrap.json").read_text());self.assertTrue(all(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest()==o["sha256"] for o in m["outputs"]))
if __name__=="__main__":unittest.main()
