"""Phase 2: baselines for the three blueprint-recovery tasks, scored against the human blueprint.

(c) key declarations: which Lean declarations did the authors promote to blueprint nodes?
(a) clustering: can the chapters be recovered from the Lean graph?
(b) ordering: how close do heuristic orders (incl. cluster-then-order and an LLM) get to the human order?
"""

from __future__ import annotations

import json
import random
import re
import statistics
from pathlib import Path

import networkx as nx
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import adjusted_rand_score, average_precision_score, normalized_mutual_info_score, roc_auc_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from .blueprint import Blueprint
from .formal import FormalDecl, formal_graph, join_blueprint, projected_graph
from .graph import (
    greedy_min_open_order,
    just_in_time_order,
    kendall_tau,
    local_search_order,
    make_dag,
    nearest_topological_order,
    order_metrics,
    random_topological_order,
)

# --- (c) key declarations ----------------------------------------------------


def dominator_subtree_sizes(fg: nx.DiGraph) -> dict[str, int]:
    """For each declaration, how many declarations can only be reached from the top-level results through it.

    Uses the reversed graph (result -> what it uses) with a virtual root above every declaration nothing
    else in the project uses. A large dominated subtree marks an unavoidable bottleneck.
    """
    root = "__cairn_root__"
    rg = fg.reverse(copy=True)
    rg.add_node(root)
    rg.add_edges_from((root, v) for v in fg.nodes if fg.out_degree(v) == 0)
    idom = nx.immediate_dominators(rg, root)
    children: dict[str, list[str]] = {}
    for v, d in idom.items():
        if v != d:
            children.setdefault(d, []).append(v)
    size: dict[str, int] = {}
    for v in reversed(list(nx.topological_sort(nx.DiGraph([(d, v) for v, d in idom.items() if v != d])))):
        size[v] = 1 + sum(size[c] for c in children.get(v, []))
    size.pop(root, None)
    return {v: size.get(v, 1) - 1 for v in fg.nodes}


_AUX_SUFFIX = re.compile(r"(_(aux|prelim|core|helper|step|lemma|tmp|technical|main)\d*|_\d+|'+)+$")
VARIANT_FEATURES = (
    "aux-style name",
    "variant of another declaration",
    "has variants",
    "used by exactly one declaration",
    "used only by its own variants",
)


def _stem(name: str) -> tuple[str, str]:
    """(namespace, last component with aux-style suffixes removed): ``Foo.bar_aux'`` -> ``("Foo", "bar")``."""
    ns, _, last = name.rpartition(".")
    return ns, _AUX_SUFFIX.sub("", last) or last


def key_node_features(decls: dict[str, FormalDecl], fg: nx.DiGraph) -> dict[str, dict[str, float]]:
    n = fg.number_of_nodes()
    pr_goal = nx.pagerank(fg)
    pr_use = nx.pagerank(fg.reverse(copy=False))
    betw = nx.betweenness_centrality(fg)
    dom = dominator_subtree_sizes(fg)
    family: dict[tuple[str, str], set[str]] = {}
    for v in fg.nodes:
        family.setdefault(_stem(v), set()).add(v)
    feats = {}
    for v in fg.nodes:
        d = decls[v]
        parts = v.split(".")
        feats[v] = {
            "users (in project)": fg.out_degree(v),
            "uses (in project)": fg.in_degree(v),
            "pagerank, towards results": pr_goal[v] * n,
            "pagerank, towards utilities": pr_use[v] * n,
            "betweenness": betw[v] * n,
            "dominated declarations": dom[v],
            "proof size": d.value_size,
            "statement size": d.type_size,
            "proof / statement size": d.value_size / max(d.type_size, 1),
            "is private": float(d.private),
            "is definition": float(d.kind != "theorem"),
            "is instance": float(parts[-1].startswith("inst")),
            "in ForMathlib/Mathlib module": float(".Mathlib." in f".{d.module}." or "ForMathlib" in d.module),
            "primed name": float(parts[-1].endswith("'")),
            "name length": len(parts[-1]),
        }
        ns_stem = _stem(v)
        relatives = family[ns_stem] - {v}
        users = set(fg.successors(v))
        feats[v].update({
            "aux-style name": float(ns_stem[1] != parts[-1]),
            "variant of another declaration": float(ns_stem[1] != parts[-1] and any(
                r.rpartition(".")[2] == ns_stem[1] for r in relatives)),
            "has variants": float(ns_stem[1] == parts[-1] and bool(relatives)),
            "used by exactly one declaration": float(len(users) == 1),
            "used only by its own variants": float(bool(users) and users <= relatives),
        })
    return feats


