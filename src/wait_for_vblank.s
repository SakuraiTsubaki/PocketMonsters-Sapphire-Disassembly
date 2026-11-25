.syntax unified
.thumb

.global WaitForVBlank
.type WaitForVBlank, %function
WaitForVBlank:
    push {lr}
    ldr r1, =gMain
    ldrh r2, [r1, #28]
    ldr r0, =0x0000FFFE
    ands r0, r2
    strh r0, [r1, #28]
    bl VBlankIntrWait
    pop {r0}
    bx r0
.size WaitForVBlank, . - WaitForVBlank
