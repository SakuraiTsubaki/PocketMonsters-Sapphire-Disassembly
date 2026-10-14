# Title-screen Kyogre across later retail revisions

The English rev1/rev2 and German, French, Italian, and Spanish rev1 ROMs were each SHA-256 gated against the release catalog. Every ROM contains exactly one BIOS-LZ77 stream whose decoded 8,192 bytes match the established Kyogre hash `8459431a41689af67a8e6607b7b7e91969e519e94d93c2d65afa332b937cf9f6`.

All six later revisions retain the same compressed stream hash (`8537f3db1bd6b09e07b85c4c5ece6abfeee6c364e2fd2be786e11d878a1d6467`) at release-specific offsets. Palette-aware re-extraction reproduces the existing PNG exactly. Every stream has one stored pointer and one direct Thumb load to VRAM `0x06008000` followed by the local LZ77 routine.

Together with rev0 and Japanese evidence, the asset and loader are now independently covered for all 12 catalogued retail releases. Release status remains candidate and raw ROM data is excluded.
