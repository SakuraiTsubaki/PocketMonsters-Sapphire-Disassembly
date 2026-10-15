# Sapphire Random and SeedRng

All 12 catalogued Sapphire releases were SHA-256 gated and searched independently. Japanese is the origin reference, followed by English revisions and German, French, Italian and Spanish revisions. Every ROM contains exactly one adjacent `Random`/`SeedRng` pair with identical instruction-range hashes: `72526af8af03e60317e6ac115ece4a9415af188772c5432ec1c145e0acaf09fb` and `77dddf4b6256d28fe54fe4fa7c41a15d549d1d3e086013e03c7919823fda7edb`.

Japanese uses `Random=$0803E130`, `gRngValue=$03004748`. English uses `$08040E84` or `$08040EA4` and `$03004818`; European localizations use `$080411A8`–`$080412A4` and `$03004828`. All prove the ISO-C recurrence `state = 1103515245 * state + 24691`, returning the upper 16 bits.

Naming is corroborated by `pret/pokeruby@5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f`, `src/random.c`. Reports publish no ROM bytes.
