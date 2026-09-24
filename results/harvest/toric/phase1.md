# Phase 1: toric

*YaelDillies/Toric @ 6eef2aacaa5e (2026-09-20), Lean leanprover/lean4:v4.35.0-rc2*

## Formal graph

- Project declarations (after folding compiler auxiliaries): 276 (def: 82, inductive: 7, theorem: 187); 1383 dependency edges, including 59 blueprint-named declarations outside the project (e.g. upstreamed to Mathlib).
- Blueprint `\lean{}` names resolved to project declarations: 89 (100%); 67 of 145 blueprint nodes have at least one.
- Project theorems the blueprint never names: 178.

## Author `\uses` edges vs Lean

Over the 67 formalised nodes. Lean edges are projected onto blueprint nodes through unlabelled helper declarations.

| | count |
|---|---:|
| Author edges | 86 |
| … also a direct Lean dependency | 53 |
| … implied by a chain of Lean dependencies | 5 |
| … not a Lean dependency at all | 28 |
| Lean edges | 144 |
| … not written by the author | 91 |
| … … of which from a definition node | 60 |

Most frequent sources of unreported edges: `0-diag` (12), `0-spec-alg` (11), `0-torus` (8), `0-spec-cocomm-bialg` (7), `1-2-1-cone-hull` (7), `0-bialg-equiv-comon-alg` (6), `0-spec-bialg` (5), `0-grp-like` (4), `0-hopf-alg-equiv-cogrp-alg` (4), `0-aff-mon` (3).

## Ordering (Phase 0 metrics) on both graphs

Share of random orders better than the human order (0% = human beats all):

| Scope | n | edges | Kahn null | uniform null | mean open: human / optimised / uniform median | τ(human, optimised) |
|---|---:|---:|---:|---:|---:|---:|
| author \uses graph (whole) | 67 | 86 | 0% | 0% | 7.4 / 4.9 / 14.9 | +0.28 |
| Lean-derived graph (whole) | 67 | 144 | 0% | 0% | 10.3 / 7.2 / 17.7 | +0.38 |
| Lean-derived, no definition edges (whole) | 67 | 48 | 6% | 0% | 6.0 / 1.6 / 8.5 | +0.16 |
| Lean: 2-2-affine-monoids | 8 | 5 | 45% | 26% | 1.1 / 0.9 / 1.3 | +0.43 |
| Lean: 2-3-hopf-algebras | 15 | 16 | 4% | 0% | 2.3 / 1.6 / 3.4 | -0.18 |
| Lean: 4-1-affine-group-schemes | 10 | 20 | 26% | 8% | 3.2 / 2.8 / 3.6 | +0.29 |
| Lean: 4-3-torus | 10 | 27 | 69% | 55% | 4.3 / 4.1 / 4.3 | +0.73 |

Forward references in the human order under Lean edges: 8

- `0-embed-aff-mon` depends on `1-2-1-cone-hull`, stated later
- `0-grp-like-grp-alg-span` depends on `1-2-1-cone-hull`, stated later
- `0-grp-like-lin-indep` depends on `1-2-1-cone-hull`, stated later
- `0-grp-like-grp-alg` depends on `1-2-1-cone-hull`, stated later
- `0-is-diag-bialg-group-like-span` depends on `1-2-1-cone-hull`, stated later
- `0-is-diag-bialg-iff-span-group-like` depends on `1-2-1-cone-hull`, stated later
- `0-is-diag` depends on `0-torus`, stated later
- `0-diag-spec` depends on `0-torus`, stated later

![mean open](phase1_mean_open.png)
