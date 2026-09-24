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

## Chapter (Lean module `PFR.ForMathlib.Entropy.Measure`)

### `ProbabilityTheory.measureEntropy` (definition)
Lean: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` wi…

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure` (theorem)
Lean: `(μ : Measure S) : Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`

### `ProbabilityTheory.FiniteSupport` (definition)
Lean: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.

### `ProbabilityTheory.integrable_of_finiteSupport` (theorem)
Lean: `(μ : Measure S) : Integrable f μ`
Docstring: The countability hypothesis can probably be dropped here. Proof is unwieldy and can probably be golfed.
Helper lemmas folded into the proof: `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.measure_compl_support`

### `ProbabilityTheory.measureMutualInfo` (definition)
Lean: `(μ : autoParam (Measure (S × T)) measureMutualInfo._auto_1) : ℝ`
Docstring: The mutual information between the marginals of a measure on a product space.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure_finite` (theorem)
Lean: `(hA : μ (↑A)ᶜ = 0) : Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
Helper lemmas folded into the proof: `ProbabilityTheory.measureEntropy_eq_sum`

### `ProbabilityTheory.measureMutualInfo_nonneg_aux` (theorem)
Lean: `0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
Docstring: An ambitious goal would be to replace FiniteSupport with finite entropy. Proof is long and slow; needs to be optimized
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure_finite`: `(hA : μ (↑A)ᶜ = 0) : Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
Helper lemmas folded into the proof: `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.measureEntropy_zero`, `ProbabilityTheory.measureMutualInfo_zero_measure`, `ProbabilityTheory.measure_compl_support`, `ProbabilityTheory.mem_support`

### `ProbabilityTheory.measureMutualInfo_of_not_isFiniteMeasure` (theorem)
Lean: `(h : ¬IsFiniteMeasure μ) : Im[μ] = 0`
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `ProbabilityTheory.measureEntropy_of_not_isFiniteMeasure`, `ProbabilityTheory.measureMutualInfo_def`

### `ProbabilityTheory.measureMutualInfo_univ_smul` (theorem)
Lean: `(μ : Measure (S × U)) : Im[(μ Set.univ)⁻¹ • μ] = Im[μ]`
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.measureMutualInfo_of_not_isFiniteMeasure`: `(h : ¬IsFiniteMeasure μ) : Im[μ] = 0`
Helper lemmas folded into the proof: `ProbabilityTheory.measureEntropy_of_not_isFiniteMeasure`, `ProbabilityTheory.measureEntropy_univ_smul`, `ProbabilityTheory.measureEntropy_zero`, `ProbabilityTheory.measureMutualInfo_def`, `ProbabilityTheory.measureMutualInfo_zero_measure`

### `ProbabilityTheory.measureMutualInfo_nonneg` (theorem)
Lean: `0 ≤ Im[μ]`
Proof uses:
- `ProbabilityTheory.measureMutualInfo_nonneg_aux`: `0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
- `ProbabilityTheory.measureMutualInfo_of_not_isFiniteMeasure`: `(h : ¬IsFiniteMeasure μ) : Im[μ] = 0`
- `ProbabilityTheory.measureMutualInfo_univ_smul`: `(μ : Measure (S × U)) : Im[(μ Set.univ)⁻¹ • μ] = Im[μ]`
Helper lemmas folded into the proof: `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.ae_mem_support`, `ProbabilityTheory.finiteSupport_of_mul`, `ProbabilityTheory.measure_compl_support`
