import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_cfg(self):
  c=json.loads((ROOT/'analysis/sapphire-jp-repeated-callback-cfg.json').read_text());self.assertEqual((c['start_address'],c['instruction_halfwords'],len(c['calls']),c['return_observed']),(0x08000348,78,7,True));self.assertTrue(all('halfword' not in i and 'bytes_le' not in i for i in c['instructions']))
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/repeated-callback-cfg.json').read_text());self.assertEqual(hashlib.sha256((ROOT/m['output']['path']).read_bytes()).hexdigest(),m['output']['sha256'])
if __name__=='__main__':unittest.main()
