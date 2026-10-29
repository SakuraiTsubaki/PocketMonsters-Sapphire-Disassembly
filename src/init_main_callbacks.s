.syntax unified
.thumb

InitMainCallbacks:
    push {lr}
    ldr r0, =gMain
    movs r1, #0
    str r1, [r0, #0x20]
    str r1, [r0, #0x24]
    str r1, [r0]
    ldr r0, =CopyrightScreenInit
    bl SetMainCallback2
    pop {r0}
    bx r0

