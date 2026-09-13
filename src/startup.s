.syntax unified
.arm
.text

/*
 * Shared Sapphire ARM startup reconstructed from the nine reference ROMs.
 * The instruction body is byte-identical across all analyzed targets.
 * Only the AgbMain and gIntrTable literal values vary by target family.
 */

.ifndef AGB_MAIN_PTR
.equ AGB_MAIN_PTR, 0x0800024D
.endif

.ifndef G_INTR_TABLE_PTR
.equ G_INTR_TABLE_PTR, 0x03001BC0
.endif

.global Init
Init:
    mov r0, #0x12
    msr cpsr_fc, r0
    ldr sp, sp_irq
    mov r0, #0x1f
    msr cpsr_fc, r0
    ldr sp, sp_sys
    ldr r1, intr_vector
    adr r0, IntrMain
    str r0, [r1]
    ldr r1, agb_main_ptr
    mov lr, pc
    bx r1
    b Init

sp_sys:
    .word 0x03007E60
sp_irq:
    .word 0x03007FA0

.global IntrMain
IntrMain:
    mov r3, #0x04000000
    add r3, r3, #0x200
    ldr r2, [r3]
    ldrh r1, [r3, #8]
    mrs r0, spsr
    stmdb sp!, {r0-r3, lr}
    mov r0, #1
    strh r0, [r3, #8]
    and r1, r2, r2, lsr #16
    mov r12, #0
    ands r0, r1, #0x80
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x40
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x2
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x1
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x4
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x8
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x10
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x20
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x100
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x200
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x400
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x800
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x1000
    bne IntrMain_FoundIntr
    add r12, r12, #4
    ands r0, r1, #0x2000
    strbne r0, [r3, #-0x17c]
IntrMain_Loop:
    bne IntrMain_Loop
IntrMain_FoundIntr:
    strh r0, [r3, #2]
    mov r1, #0xc2
    bic r2, r2, r0
    and r1, r1, r2
    strh r1, [r3]
    mrs r3, cpsr
    bic r3, r3, #0xdf
    orr r3, r3, #0x1f
    msr cpsr_fc, r3
    ldr r1, g_intr_table_ptr
    add r1, r1, r12
    ldr r0, [r1]
    stmdb sp!, {lr}
    adr lr, IntrMain_RetAddr
    bx r0
IntrMain_RetAddr:
    ldmia sp!, {lr}
    mrs r3, cpsr
    bic r3, r3, #0xdf
    orr r3, r3, #0x92
    msr cpsr_fc, r3
    ldmia sp!, {r0-r3, lr}
    strh r2, [r3]
    strh r1, [r3, #8]
    msr spsr_fc, r0
    bx lr

intr_vector:
    .word 0x03007FFC
agb_main_ptr:
    .word AGB_MAIN_PTR
g_intr_table_ptr:
    .word G_INTR_TABLE_PTR
