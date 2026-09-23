# Cairn: scope

*Status: scoping. Source notes: [`idea-notes.md`](idea-notes.md).*

## 1. The question

The notes cover a lot: RL for clarity, motivated explanations, certified wrong
turns. The first piece we can actually test is narrower:

> **Given the formal dependency graph of a verified proof, can cheap graph
> heuristics recover the structure a human expositor chose: which declarations
> they grouped into one lemma, which they promoted to named results, and the
> order they presented them in?**

Lean blueprints give this question ground truth. Each blueprint is a human
exposition whose lemmas are linked to Lean declarations. Either answer is useful:

- **Heuristics match human structure** (e.g. human order ≈ low cutwidth). That is
  a finding in its own right: expositors minimise working-memory load, and a
  readable-proof generator can start from these heuristics.
- **Heuristics fall short.** The residual measures exactly what a learned model
  (or an LLM) has to supply. That justifies the later phases and gives them a
  benchmark.

## 2. In scope and out of scope

| In scope now (Phases 0–2) | Deferred (Phase 3+) | Out of scope |
|---|---|---|
| Parsing blueprints into graphs | Learned ordering / clustering models | Training RL clarity models |
| Extracting Lean declaration dependency graphs | LLM-generated prose for a chosen structure | Building a new prover |
| Ordering, clustering and key-node baselines | *Augment* step (motivation, special cases) | Replacing blueprints / leanblueprint |
| A benchmark with metrics and null models | Certified wrong turns (formalised counterexamples) | "Why this theorem" / outward context |

## 3. What the data looks like (checked against PFR)

A shallow clone of [`teorth/pfr`](https://github.com/teorth/pfr) (toolchain
`v4.35.0-rc2`) shows:

- 14 chapter files and ~218 `lemma/theorem/proposition/corollary/definition`
  environments.
- 212 `\lean{...}` tags naming ~255 declarations. **One blueprint node often
  maps to several Lean declarations** (e.g. `shear-ent` →
  `condEntropy_add_right`, `_add_left`, `_sub_right`, `_sub_left`). These are
  the clustering labels for task (a).
- `\uses{...}` in two places: ~36 in statements (the statement depends on a
  definition) and ~167 in proofs (the proof depends on lemmas). These are
  different edge types, and the parser should keep them apart.
- Only a handful of nodes have no `\lean{}`.
- Human linear order = order of `\input` in `main.tex`, then order within each
  file.

Wrinkles the parser and graph extractor must handle:

- Declarations get upstreamed to Mathlib and renamed (many PFR nodes now point to
  `ProbabilityTheory.*`). Resolve names against the pinned toolchain, and record
  which declarations the project defines itself and which it imports. That split
  is also the "novelty" signal.
- Blueprint `\uses` edges are written by hand and coarse. Formal edges are
  fine-grained and noisy (auxiliary `_proof_n` / `match_n` declarations,
  instance arguments, tactic-introduced library lemmas).
- Blueprints change over time. Pin a commit per project.

## 4. Phases

### Phase 0: blueprint-only analysis (no Lean build) ✅ start here

Needs only a Python LaTeX parser. It answers the cheapest question first.

1. Parse a blueprint into nodes (label, kind, title, `\lean` decls, `\leanok`)
   and typed edges (statement-uses and proof-uses), plus the document order.
2. On the **blueprint graph itself**: is the human order a topological sort?
   (Count and inspect the forward references.) Compute its cutwidth and compare
   it with the distribution over random topological sorts and with the
   cutwidth-heuristic order.
3. Output: one plot and one number per project, "human order sits at the Nth
   percentile of cutwidth among valid orders".

If human order is no better than random, the working-memory hypothesis is
already in trouble. That would be worth knowing before building the Lean side.

### Phase 1: formal graph extraction

1. A Lean 4 metaprogram run against the built project. For each declaration in
   the project namespace it collects the constants used in its type and value
   (`Expr.getUsedConstants`, filtering auxiliary declarations and mapping them to
   their parent). Output: JSONL of `{name, module, kind, type_deps, value_deps,
   is_project_local}`.
