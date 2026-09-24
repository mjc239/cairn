"""Parse a leanblueprint LaTeX source tree into nodes, dependency edges and document order.

Conventions follow https://github.com/PatrickMassot/leanblueprint:

- theorem-like environments (``lemma``, ``theorem``, ...) are nodes;
- ``\\label{}`` gives a node its id, ``\\lean{a, b}`` links Lean declarations,
  ``\\leanok`` / ``\\mathlibok`` mark formalisation status;
- ``\\uses{}`` inside a statement is a *statement* dependency, inside the
  following ``proof`` environment a *proof* dependency;
- a ``proof`` belongs to the closest preceding statement unless it says ``\\proves{label}``.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

STATEMENT_ENVS = (
    "theorem",
    "lemma",
    "sublemma",
    "proposition",
    "corollary",
    "definition",
    "conjecture",
    "remark",
    "example",
)
PROOF_ENV = "proof"

_ENV_RE = re.compile(
    r"\\(begin|end)\{(" + "|".join((*STATEMENT_ENVS, PROOF_ENV)) + r")\}"
)
_HEADING_RE = re.compile(r"\\(chapter|section)\*?\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
GROUP_BY = ("file", "chapter", "section")
_INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
_COMMENT_RE = re.compile(r"(?<!\\)%.*")


def _macro_args(body: str, name: str) -> list[str]:
    """Arguments of every ``\\name{...}`` in ``body`` (single brace level)."""
    return re.findall(r"\\" + name + r"\s*\{([^}]*)\}", body)


def _split_csv(args: list[str]) -> list[str]:
    return [item.strip() for arg in args for item in arg.split(",") if item.strip()]


def _has_flag(body: str, name: str) -> bool:
    return re.search(r"\\" + name + r"(?![A-Za-z])", body) is not None


_META_RE = re.compile(r"\\(?:label|lean|uses|proves)\s*\{[^}]*\}|\\(?:leanok|mathlibok|notready)(?![A-Za-z])")


def _statement_text(body: str) -> str:
    stripped = body.lstrip(" \t")
    if stripped.startswith("["):  # optional title, brackets may nest
        depth = 0
        for j, ch in enumerate(stripped):
            depth += {"[": 1, "]": -1}.get(ch, 0)
            if depth == 0:
                body = stripped[j + 1 :]
                break
    return " ".join(_META_RE.sub("", body).split())


def _optional_title(text: str, start: int) -> str | None:
    """Parse ``[title]`` (brackets may nest) right after ``\\begin{env}``."""
    i = start
    while i < len(text) and text[i] in " \t":
        i += 1
    if i >= len(text) or text[i] != "[":
        return None
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "[":
            depth += 1
        elif text[j] == "]":
            depth -= 1
            if depth == 0:
                return text[i + 1 : j].strip()
    return None


@dataclass
class Node:
    id: str
    kind: str
    position: int
    chapter: str
    source: str
    line: int
    title: str | None = None
    labels: list[str] = field(default_factory=list)
    lean_decls: list[str] = field(default_factory=list)
    leanok: bool = False
    mathlibok: bool = False
    statement_uses: list[str] = field(default_factory=list)
    proof_uses: list[str] = field(default_factory=list)
    has_proof: bool = False
    statement_event: int = -1
    """Index of the statement in the document's sequence of statement and proof environments."""
    proof_event: int | None = None
    proof_chapter: str | None = None
    """Chapter (per ``group_by``) where the proof sits; differs from ``chapter`` for proofs deferred elsewhere."""
    """Index of the (first) proof environment for this node in that sequence; ``None`` if unproved."""
    proof_leanok: bool = False
    text: str = ""
    """Statement body with blueprint metadata macros removed and whitespace collapsed."""


@dataclass
class Blueprint:
    nodes: list[Node]
    # (node id, referenced label, "statement" | "proof") for \uses targets that match no node
    unresolved: list[tuple[str, str, str]]
    orphan_proofs: list[tuple[str, int]]

    def by_id(self) -> dict[str, Node]:
        return {n.id: n for n in self.nodes}

    def edges(self, kinds: tuple[str, ...] = ("statement", "proof")) -> list[tuple[str, str, str]]:
        """Dependency edges ``(prerequisite, dependent, kind)`` between resolved nodes."""
        alias = {label: n.id for n in self.nodes for label in n.labels}
        out: list[tuple[str, str, str]] = []
        seen: set[tuple[str, str, str]] = set()
        for n in self.nodes:
            for kind, refs in (("statement", n.statement_uses), ("proof", n.proof_uses)):
                if kind not in kinds:
                    continue
                for ref in refs:
                    src = alias.get(ref)
                    if src is None or src == n.id:
                        continue
                    edge = (src, n.id, kind)
                    if edge not in seen:
                        seen.add(edge)
                        out.append(edge)
        return out


