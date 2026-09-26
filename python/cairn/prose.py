"""Prose for outlines: chapter titles, plain-English statements and proof sketches, and a faithfulness check.

Everything goes through files, so any model or API can fill them in:

1. ``write_prose_prompts`` writes ``<chapter>.prompt.md`` per chapter: each result's Lean name and short statement,
   docstring and (for theorems) the named results its proof uses and the helpers folded into it. A model answers
   with ``<chapter>.prose.json``: a chapter title, an English statement per result, a proof sketch per theorem.
2. ``write_check_prompts`` writes ``<chapter>.check.md``, which pairs each Lean statement with its English
   translation. A *separate* reader answers ``<chapter>.check.json``, flagging translations that add, drop,
   strengthen or weaken anything.
3. ``write_repair_prompts`` writes ``<chapter>.repair.md`` for chapters with flagged translations: each flagged
   result with its Lean statement, the previous English and the checker's issue. A model answers
   ``<chapter>.repair.json`` with corrected statements, which override the originals; the chapter is then
   checked again. Later rounds write ``<chapter>.repair2.md`` / ``.repair2.json`` and so on, applied in order.
4. ``load_prose`` reads them all, and :func:`cairn.outline.render` shows the English next to the Lean statement, with
   flagged translations marked. The Lean statement always stays in the outline: it is the verified ground truth.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from .events import P, S, node_of
from .formal import FormalDecl

PROSE_INSTRUCTIONS = """You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, a
short form of its statement, the full Lean statement (every implicit argument and every instance assumption, e.g.
`[AddCommGroup G]` for "G is an abelian group", `[Field K]`, `[MetricSpace X]`), its docstring if there is one, and,
for theorems, the named results its proof uses (with their full statements) and the helper lemmas folded into the
proof. A "Project definitions" section first lists the project notions these statements refer to, with their
statements, docstrings, definition bodies and fields.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful to the FULL statement: keep every hypothesis and the exact conclusion; do not add, drop,
   strengthen or weaken anything. State the assumptions carried by instance arguments in words ("G is a finite
   abelian group", "X is a metric space", "μ is a doubling measure"); omitting one makes the English claim more than
   was proved. Only instances that carry no mathematical content at all (decidability: `Decidable…`) may be left
   unstated. Never replace an assumption by a stronger one (a metric space where the Lean has a pseudometric
   space). State restrictive types (a natural number, a nonnegative real). Cite theorem or lemma numbers, or add
   remarks, only when the docstring or the Lean supports them. Give every variable its type and introduce every
   symbol, by definition or by name; never use one letter for two things. Describe a project notion only as its
   entry under "Project definitions" supports (statement, docstring, definition body, fields), and a library
   notion only by its standard meaning; if unsure, name it rather than guess. For a definition, name the setting
   its signature assumes and say what is being defined, from its body when one is shown.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given."""

CHECK_INSTRUCTIONS = """You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \\to \\mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given."""

REPAIR_INSTRUCTIONS = """You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given."""


def chapter_key(module: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", module).strip("_")


def open_namespaces(names, share: float = 0.05, extra: tuple[str, ...] = ("MeasureTheory",)) -> tuple[str, ...]:
    """Namespaces a reader would have open: top-level namespaces of at least ``share`` of the named results
    (plus ``extra``). Their prefixes are stripped from displayed statements, as ``open`` would."""
    names = list(names)
    tops = Counter(n.split(".")[0] for n in names if "." in n)
    found = {ns for ns, c in tops.items() if c >= share * len(names)}
    return tuple(sorted(found | set(extra), key=len, reverse=True))


def strip_namespaces(text: str, namespaces: tuple[str, ...]) -> str:
    for ns in namespaces:
        text = re.sub(rf"(?<![\w.]){re.escape(ns)}\.(?=\w)", "", text)
    return text


def statement_of(d: FormalDecl, namespaces: tuple[str, ...] = ()) -> str:
    return strip_namespaces((d.stmt_short or d.type_pp or "").strip(), namespaces)


def full_statement_of(d: FormalDecl, namespaces: tuple[str, ...] = ()) -> str:
    """The complete Lean statement: every implicit argument and instance assumption (``type_pp``)."""
    return strip_namespaces((d.type_pp or d.stmt_short or "").strip(), namespaces)


def _oneline(text: str) -> str:
    return " ".join(text.split())


def _lean_lines(d: FormalDecl, nss: tuple[str, ...]) -> list[str]:
    """Short and full statement, never truncated: the prose must be checked against everything Lean assumes.
    A definition also shows its body, and a structure its constructor, so a description can be checked."""
    short, full = _oneline(statement_of(d, nss)), _oneline(full_statement_of(d, nss))
    lines = [f"Lean (short): `{short}`", f"Lean (full): `{full}`"] if full != short else [f"Lean: `{full}`"]
    if d.value_pp:
        lines.append(f"Definition: `{_oneline(strip_namespaces(d.value_pp, nss))}`")
    if d.ctor_pp:
        lines.append(f"Constructor (every field with its type): `{_oneline(strip_namespaces(d.ctor_pp, nss))}`")
    return lines


def glossary(names, decls: dict[str, FormalDecl], depth: int = 3) -> list[str]:
    """Project notions (definitions, structures, classes, instances) that the statements of ``names`` refer to,
    followed ``depth`` levels through their own statements, definition bodies and a structure's fields, in
    first-seen order.
    Without them a reader cannot check what a project notion such as ``ProofData`` or ``rdist`` *is*."""
    from .outline import is_boilerplate_instance
    fields = {f"{s}.{f}" for s, d in decls.items() for f in d.fields}
    seen: dict[str, None] = {}
    frontier = list(names)
    for _ in range(depth):
        nxt = []
        for v in frontier:
            d = decls[v]
            # a definition's body is shown, so the notions it uses are needed to read it
            body = d.value_deps if d.value_pp and v not in names else set()
            refs = sorted(d.type_deps | body) + [f"{v}.{f}" for f in d.fields]
            for u in refs:
                if u in decls and u not in seen and u not in names and decls[u].kind != "theorem" \
                        and not is_boilerplate_instance(decls[u]) and (u in fields or not decls[u].private):
                    seen[u] = None
                    nxt.append(u)
        frontier = nxt
    return list(seen)


def _glossary_lines(names, decls: dict[str, FormalDecl], nss: tuple[str, ...]) -> list[str]:
    terms = glossary(names, decls)
    if not terms:
        return []
    lines = ["## Project definitions these statements use",
             "(What each project notion is. Any description of one in the English must agree with this.)", ""]
    for u in terms:
        d = decls[u]
        lines.append(f"#### `{u}` ({'structure or class' if d.fields else d.kind})")
        lines.append(f"Lean: `{_oneline(full_statement_of(d, nss))}`")
        if d.doc:
            lines.append(f"Docstring: {_oneline(d.doc)}")
        if d.value_pp:
            lines.append(f"Definition: `{_oneline(strip_namespaces(d.value_pp, nss))}`")
        if d.ctor_pp:
            lines.append(f"Constructor (every field with its type): `{_oneline(strip_namespaces(d.ctor_pp, nss))}`")
        elif d.fields:
            lines.append("Fields: " + ", ".join(f"`{f}`" for f in d.fields))
        lines.append("")
    return lines


def _chapters(o) -> dict[str, list[str]]:
    """Chapter -> named results in the order their statements appear."""
    out: dict[str, list[str]] = {ch: [] for ch in o.chapter_order}
    for e in o.order:
        if e.startswith("S:"):
            v = node_of(e)
            out.setdefault(o.chapter[v], []).append(v)
    return out


def uses_of(o, v: str) -> list[str]:
    e = P(v) if P(v) in o.graph else S(v)
    return sorted(node_of(p) for p in o.graph.predecessors(e) if node_of(p) != v)


def helpers_of(o, v: str) -> list[str]:
    return [h for h in o.absorbed.get(v, []) if ".Tactic." not in f".{h}."]


def write_prose_prompts(o, decls: dict[str, FormalDecl], out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    nss = open_namespaces(o.named)
    paths = []
    for ch, results in _chapters(o).items():
        if not results:
            continue
        lines = [PROSE_INSTRUCTIONS, "", f"Namespaces open (prefixes omitted): {', '.join(nss)}.", "",
                 *_glossary_lines(results, decls, nss), f"## Chapter (Lean module `{ch}`)", ""]
        for v in results:
            d = decls[v]
            kind = "definition" if d.kind != "theorem" else "theorem"
            lines.append(f"### `{v}` ({kind})")
            lines += _lean_lines(d, nss)
            if d.doc:
                lines.append(f"Docstring: {_oneline(d.doc)}")
            if kind == "theorem":
                uses = uses_of(o, v)
                if uses:
                    lines.append("Proof uses:")
                    lines += [f"- `{u}`: `{_oneline(full_statement_of(decls[u], nss))}`" for u in uses]
                helpers = helpers_of(o, v)
                if helpers:
                    lines.append("Helper lemmas folded into the proof: " + ", ".join(f"`{h}`" for h in helpers))
            lines.append("")
        path = out_dir / f"{chapter_key(ch)}.prompt.md"
        path.write_text("\n".join(lines))
        paths.append(path)
    return paths


def write_check_prompts(o, decls: dict[str, FormalDecl], prose_dir: Path) -> list[Path]:
    prose = load_prose(prose_dir)
    nss = open_namespaces(o.named)
    paths = []
    for ch, results in _chapters(o).items():
        entry = prose.get(ch)
        if not entry:
            continue
        lines = [CHECK_INSTRUCTIONS, "", *_glossary_lines(results, decls, nss), "## Translations", ""]
        for v in results:
            eng = entry["results"].get(v, {}).get("statement")
            if not eng:
                continue
            doc = [f"Docstring: {_oneline(decls[v].doc)}"] if decls[v].doc else []
            lines += [f"### `{v}`", *_lean_lines(decls[v], nss), *doc, f"English: {eng}", ""]
        path = Path(prose_dir) / f"{chapter_key(ch)}.check.md"
        path.write_text("\n".join(lines))
        paths.append(path)
    return paths


def write_repair_prompts(o, decls: dict[str, FormalDecl], prose_dir: Path) -> list[Path]:
    prose = load_prose(prose_dir)
    nss = open_namespaces(o.named)
    paths = []
    for ch, results in _chapters(o).items():
        entry = prose.get(ch)
        flagged = [v for v in results if entry and entry["results"].get(v, {}).get("faithful") is False]
        if not flagged:
            continue
        lines = [REPAIR_INSTRUCTIONS, "", f"Namespaces open (prefixes omitted): {', '.join(nss)}.", "",
                 *_glossary_lines(flagged, decls, nss), "## Flagged translations", ""]
        for v in flagged:
            r, d = entry["results"][v], decls[v]
            lines += [f"### `{v}`", *_lean_lines(d, nss)]
            if d.doc:
                lines.append(f"Docstring: {_oneline(d.doc)}")
            lines += [f"Previous English: {r['statement']}", f"Checker's issue: {r.get('issue', '')}", ""]
        key = chapter_key(ch)
        n = len(_repair_files(Path(prose_dir), key)) + 1
        path = Path(prose_dir) / f"{key}.repair{n if n > 1 else ''}.md"
        path.write_text("\n".join(lines))
        paths.append(path)
    return paths


def _repair_files(prose_dir: Path, key: str) -> list[Path]:
    """``<key>.repair.json``, ``<key>.repair2.json``, … in round order."""
    files = [(int(m.group(1) or 1), f) for f in prose_dir.glob(f"{key}.repair*.json")
             if (m := re.fullmatch(re.escape(key) + r"\.repair(\d*)\.json", f.name))]
    return [f for _, f in sorted(files)]


def _answers(repair: Path | None, name: str, issue: str) -> bool:
    """Whether ``repair`` (a ``.repair*.json``) was written in answer to ``issue``: its prompt quotes the issue."""
    prompt = repair.with_suffix(".md") if repair else None
    if not (prompt and prompt.exists() and issue):
        return False
    block = prompt.read_text().split(f"### `{name}`", 1)
    return len(block) == 2 and f"Checker's issue: {issue}" in block[1].split("\n### ", 1)[0]


def load_prose(prose_dir: Path | None) -> dict[str, dict]:
    """Chapter (module) -> {"title", "results": {name: {"statement", "sketch", "faithful", "issue"}}}."""
    if prose_dir is None or not Path(prose_dir).exists():
        return {}
    out = {}
    for f in sorted(Path(prose_dir).glob("*.prose.json")):
        key = f.name[: -len(".prose.json")]
        try:
            data = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        prompt = Path(prose_dir) / f"{key}.prompt.md"
        m = re.search(r"Lean module `([^`]+)`", prompt.read_text()) if prompt.exists() else None
        module = m.group(1) if m else key
        results = {k: dict(v) for k, v in data.get("results", {}).items()}
        last_repair: dict[str, Path] = {}
        for repair in _repair_files(Path(prose_dir), key):
            try:
                for k, v in json.loads(repair.read_text()).items():
                    if k in results and v.get("statement"):
                        results[k]["statement"] = v["statement"]
                        results[k]["repaired"] = True
                        last_repair[k] = repair
            except json.JSONDecodeError:
                pass
        check = Path(prose_dir) / f"{key}.check.json"
        if check.exists():
            try:
                for k, v in json.loads(check.read_text()).items():
                    if k in results:
                        results[k]["faithful"] = bool(v.get("faithful", True))
                        results[k]["issue"] = v.get("issue", "")
                        if not results[k]["faithful"] and _answers(last_repair.get(k), k, results[k]["issue"]):
                            results[k]["recheck_pending"] = True  # repaired after this verdict, not yet re-checked
            except json.JSONDecodeError:
                pass
        out[module] = {"title": data.get("title"), "results": results}
    return out


def coverage(o, prose: dict[str, dict]) -> dict:
    named = [node_of(e) for e in o.order if e.startswith("S:")]
    have = [v for v in named if prose.get(o.chapter[v], {}).get("results", {}).get(v, {}).get("statement")]
    checked = [v for v in have if "faithful" in prose[o.chapter[v]]["results"][v]]
    flagged = [v for v in checked if not prose[o.chapter[v]]["results"][v]["faithful"]]
    pending = [v for v in flagged if prose[o.chapter[v]]["results"][v].get("recheck_pending")]
    return {"results": len(named), "translated": len(have), "checked": len(checked), "flagged": flagged,
            "recheck_pending": pending}