def _precision_at_k(y: np.ndarray, score: np.ndarray, k: int) -> float:
    top = np.argsort(-score, kind="stable")[:k]
    return float(y[top].mean())


def evaluate_key_nodes(decls: dict[str, FormalDecl], fg: nx.DiGraph, positives: set[str], seed: int = 0) -> dict:
    feats = key_node_features(decls, fg)
    names = sorted(fg.nodes)
    y = np.array([v in positives for v in names], dtype=float)
    k = int(y.sum())
    cols = list(next(iter(feats.values())).keys())
    x = np.array([[feats[v][c] for c in cols] for v in names], dtype=float)
    single = {}
    for j, c in enumerate(cols):
        s = x[:, j]
        single[c] = {"auroc": float(roc_auc_score(y, s)), "p_at_k": _precision_at_k(y, s, k)}

    # Combined: logistic regression on log-scaled features, cross-validated with Lean modules held out.
    xl = np.sign(x) * np.log1p(np.abs(x))
    groups = [decls[v].module for v in names]
    structural = [j for j, c in enumerate(cols) if c not in VARIANT_FEATURES]
    combined = {}
    for label, idx in (("structural features", structural), ("+ variant-of features", list(range(len(cols))))):
        oof, coef = _cross_validated(xl[:, idx], y, groups)
        combined[label] = {
            "auroc": float(roc_auc_score(y, oof)),
            "average_precision": float(average_precision_score(y, oof)),
            "p_at_k": _precision_at_k(y, oof, k),
            "coefficients": dict(zip([cols[j] for j in idx], coef, strict=True)),
        }
    order = np.argsort(-oof, kind="stable")  # the last (full) model
    rng = random.Random(seed)
    return {
        "n_decls": len(names),
        "n_positive": k,
        "base_rate": k / len(names),
        "single": single,
        "combined": combined,
        "random_p_at_k": statistics.fmean(
            float(y[rng.sample(range(len(names)), k)].mean()) for _ in range(200)
        ),
        "top_unlabelled": [names[i] for i in order if not y[i]][:15],
        "bottom_labelled": [names[i] for i in order[::-1] if y[i]][:15],
    }


def _cross_validated(x: np.ndarray, y: np.ndarray, groups: list[str]) -> tuple[np.ndarray, list[float]]:
    """Out-of-fold probabilities (5 folds, whole modules held out) and the full-data coefficients."""

    def model():
        return make_pipeline(StandardScaler(), LogisticRegression(class_weight="balanced", max_iter=2000))

    oof = np.zeros(len(y))
    for train, test in GroupKFold(n_splits=5).split(x, y, groups):
        oof[test] = model().fit(x[train], y[train]).predict_proba(x[test])[:, 1]
    return oof, model().fit(x, y)[-1].coef_[0].tolist()


# --- (a) chapter clustering --------------------------------------------------


