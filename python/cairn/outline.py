"""Blueprint-free outlines: from a Lean dependency dump to a readable plan of the development.

Pipeline (no blueprint needed at inference time):

1. **Select** which declarations become named results. The ``detail`` parameter is the share of
   declarations to surface, ranked by a key-declaration model trained on *other* projects' blueprints
   (:class:`KeyModel`). Optionally the project definitions that named statements mention are added,
   so every statement can be read.
2. **Fold** every other declaration into the proofs that use it: the named graph is the Lean graph
   projected through unnamed helpers, and each result records the helpers its proof absorbs.
3. **Group** named results into chapters by Lean module or by graph community.
4. **Order** chapters topologically and arrange each one with a :class:`cairn.style.Style`.
5. **Render** a markdown outline: state/prove steps with Lean statements and docstrings.
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

import networkx as nx
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from .events import P, S, node_of
from .formal import FormalDecl, formal_graph, projections
from .graph import make_dag
from .phase2 import key_node_features, key_node_matrix, lean_source_order
from .style import Style, arrange_document

DEFAULT_STYLE = Style()

# --- key-declaration model ---------------------------------------------------------------------


@dataclass
class KeyModel:
    """Logistic regression on log-scaled key-declaration features, storable as JSON."""

    cols: list[str]
    mean: list[float]
    scale: list[float]
    coef: list[float]
    intercept: float
    trained_on: list[str] = field(default_factory=list)

    @classmethod
    def fit(cls, projects: dict[str, tuple]) -> KeyModel:
        """``projects``: name -> (blueprint, decls). Labels are the blueprint's ``\\lean{}`` declarations."""
        xs, ys, cols = [], [], None
        for bp, decls in projects.values():
            _, x, y, cols = key_node_matrix(bp, decls)
            xs.append(x)
            ys.append(y)
        x, y = np.vstack(xs), np.concatenate(ys)
        scaler = StandardScaler().fit(x)
        lr = LogisticRegression(class_weight="balanced", max_iter=2000).fit(scaler.transform(x), y)
        return cls(cols, scaler.mean_.tolist(), scaler.scale_.tolist(), lr.coef_[0].tolist(),
                   float(lr.intercept_[0]), sorted(projects))

    def score(self, decls: dict[str, FormalDecl], fg: nx.DiGraph | None = None) -> dict[str, float]:
        fg = fg if fg is not None else formal_graph(decls)
        feats = key_node_features(decls, fg)
        names = sorted(fg.nodes)
        x = np.array([[feats[v][c] for c in self.cols] for v in names], dtype=float)
        x = (np.sign(x) * np.log1p(np.abs(x)) - np.array(self.mean)) / np.array(self.scale)
        z = x @ np.array(self.coef) + self.intercept
        return dict(zip(names, (1 / (1 + np.exp(-z))).tolist(), strict=True))

    def save(self, path: Path) -> None:
        Path(path).write_text(json.dumps(asdict(self), indent=1))

    @classmethod
    def load(cls, path: Path) -> KeyModel:
        return cls(**json.loads(Path(path).read_text()))


# --- selection and folding -----------------------------------------------------------------------


_BOILERPLATE_CLASSES = {"Decidable", "DecidablePred", "DecidableRel", "DecidableEq", "Inhabited", "Repr", "ToString",
                        "Hashable", "BEq", "Coe", "CoeFun", "CoeSort", "CoeOut", "CoeTC", "CoeHead", "CoeTail",
                        "FunLike", "DFunLike", "SetLike", "EquivLike", "Unique", "Nonempty", "Subsingleton"}


def is_boilerplate_instance(d: FormalDecl) -> bool:
    """An auto-named instance (``instDecidablePred…``) of a plumbing class: decidability, coercions, printing.

    Such instances are never presented as results. Instances of mathematical classes (``instModule``,
    ``instIsZLatticeE8Lattice``) stay eligible: blueprints do name those.
    """
    if not re.match(r"inst[A-Z0-9]", d.name.split(".")[-1]) or d.kind == "theorem":
        return False
    depth, cut = 0, 0
    stmt = d.stmt_short or ""
    for i, ch in enumerate(stmt):  # the conclusion follows the last top-level " : "
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if depth == 0 and stmt.startswith(" : ", i):
            cut = i + 3
    head = stmt[cut:].split(" ")[0].split(".")[-1]
    return head in _BOILERPLATE_CLASSES


