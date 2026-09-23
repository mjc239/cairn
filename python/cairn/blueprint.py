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
_INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
_COMMENT_RE = re.compile(r"(?<!\\)%.*")


def _macro_args(body: str, name: str) -> list[str]:
    """Arguments of every ``\\name{...}`` in ``body`` (single brace level)."""
    return re.findall(r"\\" + name + r"\s*\{([^}]*)\}", body)


def _split_csv(args: list[str]) -> list[str]:
    return [item.strip() for arg in args for item in arg.split(",") if item.strip()]


def _has_flag(body: str, name: str) -> bool:
    return re.search(r"\\" + name + r"(?![A-Za-z])", body) is not None


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
    proof_leanok: bool = False


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
    rel = str(path.relative_to(root))
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


def parse_blueprint(src_dir: str | Path, entry: str = "content.tex") -> Blueprint:
    """Parse the blueprint rooted at ``src_dir`` (usually ``blueprint/src``).

    ``entry`` is the file listing the chapters; leanblueprint templates call it
    ``content.tex``, older projects (e.g. PFR) ``chapter/main.tex``. If ``entry``
    does not exist, ``chapter/main.tex`` is tried.
    """
    root = Path(src_dir)
    entry_path = root / entry
    if not entry_path.exists():
        entry_path = root / "chapter" / "main.tex"
    chunks = _read_flat(entry_path, root)

    nodes: list[Node] = []
    orphan_proofs: list[tuple[str, int]] = []
    anon = 0
    for source, text, first_line in chunks:
        chapter = Path(source).stem
        open_env: tuple[str, int, int] | None = None  # (env, body_start, line)
        for m in _ENV_RE.finditer(text):
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
                    chapter=chapter,
                    source=source,
                    line=start_line,
                    title=_optional_title(text, body_start),
                    labels=labels or [node_id],
                    lean_decls=_split_csv(_macro_args(body, "lean")),
                    leanok=_has_flag(body, "leanok"),
                    mathlibok=_has_flag(body, "mathlibok"),
                    statement_uses=_split_csv(_macro_args(body, "uses")),
                )
            )

    ids = {label for n in nodes for label in n.labels}
    unresolved = [
        (n.id, ref, kind)
        for n in nodes
        for kind, refs in (("statement", n.statement_uses), ("proof", n.proof_uses))
        for ref in refs
        if ref not in ids
    ]
    return Blueprint(nodes=nodes, unresolved=unresolved, orphan_proofs=orphan_proofs)
