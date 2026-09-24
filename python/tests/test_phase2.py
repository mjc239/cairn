import json
import random

import networkx as nx

from cairn.formal import FormalDecl
from cairn.phase2 import cluster_then_order, dominator_subtree_sizes, lean_source_order, load_llm_orders


def test_dominator_subtree_sizes():
    # top uses m; m uses a and b; b uses c. Everything below m is only reachable through m.
    fg = nx.DiGraph([("m", "top"), ("a", "m"), ("b", "m"), ("c", "b")])
    sizes = dominator_subtree_sizes(fg)
    assert sizes == {"top": 4, "m": 3, "b": 1, "a": 0, "c": 0}


def test_lean_source_order_respects_modules_then_lines():
    decls = {
        "B.x": FormalDecl("B.x", "theorem", "M.B", 1),
        "A.y": FormalDecl("A.y", "theorem", "M.A", 9),
        "A.z": FormalDecl("A.z", "theorem", "M.A", 3),
    }
    fg = nx.DiGraph([("A.y", "B.x")])  # M.B imports M.A
    fg.add_node("A.z")
    assert lean_source_order(decls, fg) == ["A.z", "A.y", "B.x"]


def test_cluster_then_order_keeps_clusters_contiguous():
    g = nx.DiGraph([("a1", "a2"), ("a2", "b1"), ("b1", "b2"), ("a1", "b2")])
    clusters = {"a1": "A", "a2": "A", "b1": "B", "b2": "B"}
    order = cluster_then_order(g, clusters, random.Random(0))
    assert order == ["a1", "a2", "b1", "b2"]


def test_load_llm_orders_repairs_and_rejects(tmp_path):
    dag = nx.DiGraph([("x", "y")])
    dag.add_node("z")
    human = ["x", "y", "z"]
    chapter = {"x": "c1", "y": "c1", "z": "c2"}
    (tmp_path / "c1.response.json").write_text(json.dumps(["y", "x"]))  # violates x before y
    (tmp_path / "c2.response.json").write_text(json.dumps(["z", "extra"]))  # wrong id set
    res = load_llm_orders(tmp_path, human, chapter, dag)
    assert res["order"] == ["x", "y", "z"]
    assert res["constraint_violations_repaired"] == {"c1": 1}
    assert res["invalid_responses"] == ["c2"]
