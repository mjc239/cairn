import json

import networkx as nx

from cairn.blueprint import Blueprint, Node
from cairn.formal import fold_name, formal_graph, join_blueprint, load_decls, projected_graph


def test_fold_name():
    assert fold_name("PFR.foo._proof_1") == "PFR.foo"
    assert fold_name("PFR.foo.match_2") == "PFR.foo"
    assert fold_name("PFR.foo.eq_1") == "PFR.foo"
    assert fold_name("_private.PFR.Basic.0.PFR.bar._proof_3") == "PFR.bar"
    assert fold_name("PFR.Foo.rec", {"PFR.Foo": "inductive"}) == "PFR.Foo"
    assert fold_name("PFR.Foo.rec", {"PFR.Foo": "def"}) == "PFR.Foo.rec"
    assert fold_name("PFR.Foo.below.cons", {"PFR.Foo": "inductive"}) == "PFR.Foo"
    assert fold_name("«PFR».«a.b»") == "PFR.a.b"


def row(name, kind="theorem", deps=(), user=None, module="P.M", line=1):
    return {"name": name, "user_name": user or name, "private": False, "module": module, "kind": kind,
            "internal": False, "matcher": False, "aux_recursor": False, "line": line,
            "type_deps": [], "value_deps": list(deps)}


def write(tmp_path, rows):
    p = tmp_path / "decls.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows))
    return p


def test_load_folds_auxiliaries(tmp_path):
    p = write(tmp_path, [
        row("P.a"),
        row("P.b", deps=["P.b._proof_1", "Mathlib.x"]),
        row("P.b._proof_1", deps=["P.a"], user="P.b._proof_1"),
        row("P._aux_P_M___unexpand_foo_1", kind="def", deps=["P.a"]),
        row("P.ghost._proof_1", deps=["P.a"]),
    ])
    decls = load_decls(p)
    assert set(decls) == {"P.a", "P.b"}
    assert decls["P.b"].value_deps == {"P.a", "Mathlib.x"}
    g = formal_graph(decls)
    assert list(g.edges) == [("P.a", "P.b")]


def test_projection_passes_through_unlabelled_helpers():
    # a -> helper -> c ; c labelled node "C", a labelled "A"; b labelled but unrelated
    fg = nx.DiGraph([("P.a", "P.helper"), ("P.helper", "P.c"), ("P.b", "P.b2")])
    nodes = [Node(id=i, kind="lemma", position=k, chapter="ch", source="s", line=1, lean_decls=d)
             for k, (i, d) in enumerate([("A", ["P.a"]), ("B", ["P.b", "Mathlib.gone"]), ("C", ["P.c"])])]
    bp = Blueprint(nodes=nodes, unresolved=[], orphan_proofs=[])
    decls = {n: None for n in fg.nodes}
    join = join_blueprint(bp, decls)
    assert join.missing == {"B": ["Mathlib.gone"]}
    pg = projected_graph(bp, fg, join)
    assert set(pg.edges) == {("A", "C")}


def test_compare_edges_classifies():
    from cairn.phase1 import compare_edges

    author = nx.DiGraph([("a", "b"), ("a", "c"), ("x", "c")])
    author.add_node("x")
    lean = nx.DiGraph([("a", "b"), ("b", "c"), ("d", "c")])
    lean.add_node("x")
    author.add_node("d")
    e = compare_edges(author, lean)
    assert e["author_direct_in_lean"] == 1  # a->b
    assert e["author_implied_transitively"] == 1  # a->c via b
    assert e["author_absent_from_lean"] == [("x", "c")]
    assert e["lean_unreported_by_author"] == [("b", "c"), ("d", "c")]


def test_structure_fields_and_projections(tmp_path):
    import json

    from cairn.formal import load_decls, projections

    def row(name, kind, type_pp="", type_deps=(), value_deps=()):
        return {"name": name, "user_name": name, "private": False, "module": "M", "kind": kind, "line": 1,
                "type_size": 1, "value_size": 1, "type_pp": type_pp, "type_deps": list(type_deps),
                "value_deps": list(value_deps)}

    rows = [row("Pair", "inductive"),
            row("Pair.mk", "constructor", "{E : Type} → (π : E → ℝ) → (v : E) → π v = 1 → Pair E"),
            row("Pair.π", "def", type_deps=["Pair"]), row("Pair.v", "def", type_deps=["Pair"]),
            row("Pair.spanV", "def", type_deps=["Pair"]),
            row("Two", "inductive"), row("Two.a", "constructor", "(x : ℕ) → Two"), row("Two.b", "constructor"),
            row("Two.x", "def")]
    path = tmp_path / "d.jsonl"
    path.write_text("\n".join(json.dumps(r) for r in rows))
    decls = load_decls(path)
    assert decls["Pair"].fields == ["π", "v"]
    assert decls["Two"].fields == []  # two constructors: not a structure
    assert projections(decls) == {"Pair.π": "Pair", "Pair.v": "Pair"}


def test_restore_fintype():
    from cairn.formal import restore_fintype

    assert restore_fintype("(h : p) : q", "∀ {G} [inst : Fintype G], p → q") == "[Fintype G] (h : p) : q"
    assert restore_fintype("x = 1", "∀ {G} [inst : Fintype G], x = 1") == "[Fintype G] : x = 1"
    assert restore_fintype("[Fintype G] : x = 1", "[inst : Fintype G] → x = 1") == "[Fintype G] : x = 1"
    assert restore_fintype("(h : p) : q", "∀ {G} [inst : AddCommGroup G], p → q") == "(h : p) : q"
