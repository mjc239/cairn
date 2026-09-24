# Phase 1: flt_regular

*leanprover-community/flt-regular @ 8c3c5a908a63 (2026-08-24), Lean leanprover/lean4:v4.34.0-rc2*

## Formal graph

- Project declarations (after folding compiler auxiliaries): 295 (def: 62, inductive: 1, theorem: 232); 725 project-internal dependency edges.
- Blueprint `\lean{}` names resolved to project declarations: 12 (33%); 12 of 45 blueprint nodes have at least one.
- Project theorems the blueprint never names: 221.

## Author `\uses` edges vs Lean

Over the 12 formalised nodes. Lean edges are projected onto blueprint nodes through unlabelled helper declarations.

| | count |
|---|---:|
| Author edges | 9 |
| … also a direct Lean dependency | 9 |
| … implied by a chain of Lean dependencies | 0 |
| … not a Lean dependency at all | 0 |
| Lean edges | 14 |
| … not written by the author | 5 |
| … … of which from a definition node | 3 |

Most frequent sources of unreported edges: `defn:is_regular_number` (3), `lem:Hilbert92` (1), `lem:roots_of_unity_in_cyclo` (1).

## Ordering (Phase 0 metrics) on both graphs

Share of random orders better than the human order (0% = human beats all):

| Scope | n | edges | Kahn null | uniform null | mean open: human / optimised / uniform median | τ(human, optimised) |
|---|---:|---:|---:|---:|---:|---:|
| author \uses graph (whole) | 12 | 9 | 0% | 0% | 2.1 / 1.9 / 3.4 | +0.48 |
| Lean-derived graph (whole) | 12 | 14 | 1% | 1% | 3.1 / 2.9 / 4.0 | +0.42 |
| Lean-derived, no definition edges (whole) | 12 | 10 | 7% | 2% | 2.6 / 1.8 / 3.3 | +0.58 |
| Lean: fermats-last-theorem-for-regular-primes | 10 | 12 | 1% | 3% | 3.0 / 2.7 / 3.7 | +0.82 |

Forward references in the human order under Lean edges: 2

- `lemma:may_assume_coprime` depends on `defn:is_regular_number`, stated later
- `thm:Kummers_lemma` depends on `lem:Hilbert92`, stated later

## `\lean{}` names not found in the project

- `lemma:alt_definition_of_norm`: `Algebra.norm_eq_prod_embeddings`
- `lemma:alt_definition_of_trace`: `trace_eq_sum_embeddings`
- `defn_of_disc`: `Algebra.discr`
- `lem:lin_indep_iff_disc_ne_zero`: `Algebra.discr_not_zero_of_basis`
- `lem:disc_change_of_basis`: `Algebra.discr_of_matrix_mulVec`
- `lemma:disc_via_embs`: `Algebra.discr_eq_det_embeddingsMatrixReindex_pow_two`
- `lemma:disc_of_prim_elt_basis`: `Algebra.discr_powerBasis_eq_prod`
- `lemma:diff_of_irr_pol`: `Polynomial.aeval_root_derivative_of_splits`
- `lemma:num_field_disc_in_terms_of_norm`: `Algebra.discr_powerBasis_eq_norm`
- `lemma:norm_of_alg_int_is_int`: `Algebra.isIntegral_norm`
- `lemma:trace_of_alg_int_is_int`: `Algebra.isIntegral_trace`
- `lemma:int_basis_int_disc`: `Algebra.discr_isIntegral`
- `lemma:disc_int_basis`: `Algebra.discr_mul_isIntegral_mem_adjoin`
- `lemma:eis_crit_and_alg_ints`: `mem_adjoin_of_smul_prime_pow_smul_of_minpoly_isEisensteinAt`
- `lemma:cyclo_poly_deg`: `Polynomial.degree_cyclotomic`
- `lemma:cyclo_poly_irr`: `Polynomial.cyclotomic.irreducible`
- `lem:discr_of_cyclo`: `IsCyclotomicExtension.Rat.discr_prime_pow'`
- `theorem:ring_of_ints_of_cyclo`: `IsCyclotomicExtension.Rat.isIntegralClosure_adjoin_singleton_of_prime_pow`
- `lemma:alg_int_abs_val_one`: `mem_roots_of_unity_of_abs_eq_one`
- `lemma:unit_lemma`: `unit_lemma_gal_conj`
- `lemma:zeta_pow_sub_eq_unit_zeta_sub_one`: `is_primitive_root.zeta_pow_sub_eq_unit_zeta_sub_one`
- `lemma:ideals_mult_to_power`: `ideal.exists_eq_pow_of_mul_eq_pow`
- `lem:exists_alg_int`: `exists_alg_int`
- `Hilbert90`: `Hilbert90`

![mean open](phase1_mean_open.png)
