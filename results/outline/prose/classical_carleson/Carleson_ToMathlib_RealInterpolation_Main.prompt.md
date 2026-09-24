You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (only explicit hypotheses are shown; implicit and type-class assumptions are omitted), its
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

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

## Chapter (Lean module `Carleson.ToMathlib.RealInterpolation.Main`)

### `MeasureTheory.exists_hasStrongType_real_interpolation` (theorem)
Lean: `(hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (hq₀q₁ : q₀ ≠ q₁) (hA : 1 ≤ A) (ht : t ∈ Set.Ioo 0 1) (hC₀ : 0 < C₀) (hC₁ : 0 < C₁) (hp : p⁻¹ = (1 - t) / p₀ + t / p₁) (hq : q⁻¹ = (1 - t) / q₀ + t / q₁) (hmT : ∀ (f : α → E₁), MemLp f p μ → AEStronglyMeasurable (T f) ν) (hT : AESubadditiveOn T (fun f => MemLp f p₀ μ ∨ MemLp f p₁ μ) (↑A) ν) (h₀T : HasWeakType T p₀ q₀ μ ν ↑C₀) (h₁T : HasWeakType T p₁ q₁ μ ν ↑C₁) : HasStrongType T p q μ ν ↑(C_realInterpolation p₀ p₁ q₀ q₁ q C₀ C₁ A t)`
Docstring: Marcinkiewicz real interpolation theorem
Proof uses:
- `MeasureTheory.exists_hasStrongType_real_interpolation_aux₄`: `(hA : 0 < A) (hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (hq₀q₁ : q₀ ≠ q₁) (ht : t ∈ Set.Ioo 0 1) (hC₀ : 0 < C₀) (hC₁ : 0 < C₁) (hp : p⁻¹ = (1 - t) / p₀ + t / p₁) (hq : q⁻¹ = (1 - t) / q₀ + t…`
Helper lemmas folded into the proof: `ComputationsInterpolatedExponents.interp_exp_between`, `ComputationsInterpolatedExponents.interp_exp_eq`, `ComputationsInterpolatedExponents.interp_exp_ne_top`, `ComputationsInterpolatedExponents.interpolated_pos'`, `ComputationsInterpolatedExponents.ne_inv_toReal_exp_interp_exp`, `ComputationsInterpolatedExponents.ne_inv_toReal_exponents`, `ComputationsInterpolatedExponents.ne_toReal_exp_interp_exp`, `ComputationsInterpolatedExponents.ne_toReal_exp_interp_exp₁`

### `MeasureTheory.combine_estimates₁` (theorem)
Lean: `(hA : 0 < A) (hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (ht : t ∈ Set.Ioo 0 1) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻¹) (hf : MemLp f p μ) (hT : SubadditiveTrunc T (↑A) f ν) (h₁T : HasWeakType T p₁ q₁ μ ν ↑C₁) (h₀T : HasWeakType T p₀ q₀ μ ν ↑C₀) (h₂T : PreservesAEStrongMeasurability T p) (hC₀ : 0 < C₀) (hC₁ : 0 < C₁) (hF : eLpNorm f p μ ∈ Set.Ioo 0 ⊤) (hspf : spf = ChoiceScale.spf_ch ⋯ hq₀q₁ ⋯ ⋯ ⋯ ⋯ ⋯ hC₀ hC₁ hF) : eLpNorm (T f) q ν ≤ ENNReal.ofReal (2 * ↑A) * q ^ q⁻¹.toReal * ((if q₁ < ⊤ then 1 else 0) * ENNRea…`
Proof uses:
- `MeasureTheory.combine_estimates₀`: `(hA : 0 < A) (hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (ht : t ∈ Set.Ioo 0 1) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻…`
Helper lemmas folded into the proof: `ChoiceScale.d`, `ChoiceScale.d_ne_top_aux₀`, `ChoiceScale.d_ne_top_aux₂`, `ChoiceScale.d_ne_top_aux₃`, `ChoiceScale.d_ne_top_aux₄`, `ChoiceScale.d_ne_zero_aux₀`, `ChoiceScale.d_ne_zero_aux₂`, `ChoiceScale.d_ne_zero_aux₃`

