PYTHON ?= python3

.PHONY: help check-no-rom identify

help:
	@echo "PocketMonsters-Sapphire-Disassembly bootstrap targets"
	@echo "  make check-no-rom          Fail if a tracked working-tree ROM is present"
	@echo "  make identify ROM=path    Print header/hash metadata for a local ROM"
	@echo ""
	@echo "Full ROM build targets will be added as reconstruction coverage grows."

check-no-rom:
	@set -e; \
	if find . -type f \( -iname '*.gba' -o -iname '*.agb' \) -not -path './.git/*' | grep -q .; then \
		echo "ROM binary found in working tree; keep retail/generated ROMs outside tracked project paths."; \
		exit 1; \
	fi
	@echo "No ROM binaries found in tracked project paths."

identify:
	@test -n "$(ROM)" || (echo "Usage: make identify ROM=/path/to/file.gba" && exit 2)
	$(PYTHON) tools/identify_rom.py "$(ROM)"
