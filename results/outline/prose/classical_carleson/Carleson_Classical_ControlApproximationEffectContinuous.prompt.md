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

## Chapter (Lean module `Carleson.Classical.ControlApproximationEffectContinuous`)

### `rcarleson_exceptional_set_estimate_specific` (theorem)
Lean: `(Cpos : 0 < C) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C) (measurableSetE : MeasurableSet E) (E_subset : E ⊆ Set.Icc 0 (2 * Real.pi)) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * ENNReal.ofReal (2 * Real.pi + 2) ^ 2⁻¹ * volume E ^ 2⁻¹`
Proof uses:
- `rcarleson_exceptional_set_estimate`: `(Cpos : 0 < C) (hmf : Measurable f) (measurableSetF : MeasurableSet F) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator 1 x) (measurableSetE : MeasurableSet E) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x…`
Helper lemmas folded into the proof: `C10_0_1`, `C1_0_2`, `C_K`, `K`, `carlesonOperatorReal`, `carlesonOperatorReal_eq_of_restrict_interval`, `k`, `k_of_one_le_abs`

### `rcarleson_exceptional_set_estimate` (theorem)
Lean: `(Cpos : 0 < C) (hmf : Measurable f) (measurableSetF : MeasurableSet F) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator 1 x) (measurableSetE : MeasurableSet E) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * volume F ^ 2⁻¹ * volume E ^ 2⁻¹`
Proof uses:
- `rcarleson`: `(hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 2) * volume G ^ 2⁻…`
Helper lemmas folded into the proof: `C10_0_1`, `C1_0_2`, `C_K`, `K`, `carlesonOperatorReal`, `carlesonOperatorReal_mul`, `k`, `partialFourierSum`
