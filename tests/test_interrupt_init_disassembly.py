import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
EXPECTED_PROFILE = "rs"
EXPECTED_INIT_LENGTH = 84
EXPECTED_FUNCTIONS = 5


class InterruptInitDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_suite(self):
        summary = json.loads((ROOT / "analysis/interrupt-init-disassembly-summary.json").read_text())
        catalog = json.loads(next((ROOT / "analysis").glob("*-global-release-catalog.json")).read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["profile"], EXPECTED_PROFILE)
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(len(evidence["functions"]), EXPECTED_FUNCTIONS)
            self.assertEqual(evidence["functions"][0]["rom_code_range"]["length"],
                             EXPECTED_INIT_LENGTH)
            self.assertEqual(evidence["dma"], {"channel": 3, "byte_count": 2048,
                                               "control": "0x84000200"})
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_and_source(self):
        manifest = json.loads((ROOT / "manifests/interrupt-init-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        source = (ROOT / "src/interrupt_init.s").read_text()
        for token in ("InitIntrHandlers:", "SetVBlankCallback:", "0x04000200"):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()