2. Check the existing tools before writing our own: LeanDojo, `jixia`,
   doc-gen4's dependency data, leanblueprint's `checkdecls`.
3. Join with the blueprint via the `\lean{}` names to get a formal graph with a
   partial human labelling.

Cost warning: building PFR needs the Mathlib cache (`lake exe cache get`), which
takes several GB and a fair amount of wall-clock time. Worth a setup script or
container.

### Phase 2: baselines and benchmark

The input is the formal graph restricted to project-local declarations. The
three tasks:

| Task | Target | Baselines | Metric |
|---|---|---|---|
| (a) Clustering | Blueprint grouping of declarations | Connected components after contracting single-use lemmas; community detection; name-prefix grouping | ARI / NMI, pairwise F1 |
| (b) Ordering | Blueprint order (projected to shared nodes) | Random topo sort (null); cutwidth heuristic; DFS/BFS from the goal; LLM-chosen order | Kendall τ, forward-reference count, cutwidth |
| (c) Key nodes | Declarations the blueprint names as a node | In-degree, PageRank (IDF-weighted against Mathlib usage); dominators; min vertex cuts; betweenness; hardness (does `simp`/`aesop`/`omega` close it from its immediate deps?); proof-size/statement-size | P/R@k, AUROC |

Report every metric against the random-topological-sort null, not in absolute
terms.

### Phase 3: learned models / generation (not scoped yet)

Scope this only after Phase 2 shows how much residual there is. Candidates
include an LLM scoring or reranking orders, a model trained on blueprint
structure with held-out projects, and prose generation over a fixed structure.
There are only a few dozen serious blueprints, so treat them as an **evaluation
set**, not a training set.

## 5. Corpus candidates

Start with PFR, which is small, finished and uniform. Then add projects that use
leanblueprint, for example the PrimeNumberTheoremAnd, FLT, Carleson,
Sphere Eversion and the Infinitely-many-primes demo. Verify each one's licence,
toolchain and blueprint conventions before adding it; this list has not been
checked.

## 6. Proposed repo layout (created when the first code lands)

```
cairn/
  docs/                 # these notes
  python/cairn/
    blueprint.py        # LaTeX → nodes/edges/order
    graph.py            # graph utils, topo-sort sampling, cutwidth
    baselines/          # ordering, clustering, key-node scorers
    eval.py             # metrics + null models
  lean/CairnExtract/    # Lean metaprogram for formal dependency graphs
  data/                 # pinned project commits (gitignored raw clones)
  notebooks/            # exploratory analysis
```

Python ≥3.11 with `networkx`, `pydantic`, `pytest`, managed by `uv`.

## 7. Risks

- **Blueprint order ≠ reading order.** Blueprints are often written as project
  plans. Their order can reflect how the formalisation work was split up rather
  than how the argument should be presented. Mitigation: also compare against
  the source paper's order for PFR (arXiv 2311.05762) on the shared lemmas.
- **Name-mapping drift** (upstreamed or renamed declarations) quietly loses
  labels. Mitigation: report coverage for every project.
- **Tactic-proof noise.** Value dependencies over-count library lemmas that
  automation pulled in. Mitigation: IDF weighting and a project-local
  restriction, plus an ablation using type dependencies only.
- **Small N.** A few projects means per-project results, not pooled
  significance.

## 8. Open decisions

1. **Goal of the output**: a short write-up or blog post (maybe sent to Massot
   or Tao), a reusable tool, or a paper? This decides how polished Phase 2
   needs to be.
2. **Lean extraction**: write our own metaprogram or adopt LeanDojo/jixia?
   Decide after a half-day spike.
3. **Compute**: local build of PFR + Mathlib, or a prepared container?
4. **LLM baseline**: which model and budget for the "LLM-chosen order" baseline
   in task (b).
