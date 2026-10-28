    .syntax unified
    .thumb

CheckForFlashMemory:
    push {lr}
    bl IdentifyFlash
    lsls r0, r0, #16
    cmp r0, #0
    bne .flash_not_present
    ldr r1, =gFlashMemoryPresent
    movs r0, #1
    str r0, [r1]
    bl InitFlashTimer
    b .flash_return
.flash_not_present:
    ldr r1, =gFlashMemoryPresent
    movs r0, #0
    str r0, [r1]
.flash_return:
    pop {r0}
    bx r0

