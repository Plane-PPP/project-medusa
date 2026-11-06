#!/usr/bin/env python3
"""Imports the heroine's finished portrait frames into the Medusa package (replaces the TEMP placeholders).

Input: a folder with 56 images named by frame number, any of
    01.png ... 56.png   or   med01-01.png ... med01-56.png
in any size with the portrait's 59:79 proportion (for example 944x1264, 472x632 or exactly 118x158), RGB or RGBA.
docs/design/portraits.md lists what each frame shows.

Output: content/engine/rulesets/medusa/icons_x2/med01-01.png ... med01-56.png, 118x158 RGBA, the size of the
restored x2 portraits. The game reads them by name: no C++ rebuild, only a new content pack (Windows CI) or, in
development, nothing at all (the package is linked).

Needs Pillow (python3 -m pip install pillow). Checks: all 56 frames present, the proportion within 1 %, no extra
files with frame names. With --allow-missing, frames not supplied keep their current (placeholder) image.

    python3 tools/import_portraits.py portraits/med01/final
    python3 tools/import_portraits.py portraits/med01/final --dry-run
"""

import argparse
import re
import sys
from pathlib import Path

WIDTH, HEIGHT = 118, 158
FRAMES = range(1, 57)
PREFIX = "med01-"
PACKAGE_ICONS = Path(__file__).resolve().parent.parent / "content/engine/rulesets/medusa/icons_x2"
NAME = re.compile(r"^(?:med01-)?(\d{2})\.(png|webp|jpg|jpeg)$", re.IGNORECASE)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path)
    parser.add_argument("--out", type=Path, default=PACKAGE_ICONS)
    parser.add_argument("--allow-missing", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow is required: python3 -m pip install pillow")

    found = {}
    for path in sorted(args.source.iterdir()):
        match = NAME.match(path.name)
        if not match:
            continue
        number = int(match.group(1))
        if number not in FRAMES:
            sys.exit(f"{path.name}: frame numbers are 01..56")
        if number in found:
            sys.exit(f"Frame {number:02d} given twice: {found[number].name}, {path.name}")
        found[number] = path
    missing = [number for number in FRAMES if number not in found]
    if missing and not args.allow_missing:
        sys.exit("Missing frames: " + ", ".join(f"{n:02d}" for n in missing) + " (or pass --allow-missing)")

    sizes = set()
    for number, path in sorted(found.items()):
        with Image.open(path) as image:
            width, height = image.size
            if abs(width / height - WIDTH / HEIGHT) > 0.01 * WIDTH / HEIGHT:
                sys.exit(f"{path.name}: {width}x{height} is not the portrait proportion 59:79")
            sizes.add((width, height))
            if args.dry_run:
                continue
            frame = image.convert("RGBA")
            if frame.size != (WIDTH, HEIGHT):
                frame = frame.resize((WIDTH, HEIGHT), Image.LANCZOS)
            args.out.mkdir(parents=True, exist_ok=True)
            frame.save(args.out / f"{PREFIX}{number:02d}.png", optimize=True)
    if len(sizes) > 1:
        print("Warning: the frames come in different sizes: " + ", ".join(f"{w}x{h}" for w, h in sorted(sizes)))
    verb = "Checked" if args.dry_run else "Imported"
    print(f"{verb} {len(found)} frames" + (f"; kept {len(missing)} existing" if missing else "") + f" -> {args.out}")


if __name__ == "__main__":
    main()
