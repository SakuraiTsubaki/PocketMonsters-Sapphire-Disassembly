.syntax unified
.thumb

.global InitKeys
.type InitKeys, %function
InitKeys:
    ldr r1, =gKeyRepeatContinueDelay
    movs r0, #5
    strh r0, [r1]
    ldr r1, =gKeyRepeatStartDelay
    movs r0, #40
    strh r0, [r1]
    ldr r1, =gMain
    movs r0, #0
    strh r0, [r1, #44]
    strh r0, [r1, #46]
    strh r0, [r1, #48]
    strh r0, [r1, #40]
    strh r0, [r1, #42]
    bx lr
.size InitKeys, . - InitKeys

.global ReadKeys
.type ReadKeys, %function
ReadKeys:
    push {lr}
    ldr r0, =0x04000130
    ldrh r1, [r0]
    ldr r2, =0x000003FF
    movs r0, r2
    movs r3, r0
    eors r3, r1
    ldr r1, =gMain
    ldrh r2, [r1, #40]
    movs r0, r3
    bics r0, r2
    strh r0, [r1, #42]
    strh r0, [r1, #46]
    strh r0, [r1, #48]
    movs r2, r1
    cmp r3, #0
    beq .Lreset_repeat
    ldrh r0, [r2, #44]
    cmp r0, r3
    bne .Lreset_repeat
    ldrh r0, [r2, #50]
    subs r0, #1
    strh r0, [r2, #50]
    lsls r0, r0, #16
    cmp r0, #0
    bne .Lstore_keys
    strh r3, [r2, #48]
    ldr r0, =gKeyRepeatContinueDelay
    b .Lload_repeat
.Lreset_repeat:
    ldr r0, =gKeyRepeatStartDelay
.Lload_repeat:
    ldrh r0, [r0]
    strh r0, [r2, #50]
.Lstore_keys:
    strh r3, [r2, #40]
    strh r3, [r2, #44]
    ldr r0, =gSaveBlock2
    ldrb r0, [r0, #19]
    cmp r0, #2
    bne .Lwatched
    ldrh r1, [r2, #46]
    movs r3, #0x80
    lsls r3, r3, #2
    movs r0, r3
    ands r0, r1
    cmp r0, #0
    beq .Lheld_l
    movs r0, #1
    orrs r0, r1
    strh r0, [r2, #46]
.Lheld_l:
    ldrh r1, [r2, #44]
    movs r0, r3
    ands r0, r1
    cmp r0, #0
    beq .Lwatched
    movs r0, #1
    orrs r0, r1
    strh r0, [r2, #44]
.Lwatched:
    ldrh r1, [r2, #46]
    ldrh r0, [r2, #54]
    ands r0, r1
    cmp r0, #0
    beq .Lreturn
    movs r0, #1
    strh r0, [r2, #52]
.Lreturn:
    pop {r0}
    bx r0
.size ReadKeys, . - ReadKeys
