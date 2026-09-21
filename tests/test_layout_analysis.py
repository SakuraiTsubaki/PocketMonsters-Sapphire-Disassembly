from __future__ import annotations
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class LayoutAnalysisTests(unittest.TestCase):
 def test_origin_layout_is_complete_and_conservative(self):
  r=json.loads((ROOT/"analysis"/"sapphire-jp-rev0-layout.json").read_text(encoding="utf-8"));self.assertEqual(r["sha256"],"6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9");self.assertEqual(r["region_count"],8);self.assertEqual(r["regions"][0]["classification"],"header-and-entry");self.assertTrue(all(x["classification"]=="unclassified" for x in r["regions"][1:]));self.assertTrue(all(x["rom_pointer_words"]>=x["thumb_pointer_words"] for x in r["regions"]))
 def test_manifest_hashes_output(self):
  m=json.loads((ROOT/"analysis"/"sapphire-jp-rev0-layout-manifest.json").read_text(encoding="utf-8"));o=m["outputs"][0];self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()
