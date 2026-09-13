# PocketMonsters-Sapphire-Disassembly

Multi-region, multi-revision source reconstruction and disassembly of **Pokémon Sapphire**.

The long-term goal is to rebuild supported retail ROM revisions from repository sources **without requiring a local base ROM**. ROM binaries themselves are never committed.

## Project goals

- Reconstruct executable code, data tables, scripts, maps, text, graphics, fonts, audio, and build metadata into editable source form.
- Preserve version-specific behavior across Japanese, English/European, German, French, and Italian releases and revisions.
- Rebuild each supported target from repository sources.
- Verify rebuilt outputs against known retail hashes.
- Keep ROM binaries (`*.gba`, `*.agb`, `*.rom`) out of Git history.

## Reference set

The initial source corpus contains nine verified Sapphire ROM images used only as local read-only references during reconstruction:

| Target ID | Game code | SW ver. | Size | SHA-1 |
| --- | --- | ---: | ---: | --- |
| `JPN-AXPJ-v0` | `AXPJ` | 0 | 8 MiB | `3233342c2f3087e6ffe6c1791cd5867db07df842` |
| `USA-AXPE-v0` | `AXPE` | 0 | 16 MiB | `3ccbbd45f8553c36463f13b938e833f652b793e4` |
| `EUR-AXPE-v1` | `AXPE` | 1 | 16 MiB | `4722efb8cd45772ca32555b98fd3b9719f8e60a9` |
| `USA-EUR-AXPE-v2` | `AXPE` | 2 | 16 MiB | `89b45fb172e6b55d51fc0e61989775187f6fe63c` |
| `DEU-AXPD-v1` | `AXPD` | 1 | 16 MiB | `7e6e034f9cdca6d2c4a270fdb50a94def5883d17` |
| `FRA-AXPF-v0` | `AXPF` | 0 | 16 MiB | `c269b5692b2d0e5800ba1ddf117fda95ac648634` |
| `FRA-AXPF-v1` | `AXPF` | 1 | 16 MiB | `860e93f5ea44f4278132f6c1ee5650d07b852fd8` |
| `ITA-AXPI-v0` | `AXPI` | 0 | 16 MiB | `f729dd571fb2c09e72c5c1d68fe0a21e72713d34` |
| `ITA-AXPI-v1` | `AXPI` | 1 | 16 MiB | `73edf67b9b82ff12795622dca412733755d2c0fe` |

Full SHA-256 values and header metadata live in [`config/versions.yml`](config/versions.yml).

## Repository policy

**ROM binaries are the only project artifacts intentionally excluded from Git.** Reconstructed source material, extracted/recreated editable assets, tooling, manifests, tests, documentation, comparison data, build/intermediate data useful for reproducibility, and verification metadata belong in the repository.

Generated ROM images remain outside Git because they are ROM binaries. Other project outputs are retained unless they are ordinary workstation/cache noise.

## Planned source layout

```text
config/         target and revision definitions
src/            C / assembly source
data/           game data tables and script sources
maps/           map source and metadata
text/           language- and revision-aware text sources
graphics/       editable graphics, palettes, tiles, tilemaps, fonts
audio/          music, SFX, cries, samples, voicegroups
include/        headers and constants
tools/          extraction, conversion, validation, and build tooling
verification/   expected hashes and reproducibility checks
docs/           reconstruction notes, ROM maps, and research logs
build/          reproducible build/intermediate artifacts; ROM images excluded
```

## Current status

Reconstruction has started from the ROM entry point and is proceeding linearly into early boot code.

- Nine reference ROM identities and hashes are recorded.
- GBA header differences are mapped and validated.
- German/French/Italian extended metadata at `0xD0–0x203` is reconstructed as assembler source and reproduces the retail bytes exactly.
- Shared ARM `Init`/`IntrMain` is reconstructed in [`src/startup.s`](src/startup.s); the `0x17C`-byte block has been byte-identical in tested target configurations.
- `AgbMain` Thumb entry points, function sizes, early internal symbols, and first initialization calls are mapped by target family.

See [`docs/STARTUP_ANALYSIS.md`](docs/STARTUP_ANALYSIS.md), [`docs/AGBMAIN_ANALYSIS.md`](docs/AGBMAIN_ANALYSIS.md), and [`docs/RECONSTRUCTION.md`](docs/RECONSTRUCTION.md).

The active next step is version-aware Thumb reconstruction beginning at `AgbMain`, followed by the adjacent main-loop/input/interrupt functions.
