.syntax unified
.thumb

.global InitIntrHandlers
.type InitIntrHandlers, %function
InitIntrHandlers:
    push {r4, r5, lr}
    ldr r5, =IntrMain
    ldr r4, =IntrMain_Buffer
    ldr r3, =gIntrTableTemplate
    ldr r2, =gIntrTable
    movs r1, #13
.LCopyTable:
    ldm r3!, {r0}
    stm r2!, {r0}
    subs r1, #1
    cmp r1, #0
    bge .LCopyTable
    ldr r0, =0x040000D4
    str r5, [r0]
    str r4, [r0, #4]
    ldr r1, =0x84000200
    str r1, [r0, #8]
    ldr r0, [r0, #8]
    ldr r0, =0x03007FFC
    str r4, [r0]
    movs r0, #0
    bl SetVBlankCallback
    movs r0, #0
    bl SetHBlankCallback
    movs r0, #0
    bl SetSerialCallback
    ldr r0, =0x04000208
    movs r1, #1
    strh r1, [r0]
    ldr r0, =0x04000200
    movs r2, #1
    strh r2, [r0]
    ldr r1, =0x04000004
    movs r2, #8
    strh r2, [r1]
    ldrh r0, [r0]
    movs r1, #1
    orrs r0, r1
    ldr r1, =0x04000200
    strh r0, [r1]
    pop {r4, r5}
    pop {r0}
    bx r0
.size InitIntrHandlers, . - InitIntrHandlers

.global SetVBlankCallback
SetVBlankCallback:
    ldr r1, =gMain
    str r0, [r1, #12]
    bx lr

.global SetHBlankCallback
SetHBlankCallback:
    ldr r1, =gMain
    str r0, [r1, #16]
    bx lr

.global SetVCountCallback
SetVCountCallback:
    ldr r1, =gMain
    str r0, [r1, #20]
    bx lr

.global SetSerialCallback
SetSerialCallback:
    ldr r1, =gMain
    str r0, [r1, #24]
    bx lr
