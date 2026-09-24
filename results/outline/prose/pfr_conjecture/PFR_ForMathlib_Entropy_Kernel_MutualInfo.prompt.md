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

## Chapter (Lean module `PFR.ForMathlib.Entropy.Kernel.MutualInfo`)

### `ProbabilityTheory.Kernel.mutualInfo` (definition)
Lean: `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
Docstring: Mutual information of a kernel into a product space with respect to a measure.

### `ProbabilityTheory.Kernel.mutualInfo_nonneg` (theorem)
Lean: `(hκ : κ.AEFiniteKernelSupport μ) : 0 ≤ Ik[κ , μ]`
Proof uses:
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk`: `(hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`: `(_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.measureMutualInfo_nonneg`: `0 ≤ Im[μ]`
Helper lemmas folded into the proof: `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.ae_eq_mk`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk_eq`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk_eq_zero_of_isEmpty`, `ProbabilityTheory.Kernel.entropy_congr`, `ProbabilityTheory.Kernel.mutualInfo_congr`, `ProbabilityTheory.Kernel.mutualInfo_nonneg'`
