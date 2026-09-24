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

## Chapter (Lean module `PFR.ForMathlib.Entropy.Kernel.RuzsaDist`)

### `ProbabilityTheory.Kernel.rdistm` (definition)
Lean: `(μ : Measure G) (ν : Measure G) : ℝ`
Docstring: The Rusza distance between two measures, defined as `H[X - Y] - H[X]/2 - H[Y]/2` where `X` and `Y` are independent variables distributed according to the two measures.

### `ProbabilityTheory.Kernel.rdist` (definition)
Lean: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.

### `ProbabilityTheory.Kernel.rdist_symm` (theorem)
Lean: `dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
Proof uses:
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
- `ProbabilityTheory.integrable_of_finiteSupport`: `(μ : Measure S) : Integrable f μ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.Measure.comap_real_apply`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.FiniteSupport.comap_equiv`, `ProbabilityTheory.Kernel.entropy_comap`, `ProbabilityTheory.Kernel.entropy_comap_equiv`
