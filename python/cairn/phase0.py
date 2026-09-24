"""Phase 0: how does the human blueprint order compare with other valid orders of the same graph?"""

from __future__ import annotations

import json
import random
import statistics
from dataclasses import dataclass, field
from pathlib import Path

import networkx as nx

from .blueprint import Blueprint
from .graph import (
    OrderMetrics,
    dependency_graph,
    greedy_min_open_order,
    just_in_time_order,
    kendall_tau,
    local_search_order,
    make_dag,
    nearest_topological_order,
    order_metrics,
    random_topological_order,
    uniform_topological_orders,
)

METRICS = ("mean_open", "max_open", "mean_cut", "cutwidth", "mean_edge_length")


@dataclass
class ScopeResult:
    name: str
    n_nodes: int
    n_edges: int
    forward_refs: list[tuple[str, str]]
    cycle_edges_dropped: list[tuple[str, str]]
    orders: dict[str, OrderMetrics]
    tau_vs_human: dict[str, float]
    random: dict[str, list[float]] = field(repr=False)
    random_tau_vs_human: list[float] = field(repr=False)
    uniform: dict[str, list[float]] = field(repr=False)
    chapter_runs: dict[str, int] = field(default_factory=dict)
    """Per order: number of maximal same-chapter runs (= chapters when each chapter is contiguous)."""

    def percentile(self, order: str, metric: str, null: str = "random") -> float:
        """Share of null-model orders strictly better (lower) than ``order`` on ``metric``, ties counted half."""
        value = getattr(self.orders[order], metric)
        dist = getattr(self, null)[metric]
        better = sum(1 for x in dist if x < value) + 0.5 * sum(1 for x in dist if x == value)
        return better / len(dist)

    def summary(self) -> dict:
        return {
            "name": self.name,
            "n_nodes": self.n_nodes,
            "n_edges": self.n_edges,
            "forward_refs": self.forward_refs,
            "cycle_edges_dropped": self.cycle_edges_dropped,
            "orders": {k: v.as_dict() for k, v in self.orders.items()},
            "tau_vs_human": self.tau_vs_human,
            "random": {
                m: {
                    "mean": statistics.fmean(xs),
                    "p05": _quantile(xs, 0.05),
                    "p50": _quantile(xs, 0.5),
                    "p95": _quantile(xs, 0.95),
                }
                for m, xs in self.random.items()
            },
            "random_tau_vs_human_mean": statistics.fmean(self.random_tau_vs_human),
            "uniform": {
                m: {"p05": _quantile(xs, 0.05), "p50": _quantile(xs, 0.5), "p95": _quantile(xs, 0.95)}
                for m, xs in self.uniform.items()
            },
            "share_random_better": {
                o: {m: self.percentile(o, m) for m in METRICS} for o in self.orders
            },
            "share_uniform_better": {
                o: {m: self.percentile(o, m, "uniform") for m in METRICS} for o in self.orders
            },
            "chapter_runs": self.chapter_runs,
        }


def _quantile(xs: list[float], q: float) -> float:
    s = sorted(xs)
    return s[min(len(s) - 1, int(q * len(s)))]


