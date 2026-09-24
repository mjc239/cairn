"""Dependency graphs, linear arrangements and their readability metrics.

Edges point from prerequisite to dependent (``u -> v``: ``v`` uses ``u``). An
*order* is a list of every node. A topological order has no forward references.
"""

from __future__ import annotations

import random
from dataclasses import asdict, dataclass

import networkx as nx

from .blueprint import Blueprint


def dependency_graph(bp: Blueprint, kinds: tuple[str, ...] = ("statement", "proof")) -> nx.DiGraph:
    g = nx.DiGraph()
    for n in bp.nodes:
        g.add_node(n.id, kind=n.kind, chapter=n.chapter, position=n.position)
    for u, v, kind in bp.edges(kinds):
        g.add_edge(u, v, kind=kind)
    return g


def make_dag(g: nx.DiGraph, human_order: list[str]) -> tuple[nx.DiGraph, list[tuple[str, str]]]:
    """Break cycles by dropping forward references (in ``human_order``) inside strongly connected components.

    Every remaining edge inside an SCC then points backwards in the human order, so the result is acyclic.
    """
    pos = {v: i for i, v in enumerate(human_order)}
    dropped = []
    for scc in nx.strongly_connected_components(g):
        if len(scc) < 2:
            continue
        for u, v in list(g.subgraph(scc).edges):
            if pos[u] > pos[v]:
                dropped.append((u, v))
    dropped += [(u, v) for u, v in g.edges if u == v]  # self-loops are never meaningful dependencies
    dag = g.copy()
    dag.remove_edges_from(dropped)
    assert nx.is_directed_acyclic_graph(dag)
    return dag, dropped


# --- metrics ---------------------------------------------------------------


@dataclass
class OrderMetrics:
    n: int
    forward_refs: int
    cutwidth: int
    """Max, over gaps between consecutive nodes, of dependency edges crossing that gap."""
    mean_cut: float
    """Mean edges crossing a gap; equals total edge length / (n - 1)."""
    max_open: int
    """Max number of results "held open" at a gap: stated earlier and still needed later
    (or, for forward references, promised earlier and not yet stated). The vertex separation number."""
    mean_open: float
    mean_edge_length: float

    def as_dict(self) -> dict:
        return asdict(self)


def _profile(intervals: list[tuple[int, int]], n: int) -> list[int]:
    """How many half-open ``[lo, hi)`` gap intervals cover each of the ``n - 1`` gaps."""
    diff = [0] * n
    for lo, hi in intervals:
        if hi > lo:
            diff[lo] += 1
            diff[hi] -= 1
    out, running = [], 0
    for i in range(n - 1):
        running += diff[i]
        out.append(running)
    return out


def order_metrics(g: nx.DiGraph, order: list[str]) -> OrderMetrics:
    n = len(order)
    if n < 2:
        return OrderMetrics(n, 0, 0, 0.0, 0, 0.0, 0.0)
    pos = {v: i for i, v in enumerate(order)}
    edges = [(pos[u], pos[v]) for u, v in g.edges]
    forward = sum(1 for pu, pv in edges if pu > pv)
    cut = _profile([(min(a, b), max(a, b)) for a, b in edges], n)
    spans = []
    for v in g.nodes:
        touched = [pos[v], *(pos[w] for w in g.successors(v))]
        spans.append((min(touched), max(touched)))
    open_ = _profile(spans, n)
    lengths = [abs(a - b) for a, b in edges]
    return OrderMetrics(
        n=n,
        forward_refs=forward,
        cutwidth=max(cut),
        mean_cut=sum(cut) / (n - 1),
        max_open=max(open_),
        mean_open=sum(open_) / (n - 1),
        mean_edge_length=sum(lengths) / len(lengths) if lengths else 0.0,
    )


def kendall_tau(a: list[str], b: list[str]) -> float:
    """Kendall rank correlation between two orders of the same nodes."""
    pb = {v: i for i, v in enumerate(b)}
    seq = [pb[v] for v in a]
    n = len(seq)
    if n < 2:
        return 1.0
    discordant = sum(1 for i in range(n) for j in range(i + 1, n) if seq[i] > seq[j])
    pairs = n * (n - 1) // 2
    return 1 - 2 * discordant / pairs


# --- orders ----------------------------------------------------------------


def random_topological_order(g: nx.DiGraph, rng: random.Random) -> list[str]:
    """Randomised Kahn's algorithm: pick uniformly among the currently available nodes.

    Not uniform over all linear extensions (it favours orders that start "wide"), but a
    standard, cheap null model.
    """
    indeg = {v: g.in_degree(v) for v in g.nodes}
    ready = sorted(v for v, d in indeg.items() if d == 0)
    order = []
    while ready:
        v = ready.pop(rng.randrange(len(ready)))
        order.append(v)
        for w in g.successors(v):
            indeg[w] -= 1
            if indeg[w] == 0:
                ready.append(w)
    if len(order) != g.number_of_nodes():
        raise ValueError("graph has a cycle")
    return order


def uniform_topological_orders(
    g: nx.DiGraph, start: list[str], samples: int, rng: random.Random, thin: int | None = None
) -> list[list[str]]:
    """Approximately uniform linear extensions via the Karzanov–Khachiyan chain.

    Lazy adjacent transpositions: pick a gap, swap its two nodes with probability 1/2 unless an
    edge joins them. The chain is symmetric, so its stationary distribution is uniform over
    topological orders; mixing takes O(n^3 log n) steps, so ``thin`` (default ``4 n^2``) trades
    exactness for speed. ``start`` must be topological.
    """
    order = list(start)
    n = len(order)
    if n < 2:
        return [order] * samples
    thin = thin or 4 * n * n
    succ = {v: set(g.successors(v)) for v in g.nodes}

    def run(steps: int) -> None:
        for _ in range(steps):
            i = rng.randrange(n - 1)
            if rng.random() < 0.5:
                a, b = order[i], order[i + 1]
                if b not in succ[a]:
                    order[i], order[i + 1] = b, a

    run(10 * thin)  # burn-in
    out = []
    for _ in range(samples):
        run(thin)
        out.append(list(order))
    return out


