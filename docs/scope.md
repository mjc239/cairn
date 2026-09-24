# Cairn: scope

*Status: Phases 0–2 done on PFR (see [`phase0-pfr.md`](phase0-pfr.md), [`phase1-pfr.md`](phase1-pfr.md), [`phase2-pfr.md`](phase2-pfr.md)) and repeated on Carleson, with a cross-project comparison in [`carleson.md`](carleson.md). Source notes: [`idea-notes.md`](idea-notes.md).*

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

### Phase 1: formal graph extraction ✅ done for PFR

**Result:** 98% of blueprint `\lean{}` names resolve. Author `\uses` links are 87%
confirmed by Lean but record only about a third of Lean's links (most omissions
are definitions and workhorse lemmas). The human order still beats every random
order, but on Lean links a naive just-in-time order matches it in three
chapters. Details: [`phase1-pfr.md`](phase1-pfr.md).

1. [`lean/extract_deps.lean`](../lean/extract_deps.lean): run with
   `lake env lean --run` inside the built project. It emits JSON Lines with each
   constant's kind, module, source line and the constants used in its type and
   its value.
2. `cairn.formal` folds compiler auxiliaries into their parents, builds the
   project-local graph, joins it to the blueprint through `\lean{}` and
   projects it onto blueprint nodes through unlabelled helper declarations.
3. `cairn phase1` compares author and Lean edges and reruns the Phase 0
   ordering analysis on the Lean graph.

Cost in the cloud container: about 2 minutes for `lake exe cache get` (7.5 GB)
and 4 minutes for `lake build PFR` on 4 cores. The extraction itself takes
between 15 seconds and 6 minutes; computing term sizes made one run slow, and
the variance hasn't been investigated. Needs network access to `release.lean-lang.org`, GitHub and
`cache.mathlib.org`. `scripts/phase1_pfr.sh` does all of it.

### Phase 2: baselines and benchmark ✅ first pass done for PFR

**Result:** (c) the combined cheap features give AUROC 0.87 and P@k 61% (base
rate 18%). (a) Lean modules recover the chapters (NMI 0.83) far better than
graph communities (0.58). (b) Within chapters: minimising load gets τ 0.73,
an LLM 0.85, and Lean source order 0.87 (not independent of the blueprint).
Details: [`phase2-pfr.md`](phase2-pfr.md). Run with `cairn phase2` /
`scripts/phase2_pfr.sh`. The LLM baseline works through files
(`cairn llm-prompts`, then `<chapter>.response.json`), so any model can fill
it in. For PFR it was filled by the current Claude model via a subagent, since
this environment has no API key.

Not yet done from the original plan: the automation-hardness probe, IDF
weighting against Mathlib-wide usage, declaration → node pairwise grouping,
and an API-driven LLM runner.

Original design:

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

## 5. Corpus

Done: **PFR** (bottom-up style, one file per chapter) and **Carleson**
(paper-style narrative, one file split into `\section`s, `--group-by section`).

Surveyed on 2026-09-24 as further candidates (nodes / formalised):
- sphere-eversion (73 / 73, finished, 5 chapters);
- LeanAPAP (49 / 37);
- brownian-motion (663 / 361, in progress);
- FLT (255 / 165, in progress).

PrimeNumberTheoremAnd and flt-regular use a different blueprint layout that
the parser doesn't read yet.

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
2. **Lean extraction: our own minimal metaprogram** (implemented: `lean/extract_deps.lean`, about 70 lines), run with
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
3. **Compute:** the cloud container is enough. With network access enabled,
   PFR builds from the Mathlib cache in about 7 minutes end to end (see Phase 1).
4. **LLM baseline:** use the current Claude model.
