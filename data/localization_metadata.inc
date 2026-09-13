.macro emit_localization_metadata language_id, front, back, palette, shiny, icon, icon_indices, icon_palette, species, moves, decorations
    .rept 12
    .word 0xFFFFFFFF
    .endr
    .word 1
    .word \language_id
    .ascii "pokemon sapphire version"
    .space 8
    .word \front, \back, \palette, \shiny
    .word \icon, \icon_indices, \icon_palette
    .word \species, \moves, \decorations
    .word 0x1220, 0x1340, 0x18, 0x938, 0x3A8C, 0x46, 0x836, 0x84C, 0x182
    .word 0x0A0A0A07, 0x0C060C0C, 0x0C121006, 0x08010B0F
    .word 0xC, 0x890, 0x3AC0, 0x234, 0x238, 9, 10, 0, 8, 0x556, 0x557, 0x312F, 0x311B
    .rept 18
    .word 0
    .endr
    .word 0xFFFFFFFF
.endm