def _read_flat(path: Path, root: Path, stack: tuple[Path, ...] = ()) -> list[tuple[str, str, int]]:
    """Return ``(source_file, text, first_line)`` chunks with ``\\input`` expanded in place.

    Comments are stripped line by line so line numbers survive.
    """
    if path in stack:
        raise ValueError(f"cyclic \\input: {' -> '.join(map(str, (*stack, path)))}")
    text = "\n".join(_COMMENT_RE.sub("", line) for line in path.read_text().splitlines())
    # relpath, not relative_to: generated blueprints (LeanArchitect) \input files outside ``root``
    rel = os.path.relpath(path, root)
    chunks: list[tuple[str, str, int]] = []
    last = 0
    for m in _INPUT_RE.finditer(text):
        chunks.append((rel, text[last : m.start()], text.count("\n", 0, last) + 1))
        target = root / m.group(1)
        if target.suffix != ".tex":
            target = target.with_name(target.name + ".tex")
        chunks.extend(_read_flat(target, root, (*stack, path)))
        last = m.end()
    chunks.append((rel, text[last:], text.count("\n", 0, last) + 1))
    return chunks


def _slug(title: str) -> str:
    title = re.sub(r"\\[A-Za-z]+|[{}$\\\"']", "", title)
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:40] or "untitled"


def parse_blueprint(src_dir: str | Path, entry: str = "content.tex", group_by: str = "file") -> Blueprint:
    """Parse the blueprint rooted at ``src_dir`` (usually ``blueprint/src``).

    ``entry`` is the file listing the chapters; leanblueprint templates call it
    ``content.tex``, older projects (e.g. PFR) ``chapter/main.tex``. If ``entry``
    does not exist, ``chapter/main.tex`` is tried.

    ``group_by`` decides what ``Node.chapter`` holds: the source file's stem (``"file"``, right for
    blueprints with one file per chapter), the enclosing ``\\chapter`` or the enclosing ``\\section``
    (for single-file blueprints such as Carleson's), as a slug of its title.
    """
    if group_by not in GROUP_BY:
        raise ValueError(f"group_by must be one of {GROUP_BY}")
    root = Path(src_dir)
    entry_path = root / entry
    if not entry_path.exists():
        entry_path = root / "chapter" / "main.tex"
    chunks = _read_flat(entry_path, root)

    nodes: list[Node] = []
    orphan_proofs: list[tuple[str, int]] = []
    anon = 0
    event = 0  # counts statement and proof environments in document order
    heading = {"chapter": "front-matter", "section": "front-matter"}
    for source, text, first_line in chunks:
        headings = [(h.start(), h.group(1), _slug(h.group(2))) for h in _HEADING_RE.finditer(text)]
        open_env: tuple[str, int, int] | None = None  # (env, body_start, line)
        for m in _ENV_RE.finditer(text):
            while headings and headings[0][0] < m.start():
                _, level, slug = headings.pop(0)
                heading[level] = slug
                if level == "chapter":
                    heading["section"] = slug
            chapter = Path(source).stem if group_by == "file" else heading[group_by]
            action, env = m.group(1), m.group(2)
            line = first_line + text.count("\n", 0, m.start())
            if action == "begin":
                if open_env is None:
                    open_env = (env, m.end(), line)
                continue
            if open_env is None or open_env[0] != env:
                continue
            env, body_start, start_line = open_env
            body = text[body_start : m.start()]
            open_env = None
            if env == PROOF_ENV:
                proves = _split_csv(_macro_args(body, "proves"))
                target = next((n for n in nodes if proves and proves[0] in n.labels), None)
                if target is None and not proves and nodes and nodes[-1].source == source:
                    target = nodes[-1]
                if target is None:
                    orphan_proofs.append((source, start_line))
                    continue
                if not target.has_proof:
                    target.proof_event = event
                    target.proof_chapter = chapter
                event += 1
                target.has_proof = True
                target.proof_uses.extend(_split_csv(_macro_args(body, "uses")))
                target.proof_leanok = target.proof_leanok or _has_flag(body, "leanok")
                continue
            labels = _split_csv(_macro_args(body, "label"))
            if labels:
                node_id = labels[0]
            else:
                anon += 1
                node_id = f"_anon{anon}:{chapter}"
            nodes.append(
                Node(
                    id=node_id,
                    kind=env,
                    position=len(nodes),
                    statement_event=event,
                    chapter=chapter,
                    source=source,
                    line=start_line,
                    title=_optional_title(text, body_start),
                    labels=labels or [node_id],
                    lean_decls=_split_csv(_macro_args(body, "lean")),
                    leanok=_has_flag(body, "leanok"),
                    mathlibok=_has_flag(body, "mathlibok"),
                    statement_uses=_split_csv(_macro_args(body, "uses")),
                    text=_statement_text(body),
                )
            )
            event += 1
        for _, level, slug in headings:  # headings after the chunk's last environment
            heading[level] = slug
            if level == "chapter":
                heading["section"] = slug

    ids = {label for n in nodes for label in n.labels}
    unresolved = [
        (n.id, ref, kind)
        for n in nodes
        for kind, refs in (("statement", n.statement_uses), ("proof", n.proof_uses))
        for ref in refs
        if ref not in ids
    ]
    return Blueprint(nodes=nodes, unresolved=unresolved, orphan_proofs=orphan_proofs)
