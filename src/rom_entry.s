.syntax unified
.arm
.section .text.rom_entry, "ax", %progbits
.global rom_entry
.type rom_entry, %function
rom_entry:
    b rom_bootstrap
.size rom_entry, . - rom_entry
