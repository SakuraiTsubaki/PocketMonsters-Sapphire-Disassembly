import hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_catalog(self):
  s=json.loads((R/'analysis/repeated-callback-cfg-summary.json').read_text());c=json.loads(next((R/'analysis').glob('*-global-release-catalog.json')).read_text());self.assertEqual((s['axis'],s['release_count'],sum(x['origin_reference'] for x in s['releases'])),('Disassembly',len(c['releases']),1))
  for x in s['releases']:
   e=json.loads((R/x['evidence']).read_text());self.assertEqual((e['discovery']['repeated_direct_call_count'],e['control_flow']['return_count'],e['control_flow']['raw_halfwords_omitted']),(3,1,True));self.assertNotIn('instructions',e)
 def test_manifest(self):
  m=json.loads((R/'manifests/repeated-callback-cfg.json').read_text())
  for x in m['outputs']:self.assertEqual(hashlib.sha256((R/x['path']).read_bytes()).hexdigest(),x['sha256'])
if __name__=='__main__':unittest.main()