def analyse_scope(
    name: str,
    g: nx.DiGraph,
    human: list[str],
    samples: int = 1000,
    restarts: int = 20,
    seed: int = 0,
    uniform_samples: int = 200,
) -> ScopeResult:
    rng = random.Random(seed)
    pos = {v: i for i, v in enumerate(human)}
    forward = sorted(((u, v) for u, v in g.edges if pos[u] > pos[v]), key=lambda e: (pos[e[1]], pos[e[0]]))
    dag, dropped = make_dag(g, human)

    repaired = nearest_topological_order(dag, human)
    jit_runs = [just_in_time_order(dag, rng) for _ in range(restarts)]
    greedy_runs = [greedy_min_open_order(dag, rng) for _ in range(restarts)]
    optimised_runs = [local_search_order(dag, o) for o in greedy_runs]

    def mean_open(o):
        return order_metrics(dag, o).mean_open

    jit = sorted(jit_runs, key=mean_open)[len(jit_runs) // 2]  # median run: JIT is a policy, not an optimiser
    greedy = min(greedy_runs, key=mean_open)
    optimised = min(optimised_runs, key=mean_open)

    # Metrics use the full graph so the human order is charged for its forward references.
    orders = {
        "human": order_metrics(g, human),
        "human_repaired": order_metrics(g, repaired),
        "just_in_time": order_metrics(g, jit),
        "greedy_min_open": order_metrics(g, greedy),
        "optimised": order_metrics(g, optimised),
    }
    tau = {
        "human_repaired": kendall_tau(human, repaired),
        "just_in_time": kendall_tau(human, jit),
        "greedy_min_open": kendall_tau(human, greedy),
        "optimised": kendall_tau(human, optimised),
    }

    random_metrics: dict[str, list[float]] = {m: [] for m in METRICS}
    random_tau = []
    for _ in range(samples):
        o = random_topological_order(dag, rng)
        m = order_metrics(g, o)
        for k in METRICS:
            random_metrics[k].append(getattr(m, k))
        random_tau.append(kendall_tau(human, o))

    uniform_metrics: dict[str, list[float]] = {m: [] for m in METRICS}
    for o in uniform_topological_orders(dag, repaired, uniform_samples, rng):
        m = order_metrics(g, o)
        for k in METRICS:
            uniform_metrics[k].append(getattr(m, k))

    chapter = nx.get_node_attributes(g, "chapter")
    named = {"human": human, "human_repaired": repaired, "just_in_time": jit,
             "greedy_min_open": greedy, "optimised": optimised}
    runs = {k: 1 + sum(chapter[a] != chapter[b] for a, b in zip(o, o[1:], strict=False)) for k, o in named.items()}

    return ScopeResult(
        name=name,
        n_nodes=g.number_of_nodes(),
        n_edges=g.number_of_edges(),
        forward_refs=forward,
        cycle_edges_dropped=dropped,
        orders=orders,
        tau_vs_human=tau,
        random=random_metrics,
        random_tau_vs_human=random_tau,
        uniform=uniform_metrics,
        chapter_runs=runs,
    )


def analyse_blueprint(
    bp: Blueprint,
    samples: int = 1000,
    restarts: int = 20,
    seed: int = 0,
    min_chapter_nodes: int = 8,
    uniform_samples: int = 200,
) -> list[ScopeResult]:
    """Whole document, then each chapter with at least ``min_chapter_nodes`` nodes (intra-chapter edges only)."""
    g = dependency_graph(bp)
    human = [n.id for n in bp.nodes]
    results = [analyse_scope("(whole blueprint)", g, human, samples, restarts, seed, uniform_samples)]
    chapters = list(dict.fromkeys(n.chapter for n in bp.nodes))
    for ch in chapters:
        members = [n.id for n in bp.nodes if n.chapter == ch]
        if len(members) >= min_chapter_nodes:
            results.append(
                analyse_scope(ch, g.subgraph(members).copy(), members, samples, restarts, seed, uniform_samples)
            )
    return results


# --- reporting ---------------------------------------------------------------

ORDER_LABELS = {
    "human": "Human (as written)",
    "human_repaired": "Human, forward refs repaired",
    "just_in_time": "Just-in-time DFS (median run)",
    "greedy_min_open": "Greedy min-open (best run)",
    "optimised": "Greedy + local search (best run)",
}


def write_report(results: list[ScopeResult], out_dir: Path, project: str, provenance: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "phase0.json").write_text(
        json.dumps({"project": project, "provenance": provenance, "scopes": [r.summary() for r in results]}, indent=2)
    )
    from .plots import plot_null_distributions

    plot_null_distributions(results, out_dir / "phase0_mean_open.png", "mean_open", project)
    plot_null_distributions(results, out_dir / "phase0_mean_edge_length.png", "mean_edge_length", project)
    (out_dir / "phase0.md").write_text(_markdown(results, project, provenance))


def _markdown(results: list[ScopeResult], project: str, provenance: str) -> str:
    whole = results[0]
    lines = [
        f"# Phase 0: {project}",
        "",
        f"*{provenance}*",
        "",
        f"{whole.n_nodes} nodes, {whole.n_edges} dependency edges. "
        f"Null models per scope: {len(whole.random['mean_open'])} randomised-Kahn topological orders (biased towards "
        f"opening many results early) and {len(whole.uniform['mean_open'])} approximately uniform ones "
        "(Karzanov–Khachiyan MCMC). "
        "All metrics: lower is better.",
        "",
        "**Share of random orders better than the order** (0% = the order beats every random one; 50% = typical):",
        "",
        "| Scope | n | forward edges | Human: mean open (Kahn null) | Human: mean open (uniform null) | "
        "Human: mean edge length (Kahn) | "
        "Mean open: human / optimised / uniform median | τ(human, optimised) | τ(human, random) |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in results:
        lines.append(
            f"| {r.name} | {r.n_nodes} | {len(r.forward_refs) / max(r.n_edges, 1):.0%} | "
            f"{r.percentile('human', 'mean_open'):.0%} | "
            f"{r.percentile('human', 'mean_open', 'uniform'):.0%} | {r.percentile('human', 'mean_edge_length'):.0%} | "
            f"{r.orders['human'].mean_open:.1f} / {r.orders['optimised'].mean_open:.1f} / "
            f"{_quantile(r.uniform['mean_open'], 0.5):.1f} | {r.tau_vs_human['optimised']:+.2f} | "
            f"{statistics.fmean(r.random_tau_vs_human):+.2f} |"
        )
    lines += [
        "",
        "## Whole blueprint: raw metrics",
        "",
        "| Order | fwd refs | mean open | max open | mean cut | cutwidth | mean edge length | τ vs human "
        "| chapter runs |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, m in whole.orders.items():
        tau = whole.tau_vs_human.get(key, 1.0)
        lines.append(
            f"| {ORDER_LABELS[key]} | {m.forward_refs} | {m.mean_open:.1f} | {m.max_open} | {m.mean_cut:.1f} | "
            f"{m.cutwidth} | {m.mean_edge_length:.1f} | {tau:+.2f} | {whole.chapter_runs[key]} |"
        )
    rnd = whole.random
    lines.append(
        f"| Random topological (median) | 0 | {_quantile(rnd['mean_open'], .5):.1f} | "
        f"{_quantile(rnd['max_open'], .5):.0f} | "
        f"{_quantile(rnd['mean_cut'], .5):.1f} | {_quantile(rnd['cutwidth'], .5):.0f} | "
        f"{_quantile(rnd['mean_edge_length'], .5):.1f} | {statistics.fmean(whole.random_tau_vs_human):+.2f} | |"
    )
    uni = whole.uniform
    lines.append(
        f"| Uniform topological (median) | 0 | {_quantile(uni['mean_open'], .5):.1f} | "
        f"{_quantile(uni['max_open'], .5):.0f} | "
        f"{_quantile(uni['mean_cut'], .5):.1f} | {_quantile(uni['cutwidth'], .5):.0f} | "
        f"{_quantile(uni['mean_edge_length'], .5):.1f} | | |"
    )
    lines += ["", f"## Forward references in the human order ({len(whole.forward_refs)})", ""]
    lines += [f"- `{v}` uses `{u}`, which is stated later" for u, v in whole.forward_refs] or ["None."]
    if whole.cycle_edges_dropped:
        lines += ["", "Cycle-breaking dropped: " + ", ".join(f"`{u}→{v}`" for u, v in whole.cycle_edges_dropped)]
    lines += ["", "![mean open](phase0_mean_open.png)", "", "![mean edge length](phase0_mean_edge_length.png)", ""]
    return "\n".join(lines)
