.syntax unified
.thumb

.global AgbMain

.type AgbMain, %function
AgbMain:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl RtcInit
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl SeedRngWithRtc
    bl SetMainCallback2
    bl ReadKeys
    bl DoSoftReset
    bl LinkSendQueueReady
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl LinkRecvQueueReady
    bl LinkRecvPostprocess
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Ljp_link_postprocess_loop:
    b .Ljp_link_postprocess_loop
.size AgbMain, . - AgbMain

.type AgbMain_global_no_link_postprocess, %function
AgbMain_global_no_link_postprocess:
    @ Structural reconstruction; per-release maps preserve conditional edges.
    bl RegisterRamReset
    bl InitKeys
    bl InitIntrHandlers
    bl m4aSoundInit
    bl RtcInit
    bl CheckForFlashMemory
    bl InitMainCallbacks
    bl InitMapMusic
    bl SeedRngWithRtc
    bl SetMainCallback2
    bl ReadKeys
    bl DoSoftReset
    bl LinkSendQueueReady
    bl UpdateLinkAndCallCallbacks
    bl UpdateLinkAndCallCallbacks
    bl LinkRecvQueueReady
    bl UpdateLinkAndCallCallbacks
    bl PlayTimeCounter_Update
    bl MapMusicMain
    bl WaitForVBlank
.Lglobal_no_link_postprocess_loop:
    b .Lglobal_no_link_postprocess_loop
.size AgbMain_global_no_link_postprocess, . - AgbMain_global_no_link_postprocess
