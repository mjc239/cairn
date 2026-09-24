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
   checked again.
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
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (explicit hypotheses and meaningful instance assumptions such as `[Finite G]` are shown; implicit
arguments and purely structural instances such as `[AddCommGroup G]` are omitted), its
docstring if there is one, and, for theorems, the named results its proof uses (with their statements) and the
helper lemmas folded into the proof.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful: keep every hypothesis and the exact conclusion; do not add, drop, strengthen or weaken
   anything. If some notation's meaning is unclear, keep the notation rather than guessing. For a definition, say
   what is being defined.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given."""

CHECK_INSTRUCTIONS = """You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given."""

REPAIR_INSTRUCTIONS = """You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

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


def _clip(text: str, n: int) -> str:
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1] + "…"


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
                 f"## Chapter (Lean module `{ch}`)", ""]
        for v in results:
            d = decls[v]
            kind = "definition" if d.kind != "theorem" else "theorem"
            lines.append(f"### `{v}` ({kind})")
            lines.append(f"Lean: `{_clip(statement_of(d, nss), 3000)}`")
            if d.doc:
                lines.append(f"Docstring: {_clip(d.doc, 400)}")
            if kind == "theorem":
                uses = uses_of(o, v)
                if uses:
                    lines.append("Proof uses:")
                    lines += [f"- `{u}`: `{_clip(statement_of(decls[u], nss), 500)}`" for u in uses[:10]]
                helpers = helpers_of(o, v)
                if helpers:
                    lines.append("Helper lemmas folded into the proof: " + ", ".join(f"`{h}`" for h in helpers[:8]))
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
        lines = [CHECK_INSTRUCTIONS, ""]
        for v in results:
            eng = entry["results"].get(v, {}).get("statement")
            if not eng:
                continue
            lines += [f"### `{v}`", f"Lean: `{_clip(statement_of(decls[v], nss), 3000)}`", f"English: {eng}", ""]
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
        lines = [REPAIR_INSTRUCTIONS, "", f"Namespaces open (prefixes omitted): {', '.join(nss)}.", ""]
        for v in flagged:
            r, d = entry["results"][v], decls[v]
            lines += [f"### `{v}`", f"Lean: `{_clip(statement_of(d, nss), 3000)}`"]
            if d.doc:
                lines.append(f"Docstring: {_clip(d.doc, 400)}")
            lines += [f"Previous English: {r['statement']}", f"Checker's issue: {r.get('issue', '')}", ""]
        path = Path(prose_dir) / f"{chapter_key(ch)}.repair.md"
        path.write_text("\n".join(lines))
        paths.append(path)
    return paths


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
        repair = Path(prose_dir) / f"{key}.repair.json"
        if repair.exists():
            try:
                for k, v in json.loads(repair.read_text()).items():
                    if k in results and v.get("statement"):
                        results[k]["statement"] = v["statement"]
                        results[k]["repaired"] = True
            except json.JSONDecodeError:
                pass
        check = Path(prose_dir) / f"{key}.check.json"
        if check.exists():
            try:
                for k, v in json.loads(check.read_text()).items():
                    if k in results:
                        results[k]["faithful"] = bool(v.get("faithful", True))
                        results[k]["issue"] = v.get("issue", "")
            except json.JSONDecodeError:
                pass
        out[module] = {"title": data.get("title"), "results": results}
    return out


def coverage(o, prose: dict[str, dict]) -> dict:
    named = [node_of(e) for e in o.order if e.startswith("S:")]
    have = [v for v in named if prose.get(o.chapter[v], {}).get("results", {}).get(v, {}).get("statement")]
    checked = [v for v in have if "faithful" in prose[o.chapter[v]]["results"][v]]
    flagged = [v for v in checked if not prose[o.chapter[v]]["results"][v]["faithful"]]
    return {"results": len(named), "translated": len(have), "checked": len(checked), "flagged": flagged}
