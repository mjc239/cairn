# Phase 2 findings: PFR baselines

*Data: the Phase 1 Lean dump of PFR (`results/phase1/pfr/pfr_decls.jsonl.gz`,
which now includes statement and proof sizes) plus the blueprint. Full tables:
[`results/phase2/pfr/phase2.md`](../results/phase2/pfr/phase2.md). Reproduce
with `scripts/phase2_pfr.sh` in about 10 seconds, without Lean.*

Phase 2 asks whether cheap signals from the Lean graph recover the three
decisions a blueprint author made:

- **(c)** which declarations to promote to named results;
- **(a)** how to group them into chapters;
- **(b)** what order to present them in.

## (c) Key declarations: which of 1,395 declarations get a blueprint node?

248 are named, a base rate of 18%. The model is a logistic regression on 15
cheap features, cross-validated with whole Lean modules held out:

| | AUROC | Precision@248 |
|---|---:|---:|
| Random | 0.50 | 18% |
| Best single score (betweenness / number of project lemmas used) | 0.79 | 49–53% |
| Proof size | 0.76 | 46% |
| Dominated declarations (dominator-tree bottlenecks) | 0.62 | 33% |
| **All features combined** | **0.87** | **61%** |

- **The rule of thumb that emerges:** a named result is non-private, has a
  large statement, sits in the middle of the graph (it uses many project
  lemmas and is on many paths) and has a sizeable proof. Library-style
  `ForMathlib` declarations and instances are less likely to be named.
- **Dominators disappoint.** In PFR the formal graph is wide, so few
  declarations are unavoidable bottlenecks. Betweenness captures "on many
  paths" better.
- **The misses are informative.**
  - The top-scoring declarations the blueprint *doesn't* name are mostly
    `_aux`/`_prelim`/primed variants of named results, such as
    `tau_strictly_decreases_aux` and `weak_PFR_asymm_prelim`. These are
    exactly what a human folds into a parent lemma, which points to a
    name-based "variant of" feature as the obvious next step.
  - The lowest-scoring *named* declarations are small foundational facts,
    such as `entropy_le_log_card` and `condEntropy_add_right`. Authors name
    these for exposition even though they are structurally minor.
- **Not yet tried:** the notes' "hardness" signal, i.e. whether
  `simp`/`aesop` can re-prove a declaration from its immediate dependencies.
  It needs Lean runs per declaration. Proof size is a weak stand-in.

## (a) Recovering the 13 chapters

| Method | clusters | ARI | NMI |
|---|---:|---:|---:|
| Lean module of the node's declaration | 28 | 0.60 | 0.83 |
| Louvain communities on the Lean graph | 8 | 0.48 | 0.58 |
| Greedy modularity on the Lean graph | 8 | 0.35 | 0.56 |
| Random (chapter sizes kept) | 13 | 0.00 | 0.14 |

- **Graph structure alone recovers chapters moderately well.** Louvain
  reaches NMI 0.58.
- **The Lean file layout is a much stronger signal.** Modules are
  finer-grained than chapters (28 vs 13) but rarely cross chapter lines. The
  formalisers organised files the way the authors organised chapters.

## (b) Ordering

τ is the Kendall correlation with the human order.

| Order | τ within chapters | mean open (Lean edges) | chapter runs |
|---|---:|---:|---:|
| Human | 1.00 | 45.5 | 13 |
| Random valid order | 0.54 | 63.8 | 163 |
| Just-in-time DFS | 0.47 | 49.0 | 77 |
| Global load optimum | 0.54 | 44.4 | 106 |
| Cluster-then-order (true chapters, load-optimal within) | 0.73 | 44.3 | 13 |
| **LLM within true chapters** (current Claude model) | **0.85** | 45.4 | 13 |
| **Lean source order** (import order, then line) | **0.87** | 56.3 | 25 |

1. **Cluster-then-order is right, but minimising load within a chapter
   explains only part of the human order.** τ 0.73 vs 0.54 for random. The
   load optimum is already slightly *better* than the human order (44.3 vs
   45.5), so humans are optimising something else too.
2. **The LLM captures much of that "something else".** It reaches τ 0.85
   within chapters (≥ 0.73 in every chapter) at the same load as the human
   order, working only from statements and dependency constraints. So the
   residual looks semantic, e.g. "introduce the general tool before its
   special case" or "group by the object being studied", rather than
   graph-structural.
3. **The Lean source order is the closest match, but it isn't independent.**
   It reaches τ 0.87, and 0.91–1.00 in the long chapters, but it is not an
   independent predictor. The blueprint and the Lean files were written
   together, largely in the same order. It is still useful as an upper-bound
   reference and as evidence that the formal development's own layout
   carries most of the expository order. Its load is higher (56.3) because
   modules interleave chapters.

### Caveats

- **Contamination:** the LLM may have seen the PFR paper or blueprint in
  training. The prompts also use the authors' labels as ids (e.g.
  `pfr-9-aux`), which carry hints. It was told not to look anything up and
  could read only its prompt files.
- One project, one LLM run, no repeats. The LLM's τ has unknown variance.
- τ within chapters is inflated by dependency constraints (random is already
  0.54). Compare against that floor, not against 0.

## What this means for the next step

- **Key nodes:** add a "variant of a named result" feature, from names and
  shared statements, and the automation-hardness probe. Both target the
  observed failure modes.
- **Ordering:** combine the two strong signals: cluster by module or
  community, then let an LLM order within clusters, with a load penalty. To
  test for contamination, anonymise the ids and paraphrase the statements.
- **Generalise:** repeat Phases 0–2 on a second blueprint project so that
  none of this rests on PFR alone.
