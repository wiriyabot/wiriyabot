"""Render data/contributions.json as an animated contribution heatmap SVG.

Cells slide down diagonally (week + weekday) on load, then freeze - no loop.
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "contrib-heatmap.svg"

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

W, H = 860, 196
CELL, GAP = 12, 3
STEP = CELL + GAP
GRID_X, GRID_Y = 38, 46
STAGGER = 0.022  # seconds per diagonal


def neon_threshold(days):
    """Counts at or above the 85th percentile of active days get the neon level."""
    active = sorted(d["count"] for d in days if d["count"] > 0)
    return active[int(len(active) * 0.85)] if active else 1


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    days = data["days"]
    neon = neon_threshold(days)

    # GitHub's grid starts on Sunday; column = weeks since the first Sunday.
    first = date.fromisoformat(days[0]["date"])
    start = first.toordinal() - (first.weekday() + 1) % 7

    cells, months, seen = [], [], set()
    for d in days:
        dt = date.fromisoformat(d["date"])
        week, wd = divmod(dt.toordinal() - start, 7)
        level = 5 if d["level"] == 4 and d["count"] >= neon else d["level"]
        x, y = GRID_X + week * STEP, GRID_Y + wd * STEP
        delay = (week + wd) * STAGGER
        cells.append(
            f'<rect class="c" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
            f'fill="{PALETTE[level]}" style="animation-delay:{delay:.3f}s">'
            f'<title>{d["count"]} on {d["date"]}</title></rect>'
        )
        key = dt.strftime("%Y-%m")
        if dt.day <= 7 and wd == 0 and key not in seen and week < 52:
            seen.add(key)
            months.append(f'<text x="{x}" y="{GRID_Y - 10}">{dt.strftime("%b")}</text>')

    weekdays = "".join(
        f'<text x="{GRID_X - 10}" y="{GRID_Y + i * STEP + 10}" text-anchor="end">{n}</text>'
        for i, n in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
    )

    grid_bottom = GRID_Y + 7 * STEP
    end_delay = (53 + 6) * STAGGER + 0.3
    legend_x = W - 24 - 6 * STEP - 76
    legend = "".join(
        f'<rect x="{legend_x + 38 + i * STEP}" y="{grid_bottom + 18}" width="{CELL}" height="{CELL}" rx="2.5" fill="{c}"/>'
        for i, c in enumerate(PALETTE)
    )
    best = date.fromisoformat(data["best_day"]["date"])
    stats = [
        (f'{data["total"]:,}', "contributions"),
        (f'{data["current_streak"]}d', "streak"),
        (f'{data["longest_streak"]}d', "longest"),
        (f'{data["best_day"]["count"]}', f'best day, {best.strftime("%b")} {best.day}'),
    ]
    stat_text = '<tspan class="sep" dx="10">·</tspan>'.join(
        f'<tspan class="v" dx="{10 if i else 0}">{v}</tspan><tspan dx="6">{label}</tspan>'
        for i, (v, label) in enumerate(stats)
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{data["total"]} GitHub contributions in the last year">
<style>
  text {{ font-family: {FONT}; font-size: 11px; fill: #7d8590; }}
  .c {{ transform-box: fill-box; transform-origin: center; opacity: 0;
        animation: drop .45s cubic-bezier(.2,.8,.3,1.2) forwards; }}
  @keyframes drop {{ from {{ opacity: 0; transform: translateY(-14px) scale(.6); }}
                     to   {{ opacity: 1; transform: none; }} }}
  .foot {{ opacity: 0; animation: fade .6s ease-out {end_delay:.2f}s forwards; }}
  @keyframes fade {{ to {{ opacity: 1; }} }}
  .stats {{ font-size: 12px; }}
  .v {{ fill: #39d353; font-weight: 700; }}
  .sep {{ fill: #484f58; }}
  @media (prefers-reduced-motion: reduce) {{ .c, .foot {{ animation: none; opacity: 1; }} }}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
{"".join(months)}
{weekdays}
{"".join(cells)}
<g class="foot">
  <text class="stats" x="{GRID_X}" y="{grid_bottom + 28}">{stat_text}</text>
  <text x="{legend_x}" y="{grid_bottom + 28}">Less</text>
  {legend}
  <text x="{legend_x + 38 + 6 * STEP + 4}" y="{grid_bottom + 28}">More</text>
</g>
</svg>
'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name} ({len(cells)} cells, neon >= {neon})")


if __name__ == "__main__":
    main()
