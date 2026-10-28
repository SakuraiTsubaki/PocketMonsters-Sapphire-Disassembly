    .syntax unified
    .thumb

    .equ SPECIES_PIKACHU, 25

    @ Verified table layouts used by the runtime loaders.
    @ struct CompressedSpriteSheet { data, size, tag }
    @ struct CompressedSpritePalette { data, tag, padding }

    .macro CompressedSpriteSheet data, size, tag
    .word \\data
    .hword \\size, \\tag
    .endm

    .macro CompressedSpritePalette data, tag
    .word \\data
    .hword \\tag, 0
    .endm

