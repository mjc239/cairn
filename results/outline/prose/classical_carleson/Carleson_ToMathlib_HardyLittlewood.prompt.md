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

## Chapter (Lean module `Carleson.ToMathlib.HardyLittlewood`)

### `hasStrongType_maximalFunction` (theorem)
Lean: `(hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Docstring: The `maximalFunction` has strong type when `p₁ < p₂`.
Proof uses:
- `hasStrongType_maximalFunction_one`: `(hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Helper lemmas folded into the proof: `C2_0_6`, `CMB`, `MeasureTheory.C_realInterpolation`, `MeasureTheory.C_realInterpolation_ENNReal`, `MeasureTheory.HasStrongType`, `MeasureTheory.Measure.IsDoubling`, `enorm_NNReal`, `iSup_rpow`

### `hasStrongType_maximalFunction_one` (theorem)
Lean: `(hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Docstring: Special case of equation (2.0.44). The proof is given between (9.0.12) and (9.0.34). Use the real interpolation theorem instead of following the blueprint.
Proof uses:
- `MeasureTheory.exists_hasStrongType_real_interpolation`: `(hp₀ : p₀ ∈ Set.Ioc 0 q₀) (hp₁ : p₁ ∈ Set.Ioc 0 q₁) (hq₀q₁ : q₀ ≠ q₁) (hA : 1 ≤ A) (ht : t ∈ Set.Ioo 0 1) (hC₀ : 0 < C₀) (hC₁ : 0 < C₁) (hp : p⁻¹ = (1 - t) / p₀ + t / p₁) (hq : q⁻¹ = (1 - t) / q₀ + t…`
Helper lemmas folded into the proof: `CMB`, `MeasureTheory.AESubadditiveOn`, `MeasureTheory.AESublinearOn`, `MeasureTheory.A_pos`, `MeasureTheory.C_realInterpolation`, `MeasureTheory.C_realInterpolation_ENNReal`, `MeasureTheory.HasStrongType`, `MeasureTheory.HasStrongType.hasWeakType`
