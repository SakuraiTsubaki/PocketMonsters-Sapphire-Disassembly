# Sapphire reset SDK stubs disassembly

`sapphire-jp-rev0` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one adjacent RegisterRamReset/SoftReset suite. RegisterRamReset invokes SWI 1 and returns. SoftReset disables REG_IME, moves SP to 0x03007F00, invokes SWI 1 with flags in r0, and performs non-returning SWI 0. Per-release maps record decoded operands, layout and hashes without ROM bytes.
