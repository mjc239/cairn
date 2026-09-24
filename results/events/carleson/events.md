# Statement/proof events: Carleson

*fpvandoorn/carleson @ d966776f60fe (2026-09-23), chapters = \section*

Each blueprint node is a statement event and a proof event; a proof may use any result already *stated*, so stating a goal and proving it after its lemmas is not a forward reference. Edge kinds (statement vs proof use) come from Lean.

Whole blueprint: 453 backward edges, 37 deferred proofs, 33 genuine forward references.

**Motivated** = share of supporting results stated after the statement of a result that uses them (the reader has seen the goal a lemma serves). **Mean open** = the Phase 0 working-memory proxy on the event sequence (lower is better).

| Scope | motivated: human | random | top-down (deferred) | bottom-up | mean open: human | random (uniform median) | top-down (deferred) | bottom-up |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 60% | 59% | 100% | 0% | 12.7 | 94.3 | 30.6 | 22.0 |
| proof-of-metric-space-carleson-overview | 100% | 49% | 45% | 50% | 0.3 | 1.3 | 0.3 | 0.3 |
| proof-of-finitary-carleson | 73% | 67% | 75% | 20% | 4.8 | 9.1 | 5.5 | 4.4 |
| proof-of-discrete-carleson | 53% | 60% | 64% | 8% | 6.8 | 20.8 | 11.3 | 8.2 |
| proof-of-the-antichain-operator-proposit | 62% | 62% | 62% | 15% | 3.7 | 7.6 | 5.2 | 3.6 |
| proof-of-the-forest-operator-proposition | 64% | 61% | 70% | 10% | 7.3 | 21.8 | 11.9 | 7.6 |
| two-sided-metric-space-carleson | 44% | 57% | 100% | 0% | 4.8 | 11.0 | 8.4 | 4.1 |
| proof-of-the-classical-carleson-theorem | 73% | 78% | 100% | 23% | 10.5 | 17.3 | 11.5 | 10.3 |

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
| proof-of-metric-space-carleson-overview | human | +1.00 | 100% | 0.3 |
| | top-down, deferred proofs | -0.02 | 45% | 0.3 |
| | bottom-up, proofs immediately | -0.03 | 50% | 0.3 |
| | hybrid, goals = proofs using >= 1 results | +0.10 | 48% | 0.3 |
| | hybrid, goals = proofs using >= 2 results | +0.18 | 68% | 0.3 |
| | hybrid, goals = proofs using >= 3 results | +0.13 | 48% | 0.3 |
| | hybrid, goals = proofs using >= 4 results | +0.11 | 65% | 0.3 |
| | hybrid, goals = proofs using >= 6 results | +0.01 | 60% | 0.3 |
| proof-of-finitary-carleson | human | +1.00 | 73% | 4.8 |
| | top-down, deferred proofs | +0.15 | 75% | 5.5 |
| | bottom-up, proofs immediately | +0.15 | 20% | 4.4 |
| | hybrid, goals = proofs using >= 1 results | +0.23 | 79% | 5.1 |
| | hybrid, goals = proofs using >= 2 results | +0.17 | 69% | 5.2 |
| | hybrid, goals = proofs using >= 3 results | +0.15 | 64% | 5.3 |
| | hybrid, goals = proofs using >= 4 results | +0.19 | 68% | 4.9 |
| | hybrid, goals = proofs using >= 6 results | +0.27 | 20% | 4.6 |
| proof-of-discrete-carleson | human | +1.00 | 53% | 6.8 |
| | top-down, deferred proofs | +0.05 | 64% | 11.3 |
| | bottom-up, proofs immediately | +0.09 | 8% | 8.2 |
| | hybrid, goals = proofs using >= 1 results | +0.07 | 79% | 9.1 |
| | hybrid, goals = proofs using >= 2 results | +0.17 | 58% | 8.4 |
| | hybrid, goals = proofs using >= 3 results | +0.03 | 47% | 8.5 |
| | hybrid, goals = proofs using >= 4 results | +0.08 | 28% | 7.9 |
| | hybrid, goals = proofs using >= 6 results | +0.11 | 23% | 7.7 |
| proof-of-the-antichain-operator-proposit | human | +1.00 | 62% | 3.7 |
| | top-down, deferred proofs | +0.05 | 62% | 5.2 |
| | bottom-up, proofs immediately | -0.10 | 15% | 3.6 |
| | hybrid, goals = proofs using >= 1 results | +0.08 | 76% | 4.6 |
| | hybrid, goals = proofs using >= 2 results | +0.12 | 72% | 4.5 |
| | hybrid, goals = proofs using >= 3 results | +0.00 | 63% | 4.1 |
| | hybrid, goals = proofs using >= 4 results | +0.00 | 15% | 3.7 |
| | hybrid, goals = proofs using >= 6 results | -0.01 | 15% | 3.7 |
| proof-of-the-forest-operator-proposition | human | +1.00 | 64% | 7.3 |
| | top-down, deferred proofs | +0.25 | 70% | 11.9 |
| | bottom-up, proofs immediately | +0.31 | 10% | 7.6 |
| | hybrid, goals = proofs using >= 1 results | +0.35 | 83% | 9.2 |
| | hybrid, goals = proofs using >= 2 results | +0.38 | 71% | 8.9 |
| | hybrid, goals = proofs using >= 3 results | +0.33 | 68% | 9.1 |
| | hybrid, goals = proofs using >= 4 results | +0.39 | 47% | 8.2 |
| | hybrid, goals = proofs using >= 6 results | +0.38 | 10% | 7.7 |
| two-sided-metric-space-carleson | human | +1.00 | 44% | 4.8 |
| | top-down, deferred proofs | +0.25 | 100% | 8.4 |
| | bottom-up, proofs immediately | -0.03 | 0% | 4.1 |
| | hybrid, goals = proofs using >= 1 results | +0.25 | 100% | 8.3 |
| | hybrid, goals = proofs using >= 2 results | +0.14 | 80% | 7.1 |
| | hybrid, goals = proofs using >= 3 results | +0.13 | 44% | 5.6 |
| | hybrid, goals = proofs using >= 4 results | +0.15 | 39% | 5.4 |
| | hybrid, goals = proofs using >= 6 results | +0.08 | 0% | 4.8 |
| proof-of-the-classical-carleson-theorem | human | +1.00 | 73% | 10.5 |
| | top-down, deferred proofs | -0.05 | 100% | 11.5 |
| | bottom-up, proofs immediately | -0.08 | 23% | 10.3 |
| | hybrid, goals = proofs using >= 1 results | -0.06 | 100% | 11.7 |
| | hybrid, goals = proofs using >= 2 results | -0.11 | 93% | 11.5 |
| | hybrid, goals = proofs using >= 3 results | -0.02 | 89% | 11.4 |
| | hybrid, goals = proofs using >= 4 results | -0.17 | 77% | 11.1 |
| | hybrid, goals = proofs using >= 6 results | -0.09 | 65% | 10.6 |

