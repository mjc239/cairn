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

## Chapter (Lean module `APAP.Physics.DRC`)

### `s` (definition)
Lean: `(p : NNReal) (ε : ℝ) (B₁ : Finset G) (B₂ : Finset G) (A : Finset G) : Finset G`

### `drc` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hp₂ : 2 ≤ p) (f : G → NNReal) (hf : ∃ x ∈ B₁ - B₂, x ∈ A - A ∧ x ∈ Function.support f) (hB : (B₁ ∩ B₂).Nonempty) (hA : A.Nonempty) : ∃ A₁ ⊆ B₁, ∃ A₂ ⊆ B₂, ⟪mu A₁ ○ᵈ mu A₂, NNReal.toReal ∘ f⟫_[ℝ] * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ p ≤ 2 * ∑ x, (mu B₁ ○ᵈ mu B₂) x * (((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1) x ^ p * ↑(f x) ∧ 4⁻¹ * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ (2 * p) / ↑A.card ^ (2 * p) ≤ ↑A₁.card / ↑B₁.card ∧ 4⁻¹ * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ (2 * p) / ↑A.card ^ (2 * p) ≤ ↑A₂.card / ↑B₂.card`
Proof uses:
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Helper lemmas folded into the proof: `NNReal.coe_comp_mu`, `NNReal.coe_dddconv`, `NNReal.coe_mu`, `c`, `card_smul_mu`, `card_smul_mu_apply`, `dLpNorm_ddconv_pos`, `ddconv_apply_add`

### `sifting` (theorem)
Lean: `[DiscreteMeasurableSpace G] (B₁ : Finset G) (B₂ : Finset G) (hε : 0 < ε) (hε₁ : ε ≤ 1) (hδ : 0 < δ) (hp : Even p) (hp₂ : 2 ≤ p) (hpε : ε⁻¹ * Real.log (2 / δ) ≤ ↑p) (hB : (B₁ ∩ B₂).Nonempty) (hA : A.Nonempty) (hf : ∃ x ∈ B₁ - B₂, x ∈ A - A ∧ x ∉ s (↑p) ε B₁ B₂ A) : ∃ A₁ ⊆ B₁, ∃ A₂ ⊆ B₂, 1 - δ ≤ ∑ x ∈ s (↑p) ε B₁ B₂ A, (mu A₁ ○ᵈ mu A₂) x ∧ 4⁻¹ * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ (2 * p) / ↑A.card ^ (2 * p) ≤ ↑A₁.card / ↑B₁.card ∧ 4⁻¹ * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ (2 * p) / ↑A.card ^ (2 * p) ≤ ↑A₂.card / ↑B₂.card`
Proof uses:
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `drc`: `[DiscreteMeasurableSpace G] (hp₂ : 2 ≤ p) (f : G → NNReal) (hf : ∃ x ∈ B₁ - B₂, x ∈ A - A ∧ x ∈ Function.support f) (hB : (B₁ ∩ B₂).Nonempty) (hA : A.Nonempty) : ∃ A₁ ⊆ B₁, ∃ A₂ ⊆ B₂, ⟪mu A₁ ○ᵈ mu A₂, NNReal.toReal ∘ f⟫_[ℝ] * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ p ≤ 2 * ∑ x, (mu B₁ ○ᵈ mu B₂) x * (((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1) x ^ p * ↑(f x) ∧ 4⁻¹ * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu…`
Helper lemmas folded into the proof: `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dL1Norm_mu_le_one`, `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_conj`, `MeasureTheory.dLpNorm_conjneg`, `MeasureTheory.dLpNorm_const_smul`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`

### `sifting_cor` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hε : 0 < ε) (hε₁ : ε ≤ 1) (hδ : 0 < δ) (hp : Even p) (hp₀ : p ≠ 0) (hpε : ε⁻¹ * Real.log (2 / δ) ≤ ↑p) (hA : A.Nonempty) : ∃ A₁ A₂, 1 - δ ≤ ∑ x ∈ s (↑p) ε Finset.univ Finset.univ A, (mu A₁ ○ᵈ mu A₂) x ∧ 4⁻¹ * ↑A.dens ^ (2 * p) ≤ ↑A₁.dens ∧ 4⁻¹ * ↑A.dens ^ (2 * p) ≤ ↑A₂.dens`
Docstring: Special case of `sifting` when `B₁ = B₂ = univ`.
Proof uses:
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `sifting`: `[DiscreteMeasurableSpace G] (B₁ : Finset G) (B₂ : Finset G) (hε : 0 < ε) (hε₁ : ε ≤ 1) (hδ : 0 < δ) (hp : Even p) (hp₂ : 2 ≤ p) (hpε : ε⁻¹ * Real.log (2 / δ) ≤ ↑p) (hB : (B₁ ∩ B₂).Nonempty) (hA : A.Nonempty) (hf : ∃ x ∈ B₁ - B₂, x ∈ A - A ∧ x ∉ s (↑p) ε B₁ B₂ A) : ∃ A₁ ⊆ B₁, ∃ A₂ ⊆ B₂, 1 - δ ≤ ∑ x ∈ s (↑p) ε B₁ B₂ A, (mu A₁ ○ᵈ mu A₂) x ∧ 4⁻¹ * ‖((↑A).indicator fun x => 1) ○ᵈ (↑A).indicator fun x => 1‖_[↑p, mu B₁ ○ᵈ mu B₂] ^ (2 * p) / ↑A.card ^ (2 * p) ≤ ↑A₁.card / ↑B₁.card ∧ 4⁻¹ * ‖((↑A).indica…`
- `wLpNorm`: `(p : ENNReal) (w : α → NNReal) (f : α → E) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dL1Norm_indicator_one`, `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_conj`, `MeasureTheory.dLpNorm_conjneg`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`, `MeasureTheory.dLpNorm_exponent_zero`
