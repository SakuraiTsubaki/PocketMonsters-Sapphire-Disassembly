import hashlib,json,struct,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1];COUNT=12;RAW='08a0153cfd6b0ea54b938f7d209933fa849da0d56f5a34c481060c9ff2fad818'
class T(unittest.TestCase):
 def test_catalog(self):
  s=json.loads((ROOT/'analysis/header-logo-catalog-summary.json').read_text());self.assertEqual((s['release_count'],s['source_sha256'],sum(x['origin_reference'] for x in s['releases'])),(COUNT,RAW,1));self.assertEqual(struct.unpack('>II',(ROOT/s['png']).read_bytes()[16:24]),(416,64))
  for x in s['releases']:
   r=json.loads((ROOT/x['evidence']).read_text());self.assertEqual((r['target']['sha256'],r['asset']['source_sha256']),(x['sha256'],RAW));self.assertFalse(r['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/header-logo-catalog.json').read_text());[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
