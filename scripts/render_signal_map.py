#!/usr/bin/env python3
"""Amber 'signal map' contribution heatmap — distinct from GitHub-green clones."""
from __future__ import annotations

import datetime
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "signal-map.svg")

# empty → hot amber
PALETTE = ["#1c1917", "#78350f", "#b45309", "#d97706", "#f59e0b", "#fbbf24"]

CELL, GAP = 11, 3
STEP = CELL + GAP
PAD = 20
LEFT_LABEL_W = 28
TOP_LABEL_H = 18
TITLEBAR_H = 30

BG, BG2, FRAME = "#0c0a09", "#1c1917", "#57534e"
MUTED, TEXT, AMBER = "#a8a29e", "#fafaf9", "#f59e0b"

COL_T, ROW_T, CELL_DUR = 0.016, 0.04, 0.38


def level_for(count: int, level_hint: int | None = None) -> int:
    if level_hint is not None and 0 <= level_hint <= 4:
        # map GitHub 0-4 → our 0-5 (boost top)
        return [0, 1, 2, 3, 5][level_hint] if level_hint < 5 else 5
    if count <= 0:
        return 0
    if count <= 3:
        return 1
    if count <= 8:
        return 2
    if count <= 16:
        return 3
    if count <= 28:
        return 4
    return 5


def build_grid(days: list[dict]) -> list[list]:
    first = datetime.date.fromisoformat(days[0]["date"])
    lead_pad = (first.weekday() + 1) % 7  # Sunday-first like GitHub
    grid: list[list] = []
    col: list = [None] * lead_pad
    for d in days:
        date = datetime.date.fromisoformat(d["date"])
        weekday = (date.weekday() + 1) % 7
        while len(col) < weekday:
            col.append(None)
        lvl = level_for(int(d.get("count", 0)), d.get("level"))
        col.append((d["date"], int(d.get("count", 0)), lvl))
        if len(col) == 7:
            grid.append(col)
            col = []
    if col:
        while len(col) < 7:
            col.append(None)
        grid.append(col)
    return grid


def render(data: dict) -> str:
    days = data["days"]
    grid = build_grid(days)
    n_cols = len(grid)
    art_w = n_cols * STEP
    art_h = 7 * STEP

    month_labels = []
    seen = set()
    for ci, column in enumerate(grid):
        for cell in column:
            if cell is None:
                continue
            date = datetime.date.fromisoformat(cell[0])
            key = (date.year, date.month)
            if key not in seen and date.day <= 7:
                seen.add(key)
                month_labels.append((ci, date.strftime("%b")))
            break

    canvas_w = PAD + LEFT_LABEL_W + art_w + PAD
    stats_h = 78
    canvas_h = TITLEBAR_H + TOP_LABEL_H + art_h + stats_h + PAD

    css = (
        f"@keyframes cell{{0%{{opacity:0;transform:translateY(-5px)}}"
        f"100%{{opacity:1;transform:translateY(0)}}}}"
        f".c{{opacity:0;animation:cell {CELL_DUR:.2f}s cubic-bezier(.2,.8,.2,1) both}}"
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" height="{canvas_h}" '
        f'viewBox="0 0 {canvas_w} {canvas_h}" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        f"<style>{css}</style>",
        "<defs>"
        f'<linearGradient id="sbg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>'
        f"</linearGradient></defs>",
        f'<rect width="{canvas_w}" height="{canvas_h}" rx="12" fill="url(#sbg)"/>',
        f'<rect x="0.5" y="0.5" width="{canvas_w - 1}" height="{canvas_h - 1}" rx="12" '
        f'fill="none" stroke="{FRAME}" stroke-opacity="0.9"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{canvas_w}" y2="{TITLEBAR_H}" '
        f'stroke="{FRAME}" stroke-opacity="0.7"/>',
    ]
    for i, col in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i * 16}" cy="{TITLEBAR_H / 2}" r="5" fill="{col}"/>')
    parts.append(
        f'<text x="{canvas_w / 2}" y="{TITLEBAR_H / 2 + 4}" fill="{MUTED}" font-size="12" '
        f'text-anchor="middle">navneet@lab: ~/signal-map --year</text>'
    )

    grid_top = TITLEBAR_H + TOP_LABEL_H
    grid_left = PAD + LEFT_LABEL_W

    for ci, label in month_labels:
        x = grid_left + ci * STEP
        parts.append(f'<text x="{x}" y="{TITLEBAR_H + 13}" fill="{MUTED}" font-size="10">{label}</text>')

    for wi, wname in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        y = grid_top + wi * STEP + CELL * 0.75
        parts.append(f'<text x="{PAD}" y="{y:.1f}" fill="{MUTED}" font-size="9">{wname}</text>')

    for ci, column in enumerate(grid):
        gx = grid_left + ci * STEP
        for ri, cell in enumerate(column):
            if cell is None:
                continue
            _date, count, lvl = cell
            gy = grid_top + ri * STEP
            delay = ci * COL_T + ri * ROW_T
            fill = PALETTE[lvl]
            title = f"{count} on {_date}"
            parts.append(
                f'<rect class="c" x="{gx}" y="{gy}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{fill}" style="animation-delay:{delay:.3f}s">'
                f"<title>{title}</title></rect>"
            )

    # legend + stats
    legend_y = grid_top + art_h + 28
    parts.append(f'<text x="{PAD}" y="{legend_y}" fill="{MUTED}" font-size="11">quiet</text>')
    lx = PAD + 42
    for i, col in enumerate(PALETTE):
        parts.append(
            f'<rect x="{lx + i * (CELL + 2)}" y="{legend_y - 10}" width="{CELL}" height="{CELL}" '
            f'rx="2" fill="{col}"/>'
        )
    parts.append(
        f'<text x="{lx + 6 * (CELL + 2) + 8}" y="{legend_y}" fill="{MUTED}" font-size="11">loud</text>'
    )

    total = data.get("total", sum(d.get("count", 0) for d in days))
    active = data.get("active_days", sum(1 for d in days if d.get("count", 0) > 0))
    generated = data.get("generated", "")
    parts.append(
        f'<text x="{PAD}" y="{legend_y + 28}" fill="{TEXT}" font-size="12">'
        f'<tspan fill="{AMBER}" font-weight="700">{total}</tspan>'
        f'<tspan fill="{MUTED}"> signals · </tspan>'
        f'<tspan fill="{AMBER}" font-weight="700">{active}</tspan>'
        f'<tspan fill="{MUTED}"> active days</tspan></text>'
    )
    parts.append(
        f'<text x="{PAD}" y="{legend_y + 48}" fill="{MUTED}" font-size="10">'
        f"refreshed {generated} · scraped from public profile · no token</text>"
    )
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    if not os.path.exists(IN_PATH):
        raise SystemExit(f"missing {IN_PATH} — run fetch_contributions.py first")
    with open(IN_PATH, encoding="utf-8") as f:
        data = json.load(f)
    svg = render(data)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
        f.write("\n")
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
