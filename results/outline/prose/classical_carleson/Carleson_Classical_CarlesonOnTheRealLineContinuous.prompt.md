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

## Chapter (Lean module `Carleson.Classical.CarlesonOnTheRealLineContinuous`)

### `rcarleson` (theorem)
Lean: `(hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 2) * volume G ^ 2⁻¹ * volume F ^ 2⁻¹`
Proof uses:
- `rcarleson_general`: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carles…`
Helper lemmas folded into the proof: `C10_0_1`, `C1_0_2`, `C_K`, `K`, `carlesonOperatorReal`, `k`, `partialFourierSum`, `𝕔`

### `rcarleson_general` (theorem)
Lean: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Proof uses:
- `CompatibleFunctions.toFunctionDistances`: `FunctionDistances 𝕜 X`
- `two_sided_metric_carleson`: `(ha : 4 ≤ a) (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hmf …`
Helper lemmas folded into the proof: `AEEqFun.mk_sum`, `AEMeasurable.modulationOperator`, `AddCircle.eLpNorm_liftIoc`, `AddCircle.eLpNorm_liftIoc'`, `AddCircle.haarAddCircle_eq_smul_volume`, `AddCircle.liftIco_coe_apply_of_periodic`, `AddCircle.liftIco_convolution_liftIco`, `AddCircle.liftIco_eq_liftIoc`
