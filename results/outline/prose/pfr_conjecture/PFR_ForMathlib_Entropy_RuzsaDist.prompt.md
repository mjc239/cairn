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

## Chapter (Lean module `PFR.ForMathlib.Entropy.RuzsaDist`)

### `condRuzsaDist` (definition)
Lean: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
Docstring: The conditional Ruzsa distance `d[X|Z ; Y|W]`.

### `condRuzsaDist'` (definition)
Lean: `(X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) : ℝ`
Docstring: The conditional Ruzsa distance `d[X ; Y|W]`.

### `rdist` (definition)
Lean: `(X : Ω → G) (Y : Ω' → G) (μ : autoParam (Measure Ω) rdist._auto_1) (μ' : autoParam (Measure Ω') rdist._auto_3) : ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.

### `condRuzsaDist'_eq_sum` (theorem)
Lean: `(hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X ; μ # Y | W ; μ'] = ∑ w ∈ FiniteRange.toFinset W, μ'.real (W ⁻¹' {w}) * d[X; μ # Y; μ'[|W ⁻¹' {w}]]`
Docstring: Explicit formula for conditional Ruzsa distance `d[X ; Y | W]`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.range`, `MeasureTheory.Measure.prod_apply_singleton`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.prod_real_singleton`, `ProbabilityTheory.condDistrib_apply`, `ProbabilityTheory.condDistrib_apply'`, `condRuzsaDist'_def`, `rdist_eq_rdistm`

### `condRuzsaDist'_eq_integral` (theorem)
Lean: `(X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X ; μ # Y | W ; μ'] = ∫ (x : T), (fun w => d[X; μ # Y; μ'[|W ⁻¹' {w}]]) x ∂Measure.map W μ'`
Docstring: Explicit formula for conditional Ruzsa distance `d[X ; Y | W]`, in integral form.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `condRuzsaDist'_eq_sum`: `(hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X ; μ # Y | W ; μ'] = ∑ w ∈ FiniteRange.toFinset W, μ'.real (W ⁻¹' {w}) * d[X; μ # Y; μ'[|W ⁻¹' {w}]]`
Helper lemmas folded into the proof: `FiniteRange.range`

### `kaimanovich_vershik` (theorem)
Lean: `(h : iIndepFun ![X, Y, Z] μ) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : H[X + Y + Z; μ] - H[X + Y; μ] ≤ H[Y + Z; μ] - H[Y; μ]`
Docstring: The **Kaimanovich-Vershik inequality**. `H[X + Y + Z] - H[X + Y] ≤ H[Y + Z] - H[Y]`.
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
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`

### `comparison_of_ruzsa_distances` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), H[Y + Z; μ'] - H[Y; μ'] = d[Y; μ' # Z; μ'] + H[Z; μ'] / 2 - H[Y; μ'] / 2`
Proof uses:
- `ProbabilityTheory.independent_copies3_nondep_finiteRange`: `(hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₃ : Measurable X₃) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) (μ₃ : Measure Ω₃) : ∃ A x μA X₁' X₂' X₃', IsProbabilityMeasure μA ∧ iIndepFun ![X₁', X₂', X₃'] μA…`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `kaimanovich_vershik`: `(h : iIndepFun ![X, Y, Z] μ) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : H[X + Y + Z; μ] - H[X + Y; μ] ≤ H[Y + Z; μ] - H[Y; μ]`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.neg`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.add`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.prodMk`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IndepFun.rdist_eq`

