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

## Chapter (Lean module `APAP.Prereqs.Rudin`)

### `rudin_ineq` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
Docstring: **Rudin's inequality**, usual form.
Proof uses:
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
Helper lemmas folded into the proof: `Mathlib.Meta.Positivity.cLpNorm_pos_of_ne_zero`, `MeasureTheory.Complex.cLpNorm_coe_comp`, `MeasureTheory.RCLike.cLpNorm_coe_comp`, `MeasureTheory.cL2Norm_sq_eq_expect_norm`, `MeasureTheory.cLpNorm_add_le`, `MeasureTheory.cLpNorm_const_smul`, `MeasureTheory.cLpNorm_eq_expect_norm`, `MeasureTheory.cLpNorm_eq_expect_norm'`
