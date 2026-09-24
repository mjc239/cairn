# Phase 2: PFR

*teorth/pfr @ ddd44f6ce82e, Lean v4.35.0-rc2*

## (c) Which Lean declarations become blueprint nodes?

248 of 1395 project declarations are named in the blueprint (base rate 18%). Precision@k uses k = 248; random P@k = 18%.

| Score | AUROC | P@k |
|---|---:|---:|
| betweenness | 0.79 | 53% |
| uses (in project) | 0.79 | 49% |
| pagerank, towards results | 0.77 | 52% |
| proof size | 0.76 | 46% |
| statement size | 0.74 | 44% |
| proof / statement size | 0.70 | 36% |
| in ForMathlib/Mathlib module | 0.37 | 4% |
| dominated declarations | 0.62 | 33% |
| users (in project) | 0.60 | 24% |
| has variants | 0.54 | 20% |
| is private | 0.47 | 5% |
| used only by its own variants | 0.52 | 12% |
| pagerank, towards utilities | 0.52 | 17% |
| used by exactly one declaration | 0.52 | 8% |
| aux-style name | 0.52 | 18% |
| name length | 0.52 | 12% |
| is instance | 0.49 | 5% |
| is definition | 0.49 | 10% |
| variant of another declaration | 0.51 | 14% |
| primed name | 0.50 | 13% |
| **Logistic regression, structural features** (5-fold, Lean modules held out) | **0.87** | **61%** |
| **Logistic regression, + variant-of features** (5-fold, Lean modules held out) | **0.86** | **60%** |

Average precision of the full combined score: 0.61. AUROC below 0.5 means the score points the other way (e.g. heavily used declarations are *less* likely to be named).

Coefficients (standardised log features): is private -1.21, statement size +0.83, users (in project) +0.71, pagerank, towards results +0.57, uses (in project) +0.57, proof size +0.50, is definition +0.43, is instance -0.42, in ForMathlib/Mathlib module -0.40, primed name +0.35, betweenness +0.34, aux-style name -0.32, variant of another declaration -0.32, dominated declarations -0.26, used by exactly one declaration -0.15, name length +0.09, proof / statement size -0.08, used only by its own variants -0.05, has variants +0.04, pagerank, towards utilities -0.00

Highest-scoring declarations the blueprint does **not** name: `averaged_final`, `ProbabilityTheory.Kernel.chain_rule`, `ProbabilityTheory.Kernel.entropy_compProd`, `app_ent_PFR'`, `tau_strictly_decreases_aux'`, `dist_le_of_sum_zero_cond`, `dist_of_min_eq_zero'`, `gen_ineq_aux2`, `ProbabilityTheory.Kernel.entropy_snd_sub_mutualInfo_le_entropy_map_of_injective`, `new_gen_ineq`.

Lowest-scoring declarations it **does** name: `ProbabilityTheory.entropy_le_log_card`, `ProbabilityTheory.entropy_le_log_card_of_mem`, `ProbabilityTheory.IsUniform.entropy_eq`, `Real.sum_mul_log_div_eq_iff`, `Finset.addEnergy'`, `ProbabilityTheory.condEntropy_add_right`, `ProbabilityTheory.mutualInfo_def`, `ProbabilityTheory.condEntropy_comp_of_injective`, `diff_ent_le_rdist'`, `diff_ent_le_rdist''`.

## (a) Recovering chapters from the Lean graph

| Method | clusters | ARI | NMI |
|---|---:|---:|---:|
| Lean module of the node's declaration | 28 | 0.60 | 0.83 |
| Louvain communities (Lean graph) | 8 | 0.48 | 0.58 |
| Greedy modularity (Lean graph) | 8 | 0.35 | 0.56 |
| Random (chapter sizes kept) | 13 | -0.00 | 0.14 |

## (b) Ordering

τ = Kendall rank correlation with the human blueprint order (1 = identical). *Within chapters* averages τ over chapters with at least 8 nodes. Mean open is the working-memory proxy from Phase 0 (lower is better), on Lean-derived edges.

| Order | τ whole | τ within chapters | mean open | forward refs | chapter runs |
|---|---:|---:|---:|---:|---:|
| Human (blueprint) | +1.00 | +1.00 | 45.5 | 8 | 13 |
| Lean source order | +0.58 | +0.87 | 56.3 | 2 | 25 |
| Just-in-time DFS | +0.23 | +0.47 | 49.0 | 1 | 77 |
| Global optimum (greedy + local search) | +0.11 | +0.54 | 44.4 | 1 | 106 |
| Cluster-then-order, true chapters | +0.95 | +0.73 | 44.3 | 6 | 13 |
| Cluster-then-order, Lean modules | +0.56 | +0.73 | 56.0 | 1 | 25 |
| LLM within true chapters | +0.98 | +0.85 | 45.4 | 6 | 13 |
| Random topological (mean of 200) | +0.25 | +0.54 | 63.8 | 0 | 163 |

Per-chapter τ with the human order:

| Chapter | Lean source order | Just-in-time DFS | Global optimum (greedy + local search) | Cluster-then-order, true chapters | Cluster-then-order, Lean modules | LLM within true chapters |
|---|---:|---:|---:|---:|---:|---:|
| entropy | +0.67 | +0.50 | +0.11 | +0.63 | +0.34 | +0.92 |
| distance | +0.78 | +0.40 | +0.31 | +0.17 | +0.64 | +0.75 |
| entropy_pfr | +1.00 | +0.57 | +0.38 | +0.80 | +0.91 | +0.97 |
| improved_exponent | +0.87 | +0.73 | +0.73 | +1.00 | +1.00 | +0.87 |
| approx_hom_pfr | +1.00 | +0.07 | +0.79 | +1.00 | +0.79 | +0.79 |
| weak_pfr | +0.73 | +0.64 | +0.78 | +0.73 | +0.47 | +0.73 |
| torsion | +0.91 | +0.30 | +0.36 | +0.65 | +0.83 | +0.90 |
| further_improvement | +0.99 | +0.57 | +0.84 | +0.84 | +0.85 | +0.87 |

LLM responses for 8 chapters; constraint violations repaired: {'entropy': 0, 'distance': 0, 'entropy_pfr': 0, 'improved_exponent': 0, 'approx_hom_pfr': 0, 'weak_pfr': 0, 'torsion': 0, 'further_improvement': 0}; invalid: none.
