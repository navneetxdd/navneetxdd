#!/usr/bin/env python3
"""Scrape public GitHub contribution calendar (no auth)."""
from __future__ import annotations

import json
import os
import re
import urllib.request
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "contributions.json")
USER = os.environ.get("GH_PROFILE_USER", "navneetxdd")


def fetch_html(user: str) -> str:
    url = f"https://github.com/users/{user}/contributions"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "navneetxdd-profile-signal-map/1.0",
            "Accept": "text/html",
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_days(html: str) -> list[dict]:
    # GitHub calendar cells: data-date + data-level (0-4). Count via tooltip when present.
    cells = re.findall(
        r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*data-level="(\d+)"|'
        r'data-level="(\d+)"[^>]*data-date="(\d{4}-\d{2}-\d{2})"',
        html,
    )
    level_map: dict[str, int] = {}
    for a, b, c, d in cells:
        if a:
            level_map[a] = int(b)
        else:
            level_map[d] = int(c)

    # Optional: tooltips like "3 contributions on January 1, 2025"
    for m in re.finditer(
        r'(\d+)\s+contributions?\s+on\s+[A-Za-z]+\s+\d+,\s+(\d{4})|'
        r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*>.*?(\d+)\s+contribution',
        html,
        re.I | re.S,
    ):
        pass  # levels are enough for palette; keep counts approximate from level

    if not level_map:
        raise SystemExit("No contribution cells found — GitHub markup may have changed.")

    # Approximate counts from level buckets (visual parity with GitHub greens→amber)
    level_to_count = {0: 0, 1: 2, 2: 8, 3: 18, 4: 35}
    days = [
        {"date": d, "count": level_to_count.get(lvl, lvl), "level": lvl}
        for d, lvl in sorted(level_map.items())
    ]
    return days


def fill_year(days: list[dict]) -> list[dict]:
    """Ensure contiguous last-365-ish range for the renderer."""
    by_date = {d["date"]: d for d in days}
    end = date.fromisoformat(max(by_date))
    start = end - timedelta(days=364)
    out = []
    cur = start
    while cur <= end:
        key = cur.isoformat()
        if key in by_date:
            out.append(by_date[key])
        else:
            out.append({"date": key, "count": 0, "level": 0})
        cur += timedelta(days=1)
    return out


def main() -> None:
    html = fetch_html(USER)
    days = fill_year(parse_days(html))
    total = sum(d["count"] for d in days)
    active = sum(1 for d in days if d["count"] > 0)
    payload = {
        "user": USER,
        "generated": date.today().isoformat(),
        "total": total,
        "active_days": active,
        "days": days,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
    print(f"wrote {OUT} ({len(days)} days, ~{total} events, {active} active)")


if __name__ == "__main__":
    main()
