.syntax unified
.thumb

.macro LOAD_SAVE reg
    ldr \reg, =gSaveBlock2
.endm

.macro SET_COUNTER_STATE value
    ldr r1, =sPlayTimeCounterState
    movs r0, #\value
    strb r0, [r1]
.endm

.global PlayTimeCounter_Reset
.type PlayTimeCounter_Reset, %function
PlayTimeCounter_Reset:
    SET_COUNTER_STATE 0
    LOAD_SAVE r2
    movs r1, #0
    movs r0, #0
    strh r0, [r2, #14]
    strb r1, [r2, #16]
    strb r1, [r2, #17]
    strb r1, [r2, #18]
    bx lr
.size PlayTimeCounter_Reset, . - PlayTimeCounter_Reset

.global PlayTimeCounter_Start
.type PlayTimeCounter_Start, %function
PlayTimeCounter_Start:
    push {lr}
    SET_COUNTER_STATE 1
    LOAD_SAVE r0
    ldrh r0, [r0, #14]
    ldr r1, =999
    cmp r0, r1
    bls .LStartReturn
    bl PlayTimeCounter_SetToMax
.LStartReturn:
    pop {r0}
    bx r0
.size PlayTimeCounter_Start, . - PlayTimeCounter_Start

.global PlayTimeCounter_Stop
.type PlayTimeCounter_Stop, %function
PlayTimeCounter_Stop:
    SET_COUNTER_STATE 0
    bx lr
.size PlayTimeCounter_Stop, . - PlayTimeCounter_Stop

.global PlayTimeCounter_Update
.type PlayTimeCounter_Update, %function
PlayTimeCounter_Update:
    push {r4, lr}
    ldr r0, =sPlayTimeCounterState
    ldrb r0, [r0]
    cmp r0, #1
    bne .LUpdateReturn
    LOAD_SAVE r4
    ldrb r0, [r4, #18]
    adds r0, #1
    strb r0, [r4, #18]
    cmp r0, #60
    blo .LUpdateReturn
    movs r0, #0
    strb r0, [r4, #18]
    ldrb r0, [r4, #17]
    adds r0, #1
    strb r0, [r4, #17]
    cmp r0, #60
    blo .LUpdateReturn
    movs r0, #0
    strb r0, [r4, #17]
    ldrb r0, [r4, #16]
    adds r0, #1
    strb r0, [r4, #16]
    cmp r0, #60
    blo .LUpdateReturn
    movs r0, #0
    strb r0, [r4, #16]
    ldrh r0, [r4, #14]
    adds r0, #1
    strh r0, [r4, #14]
    ldr r1, =999
    cmp r0, r1
    bls .LUpdateReturn
    bl PlayTimeCounter_SetToMax
.LUpdateReturn:
    pop {r4}
    pop {r0}
    bx r0
.size PlayTimeCounter_Update, . - PlayTimeCounter_Update

.global PlayTimeCounter_SetToMax
.type PlayTimeCounter_SetToMax, %function
PlayTimeCounter_SetToMax:
    SET_COUNTER_STATE 2
    LOAD_SAVE r2
    ldr r0, =999
    strh r0, [r2, #14]
    movs r1, #59
    strb r1, [r2, #16]
    strb r1, [r2, #17]
    strb r1, [r2, #18]
    bx lr
.size PlayTimeCounter_SetToMax, . - PlayTimeCounter_SetToMax
