# Statement/proof events: Carleson

*fpvandoorn/carleson @ d966776f60fe (2026-09-23), chapters = \section*

Each blueprint node is a statement event and a proof event; a proof may use any result already *stated*, so stating a goal and proving it after its lemmas is not a forward reference. Edge kinds (statement vs proof use) come from Lean.

Whole blueprint: 453 backward edges, 37 deferred proofs, 33 genuine forward references.

**Motivated** = share of supporting results stated after the statement of a result that uses them (the reader has seen the goal a lemma serves). **Mean open** = the Phase 0 working-memory proxy on the event sequence (lower is better).

| Scope | motivated: human | random | top-down (deferred) | bottom-up | mean open: human | random (uniform median) | top-down (deferred) | bottom-up |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 60% | 59% | 100% | 0% | 12.7 | 94.3 | 30.6 | 22.0 |
| proof-of-metric-space-carleson-overview | 100% | 52% | 100% | 0% | 4.6 | 3.8 | 0.9 | 0.8 |
| proof-of-finitary-carleson | 67% | 57% | 100% | 0% | 4.8 | 8.6 | 4.4 | 3.4 |
| proof-of-discrete-carleson | 48% | 55% | 100% | 0% | 6.8 | 20.2 | 7.5 | 5.8 |
| proof-of-the-antichain-operator-proposit | 55% | 54% | 100% | 0% | 3.4 | 7.4 | 4.4 | 3.1 |
| proof-of-the-forest-operator-proposition | 58% | 56% | 99% | 0% | 7.3 | 21.5 | 9.6 | 6.7 |
| two-sided-metric-space-carleson | 44% | 57% | 100% | 0% | 4.8 | 11.0 | 8.4 | 4.1 |
| proof-of-the-classical-carleson-theorem | 64% | 68% | 100% | 0% | 9.6 | 16.8 | 10.9 | 10.0 |

## Hybrid styles: state a goal first (deferring its proof) iff its proof uses at least m results