def select(decls: dict[str, FormalDecl], fg: nx.DiGraph, scores: dict[str, float], detail: float = 0.15,
           count: int | None = None, roots: list[str] | None = None, define_used: bool = True,
           modules: list[str] | None = None) -> set[str]:
    """Declarations to present as named results (restricted to modules under ``modules`` prefixes)."""
    universe = set(fg.nodes)
    if modules:
        universe = {v for v in universe if any(decls[v].module == m or decls[v].module.startswith(m + ".")
                                               for m in modules)}
    if roots:
        missing = [r for r in roots if r not in fg]
        if missing:
            raise KeyError(f"unknown root declarations: {missing}")
        universe &= set(roots).union(*(nx.ancestors(fg, r) for r in roots))
    universe = {v for v in universe if not is_boilerplate_instance(decls[v])}
    ranked = sorted(universe, key=lambda v: (-scores.get(v, 0.0), v))
    k = count if count is not None else max(1, round(detail * len(universe)))
    named = set(ranked[:k]) | set(roots or [])
    if define_used:  # make every named statement readable: add the project definitions it mentions
        frontier = list(named)
        while frontier:
            v = frontier.pop()
            for u in decls[v].type_deps:
                if u in universe and u not in named and decls[u].kind != "theorem":
                    named.add(u)
                    frontier.append(u)
    # A structure's field projections (`DualPair.v`) are presented with the structure, not as results of their own.
    proj = {p: s for p, s in projections(decls).items() if s in universe}
    return {proj.get(v, v) for v in named}


def fold(fg: nx.DiGraph, named: set[str]) -> tuple[nx.DiGraph, dict[str, list[str]]]:
    """Project ``fg`` onto ``named`` through unnamed helpers; also return each result's absorbed helpers."""
    g = nx.DiGraph()
    g.add_nodes_from(named)
    absorbed: dict[str, list[str]] = {}
    for v in named:
        seen: set[str] = set()
        stack = list(fg.predecessors(v))
        helpers = []
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            if u in named:
                if u != v:  # folding generated companions can make a declaration reach itself
                    g.add_edge(u, v)
                continue
            helpers.append(u)
            stack.extend(fg.predecessors(u))
        absorbed[v] = sorted(helpers)
    return g, absorbed


def chapters_for(named: set[str], g: nx.DiGraph, decls: dict[str, FormalDecl], how: str = "module",
                 seed: int = 0) -> dict[str, str]:
    if how == "module":
        return {v: decls[v].module for v in named}
    if how == "community":
        comms = nx.community.greedy_modularity_communities(g.to_undirected()) if g.number_of_edges() else [named]
        out = {}
        for c in comms:
            label = Counter(decls[v].module for v in c).most_common(1)[0][0]
            for v in c:
                out[v] = label
        # disambiguate communities sharing a majority module
        seen: Counter = Counter()
        relabel = {}
        for c in comms:
            lab = out[next(iter(c))]
            seen[lab] += 1
            relabel[id(c)] = lab if seen[lab] == 1 else f"{lab} ({seen[lab]})"
        return {v: relabel[id(c)] for c in comms for v in c}
    raise ValueError("chapters must be 'module' or 'community'")


# --- the outline ----------------------------------------------------------------------------------


@dataclass
class Outline:
    order: list[str]
    chapter: dict[str, str]
    chapter_order: list[str]
    graph: nx.DiGraph
    absorbed: dict[str, list[str]]
    named: set[str]
    scores: dict[str, float]