def evaluate_chapter_clustering(bp: Blueprint, join, decls, lean_g: nx.DiGraph, seed: int = 0) -> tuple[dict, dict]:
    nodes = list(lean_g.nodes)
    by_id = bp.by_id()
    truth = [by_id[v].chapter for v in nodes]
    und = lean_g.to_undirected()
    methods: dict[str, dict[str, str]] = {
        "Lean module of the node's declaration": {v: decls[join.node_decls[v][0]].module for v in nodes},
        "Louvain communities (Lean graph)": _communities_to_labels(
            nx.community.louvain_communities(und, seed=seed)),
        "Greedy modularity (Lean graph)": _communities_to_labels(nx.community.greedy_modularity_communities(und)),
    }
    out = {}
    for name, labels in methods.items():
        pred = [labels[v] for v in nodes]
        out[name] = {
            "clusters": len(set(pred)),
            "ari": float(adjusted_rand_score(truth, pred)),
            "nmi": float(normalized_mutual_info_score(truth, pred)),
        }
    rng = random.Random(seed)
    shuffled = []
    for _ in range(200):
        perm = truth[:]
        rng.shuffle(perm)
        shuffled.append((adjusted_rand_score(truth, perm), normalized_mutual_info_score(truth, perm)))
    out["Random (chapter sizes kept)"] = {
        "clusters": len(set(truth)),
        "ari": statistics.fmean(a for a, _ in shuffled),
        "nmi": statistics.fmean(b for _, b in shuffled),
    }
    return out, methods


def _communities_to_labels(comms) -> dict[str, str]:
    return {v: f"c{i}" for i, c in enumerate(comms) for v in c}


# --- (b) ordering --------------------------------------------------------------


def lean_source_order(decls: dict[str, FormalDecl], fg: nx.DiGraph) -> list[str]:
    """Declarations in the order a reader of the Lean sources meets them: modules in import-compatible
    (topological) order, then by line."""
    mg = nx.DiGraph()
    mg.add_nodes_from({d.module for d in decls.values()})
    mg.add_edges_from((decls[u].module, decls[v].module) for u, v in fg.edges if decls[u].module != decls[v].module)
    cond = nx.condensation(mg)
    mod_rank: dict[str, int] = {}
    for i, c in enumerate(nx.lexicographical_topological_sort(cond, key=lambda c: min(cond.nodes[c]["members"]))):
        for m in sorted(cond.nodes[c]["members"]):
            mod_rank[m] = i
    return sorted(decls, key=lambda v: (mod_rank[decls[v].module], decls[v].line or 0, v))


def optimise_order(g: nx.DiGraph, rng: random.Random, restarts: int = 10) -> list[str]:
    runs = [local_search_order(g, greedy_min_open_order(g, rng)) for _ in range(restarts)]
    return min(runs, key=lambda o: order_metrics(g, o).mean_open)


def cluster_then_order(g: nx.DiGraph, clusters: dict[str, str], rng: random.Random,
                       cluster_order: list[str] | None = None, tie: dict[str, int] | None = None) -> list[str]:
    """Order clusters (given, or topologically on the cluster quotient graph), then each cluster internally."""
    members: dict[str, list[str]] = {}
    for v in g.nodes:
        members.setdefault(clusters[v], []).append(v)
    if cluster_order is None:
        q = nx.DiGraph()
        q.add_nodes_from(members)
        q.add_edges_from((clusters[u], clusters[v]) for u, v in g.edges if clusters[u] != clusters[v])
        cond = nx.condensation(q)
        tie = tie or {}

        def key(c):
            return min(min(tie.get(v, 0) for v in members[m]) for m in cond.nodes[c]["members"])

        cluster_order = [m for c in nx.lexicographical_topological_sort(cond, key=key)
                         for m in sorted(cond.nodes[c]["members"])]
    order = []
    for c in cluster_order:
        sub = g.subgraph(members[c]).copy()
        sub_dag, _ = make_dag(sub, sorted(sub.nodes, key=lambda v: (tie or {}).get(v, 0)))
        order.extend(optimise_order(sub_dag, rng) if len(sub) > 2 else nearest_topological_order(sub_dag, sorted(sub)))
    return order


