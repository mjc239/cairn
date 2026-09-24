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

## Chapter (Lean module `PFR.ForMathlib.Entropy.Kernel.Basic`)

### `ProbabilityTheory.Kernel.entropy` (definition)
Lean: `(κ : Kernel T S) (μ : Measure T) : ℝ`
Docstring: Entropy of a kernel with respect to a measure.

### `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit` (theorem)
Lean: `(κ : Kernel T S) : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.Measure.comap_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.FiniteSupport.comap_equiv`, `ProbabilityTheory.Kernel.entropy_comap`, `ProbabilityTheory.Kernel.entropy_comap_equiv`, `ProbabilityTheory.measure_compl_support`

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib` (theorem)
Lean: `(X : Ω → S) (Y : Ω → T) (μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.condDistrib_ae_eq`, `ProbabilityTheory.condDistrib_apply`, `ProbabilityTheory.condDistrib_apply'`, `ProbabilityTheory.finiteSupport_of_finiteRange`

### `ProbabilityTheory.Kernel.entropy_compProd` (theorem)
Lean: `(hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Proof uses:
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk`: `(hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`: `(_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.integrable_of_finiteSupport`: `(μ : Measure S) : Integrable f μ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ae_of_ae_compProd`, `MeasureTheory.Measure.ae_of_compProd_eq_zero`, `MeasureTheory.Measure.support`, `MeasureTheory.lintegral_eq_setLIntegral`, `MeasureTheory.setLIntegral_eq_sum`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.ae_eq_mk`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.isMarkovKernel_mk`

### `ProbabilityTheory.Kernel.chain_rule` (theorem)
Lean: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
Proof uses:
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond`: `(μ : Measure T) (hκ : κ.AEFiniteKernelSupport μ) : κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
- `ProbabilityTheory.Kernel.disintegration`: `(κ : Kernel T (S × U)) : κ = κ.fst.compProd κ.condKernel`
- `ProbabilityTheory.Kernel.entropy_compProd`: `(hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Helper lemmas folded into the proof: `ProbabilityTheory.Kernel.AEFiniteKernelSupport.fst`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.map`, `ProbabilityTheory.Kernel.FiniteKernelSupport.aefiniteKernelSupport`, `ProbabilityTheory.Kernel.aefiniteKernelSupport_zero`, `ProbabilityTheory.Kernel.finiteKernelSupport_zero`
