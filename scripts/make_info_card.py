"""Render a neofetch-style info card SVG (info-card.svg).

Lines fade and slide in one after another. Reads data/contributions.json (if
present) for the live commit stats, so the daily workflow keeps it current.
Set STATIC=1 for a non-animated preview.
"""
import json
import os
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "info-card.svg"

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
W, H = 490, 440
PAD_X = 22
KEY_W = 92
LINE_H = 18.5
STAGGER = 0.09

KEY_COLORS = {"head": "#39d353", "key": "#58a6ff", "sec": "#d2a8ff"}


def rows(stats):
    """(kind, key, value) tuples. kind: head | rule | key | cont | sec | item | gap | swatch"""
    out = [
        ("head", "wiriya@github", ""),
        ("rule", "", ""),
        ("key", "Role", "AI Engineer @ Verisci"),
        ("key", "Prev", "Head of Coding Instructor @ Thideerich"),
        ("key", "Edu", "MSc AI for Business Analytics, KMITL"),
        ("cont", "", "BSc Information Technology, KMITL"),
        ("key", "Focus", "Multi-agent LLMs · RAG · Thai NLP"),
        ("key", "Stack", "Python · LangGraph · LangChain · PyTorch"),
        ("cont", "", "Transformers · PEFT · FastAPI · Docker"),
        ("key", "Data", "Pandas · Supabase/Postgres · ChromaDB"),
        ("key", "Location", "Bangkok, Thailand"),
    ]
    if stats:
        out.append(("key", "Commits", f'{stats["total"]:,} this year · {stats["current_streak"]}d streak'))
    out += [
        ("gap", "", ""),
        ("sec", "Highlights", ""),
        ("item", "", "Multi-agent orchestration w/ shared context"),
        ("item", "", "Data-analysis & geospatial analysis agents"),
        ("item", "", "Document → LLM-wiki ingestion pipeline"),
        ("item", "", "Thai QA retriever + LoRA on Qwen2.5-7B"),
        ("gap", "", ""),
        ("swatch", "", ""),
    ]
    return out


def main():
    static = os.environ.get("STATIC") == "1"
    stats = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else None

    body, y, n = [], 64, 0
    for kind, key, val in rows(stats):
        if kind == "gap":
            y += LINE_H * 0.5
            continue
        delay = 0.3 + n * STAGGER
        style = "" if static else f' style="animation-delay:{delay:.2f}s"'
        g = f'<g class="ln"{style}>'
        if kind == "head":
            g += f'<text x="{PAD_X}" y="{y}" class="b" fill="{KEY_COLORS["head"]}">{escape(key)}</text>'
        elif kind == "rule":
            g += f'<text x="{PAD_X}" y="{y}" fill="#30363d">{"─" * 13}</text>'
        elif kind in ("key", "cont"):
            if key:
                g += f'<text x="{PAD_X}" y="{y}" class="b" fill="{KEY_COLORS["key"]}">{escape(key)}</text>'
            g += f'<text x="{PAD_X + KEY_W}" y="{y}">{escape(val)}</text>'
        elif kind == "sec":
            g += f'<text x="{PAD_X}" y="{y}" class="b" fill="{KEY_COLORS["sec"]}">{escape(key)}</text>'
        elif kind == "item":
            g += (f'<text x="{PAD_X + 6}" y="{y}" fill="#39d353">▸</text>'
                  f'<text x="{PAD_X + 22}" y="{y}">{escape(val)}</text>')
        elif kind == "swatch":
            colors = ["#f85149", "#d29922", "#39d353", "#58a6ff", "#d2a8ff", "#56d4dd", "#c9d1d9", "#484f58"]
            g += "".join(
                f'<rect x="{PAD_X + i * 26}" y="{y - 12}" width="22" height="14" rx="3" fill="{c}"/>'
                for i, c in enumerate(colors)
            )
        body.append(g + "</g>")
        y += LINE_H
        n += 1

    anim = "" if static else """
  .ln { opacity: 0; animation: in .5s cubic-bezier(.2,.7,.3,1) forwards; }
  @keyframes in { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: none; } }
  .cur { animation: blink 1.1s steps(1) infinite; }
  @keyframes blink { 50% { opacity: 0; } }
  @media (prefers-reduced-motion: reduce) { .ln { animation: none; opacity: 1; } }"""

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Wiriya Polchumni - AI Engineer">
<style>
  text {{ font-family: {FONT}; font-size: 12.5px; fill: #c9d1d9; white-space: pre; }}
  .b {{ font-weight: 700; }}
  .t {{ font-size: 11.5px; fill: #7d8590; }}{anim}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0d1117" stroke="#30363d"/>
<path d="M.5 34V10.5a10 10 0 0 1 10-10h{W - 21}a10 10 0 0 1 10 10V34z" fill="#161b22"/>
<line x1="0" y1="34" x2="{W}" y2="34" stroke="#30363d"/>
<circle cx="20" cy="17" r="5.5" fill="#f85149"/><circle cx="38" cy="17" r="5.5" fill="#d29922"/><circle cx="56" cy="17" r="5.5" fill="#39d353"/>
<text class="t" x="{W / 2}" y="21" text-anchor="middle">wiriya@github: ~ — neofetch</text>
{chr(10).join(body)}
<text x="{PAD_X}" y="{H - 18}" fill="#39d353">$</text><rect class="cur" x="{PAD_X + 14}" y="{H - 29}" width="8" height="14" fill="#c9d1d9"/>
</svg>
'''
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT.name}: {n} lines, last baseline y={y - LINE_H:.0f} / {H}")


if __name__ == "__main__":
    main()
