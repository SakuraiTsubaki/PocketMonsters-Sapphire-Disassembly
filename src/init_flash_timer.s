.syntax unified
.thumb

InitFlashTimer:
    push {lr}
    ldr r0, =gFlashTimerIntrFunc
    ldr r1, [r0]
    movs r0, #2
    bl SetFlashTimerIntr
    pop {r0}
    bx r0