def within_chapter_tau(order: list[str], human: list[str], chapter: dict[str, str], min_size: int = 8) -> float:
    taus = []
    for ch in dict.fromkeys(chapter[v] for v in human):
        h = [v for v in human if chapter[v] == ch]
        if len(h) >= min_size:
            taus.append(kendall_tau(h, [v for v in order if chapter[v] == ch]))
    return statistics.fmean(taus)


def evaluate_orders(bp: Blueprint, decls, fg, join, lean_g: nx.DiGraph, predicted_clusters: dict[str, str],
                    llm_dir: Path | None, seed: int = 0) -> dict:
    rng = random.Random(seed)
    by_id = bp.by_id()
    human = [n.id for n in bp.nodes if n.id in lean_g]
    chapter = {v: by_id[v].chapter for v in human}
    dag, _ = make_dag(lean_g, human)

    src = lean_source_order(decls, fg)
    src_pos = {d: i for i, d in enumerate(src)}
    node_src = {v: min(src_pos[d] for d in join.node_decls[v]) for v in human}
    lean_src_nodes = sorted(human, key=node_src.__getitem__)

    chapters_in_order = list(dict.fromkeys(chapter[v] for v in human))
    orders = {
        "Human (blueprint)": human,
        "Lean source order": lean_src_nodes,
        "Just-in-time DFS": just_in_time_order(dag, rng),
        "Global optimum (greedy + local search)": optimise_order(dag, rng),
        "Cluster-then-order, true chapters": cluster_then_order(dag, chapter, rng, chapters_in_order, node_src),
        "Cluster-then-order, Lean modules": cluster_then_order(dag, predicted_clusters, rng, tie=node_src),
    }
    llm = load_llm_orders(llm_dir, human, chapter, dag) if llm_dir else None
    if llm is not None:
        orders["LLM within true chapters"] = llm["order"]

    randoms = [random_topological_order(dag, rng) for _ in range(200)]
    rows = {}
    for name, o in orders.items():
        m = order_metrics(lean_g, o)
        rows[name] = {
            "tau_whole": kendall_tau(human, o),
            "tau_within_chapters": within_chapter_tau(o, human, chapter),
            "mean_open": m.mean_open,
            "forward_refs": m.forward_refs,
            "chapter_runs": 1 + sum(chapter[a] != chapter[b] for a, b in zip(o, o[1:], strict=False)),
        }
    rows["Random topological (mean of 200)"] = {
        "tau_whole": statistics.fmean(kendall_tau(human, o) for o in randoms),
        "tau_within_chapters": statistics.fmean(within_chapter_tau(o, human, chapter) for o in randoms[:50]),
        "mean_open": statistics.fmean(order_metrics(lean_g, o).mean_open for o in randoms),
        "forward_refs": 0,
        "chapter_runs": statistics.fmean(
            1 + sum(chapter[a] != chapter[b] for a, b in zip(o, o[1:], strict=False)) for o in randoms),
    }
    per_chapter = {}
    for ch in chapters_in_order:
        h = [v for v in human if chapter[v] == ch]
        if len(h) < 8:
            continue
        per_chapter[ch] = {name: kendall_tau(h, [v for v in o if chapter[v] == ch]) for name, o in orders.items()}
    llm_summary = llm and {k: v for k, v in llm.items() if k != "order"}
    return {"orders": rows, "per_chapter_tau": per_chapter, "llm": llm_summary}


# --- LLM ordering baseline (file-based, so any model or API can fill it in) ----------------------------

LLM_INSTRUCTIONS = """You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order."""


_REF_RE = re.compile(r"\\(?:[cC]ref|ref|eqref|autoref)\{([^}]*)\}")