### `condRuzsaDist_diff_le` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2`
Docstring: Let `X, Y, Z` be random variables taking values in some abelian group, and with `Y, Z` independent. Then we have `d[X ; Y + Z] - d[X ; Y] ≤ 1/2 (H[Y+ Z] - H[Y])` $$= \tfrac{1}{2} d[Y ; Z] + \tfrac{1}{4} H[Z] - \tfrac{1}{4} H[Y]$$ and $$d[X ; Y|Y+ Z] - d[X ; Y] \leq \tfrac{1}{2} \bigl(H[Y+ Z] - H[Z]\bigr)$$ $$= \tfrac{1}{2} d[Y ; Z] + \tfrac{1}{4} H[Y] - \tfrac{1}{4} H[Z]$$
Proof uses:
- `comparison_of_ruzsa_distances`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), …`

### `condRuzsaDist_of_copy` (theorem)
Lean: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (hX' : Measurable X') (hZ' : Measurable Z') (hY' : Measurable Y') (hW' : Measurable W') (h1 : IdentDistrib (⟨X, Z⟩) (⟨X', Z'⟩) μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') : d[X | Z ; μ # Y | W ; μ'] = d[X' | Z' ; μ'' # Y' | W' ; μ''']`
Docstring: The conditional Ruzsa distance is unchanged if the sets of random variables are replaced with copies.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.range`, `MeasureTheory.Measure.prod_apply_singleton`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.prod_real_apply_singleton`, `ProbabilityTheory.condDistrib_apply'`, `Set.inter_eq_left'`, `Set.inter_eq_right'`, `condRuzsaDist_def`

