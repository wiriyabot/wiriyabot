"""Render profile.svg: ASCII portrait + intro on top, contribution grid below.

Inputs: data/portrait.txt (make_ascii.py) and data/contributions.json
(fetch_contributions.py). Animations play once on load, then freeze.
"""
import json
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
PORTRAIT = ROOT / "data" / "portrait.txt"
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "profile.svg"

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

W, H = 860, 530
PAD = 32

# Portrait block
ART_W = 250
ART_Y = 30

# Intro text block
TEXT_X = 330
NAME = "Wiriya Polchumni"
ROLE = "AI Engineer @ Verisci"
LINES = [
    "Multi-agent LLMs · RAG · Thai NLP",
    "MSc AI for Business Analytics, KMITL",
    "Bangkok, Thailand",
]

# Contribution grid
CELL, GAP = 12, 3
STEP = CELL + GAP
GRID_Y = 372


def portrait(lines):
    cols = max(len(l) for l in lines)
    char_w = ART_W / cols
    line_h = char_w / 0.55
    out = []
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        y = ART_Y + (i + 1) * line_h
        width = len(line) * char_w
        out.append(
            f'<clipPath id="r{i}"><rect x="{PAD}" y="{y - line_h:.2f}" height="{line_h + 1:.2f}" width="0">'
            f'<animate attributeName="width" to="{width + 2:.2f}" begin="{0.1 + i * 0.03:.2f}s" dur=".5s" fill="freeze"/>'
            f'</rect></clipPath>'
            f'<text class="a" x="{PAD}" y="{y:.2f}" textLength="{width:.2f}" lengthAdjust="spacingAndGlyphs" '
            f'clip-path="url(#r{i})">{escape(line)}</text>'
        )
    return "".join(out), char_w * 1.3, ART_Y + len(lines) * line_h


def grid(days):
    first = date.fromisoformat(days[0]["date"])
    start = first.toordinal() - (first.weekday() + 1) % 7
    weeks = (date.fromisoformat(days[-1]["date"]).toordinal() - start) // 7 + 1
    x0 = (W - weeks * STEP + GAP) / 2
    cells = []
    for d in days:
        week, wd = divmod(date.fromisoformat(d["date"]).toordinal() - start, 7)
        cells.append(
            f'<rect class="c" x="{x0 + week * STEP:.1f}" y="{GRID_Y + wd * STEP}" width="{CELL}" height="{CELL}" '
            f'rx="2.5" fill="{PALETTE[d["level"]]}" style="animation-delay:{0.6 + (week + wd) * 0.015:.3f}s"/>'
        )
    return "".join(cells), x0


def main():
    art_lines = PORTRAIT.read_text(encoding="utf-8").rstrip("\n").split("\n")
    art, font_size, art_bottom = portrait(art_lines)

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cells, grid_x = grid(data["days"])

    mid = (ART_Y + art_bottom) / 2
    intro = [
        f'<text class="name f" x="{TEXT_X}" y="{mid - 34:.0f}" style="animation-delay:.3s">{escape(NAME)}</text>',
        f'<text class="role f" x="{TEXT_X}" y="{mid - 4:.0f}" style="animation-delay:.45s">{escape(ROLE)}</text>',
    ]
    for i, line in enumerate(LINES):
        intro.append(
            f'<text class="m f" x="{TEXT_X}" y="{mid + 34 + i * 22:.0f}" style="animation-delay:{0.6 + i * 0.1:.2f}s">'
            f'{escape(line)}</text>'
        )

    footer = (
        f'{data["total"]:,} contributions in the last year'
        f'  ·  {data["current_streak"]}-day streak'
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{NAME}, {ROLE}">
<style>
  .a {{ font-family: {MONO}; font-size: {font_size:.2f}px; fill: #b1bac4; white-space: pre; }}
  .name {{ font-family: {SANS}; font-size: 30px; font-weight: 600; fill: #e6edf3; }}
  .role {{ font-family: {SANS}; font-size: 17px; fill: #39d353; }}
  .m {{ font-family: {MONO}; font-size: 13px; fill: #7d8590; }}
  .f {{ opacity: 0; animation: fade .7s ease-out forwards; }}
  .c {{ opacity: 0; animation: fade .4s ease-out forwards; }}
  @keyframes fade {{ to {{ opacity: 1; }} }}
  @media (prefers-reduced-motion: reduce) {{ .f, .c {{ animation: none; opacity: 1; }} }}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="#0d1117" stroke="#21262d"/>
{art}
{"".join(intro)}
{cells}
<text class="m f" x="{grid_x:.1f}" y="{GRID_Y + 7 * STEP + 26}" style="animation-delay:1.6s;font-size:12px">{footer}</text>
</svg>
'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name}: portrait bottom y={art_bottom:.0f}, {len(data['days'])} days")


if __name__ == "__main__":
    main()