def write_llm_prompts(bp: Blueprint, lean_g: nx.DiGraph, out_dir: Path, seed: int = 0, min_size: int = 8,
                      anonymise: bool = False, titles: bool = True) -> list[Path]:
    """One prompt per chapter, results shuffled with ``seed``.

    With ``anonymise``, blueprint labels are replaced by random ids (``r017``) everywhere, including
    ``\\ref``-style cross-references in statements (references outside the chapter become "[another
    result]"), and the mapping is written to ``<chapter>.ids.json`` so responses can be read back.
    """
    rng = random.Random(seed)
    by_id = bp.by_id()
    human = [n.id for n in bp.nodes if n.id in lean_g]
    dag, _ = make_dag(lean_g, human)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for ch in dict.fromkeys(by_id[v].chapter for v in human):
        members = [v for v in human if by_id[v].chapter == ch]
        if len(members) < min_size:
            continue
        shuffled = members[:]
        rng.shuffle(shuffled)
        sub = dag.subgraph(members)
        if anonymise:
            codes = rng.sample(range(100, 1000), len(members))
            alias = {v: f"r{c}" for v, c in zip(shuffled, codes, strict=True)}
            label_alias = {lab: alias[v] for v in members for lab in by_id[v].labels}
            (out_dir / f"{ch}.ids.json").write_text(json.dumps({a: v for v, a in alias.items()}, indent=1))
        else:
            alias = {v: v for v in members}
            label_alias = None

        def text_of(n, label_alias=label_alias):
            if label_alias is None:
                return n.text
            return _REF_RE.sub(lambda m: ", ".join(
                f"`{label_alias[x.strip()]}`" if x.strip() in label_alias else "[another result]"
                for x in m.group(1).split(",")), n.text)

        lines = [LLM_INSTRUCTIONS, "", "## Results", ""]
        for v in shuffled:
            n = by_id[v]
            title = f" ({n.title})" if n.title and titles else ""
            lines.append(f"- id `{alias[v]}`: {n.kind}{title}. {text_of(n)}")
        lines += ["", "## Constraints", ""]
        edges = sorted((alias[u], alias[v]) for u, v in sub.edges)
        lines += [f"- `{u}` before `{v}`" for u, v in edges] or ["None."]
        path = out_dir / f"{ch}.prompt.md"
        path.write_text("\n".join(lines) + "\n")
        paths.append(path)
    return paths


def load_llm_orders(llm_dir: Path, human: list[str], chapter: dict[str, str], dag: nx.DiGraph) -> dict | None:
    """Read ``<chapter>.response.json`` files; chapters without one keep the human order (and are reported)."""
    if not llm_dir.exists():
        return None
    order, answered, repaired, invalid = [], [], {}, []
    for ch in dict.fromkeys(chapter[v] for v in human):
        h = [v for v in human if chapter[v] == ch]
        resp = llm_dir / f"{ch}.response.json"
        if not resp.exists():
            order.extend(h)
            continue
        try:
            got = json.loads(resp.read_text())
            ids = llm_dir / f"{ch}.ids.json"
            if ids.exists():
                mapping = json.loads(ids.read_text())
                got = [mapping.get(x, x) for x in got]
        except json.JSONDecodeError:
            invalid.append(ch)
            order.extend(h)
            continue
        if sorted(got) != sorted(h):
            invalid.append(ch)
            order.extend(h)
            continue
        sub = dag.subgraph(h)
        pos = {v: i for i, v in enumerate(got)}
        violations = sum(1 for u, v in sub.edges if pos[u] > pos[v])
        if violations:
            got = nearest_topological_order(sub, got)
        repaired[ch] = violations
        answered.append(ch)
        order.extend(got)
    if not answered:
        return None
    return {"order": order, "chapters_answered": answered, "constraint_violations_repaired": repaired,
            "invalid_responses": invalid}


