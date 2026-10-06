"""Scrape the public GitHub contribution calendar into data/contributions.json.

Uses the unauthenticated endpoint https://github.com/users/<user>/contributions,
so no token is needed locally or in Actions.
"""
import json
import re
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USER = "wiriyabot"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "contributions.json"


def parse_count(text):
    m = re.match(r"\s*([\d,]+) contribution", text)
    return int(m.group(1).replace(",", "")) if m else 0


def streaks(days):
    """Return (current, longest) streak lengths over a date-sorted day list."""
    longest = run = 0
    for d in days:
        run = run + 1 if d["count"] > 0 else 0
        longest = max(longest, run)

    # Current streak may still be alive if today simply has no commits yet.
    current = 0
    tail = list(reversed(days))
    if tail and tail[0]["count"] == 0 and tail[0]["date"] == date.today().isoformat():
        tail = tail[1:]
    for d in tail:
        if d["count"] == 0:
            break
        current += 1
    return current, longest


def main():
    url = f"https://github.com/users/{USER}/contributions"
    html = requests.get(url, timeout=30, headers={"User-Agent": "profile-art"}).text
    soup = BeautifulSoup(html, "html.parser")

    counts = {t["for"]: parse_count(t.get_text()) for t in soup.find_all("tool-tip") if t.get("for")}

    days = []
    for td in soup.select("td.ContributionCalendar-day[data-date]"):
        days.append({
            "date": td["data-date"],
            "level": int(td.get("data-level", 0)),
            "count": counts.get(td.get("id"), 0),
        })
    days.sort(key=lambda d: d["date"])
    if not days:
        raise SystemExit("No contribution cells found - GitHub markup may have changed.")

    current, longest = streaks(days)
    best = max(days, key=lambda d: d["count"])
    monthly = defaultdict(int)
    for d in days:
        monthly[d["date"][:7]] += d["count"]

    data = {
        "user": USER,
        "generated": date.today().isoformat(),
        "total": sum(d["count"] for d in days),
        "current_streak": current,
        "longest_streak": longest,
        "best_day": {"date": best["date"], "count": best["count"]},
        "active_days": sum(1 for d in days if d["count"] > 0),
        "monthly": dict(sorted(monthly.items())),
        "days": days,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1), encoding="utf-8")
    print(f"{len(days)} days, {data['total']} contributions, streak {current} (best {longest})")


if __name__ == "__main__":
    main()
