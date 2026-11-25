.syntax unified
.thumb

.global VBlankIntr
.type VBlankIntr, %function
VBlankIntr:
    @ Synchronize link/wireless state according to the release profile.
    @ Advance the verified gMain VBlank counters and invoke its callback.
    @ Flush buffered video/DMA state where present, service sound/link data,
    @ advance RNG under the profile guard, then set bit 0 in both interrupt flags.
    bl LinkVSync
    bl m4aSoundVSync
    bl CallVBlankCallback
    bl m4aSoundMain
    bl sub_800C35C
    bl Random
    bx lr
.size VBlankIntr, . - VBlankIntr
