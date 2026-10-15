; Sapphire Random/SeedRng semantic Thumb reconstruction.
Random::
    ldr r2, =gRngValue
    ldr r1, [r2]
    ldr r0, =1103515245
    muls r0, r1
    ldr r1, =24691
    adds r0, r0, r1
    str r0, [r2]
    lsrs r0, r0, 16
    bx lr

SeedRng::
    lsls r0, r0, 16
    lsrs r0, r0, 16
    ldr r1, =gRngValue
    str r0, [r1]
    bx lr
