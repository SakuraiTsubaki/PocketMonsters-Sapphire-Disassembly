.syntax unified
.thumb

.global RegisterRamReset
.type RegisterRamReset, %function
RegisterRamReset:
    swi 1
    bx lr
.size RegisterRamReset, . - RegisterRamReset

.global SoftReset
.type SoftReset, %function
SoftReset:
    ldr r3, .LRegIme
    movs r2, #0
    strb r2, [r3]
    ldr r1, .LResetStack
    mov sp, r1
    swi 1
    swi 0
    .align 2
.LRegIme:
    .word 0x04000208
.LResetStack:
    .word 0x03007F00
.size SoftReset, . - SoftReset
