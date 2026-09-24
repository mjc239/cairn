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

## Chapter (Lean module `APAP.Prereqs.Chang`)

### `changConst` (definition)
Lean: `ℝ`

### `AddDissociated.boringEnergy_le` (theorem)
Lean: `[DiscreteMeasurableSpace G] [Finite G] (hs : AddDissociated ↑s) (n : ℕ) : boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
Proof uses:
- `MeasureTheory.cLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `cL2Norm_dft_indicator_one`: `[DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
- `cLpNorm_dft_indicator_one_pow`: `[DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
- `cft`: `(f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
- `dft`: `(f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
- `energy`: `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
- `rudin_ineq`: `[DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
- `trivChar`: `(_ : G) : R`
Helper lemmas folded into the proof: `MeasureTheory.cLpNorm_nonneg`, `boringEnergy_zero`, `cft_dft`, `cft_dft_doubleDualEmb`, `dft_inversion`, `energy_zero`

### `general_hoelder` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
Helper lemmas folded into the proof: `Mathlib.Meta.Positivity.dLpNorm_pos_of_ne_zero`, `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dL2Norm_sq_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`, `MeasureTheory.dLpNorm_eq_zero`, `MeasureTheory.dLpNorm_pos`, `MeasureTheory.dLpNorm_pow_eq_sum_norm`

### `spec_hoelder` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Proof uses:
- `dft`: `(f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
- `energy`: `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
- `general_hoelder`: `[DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
- `trivChar`: `(_ : G) : R`
Helper lemmas folded into the proof: `dft_dft`, `dft_dft_doubleDualEmb`, `dft_injective`, `dft_inversion`, `dft_one`, `dft_smul`, `dft_trivChar`, `energy_nsmul`

### `chang` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Docstring: **Chang's lemma**.
Proof uses:
- `AddDissociated.boringEnergy_le`: `[DiscreteMeasurableSpace G] [Finite G] (hs : AddDissociated ↑s) (n : ℕ) : boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
- `boringEnergy`: `(n : ℕ) (s : Finset G) : ℝ`
- `spec_hoelder`: `[DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Helper lemmas folded into the proof: `Mathlib.Meta.Positivity.dLpNorm_pos_of_ne_zero`, `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dL2Norm_sq_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm'`, `MeasureTheory.dLpNorm_eq_zero`, `MeasureTheory.dLpNorm_pos`, `MeasureTheory.dLpNorm_pow_eq_sum_norm`
