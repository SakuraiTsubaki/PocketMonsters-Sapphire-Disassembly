import hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];COUNT=12;NAMES=['write_word_to_mem','copy_word_to_mem']
class T(unittest.TestCase):
 def test_release_matrix(self):
  s=json.loads((R/'analysis/trainer-id-disassembly-summary.json').read_text());c=json.loads((R/'analysis/sapphire-global-release-catalog.json').read_text());self.assertEqual((s['axis'],s['release_count'],len(c['releases']),s['functions'],sum(x['origin_reference'] for x in s['releases'])),('Disassembly',COUNT,COUNT,NAMES,1))
  for x in s['releases']:
   m=json.loads((R/x['evidence']['map']).read_text());self.assertEqual((m['target']['sha256'],[f['name'] for f in m['functions']]),(x['sha256'],NAMES));self.assertFalse(m['raw_rom_bytes_included'])
   for f,p in zip(m['functions'],x['evidence']['cfgs']):
    cfg=json.loads((R/p).read_text());self.assertEqual((cfg['source_sha256'],len(cfg['returns']),cfg['calls']),(x['sha256'],1,[]));self.assertNotIn('bytes_le',cfg['instructions'][0]);self.assertEqual((cfg['range_start'],cfg['range_end']),(int(f['address'],16),int(f['range_end_exclusive'],16)))
 def test_manifest(self):
  m=json.loads((R/'manifests/trainer-id-disassembly.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