### `MeasureTheory.combine_estimates₀` (theorem)
Lean: `(hA : 0 < A) (hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (ht : t ∈ Set.Ioo 0 1) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻¹) (hf : MemLp f p μ) (hT : SubadditiveTrunc T (↑A) f ν) (hC₀ : 0 < C₀) (hC₁ : 0 < C₁) (hF : eLpNorm f p μ ∈ Set.Ioo 0 ⊤) (hspf : spf = ChoiceScale.spf_ch ⋯ hq₀q₁ ⋯ ⋯ ⋯ ⋯ ⋯ hC₀ hC₁ hF) (h₁T : HasWeakType T p₁ q₁ μ ν ↑C₁) (h₀T : HasWeakType T p₀ q₀ μ ν ↑C₀) (h₂T : PreservesAEStrongMeasurability T p) : ∫⁻ (x : α'), ‖T f x‖ₑ ^ q.toReal ∂ν ≤ ENNReal.ofReal ((2 * ↑A) ^ q.toReal * q.toReal) * ((if q₁ < …`
Proof uses:
- `MeasureTheory.estimate_trnc₁`: `(ht : t ∈ Set.Ioo 0 1) (hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₁ : 0 < p₁) (hq₁ : 0 < q₁) (hpq : sel j p₀ p₁ ≤ sel j q₀ q₁) (hp' : sel j p₀ p₁ ≠ ⊤) (hq' : sel j q₀ q₁ ≠ ⊤) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁…`
Helper lemmas folded into the proof: `ChoiceScale.d`, `ChoiceScale.d_eq_top_top`, `ChoiceScale.d_eq_top₀`, `ChoiceScale.d_eq_top₁`, `ChoiceScale.d_ne_top_aux₀`, `ChoiceScale.d_ne_top_aux₂`, `ChoiceScale.d_ne_top_aux₃`, `ChoiceScale.d_ne_top_aux₄`

### `MeasureTheory.exists_hasStrongType_real_interpolation_aux₄` (theorem)
Lean: `(hA : 0 < A) (hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (hq₀q₁ : q₀ ≠ q₁) (ht : t ∈ Set.Ioo 0 1) (hC₀ : 0 < C₀) (hC₁ : 0 < C₁) (hp : p⁻¹ = (1 - t) / p₀ + t / p₁) (hq : q⁻¹ = (1 - t) / q₀ + t / q₁) (hT : SubadditiveTrunc T (↑A) f ν) (h₀T : HasWeakType T p₀ q₀ μ ν ↑C₀) (h₁T : HasWeakType T p₁ q₁ μ ν ↑C₁) (h₂T : PreservesAEStrongMeasurability T p) (hf : MemLp f p μ) : eLpNorm (T f) q ν ≤ (if p₀ = p₁ then 1 else ENNReal.ofReal (2 * ↑A)) * q ^ q⁻¹.toReal * ((if q₁ < ⊤ then 1 else 0) * ENNReal.ofReal |q.toReal - q₁.toReal|⁻¹ + (if q₀ < ⊤ then 1 else 0) * ENNReal.ofReal |q.toReal - q₀.toRea…`
Docstring: The main estimate for the real interpolation theorem, before taking roots, combining the cases `p₀ ≠ p₁` and `p₀ = p₁`.
Proof uses:
- `MeasureTheory.combine_estimates₁`: `(hA : 0 < A) (hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (ht : t ∈ Set.Ioo 0 1) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻…`
Helper lemmas folded into the proof: `ChoiceScale.d`, `ChoiceScale.d_eq_top_of_eq`, `ChoiceScale.d_eq_top₁`, `ChoiceScale.d_ne_top`, `ChoiceScale.d_ne_top_aux₀`, `ChoiceScale.d_ne_top_aux₂`, `ChoiceScale.d_ne_top_aux₃`, `ChoiceScale.d_ne_top_aux₄`
