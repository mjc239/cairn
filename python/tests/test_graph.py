import random

import networkx as nx
import pytest

from cairn.graph import (
    goal_first_order,
    greedy_min_open_order,
    just_in_time_order,
    kendall_tau,
    local_search_order,
    make_dag,
    nearest_topological_order,
    order_metrics,
    random_topological_order,
)


def path_plus_hub():
    # a -> b -> c -> d, and a -> d
    g = nx.DiGraph([("a", "b"), ("b", "c"), ("c", "d"), ("a", "d")])
    return g


def test_metrics_on_known_order():
    g = path_plus_hub()
    m = order_metrics(g, ["a", "b", "c", "d"])
    # gaps: a|b crosses a-b, a-d; b|c crosses b-c, a-d; c|d crosses c-d, a-d
    assert m.cutwidth == 2 and m.mean_cut == 2
    assert m.forward_refs == 0
    # open sets: after a {a}; after b {a,b}; after c {a,c}
    assert m.max_open == 2 and m.mean_open == pytest.approx(5 / 3)
    assert m.mean_edge_length == pytest.approx((1 + 1 + 1 + 3) / 4)


def test_forward_refs_counted():
    g = path_plus_hub()
    assert order_metrics(g, ["b", "a", "c", "d"]).forward_refs == 1


def test_kendall_tau():
    assert kendall_tau(list("abcd"), list("abcd")) == 1
    assert kendall_tau(list("abcd"), list("dcba")) == -1


def is_topological(g, order):
    pos = {v: i for i, v in enumerate(order)}
    return sorted(order) == sorted(g.nodes) and all(pos[u] < pos[v] for u, v in g.edges)


@pytest.mark.parametrize("seed", range(5))
def test_orders_are_topological(seed):
    g = nx.gnp_random_graph(40, 0.08, seed=seed, directed=True)
    g = nx.DiGraph([(u, v) for u, v in g.edges if u < v])
    g.add_nodes_from(range(40))
    g = nx.relabel_nodes(g, str)
    rng = random.Random(seed)
    for order in (
        random_topological_order(g, rng),
        just_in_time_order(g, rng),
        greedy_min_open_order(g, rng),
    ):
        assert is_topological(g, order)
        improved = local_search_order(g, order)
        assert is_topological(g, improved)
        assert order_metrics(g, improved).mean_cut <= order_metrics(g, order).mean_cut


def test_make_dag_and_nearest_order():
    g = nx.DiGraph([("a", "b"), ("b", "a"), ("b", "c")])
    dag, dropped = make_dag(g, ["a", "b", "c"])
    assert dropped == [("b", "a")]
    assert nearest_topological_order(dag, ["c", "b", "a"]) == ["a", "b", "c"]
    h = nx.DiGraph([("x", "y")])
    h.add_node("z")
    assert nearest_topological_order(h, ["z", "y", "x"]) == ["z", "x", "y"]


def test_uniform_orders_cover_antichain_evenly():
    from collections import Counter

    from cairn.graph import uniform_topological_orders

    g = nx.DiGraph()
    g.add_nodes_from("abc")
    g.add_edge("x", "c")  # x before c; 4!/2 = 12 linear extensions
    samples = uniform_topological_orders(g, ["a", "b", "x", "c"], 2400, random.Random(1), thin=20)
    counts = Counter(tuple(o) for o in samples)
    assert all(is_topological(g, list(o)) for o in counts)
    assert len(counts) == 12
    assert max(counts.values()) < 2 * min(counts.values())


def test_metrics_are_reversal_invariant():
    # Top-down (goal-first) and bottom-up presentations of the same order are charged the same load,
    # so bottom-up null models are fair to top-down blueprints.
    g = nx.gnp_random_graph(30, 0.1, seed=4, directed=True)
    g = nx.relabel_nodes(nx.DiGraph([(u, v) for u, v in g.edges if u < v]), str)
    order = random_topological_order(g, random.Random(0))
    a, b = order_metrics(g, order), order_metrics(g, order[::-1])
    assert (a.cutwidth, a.mean_cut, a.max_open, a.mean_open, a.mean_edge_length) == (
        b.cutwidth, b.mean_cut, b.max_open, b.mean_open, b.mean_edge_length)
    assert b.forward_refs == g.number_of_edges()


def test_goal_first_order_is_top_down():
    g = nx.DiGraph([("a", "b"), ("b", "c"), ("a", "c"), ("d", "c")])
    for seed in range(5):
        order = goal_first_order(g, random.Random(seed))
        assert order[0] == "c"
        pos = {v: i for i, v in enumerate(order)}
        # every non-final result appears after at least one result that uses it
        assert all(any(pos[w] < pos[v] for w in g.successors(v)) for v in g if g.out_degree(v))


