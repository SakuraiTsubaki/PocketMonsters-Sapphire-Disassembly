PYTHON ?= python3

.PHONY: help check-no-rom identify analyze-startup analyze-early-main analyze-early-sprite analyze-sprite-resources analyze-sprite-animation analyze-sprite-affine-core analyze-sprite-affine-api analyze-sprite-sheet-tiles analyze-sprite-palette

help:
	@echo "PocketMonsters-Sapphire-Disassembly reconstruction targets"
	@echo "  make check-no-rom                    Fail if a working-tree ROM is present"
	@echo "  make identify ROM=path              Print header/hash metadata for a local ROM"
	@echo "  make analyze-startup ROM=path       Decode Init/IntrMain and localization metadata"
	@echo "  make analyze-early-main ROM=path    Fingerprint early main.c function boundaries"
	@echo "  make analyze-early-sprite ROM=path  Fingerprint first 21 sprite.c functions"
	@echo "  make analyze-sprite-resources ROM=path  Fingerprint next 13 sprite.c resource functions"
	@echo "  make analyze-sprite-animation ROM=path  Fingerprint sprite animation-loop functions"
	@echo "  make analyze-sprite-affine-core ROM=path  Fingerprint first 19 affine-animation helpers"
	@echo "  make analyze-sprite-affine-api ROM=path   Fingerprint affine frame/public animation APIs"
	@echo "  make analyze-sprite-sheet-tiles ROM=path  Fingerprint sprite sheet/tile-range functions"
	@echo "  make analyze-sprite-palette ROM=path      Fingerprint sprite palette/tag functions"
	@echo ""
	@echo "Full ROM build targets will be added as reconstruction coverage grows."

check-no-rom:
	@set -e; \
	if find . -type f \( -iname '*.gba' -o -iname '*.agb' -o -iname '*.rom' \) -not -path './.git/*' | grep -q .; then \
		echo "ROM binary found in working tree; keep retail/generated ROMs outside tracked project paths."; \
		exit 1; \
	fi
	@echo "No ROM binaries found in tracked project paths."

identify:
	@test -n "$(ROM)" || (echo "Usage: make identify ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/identify_rom.py "$(ROM)"

analyze-startup:
	@test -n "$(ROM)" || (echo "Usage: make analyze-startup ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_startup.py "$(ROM)"

analyze-early-main:
	@test -n "$(ROM)" || (echo "Usage: make analyze-early-main ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_early_main.py "$(ROM)"

analyze-early-sprite:
	@test -n "$(ROM)" || (echo "Usage: make analyze-early-sprite ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_early_sprite.py "$(ROM)"

analyze-sprite-resources:
	@test -n "$(ROM)" || (echo "Usage: make analyze-sprite-resources ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_sprite_resources.py "$(ROM)"

analyze-sprite-animation:
	@test -n "$(ROM)" || (echo "Usage: make analyze-sprite-animation ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_sprite_animation.py "$(ROM)"

analyze-sprite-affine-core:
	@test -n "$(ROM)" || (echo "Usage: make analyze-sprite-affine-core ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_sprite_affine_core.py "$(ROM)"

analyze-sprite-affine-api:
	@test -n "$(ROM)" || (echo "Usage: make analyze-sprite-affine-api ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_sprite_affine_api.py "$(ROM)"

analyze-sprite-sheet-tiles:
	@test -n "$(ROM)" || (echo "Usage: make analyze-sprite-sheet-tiles ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_sprite_sheet_tiles.py "$(ROM)"

analyze-sprite-palette:
	@test -n "$(ROM)" || (echo "Usage: make analyze-sprite-palette ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/analyze_sprite_palette.py "$(ROM)"
