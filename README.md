# cairn

*Clarifying Arguments by Identifying Relevant Nodes.*

Cairn aims to turn verified proofs (from Lean, or from an AI prover) into proofs
a person can read. A formal proof already fixes a dependency DAG, and any
topological sort of it is a valid proof. Cairn treats readability as a search
over how to present that DAG: how to **order** the results, **cluster** them,
**name** them, **elide** routine steps and **augment** them with motivation.
Correctness is guaranteed by the formal proof throughout.

**Status:** Phase 0 (blueprint-only analysis) done on PFR. Findings: [`docs/phase0-pfr.md`](docs/phase0-pfr.md).

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
uv run pytest
```

The entry file defaults to `content.tex` and falls back to `chapter/main.tex`
(pass `--entry` otherwise).

## Plan

First milestone: use Lean blueprints (starting with
[PFR](https://github.com/teorth/pfr)) as ground truth, and test whether cheap
graph heuristics such as cutwidth, dominators and IDF-weighted centrality
recover how human expositors ordered, grouped and named the lemmas.
