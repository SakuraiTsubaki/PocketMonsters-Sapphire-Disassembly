# Pokemon Sapphire SeedRngWithRtc disassembly

The Japanese release `axp-j-rev0-retail` is the origin reference. Independent ROM scanning found exactly one matching 24-byte Thumb function plus its 0x0000FFFF literal in all 12 cataloged releases (Japanese, English, German, French, Italian, Spanish).

The assembly calls the release-specific RTC minute-count routine, XOR-folds the 32-bit result to 16 bits, then calls the release-specific RNG seeder. CFGs omit raw halfwords; maps retain ranges, hashes, literal location and call targets. Names are corroborated by `pret/pokeruby` at `5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/main.c`.
