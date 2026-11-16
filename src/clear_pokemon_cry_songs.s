.syntax unified
.thumb

.global ClearPokemonCrySongs
.type ClearPokemonCrySongs, %function
ClearPokemonCrySongs:
    push {lr}
    sub sp, #4
    mov r1, sp
    movs r0, #0
    strh r0, [r1]
    ldr r1, =gPokemonCrySongs
    ldr r2, =0x01000034
    mov r0, sp
    bl CpuSet
    add sp, #4
    pop {r0}
    bx r0
.size ClearPokemonCrySongs, . - ClearPokemonCrySongs
