from __future__ import annotations
import hashlib,json,re,struct,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RomEntryTests(unittest.TestCase):
 def test_entry_disassembly_and_source(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-rev0-entrypoint.json").read_text());s=(ROOT/"src"/"rom_entry.s").read_text();word=int(re.search(r"\.word 0x([0-9a-f]+)",s).group(1),16);self.assertEqual((r["instruction_word"],r["instruction_bytes_le"],r["target_address"]),(0xEA000032,"320000ea",0x080000D0));self.assertEqual(struct.pack("<I",word).hex(),r["instruction_bytes_le"]);self.assertTrue(r["round_trip_verified"])
 def test_manifest_hashes(self):
  m=json.loads((ROOT/"manifests"/"entrypoint.json").read_text());self.assertTrue(all(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest()==o["sha256"] for o in m["outputs"]))
if __name__=="__main__":unittest.main()