def evaluate_llm_runs(bp: Blueprint, decls: dict[str, FormalDecl], runs: dict[str, list[Path]]) -> dict:
    """Score repeated LLM runs per prompt variant: τ with the human order within chapters, and load."""
    fg = formal_graph(decls)
    join = join_blueprint(bp, decls)
    formalised = [n.id for n in bp.nodes if n.id in join.node_decls]
    lean_g = projected_graph(bp, fg, join).subgraph(formalised).copy()
    by_id = bp.by_id()
    human = formalised
    chapter = {v: by_id[v].chapter for v in human}
    dag, _ = make_dag(lean_g, human)
    out: dict = {"variants": {}}
    for variant, dirs in runs.items():
        scores = []
        for d in dirs:
            res = load_llm_orders(d, human, chapter, dag)
            if res is None:
                continue
            o = res["order"]
            per = {}
            for ch in res["chapters_answered"]:
                h = [v for v in human if chapter[v] == ch]
                per[ch] = kendall_tau(h, [v for v in o if chapter[v] == ch])
            scores.append({"run": str(d), "tau_within_chapters": statistics.fmean(per.values()),
                           "per_chapter": per, "mean_open": order_metrics(lean_g, o).mean_open,
                           "violations_repaired": sum(res["constraint_violations_repaired"].values()),
                           "invalid": res["invalid_responses"]})
        taus = [r["tau_within_chapters"] for r in scores]
        out["variants"][variant] = {
            "runs": scores,
            "tau_mean": statistics.fmean(taus) if taus else None,
            "tau_sd": statistics.stdev(taus) if len(taus) > 1 else 0.0,
        }
    return out


