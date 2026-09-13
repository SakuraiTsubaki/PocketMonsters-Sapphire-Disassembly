PYTHON ?= python3

.PHONY: help check-no-rom identify analyze-startup

help:
	@echo "PocketMonsters-Sapphire-Disassembly reconstruction targets"
	@echo "  make check-no-rom                 Fail if a working-tree ROM is present"
	@echo "  make identify ROM=path           Print header/hash metadata for a local ROM"
	@echo "  make analyze-startup ROM=path    Decode Init/IntrMain and localization metadata"
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
