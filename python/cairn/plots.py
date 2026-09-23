"""Static figures for reports (PNG, light surface)."""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SURFACE = "#fcfcfb"
TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e4e3df"
NULL_FILL = "#c9c8c1"
# Categorical slots from the reference palette, in fixed order.
LINES = {
    "just_in_time": ("#2a78d6", "-", "Just-in-time DFS"),
    "human": ("#eb6834", "-", "Human (as written)"),
    "human_repaired": ("#eb6834", (0, (3, 2)), "Human, forward refs repaired"),
    "optimised": ("#1baf7a", "-", "Greedy + local search"),
}
METRIC_LABELS = {
    "mean_open": "mean results held open",
    "mean_edge_length": "mean distance from a result to where it is used",
    "mean_cut": "mean dependency edges crossing a gap",
}


def plot_null_distributions(results, path: Path, metric: str, project: str) -> None:
    k = len(results)
    cols = min(3, k)
    rows = math.ceil(k / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(4.2 * cols, 2.9 * rows), squeeze=False, facecolor=SURFACE)
    for ax, r in zip(axes.flat, results):
        ax.set_facecolor(SURFACE)
        xs = r.random[metric]
        ax.hist(xs, bins=30, color=NULL_FILL, edgecolor=SURFACE, linewidth=1)
        for key, (colour, style, _) in LINES.items():
            ax.axvline(getattr(r.orders[key], metric), color=colour, linestyle=style, linewidth=2)
        ax.set_title(f"{r.name}  (n={r.n_nodes})", color=TEXT_PRIMARY, fontsize=10, loc="left")
        ax.tick_params(colors=TEXT_SECONDARY, labelsize=8, length=0)
        ax.set_yticks([])
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color(GRID)
    for ax in list(axes.flat)[k:]:
        ax.set_visible(False)
    handles = [plt.Line2D([], [], color=NULL_FILL, linewidth=8)] + [
        plt.Line2D([], [], color=c, linestyle=s, linewidth=2) for c, s, _ in LINES.values()
    ]
    labels = ["Random topological orders"] + [label for *_, label in LINES.values()]
    fig.legend(handles, labels, loc="lower center", ncol=len(labels), frameon=False, fontsize=8,
               labelcolor=TEXT_SECONDARY, bbox_to_anchor=(0.5, 0))
    fig.suptitle(f"{project}: {METRIC_LABELS.get(metric, metric)} (lower is better)",
                 color=TEXT_PRIMARY, fontsize=12, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.06, 1, 0.97))
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
