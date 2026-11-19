#!/usr/bin/env python3
"""make.fun entry: Sum up 19 November's world news in one image.

Draws a one-page newspaper front page with the 9 biggest stories of
19 November 2026 and writes it to /output/entry.png.
Deterministic, no network, no input files: the image is drawn from
the headline list below with Pillow only.
Output: 960x640 PNG, under 1 MB (make.fun limit: max 1024x1024, max 1 MB).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 960, 640
BG = (250, 246, 236)
INK = (20, 20, 20)
RED = (178, 34, 34)
GREY = (90, 90, 90)
LINE = (180, 170, 150)

STORIES = [
    ("Trump, Xi and Putin meet in China",
     "Trilateral talks at the APEC summit in Shenzhen."),
    ("Israeli ground operation in Gaza",
     "Ground forces advance as fighting continues."),
    ("Crimean Bridge attacked again",
     "The key crossing is hit once more in the war."),
    ("Anthropic's $81.3bn IPO, biggest ever",
     "The AI firm debuts in the largest listing on record."),
    ("Van Gogh painting sells for record $190.4m",
     "A masterpiece fetches a historic auction price."),
    ("Cyclone Akvan nears India",
     "Storm heads for the coast as warnings go out."),
    ("Hakeem Jeffries set to be first African-American US House Speaker",
     "A historic first for the House of Representatives."),
    ("GTA VI global rollout",
     "The long-awaited game launches around the world."),
    ("NASA Voyager 1 reaches one light-day",
     "The probe is now one light-day from Earth."),
]


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    serif_b = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    serif = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    sans_b = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    f_mast = font(serif_b, 54)
    f_date = font(sans_b, 16)
    f_head = font(sans_b, 19)
    f_body = font(sans, 15)

    d.text((W // 2, 44), "THE WORLD TODAY", font=f_mast, fill=INK, anchor="ma")
    d.text((W // 2, 104), "19 NOVEMBER 2026  -  THE DAY IN NINE STORIES",
           font=f_date, fill=RED, anchor="ma")
    d.line([(40, 132), (W - 40, 132)], fill=LINE, width=2)

    x0, col_w, y = 48, 424, 152
    for i, (head, body) in enumerate(STORIES):
        cx = x0 + (i % 2) * (col_w + 16)
        cy = y + (i // 2) * 94
        d.text((cx, cy), f"{i + 1}.", font=f_head, fill=RED)
        for ln in wrap(d, head, f_head, col_w - 28):
            d.text((cx + 28, cy), ln, font=f_head, fill=INK)
            cy += 23
        for ln in wrap(d, body, f_body, col_w - 28):
            d.text((cx + 28, cy), ln, font=f_body, fill=GREY)
            cy += 19

    d.line([(40, H - 44), (W - 40, H - 44)], fill=LINE, width=2)
    d.text((W // 2, H - 32), "Nine stories, one day  -  19 November 2026",
           font=f_body, fill=GREY, anchor="ma")

    os.makedirs("/output", exist_ok=True)
    im.save("/output/entry.png", "PNG", optimize=True, compress_level=9)
    size = os.path.getsize("/output/entry.png")
    print(f"wrote /output/entry.png {W}x{H} {size} bytes")
    assert size <= 1_000_000, "over 1 MB limit"


if __name__ == "__main__":
    main()
