# Cross-project results: a scalable optimiser, and models trained on 9 projects

*Code: `python/cairn/graph.py` (`local_search_order(objective="open")`), `python/cairn/phase0.py`,
`python/cairn/phase2.py` (`leave_one_out_key_nodes`) and `scripts/cross_project.py`. Results:
Phase 0 reports in `results/phase0/{pfr,carleson}/` and `results/harvest/<project>/phase0/`,
[`results/cross_project/key_node_loo.md`](../results/cross_project/key_node_loo.md), style fits in
`results/harvest/<project>/style/`. The model trained on all 9 projects is
`results/outline/key_model_all.json`.*

This builds on the 20 harvested blueprints in [`harvest.md`](harvest.md), and
does two things:

1. makes the order optimiser scale, and redoes the order-vs-load comparison;
2. retrains the key-declaration model, and fits exposition styles, on the
   well-linked projects instead of PFR and Carleson alone.

## 1. An optimiser that scales

**The problem.** On Brownian motion (663 nodes), our "optimised" order held
59.1 results open on average against the authors' 39.7. Two causes:

- **Wrong objective.** The local search minimised total edge length (mean
  cut), but the reports compare *mean open results*. The two agree on small
  graphs and drift apart on large ones.
- **Weak starts.** It started only from greedy orders, and those get worse as
  graphs grow (84 open on Brownian motion).

**The fix.**
- **Search on the reported metric.** Mean open × (n − 1) is the sum, over
  results, of (position of last use − position stated). Swapping two adjacent,
  unrelated results changes it by an amount computed from their immediate
  neighbours alone. A test checks this against brute force on every adjacent
  swap of random graphs. The local search slides each result through its
  valid window, using these exact deltas.
- **A best-known order.** Phase 0 now reports two orders:
  - `optimised`: from greedy starts only. It is independent of the author, so τ
    against it still says how closely the author follows an optimum.
  - `best_known`: the better of that and a local search started from the
    author's own (forward-repaired) order. It is the reference for the gap,
    and an upper bound on the true optimum.

On Brownian motion, the greedy-start optimum drops from 59.1 to 42.0 and the
best known to 29.7. Phase 0 on 663 nodes takes about 5.5 minutes.

### Order vs load, all 20 blueprints

*Gap* = (human − best known) / (uniform random − best known), on mean open
results: 0 means as light as the best order known, 1 means no better than a
random valid order. "Chapter gap" is the median over chapters with at least 5
nodes. Iwasawa (15 nodes, 3 edges) is too small to score.

| Project | Nodes | Forward refs | Mean open: human / greedy-start optimum / best known / random | Gap | Chapter gap (n) |
|---|---:|---:|---|---:|---|
| brownian_motion | 663 | 15 | 39.7 / 42.0 / 29.7 / 145.1 | 0.09 | 0.21 (14) |
| testing_lower_bounds | 344 | 28 | 32.8 / 25.9 / 25.9 / 61.7 | 0.19 | 0.49 (12) |
| *PFR* | 218 | 2 | 31.9 / 27.4 / 26.2 / 55.4 | 0.20 | 0.17 (8) |
| semicircle | 205 | 5 | 14.6 / 12.5 / 9.7 / 41.6 | 0.15 | 0.17 (4) |
| formal_book | 192 | 11 | 1.2 / 1.5 / 1.0 / 32.8 | 0.01 | 0.52 (8) |
| *Carleson* | 180 | 90 | 16.6 / 10.7 / 9.3 / 39.2 | 0.24 | 1.26 (7) |
| con_nf | 159 | 2 | 15.1 / 13.1 / 13.1 / 29.4 | 0.12 | 0.21 (7) |
| toric | 145 | 7 | 17.7 / 9.9 / 9.9 / 36.2 | 0.30 | 0.80 (7) |
| sphere_packing | 141 | 13 | 15.7 / 13.1 / 13.1 / 33.2 | 0.13 | 0.11 (5) |
| flt3 | 92 | 0 | 16.0 / 10.4 / 10.4 / 20.4 | 0.56 | 0.26 (2) |
| sphere_eversion | 73 | 11 | 7.9 / 7.0 / 7.0 / 20.4 | 0.07 | 0.46 (4) |
| bonn_analysis | 65 | 0 | 1.2 / 1.0 / 1.0 / 5.1 | 0.06 | 1.00 (3) |
| abc_exceptions | 58 | 12 | 9.8 / 8.6 / 8.6 / 13.4 | 0.25 | 1.03 (2) |
| clt | 50 | 0 | 8.8 / 5.7 / 5.7 / 14.2 | 0.37 | 0.76 (4) |
| apap | 49 | 0 | 5.3 / 5.0 / 4.3 / 11.8 | 0.13 | 0.24 (4) |
| flt_regular | 45 | 1 | 3.7 / 3.5 / 3.2 / 12.0 | 0.05 | 0.32 (4) |
| infinity_cosmos | 41 | 0 | 4.4 / 1.4 / 1.4 / 7.3 | 0.50 | 0.56 (2) |
| chandra_furst_lipton | 31 | 0 | 7.7 / 5.7 / 5.7 / 8.9 | 0.61 | 1.00 (1) |
| banach_tarski | 30 | 1 | 4.4 / 4.0 / 3.6 / 8.0 | 0.18 | 0.14 (1) |
| zeta3 | 30 | 0 | 5.2 / 4.0 / 4.0 / 8.3 | 0.30 | 0.30 (1) |

