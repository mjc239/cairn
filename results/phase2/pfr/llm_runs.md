# LLM ordering runs: PFR

τ = Kendall correlation with the human order, averaged over the answered chapters.

| Variant | runs | τ within chapters (mean ± sd) | individual runs | mean open | repaired violations |
|---|---:|---:|---|---:|---:|
| named | 3 | +0.85 ± 0.00 | +0.85, +0.85, +0.86 | 45.4 | 0 |
| blind | 3 | +0.83 ± 0.01 | +0.83, +0.84, +0.83 | 45.4 | 0 |

Per-chapter τ (mean over runs):

| Variant | entropy | distance | entropy_pfr | improved_exponent | approx_hom_pfr | weak_pfr | torsion | further_improvement |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| named | +0.93 | +0.75 | +0.97 | +0.78 | +0.93 | +0.73 | +0.86 | +0.87 |
| blind | +0.90 | +0.68 | +0.97 | +0.73 | +1.00 | +0.64 | +0.82 | +0.90 |
