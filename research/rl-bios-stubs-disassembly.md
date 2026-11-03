# Sapphire run-length BIOS stubs

sapphire-jp-rev0 is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) verify adjacent RLUnCompVram and RLUnCompWram wrappers at the family-specific SDK positions after LZ77UnCompVram. They invoke BIOS SWI 0x15 and 0x14 with source and destination in r0/r1. Pinned libagbsyscall sources corroborate names and calling conventions. No ROM bytes are published.
