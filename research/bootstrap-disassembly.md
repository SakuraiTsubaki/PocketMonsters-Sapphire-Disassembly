# Japanese ARM bootstrap disassembly

Starting at the independently decoded entry target `0x080000d0`, twelve ARM words end at `bx r1` at `0x080000fc`. The latest PC-relative load into `r1` reads literal `0x0800024d` from `0x08000244`, proving a Thumb-state transition to aligned address `0x0800024c`.

The exact 48-byte instruction range has SHA-256 `f02a14383a340aceb5cab128e813451f7b6601b552ebb0f412cfc2359d11b2cc`. `src/rom_bootstrap.s` preserves all twelve words byte-for-byte; literal data outside that range remains represented only as verified address/value evidence. This Disassembly result is independently generated and does not import Decompilation source state.

