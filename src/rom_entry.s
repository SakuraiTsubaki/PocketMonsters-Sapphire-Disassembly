.syntax unified
.arm
.section .text.rom_entry, "ax", %progbits
.global rom_entry
rom_entry:
    .word 0xea000032 @ b 0x080000d0 when linked at 0x08000000

