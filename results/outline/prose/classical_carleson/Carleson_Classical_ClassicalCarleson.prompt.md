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

## Chapter (Lean module `Carleson.Classical.ClassicalCarleson`)

### `classical_carleson` (theorem)
Lean: `(cont_f : Continuous f) (periodic_f : Function.Periodic f (2 * Real.pi)) : ∀ᵐ (x : ℝ), Filter.Tendsto (fun x_1 => partialFourierSum x_1 f x) Filter.atTop (nhds (f x))`
Proof uses:
- `rcarleson_exceptional_set_estimate_specific`: `(Cpos : 0 < C) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C) (measurableSetE : MeasurableSet E) (E_subset : E ⊆ Set.Icc 0 (2 * Real.pi)) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * vol…`
Helper lemmas folded into the proof: `C10_0_1`, `C10_0_1_pos`, `C1_0_2`, `C1_0_2_pos`, `C_K`, `C_K_pos`, `C_control_approximation_effect'`, `C_control_approximation_effect'_le`
