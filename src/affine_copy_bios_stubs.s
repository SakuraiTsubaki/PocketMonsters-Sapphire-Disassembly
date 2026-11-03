.syntax unified
.thumb

.global BgAffineSet
.type BgAffineSet, %function
BgAffineSet:
    swi 0x0E
    bx lr
.size BgAffineSet, . - BgAffineSet

.global CpuFastSet
.type CpuFastSet, %function
CpuFastSet:
    swi 0x0C
    bx lr
.size CpuFastSet, . - CpuFastSet

.global ObjAffineSet
.type ObjAffineSet, %function
ObjAffineSet:
    swi 0x0F
    bx lr
.size ObjAffineSet, . - ObjAffineSet
