# Sapphire InitMapMusic disassembly

`axp-j-rev0-retail` is the Japanese origin reference. All 12 cataloged releases (Japanese, English, German, French, Italian, Spanish) independently resolve the direct boot call immediately after InitMainCallbacks. Every 16-byte routine clears a verified IWRAM gDisableMusic byte and calls ResetMapMusic at relative target +0x10C. Maps publish addresses, structure and hashes, never ROM bytes or halfwords.