def build(decls: dict[str, FormalDecl], scores: dict[str, float], style: Style = DEFAULT_STYLE, detail: float = 0.15,
          count: int | None = None, roots: list[str] | None = None, chapters: str = "module",
          define_used: bool = True, modules: list[str] | None = None, seed: int = 0) -> Outline:
    fg = formal_graph(decls)
    named = select(decls, fg, scores, detail, count, roots, define_used, modules)
    full, absorbed = fold(fg, named)
    statement, _ = fold(formal_graph(decls, include_value=False), named)
    chapter = chapters_for(named, full, decls, chapters, seed)

    ev = nx.DiGraph()
    for v in named:
        kind = "definition" if decls[v].kind != "theorem" else "theorem"
        ev.add_node(S(v), chapter=chapter[v], kind="statement", result=kind)
        if kind == "theorem":
            ev.add_node(P(v), chapter=chapter[v], kind="proof")
            ev.add_edge(S(v), P(v))
    for u, v in full.edges:
        if statement.has_edge(u, v) or P(v) not in ev:
            ev.add_edge(S(u), S(v))
        else:
            ev.add_edge(S(u), P(v))

    # chapters in dependency order, ties broken by where the Lean sources put them
    src = {d: i for i, d in enumerate(lean_source_order(decls, fg))}
    q = nx.DiGraph()
    q.add_nodes_from(set(chapter.values()))
    q.add_edges_from((chapter[u], chapter[v]) for u, v in full.edges if chapter[u] != chapter[v])
    first = {c: min(src[v] for v in named if chapter[v] == c) for c in q}
    cond = nx.condensation(q)
    chapter_order = [c for comp in nx.lexicographical_topological_sort(
        cond, key=lambda n: min(first[c] for c in cond.nodes[n]["members"]))
        for c in sorted(cond.nodes[comp]["members"], key=first.__getitem__)]

    reference = sorted(ev, key=lambda e: (src[node_of(e)], e[0] == "P"))
    dag, _ = make_dag(ev, reference)
    order = arrange_document(dag, chapter_order, style, random.Random(seed))
    return Outline(order, chapter, chapter_order, dag, absorbed, named, scores)


def _short(text: str, n: int = 400) -> str:
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1] + "…"


def render(o: Outline, decls: dict[str, FormalDecl], title: str, style: Style, detail_note: str,
           prose: dict[str, dict] | None = None) -> str:
    """Markdown outline. With ``prose`` (see :mod:`cairn.prose`), chapters get titles, results an English
    statement next to the Lean one, and proofs a sketch; translations a checker flagged are marked."""
    from .prose import helpers_of, open_namespaces, statement_of, uses_of

    prose = prose or {}
    nss = open_namespaces(o.named)
    pos = {e: i for i, e in enumerate(o.order)}
    lines = [f"# {title}", "",
             f"*Generated by Cairn from Lean declarations only. Style: {style.label()}. {detail_note} "
             f"Statements show explicit hypotheses only, with namespaces {', '.join(nss)} open.*"]
    if prose:
        lines.append("*Chapter titles, English statements and proof sketches are LLM-written; each sits next to "
                     "its verified Lean statement, and ⚠ marks translations a second reader flagged.*")
    lines.append("")
    current = None
    k = 0
    for e in o.order:
        v = node_of(e)
        ch = o.chapter[v]
        text = prose.get(ch, {})
        entry = text.get("results", {}).get(v, {})
        if ch != current:
            current = ch
            k += 1
            heading = text.get("title")
            lines += ["", f"## {k}. {heading}" if heading else f"## {k}. `{ch}`", ""]
            if heading:
                lines += [f"*Lean module `{ch}`*", ""]
        d = decls[v]
        kind = "Definition" if d.kind != "theorem" else "Theorem"
        if e.startswith("S:"):
            deferred = P(v) in pos and pos[P(v)] - pos[e] > 1
            tag = " *(proof deferred)*" if deferred else ""
            if entry.get("statement"):
                lines.append(f"- **{kind}** (`{v}`){tag}. {entry['statement']}")
                if entry.get("faithful") is False:
                    lines.append(f"  ⚠ *Translation flagged: {entry.get('issue') or 'see the Lean statement'}*")
                if statement_of(d, nss):
                    lines.append(f"  <br>Lean: `{_short(statement_of(d, nss), 300)}`")
            else:
                lines.append(f"- **{kind}** `{v}`{tag}")
                if statement_of(d, nss):
                    lines.append(f"  `{_short(statement_of(d, nss))}`")
                if d.doc:
                    lines.append(f"  — {_short(d.doc, 300)}")
        else:
            uses = uses_of(o, v)
            helpers = helpers_of(o, v)
            note = []
            if pos[e] - pos[S(v)] > 1:
                note.append("stated above")
            if uses:
                note.append("uses " + ", ".join(f"`{u}`" for u in uses[:8]) + (" …" if len(uses) > 8 else ""))
            if helpers:
                note.append(f"folds in {len(helpers)} helper lemma{'s' if len(helpers) != 1 else ''}"
                            + (": " + ", ".join(f"`{h}`" for h in helpers[:5]) + (" …" if len(helpers) > 5 else "")))
            if entry.get("sketch"):
                lines.append(f"- *Proof of* `{v}`. {entry['sketch']}" + (f" <br>*({'; '.join(note)})*" if note else ""))
            else:
                lines.append(f"- *Proof of* `{v}`" + (f" — {'; '.join(note)}" if note else ""))
    return "\n".join(lines) + "\n"