def test_event_styles_and_motivation():
    from cairn.events import P, S, bottom_up_order, deferred_goal_first_order, motivated_share

    # goal g's proof uses lemmas a and b; b's proof uses a
    g = nx.DiGraph([(S("g"), P("g")), (S("a"), P("a")), (S("b"), P("b")),
                    (S("a"), P("g")), (S("b"), P("g")), (S("a"), P("b"))])
    rng = random.Random(0)
    td = deferred_goal_first_order(g, rng)
    bu = bottom_up_order(g, rng)
    for order in (td, bu):
        pos = {e: i for i, e in enumerate(order)}
        assert sorted(order) == sorted(g) and all(pos[u] < pos[v] for u, v in g.edges)
    assert td[0] == S("g") and td[-1] == P("g")
    assert bu[-2:] == [S("g"), P("g")]
    assert motivated_share(g, td) == 1.0
    assert motivated_share(g, bu) == 0.0


def test_hybrid_order_interpolates_styles():
    from cairn.events import P, S, goals_by_fan_in, hybrid_order, motivated_share

    g = nx.DiGraph([(S("g"), P("g")), (S("a"), P("a")), (S("b"), P("b")),
                    (S("a"), P("g")), (S("b"), P("g")), (S("a"), P("b"))])
    assert goals_by_fan_in(g, 2) == {"g"}
    order = hybrid_order(g, {"g"}, random.Random(0))
    pos = {e: i for i, e in enumerate(order)}
    assert all(pos[u] < pos[v] for u, v in g.edges)
    assert order[0] == S("g") and order[-1] == P("g")
    assert order[1:3] == [S("a"), P("a")]  # a is not a goal: stated and proved together, bottom-up
    assert motivated_share(g, hybrid_order(g, set(), random.Random(0))) == 0.0


def _toy_chapter():
    from cairn.events import P, S

    # definition d; lemmas a, b; main result g whose proof uses a and b; b's proof uses a; a's statement uses d
    g = nx.DiGraph([(S("g"), P("g")), (S("a"), P("a")), (S("b"), P("b")),
                    (S("a"), P("g")), (S("b"), P("g")), (S("a"), P("b")), (S("d"), S("a"))])
    g.nodes[S("d")]["result"] = "definition"
    return g


@pytest.mark.parametrize("top_down", [0, 0.5, 1])
@pytest.mark.parametrize("roadmap", ["none", "chapter"])
@pytest.mark.parametrize("definitions", ["just-in-time", "upfront"])
def test_arrange_is_always_valid(top_down, roadmap, definitions):
    from cairn.style import Style, arrange

    g = _toy_chapter()
    for seed in range(3):
        order = arrange(g, Style(top_down, roadmap, definitions), random.Random(seed))
        pos = {e: i for i, e in enumerate(order)}
        assert sorted(order) == sorted(g) and all(pos[u] < pos[v] for u, v in g.edges)


def test_style_parameters_do_what_they_say():
    from cairn.events import P, S, motivated_share
    from cairn.style import Style, arrange

    g = _toy_chapter()
    rng = random.Random(0)
    assert motivated_share(g, arrange(g, Style(0), rng)) == 0.0
    assert arrange(g, Style(0, roadmap="chapter"), rng)[0] == S("g")  # main result announced first ...
    assert arrange(g, Style(0, roadmap="chapter"), rng)[-1] == P("g")  # ... and proved last
    assert arrange(g, Style(1), rng)[0] == S("g")
    assert arrange(g, Style(0, definitions="upfront"), rng)[0] == S("d")


def test_open_swap_delta_is_exact_and_local_search_improves_mean_open():
    from cairn.graph import _open_swap_delta, local_search_order, order_metrics, random_topological_order

    rng = random.Random(3)
    for t in range(25):
        n = rng.randint(4, 30)
        raw = nx.gnp_random_graph(n, 0.2, seed=t, directed=True)
        g = nx.DiGraph([(f"n{u}", f"n{v}") for u, v in raw.edges if u < v])
        g.add_nodes_from(f"n{i}" for i in range(n))
        order = random_topological_order(g, rng)
        total = order_metrics(g, order).mean_open * (n - 1)
        preds = {v: list(g.predecessors(v)) for v in g}
        succs = {v: set(g.successors(v)) for v in g}
        pos = {v: i for i, v in enumerate(order)}
        last = {v: max(pos[w] for w in succs[v]) for v in g if succs[v]}
        for k in range(n - 1):
            a, b = order[k], order[k + 1]
            if g.has_edge(a, b):
                continue
            swapped = order[:k] + [b, a] + order[k + 2 :]
            brute = order_metrics(g, swapped).mean_open * (n - 1) - total
            assert abs(_open_swap_delta(preds, succs, pos, last, a, b) - brute) < 1e-9
        better = local_search_order(g, order, objective="open")
        p = {v: i for i, v in enumerate(better)}
        assert all(p[u] < p[v] for u, v in g.edges)
        assert order_metrics(g, better).mean_open <= order_metrics(g, order).mean_open + 1e-9
