# Architecture

The target executes on ARM7TDMI using ARMv4T ARM and Thumb instruction sets.
Record ROM file offsets separately from bus addresses.

- direct cartridge ROM is conventionally mapped from `0x08000000`;
- the low bit of a code pointer may indicate Thumb state and is not part of the
  aligned instruction address;
- file-offset conversion is asserted only for verified direct-ROM ranges;
- all ranges in `analysis/sections.csv` are half-open.

Instruction-set state, alignment, pointer encoding, and data byte order must be
recorded rather than inferred silently.
