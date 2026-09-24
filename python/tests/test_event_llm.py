import json

from cairn.blueprint import parse_blueprint
from cairn.event_llm import chapters_of, load_event_run, write_event_prompts
from cairn.events import event_graph
from cairn.formal import FormalDecl


def _project(tmp_path):
    # Overview states `main`; section "details" has 8 lemmas feeding main's (deferred) proof.
    lemmas = "".join(
        f"\\begin{{lemma}}\\label{{l{i}}}\\lean{{L{i}}}Lemma {i}.\\end{{lemma}}\\begin{{proof}}Easy.\\end{{proof}}\n"
        for i in range(8))
    (tmp_path / "content.tex").write_text(
        "\\section{Overview}\n\\begin{theorem}\\label{main}\\lean{Main}Main, cf. \\Cref{l0}.\\end{theorem}\n"
        "\\section{Details}\n" + lemmas + "\\begin{proof}\\proves{main}Combine.\\end{proof}\n")
    bp = parse_blueprint(tmp_path, group_by="section")
    decls = {f"L{i}": FormalDecl(f"L{i}", "theorem", "M", i, value_deps={f"L{i - 1}"} if i else set())
             for i in range(8)}
    decls["Main"] = FormalDecl("Main", "theorem", "M", 99, value_deps={f"L{i}" for i in range(8)})
    return bp, decls


def test_event_prompt_roundtrip_with_cross_section_proof(tmp_path):
    bp, decls = _project(tmp_path)
    out = tmp_path / "prompts"
    write_event_prompts(bp, decls, out, seed=1, anonymise=True, titles=False)
    prompt = (out / "details.prompt.md").read_text()
    assert "prove only (it was stated in an earlier section)" in prompt
    assert "l0" not in prompt and "\\Cref" not in prompt
    g, human = event_graph(bp, decls)
    chapters = chapters_of(bp, g, human)
    assert set(chapters) == {"details"} and "S:main" not in chapters["details"]
    inverse = {v: a for a, v in json.loads((out / "details.ids.json").read_text()).items()}
    answer = [f"{e[:2]}{inverse[e[2:]]}" for e in chapters["details"]]
    (out / "details.response.json").write_text(json.dumps(answer))
    res = load_event_run(out, g, chapters)
    assert res["orders"]["details"] == chapters["details"] and res["violations_repaired"] == {"details": 0}
