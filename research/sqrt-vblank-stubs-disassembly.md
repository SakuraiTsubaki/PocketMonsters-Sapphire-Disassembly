# Sapphire Sqrt and VBlankIntrWait SDK stubs

`sapphire-jp-rev0` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one adjacent Sqrt/VBlankIntrWait suite at a fixed +28-byte displacement from the verified reset-stub suite. Sqrt invokes BIOS SWI 8. VBlankIntrWait clears r2, invokes BIOS SWI 5, and returns. Stub presence is recorded independently of whether a game's main loop calls it; Ruby/Sapphire use the call while Emerald/FRLG poll VBlank state directly. No ROM bytes are published.
