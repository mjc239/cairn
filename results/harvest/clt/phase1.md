# Phase 1: clt

*RemyDegenne/CLT @ 760df08d054d (2026-05-06), Lean leanprover/lean4:v4.29.0-rc3*

## Formal graph

- Project declarations (after folding compiler auxiliaries): 26 (def: 4, theorem: 22); 94 dependency edges, including 32 blueprint-named declarations outside the project (e.g. upstreamed to Mathlib).
- Blueprint `\lean{}` names resolved to project declarations: 40 (89%); 40 of 50 blueprint nodes have at least one.
- Project theorems the blueprint never names: 15.

## Author `\uses` edges vs Lean

Over the 40 formalised nodes. Lean edges are projected onto blueprint nodes through unlabelled helper declarations.

| | count |
|---|---:|
| Author edges | 57 |
| … also a direct Lean dependency | 42 |
| … implied by a chain of Lean dependencies | 0 |
| … not a Lean dependency at all | 15 |
| Lean edges | 64 |
| … not written by the author | 22 |
| … … of which from a definition node | 11 |

Most frequent sources of unreported edges: `def:charFun` (5), `def:tight` (4), `def:gaussianReal` (2), `lem:bounded_continuous_separating` (2), `lem:dist_integral_mulExpNegMulSq_comp_le` (2), `lem:introduce_exponential` (2), `lem:starSubalgebra_expPoly` (2), `lem:exp_character` (1), `lem:ext_charFun` (1), `lem:isTightMeasureSet_iff_norm` (1).

## Ordering (Phase 0 metrics) on both graphs

Share of random orders better than the human order (0% = human beats all):

| Scope | n | edges | Kahn null | uniform null | mean open: human / optimised / uniform median | τ(human, optimised) |
|---|---:|---:|---:|---:|---:|---:|
| author \uses graph (whole) | 40 | 57 | 0% | 0% | 7.4 / 5.1 / 11.8 | +0.44 |
| Lean-derived graph (whole) | 40 | 64 | 0% | 0% | 6.9 / 4.2 / 10.8 | +0.44 |
| Lean-derived, no definition edges (whole) | 40 | 37 | 0% | 0% | 5.4 / 2.4 / 8.3 | +0.30 |
| Lean: separating | 10 | 9 | 8% | 4% | 1.9 / 1.3 / 2.7 | +0.69 |
| Lean: char_fun | 13 | 17 | 35% | 53% | 2.7 / 1.7 / 2.7 | +0.15 |

Forward references in the human order under Lean edges: 0


## `\lean{}` names not found in the project

- `lem:isTightMeasureSet_iff_basis`: `isTightMeasureSet_iff_tendsto_limsup_inner`
- `lem:charFun_contDiff`: `contDiff_charFun`
- `lem:charFun_continuous`: `continuous_charFun`
- `lem:deriv_charFun`: `iteratedDeriv_charFun`
- `lem:charFun_taylor`: `taylor_charFun`

![mean open](phase1_mean_open.png)