# --- evaluation against a blueprint (the blueprint is used only here) ------------------------------


def evaluate(bp, decls: dict[str, FormalDecl], scores: dict[str, float], style: Style,
             details=(0.05, 0.1, 0.15, 0.2, 0.3), chapters: str = "module", modules: list[str] | None = None,
             min_chapter: int = 8, define_used: bool = True) -> list[dict]:
    """How close blueprint-free outlines come to the human blueprint, per ``detail``."""
    import statistics

    from sklearn.metrics import normalized_mutual_info_score

    from .formal import join_blueprint
    from .graph import kendall_tau

    join = join_blueprint(bp, decls)
    by_id = bp.by_id()
    owner: dict[str, str] = {}
    for node, ds in join.node_decls.items():
        for d in ds:
            owner.setdefault(d, node)
    fg = formal_graph(decls)
    universe = {v for v in fg if not modules or any(decls[v].module.startswith(m) for m in modules)}
    positives = set(owner) & universe
    rows = []
    for detail in details:
        o = build(decls, scores, style, detail, chapters=chapters, define_used=define_used, modules=modules)
        named = o.named
        hit = named & positives
        pos_of = {node_of(e): i for i, e in enumerate(o.order) if e.startswith("S:")}
        node_pos: dict[str, int] = {}
        for d in hit:
            node_pos[owner[d]] = min(node_pos.get(owner[d], 10**9), pos_of[d])
        covered = sorted(node_pos, key=lambda n: by_id[n].statement_event)
        outline_order = sorted(covered, key=node_pos.__getitem__)
        within = []
        for ch in dict.fromkeys(by_id[n].chapter for n in covered):
            h = [n for n in covered if by_id[n].chapter == ch]
            if len(h) >= min_chapter:
                within.append(kendall_tau(h, [n for n in outline_order if by_id[n].chapter == ch]))
        first_decl = {n: min((d for d in hit if owner[d] == n), key=pos_of.__getitem__) for n in covered}
        theorems = {v for v in named if decls[v].kind == "theorem"}
        rows.append({
            "detail": detail,
            "named": len(named),
            "named_theorems": len(theorems),
            "precision": len(hit) / len(named),
            "theorem_precision": len(hit & theorems) / max(len(theorems), 1),
            "recall": len(hit) / len(positives),
            "node_coverage": len(covered) / len(join.node_decls),
            "chapter_nmi": float(normalized_mutual_info_score(
                [by_id[n].chapter for n in covered], [o.chapter[first_decl[n]] for n in covered])),
            "tau_whole": kendall_tau(covered, outline_order),
            "tau_within_chapters": statistics.fmean(within) if within else float("nan"),
            "chapters": len(o.chapter_order),
        })
    return rows