- **No author beats the optimiser any more.** Brownian motion, semicircle,
  sphere eversion and FormalBook had negative gaps before; that was the old
  optimiser's weakness.
- **Authors are close to, but not at, the load optimum.** The median author
  order holds 25% more results open than the best known (range 14%–213%), and
  the median gap is 0.19. For comparison, random orders are typically 2–5
  times heavier than the best known (1.6–33 times). 16 of the 20 blueprints have a gap of 0.3 or less.
- **The earlier "within 5% of optimal" was too generous.** PFR's gap rises from
  0.06 to 0.20 (human 31.9 against a best known of 26.2) and Carleson's from
  0.13 to 0.24. The qualitative reading stands: authors order whole documents
  much closer to the optimum than to random. But there is real room left, and
  that room is what an optimiser could offer a reader.
- **Within chapters, little changes.** Small scopes were already near-optimal
  for the old search. The split between dependency-order and paper-order
  authors stands: chapter gaps around 0.1–0.3 for most projects, about 1 for
  Carleson, ABC, Bonn and Chandra–Furst–Lipton.
- **Searching from the author's order helps on the biggest documents.** It finds
  a better order than any greedy start on 8 of the 20 blueprints, including
  PFR, Carleson and Brownian motion. On Brownian motion the gain is large (42.0
  to 29.7). Starting from an author's order is a good way to improve it for
  readers.

## 2. Key-declaration model on 9 projects

**Training projects** have blueprints mostly linked to Lean (at least half the
nodes) and at least 30 blueprint-named declarations inside the project:

- PFR and Carleson
- Brownian motion, testing lower bounds, sphere packing, FLT3, sphere eversion,
  ABC and APAP

Other projects are scored as *held out*. Their unlinked nodes make "not named"
unreliable as a negative label for training, but it's still informative for
evaluation.

**Leave one project out.** Each training project is scored by a model trained
on the other 8. Each held-out project is scored by the model trained on all 9.
*Baseline* is the previous model, trained on PFR and Carleson (minus the
project itself). P@k is precision among the top k, with k the number of named
declarations.

| Project | Role | Named / decls | AUROC | P@k | Baseline AUROC | Baseline P@k |
|---|---|---|---:|---:|---:|---:|
| PFR | train | 248 / 1395 | 0.82 | 57% | 0.79 | 50% |
| Carleson | train | 236 / 3422 | 0.86 | 34% | 0.85 | 30% |
| brownian_motion | train | 325 / 2222 | 0.70 | 30% | 0.68 | 28% |
| testing_lower_bounds | train | 126 / 1035 | 0.67 | 26% | 0.63 | 24% |
| sphere_packing | train | 100 / 1468 | 0.79 | 33% | 0.74 | 30% |
| flt3 | train | 90 / 235 | 0.73 | 57% | 0.68 | 54% |
| sphere_eversion | train | 80 / 1378 | 0.86 | 32% | 0.82 | 30% |
| abc_exceptions | train | 49 / 248 | 0.81 | 49% | 0.77 | 43% |
| apap | train | 34 / 769 | 0.93 | 65% | 0.89 | 68% |
| con_nf | held out | 57 / 1998 | 0.81 | 9% | 0.71 | 2% |
| toric | held out | 29 / 276 | 0.71 | 28% | 0.55 | 14% |
| chandra_furst_lipton | held out | 15 / 29 | 0.91 | 80% | 0.68 | 60% |
| flt_regular | held out | 12 / 295 | 0.73 | 17% | 0.65 | 8% |
| iwasawa | held out | 10 / 950 | 0.83 | 10% | 0.55 | 0% |
| bonn_analysis | held out | 8 / 393 | 0.81 | 12% | 0.78 | 25% |
| semicircle | held out | 59 / 229 | 0.68 | 44% | 0.72 | 51% |
| formal_book | held out | 68 / 507 | 0.56 | 16% | 0.60 | 18% |
| clt | held out | 7 / 26 | 0.67 | 29% | 0.75 | 43% |

