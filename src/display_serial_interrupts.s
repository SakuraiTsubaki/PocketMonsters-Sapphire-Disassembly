.syntax unified
.thumb

.macro SET_INTR_FLAG flag
    ldr r2, =0x03007FF8
    ldrh r0, [r2]
    movs r1, #\flag
    orrs r0, r1
    strh r0, [r2]
.endm

.macro SET_MAIN_INTR_FLAG base
    ldrh r0, [\base, #28]
    ldrh r2, [\base, #28]
    orrs r1, r0
    strh r1, [\base, #28]
.endm

.global HBlankIntr
.type HBlankIntr, %function
HBlankIntr:
    push {r4, lr}
    ldr r4, =gMain
    ldr r0, [r4, #16]
    cmp r0, #0
    beq .LHBlankNoCallback
    bl CallHBlankCallback
.LHBlankNoCallback:
    SET_INTR_FLAG 2
    SET_MAIN_INTR_FLAG r4
    pop {r4}
    pop {r0}
    bx r0
.size HBlankIntr, . - HBlankIntr

.global VCountIntr
.type VCountIntr, %function
VCountIntr:
    push {r4, lr}
    ldr r4, =gMain
    ldr r0, [r4, #20]
    cmp r0, #0
    beq .LVCountNoCallback
    bl CallVCountCallback
.LVCountNoCallback:
    SET_INTR_FLAG 4
    SET_MAIN_INTR_FLAG r4
    pop {r4}
    pop {r0}
    bx r0
.size VCountIntr, . - VCountIntr

.global SerialIntr
.type SerialIntr, %function
SerialIntr:
    push {r4, lr}
    ldr r4, =gMain
    ldr r0, [r4, #24]
    cmp r0, #0
    beq .LSerialNoCallback
    bl CallSerialCallback
.LSerialNoCallback:
    SET_INTR_FLAG 0x80
    SET_MAIN_INTR_FLAG r4
    pop {r4}
    pop {r0}
    bx r0
.size SerialIntr, . - SerialIntr
