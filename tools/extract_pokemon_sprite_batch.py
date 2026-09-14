#!/usr/bin/env python3
"""Extract a small Pokémon sprite batch from Pokémon Sapphire (GBA).

The script reads the front/back/palette table pointers from the European
Sapphire metadata block (the block beginning with "pokemon sapphire version"),
decodes BIOS LZ77 data, writes canonical 4bpp/palette binaries and PNG previews,
and can verify that identical compressed assets occur in additional ROMs.

ROM binaries are inputs only and are never written to the output tree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

from PIL import Image

GBA_BASE = 0x08000000
MARKER = b"pokemon sapphire version"
SPECIES = {
    1: "bulbasaur",
    2: "ivysaur",
    3: "venusaur",
    4: "charmander",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def rom_offset(ptr: int) -> int:
    if not (GBA_BASE <= ptr < GBA_BASE + 0x02000000):
        raise ValueError(f"not a ROM pointer: 0x{ptr:08X}")
    return ptr - GBA_BASE


def find_metadata_tables(rom: bytes) -> dict[str, int]:
    marker = rom.find(MARKER, 0, 0x400)
    if marker < 0:
        raise ValueError("Sapphire metadata marker not found in first 0x400 bytes")
    p = marker + 32
    names = (
        "front_table", "back_table", "normal_palette_table",
        "shiny_palette_table", "icon_table", "icon_palette_indices",
        "icon_palette_table",
    )
    values = struct.unpack_from("<7I", rom, p)
    return {name: rom_offset(value) for name, value in zip(names, values)}


def table_entry(rom: bytes, table_off: int, index: int) -> tuple[int, int, int]:
    ptr, size_or_tag, tag_or_pad = struct.unpack_from("<IHH", rom, table_off + index * 8)
    return rom_offset(ptr), size_or_tag, tag_or_pad


def lz77_decode_with_consumed(src: bytes, off: int) -> tuple[bytes, int]:
    if src[off] != 0x10:
        raise ValueError(f"expected GBA LZ77 header at 0x{off:X}")
    out_len = int.from_bytes(src[off + 1:off + 4], "little")
    i = off + 4
    out = bytearray()
    while len(out) < out_len:
        flags = src[i]
        i += 1
        for bit in range(7, -1, -1):
            if len(out) >= out_len:
                break
            if flags & (1 << bit):
                a = src[i]
                b = src[i + 1]
                i += 2
                length = (a >> 4) + 3
                disp = ((a & 0xF) << 8) | b
                ref = len(out) - disp - 1
                if ref < 0:
                    raise ValueError("invalid LZ77 back-reference")
                for _ in range(length):
                    out.append(out[ref])
                    ref += 1
            else:
                out.append(src[i])
                i += 1
    return bytes(out[:out_len]), i - off


def bgr555_to_rgba(v: int, alpha: int = 255) -> tuple[int, int, int, int]:
    r = (v & 0x1F) * 255 // 31
    g = ((v >> 5) & 0x1F) * 255 // 31
    b = ((v >> 10) & 0x1F) * 255 // 31
    return r, g, b, alpha


def decode_palette(data: bytes) -> list[tuple[int, int, int, int]]:
    if len(data) != 32:
        raise ValueError(f"expected 32-byte 16-color palette, got {len(data)}")
    colors = []
    for i in range(16):
        v = struct.unpack_from("<H", data, i * 2)[0]
        colors.append(bgr555_to_rgba(v, 0 if i == 0 else 255))
    return colors


def render_64x64_4bpp(tiles: bytes, palette: bytes) -> Image.Image:
    if len(tiles) != 0x800:
        raise ValueError(f"expected 0x800 bytes of 64x64 4bpp tiles, got {len(tiles):#x}")
    colors = decode_palette(palette)
    image = Image.new("RGBA", (64, 64))
    px = image.load()
    for tile in range(64):
        tx = (tile % 8) * 8
        ty = (tile // 8) * 8
        base = tile * 32
        for y in range(8):
            for xpair in range(4):
                v = tiles[base + y * 4 + xpair]
                for n, idx in enumerate((v & 0xF, v >> 4)):
                    x = tx + xpair * 2 + n
                    px[x, ty + y] = colors[idx]
    return image


def rom_identity(path: Path, data: bytes) -> dict[str, object]:
    title = data[0xA0:0xAC].rstrip(b"\0").decode("ascii", "replace")
    code = data[0xAC:0xB0].decode("ascii", "replace")
    return {
        "file": path.name,
        "size": len(data),
        "game_title": title,
        "game_code": code,
        "revision": data[0xBC],
        "sha1": sha1(data),
        "sha256": sha256(data),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_rom", type=Path, help="canonical European Sapphire ROM used for table pointers")
    ap.add_argument("--verify-rom", type=Path, action="append", default=[], help="additional ROM in which to locate identical compressed assets")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--species", type=int, nargs="+", default=[1])
    args = ap.parse_args()

    source = args.source_rom.read_bytes()
    tables = find_metadata_tables(source)
    out = args.out
    dirs = {
        "front_raw": out / "graphics/pokemon/raw/front",
        "back_raw": out / "graphics/pokemon/raw/back",
        "pal_normal": out / "graphics/pokemon/raw/palettes/normal",
        "pal_shiny": out / "graphics/pokemon/raw/palettes/shiny",
        "front_normal": out / "graphics/pokemon/front/normal",
        "front_shiny": out / "graphics/pokemon/front/shiny",
        "back_normal": out / "graphics/pokemon/back/normal",
        "back_shiny": out / "graphics/pokemon/back/shiny",
    }
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    verify = [(p, p.read_bytes()) for p in args.verify_rom]
    manifest = {
        "schema": 1,
        "batch": "pokemon-sprites-001-bulbasaur",
        "source": rom_identity(args.source_rom, source),
        "table_offsets": {k: f"0x{v:X}" for k, v in tables.items()},
        "dedupe_policy": "one canonical extracted asset per byte-identical sprite/palette; per-ROM occurrences are recorded as references",
        "species": [],
    }

    for species in args.species:
        name = SPECIES.get(species, f"species_{species:03d}")
        stem = f"{species:03d}_{name}"
        front_off, front_size, front_tag = table_entry(source, tables["front_table"], species)
        back_off, back_size, back_tag = table_entry(source, tables["back_table"], species)
        pal_off, pal_tag, _ = table_entry(source, tables["normal_palette_table"], species)
        shiny_off, shiny_tag, _ = table_entry(source, tables["shiny_palette_table"], species)

        front, front_used = lz77_decode_with_consumed(source, front_off)
        back, back_used = lz77_decode_with_consumed(source, back_off)
        pal, pal_used = lz77_decode_with_consumed(source, pal_off)
        shiny, shiny_used = lz77_decode_with_consumed(source, shiny_off)
        compressed = {
            "front": source[front_off:front_off + front_used],
            "back": source[back_off:back_off + back_used],
            "palette_normal": source[pal_off:pal_off + pal_used],
            "palette_shiny": source[shiny_off:shiny_off + shiny_used],
        }
        raw = {"front": front, "back": back, "palette_normal": pal, "palette_shiny": shiny}

        (dirs["front_raw"] / f"{stem}.4bpp").write_bytes(front)
        (dirs["back_raw"] / f"{stem}.4bpp").write_bytes(back)
        (dirs["pal_normal"] / f"{stem}.gbapal").write_bytes(pal)
        (dirs["pal_shiny"] / f"{stem}.gbapal").write_bytes(shiny)
        render_64x64_4bpp(front, pal).save(dirs["front_normal"] / f"{stem}.png")
        render_64x64_4bpp(front, shiny).save(dirs["front_shiny"] / f"{stem}.png")
        render_64x64_4bpp(back, pal).save(dirs["back_normal"] / f"{stem}.png")
        render_64x64_4bpp(back, shiny).save(dirs["back_shiny"] / f"{stem}.png")

        canonical_offsets = {
            "front": front_off,
            "back": back_off,
            "palette_normal": pal_off,
            "palette_shiny": shiny_off,
        }
        occurrences = []
        for p, rb in [(args.source_rom, source), *verify]:
            locs = {}
            for kind, blob in compressed.items():
                pos = rb.find(blob)
                if pos < 0:
                    raise RuntimeError(f"{kind} for {stem} not found byte-identically in {p.name}")
                locs[kind] = f"0x{pos:X}"
            occurrences.append({"rom": rom_identity(p, rb), "offsets": locs})

        manifest["species"].append({
            "species_id": species,
            "name": name,
            "table_entry": {
                "front_size": front_size,
                "front_tag": front_tag,
                "back_size": back_size,
                "back_tag": back_tag,
                "normal_palette_tag": pal_tag,
                "shiny_palette_tag": shiny_tag,
            },
            "canonical_offsets": {k: f"0x{v:X}" for k, v in canonical_offsets.items()},
            "decoded_sha256": {k: sha256(v) for k, v in raw.items()},
            "compressed_sha256": {k: sha256(v) for k, v in compressed.items()},
            "compressed_size": {k: len(v) for k, v in compressed.items()},
            "occurrences": occurrences,
        })

    manifest_path = out / "data/sprites/pokemon/batch_001_001_bulbasaur.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(manifest_path)


if __name__ == "__main__":
    main()
