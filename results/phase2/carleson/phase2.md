# Phase 2: Carleson

*fpvandoorn/carleson @ d966776f60fe (2026-09-23), chapters = \section*

## (c) Which Lean declarations become blueprint nodes?

236 of 3422 project declarations are named in the blueprint (base rate 7%). Precision@k uses k = 236; random P@k = 7%.

| Score | AUROC | P@k |
|---|---:|---:|
| proof size | 0.84 | 33% |
| pagerank, towards results | 0.84 | 37% |
| uses (in project) | 0.84 | 36% |
| betweenness | 0.80 | 30% |
| statement size | 0.80 | 21% |
| dominated declarations | 0.73 | 36% |
| proof / statement size | 0.68 | 13% |
| pagerank, towards utilities | 0.35 | 0% |
| name length | 0.60 | 3% |
| used by exactly one declaration | 0.60 | 3% |
| is definition | 0.43 | 0% |
| has variants | 0.55 | 16% |
| is private | 0.46 | 0% |
| users (in project) | 0.46 | 1% |
| aux-style name | 0.47 | 3% |
| variant of another declaration | 0.47 | 1% |
| primed name | 0.47 | 2% |
| is instance | 0.49 | 3% |
| used only by its own variants | 0.51 | 6% |
| in ForMathlib/Mathlib module | 0.50 | 3% |
| **Logistic regression, structural features** (5-fold, Lean modules held out) | **0.89** | **44%** |
| **Logistic regression, + variant-of features** (5-fold, Lean modules held out) | **0.90** | **46%** |

Average precision of the full combined score: 0.44. AUROC below 0.5 means the score points the other way (e.g. heavily used declarations are *less* likely to be named).

Coefficients (standardised log features): is private -1.70, proof / statement size +1.05, uses (in project) +0.94, pagerank, towards utilities -0.89, statement size +0.83, is definition -0.67, variant of another declaration -0.61, pagerank, towards results +0.50, users (in project) +0.50, name length +0.37, has variants +0.34, proof size -0.28, betweenness -0.22, primed name +0.21, used by exactly one declaration -0.18, used only by its own variants -0.17, dominated declarations +0.07, is instance +0.05, aux-style name +0.04, in ForMathlib/Mathlib module +0.00

Highest-scoring declarations the blueprint does **not** name: `MeasureTheory.eLorentzNorm'_eq`, `lintegral_carlesonSum_forest`, `Construction.Ω_disjoint`, `TileStructure.Forest.global_tree_control1_edist_part2`, `two_sided_metric_carleson_hasStrongType`, `MeasureTheory.HasRestrictedWeakType.hasRestrictedWeakType'_nnreal`, `MeasureTheory.combine_estimates₀`, `Tile.boundedCompactSupport_aux_6_2_26`, `MeasureTheory.lintegral_rearrangement_eq`, `TileStructure.Forest.edist_holderFunction_le`.

Lowest-scoring declarations it **does** name: `instFunctionDistancesReal`, `Tile.correlation`, `lower_secant_bound'`, `integral_czRemainder'`, `measurable_maximalFunction`, `MeasureTheory.InnerProductSpace.IsDoubling`, `czApproximation_add_czRemainder`, `laverage_le_globalMaximalFunction`, `dist_mem_Icc_of_Ks_ne_zero`, `MeasureTheory.eLpNorm_pow_eq_distribution`.

## (a) Recovering chapters from the Lean graph

| Method | clusters | ARI | NMI |
|---|---:|---:|---:|
| Lean module of the node's declaration | 47 | 0.34 | 0.72 |
| Louvain communities (Lean graph) | 12 | 0.62 | 0.78 |
| Greedy modularity (Lean graph) | 12 | 0.79 | 0.82 |
| Random (chapter sizes kept) | 11 | -0.00 | 0.12 |

## (b) Ordering

τ = Kendall rank correlation with the human blueprint order (1 = identical). *Within chapters* averages τ over chapters with at least 8 nodes. Mean open is the working-memory proxy from Phase 0 (lower is better), on Lean-derived edges.

| Order | τ whole | τ within chapters | mean open | forward refs | chapter runs |
|---|---:|---:|---:|---:|---:|
| Human (blueprint) | +1.00 | +1.00 | 21.6 | 126 | 11 |
| Lean source order | +0.34 | +0.18 | 19.7 | 0 | 30 |
| Just-in-time DFS | +0.05 | -0.10 | 20.2 | 0 | 26 |
| Goal-first DFS | -0.03 | +0.15 | 31.3 | 188 | 31 |
| Global optimum (greedy + local search) | +0.04 | +0.01 | 17.4 | 0 | 58 |
| Cluster-then-order, true chapters | +0.89 | +0.09 | 18.6 | 23 | 11 |
| Cluster-then-order, Lean modules | +0.33 | +0.04 | 19.6 | 0 | 30 |
| LLM within true chapters | +0.92 | +0.19 | 19.4 | 26 | 11 |
| Random topological (mean of 200) | -0.08 | -0.10 | 44.9 | 0 | 132 |

Per-chapter τ with the human order:

| Chapter | Lean source order | Just-in-time DFS | Goal-first DFS | Global optimum (greedy + local search) | Cluster-then-order, true chapters | Cluster-then-order, Lean modules | LLM within true chapters |
|---|---:|---:|---:|---:|---:|---:|---:|
| proof-of-metric-space-carleson-overview | -0.67 | -0.44 | +0.28 | -0.61 | -0.17 | -0.67 | -0.89 |
| proof-of-finitary-carleson | +0.37 | +0.14 | +0.22 | -0.22 | +0.39 | -0.24 | +0.33 |
| proof-of-discrete-carleson | +0.42 | -0.25 | -0.17 | +0.45 | +0.39 | +0.34 | +0.77 |
| proof-of-the-antichain-operator-proposit | +0.21 | -0.08 | -0.28 | +0.10 | -0.23 | +0.13 | +0.46 |
| proof-of-the-forest-operator-proposition | +0.82 | +0.43 | +0.35 | +0.34 | +0.42 | +0.74 | +0.75 |
| two-sided-metric-space-carleson | -0.17 | -0.16 | +0.58 | -0.03 | -0.26 | -0.24 | -0.17 |
| proof-of-the-classical-carleson-theorem | +0.28 | -0.36 | +0.10 | +0.04 | +0.10 | +0.24 | +0.08 |

LLM responses for 7 chapters; constraint violations repaired: {'proof-of-metric-space-carleson-overview': 0, 'proof-of-finitary-carleson': 0, 'proof-of-discrete-carleson': 0, 'proof-of-the-antichain-operator-proposit': 0, 'proof-of-the-forest-operator-proposition': 0, 'two-sided-metric-space-carleson': 0, 'proof-of-the-classical-carleson-theorem': 0}; invalid: none.
