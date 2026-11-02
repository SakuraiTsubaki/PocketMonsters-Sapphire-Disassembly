.syntax unified
.thumb

.global LZ77UnCompVram
.type LZ77UnCompVram, %function
LZ77UnCompVram:
    swi 0x12
    bx lr
.size LZ77UnCompVram, . - LZ77UnCompVram

.global LZ77UnCompWram
.type LZ77UnCompWram, %function
LZ77UnCompWram:
    swi 0x11
    bx lr
.size LZ77UnCompWram, . - LZ77UnCompWram