| Scope | style | τ with human | motivated | mean open |
|---|---|---:|---:|---:|
| (whole blueprint) | human | +1.00 | 60% | 12.7 |
| | top-down, deferred proofs | -0.11 | 100% | 30.6 |
| | bottom-up, proofs immediately | +0.01 | 0% | 22.0 |
| | hybrid, goals = proofs using >= 1 results | +0.03 | 100% | 30.6 |
| | hybrid, goals = proofs using >= 2 results | +0.02 | 92% | 30.4 |
| | hybrid, goals = proofs using >= 3 results | +0.12 | 78% | 27.5 |
| | hybrid, goals = proofs using >= 4 results | +0.28 | 60% | 24.3 |
| | hybrid, goals = proofs using >= 6 results | +0.15 | 28% | 21.9 |
| proof-of-metric-space-carleson-overview | human | +1.00 | 100% | 4.6 |
| | top-down, deferred proofs | +0.08 | 100% | 0.9 |
| | bottom-up, proofs immediately | +0.05 | 0% | 0.8 |
| | hybrid, goals = proofs using >= 1 results | +0.10 | 100% | 0.9 |
| | hybrid, goals = proofs using >= 2 results | +0.05 | 0% | 0.8 |
| | hybrid, goals = proofs using >= 3 results | +0.04 | 0% | 0.8 |
| | hybrid, goals = proofs using >= 4 results | +0.02 | 0% | 0.8 |
| | hybrid, goals = proofs using >= 6 results | +0.03 | 0% | 0.8 |
| proof-of-finitary-carleson | human | +1.00 | 67% | 4.8 |
| | top-down, deferred proofs | +0.32 | 100% | 4.4 |
| | bottom-up, proofs immediately | +0.27 | 0% | 3.4 |
| | hybrid, goals = proofs using >= 1 results | +0.36 | 100% | 4.4 |
| | hybrid, goals = proofs using >= 2 results | +0.31 | 92% | 4.3 |
| | hybrid, goals = proofs using >= 3 results | +0.39 | 92% | 4.3 |
| | hybrid, goals = proofs using >= 4 results | +0.28 | 92% | 4.2 |
| | hybrid, goals = proofs using >= 6 results | +0.27 | 0% | 3.2 |
| proof-of-discrete-carleson | human | +1.00 | 48% | 6.8 |
| | top-down, deferred proofs | +0.17 | 100% | 7.5 |
| | bottom-up, proofs immediately | +0.18 | 0% | 5.8 |
| | hybrid, goals = proofs using >= 1 results | +0.20 | 100% | 7.3 |
| | hybrid, goals = proofs using >= 2 results | +0.11 | 83% | 6.9 |
| | hybrid, goals = proofs using >= 3 results | +0.27 | 67% | 6.8 |
| | hybrid, goals = proofs using >= 4 results | +0.09 | 40% | 6.0 |
| | hybrid, goals = proofs using >= 6 results | +0.20 | 29% | 6.3 |
| proof-of-the-antichain-operator-proposit | human | +1.00 | 55% | 3.4 |
| | top-down, deferred proofs | +0.37 | 100% | 4.4 |
| | bottom-up, proofs immediately | +0.18 | 0% | 3.1 |
| | hybrid, goals = proofs using >= 1 results | +0.39 | 100% | 4.4 |
| | hybrid, goals = proofs using >= 2 results | +0.20 | 88% | 4.2 |
| | hybrid, goals = proofs using >= 3 results | +0.26 | 76% | 4.0 |
| | hybrid, goals = proofs using >= 4 results | -0.00 | 0% | 3.0 |
| | hybrid, goals = proofs using >= 6 results | -0.00 | 0% | 3.0 |
| proof-of-the-forest-operator-proposition | human | +1.00 | 58% | 7.3 |
| | top-down, deferred proofs | +0.36 | 99% | 9.6 |
| | bottom-up, proofs immediately | +0.26 | 0% | 6.7 |
| | hybrid, goals = proofs using >= 1 results | +0.44 | 99% | 9.7 |
| | hybrid, goals = proofs using >= 2 results | +0.37 | 91% | 9.2 |
| | hybrid, goals = proofs using >= 3 results | +0.40 | 80% | 9.1 |
| | hybrid, goals = proofs using >= 4 results | +0.67 | 47% | 7.8 |
| | hybrid, goals = proofs using >= 6 results | +0.63 | 0% | 7.1 |
| two-sided-metric-space-carleson | human | +1.00 | 44% | 4.8 |
| | top-down, deferred proofs | +0.25 | 100% | 8.4 |
| | bottom-up, proofs immediately | -0.03 | 0% | 4.1 |
| | hybrid, goals = proofs using >= 1 results | +0.25 | 100% | 8.3 |
| | hybrid, goals = proofs using >= 2 results | +0.14 | 80% | 7.1 |
| | hybrid, goals = proofs using >= 3 results | +0.13 | 44% | 5.6 |
| | hybrid, goals = proofs using >= 4 results | +0.15 | 39% | 5.4 |
| | hybrid, goals = proofs using >= 6 results | +0.08 | 0% | 4.8 |
| proof-of-the-classical-carleson-theorem | human | +1.00 | 64% | 9.6 |
| | top-down, deferred proofs | -0.08 | 100% | 10.9 |
| | bottom-up, proofs immediately | -0.10 | 0% | 10.0 |
| | hybrid, goals = proofs using >= 1 results | -0.07 | 100% | 11.0 |
| | hybrid, goals = proofs using >= 2 results | -0.08 | 93% | 11.1 |
| | hybrid, goals = proofs using >= 3 results | -0.07 | 88% | 10.8 |
| | hybrid, goals = proofs using >= 4 results | -0.10 | 68% | 10.5 |
| | hybrid, goals = proofs using >= 6 results | -0.10 | 56% | 9.8 |

## Detail

Mean open = the Phase 0 working-memory proxy on the event sequence; a deferred proof counts as open from its statement to its proof. τ = Kendall correlation with the human event order.

| Scope | events | deferred proofs | genuine fwd refs | human mean open | uniform median | uniform orders better | optimum | τ random | τ top-down (deferred) | τ bottom-up |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 340 | 37 | 33 | 12.7 | 94.3 | 0% | 42.3 | +0.05 | -0.11 | +0.01 |
| proof-of-metric-space-carleson-overview | 18 | 6 | 0 | 4.6 | 3.8 | 88% | 0.8 | +0.29 | +0.08 | +0.05 |
| proof-of-finitary-carleson | 30 | 2 | 0 | 4.8 | 8.6 | 0% | 3.4 | +0.17 | +0.32 | +0.27 |
| proof-of-discrete-carleson | 74 | 3 | 0 | 6.8 | 20.2 | 0% | 8.1 | +0.10 | +0.17 | +0.18 |
| proof-of-the-antichain-operator-proposit | 26 | 2 | 2 | 3.4 | 7.4 | 0% | 3.0 | +0.11 | +0.37 | +0.18 |
| proof-of-the-forest-operator-proposition | 78 | 12 | 5 | 7.3 | 21.5 | 0% | 10.2 | +0.08 | +0.36 | +0.26 |
| two-sided-metric-space-carleson | 38 | 3 | 0 | 4.8 | 11.0 | 0% | 4.9 | +0.14 | +0.25 | -0.03 |
| proof-of-the-classical-carleson-theorem | 58 | 6 | 18 | 9.6 | 16.8 | 0% | 7.9 | +0.24 | -0.08 | -0.10 |
