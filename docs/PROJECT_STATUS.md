# Project Status

## Current stage

**Phase 1 — target inventory and architecture mapping active**

The clean repository baseline is complete and game-specific disassembly work has started. This project targets the Game Boy Advance architecture and must be mapped as ROM ranges, ARM/Thumb code, data tables, scripts, and assets rather than using the 16 KiB bank model used by Game Boy projects.

| Area | Status |
| --- | --- |
| Version/revision inventory | In progress |
| ROM / section mapping | In progress |
| Code reconstruction | Pending verified target lock |
| Data reconstruction | Pending section classification |
| Scripts / events | Pending section classification |
| Graphics / assets | Pending section classification |
| Audio / resources | Pending section classification |
| Maps / world data | Pending section classification |
| Build / matching verification | Baseline workflow pending |

## Phase 1 rules

- Original ROM binaries are never committed.
- Every target is tracked separately by region, language, revision, and cryptographic hashes.
- ARM and Thumb code ranges are distinguished from data before source conversion.
- Unknown ranges remain explicitly unknown; they are not guessed into named structures.
- The first reconstruction baseline must preserve every byte of the selected target before ranges are replaced with labeled source.

## Next milestone

Lock the first verified Sapphire target, record its header and hashes, establish the ROM-range map, and create the initial byte-preserving reconstruction baseline. Then replace ranges incrementally with labeled ARM/Thumb source and typed data while maintaining matching verification.