def write_llm_runs_report(res: dict, path: Path, project: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.with_suffix(".json").write_text(json.dumps(res, indent=2))
    lines = [f"# LLM ordering runs: {project}", "",
             "τ = Kendall correlation with the human order, averaged over the answered chapters.", "",
             "| Variant | runs | τ within chapters (mean ± sd) | individual runs | mean open | repaired violations |",
             "|---|---:|---:|---|---:|---:|"]
    for name, v in res["variants"].items():
        runs = v["runs"]
        if not runs:
            continue
        lines.append(f"| {name} | {len(runs)} | {v['tau_mean']:+.2f} ± {v['tau_sd']:.2f} | "
                     + ", ".join(f"{r['tau_within_chapters']:+.2f}" for r in runs) + " | "
                     f"{statistics.fmean(r['mean_open'] for r in runs):.1f} | "
                     f"{sum(r['violations_repaired'] for r in runs)} |")
    chapters = list(next(r for v in res["variants"].values() for r in v["runs"])["per_chapter"])
    lines += ["", "Per-chapter τ (mean over runs):", "", "| Variant | " + " | ".join(chapters) + " |",
              "|---|" + "---:|" * len(chapters)]
    for name, v in res["variants"].items():
        if v["runs"]:
            lines.append(f"| {name} | " + " | ".join(
                f"{statistics.fmean(r['per_chapter'].get(c, float('nan')) for r in v['runs']):+.2f}"
                for c in chapters) + " |")
    path.write_text("\n".join(lines) + "\n")


# --- driver + report ----------------------------------------------------------------


def analyse(bp: Blueprint, decls: dict[str, FormalDecl], llm_dir: Path | None = None, seed: int = 0) -> dict:
    fg = formal_graph(decls)
    join = join_blueprint(bp, decls)
    formalised = [n.id for n in bp.nodes if n.id in join.node_decls]
    lean_g = projected_graph(bp, fg, join).subgraph(formalised).copy()
    positives = {d for ds in join.node_decls.values() for d in ds}
    key = evaluate_key_nodes(decls, fg, positives, seed)
    clustering, labels = evaluate_chapter_clustering(bp, join, decls, lean_g, seed)
    ordering = evaluate_orders(bp, decls, fg, join, lean_g, labels["Lean module of the node's declaration"],
                               llm_dir, seed)
    return {"key_nodes": key, "clustering": clustering, "ordering": ordering}


def write_report(res: dict, out_dir: Path, project: str, provenance: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "phase2.json").write_text(json.dumps({"project": project, "provenance": provenance, **res}, indent=2))
    k = res["key_nodes"]
    lines = [
        f"# Phase 2: {project}",
        "",
        f"*{provenance}*",
        "",
        "## (c) Which Lean declarations become blueprint nodes?",
        "",
        f"{k['n_positive']} of {k['n_decls']} project declarations are named in the blueprint "
        f"(base rate {k['base_rate']:.0%}). Precision@k uses k = {k['n_positive']}; "
        f"random P@k = {k['random_p_at_k']:.0%}.",
        "",
        "| Score | AUROC | P@k |",
        "|---|---:|---:|",
    ]
    for name, m in sorted(k["single"].items(), key=lambda kv: -abs(kv[1]["auroc"] - 0.5)):
        lines.append(f"| {name} | {m['auroc']:.2f} | {m['p_at_k']:.0%} |")
    for label, c in k["combined"].items():
        lines.append(f"| **Logistic regression, {label}** (5-fold, Lean modules held out) | **{c['auroc']:.2f}** | "
                     f"**{c['p_at_k']:.0%}** |")
    c = k["combined"]["+ variant-of features"]
    lines += [
        "",
        f"Average precision of the full combined score: {c['average_precision']:.2f}. AUROC below 0.5 means the "
        "score points the other way (e.g. heavily used declarations are *less* likely to be named).",
        "",
        "Coefficients (standardised log features): "
        + ", ".join(f"{n} {w:+.2f}" for n, w in sorted(c["coefficients"].items(), key=lambda kv: -abs(kv[1]))),
        "",
        "Highest-scoring declarations the blueprint does **not** name: "
        + ", ".join(f"`{v}`" for v in k["top_unlabelled"][:10]) + ".",
        "",
        "Lowest-scoring declarations it **does** name: " + ", ".join(f"`{v}`" for v in k["bottom_labelled"][:10]) + ".",
        "",
        "## (a) Recovering chapters from the Lean graph",
        "",
        "| Method | clusters | ARI | NMI |",
        "|---|---:|---:|---:|",
    ]
    for name, m in res["clustering"].items():
        lines.append(f"| {name} | {m['clusters']:.0f} | {m['ari']:.2f} | {m['nmi']:.2f} |")
    o = res["ordering"]
    lines += [
        "",
        "## (b) Ordering",
        "",
        "τ = Kendall rank correlation with the human blueprint order (1 = identical). *Within chapters* averages τ "
        "over chapters with at least 8 nodes. Mean open is the working-memory proxy from Phase 0 (lower is better), "
        "on Lean-derived edges.",
        "",
        "| Order | τ whole | τ within chapters | mean open | forward refs | chapter runs |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, m in o["orders"].items():
        lines.append(f"| {name} | {m['tau_whole']:+.2f} | {m['tau_within_chapters']:+.2f} | {m['mean_open']:.1f} | "
                     f"{m['forward_refs']:.0f} | {m['chapter_runs']:.0f} |")
    names = list(next(iter(o["per_chapter_tau"].values())).keys())
    lines += ["", "Per-chapter τ with the human order:", "",
              "| Chapter | " + " | ".join(names[1:]) + " |", "|---|" + "---:|" * (len(names) - 1)]
    for ch, taus in o["per_chapter_tau"].items():
        lines.append(f"| {ch} | " + " | ".join(f"{taus[n]:+.2f}" for n in names[1:]) + " |")
    if o.get("llm"):
        llm = o["llm"]
        lines += ["", f"LLM responses for {len(llm['chapters_answered'])} chapters; constraint violations repaired: "
                  f"{llm['constraint_violations_repaired']}; invalid: {llm['invalid_responses'] or 'none'}."]
    lines.append("")
    (out_dir / "phase2.md").write_text("\n".join(lines))