### `condRuzsaDist_of_indep` (theorem)
Lean: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (h : IndepFun (⟨X, Z⟩) (⟨Y, W⟩) μ) : d[X | Z ; μ # Y | W ; μ] = H[X - Y | ⟨Z, W⟩ ; μ] - H[X | Z ; μ] / 2 - H[Y | W ; μ] / 2`
Docstring: If `$(X,Z)$` and `$(Y,W)$` are independent, then `d[X | Z ; Y | W] = H[X'- Y' | Z', W'] - H[X'|Z']/2 - H[Y'|W']/2`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
- `ProbabilityTheory.condDistrib_eq_prod_of_indepFun`: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (h : IndepFun (fun ω => (X ω, Z ω)) (fun ω => (Y ω, W ω)) μ) : ⇑(condDistrib (fun ω => (X ω, Y ω)) (fun…`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
- `ProbabilityTheory.integrable_of_finiteSupport`: `(μ : Measure S) : Integrable f μ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.entropy_congr`

### `condRuzsaDist_le` (theorem)
Lean: `(μ : Measure Ω) (μ' : Measure Ω') (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) : d[X | Z ; μ # Y | W ; μ'] ≤ d[X; μ # Y; μ'] + I[X : Z ; μ] / 2 + I[Y : W ; μ'] / 2`
Docstring: Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then $$d[X | Z ; Y | W] \leq d[X ; Y] + \tfrac{1}{2} I[X : Z] + \tfrac{1}{2} I[Y : W]$$
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

### `condRuzsaDist_of_const` (theorem)
Lean: `(hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
Docstring: Conditioning by a constant does not affect Ruzsa distance.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
- `ProbabilityTheory.integrable_of_finiteSupport`: `(μ : Measure S) : Integrable f μ`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.condDistrib_apply`, `ProbabilityTheory.condDistrib_apply'`

### `condRuzsaDist_diff_ofsum_le` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (hZ' : Measurable Z') (h : iIndepFun ![Y, Z, Z'] μ') : d[X ; μ # Y + Z | Y + Z + Z' ; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z + Z'; μ'] + H[Y + Z; μ'] - H[Y; μ'] - H[Z'; μ']) / 2`
Proof uses:
- `ProbabilityTheory.entropy_add_right`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist_diff_le`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2`
- `condRuzsaDist_le`: `(μ : Measure Ω) (μ' : Measure Ω') (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) : d[X | Z ; μ # Y | W ; μ'] ≤ d[X; μ # Y; μ'] + I[X : Z ; μ] / 2 + I[Y : W ; μ'] / 2`
- `condRuzsaDist_of_const`: `(hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `ProbabilityTheory.IndepFun.entropy_pair_eq_add`, `ProbabilityTheory.IndepFun.mutualInfo_eq_zero`, `ProbabilityTheory.entropy_pair_eq_add`, `ProbabilityTheory.indepFun_const`, `ProbabilityTheory.indepFun_zero_measure`, `ProbabilityTheory.mutualInfo_add_right`

### `ent_of_diff_le` (theorem)
Lean: `(X : Ω → G) (Y : Ω → G) (Z : Ω → G) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun (⟨X, Y⟩) Z μ) : H[X - Y; μ] ≤ H[X - Z; μ] + H[Z - Y; μ] - H[Z; μ]`
Docstring: The **improved entropic Ruzsa triangle inequality**.
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

### `rdist_triangle` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : d[X; μ # Z; μ''] ≤ d[X; μ # Y; μ'] + d[Y; μ' # Z; μ'']`
Docstring: The **entropic Ruzsa triangle inequality**
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.independent_copies3_nondep_finiteRange`: `(hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₃ : Measurable X₃) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) (μ₃ : Measure Ω₃) : ∃ A x μA X₁' X₂' X₃', IsProbabilityMeasure μA ∧ iIndepFun ![X₁', X₂', X₃'] μA…`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ent_of_diff_le`: `(X : Ω → G) (Y : Ω → G) (Z : Ω → G) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun (⟨X, Y⟩) Z μ) : H[X - Y; μ] ≤ H[X - Z; μ] + H[Z - Y; μ] - H[Z; μ]`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.entropy_def`, `rdist_def`

### `condRuzsaDist_eq_sum` (theorem)
Lean: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X | Z ; μ # Y | W ; μ'] = ∑ z ∈ FiniteRange.toFinset Z, ∑ w ∈ FiniteRange.toFinset W, μ.real (Z ⁻¹' {z}) * μ'.real (W ⁻¹' {w}) * d[X; μ[|Z ⁻¹' {z}] # Y; μ'[|W ⁻¹' {w}]]`
Docstring: Explicit formula for conditional Ruzsa distance $d[X|Z; Y|W]$.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.range`, `MeasureTheory.Measure.prod_apply_singleton`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.prod_real_singleton`, `ProbabilityTheory.condDistrib_apply`, `ProbabilityTheory.condDistrib_apply'`, `condRuzsaDist_def`, `rdist_eq_rdistm`

### `condRuzsaDist'_of_copy` (theorem)
Lean: `(X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (X' : Ω'' → G) (hY' : Measurable Y') (hW' : Measurable W') (h1 : IdentDistrib X X' μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') : d[X ; μ # Y | W ; μ'] = d[X' ; μ'' # Y' | W' ; μ''']`
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdistm`: `(μ : Measure G) (ν : Measure G) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.range`, `MeasureTheory.Measure.prod_apply_singleton`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.prod_real_apply_singleton`, `ProbabilityTheory.condDistrib_apply'`, `Set.inter_eq_left'`, `Set.inter_eq_right'`, `condRuzsaDist'_def`

### `condRuzsaDist_of_inj_map` (theorem)
Lean: `(Y : Fin 4 → Ω → G) (h_indep : IndepFun (⟨Y 0, Y 2⟩) (⟨Y 1, Y 3⟩) μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) (π : G × G →+ G') (hπ : ∀ (h : G), Function.Injective fun g => π (g, h)) : d[⇑π ∘ ⟨Y 0, Y 2⟩ | Y 2 ; μ # ⇑π ∘ ⟨Y 1, Y 3⟩ | Y 3 ; μ] = d[Y 0 | Y 2 ; μ # Y 1 | Y 3 ; μ]`
Proof uses:
- `ProbabilityTheory.condEntropy`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
- `ProbabilityTheory.condEntropy_of_injective`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
- `condRuzsaDist_of_indep`: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (h : IndepFun (⟨X, Z⟩) (⟨Y, W⟩) μ) : d[X | Z ; μ # Y | W ; μ] = H[X - Y | ⟨Z, W⟩ ; μ] - H[X | Z ; μ] / …`
Helper lemmas folded into the proof: `FiniteRange.finite`, `instFiniteRangeProdMk`

### `condRuzsaDist'_of_inj_map` (theorem)
Lean: `(hX : Measurable X) (hB : Measurable B) (hC : Measurable C) (h_indep : IndepFun X (⟨B, C⟩) μ) : d[X ; μ # B | B + C ; μ] = d[X ; μ # C | B + C ; μ]`
Proof uses:
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist_of_const`: `(hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
- `condRuzsaDist_of_inj_map`: `(Y : Fin 4 → Ω → G) (h_indep : IndepFun (⟨Y 0, Y 2⟩) (⟨Y 1, Y 3⟩) μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) (π : G × G →+ G') (hπ : ∀ (h : G), Function.Injective fun g => π (g, h)) : d[⇑π ∘ ⟨Y 0,…`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `FiniteRange.neg`, `condRuzsaDist'.congr_simp`, `finiteRange_of_finset`, `instFiniteRange`, `instFiniteRangeComp`, `instFiniteRangeProdMk`

### `condRuzsaDist'_of_inj_map'` (theorem)
Lean: `(hA : Measurable A) (hB : Measurable B) (hC : Measurable C) : d[A ; μ'' # B | B + C ; μ] = d[A ; μ'' # C | B + C ; μ]`
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `condRuzsaDist'_of_copy`: `(X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (X' : Ω'' → G) (hY' : Measurable Y') (hW' : Measurable W') (h1 : IdentDistrib X X' μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') : d[X ; μ…`
- `condRuzsaDist'_of_inj_map`: `(hX : Measurable X) (hB : Measurable B) (hC : Measurable C) (h_indep : IndepFun X (⟨B, C⟩) μ) : d[X ; μ # B | B + C ; μ] = d[X ; μ # C | B + C ; μ]`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `FiniteRange.mem`, `FiniteRange.range`, `finiteRange_of_finset`, `instFiniteRangeComp`, `instFiniteRangeComp_1`, `instFiniteRangeProdMk`

### `rdist_add_const` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) : d[X; μ # Y + fun x => c; μ'] = d[X; μ # Y; μ']`
Docstring: Adding a constant to a random variable does not change the Rusza distance.
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.independent_copies_finiteRange`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) (μ' : Measure Ω') : ∃ ν X' Y', IsProbabilityMeasure ν ∧ Measurable X' ∧ Measurable Y' ∧ IndepFun X' Y' ν ∧ IdentDistrib X' X ν μ ∧ IdentDistrib…`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.entropy_add_const`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_zero_measure`

### `continuous_rdist_restrict_probabilityMeasure` (theorem)
Lean: `Continuous fun μ => d[id; ↑μ.1 # id; ↑μ.2]`
Docstring: Ruzsa distance depends continuously on the measure.
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `continuous_measureEntropy_probabilityMeasure`, `continuous_probabilityMeasure_apply_of_isClopen`

### `diff_ent_le_rdist` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) : |H[X; μ] - H[Y; μ']| ≤ 2 * d[X; μ # Y; μ']`
Docstring: `|H[X] - H[Y]| ≤ 2 d[X ; Y]`.
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

### `ent_bsg` (theorem)
Lean: `(hA : Measurable A) (hB : Measurable B) : ∫ (x : G), (fun z => d[A; μ[|(A + B) ⁻¹' {z}] # B; μ[|(A + B) ⁻¹' {z}]]) x ∂Measure.map (A + B) μ ≤ 3 * I[A : B ; μ] + 2 * H[A + B; μ] - H[A; μ] - H[B; μ]`
Docstring: The **entropic Balog-Szemerédi-Gowers inequality**. Let `A, B` be `G`-valued random variables on `Ω`, and set `Z := A+B`. Then `∑ z, P[Z=z] d[(A | Z = z) ; (B | Z = z)] ≤ 3 I[A :B] + 2 H[Z] - H[A] - H[B].` TODO: remove the hypothesis of `Fintype G` from here and from `condIndep_copies'`
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.CondIndepFun`: `(f : Ω → α) (g : Ω → β) (h : Ω → γ) (μ : autoParam (Measure Ω) CondIndepFun._auto_1) : Prop`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport`: `(κ : Kernel T S) (μ : Measure T) : Prop`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`: `(κ : Kernel T S) : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `FiniteRange.sub`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`
