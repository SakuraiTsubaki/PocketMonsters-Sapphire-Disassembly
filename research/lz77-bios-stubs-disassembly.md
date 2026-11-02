# Sapphire LZ77 BIOS stubs disassembly

`sapphire-jp-rev0` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one adjacent `LZ77UnCompVram`/`LZ77UnCompWram` suite. The wrappers preserve r0/r1 as source/destination arguments, invoke BIOS SWI 0x12 and 0x11 respectively, and return through lr. The pinned upstream libagbsyscall source corroborates names and order. Per-release maps retain addresses, decoded behavior, and hashes without publishing ROM bytes.
