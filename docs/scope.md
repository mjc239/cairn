# Cairn: scope

*Status: Phase 0 done on PFR (see [`phase0-pfr.md`](phase0-pfr.md)). Source notes: [`idea-notes.md`](idea-notes.md).*

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

### Phase 0: blueprint-only analysis (no Lean build) ✅ done for PFR

**Result:** in every scope the human order beats all sampled valid orders on working-memory
load, and it is near the local-search optimum within chapters. Across chapters, grouping by
topic beats load minimisation. Details and caveats: [`phase0-pfr.md`](phase0-pfr.md).
Run with `cairn phase0 <blueprint/src> ...` or `scripts/phase0_pfr.sh`.

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
2. **Decision: write our own small metaprogram** (see §8.2). Don't adopt LeanDojo or jixia.
3. Join with the blueprint via the `\lean{}` names to get a formal graph with a
   partial human labelling.

Cost: building PFR (75 files, about 13k lines of Lean on toolchain `v4.35.0-rc2`)
needs the prebuilt Mathlib cache (`lake exe cache get`, several GB) and then a
compile of PFR itself. About 86% of the blueprint's `\lean{}` names (220 of 255)
are still defined in PFR; the rest have been upstreamed to Mathlib or renamed.

**Blocked in the current cloud environment:** its network policy denies
`release.lean-lang.org` (the Lean toolchain download). Toolchain and cache
downloads need that host, GitHub release assets and the Mathlib cache host
allowed in the environment's network settings. Alternatively, build locally and
commit only the extracted JSONL.

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

Start with PFR: finished, one uniform blueprint, 218 nodes, and a medium-sized Lean project. Then add projects that use
leanblueprint, for example the PrimeNumberTheoremAnd, FLT, Carleson,
Sphere Eversion and the Infinitely-many-primes demo. Verify each one's licence,
toolchain and blueprint conventions before adding it; this list has not been
checked.

## 6. Repo layout

```
cairn/
  docs/                 # these notes
  python/cairn/
    blueprint.py        # LaTeX → nodes/edges/order            (exists)
    graph.py            # orders, null models, metrics         (exists)
    phase0.py, plots.py # Phase 0 analysis + report            (exists)
    cli.py              # `cairn parse`, `cairn phase0`         (exists)
  python/tests/         # pytest, incl. a tiny fixture blueprint (exists)
  scripts/              # pinned reproduction scripts          (exists)
  results/              # committed reports and figures        (exists)
  lean/CairnExtract/    # Phase 1 metaprogram                  (next)
  data/raw/             # pinned project clones (gitignored)
```

Python ≥3.11 with `networkx`, `matplotlib`, `pytest`, managed by `uv`.

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

## 8. Decisions

1. **Output: a reusable tool.** Everything lives in the `cairn` package and CLI
   and runs on any leanblueprint project. Reports are generated, not hand-edited.
2. **Lean extraction: our own minimal metaprogram**, run with
   `lake env lean --run` inside each target project. What we need is small: for
   each project declaration, the constants used in its type and value, with
   compiler auxiliaries (`_proof_n`, `match_n`, `_eq_n`, …) folded into their
   parents. That is roughly 100 lines over `Environment` and
   `Expr.getUsedConstants`. It has to compile against each project's own
   (often release-candidate) toolchain, and a tiny script is the easiest thing
   to keep working across versions. LeanDojo traces whole repositories, is slow,
   and lags new Lean releases. jixia gives much more (syntax, tactic-level
   data) than a dependency graph needs. doc-gen4 and `checkdecls` don't give
   declaration-level dependencies. Revisit if tactic-level hardness signals
   (Phase 2c) need per-step data.
3. **Compute:** see Phase 1. The cloud environment needs Lean hosts allowed
   before it can build, or the build runs locally.
4. **LLM baseline:** use the current Claude model.
