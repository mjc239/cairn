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
    "best_known": ("#1baf7a", (0, (3, 2)), "Best known (also from author's order)"),
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
    for ax, r in zip(axes.flat, results, strict=False):
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


def plot_motivation_frontier(projects: dict[str, dict], path: Path) -> None:
    """Small multiples, one per project: mean open vs motivated share for the style sweep (bottom-up ->
    hybrid -> top-down), averaged over chapters, with the human order marked."""
    import statistics

    fig, axes = plt.subplots(1, len(projects), figsize=(4.6 * len(projects), 3.6), squeeze=False,
                             facecolor=SURFACE)
    sweep = ["bottom-up, proofs immediately"] + [
        f"hybrid, goals = proofs using >= {m} results" for m in (6, 4, 3, 2, 1)] + ["top-down, deferred proofs"]
    for ax, (name, res) in zip(axes.flat, projects.items(), strict=True):
        ax.set_facecolor(SURFACE)
        scopes = [v for k, v in res["scopes"].items() if k != "(whole blueprint)"]

        def avg(style, key, scopes=scopes):
            return statistics.fmean(s[style][key] for s in scopes)

        xs = [avg(s, "motivated") * 100 for s in sweep]
        ys = [avg(s, "mean_open") for s in sweep]
        ax.plot(xs, ys, color="#2a78d6", linewidth=2, marker="o", markersize=5, zorder=2)
        ax.annotate("bottom-up", (xs[0], ys[0]), textcoords="offset points", xytext=(8, 6),
                    fontsize=8, color=TEXT_SECONDARY)
        ax.annotate("top-down", (xs[-1], ys[-1]), textcoords="offset points", xytext=(-52, -4),
                    fontsize=8, color=TEXT_SECONDARY)
        hx = statistics.fmean(s["human_motivated"] for s in scopes) * 100
        hy = statistics.fmean(s["human_mean_open"] for s in scopes)
        ax.scatter([hx], [hy], s=90, color="#eb6834", edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.annotate("human", (hx, hy), textcoords="offset points", xytext=(10, -10), fontsize=9,
                    color=TEXT_PRIMARY)
        ax.set_title(name, color=TEXT_PRIMARY, fontsize=10, loc="left")
        ax.set_xlabel("lemmas stated after a goal they serve (%)", color=TEXT_SECONDARY, fontsize=8)
        ax.set_ylabel("mean results held open", color=TEXT_SECONDARY, fontsize=8)
        ax.set_xlim(-5, 105)
        ax.tick_params(colors=TEXT_SECONDARY, labelsize=8, length=0)
        ax.grid(color=GRID, linewidth=0.8)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
    handles = [plt.Line2D([], [], color="#2a78d6", linewidth=2, marker="o", markersize=5),
               plt.Line2D([], [], color="#eb6834", marker="o", linestyle="", markersize=9)]
    fig.legend(handles, ["Style sweep: goals = results whose proof uses ≥ m others (m = ∞ … 1)", "Human blueprint"],
               loc="lower center", ncol=2, frameon=False, fontsize=8, labelcolor=TEXT_SECONDARY)
    fig.suptitle("Motivation costs working memory: averaged over chapters", color=TEXT_PRIMARY, fontsize=12,
                 x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.07, 1, 0.95))
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def plot_style_frontier(projects: dict[str, dict], path: Path) -> None:
    """Whole-document motivation vs load for the top_down sweep, one line per roadmap setting."""
    fig, axes = plt.subplots(1, len(projects), figsize=(4.8 * len(projects), 3.8), squeeze=False,
                             facecolor=SURFACE)
    colours = {"none": "#2a78d6", "chapter": "#1baf7a", "document": "#eda100"}
    labels = {"none": "no roadmap", "chapter": "chapter roadmap", "document": "document overview"}
    for ax, (name, res) in zip(axes.flat, projects.items(), strict=True):
        ax.set_facecolor(SURFACE)
        doc = res["document"]
        for roadmap, colour in colours.items():
            rows = sorted((r for r in doc["results"] if r["style"]["roadmap"] == roadmap),
                          key=lambda r: r["style"]["top_down"])
            xs = [r["motivated"] * 100 for r in rows]
            ys = [r["mean_open"] for r in rows]
            ax.plot(xs, ys, color=colour, linewidth=2, marker="o", markersize=4, zorder=2)
            ax.annotate(labels[roadmap], (xs[-1], ys[-1]), textcoords="offset points", xytext=(4, 4),
                        fontsize=7.5, color=TEXT_SECONDARY)
        ends = sorted((r for r in doc["results"] if r["style"]["roadmap"] == "none"),
                      key=lambda r: r["style"]["top_down"])
        ax.annotate("top_down = 0", (ends[0]["motivated"] * 100, ends[0]["mean_open"]), textcoords="offset points",
                    xytext=(-6, 8), fontsize=7.5, color=TEXT_SECONDARY)
        h = doc["human"]
        ax.scatter([h["motivated"] * 100], [h["mean_open"]], s=90, color="#eb6834", edgecolor=SURFACE,
                   linewidth=2, zorder=3)
        ax.annotate("human", (h["motivated"] * 100, h["mean_open"]), textcoords="offset points", xytext=(8, -12),
                    fontsize=9, color=TEXT_PRIMARY)
        ax.set_title(name, color=TEXT_PRIMARY, fontsize=10, loc="left")
        ax.set_xlabel("lemmas stated after a goal they serve (%)", color=TEXT_SECONDARY, fontsize=8)
        ax.set_ylabel("mean results held open (whole document)", color=TEXT_SECONDARY, fontsize=8)
        ax.set_xlim(-5, 115)
        ax.tick_params(colors=TEXT_SECONDARY, labelsize=8, length=0)
        ax.grid(color=GRID, linewidth=0.8)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(GRID)
    handles = [plt.Line2D([], [], color=c, linewidth=2, marker="o", markersize=4) for c in colours.values()]
    handles.append(plt.Line2D([], [], color="#eb6834", marker="o", linestyle="", markersize=9))
    fig.legend(handles, [f"top_down 0 → 1, {labels[k]}" for k in colours] + ["human blueprint"],
               loc="lower center", ncol=4, frameon=False, fontsize=8, labelcolor=TEXT_SECONDARY)
    fig.suptitle("Style parameters, whole document: top_down is the efficient lever", color=TEXT_PRIMARY,
                 fontsize=12, x=0.01, ha="left")
    fig.tight_layout(rect=(0, 0.07, 1, 0.95))
    fig.savefig(path, dpi=150, facecolor=SURFACE)
    plt.close(fig)
