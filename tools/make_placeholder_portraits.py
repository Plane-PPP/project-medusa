#!/usr/bin/env python3
"""Writes TEMPORARY placeholder portrait frames for the Medusa heroine (med01-01 ... med01-56).

They are not the heroine: a dark card with a plain green bust silhouette, the word TEMP, the frame number and a coloured
state band, so a game check shows which frame the engine picked (damage red, poison green, disease yellow, sleep blue,
petrified grey, unconscious black). Replace them with tools/import_portraits.py once the real frames exist.

Standard library only (zlib, struct): no image library is needed on the build machine.

    python3 tools/make_placeholder_portraits.py            # writes into the Medusa package
    python3 tools/make_placeholder_portraits.py --out DIR
"""

import argparse
import struct
import zlib
from pathlib import Path

WIDTH, HEIGHT = 118, 158  # x2 of the original 59x79 portrait
PREFIX = "med01-"
PACKAGE_ICONS = Path(__file__).resolve().parent.parent / "content/engine/rulesets/medusa/icons_x2"

# Frame -> (short label, band colour). docs/design/portraits.md has the full table.
NEUTRAL = (150, 140, 110)
STATES = {
    1: ("NORMAL", NEUTRAL), 2: ("CURSED", (120, 60, 150)), 3: ("WEAK", (170, 150, 90)), 4: ("SLEEP", (60, 90, 200)),
    5: ("FEAR", (200, 120, 40)), 6: ("DRUNK", (190, 90, 140)), 7: ("INSANE", (220, 60, 200)),
    8: ("POISON", (40, 190, 60)), 9: ("DISEASE", (210, 200, 40)), 10: ("PARALYZ", (90, 200, 220)),
    11: ("UNCONSC", (20, 20, 20)), 12: ("STONE", (150, 150, 150)), 13: ("BLINK", NEUTRAL), 14: ("WINK", NEUTRAL),
    37: ("HIT 1", (200, 70, 60)), 38: ("HIT 2", (210, 40, 40)), 39: ("HIT 3", (230, 10, 10)),
    40: ("SMILE", (230, 190, 60)), 41: ("GRIN", (240, 210, 70)), 42: ("SAD", (90, 110, 150)),
    43: ("CAST", (120, 120, 240)), 49: ("SCARED", (200, 120, 40)),
}

# 5x7 glyphs for the few characters used.
GLYPHS = {
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    "D": ["11100", "10010", "10001", "10001", "10001", "10010", "11100"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    " ": ["00000"] * 7,
}


class Canvas:
    def __init__(self, width, height, colour):
        self.width, self.height = width, height
        self.pixels = [list(colour) + [255] for _ in range(width * height)]

    def put(self, x, y, colour):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y * self.width + x] = list(colour) + [255]

    def rect(self, x0, y0, x1, y1, colour):
        for y in range(y0, y1):
            for x in range(x0, x1):
                self.put(x, y, colour)

    def ellipse(self, cx, cy, rx, ry, colour):
        for y in range(cy - ry, cy + ry + 1):
            for x in range(cx - rx, cx + rx + 1):
                if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
                    self.put(x, y, colour)

    def text(self, x, y, value, scale, colour):
        for character in value:
            glyph = GLYPHS.get(character, GLYPHS[" "])
            for row, bits in enumerate(glyph):
                for column, bit in enumerate(bits):
                    if bit == "1":
                        self.rect(x + column * scale, y + row * scale, x + (column + 1) * scale,
                                  y + (row + 1) * scale, colour)
            x += 6 * scale

    def png(self):
        raw = b"".join(b"\x00" + bytes(sum((self.pixels[y * self.width + x] for x in range(self.width)), []))
                       for y in range(self.height))

        def chunk(kind, data):
            return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

        header = struct.pack(">IIBBBBB", self.width, self.height, 8, 6, 0, 0, 0)
        return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")


def text_width(value, scale):
    return len(value) * 6 * scale - scale


def frame(number):
    label, band = STATES.get(number, ("EXPR", NEUTRAL))
    canvas = Canvas(WIDTH, HEIGHT, (24, 30, 28))
    # A plain bust: shoulders, neck and head, faintly green, with a few "snake" strokes. Not the heroine.
    canvas.ellipse(59, 150, 50, 30, (60, 82, 64))
    canvas.rect(51, 96, 67, 122, (120, 150, 110))
    canvas.ellipse(59, 74, 26, 32, (132, 165, 120))
    for offset in (-24, -12, 0, 12, 24):
        for step in range(18):
            canvas.rect(59 + offset + (step % 4) - 2, 34 + step, 59 + offset + (step % 4) + 1, 35 + step, (52, 110, 58))
    canvas.rect(0, 0, WIDTH, 16, band)
    canvas.text((WIDTH - text_width(label, 2)) // 2, 1, label, 2, (255, 255, 255) if sum(band) < 360 else (0, 0, 0))
    canvas.text((WIDTH - text_width("TEMP", 4)) // 2, 52, "TEMP", 4, (230, 40, 40))
    number_text = f"{number:02d}"
    canvas.text((WIDTH - text_width(number_text, 3)) // 2, 132, number_text, 3, (255, 240, 200))
    return canvas.png()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=PACKAGE_ICONS)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for number in range(1, 57):
        (args.out / f"{PREFIX}{number:02d}.png").write_bytes(frame(number))
    print(f"Wrote 56 TEMPORARY placeholder frames to {args.out}")


if __name__ == "__main__":
    main()
