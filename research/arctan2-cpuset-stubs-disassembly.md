# Sapphire ArcTan2 and CpuSet BIOS stubs

sapphire-jp-rev0 is the Japanese origin reference. All 12 releases (Japanese, English, German, French, Italian, Spanish) verify ArcTan2 SWI 0x0A and CpuSet SWI 0x0B at SDK-layout offsets from the LZ77 VRAM wrapper. CpuSet has duplicate byte signatures in 0 build(s), so the selected function is the sole candidate at the verified -4/-8 layout position. Pinned libagbsyscall sources corroborate symbols and calling conventions. No ROM bytes are published.
