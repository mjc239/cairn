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

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Chapter (Lean module `PFR.ForMathlib.FiniteRange.ConditionalProbability`)

### `ProbabilityTheory.sum_meas_smul_cond_fiber'` (theorem)
Lean: `(hX : Measurable X) (μ : Measure Ω) : ∑ x ∈ FiniteRange.toFinset X, μ (X ⁻¹' {x}) • μ[|X ⁻¹' {x}] = μ`
Docstring: The **law of total probability** for a random variable taking finitely many values: a measure `μ` can be expressed as a linear combination of its conditional measures `μ[|X ← x]` on fibers of a random variable `X` valued in a fintype.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.range`