- **More projects help everywhere they can be measured cleanly.** AUROC rises on
  all 9 training projects, from a mean of 0.76 to 0.80. P@k rises on 8 of 9.
- **Held-out projects improve on average** (mean AUROC 0.67 to 0.75), most on
  Toric, Iwasawa and Chandra–Furst–Lipton.
- **Three held-out projects get slightly worse:** semicircle, FormalBook and
  CLT. They are the ones with the least reliable labels:
  - semicircle links 28% of its nodes;
  - FormalBook has `sorry` in 30 of its 68 named theorems;
  - CLT has 7 named declarations among 26.
- **What is named still varies by author.** Brownian motion and testing lower
  bounds, the two largest, are among the hardest (AUROC 0.67–0.70): their
  blueprints name many mid-level lemmas that look structurally like helpers.

`results/outline/key_model_all.json` is trained on all 9 projects. It is the
model to use for outlining a new project; `cairn outline --model` takes it
directly.

## 3. Exposition styles, 9 projects

The style fit ([`style.md`](style.md)) finds the style parameters that best
reproduce each author's order. It is run here with `--external`, so nodes
linked only through Mathlib count. *Motivated*: the share of lemmas stated
after a goal they serve.

| Project | Motivated (chapters) | Best τ, within chapters | Best τ, whole document | Closest profile, whole document |
|---|---:|---|---|---|
| *PFR* | 2% | `top_down=0` (+0.55) | `top_down=0` (+0.92) | `top_down=0` |
| apap | 0% | `top_down=0` (+0.57) | `top_down=0` (+0.91) | `top_down=0` |
| flt3 | 1% | `top_down=0` (+0.42) | `top_down=0.2` (+0.78) | `top_down=0` |
| sphere_packing | 8% | `top_down=0`, definitions up front (+0.55) | `top_down=0` (+0.85) | `top_down=0` |
| brownian_motion | 9% | `top_down=0.2`, definitions up front, goals by key (+0.25) | `top_down=0` (+0.91) | `top_down=0` |
| abc_exceptions | 19% | `top_down=0.6`, definitions up front (+0.67) | `top_down=0.4` (+0.76) | `top_down=0.2`, chapter roadmap |
| testing_lower_bounds | 36% | `top_down=0`, definitions up front (+0.31) | `top_down=0.2` (+0.86) | `top_down=0` |
| sphere_eversion | 39% | `top_down=0.2`, definitions up front (+0.44) | `top_down=0.2` (+0.81) | `top_down=0.2` |
| *Carleson* | 67% | `top_down=0.6`, chapter roadmap (+0.20) | `top_down=0.2`, chapter roadmap (+0.86) | `top_down=0.2`, chapter roadmap |

- **Bottom-up is the norm.** By closest profile, five of the seven new projects
  fit `top_down = 0` on the whole document, like PFR. Carleson remains the most
  goal-first author, with sphere eversion, testing lower bounds and ABC in
  between (19–39% motivated). ABC is the only other project whose document
  fit includes a chapter roadmap.
- **Definitions up front is common.** It appears in the best within-chapter fit
  for five of the seven new projects. PFR alone favoured just-in-time
  definitions (Carleson has no definition nodes). So "definitions in the
  middle" was a PFR habit, not a general one.
- **Within-chapter order is still only partly explained.** Best τ within
  chapters ranges from 0.25 (Brownian motion) to 0.67 (ABC). Whole-document τ
  stays high (0.76–0.92), mostly because chapter order is fixed.

## Next

- **Outline the new projects** with `key_model_all.json`, and evaluate against
  their blueprints as [`outline.md`](outline.md) does for PFR and Carleson.
- **Use the best-known order as a reading aid:** show where it improves on the
  author's order, and which moves save the most working memory.
- **The three large projects** (PNT+, FLT, Equational Theories).
