# cairn

*Clarifying Arguments by Identifying Relevant Nodes.*

Cairn aims to turn verified proofs (from Lean, or from an AI prover) into proofs
a person can read. A formal proof already fixes a dependency DAG, and any
topological sort of it is a valid proof. Cairn treats readability as a search
over how to present that DAG: how to **order** the results, **cluster** them,
**name** them, **elide** routine steps and **augment** them with motivation.
Correctness is guaranteed by the formal proof throughout.

**Status:** Phases 0 (blueprint graph), 1 (Lean dependency graph) and 2 (baselines) done on PFR
and Carleson. Findings: [`docs/phase0-pfr.md`](docs/phase0-pfr.md), [`docs/phase1-pfr.md`](docs/phase1-pfr.md),
[`docs/phase2-pfr.md`](docs/phase2-pfr.md), the cross-project comparison in
[`docs/carleson.md`](docs/carleson.md), and the statement/proof model of load vs motivation in
[`docs/statement-proof-events.md`](docs/statement-proof-events.md).

- [`docs/idea-notes.md`](docs/idea-notes.md): the original idea notes (motivation,
  challenges, graph formulation, prior work).
- [`docs/scope.md`](docs/scope.md): what we're building first, the phases, the
  benchmark design, risks and open decisions.

## Usage

```sh
uv sync
uv run cairn parse  path/to/project/blueprint/src -o graph.json   # nodes, typed \uses edges, document order
uv run cairn phase0 path/to/project/blueprint/src --project NAME -o results/phase0/NAME
./scripts/phase0_pfr.sh                                          # reproduce the PFR report

# Phase 1: Lean dependencies (needs elan; run inside the built Lean project)
lake env lean --run /path/to/cairn/lean/extract_deps.lean RootModule ModulePrefix... > decls.jsonl
uv run cairn phase1 path/to/project/blueprint/src decls.jsonl --project NAME -o results/phase1/NAME
./scripts/phase1_pfr.sh                                          # build PFR + extract + analyse (~7-13 min)

# Phase 2: key declarations, chapter clustering, ordering baselines
uv run cairn llm-prompts path/to/blueprint/src decls.jsonl -o results/phase2/NAME/llm   # then fill *.response.json
uv run cairn phase2 path/to/blueprint/src decls.jsonl --project NAME --llm-dir results/phase2/NAME/llm -o results/phase2/NAME
./scripts/phase2_pfr.sh                                          # from the committed dump, no Lean needed
uv run cairn llm-prompts ... --anonymise --no-titles --seed N    # blind LLM prompts; score runs with `cairn llm-eval`
uv run cairn transfer --project A=SRC:DECLS --project B=SRC:DECLS:section -o out.json   # cross-project key decls

./scripts/carleson.sh [--no-lean]                                # all phases on the second project
uv run cairn events path/to/blueprint/src decls.jsonl --project NAME -o results/events/NAME  # statements vs proofs, motivation
uv run cairn event-prompts ... -o DIR [--anonymise --no-titles]  # LLM orders S:/P: steps; score with `cairn event-llm-eval`
uv run pytest && uv run ruff check python
```

In Claude Code on the web, `.claude/hooks/session-start.sh` installs the Python deps and the
Lean toolchain at session start.

The entry file defaults to `content.tex` and falls back to `chapter/main.tex`
(pass `--entry` otherwise). For single-file blueprints, `--group-by section` (or `chapter`) treats
`\section`s as chapters.

## Plan

First milestone: use Lean blueprints (starting with
[PFR](https://github.com/teorth/pfr)) as ground truth, and test whether cheap
graph heuristics such as cutwidth, dominators and IDF-weighted centrality
recover how human expositors ordered, grouped and named the lemmas.
