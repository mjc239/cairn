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

## Chapter (Lean module `PFR.ForMathlib.Entropy.Group`)

### `ProbabilityTheory.entropy_add_right` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
Docstring: `H[X, X + Y] = H[X, Y]`
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.measureEntropy_map_of_injective`

### `ProbabilityTheory.entropy_add_left` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
Docstring: `H[Y + X, Y] = H[X, Y]`
Proof uses:
- `ProbabilityTheory.entropy_add_right`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.entropy_comm`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.measureEntropy_map_of_injective`

### `ProbabilityTheory.entropy_sub_mutualInfo_le_entropy_sub` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) : H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Docstring: `H[X] - I[X : Y] ≤ H[X - Y]`
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport`: `(κ : Kernel T S) (μ : Measure T) : Prop`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`: `(κ : Kernel T S) : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
- `ProbabilityTheory.condEntropy`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `FiniteRange.sub`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`
