# Sapphire Japanese title-screen Kyogre tiles

The Japanese revision-0 candidate (`AXPJ`, ROM SHA-256
`6a5ff7656531ab41d1ea9cd8f2d045ab6228405b43f3ee09ea3ff5077c0f60c9`)
contains a GBA BIOS-LZ77 stream at `0x36F250`.

Decompression produces 8,192 bytes (256 GBA 4bpp tiles) with SHA-256
`8459431a41689af67a8e6607b7b7e91969e519e94d93c2d65afa332b937cf9f6`.
Converting `pret/pokeruby`'s indexed `graphics/title_screen/kyogre.png`
in 8x8 tile order independently produces the same digest. No compressed
stream or raw ROM fragment is published.

`graphics/title/kyogre-dark.png` is a deterministic 2x tile-sheet rendering
with the public `kyogre_dark.pal` palette. It is not a composed screenshot;
tile-map reconstruction remains separate.

The common `SakuraiTsubaki/Disassembly` GBA LZ77 4bpp extractor reproduces
the image using offset `0x36F250`, 16 tiles per row, and the ROM SHA-256 gate
recorded above. This asset match does not promote the release candidate to
`verified`.

## Whole-ROM discovery evidence

A bounded scan of the complete 8 MiB Japanese ROM found 54 valid BIOS-LZ77
streams with an 8,192-byte decoded length, all with distinct decoded hashes.
The equivalent Ruby scan also found 54. Exactly 53 decoded hashes are shared;
Sapphire's sole unmatched stream is the Kyogre stream at `0x36F250`, and
Ruby's sole unmatched stream is the independently identified Groudon stream.
`analysis/sapphire-jp-rev0-lz77-8192-scan.json` preserves the offsets, lengths,
and hashes for reproduction without publishing ROM bytes.
