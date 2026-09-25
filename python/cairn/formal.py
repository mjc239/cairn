"""Formal (Lean) dependency graphs, from the JSON Lines written by ``lean/extract_deps.lean``.

Compiler auxiliaries (``foo._proof_1``, ``foo.match_1``, ``foo.eq_1``, recursors, constructors, ...)
are folded into the user-facing declaration they belong to, both as dependents and as dependencies.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import networkx as nx

from .blueprint import Blueprint

_INTERNAL_COMPONENT = re.compile(r"^(_.*|\d+|(match|proof|eq|omega)_\d+.*)$")
_GENERATED_SUFFIXES = {
    "rec", "recOn", "casesOn", "below", "brecOn", "binductionOn", "ibelow", "noConfusion",
    "noConfusionType", "mk", "sizeOf_spec", "injEq", "inj", "ext_iff", "ctorIdx", "toCtorIdx",
}


_FINTYPE = re.compile(r"\[(?:[^\[\]:]+ : )?(Fintype [^\]]+)\]")


def restore_fintype(stmt_short: str, type_pp: str) -> str:
    """Add the ``[Fintype X]`` assumptions of the full statement to a short statement that dropped them.

    ``Fintype X`` is data, so extractors before this fix hid it like ``[AddCommGroup X]``, but it states that X is
    finite. Current extractors keep it; this repairs older dumps.
    """
    missing = [f for f in dict.fromkeys(_FINTYPE.findall(type_pp or "")) if f"[{f}]" not in stmt_short]
    if not missing or not stmt_short:
        return stmt_short
    prefix = " ".join(f"[{f}]" for f in missing)
    has_binders = stmt_short.startswith("[") or re.match(r"\((\S+) : ", stmt_short)
    return f"{prefix} {stmt_short}" if has_binders else f"{prefix} : {stmt_short}"


_BINDER = re.compile(r"\(([^\s():]+) :")


def projections(decls: dict[str, FormalDecl]) -> dict[str, str]:
    """Structure field projections present as declarations, mapped to their structure (``DualPair.v -> DualPair``)."""
    return {f"{s}.{f}": s for s, d in decls.items() for f in d.fields
            if f"{s}.{f}" in decls and decls[f"{s}.{f}"].kind != "theorem"}


def _components(name: str) -> list[str]:
    # Lean escapes unusual components with «»; dots inside them are not separators.
    return [c.strip("«»") for c in re.findall(r"«[^»]*»|[^.]+", name)]


def fold_name(name: str, kinds: dict[str, str] | None = None) -> str:
    """Map a constant to the user-facing declaration it was generated for.

    Private prefixes are stripped, internal components (``_proof_1``, ``match_2``, numbers, ``_private``)
    are dropped from the end, and generated structure/inductive companions (``.rec``, ``.mk``, ...) map
    to the type.
    """
    if name.startswith("_private."):
        # _private.<Module>.<n>.<user name>
        parts = _components(name)
        idx = next((i for i, p in enumerate(parts) if p.isdigit()), None)
        name = ".".join(parts[idx + 1 :]) if idx is not None else name
    parts = _components(name)
    while len(parts) > 1 and _INTERNAL_COMPONENT.match(parts[-1]):
        parts.pop()
    if kinds is not None:
        if kinds.get(".".join(parts)) == "constructor" and len(parts) > 1:
            return ".".join(parts[:-1])
        for i in range(1, len(parts)):
            if parts[i] in _GENERATED_SUFFIXES and kinds.get(".".join(parts[:i])) == "inductive":
                return ".".join(parts[:i])
    return ".".join(parts)


@dataclass
class FormalDecl:
    name: str
    kind: str
    module: str
    line: int | None
    type_deps: set[str] = field(default_factory=set)
    value_deps: set[str] = field(default_factory=set)
    members: list[str] = field(default_factory=list)
    type_size: int = 0
    """Size of the statement (distinct ``Expr`` objects), from the declaration itself."""
    value_size: int = 0
    """Size of the proof / body, summed over the declaration and its folded auxiliaries."""
    private: bool = False
    doc: str | None = None
    type_pp: str = ""
    """Pretty-printed statement (Lean syntax), when the dump has it."""
    stmt_short: str = ""
    """Short statement: explicit hypotheses and conclusion only."""
    value_pp: str = ""
    """For a definition: its pretty-printed body, when the dump has it."""
    external: bool = False
    """Declared outside the project (e.g. upstreamed to Mathlib) but named by the blueprint."""
    fields: list[str] = field(default_factory=list)
    """For a structure (single-constructor inductive): the named explicit fields of its constructor."""
    ctor_pp: str = ""
    """For a structure: its constructor's pretty-printed type, i.e. every field with its type."""


