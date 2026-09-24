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

## Chapter (Lean module `APAP.Physics.Unbalancing`)

### `unbalancing` (theorem)
Lean: `[DiscreteMeasurableSpace G] (p : ℕ) (hp : p ≠ 0) (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (f : G → ℝ) (g : G → ℂ) (h : G → ℂ) (hf : g ○ᵈ g = Complex.ofReal ∘ f) (hh : h ○ᵈ h = mu Finset.univ) (hε : ε ≤ ‖f‖_[↑p, mu Finset.univ]) : ∃ p', ↑p' ≤ 2 ^ 10 * ε⁻¹ ^ 2 * ↑p ∧ 1 + ε / 2 ≤ ‖f + 1‖_[↑p', mu Finset.univ]`
Docstring: The unbalancing step. Note that we do the physical proof in order to avoid the Fourier transform.
Proof uses:
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Helper lemmas folded into the proof: `Complex.ofReal_comp_mu`, `Complex.ofReal_mu`, `NNReal.coe_comp_mu`, `NNReal.coe_mu`, `ddconv_apply_add`, `ddconv_conjneg`, `dddconv.congr_simp`, `dddconv_apply_sub`
