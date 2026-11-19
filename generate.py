#!/usr/bin/env python3
"""
make.fun bounty entry — "Sum up 19 November's world news in one image"
Bounty: $250 pool, 50 paid places (1st $50, 2nd $30, 3rd $15).
Closes: Saturday 21 Nov 2026, 07:00 WIB.

What this program does:
  1. Takes the entry image (source.jpg/webp in this repo, or --input PATH).
  2. Resizes it proportionally so neither side exceeds 1024 px
     (make.fun limit: max 1024x1024, max 1 MB) — no cropping, so no
     headline is cut off.
  3. Saves it as output.jpg and checks size/dimensions, failing loudly
     if it is still over the limit.
  4. Prints the 9 headlines in the image, with the sources checked
     on 19 Nov 2026 (see HEADLINES below and README.md).

Run:
  python3 generate.py
  python3 generate.py --input my-image.webp --output output.jpg

Requires: Pillow (`pip install Pillow`). No network, no API key.
"""
import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required: pip install Pillow")

MAX_SIDE = 1024
MAX_BYTES = 1_000_000

HEADLINES = [
    "Trump, Xi and Putin meet in China (trilateral, APEC summit, Shenzhen)",
    "Israeli ground operation in Gaza beyond the Yellow Line",
    "Crimean Bridge attacked again",
    "Anthropic $81.3bn IPO — biggest ever (shares +28% day one, per Al Jazeera)",
    "Van Gogh painting sells for record $190.4m at Sotheby's London",
    "Cyclone Akvan nears India (Bay of Bengal, landfall ~20 Nov)",
    "Hakeem Jeffries set to be first African-American U.S. House Speaker",
    "GTA VI global rollout",
    "NASA Voyager 1 reaches one light-day from Earth",
]

SOURCES_CHECKED_19_NOV_2026 = [
    "BBC / NYT via NewsBites — Trump, Xi, Putin in Shenzhen; Crimean Bridge; Van Gogh $190.4m",
    "Al Jazeera via news aggregators — Anthropic raises $81.3bn in biggest IPO of all-time",
    "NDTV / BBC — Hakeem Jeffries nominated/set to be Speaker",
    "Jagran Josh school-assembly headlines 19 Nov 2026 — Cyclone Akvan, GTA VI, Voyager 1",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="source.webp",
                    help="entry image to prepare (default: source.webp)")
    ap.add_argument("--output", default="output.jpg",
                    help="compliant image to write (default: output.jpg)")
    ap.add_argument("--quality", type=int, default=88)
    args = ap.parse_args()

    if not os.path.exists(args.input):
        print(f"input not found: {args.input}")
        print("Put the generated newspaper image next to this script as source.webp,")
        print("or pass --input PATH to the image file.")
        return 2

    im = Image.open(args.input).convert("RGB")
    print(f"input:  {im.size[0]}x{im.size[1]}  {os.path.getsize(args.input):,} bytes")
    im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    im.save(args.output, "JPEG", quality=args.quality)
    size = os.path.getsize(args.output)
    print(f"output: {im.size[0]}x{im.size[1]}  {size:,} bytes  -> {args.output}")

    ok = im.size[0] <= MAX_SIDE and im.size[1] <= MAX_SIDE and size <= MAX_BYTES
    print("make.fun spec (<=1024x1024, <=1 MB):", "PASS" if ok else "FAIL")
    if not ok:
        return 1

    print("\n9 headlines in the image:")
    for i, h in enumerate(HEADLINES, 1):
        print(f"  {i}. {h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
