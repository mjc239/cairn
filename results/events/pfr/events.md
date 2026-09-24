# Statement/proof events: PFR

*teorth/pfr @ ddd44f6ce82e*

Each blueprint node is a statement event and a proof event; a proof may use any result already *stated*, so stating a goal and proving it after its lemmas is not a forward reference. Edge kinds (statement vs proof use) come from Lean.

Whole blueprint: 1348 backward edges, 0 deferred proofs, 8 genuine forward references.

**Motivated** = share of supporting results stated after the statement of a result that uses them (the reader has seen the goal a lemma serves). **Mean open** = the Phase 0 working-memory proxy on the event sequence (lower is better).

| Scope | motivated: human | random | top-down (deferred) | bottom-up | mean open: human | random (uniform median) | top-down (deferred) | bottom-up |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 2% | 60% | 97% | 1% | 46.2 | 118.9 | 52.5 | 47.9 |
| entropy | 6% | 52% | 71% | 0% | 6.2 | 13.7 | 7.6 | 7.3 |
| distance | 0% | 67% | 100% | 0% | 6.0 | 14.0 | 6.5 | 6.4 |
| entropy_pfr | 0% | 53% | 100% | 0% | 7.7 | 13.4 | 10.6 | 8.2 |
| improved_exponent | 0% | 50% | 100% | 0% | 1.7 | 5.6 | 5.4 | 1.7 |
| approx_hom_pfr | 0% | 59% | 100% | 0% | 2.5 | 4.7 | 3.6 | 2.5 |
| weak_pfr | 0% | 47% | 89% | 0% | 2.4 | 5.6 | 5.2 | 2.9 |
| torsion | 0% | 48% | 98% | 0% | 12.9 | 27.0 | 17.4 | 12.9 |
| further_improvement | 3% | 55% | 88% | 0% | 10.6 | 21.3 | 13.7 | 10.4 |

## Hybrid styles: state a goal first (deferring its proof) iff its proof uses at least m results

