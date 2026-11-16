import hashlib
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
EXPECTED_PROFILE = "rs"
EXPECTED_VCOUNT_LENGTH = 38
EXPECTED_VCOUNT_CALLS = ["indirect vcount callback trampoline"]


class DisplaySerialInterruptDisassemblyTests(unittest.TestCase):
    def test_release_matrix_and_handlers(self):
        summary = json.loads((ROOT / "analysis/display-serial-interrupt-disassembly-summary.json").read_text())
        catalog = json.loads(next((ROOT / "analysis").glob("*-global-release-catalog.json")).read_text())
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["profile"], EXPECTED_PROFILE)
        self.assertEqual(summary["release_count"], len(catalog["releases"]))
        self.assertEqual(catalog["releases"][0]["language"], "Japanese")
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual([item["name"] for item in evidence["functions"]],
                             ["HBlankIntr", "VCountIntr", "SerialIntr"])
            vcount = evidence["functions"][1]
            self.assertEqual(vcount["rom_code_range"]["length"], EXPECTED_VCOUNT_LENGTH)
            self.assertEqual([call["name"] for call in vcount["calls"]], EXPECTED_VCOUNT_CALLS)
            self.assertTrue(all(item["control_flow"]["raw_halfwords_omitted"]
                                for item in evidence["functions"]))
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_and_source(self):
        manifest = json.loads((ROOT / "manifests/display-serial-interrupt-disassembly.json").read_text())
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])
        source = (ROOT / "src/display_serial_interrupts.s").read_text()
        for token in ("HBlankIntr:", "VCountIntr:", "SerialIntr:", "0x03007FF8"):
            self.assertIn(token, source)
        self.assertNotIn(".hword", source)


if __name__ == "__main__":
    unittest.main()
