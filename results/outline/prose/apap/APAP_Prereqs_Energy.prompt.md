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

## Chapter (Lean module `APAP.Prereqs.Energy`)

### `energy` (definition)
Lean: `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`

### `boringEnergy` (definition)
Lean: `(n : ℕ) (s : Finset G) : ℝ`

### `cLpNorm_dft_indicator_one_pow` (theorem)
Lean: `[DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
Proof uses:
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `energy`: `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
- `iterConv`: `(f : G → R) (_ : ℕ) (_ : G) : R`
- `trivChar`: `(_ : G) : R`
Helper lemmas folded into the proof: `Complex.ofReal_comp_indicator_one`, `Complex.ofReal_indicator_one`, `Complex.ofReal_iterConv`, `IsSelfAdjoint.iterConv`, `MeasureTheory.cLpNorm_eq_expect_norm`, `MeasureTheory.cLpNorm_eq_expect_norm'`, `MeasureTheory.cLpNorm_exponent_zero`, `MeasureTheory.cLpNorm_pow_eq_expect_norm`

### `cL2Norm_dft_indicator_one` (theorem)
Lean: `[DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
Proof uses:
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `boringEnergy`: `(n : ℕ) (s : Finset G) : ℝ`
- `cLpNorm_dft_indicator_one_pow`: `[DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `iterConv`: `(f : G → R) (_ : ℕ) (_ : G) : R`
- `trivChar`: `(_ : G) : R`
Helper lemmas folded into the proof: `MeasureTheory.cL2Norm_sq_eq_expect_norm`, `MeasureTheory.cLpNorm_eq_expect_norm`, `MeasureTheory.cLpNorm_eq_expect_norm'`, `MeasureTheory.cLpNorm_nonneg`, `MeasureTheory.cLpNorm_pow_eq_expect_norm`, `MeasureTheory.cLpNorm_rpow_eq_expect_norm`, `MeasureTheory.dL2Norm_sq_eq_sum_norm`, `MeasureTheory.dLpNorm_eq_sum_norm`