| Scope | style | τ with human | motivated | mean open |
|---|---|---:|---:|---:|
| (whole blueprint) | human | +1.00 | 2% | 46.2 |
| | top-down, deferred proofs | +0.29 | 97% | 52.5 |
| | bottom-up, proofs immediately | +0.38 | 1% | 47.9 |
| | hybrid, goals = proofs using >= 1 results | +0.28 | 97% | 53.1 |
| | hybrid, goals = proofs using >= 2 results | +0.28 | 89% | 51.4 |
| | hybrid, goals = proofs using >= 3 results | +0.36 | 81% | 51.3 |
| | hybrid, goals = proofs using >= 4 results | +0.30 | 74% | 51.4 |
| | hybrid, goals = proofs using >= 6 results | +0.28 | 63% | 50.8 |
| entropy | human | +1.00 | 6% | 6.2 |
| | top-down, deferred proofs | +0.22 | 71% | 7.6 |
| | bottom-up, proofs immediately | +0.24 | 0% | 7.3 |
| | hybrid, goals = proofs using >= 1 results | +0.16 | 73% | 7.8 |
| | hybrid, goals = proofs using >= 2 results | +0.15 | 62% | 7.7 |
| | hybrid, goals = proofs using >= 3 results | +0.26 | 41% | 7.7 |
| | hybrid, goals = proofs using >= 4 results | +0.19 | 23% | 7.4 |
| | hybrid, goals = proofs using >= 6 results | +0.25 | 19% | 7.4 |
| distance | human | +1.00 | 0% | 6.0 |
| | top-down, deferred proofs | +0.28 | 100% | 6.5 |
| | bottom-up, proofs immediately | +0.43 | 0% | 6.4 |
| | hybrid, goals = proofs using >= 1 results | +0.30 | 100% | 6.9 |
| | hybrid, goals = proofs using >= 2 results | +0.28 | 81% | 7.0 |
| | hybrid, goals = proofs using >= 3 results | +0.34 | 62% | 6.7 |
| | hybrid, goals = proofs using >= 4 results | +0.27 | 56% | 6.6 |
| | hybrid, goals = proofs using >= 6 results | +0.32 | 33% | 6.6 |
| entropy_pfr | human | +1.00 | 0% | 7.7 |
| | top-down, deferred proofs | +0.39 | 100% | 10.6 |
| | bottom-up, proofs immediately | +0.68 | 0% | 8.2 |
| | hybrid, goals = proofs using >= 1 results | +0.40 | 100% | 10.3 |
| | hybrid, goals = proofs using >= 2 results | +0.37 | 86% | 10.7 |
| | hybrid, goals = proofs using >= 3 results | +0.43 | 74% | 9.8 |
| | hybrid, goals = proofs using >= 4 results | +0.49 | 55% | 9.8 |
| | hybrid, goals = proofs using >= 6 results | +0.45 | 27% | 8.6 |
| improved_exponent | human | +1.00 | 0% | 1.7 |
| | top-down, deferred proofs | +0.08 | 100% | 5.4 |
| | bottom-up, proofs immediately | +0.89 | 0% | 1.7 |
| | hybrid, goals = proofs using >= 1 results | +0.03 | 100% | 5.4 |
| | hybrid, goals = proofs using >= 2 results | +0.77 | 22% | 2.2 |
| | hybrid, goals = proofs using >= 3 results | +1.00 | 0% | 1.7 |
| | hybrid, goals = proofs using >= 4 results | +1.00 | 0% | 1.7 |
| | hybrid, goals = proofs using >= 6 results | +1.00 | 0% | 1.7 |
| approx_hom_pfr | human | +1.00 | 0% | 2.5 |
| | top-down, deferred proofs | +0.16 | 100% | 3.6 |
| | bottom-up, proofs immediately | +0.57 | 0% | 2.5 |
| | hybrid, goals = proofs using >= 1 results | +0.09 | 100% | 3.6 |
| | hybrid, goals = proofs using >= 2 results | +0.09 | 100% | 3.6 |
| | hybrid, goals = proofs using >= 3 results | +0.88 | 43% | 2.6 |
| | hybrid, goals = proofs using >= 4 results | +0.92 | 0% | 2.5 |
| | hybrid, goals = proofs using >= 6 results | +0.92 | 0% | 2.5 |
| weak_pfr | human | +1.00 | 0% | 2.4 |
| | top-down, deferred proofs | +0.01 | 89% | 5.2 |
| | bottom-up, proofs immediately | +0.65 | 0% | 2.9 |
| | hybrid, goals = proofs using >= 1 results | -0.04 | 89% | 5.3 |
| | hybrid, goals = proofs using >= 2 results | +0.42 | 33% | 3.5 |
| | hybrid, goals = proofs using >= 3 results | +0.49 | 33% | 3.5 |
| | hybrid, goals = proofs using >= 4 results | +0.45 | 33% | 3.5 |
| | hybrid, goals = proofs using >= 6 results | +0.49 | 0% | 2.9 |
| torsion | human | +1.00 | 0% | 12.9 |
| | top-down, deferred proofs | +0.08 | 98% | 17.4 |
| | bottom-up, proofs immediately | +0.35 | 0% | 12.9 |
| | hybrid, goals = proofs using >= 1 results | +0.11 | 98% | 17.4 |
| | hybrid, goals = proofs using >= 2 results | +0.23 | 82% | 15.3 |
| | hybrid, goals = proofs using >= 3 results | +0.23 | 70% | 15.4 |
| | hybrid, goals = proofs using >= 4 results | +0.24 | 59% | 15.2 |
| | hybrid, goals = proofs using >= 6 results | +0.32 | 41% | 14.4 |
| further_improvement | human | +1.00 | 3% | 10.6 |
| | top-down, deferred proofs | +0.33 | 88% | 13.7 |
| | bottom-up, proofs immediately | +0.50 | 0% | 10.4 |
| | hybrid, goals = proofs using >= 1 results | +0.30 | 89% | 13.8 |
| | hybrid, goals = proofs using >= 2 results | +0.40 | 72% | 12.2 |
| | hybrid, goals = proofs using >= 3 results | +0.36 | 64% | 12.2 |
| | hybrid, goals = proofs using >= 4 results | +0.38 | 62% | 12.0 |
| | hybrid, goals = proofs using >= 6 results | +0.40 | 50% | 12.0 |

## Detail

Mean open = the Phase 0 working-memory proxy on the event sequence; a deferred proof counts as open from its statement to its proof. τ = Kendall correlation with the human event order.

| Scope | events | deferred proofs | genuine fwd refs | human mean open | uniform median | uniform orders better | optimum | τ random | τ top-down (deferred) | τ bottom-up |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 392 | 0 | 8 | 46.2 | 118.9 | 0% | 50.3 | +0.18 | +0.29 | +0.38 |
| entropy | 50 | 0 | 1 | 6.2 | 13.7 | 0% | 5.3 | +0.21 | +0.22 | +0.24 |
| distance | 50 | 0 | 0 | 6.0 | 14.0 | 0% | 6.0 | +0.12 | +0.28 | +0.43 |
| entropy_pfr | 44 | 0 | 0 | 7.7 | 13.4 | 0% | 7.3 | +0.13 | +0.39 | +0.68 |
| improved_exponent | 20 | 0 | 0 | 1.7 | 5.6 | 0% | 1.9 | +0.10 | +0.08 | +0.89 |
| approx_hom_pfr | 15 | 0 | 0 | 2.5 | 4.7 | 0% | 2.0 | +0.06 | +0.16 | +0.57 |
| weak_pfr | 19 | 0 | 0 | 2.4 | 5.6 | 0% | 2.4 | +0.21 | +0.01 | +0.65 |
| torsion | 91 | 0 | 0 | 12.9 | 27.0 | 0% | 11.6 | +0.25 | +0.08 | +0.35 |
| further_improvement | 70 | 0 | 1 | 10.6 | 21.3 | 0% | 9.1 | +0.33 | +0.33 | +0.50 |
