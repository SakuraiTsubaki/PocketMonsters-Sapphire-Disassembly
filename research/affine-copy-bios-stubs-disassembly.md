# Sapphire affine and fast-copy BIOS stubs

sapphire-jp-rev0 is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one BgAffineSet, CpuFastSet, and ObjAffineSet Thumb wrapper. Their SWI 0x0E, 0x0C, and 0x0F encodings are selected by globally unique signatures and verified again at family-specific offsets from the LZ77 VRAM wrapper. Pinned upstream libagbsyscall sources corroborate names and calling conventions. No ROM bytes are published.
