.syntax unified
.arm
.section .text.rom_bootstrap, "ax", %progbits
.global rom_bootstrap
rom_bootstrap:
    .word 0xe3a00012 @ 0x080000d0 other
    .word 0xe129f000 @ 0x080000d4 other
    .word 0xe59fd028 @ 0x080000d8 ldr-literal
    .word 0xe3a0001f @ 0x080000dc other
    .word 0xe129f000 @ 0x080000e0 other
    .word 0xe59fd018 @ 0x080000e4 ldr-literal
    .word 0xe59f1150 @ 0x080000e8 ldr-literal
    .word 0xe28f0018 @ 0x080000ec other
    .word 0xe5810000 @ 0x080000f0 other
    .word 0xe59f1148 @ 0x080000f4 ldr-literal
    .word 0xe1a0e00f @ 0x080000f8 other
    .word 0xe12fff11 @ 0x080000fc bx

