# Japanese ROM entry disassembly

The exact-hash Japanese revision 0 ROM begins with little-endian bytes `320000ea`, decoded independently as ARM instruction `b 0x080000d0` at `0x08000000` (word `0xea000032`). The shared Disassembly tool re-encodes the target and requires an exact word match before setting `round_trip_verified`.

`src/rom_entry.s` preserves this first instruction byte-for-byte. This establishes only the entry branch and does not import or imply Decompilation reconstruction state. The release remains a candidate.

