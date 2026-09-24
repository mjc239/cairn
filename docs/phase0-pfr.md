# Phase 0 findings: PFR blueprint

*Data: [`teorth/pfr`](https://github.com/teorth/pfr) @ `ddd44f6ce82e` (2026-09-20),
`blueprint/src`. Reproduce with `scripts/phase0_pfr.sh`. Full tables:
[`results/phase0/pfr/phase0.md`](../results/phase0/pfr/phase0.md).*

## Question

Take the dependency graph the blueprint authors wrote down (`\uses{}`). Among
all orders that respect it, how good is the order they actually wrote on
working-memory load?

## Setup

- **Graph.** 218 nodes: 145 lemmas, 30 definitions, 18 corollaries,
  15 theorems and 10 propositions. There are 497 edges: 424 proof → uses and
  73 statement → uses. All `\uses` labels resolve.
- **Metrics** (lower is better):
  - *mean open* is the average number of results already stated and still
    needed later. It is the working-memory proxy, a vertex-separation profile.
  - *mean edge length* is how far back the reader has to look on average.
  - *mean cut* and *cutwidth* are also computed.
- **Orders compared:**
  - human, as written;
  - human with forward references repaired;
  - just-in-time DFS, where each lemma comes right before its first use;
  - greedy min-open;
  - greedy followed by a local search on total edge length.
- **Null models:**
  - 1,000 randomised-Kahn topological orders. These are cheap but biased
    towards stating everything available early.
  - 200 approximately uniform topological orders, sampled with the
    Karzanov–Khachiyan adjacent-transposition chain.
- **Scopes:** the whole blueprint, plus each chapter with at least 8 nodes,
  using only the edges inside that chapter.

## Results

![mean open](../results/phase0/pfr/phase0_mean_open.png)

| Scope | n | Mean open: human | optimised | uniform median | Uniform orders better than human | τ(human, optimised) |
|---|---:|---:|---:|---:|---:|---:|
| whole blueprint | 218 | 31.9 | 30.5 | 55.4 | 0% | +0.06 |
| entropy | 30 | 3.3 | 2.8 | 6.6 | 0% | +0.87 |
| distance | 26 | 5.3 | 3.8 | 7.7 | 0% | +0.74 |
| entropy_pfr | 24 | 5.1 | 5.2 | 7.0 | 0% | +0.88 |
| torsion | 49 | 10.7 | 8.4 | 13.5 | 0% | +0.43 |
| further_improvement | 41 | 6.2 | 5.1 | 9.8 | 0% | +0.85 |
| weak_pfr, improved_exponent, approx_hom_pfr | 8–11 | ≈ optimum | | | 0–1% | +0.73 to +1.00 |

1. **The human order is far from random.** In every scope and on every metric
   it beats all 1,200 sampled topological orders. Its load is about 40% below
   the uniform median for the whole document.
2. **It is close to the local optimum.** For the whole document it is within 5%
   (31.9 vs 30.5). *Correction ([`cross_project.md`](cross_project.md)): that
   optimiser minimised edge length, not mean open. Optimising mean open
   directly, and also searching from the author's order, gives 26.2, so the
   human order is about 22% above the best known. It is still far from random
   (55.4). Chapter-level numbers barely change.* In several chapters it matches or beats our optimiser: in
   `entropy_pfr` the human order scores 5.1 and the optimiser 5.2.
3. **Inside a chapter, low load and the human order largely coincide.** The
   order our optimiser finds has τ = 0.74–0.88 with the human order in most
   chapters. Even random valid orders have τ of about 0.4–0.5, because the
   dependency constraints already fix a lot. So judge τ against that baseline,
   not against 0.
4. **Across chapters, working memory is not the organising principle.** The
   whole-document optimum reaches the human's load only by breaking the 13
   chapters into 85 same-chapter runs, and its τ with the human order is 0.06.
   Humans group material by topic or result, then minimise load within each
   group. This is direct evidence that **clustering** (task (a)) is a separate
   signal from **ordering**, as the notes guessed.
5. **Torsion is the outlier.** τ is only 0.43 and the human load is 10.7 vs an
   optimum of 8.4. This is the chapter to read by hand for what else drives the
   order there, such as narrative, "no node before the goal it serves", or
   history.
6. **Forward references are rare.** There are 2 in the whole blueprint, both to
   `pfr-9-aux'` from later "hom-PFR" corollaries. The authors almost always
   write in dependency order.

## Caveats (important)

- **The graph is circular evidence.** The same authors wrote both the `\uses`
  edges and the order. Blueprint edges are sparse and written with the text in
  front of the author. They may under-report long-range dependencies, which
  would flatter the human order's edge lengths. Phase 1's formal graph, which
  is independent of the author, removes this.
- The uniform null is approximate: the chain is thinned at 4n² steps, below the
  O(n³ log n) mixing bound. Both nulls agree qualitatively.
- "Optimised" is a local search from a greedy start, not a true optimum. The
  human order can only be claimed *near*-optimal relative to it.
- One project. PFR's chapters are uneven in size (3–49 nodes), and the small
  ones have few valid orders to compare against.

## What this means for the plan

- The working-memory hypothesis holds up *within* chapters, so a cutwidth-style
  objective is a reasonable ordering baseline for Phase 2.
- A readable-proof generator needs a **cluster-then-order** structure. Ordering
  alone on the full graph produces a low-load but interleaved, unreadable
  document.
- Next steps are Phase 1, to re-test all of this on the Lean graph, and a hand
  read of `torsion`.
