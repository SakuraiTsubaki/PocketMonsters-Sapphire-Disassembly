from __future__ import annotations
import csv,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ReleaseReportTests(unittest.TestCase):
 def test_release_evidence_is_synchronized(self):
  p={x["id"]:x for x in json.loads((ROOT/"project.json").read_text(encoding="utf-8"))["releases"]}; r={x["id"]:x for x in json.loads((ROOT/"analysis"/"sapphire-release-header-report.json").read_text(encoding="utf-8"))["releases"]}
  with (ROOT/"research"/"releases.csv").open(newline="",encoding="utf-8") as s:c={x["id"]:x for x in csv.DictReader(s)}
  self.assertEqual(set(p),set(r));self.assertEqual(set(p),set(c));self.assertEqual(len(p),4)
  for i,x in p.items():self.assertEqual(x["status"],"candidate");self.assertEqual(x["sha256"],r[i]["sha256"]);self.assertEqual(x["sha256"],c[i]["sha256"]);self.assertTrue(all(r[i]["validation"].values()))
 def test_region_codes_revisions_and_observed_sizes(self):
  rs=json.loads((ROOT/"analysis"/"sapphire-release-header-report.json").read_text(encoding="utf-8"))["releases"];jp=next(x for x in rs if x["id"]=="sapphire-jp-rev0");west=sorted((x for x in rs if x["id"].startswith("sapphire-en-")),key=lambda x:x["header"]["software_version"])
  self.assertEqual((jp["header"]["game_code"],jp["size"]),("AXPJ",8388608));self.assertEqual([x["header"]["software_version"] for x in west],[0,1,2]);self.assertTrue(all(x["header"]["game_code"]=="AXPE" and x["size"]==16777216 for x in west))
if __name__=="__main__":unittest.main()
