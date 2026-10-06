"""Turn .local/source-prepped.png into an animated ASCII portrait SVG.

Each row is revealed by a left-to-right wipe (SMIL), staggered top to bottom.
Plays once and freezes. Set STATIC=1 to skip the animation.
"""
import os
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".local" / "source-prepped.png"
OUT = ROOT / "wiriya-ascii.svg"

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

W, H = 370, 440
PAD = 16
COLS = 78
FONT_SIZE = 7.2
CHAR_W = (W - 2 * PAD) / COLS
LINE_H = CHAR_W / 0.55  # monospace glyphs are ~0.55-0.6 of their height
GAMMA = 1.4
ROW_STAGGER = 0.035
WIPE = 0.55


def to_ascii(img):
    aspect = img.height / img.width
    rows = int(COLS * aspect * CHAR_W / LINE_H)
    small = img.convert("L").resize((COLS, rows), Image.LANCZOS)
    a = np.asarray(small, dtype=np.float32) / 255.0
    darkness = (1.0 - a) ** GAMMA
    idx = np.clip((darkness * len(RAMP)).astype(int), 0, len(RAMP) - 1)
    return ["".join(RAMP[i] for i in row).rstrip() for row in idx]


def main():
    static = os.environ.get("STATIC") == "1"
    lines = to_ascii(Image.open(SRC))
    top = (H - len(lines) * LINE_H) / 2 + LINE_H * 0.8

    clips, texts = [], []
    for i, line in enumerate(lines):
        if not line:
            continue
        y = top + i * LINE_H
        x_len = len(line) * CHAR_W
        attrs = f'x="{PAD}" y="{y:.2f}" textLength="{x_len:.2f}" lengthAdjust="spacingAndGlyphs"'
        if static:
            texts.append(f'<text {attrs}>{escape(line)}</text>')
            continue
        clips.append(
            f'<clipPath id="r{i}"><rect x="{PAD}" y="{y - LINE_H:.2f}" height="{LINE_H + 1:.2f}" width="0">'
            f'<animate attributeName="width" from="0" to="{x_len + 2:.2f}" begin="{0.2 + i * ROW_STAGGER:.3f}s" '
            f'dur="{WIPE}s" fill="freeze" calcMode="spline" keySplines=".3 0 .2 1" keyTimes="0;1"/></rect></clipPath>'
        )
        texts.append(f'<text {attrs} clip-path="url(#r{i})">{escape(line)}</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="ASCII portrait of Wiriya">
<style>
  text {{ font-family: {FONT}; font-size: {FONT_SIZE}px; fill: #c9d1d9; white-space: pre; }}
</style>
<defs>{"".join(clips)}</defs>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
{chr(10).join(texts)}
</svg>
'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name}: {len(lines)} rows x {COLS} cols")


if __name__ == "__main__":
    main()
