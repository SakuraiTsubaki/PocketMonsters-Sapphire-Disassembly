.syntax unified
.thumb

.global RLUnCompVram
.type RLUnCompVram, %function
RLUnCompVram:
    swi 0x15
    bx lr
.size RLUnCompVram, . - RLUnCompVram

.global RLUnCompWram
.type RLUnCompWram, %function
RLUnCompWram:
    swi 0x14
    bx lr
.size RLUnCompWram, . - RLUnCompWram
