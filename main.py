#!/usr/bin/env python3
"""make.fun entry: Sum up 19 November's world news in one image.
Writes one image to /output/entry.png, deterministically, no network.
Input: source.webp in this repo (1920x1280 newspaper image).
Output: 960x640 PNG, under 1 MB (make.fun limit: max 1024x1024, max 1 MB).
"""
import os
from PIL import Image

def main():
    im = Image.open("source.webp").convert("RGB")
    im = im.resize((960, 640), Image.LANCZOS)
    os.makedirs("/output", exist_ok=True)
    im.save("/output/entry.png", "PNG", optimize=True, compress_level=9)
    size = os.path.getsize("/output/entry.png")
    print(f"wrote /output/entry.png 960x640 {size} bytes")
    assert size <= 1_000_000, "over 1 MB limit"

if __name__ == "__main__":
    main()
