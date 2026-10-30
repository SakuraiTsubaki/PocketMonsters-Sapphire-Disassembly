.syntax unified
.thumb

.balign 4, 0
.global _call_via_r0
.type _call_via_r0, %function
_call_via_r0:
    bx r0
    nop
.size _call_via_r0, . - _call_via_r0

.global _call_via_r1
.type _call_via_r1, %function
_call_via_r1:
    bx r1
    nop
.size _call_via_r1, . - _call_via_r1

.global _call_via_r2
.type _call_via_r2, %function
_call_via_r2:
    bx r2
    nop
.size _call_via_r2, . - _call_via_r2

.global _call_via_r3
.type _call_via_r3, %function
_call_via_r3:
    bx r3
    nop
.size _call_via_r3, . - _call_via_r3

.global _call_via_r4
.type _call_via_r4, %function
_call_via_r4:
    bx r4
    nop
.size _call_via_r4, . - _call_via_r4

.global _call_via_r5
.type _call_via_r5, %function
_call_via_r5:
    bx r5
    nop
.size _call_via_r5, . - _call_via_r5

.global _call_via_r6
.type _call_via_r6, %function
_call_via_r6:
    bx r6
    nop
.size _call_via_r6, . - _call_via_r6

.global _call_via_r7
.type _call_via_r7, %function
_call_via_r7:
    bx r7
    nop
.size _call_via_r7, . - _call_via_r7

.global _call_via_r8
.type _call_via_r8, %function
_call_via_r8:
    bx r8
    nop
.size _call_via_r8, . - _call_via_r8

.global _call_via_r9
.type _call_via_r9, %function
_call_via_r9:
    bx r9
    nop
.size _call_via_r9, . - _call_via_r9

.global _call_via_sl
.type _call_via_sl, %function
_call_via_sl:
    bx sl
    nop
.size _call_via_sl, . - _call_via_sl

.global _call_via_fp
.type _call_via_fp, %function
_call_via_fp:
    bx fp
    nop
.size _call_via_fp, . - _call_via_fp

.global _call_via_ip
.type _call_via_ip, %function
_call_via_ip:
    bx ip
    nop
.size _call_via_ip, . - _call_via_ip

.global _call_via_sp
.type _call_via_sp, %function
_call_via_sp:
    bx sp
    nop
.size _call_via_sp, . - _call_via_sp

.global _call_via_lr
.type _call_via_lr, %function
_call_via_lr:
    bx lr
    nop
.size _call_via_lr, . - _call_via_lr
