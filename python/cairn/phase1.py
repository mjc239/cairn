"""Phase 1: compare the blueprint's hand-written ``\\uses`` graph with the dependencies Lean actually records,
and re-run the Phase 0 ordering analysis on the Lean-derived graph."""

from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from .blueprint import Blueprint
from .formal import FormalDecl, formal_graph, join_blueprint, projected_graph
from .graph import dependency_graph
from .phase0 import ScopeResult, _quantile, analyse_scope


def compare_edges(author: nx.DiGraph, lean: nx.DiGraph) -> dict:
    """Classify author ``\\uses`` edges against Lean-derived edges (restricted to nodes present in both)."""
    nodes = set(author.nodes) & set(lean.nodes)
    a = {(u, v) for u, v in author.edges if u in nodes and v in nodes}
    lean_edges = {(u, v) for u, v in lean.edges if u in nodes and v in nodes}
    closure = nx.transitive_closure(lean.subgraph(nodes), reflexive=False)
    direct = a & lean_edges
    implied = {e for e in a - lean_edges if closure.has_edge(*e)}
    absent = a - lean_edges - implied
    unreported = lean_edges - a
    return {
        "author_edges": len(a),
        "lean_edges": len(lean_edges),
        "author_direct_in_lean": len(direct),
        "author_implied_transitively": len(implied),
        "author_absent_from_lean": sorted(absent),
        "lean_unreported_by_author": sorted(unreported),
    }


def analyse(bp: Blueprint, decls: dict[str, FormalDecl], samples: int = 1000, restarts: int = 20,
            seed: int = 0, min_chapter_nodes: int = 8, uniform_samples: int = 200):
    fg = formal_graph(decls)
    join = join_blueprint(bp, decls)
    labelled = {d for ds in join.node_decls.values() for d in ds}
    lean_nodes = projected_graph(bp, fg, join)
    formalised = [n.id for n in bp.nodes if n.id in join.node_decls]
    lean_g = lean_nodes.subgraph(formalised).copy()
    author_g = dependency_graph(bp).subgraph(formalised).copy()

    stats = {
        "project_decls": len(decls),
        "project_decls_by_kind": dict(sorted(_count(d.kind for d in decls.values()).items())),
        "formal_edges": fg.number_of_edges(),
        "blueprint_nodes": len(bp.nodes),
        "blueprint_nodes_with_formal_decl": len(formalised),
        "lean_names_resolved": sum(len(v) for v in join.node_decls.values()),
        "lean_names_missing": join.missing,
        "coverage": join.coverage,
        "labelled_decls": len(labelled),
        "unlabelled_theorems": sum(1 for d in decls.values() if d.kind == "theorem" and d.name not in labelled),
        "edges": compare_edges(author_g, lean_g),
        "cycles_in_lean_projection": not nx.is_directed_acyclic_graph(lean_g),
    }
    kinds = nx.get_node_attributes(lean_g, "kind")
    unreported = stats["edges"]["lean_unreported_by_author"]
    stats["unreported_from_definitions"] = sum(1 for u, _ in unreported if kinds[u] == "definition")
    stats["unreported_top_sources"] = _count(u for u, _ in unreported)
    stats["unreported_top_sources"] = dict(sorted(stats["unreported_top_sources"].items(), key=lambda kv: -kv[1])[:10])
    lemma_g = lean_g.copy()
    lemma_g.remove_edges_from([(u, v) for u, v in lean_g.edges if kinds[u] == "definition"])

    results: list[ScopeResult] = []
    for name, graph in (("author \\uses graph", author_g), ("Lean-derived graph", lean_g),
                        ("Lean-derived, no definition edges", lemma_g)):
        results.append(analyse_scope(f"{name} (whole)", graph, formalised, samples, restarts, seed, uniform_samples))
    chapters = list(dict.fromkeys(bp.by_id()[n].chapter for n in formalised))
    for ch in chapters:
        members = [n for n in formalised if bp.by_id()[n].chapter == ch]
        if len(members) >= min_chapter_nodes:
            results.append(analyse_scope(f"Lean: {ch}", lean_g.subgraph(members).copy(), members,
                                         samples, restarts, seed, uniform_samples))
    return stats, results, lean_g


