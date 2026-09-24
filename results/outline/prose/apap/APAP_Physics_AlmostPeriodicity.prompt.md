You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (explicit hypotheses and meaningful instance assumptions such as `[Finite G]` are shown; implicit
arguments and purely structural instances such as `[AddCommGroup G]` are omitted), its
docstring if there is one, and, for theorems, the named results its proof uses (with their statements) and the
helper lemmas folded into the proof.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful: keep every hypothesis and the exact conclusion; do not add, drop, strengthen or weaken
   anything. If some notation's meaning is unclear, keep the notation rather than guessing. For a definition, say
   what is being defined.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

## Chapter (Lean module `APAP.Physics.AlmostPeriodicity`)

### `AlmostPeriodicity.LProp` (definition)
Lean: `(k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) : Prop`

### `AlmostPeriodicity.instDecidablePredForallFinLProp` (definition)
Lean: `DecidablePred (LProp✝ k m ε f A)`

### `AlmostPeriodicity.l` (definition)
Lean: `(k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) : Finset (Fin k → G)`

### `AlmostPeriodicity.just_the_triangle_inequality` (theorem)
Lean: `[DiscreteMeasurableSpace G] (ha : a ∈ l k m ε f A) (ha' : (a + fun x => t) ∈ l k m ε f A) (hk : 0 < k) (hm : 1 ≤ m) : ‖translate (-t) (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ 2 * ε * ‖f‖_[2 * ↑m]`
Proof uses:
- `AlmostPeriodicity.LProp`: `(k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) : Prop`
- `AlmostPeriodicity.instDecidablePredForallFinLProp`: `DecidablePred (LProp✝ k m ε f A)`
Helper lemmas folded into the proof: `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`, `MeasureTheory.dLpNorm_exponent_zero`, `MeasureTheory.dLpNorm_nsmul`, `MeasureTheory.dLpNorm_sub_comm`, `MeasureTheory.dLpNorm_sub_le_dLpNorm_sub_add_dLpNorm_sub`, `MeasureTheory.dLpNorm_translate`

### `AlmostPeriodicity.lemma28` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hε : 0 < ε) (hm : 1 ≤ m) (hk : 64 * ↑m / ε ^ 2 ≤ ↑k) : ↑A.card ^ k / 2 ≤ ↑(l k m ε f A).card`
Proof uses:
- `AlmostPeriodicity.LProp`: `(k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) : Prop`
- `AlmostPeriodicity.instDecidablePredForallFinLProp`: `DecidablePred (LProp✝ k m ε f A)`
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `RCLike.marcinkiewicz_zygmund`: `(hm : m ≠ 0) (f : ι → 𝕜) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, ‖∑ i, f (a i)‖ ^ (2 * m) ≤ (8 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, ‖f (a i)‖ ^ (2 * m)`
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `mu`: `(s : Finset α) (_ : α) : K`
Helper lemmas folded into the proof: `AlmostPeriodicity.lemma28_markov`, `AlmostPeriodicity.lemma28_part_two`, `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dL1Norm_mu`, `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_const_smul`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`

### `AlmostPeriodicity.almost_periodicity` (theorem)
Lean: `[DiscreteMeasurableSpace G] (ε : ℝ) (hε : 0 < ε) (hε' : ε ≤ 1) (m : ℕ) (f : G → ℂ) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) : ∃ T, K ^ (-512 * ↑m / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ ε * ‖f‖_[2 * ↑m]`
Proof uses:
- `AlmostPeriodicity.LProp`: `(k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) : Prop`
- `AlmostPeriodicity.instDecidablePredForallFinLProp`: `DecidablePred (LProp✝ k m ε f A)`
- `AlmostPeriodicity.just_the_triangle_inequality`: `[DiscreteMeasurableSpace G] (ha : a ∈ l k m ε f A) (ha' : (a + fun x => t) ∈ l k m ε f A) (hk : 0 < k) (hm : 1 ≤ m) : ‖translate (-t) (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ 2 * ε * ‖f‖_[2 * ↑m]`
- `AlmostPeriodicity.l`: `(k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) : Finset (Fin k → G)`
- `AlmostPeriodicity.lemma28`: `[DiscreteMeasurableSpace G] (hε : 0 < ε) (hm : 1 ≤ m) (hk : 64 * ↑m / ε ^ 2 ≤ ↑k) : ↑A.card ^ k / 2 ≤ ↑(l k m ε f A).card`
Helper lemmas folded into the proof: `AlmostPeriodicity.T_bound`, `Finset.big_shifts_step1`, `Finset.reindex_count`, `MeasureTheory.dLpNorm_exponent_zero`, `MeasureTheory.dLpNorm_nonneg`, `MeasureTheory.dLpNorm_zero`, `big_shifts`, `big_shifts_step2`

### `AlmostPeriodicity.linfty_almost_periodicity` (theorem)
Lean: `[DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
Proof uses:
- `AlmostPeriodicity.almost_periodicity`: `[DiscreteMeasurableSpace G] (ε : ℝ) (hε : 0 < ε) (hε' : ε ≤ 1) (m : ℕ) (f : G → ℂ) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) : ∃ T, K ^ (-512 * ↑m / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ ε * ‖f‖_[2 * ↑m]`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Helper lemmas folded into the proof: `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_const_smul`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`, `MeasureTheory.dLpNorm_indicator_one`, `MeasureTheory.dLpNorm_mu`, `MeasureTheory.dLpNorm_mul_le`

### `AlmostPeriodicity.linfty_almost_periodicity_boosted` (theorem)
Lean: `[DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (k : ℕ) (hk : k ≠ 0) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (hS : S.Nonempty) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ * ↑k ^ 2 / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ‖mu T ∗ᵈ^ k ∗ᵈ ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
Proof uses:
- `AlmostPeriodicity.linfty_almost_periodicity`: `[DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `trivChar`: `(_ : G) : R`
Helper lemmas folded into the proof: `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_add_le`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`, `MeasureTheory.dLpNorm_expect_le`, `MeasureTheory.dLpNorm_exponent_zero`, `MeasureTheory.dLpNorm_translate`, `MeasureTheory.dLpNorm_translate_sum_sub_le`
