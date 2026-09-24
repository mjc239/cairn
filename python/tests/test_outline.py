import pytest

from cairn.events import P, S
from cairn.formal import FormalDecl, formal_graph
from cairn.outline import build, fold, render, select
from cairn.style import Style


def _decls():
    # def D; helper h (unnamed) used by main lemma L; theorem T uses L; T's statement mentions D.
    d = {
        "D": FormalDecl("D", "def", "M.Defs", 1),
        "h": FormalDecl("h", "theorem", "M.A", 2, type_pp="h : True"),
        "L": FormalDecl("L", "theorem", "M.A", 3, value_deps={"h"}, type_pp="L : True", doc="Key lemma."),
        "T": FormalDecl("T", "theorem", "M.B", 4, type_deps={"D"}, value_deps={"L"}, type_pp="T : D"),
        "X": FormalDecl("X", "theorem", "Other.C", 5),
    }
    return d


def test_select_fold_and_define_used():
    d = _decls()
    fg = formal_graph(d)
    scores = {"T": 0.9, "L": 0.8, "h": 0.1, "D": 0.05, "X": 0.95}
    assert select(d, fg, scores, count=2, modules=["M"], define_used=False) == {"T", "L"}
    assert select(d, fg, scores, count=2, modules=["M"]) == {"T", "L", "D"}  # T's statement mentions D
    assert select(d, fg, scores, count=1, roots=["L"], define_used=False) == {"L"}
    g, absorbed = fold(fg, {"T", "L"})
    assert set(g.edges) == {("L", "T")} and absorbed["L"] == ["h"]


@pytest.mark.parametrize("style", [Style(0), Style(1, "chapter")])
def test_build_and_render(style):
    d = _decls()
    scores = {"T": 0.9, "L": 0.8, "h": 0.1, "D": 0.05, "X": 0.95}
    o = build(d, scores, style, count=2, modules=["M"], seed=1)
    pos = {e: i for i, e in enumerate(o.order)}
    assert pos[S("D")] < pos[S("T")] and pos[S("L")] < pos[P("T")]
    assert o.chapter_order == ["M.Defs", "M.A", "M.B"] or o.chapter_order.index("M.A") < o.chapter_order.index("M.B")
    md = render(o, d, "Test", style, "note")
    assert "**Theorem** `T`" in md and "folds in 1 helper lemma: `h`" in md and "Key lemma." in md


def test_prose_roundtrip(tmp_path):
    import json

    from cairn.prose import coverage, load_prose, strip_namespaces, write_check_prompts, write_prose_prompts

    d = _decls()
    d["T"].stmt_short = "(h : Foo.P) : Foo.Q"
    scores = {"T": 0.9, "L": 0.8, "h": 0.1, "D": 0.05, "X": 0.95}
    o = build(d, scores, Style(0), count=2, modules=["M"], seed=1)
    paths = write_prose_prompts(o, d, tmp_path)
    assert {p.name for p in paths} == {"M_Defs.prompt.md", "M_A.prompt.md", "M_B.prompt.md"}
    prompt = (tmp_path / "M_B.prompt.md").read_text()
    assert "`T` (theorem)" in prompt and "Proof uses:" in prompt and "- `L`" in prompt
    (tmp_path / "M_B.prose.json").write_text(json.dumps(
        {"title": "The main theorem", "results": {"T": {"statement": "If P then Q.", "sketch": "Apply L."}}}))
    write_check_prompts(o, d, tmp_path)
    assert "English: If P then Q." in (tmp_path / "M_B.check.md").read_text()
    (tmp_path / "M_B.check.json").write_text(json.dumps({"T": {"faithful": False, "issue": "drops h"}}))
    prose = load_prose(tmp_path)
    assert prose["M.B"]["title"] == "The main theorem"
    md = render(o, d, "Test", Style(0), "note", prose)
    assert "## 3. The main theorem" in md and "If P then Q." in md and "Apply L." in md
    assert "Translation flagged: drops h" in md and "Lean: `(h : Foo.P) : Foo.Q`" in md
    assert coverage(o, prose) == {"results": 3, "translated": 1, "checked": 1, "flagged": ["T"]}
    assert strip_namespaces("Foo.P ∧ Bar.Foo.P ∧ Foo.x", ("Foo",)) == "P ∧ Bar.Foo.P ∧ x"