def nearest_topological_order(g: nx.DiGraph, reference: list[str]) -> list[str]:
    """The topological order that follows ``reference`` as closely as possible
    (lexicographically smallest by reference position): forward references are
    repaired by pulling prerequisites up to just where they are first needed."""
    pos = {v: i for i, v in enumerate(reference)}
    return list(nx.lexicographical_topological_sort(g, key=pos.__getitem__))


def just_in_time_order(g: nx.DiGraph, rng: random.Random) -> list[str]:
    """Goal-directed DFS: for each sink (final result) in random order, emit its
    unmet prerequisites depth-first, each just before the node that needs it."""
    seen: set[str] = set()
    order: list[str] = []

    def visit(v: str) -> None:
        stack = [(v, iter(_shuffled(g.predecessors(v), rng)))]
        seen.add(v)
        while stack:
            node, preds = stack[-1]
            nxt = next((p for p in preds if p not in seen), None)
            if nxt is None:
                stack.pop()
                order.append(node)
            else:
                seen.add(nxt)
                stack.append((nxt, iter(_shuffled(g.predecessors(nxt), rng))))

    for sink in _shuffled((v for v in g.nodes if g.out_degree(v) == 0), rng):
        visit(sink)
    return order


def goal_first_order(g: nx.DiGraph, rng: random.Random) -> list[str]:
    """Top-down narrative DFS: for each final result in random order, state it, then (depth-first) the
    results it uses that have not appeared yet. Each non-final result appears right after the first result
    that needs it; a lemma shared by siblings can therefore precede a sibling that uses it, so this is not a
    strict reverse-topological order (``just_in_time_order(...)[::-1]`` is)."""
    seen: set[str] = set()
    order: list[str] = []
    for sink in _shuffled((v for v in g.nodes if g.out_degree(v) == 0), rng):
        stack = [sink]
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            order.append(v)
            stack.extend(reversed(_shuffled((p for p in g.predecessors(v) if p not in seen), rng)))
    return order


def _shuffled(items, rng: random.Random) -> list:
    items = sorted(items)
    rng.shuffle(items)
    return items


def greedy_min_open_order(g: nx.DiGraph, rng: random.Random) -> list[str]:
    """Kahn's algorithm choosing, among available nodes, the one that leaves the fewest results open.

    Placing ``v`` closes each prerequisite whose last unplaced dependent is ``v`` and opens ``v``
    itself if anything still depends on it. Ties are broken randomly.
    """
    indeg = {v: g.in_degree(v) for v in g.nodes}
    remaining_out = {v: g.out_degree(v) for v in g.nodes}
    ready = {v for v, d in indeg.items() if d == 0}
    order = []
    while ready:
        def gain(v: str) -> int:
            closes = sum(1 for u in g.predecessors(v) if remaining_out[u] == 1)
            opens = 1 if g.out_degree(v) > 0 else 0
            return opens - closes

        best = min(gain(v) for v in ready)
        v = rng.choice(sorted(v for v in ready if gain(v) == best))
        ready.remove(v)
        order.append(v)
        for u in g.predecessors(v):
            remaining_out[u] -= 1
        for w in g.successors(v):
            indeg[w] -= 1
            if indeg[w] == 0:
                ready.add(w)
    return order


def local_search_order(g: nx.DiGraph, order: list[str], max_sweeps: int = 50) -> list[str]:
    """Improve total edge length (= mean cut) by moving single nodes within their precedence window.

    Each move slides a node past neighbours it has no edge with, accumulating the exact change in
    total length, and keeps the best position found. Stops at a local optimum.
    """
    order = list(order)
    nbrs = {v: set(g.predecessors(v)) | set(g.successors(v)) for v in g.nodes}

    def slide_delta(pos: dict[str, int], x: str, y: str) -> int:
        # x at i moves right past y at i + 1 (no edge between them).
        i = pos[x]
        lx = sum(1 for w in nbrs[x] if pos[w] < i)
        rx = len(nbrs[x]) - lx
        ly = sum(1 for w in nbrs[y] if pos[w] < i)
        ry = len(nbrs[y]) - ly
        return (lx - rx) + (ry - ly)

    for _ in range(max_sweeps):
        improved = False
        for x in list(order):
            pos = {v: i for i, v in enumerate(order)}
            i = pos[x]
            best_delta, best_j = 0, i
            # slide right
            delta, j = 0, i
            p = dict(pos)
            while j + 1 < len(order) and order[j + 1] not in nbrs[x]:
                y = order[j + 1]
                delta += slide_delta(p, x, y)
                p[x], p[y] = j + 1, j
                j += 1
                if delta < best_delta:
                    best_delta, best_j = delta, j
            # slide left (y moves right past x)
            delta, j = 0, i
            p = dict(pos)
            while j - 1 >= 0 and order[j - 1] not in nbrs[x]:
                y = order[j - 1]
                delta += slide_delta(p, y, x)
                p[x], p[y] = j - 1, j
                j -= 1
                if delta < best_delta:
                    best_delta, best_j = delta, j
            if best_j != i:
                order.pop(i)
                order.insert(best_j, x)
                improved = True
        if not improved:
            break
    return order
