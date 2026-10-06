"""Turn .local/source-prepped.png (from prep_photo.py) into data/portrait.txt.

The text file is committed, so the daily workflow can re-render profile.svg
without needing the source photo.
"""
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".local" / "source-prepped.png"
OUT = ROOT / "data" / "portrait.txt"

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)
COLS = 64
CELL_ASPECT = 0.55  # monospace glyph width / line height
GAMMA = 1.4


def main():
    img = Image.open(SRC).convert("L")
    rows = int(COLS * img.height / img.width * CELL_ASPECT)
    a = np.asarray(img.resize((COLS, rows), Image.LANCZOS), dtype=np.float32) / 255.0
    idx = np.clip(((1.0 - a) ** GAMMA * len(RAMP)).astype(int), 0, len(RAMP) - 1)
    lines = ["".join(RAMP[i] for i in row).rstrip() for row in idx]
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name}: {rows} rows x {COLS} cols")


if __name__ == "__main__":
    main()
