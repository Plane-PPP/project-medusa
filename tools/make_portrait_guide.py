#!/usr/bin/env python3
"""Writes the framing guide for the heroine's portrait frames (portraits/templates/).

The geometry is measured from the game's own restored portraits (pc02-01.png, 118x158, x8 here):
head silhouette (hair) from 2.5 % to 99 % of the height and 5-97 % of the width, eye line 49 %, brows 42 %,
hairline 20 %, nose tip 63 %, mouth 74 %, chin 96 %, pupils at 35 % and 66 % of the width.

    guide-944x1264.png          transparent, coloured lines: an overlay for aligning frames in an image editor
    guide-944x1264-on-grey.png  the same on flat grey #808080: an attachment showing a generator the framing

Standard library only.
"""

import struct
import zlib
from pathlib import Path

W, H = 944, 1264
OUT = Path(__file__).resolve().parent.parent / "portraits/templates"

LINES = {  # fraction of height -> colour
    0.025: (255, 255, 0),   # top of hair / snakes
    0.20: (255, 160, 0),    # hairline
    0.42: (0, 200, 255),    # brows
    0.49: (255, 0, 0),      # EYE LINE
    0.63: (0, 255, 0),      # nose tip
    0.74: (0, 200, 255),    # mouth
    0.96: (255, 160, 0),    # chin
}


def png(pixels):
    raw = b"".join(b"\x00" + bytes(pixels[y * W * 4:(y + 1) * W * 4]) for y in range(H))

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def draw(background):
    pixels = bytearray(background * (W * H))

    def put(x, y, colour):
        if 0 <= x < W and 0 <= y < H:
            pixels[(y * W + x) * 4:(y * W + x) * 4 + 4] = bytes(colour) + b"\xff"

    for fraction, colour in LINES.items():
        y = round(fraction * H)
        for x in range(W):
            for dy in (-1, 0, 1):
                put(x, y + dy, colour)
    for y in range(H):  # centre line, dashed
        if (y // 12) % 2 == 0:
            for dx in (-1, 0, 1):
                put(W // 2 + dx, y, (255, 255, 255))
    for fraction in (0.35, 0.66):  # pupils
        cx, cy = round(fraction * W), round(0.49 * H)
        for r in range(18, 22):
            for step in range(360):
                import math
                put(round(cx + r * math.cos(math.radians(step))), round(cy + r * math.sin(math.radians(step))),
                    (255, 0, 255) if background[3] == 0 else (255, 0, 0))
    import math
    cx, cy, rx, ry = W * 0.51, H * 0.51, W * 0.46, H * 0.485  # head silhouette
    for step in range(3600):
        angle = math.radians(step / 10)
        for dr in (0, 1, 2):
            put(round(cx + (rx + dr) * math.cos(angle)), round(cy + (ry + dr) * math.sin(angle)), (255, 255, 255))
    return png(pixels)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "guide-944x1264.png").write_bytes(draw(bytes((0, 0, 0, 0))))
    (OUT / "guide-944x1264-on-grey.png").write_bytes(draw(bytes((128, 128, 128, 255))))
    print(f"Wrote guides to {OUT}")


if __name__ == "__main__":
    main()