def _count(items):
    out: dict[str, int] = {}
    for x in items:
        out[x] = out.get(x, 0) + 1
    return out


def write_report(stats: dict, results: list[ScopeResult], out_dir: Path, project: str, provenance: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "phase1.json").write_text(json.dumps(
        {"project": project, "provenance": provenance, "stats": stats, "scopes": [r.summary() for r in results]},
        indent=2, default=list))
    from .plots import plot_null_distributions

    plot_null_distributions(results, out_dir / "phase1_mean_open.png", "mean_open", f"{project} (Lean-derived edges)")
    e = stats["edges"]
    lines = [
        f"# Phase 1: {project}",
        "",
        f"*{provenance}*",
        "",
        "## Formal graph",
        "",
        f"- Project declarations (after folding compiler auxiliaries): {stats['project_decls']} "
        f"({', '.join(f'{k}: {v}' for k, v in stats['project_decls_by_kind'].items())}); "
        f"{stats['formal_edges']} project-internal dependency edges.",
        f"- Blueprint `\\lean{{}}` names resolved to project declarations: {stats['lean_names_resolved']} "
        f"({stats['coverage']:.0%}); {stats['blueprint_nodes_with_formal_decl']} of {stats['blueprint_nodes']} "
        "blueprint nodes have at least one.",
        f"- Project theorems the blueprint never names: {stats['unlabelled_theorems']}.",
        "",
        "## Author `\\uses` edges vs Lean",
        "",
        f"Over the {stats['blueprint_nodes_with_formal_decl']} formalised nodes. Lean edges are projected onto "
        "blueprint nodes through unlabelled helper declarations.",
        "",
        "| | count |",
        "|---|---:|",
        f"| Author edges | {e['author_edges']} |",
        f"| … also a direct Lean dependency | {e['author_direct_in_lean']} |",
        f"| … implied by a chain of Lean dependencies | {e['author_implied_transitively']} |",
        f"| … not a Lean dependency at all | {len(e['author_absent_from_lean'])} |",
        f"| Lean edges | {e['lean_edges']} |",
        f"| … not written by the author | {len(e['lean_unreported_by_author'])} |",
        f"| … … of which from a definition node | {stats['unreported_from_definitions']} |",
        "",
        "Most frequent sources of unreported edges: "
        + ", ".join(f"`{k}` ({v})" for k, v in stats["unreported_top_sources"].items()) + ".",
        "",
        "## Ordering (Phase 0 metrics) on both graphs",
        "",
        "Share of random orders better than the human order (0% = human beats all):",
        "",
        "| Scope | n | edges | Kahn null | uniform null | mean open: human / optimised / uniform median "
        "| τ(human, optimised) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in results:
        lines.append(
            f"| {r.name} | {r.n_nodes} | {r.n_edges} | {r.percentile('human', 'mean_open'):.0%} | "
            f"{r.percentile('human', 'mean_open', 'uniform'):.0%} | {r.orders['human'].mean_open:.1f} / "
            f"{r.orders['optimised'].mean_open:.1f} / {_quantile(r.uniform['mean_open'], 0.5):.1f} | "
            f"{r.tau_vs_human['optimised']:+.2f} |"
        )
    lines += ["", f"Forward references in the human order under Lean edges: {len(results[1].forward_refs)}", ""]
    lines += [f"- `{v}` depends on `{u}`, stated later" for u, v in results[1].forward_refs[:40]]
    if stats["lean_names_missing"]:
        lines += ["", "## `\\lean{}` names not found in the project", ""]
        lines += [f"- `{node}`: " + ", ".join(f"`{n}`" for n in names)
                  for node, names in stats["lean_names_missing"].items()]
    lines += ["", "![mean open](phase1_mean_open.png)", ""]
    (out_dir / "phase1.md").write_text("\n".join(lines))
