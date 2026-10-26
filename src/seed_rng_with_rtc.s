.syntax unified
.thumb

.global SeedRngWithRtc
.type SeedRngWithRtc, %function
.thumb_func
SeedRngWithRtc:
    push {lr}
    bl RtcGetMinuteCount
    adds r2, r0, #0
    lsrs r0, r0, #16
    ldr r1, .LSeedMask
    ands r1, r2
    eors r0, r1
    bl SeedRng
    pop {r0}
    bx r0
.size SeedRngWithRtc, . - SeedRngWithRtc

.align 2
.LSeedMask:
    .4byte 0x0000ffff
