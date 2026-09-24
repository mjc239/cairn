# Event-level LLM ordering: PFR

The model orders statements (`S:x`) and proofs (`P:x`) separately and may defer proofs. Everything is scored on statement/proof events, averaged over chapters with at least 8 results. τ = Kendall correlation with the human event order; motivated = share of lemmas stated after a goal they serve; mean open = working-memory proxy (lower is better). Node-level LLM runs are recast with each proof straight after its statement. All orders are compared on each chapter's *core*: results whose statement and proof both sit in that chapter (proofs deferred to another section, and their statements, are left out, since node-level prompts never placed them).

Chapters compared: 8. Excluded (not answerable by every method, e.g. node-level prompts cannot place a proof whose statement is in another section): none.

| Order | runs | τ with human (mean ± sd over runs) | motivated | mean open | deferred proofs / chapter |
|---|---:|---:|---:|---:|---:|
| human | 1 | +1.00 ± 0.00 | 2% | 6.3 | 0.0 |
| bottom-up (m = ∞) | 5 | +0.53 ± 0.03 | 1% | 6.5 | 0.0 |
| hybrid m = 3 | 5 | +0.47 ± 0.05 | 50% | 7.5 | 4.5 |
| top-down (m = 1) | 5 | +0.17 ± 0.07 | 93% | 9.0 | 10.8 |
| node-level LLM, labelled | 3 | +0.86 ± 0.01 | 1% | 6.3 | 0.0 |
| node-level LLM, anonymised | 3 | +0.85 ± 0.01 | 1% | 6.5 | 0.0 |
| event-level LLM, labelled | 2 | +0.58 ± 0.15 | 29% | 6.9 | 1.9 |
| event-level LLM, anonymised | 2 | +0.52 ± 0.04 | 29% | 6.8 | 2.0 |

Per-chapter τ with the human order (mean over runs):

| Order | entropy | distance | entropy_pfr | improved_exponent | approx_hom_pfr | weak_pfr | torsion | further_improvement |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| bottom-up (m = ∞) | +0.24 | +0.41 | +0.48 | +1.00 | +0.92 | +0.49 | +0.32 | +0.38 |
| hybrid m = 3 | +0.10 | +0.27 | +0.42 | +1.00 | +0.90 | +0.44 | +0.18 | +0.44 |
| top-down (m = 1) | +0.28 | +0.23 | +0.49 | +0.03 | +0.06 | -0.03 | +0.05 | +0.28 |
| node-level LLM, labelled | +0.92 | +0.74 | +0.97 | +0.79 | +0.92 | +0.81 | +0.87 | +0.86 |
| node-level LLM, anonymised | +0.89 | +0.68 | +0.96 | +0.75 | +1.00 | +0.77 | +0.84 | +0.89 |
| event-level LLM, labelled | +0.91 | +0.70 | +0.74 | -0.11 | +0.79 | +0.22 | +0.64 | +0.78 |
| event-level LLM, anonymised | +0.90 | +0.65 | +0.74 | -0.55 | +0.90 | +0.12 | +0.64 | +0.76 |

Invalid responses or repaired constraint violations: none.
