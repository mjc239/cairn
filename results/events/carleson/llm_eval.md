# Event-level LLM ordering: Carleson

The model orders statements (`S:x`) and proofs (`P:x`) separately and may defer proofs. Everything is scored on statement/proof events, averaged over chapters with at least 8 results. τ = Kendall correlation with the human event order; motivated = share of lemmas stated after a goal they serve; mean open = working-memory proxy (lower is better). Node-level LLM runs are recast with each proof straight after its statement. All orders are compared on each chapter's *core*: results whose statement and proof both sit in that chapter (proofs deferred to another section, and their statements, are left out, since node-level prompts never placed them).

Chapters compared: 7. Excluded (not answerable by every method, e.g. node-level prompts cannot place a proof whose statement is in another section): none.

| Order | runs | τ with human (mean ± sd over runs) | motivated | mean open | deferred proofs / chapter |
|---|---:|---:|---:|---:|---:|
| human | 1 | +1.00 ± 0.00 | 67% | 5.3 | 4.0 |
| bottom-up (m = ∞) | 5 | +0.12 ± 0.03 | 25% | 5.4 | 0.0 |
| hybrid m = 3 | 5 | +0.11 ± 0.09 | 65% | 6.3 | 4.1 |
| top-down (m = 1) | 5 | +0.12 ± 0.09 | 86% | 6.6 | 8.8 |
| node-level LLM, labelled | 2 | +0.39 ± 0.03 | 25% | 4.7 | 0.0 |
| node-level LLM, anonymised | 2 | +0.33 ± 0.01 | 25% | 4.7 | 0.0 |
| event-level LLM, labelled | 2 | +0.49 ± 0.01 | 56% | 5.7 | 2.9 |
| event-level LLM, anonymised | 2 | +0.46 ± 0.01 | 56% | 5.6 | 2.5 |

Per-chapter τ with the human order (mean over runs):

| Order | proof-of-metric-space-carleson-overview | proof-of-finitary-carleson | proof-of-discrete-carleson | proof-of-the-antichain-operator-proposit | proof-of-the-forest-operator-proposition | two-sided-metric-space-carleson | proof-of-the-classical-carleson-theorem |
|---|---:|---:|---:|---:|---:|---:|---:|
| bottom-up (m = ∞) | +0.04 | +0.24 | +0.21 | -0.18 | +0.32 | +0.08 | +0.13 |
| hybrid m = 3 | -0.07 | +0.31 | +0.11 | -0.04 | +0.43 | +0.12 | -0.06 |
| top-down (m = 1) | +0.15 | +0.21 | +0.02 | -0.03 | +0.23 | +0.33 | -0.06 |
| node-level LLM, labelled | -0.07 | +0.54 | +0.89 | +0.41 | +0.82 | -0.09 | +0.20 |
| node-level LLM, anonymised | -0.33 | +0.54 | +0.78 | +0.40 | +0.70 | -0.09 | +0.29 |
| event-level LLM, labelled | -0.07 | +0.71 | +0.96 | +0.66 | +0.56 | +0.28 | +0.33 |
| event-level LLM, anonymised | -0.60 | +0.99 | +0.91 | +0.69 | +0.49 | +0.28 | +0.46 |

Invalid responses or repaired constraint violations: none.
