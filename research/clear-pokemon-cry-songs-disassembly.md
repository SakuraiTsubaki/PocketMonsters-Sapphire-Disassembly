# Pokemon Sapphire ClearPokemonCrySongs disassembly

`axp-j-rev0-retail` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one 26-byte Thumb function. It places a zero halfword on the stack and calls CpuSet in source-fixed mode to clear 52 halfwords (104 bytes) at the release-specific gPokemonCrySongs IWRAM address. Maps preserve ranges, hashes, destinations, call targets and raw-free CFG evidence.