## Detail

Mean open = the Phase 0 working-memory proxy on the event sequence; a deferred proof counts as open from its statement to its proof. τ = Kendall correlation with the human event order.

| Scope | events | deferred proofs | genuine fwd refs | human mean open | uniform median | uniform orders better | optimum | τ random | τ top-down (deferred) | τ bottom-up |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 340 | 37 | 33 | 12.7 | 94.3 | 0% | 42.3 | +0.05 | -0.11 | +0.01 |
| proof-of-metric-space-carleson-overview | 12 | 0 | 0 | 0.3 | 1.3 | 0% | 0.3 | +0.18 | -0.02 | -0.03 |
| proof-of-finitary-carleson | 31 | 2 | 0 | 4.8 | 9.1 | 0% | 3.9 | +0.14 | +0.15 | +0.15 |
| proof-of-discrete-carleson | 75 | 3 | 0 | 6.8 | 20.8 | 0% | 8.9 | +0.09 | +0.05 | +0.09 |
| proof-of-the-antichain-operator-proposit | 27 | 2 | 2 | 3.7 | 7.6 | 0% | 3.5 | +0.10 | +0.05 | -0.10 |
| proof-of-the-forest-operator-proposition | 79 | 12 | 5 | 7.3 | 21.8 | 0% | 9.5 | +0.08 | +0.25 | +0.31 |
| two-sided-metric-space-carleson | 38 | 3 | 0 | 4.8 | 11.0 | 0% | 4.9 | +0.14 | +0.25 | -0.03 |
| proof-of-the-classical-carleson-theorem | 59 | 6 | 21 | 10.5 | 17.3 | 0% | 7.9 | +0.20 | -0.05 | -0.08 |
