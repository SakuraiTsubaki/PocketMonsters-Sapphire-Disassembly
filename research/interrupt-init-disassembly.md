# Pokemon Sapphire interrupt initialization disassembly

`axp-j-rev0-retail` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain one InitIntrHandlers suite matching the `rs` profile. VBlank uses direct IE and DISPSTAT writes. The routine copies 14 table entries, DMA-copies the 0x800-byte dispatcher with DMA3 control 0x84000200, installs the IWRAM vector, clears callbacks and enables VBlank. Evidence omits ROM bytes and instruction halfwords.
