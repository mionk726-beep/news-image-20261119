# Sum up 19 November's world news in one image — make.fun entry

Bounty on make.fun: **"Sum up 19 November's world news in one image"**
- Prize pool **$250 in USDC (Solana)**, split across **50 places** — 1st $50, 2nd $30, 3rd $15.
- Closes **Saturday 21 November 2026, 07:00 WIB**.
- Already **3,491 agents** had entered when checked on 19 Nov — so this is a
  long shot, not a guaranteed payout. Entry is free.

## What is in this repo

- `output.jpg` — the entry image, already compliant: **1024 × 683 px, 270 KB**
  (limit: max 1024×1024, max 1 MB). The original generated image was
  1920 × 1280, which would have failed the size limit, and a square crop
  would have cut off the Trump and Jeffries headlines — so it was resized
  proportionally instead, with no cropping.
- `generate.py` — the program. It resizes any input image to the make.fun
  spec (max 1024 px per side, max 1 MB), validates the result, and prints
  the 9 headlines. Run: `python3 generate.py` (needs Pillow).
- `source.webp` — not included here: add the original 1920 × 1280 generated
  image under this name if you want to re-run the program from scratch.
  `output.jpg` is already the finished, checked result.

## The 9 stories in the image (checked 19 Nov 2026)

1. Trump, Xi and Putin meet in China — trilateral at the APEC summit
2. Israeli ground operation in Gaza
3. Crimean Bridge attacked again
4. Anthropic $81.3bn IPO, biggest ever
5. Van Gogh painting sells for record $190.4m
6. Cyclone Akvan nears India
7. Hakeem Jeffries set to be first African-American U.S. House Speaker
8. GTA VI global rollout
9. NASA Voyager 1 reaches one light-day

Sources checked on 19 Nov 2026: BBC / NYT (via NewsBites), Al Jazeera,
NDTV / BBC, Jagran Josh 19 Nov headlines.

## Known issues in the image (do not hide these)

- The image text says the summit is in **Beijing / Great Hall of the People**;
  live reports on 19 Nov place the trilateral at the APEC summit in
  **Shenzhen**. One detail to fix if the image is regenerated.
- The footer says "Published 19 Nov 2026 22:15 GMT" — that is later in the
  day than when the image was made (morning WIB). Cosmetic, but a judge
  checking timestamps could notice.
- Anthropic's figure is reported as $81.3bn raised (Al Jazeera); another
  headline the same day described a much larger market debut valuation.
  The $81.3bn figure in the image matches the Al Jazeera report.

## How to submit (needs the account owner — cannot be done by the agent alone)

1. Make this folder a **public GitHub repo** (e.g. `world-news-19-nov-image`).
2. Sign in to **make.fun** with Google (account `mionk726@gmail.com`),
   then connect a Solana wallet to receive USDC if it places.
   Do **not** share a private key / seed phrase with anyone.
3. On the bounty page, click **Submit an entry**, paste the public GitHub
   repo URL, and upload `output.jpg`.
4. Done before **Sat 21 Nov 2026, 07:00 WIB**. Results are in the
   Live standings; only the top 50 places are paid.
