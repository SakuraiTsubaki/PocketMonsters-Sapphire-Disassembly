; Verified CB2_InitTitleScreen state-1 statement for every documented locale.
; Per-ROM instruction and literal offsets are recorded in analysis/*-title-kyogre-load.json.

LoadTitleScreenKyogreTiles::
    ldr r0, =TitleScreenKyogreTiles
    ldr r1, =$06008000
    bl LZ77UnCompVram
