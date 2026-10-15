import csv,hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
ADDR={'sapphire-jp-rev0':(0x0803E130,'0x03004748'),'sapphire-en-rev0':(0x08040E84,'0x03004818'),'sapphire-en-rev1':(0x08040EA4,'0x03004818'),'sapphire-en-rev2':(0x08040EA4,'0x03004818'),'sapphire-de-rev0':(0x080411A8,'0x03004828'),'sapphire-de-rev1':(0x080411A8,'0x03004828'),'sapphire-fr-rev0':(0x08041294,'0x03004828'),'sapphire-fr-rev1':(0x08041294,'0x03004828'),'sapphire-it-rev0':(0x080411BC,'0x03004828'),'sapphire-it-rev1':(0x080411BC,'0x03004828'),'sapphire-es-rev0':(0x080412A4,'0x03004828'),'sapphire-es-rev1':(0x080412A4,'0x03004828')}
class Tests(unittest.TestCase):
 def test_all_releases(self):
  rows={r['id']:r for r in csv.DictReader((ROOT/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(ADDR))
  for release,(address,state) in ADDR.items():
   m=json.loads((ROOT/f'analysis/{release}-rng.json').read_text());self.assertEqual(m['target']['sha256'],rows[release]['sha256']);self.assertEqual((m['variant'],m['functions']['Random']['address'],m['globals']['gRngValue']),('standard',f'0x{address:08X}',state));self.assertEqual(m['functions']['SeedRng']['rom_offset']-m['functions']['Random']['rom_offset'],32);self.assertEqual((m['functions']['Random']['code_sha256'],m['functions']['SeedRng']['code_sha256']),('72526af8af03e60317e6ac115ece4a9415af188772c5432ec1c145e0acaf09fb','77dddf4b6256d28fe54fe4fa7c41a15d549d1d3e086013e03c7919823fda7edb'))
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/rng-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
