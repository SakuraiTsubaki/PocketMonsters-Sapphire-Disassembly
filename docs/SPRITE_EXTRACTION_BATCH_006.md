# Pokémon sprite extraction — batch 006

Batch 006 contains one species to keep sprite commits small and reviewable.

## Included

- Species 006 Charizard.
- 64×64 front and back 4bpp source graphics.
- Normal and shiny 16-color palette source data.
- Front/back PNG previews using both normal and shiny palettes.
- Cross-version provenance for all nine Sapphire ROMs in this project.

## Deduplication result

The Charizard front graphics, back graphics, normal palette, and shiny palette compressed streams are byte-identical across all nine tested ROMs (JP, US/EU revisions, DE Rev 1, FR revisions, IT revisions). The repository therefore stores one canonical copy of each extracted asset. The manifest records each ROM's matching offset and cryptographic hashes instead of duplicating image files per release.

ROM binaries remain input-only and are never committed.