def load_decls(path: str | Path, external: bool = False) -> dict[str, FormalDecl]:
    """Load ``extract_deps`` output and fold auxiliaries into user-facing declarations.

    Dumps made with ``--extra`` also hold *external* records: declarations outside the project (typically results
    upstreamed to Mathlib) that the blueprint names. They are skipped unless ``external`` is set, so blueprint-free
    analyses see only the project. Their ``blueprint_reach`` (other blueprint-named external declarations reached
    through non-project constants) counts as a proof dependency.
    """
    rows = [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
    if not external:
        rows = [r for r in rows if not r.get("external")]
    kinds = {r["name"]: r["kind"] for r in rows}
    ctors: dict[str, list[dict]] = {}
    for r in rows:
        if r["kind"] == "constructor":
            ctors.setdefault(fold_name(r["name"], kinds), []).append(r)
    user_names = {r["user_name"] for r in rows}
    decls: dict[str, FormalDecl] = {}
    for r in rows:
        if any(c.startswith(("_aux", "_unexpand", "_delab")) for c in _components(r["user_name"])):
            continue  # notation / macro plumbing, not mathematics
        target = fold_name(r["name"], kinds)
        if target != r["user_name"] and target not in user_names:
            continue  # auxiliary of something that is not a declaration here
        d = decls.get(target)
        if d is None:
            d = decls[target] = FormalDecl(target, r["kind"], r["module"], r["line"])
        if r["user_name"] == target:  # the declaration itself, not one of its auxiliaries
            d.kind, d.module = r["kind"], r["module"]
            d.line = r["line"] if r["line"] is not None else d.line
            d.type_size = r.get("type_size", 0)
            d.private = r["private"]
            d.doc = r.get("doc")
            d.type_pp = r.get("type_pp", "")
            d.stmt_short = restore_fintype(r.get("stmt_short", ""), d.type_pp)
            d.value_pp = r.get("value_pp", "")
            d.external = bool(r.get("external"))
        d.value_size += r.get("value_size", 0)
        d.members.append(r["name"])
        d.type_deps.update(fold_name(x, kinds) for x in r["type_deps"])
        d.value_deps.update(fold_name(x, kinds) for x in r["value_deps"])
        d.value_deps.update(r.get("blueprint_reach", []))
    for target, rs in ctors.items():
        if target in decls and len(rs) == 1:  # a structure: its constructor's explicit binders are the fields
            decls[target].fields = list(dict.fromkeys(_BINDER.findall(rs[0].get("type_pp", ""))))
            decls[target].ctor_pp = rs[0].get("type_pp", "")
    for d in decls.values():
        d.type_deps.discard(d.name)
        d.value_deps.discard(d.name)
    return decls


def formal_graph(decls: dict[str, FormalDecl], include_type: bool = True, include_value: bool = True) -> nx.DiGraph:
    """Project-local graph: edge ``u -> v`` when declaration ``v`` uses project declaration ``u``."""
    g = nx.DiGraph()
    for d in decls.values():
        g.add_node(d.name, kind=d.kind, module=d.module, line=d.line)
    for d in decls.values():
        deps = (d.type_deps if include_type else set()) | (d.value_deps if include_value else set())
        for u in deps:
            if u in decls:
                g.add_edge(u, d.name)
    return g


@dataclass
class BlueprintJoin:
    """Blueprint nodes mapped onto formal declarations."""

    node_decls: dict[str, list[str]]
    """Blueprint node id -> formal declarations it names that exist in the project."""
    missing: dict[str, list[str]]
    """Blueprint node id -> ``\\lean`` names not found among project declarations (upstreamed, renamed, typo)."""

    @property
    def coverage(self) -> float:
        found = sum(len(v) for v in self.node_decls.values())
        total = found + sum(len(v) for v in self.missing.values())
        return found / total if total else 0.0


def join_blueprint(bp: Blueprint, decls: dict[str, FormalDecl]) -> BlueprintJoin:
    node_decls: dict[str, list[str]] = {}
    missing: dict[str, list[str]] = {}
    for n in bp.nodes:
        for name in n.lean_decls:
            target = name if name in decls else fold_name(name)
            if target in decls:
                node_decls.setdefault(n.id, []).append(target)
            else:
                missing.setdefault(n.id, []).append(name)
    return BlueprintJoin(node_decls, missing)


def projected_graph(bp: Blueprint, fg: nx.DiGraph, join: BlueprintJoin) -> nx.DiGraph:
    """Blueprint-node graph whose edges come from Lean, not from ``\\uses``.

    ``B -> A`` when some declaration of ``A`` depends on a declaration of ``B``, either directly or
    through a chain of project declarations that belong to no blueprint node (helper lemmas the
    blueprint never mentions). Nodes without any formal declaration are kept as isolated nodes.
    """
    owner: dict[str, str] = {}
    for node, ds in join.node_decls.items():
        for d in ds:
            owner.setdefault(d, node)
    g = nx.DiGraph()
    for n in bp.nodes:
        g.add_node(n.id, kind=n.kind, chapter=n.chapter, position=n.position)
    for node, ds in join.node_decls.items():
        seen: set[str] = set()
        stack = [p for d in ds for p in fg.predecessors(d)]
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            src = owner.get(u)
            if src is not None:
                if src != node:
                    g.add_edge(src, node)
                continue  # stop at labelled declarations: their own deps belong to them
            stack.extend(fg.predecessors(u))
    return g
