import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_all_official_languages_match(self):
  m=json.loads((ROOT/'manifests/title-kyogre-global.json').read_text());self.assertEqual(m['languages'],['ja','en','de','fr','it','es']);self.assertFalse(m['official_korean_release_available'])
  for lang in m['languages']:
   file_lang='jp' if lang=='ja' else lang;r=json.loads((ROOT/f'analysis/sapphire-{file_lang}-rev0-title-kyogre.json').read_text());self.assertEqual(r['decompressed_sha256'],m['decoded_sha256']);self.assertEqual(r['compressed_sha256'],m['compressed_sha256']);self.assertEqual(r['png_sha256'],m['png_sha256']);self.assertFalse(r['raw_rom_bytes_included'])
 def test_outputs_are_hash_locked(self):
  m=json.loads((ROOT/'manifests/title-kyogre-global.json').read_text())
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()

