.syntax unified
.thumb

InitMapMusic:
    push {lr}
    ldr r1, =gDisableMusic
    movs r0, #0
    strb r0, [r1]
    bl ResetMapMusic
    pop {r0}
    bx r0

