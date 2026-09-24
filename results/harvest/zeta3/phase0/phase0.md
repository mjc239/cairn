# Phase 0: zeta3

*ahhwuhu/zeta_3_irrational @ e8785315a01c (2026-03-20)*

30 nodes, 92 dependency edges. Null models per scope: 300 randomised-Kahn topological orders (biased towards opening many results early) and 200 approximately uniform ones (Karzanov–Khachiyan MCMC). All metrics: lower is better.

**Share of random orders better than the order** (0% = the order beats every random one; 50% = typical):

| Scope | n | forward edges | Human: mean open (Kahn null) | Human: mean open (uniform null) | Human: mean edge length (Kahn) | Mean open: human / optimised / uniform median | τ(human, optimised) | τ(human, random) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (whole blueprint) | 30 | 0% | 78% | 98% | 98% | 9.9 / 7.9 / 9.2 | +0.64 | +0.68 |
| front-matter | 30 | 0% | 78% | 98% | 98% | 9.9 / 7.9 / 9.2 | +0.64 | +0.68 |

## Whole blueprint: raw metrics

| Order | fwd refs | mean open | max open | mean cut | cutwidth | mean edge length | τ vs human | chapter runs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Human (as written) | 0 | 9.9 | 16 | 34.7 | 47 | 10.9 | +1.00 | 1 |
| Human, forward refs repaired | 0 | 9.9 | 16 | 34.7 | 47 | 10.9 | +1.00 | 1 |
| Just-in-time DFS (median run) | 0 | 8.3 | 13 | 32.7 | 48 | 10.3 | +0.63 | 1 |
| Greedy min-open (best run) | 0 | 8.1 | 13 | 32.4 | 45 | 10.2 | +0.66 | 1 |
| Greedy + local search (best run) | 0 | 7.9 | 13 | 27.3 | 44 | 8.6 | +0.64 | 1 |
| Random topological (median) | 0 | 9.7 | 15 | 32.6 | 47 | 10.3 | +0.68 | |
| Uniform topological (median) | 0 | 9.2 | 13 | 33.1 | 48 | 10.4 | | |

## Forward references in the human order (0)

None.

![mean open](phase0_mean_open.png)

![mean edge length](phase0_mean_edge_length.png)
