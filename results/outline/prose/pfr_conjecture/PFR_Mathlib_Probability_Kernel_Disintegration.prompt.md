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

## Chapter (Lean module `PFR.Mathlib.Probability.Kernel.Disintegration`)

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (definition)
Lean: `(κ : Kernel T S) (μ : Measure T) : Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk` (definition)
Lean: `(_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
Docstring: The definition doesn't use `_hκ`, but we keep it here still as it doesn't give anything interesting otherwise.

### `ProbabilityTheory.Kernel.FiniteKernelSupport` (definition)
Lean: `(κ : Kernel T S) : Prop`
Docstring: The analogue of FiniteSupport for probability kernels.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk` (theorem)
Lean: `(hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
Helper lemmas folded into the proof: `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk_eq`, `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk_eq_zero_of_isEmpty`, `ProbabilityTheory.Kernel.finiteKernelSupport_zero`

### `ProbabilityTheory.Kernel.disintegration` (theorem)
Lean: `(κ : Kernel T (S × U)) : κ = κ.fst.compProd κ.condKernel`
Helper lemmas folded into the proof: `MeasureTheory.lintegral_eq_tsum`, `ProbabilityTheory.Kernel.condKernel_apply`, `ProbabilityTheory.Kernel.condKernel_apply'`

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond` (theorem)
Lean: `(μ : Measure T) (hκ : κ.AEFiniteKernelSupport μ) : κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
Docstring: Conditioning a kernel preserves finite kernel support.
Helper lemmas folded into the proof: `MeasureTheory.Measure.compProd_apply_singleton`, `ProbabilityTheory.Kernel.condKernel_apply`, `ProbabilityTheory.Kernel.condKernel_apply'`

### `ProbabilityTheory.condDistrib_eq_prod_of_indepFun` (theorem)
Lean: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (h : IndepFun (fun ω => (X ω, Z ω)) (fun ω => (Y ω, W ω)) μ) : ⇑(condDistrib (fun ω => (X ω, Y ω)) (fun ω => (Z ω, W ω)) μ) =ᵐ[Measure.map (fun ω => (Z ω, W ω)) μ] ⇑((Kernel.prodMkRight V (condDistrib X Z μ)).prod (Kernel.prodMkLeft U (condDistrib Y W μ)))`
Helper lemmas folded into the proof: `MeasureTheory.lintegral_eq_tsum`, `ProbabilityTheory.condDistrib_apply`, `ProbabilityTheory.condDistrib_apply'`

### `ProbabilityTheory.condKernel_condDistrib_ae_eq` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : ⇑(condDistrib (fun a => (X a, Y a)) Z μ).condKernel =ᵐ[Measure.map (fun ω => (Z ω, X ω)) μ] ⇑(condDistrib Y (fun ω => (Z ω, X ω)) μ)`
Helper lemmas folded into the proof: `ProbabilityTheory.Kernel.condKernel_apply`, `ProbabilityTheory.Kernel.condKernel_apply'`, `ProbabilityTheory.condDistrib_apply'`
