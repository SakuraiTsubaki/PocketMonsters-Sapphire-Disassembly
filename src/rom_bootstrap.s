.syntax unified
.arm
.section .text.rom_bootstrap, "ax", %progbits
.global rom_bootstrap
.type rom_bootstrap, %function
.extern irq_stack_top
.extern system_stack_top
.extern interrupt_vector
.extern thumb_entry_reachable
rom_bootstrap:
    mov r0, #0x12
    msr cpsr_c, r0
    ldr sp, =irq_stack_top
    mov r0, #0x1f
    msr cpsr_c, r0
    ldr sp, =system_stack_top
    ldr r1, =interrupt_vector
    adr r0, arm_interrupt_return
    str r0, [r1]
    ldr r1, =thumb_entry_reachable + 1
    mov lr, pc
    bx r1
arm_interrupt_return:
.size rom_bootstrap, . - rom_bootstrap
