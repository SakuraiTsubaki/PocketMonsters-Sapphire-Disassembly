.syntax unified
.thumb

.global Sqrt
.type Sqrt, %function
Sqrt:
    swi 8
    bx lr
.size Sqrt, . - Sqrt

.global VBlankIntrWait
.type VBlankIntrWait, %function
VBlankIntrWait:
    movs r2, #0
    swi 5
    bx lr
.size VBlankIntrWait, . - VBlankIntrWait
