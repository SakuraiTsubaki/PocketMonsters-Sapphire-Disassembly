.syntax unified
.thumb

.global ArcTan2
.type ArcTan2, %function
ArcTan2:
    swi 0x0A
    bx lr
.size ArcTan2, . - ArcTan2

.global CpuSet
.type CpuSet, %function
CpuSet:
    swi 0x0B
    bx lr
.size CpuSet, . - CpuSet
