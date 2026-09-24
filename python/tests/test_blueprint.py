from pathlib import Path

from cairn.blueprint import parse_blueprint

MINI = Path(__file__).parent / "fixtures" / "mini"


def test_parse_mini():
    bp = parse_blueprint(MINI)
    assert [n.id for n in bp.nodes] == ["def-widget", "nice", "later", "main"]
    nodes = bp.by_id()
    assert [n.chapter for n in bp.nodes] == ["one", "one", "two", "two"]

    nice = nodes["nice"]
    assert nice.title == "Widgets are nice [really]"
    assert nice.lean_decls == ["Foo.nice", "Foo.nice'"]
    assert nice.leanok and nice.has_proof and nice.proof_leanok
    assert nice.statement_uses == ["def-widget"]
    assert nice.proof_uses == ["later"]

    assert nodes["def-widget"].statement_uses == []  # commented out
    assert nice.text == "Every widget is nice."
    assert nodes["later"].labels == ["later", "later-alias"]
    assert nodes["main"].mathlibok and not nodes["main"].leanok

    assert bp.unresolved == [("later", "missing-label", "proof")]


def test_edges_resolve_aliases_and_kinds():
    bp = parse_blueprint(MINI)
    edges = set(bp.edges())
    assert ("later", "main", "proof") in edges  # via later-alias
    assert ("def-widget", "nice", "statement") in edges
    assert {e for e in edges if e[2] == "proof"} == {
        ("later", "nice", "proof"),
        ("nice", "main", "proof"),
        ("later", "main", "proof"),
    }
    assert all(k == "statement" for *_, k in bp.edges(("statement",)))


def test_group_by_section_and_chapter():
    bp = parse_blueprint(MINI, "sections.tex", group_by="section")
    assert [n.chapter for n in bp.nodes] == ["basic-facts", "the-main-result", "gadgets"]
    bp = parse_blueprint(MINI, "sections.tex", group_by="chapter")
    assert [n.chapter for n in bp.nodes] == ["widgets", "widgets", "gadgets"]
    bp = parse_blueprint(MINI, "sections.tex")
    assert [n.chapter for n in bp.nodes] == ["sections", "tail", "tail"]


def test_deferred_proof_records_its_own_section(tmp_path):
    (tmp_path / "content.tex").write_text(
        "\\section{Overview}\n\\begin{theorem}\\label{main}Main.\\end{theorem}\n"
        "\\section{Details}\n\\begin{lemma}\\label{aux}Aux.\\end{lemma}\\begin{proof}Easy.\\end{proof}\n"
        "\\begin{proof}\\proves{main}\\uses{aux}Done.\\end{proof}\n")
    bp = parse_blueprint(tmp_path, group_by="section")
    main, aux = bp.by_id()["main"], bp.by_id()["aux"]
    assert (main.chapter, main.proof_chapter) == ("overview", "details")
    assert main.statement_event < aux.statement_event < aux.proof_event < main.proof_event
