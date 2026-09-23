# cairn

*Clarifying Arguments by Identifying Relevant Nodes.*

Cairn aims to turn verified proofs (from Lean, or from an AI prover) into proofs
a person can read. A formal proof already fixes a dependency DAG, and any
topological sort of it is a valid proof. Cairn treats readability as a search
over how to present that DAG: how to **order** the results, **cluster** them,
**name** them, **elide** routine steps and **augment** them with motivation.
Correctness is guaranteed by the formal proof throughout.

**Status:** scoping, no code yet.

- [`docs/idea-notes.md`](docs/idea-notes.md): the original idea notes (motivation,
  challenges, graph formulation, prior work).
- [`docs/scope.md`](docs/scope.md): what we're building first, the phases, the
  benchmark design, risks and open decisions.

First milestone: use Lean blueprints (starting with
[PFR](https://github.com/teorth/pfr)) as ground truth, and test whether cheap
graph heuristics such as cutwidth, dominators and IDF-weighted centrality
recover how human expositors ordered, grouped and named the lemmas.
