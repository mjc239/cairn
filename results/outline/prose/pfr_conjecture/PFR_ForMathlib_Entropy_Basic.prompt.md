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

## Chapter (Lean module `PFR.ForMathlib.Entropy.Basic`)

### `ProbabilityTheory.entropy` (definition)
Lean: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.

### `ProbabilityTheory.condEntropy` (definition)
Lean: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
Docstring: Conditional entropy of a random variable w.r.t. another. This is the expectation under the law of `Y` of the entropy of the law of `X` conditioned on the event `Y = y`.

### `ProbabilityTheory.condEntropy_of_injective` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
Docstring: If `X : Ω → S`, `Y : Ω → T` are random variables, and `f : T × S → U` is injective for each fixed `t ∈ T`, then `H[f(Y, X) | Y] = H[X | Y]`. Thus for instance `H[X-Y|Y] = H[X|Y]`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.ae_mem_of_finiteRange`, `ProbabilityTheory.condEntropy_def`, `ProbabilityTheory.condEntropy_eq_sum`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_congr`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.full_measure_of_finiteRange`

### `ProbabilityTheory.condMutualInfo` (definition)
Lean: `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.

### `ProbabilityTheory.condEntropy_eq_kernel_entropy` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Docstring: Conditional entropy of a random variable is equal to the entropy of its conditional kernel.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.condDistrib_apply'`, `ProbabilityTheory.condEntropy_def`, `ProbabilityTheory.finiteSupport_of_finiteRange`

### `ProbabilityTheory.condMutualInfo_eq_kernel_mutualInfo` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : I[X : Y|Z;μ] = Ik[condDistrib (⟨X, Y⟩) Z μ , Measure.map Z μ]`
Docstring: The conditional mutual information agrees with the information of the conditional kernel.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `ProbabilityTheory.condDistrib_apply`, `ProbabilityTheory.condDistrib_apply'`, `ProbabilityTheory.condDistrib_fst_ae_eq`, `ProbabilityTheory.condDistrib_fst_of_ne_zero`, `ProbabilityTheory.condDistrib_snd_ae_eq`

### `ProbabilityTheory.condMutualInfo_eq` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : I[X : Y|Z;μ] = H[X | Z ; μ] + H[Y | Z ; μ] - H[⟨X, Y⟩ | Z ; μ]`
Docstring: `I[X : Y| Z] = H[X| Z] + H[Y| Z] - H[X, Y| Z]`.
Proof uses:
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.mutualInfo`: `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
- `ProbabilityTheory.condMutualInfo_eq_kernel_mutualInfo`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : I[X : Y|Z;μ] = Ik[condDistrib (⟨X, Y⟩) Z μ , Measure.map Z μ]`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `ProbabilityTheory.Kernel.entropy_congr`, `ProbabilityTheory.condDistrib_apply'`, `ProbabilityTheory.condDistrib_fst_ae_eq`, `ProbabilityTheory.condDistrib_fst_of_ne_zero`, `ProbabilityTheory.condDistrib_snd_ae_eq`, `ProbabilityTheory.condDistrib_snd_of_ne_zero`, `ProbabilityTheory.condEntropy_zero_measure`, `ProbabilityTheory.condMutualInfo_zero_measure`

### `ProbabilityTheory.condMutualInfo_of_inj_map` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (f : U → S → V) (hf : ∀ (t : U), Function.Injective (f t)) : I[fun ω => f (Z ω) (X ω) : Y|Z;μ] = I[X : Y|Z;μ]`
Docstring: If `f(Z, X)` is injective for each fixed `Z`, then `I[f(Z, X) : Y| Z] = I[X : Y| Z]`.
Proof uses:
- `ProbabilityTheory.condEntropy`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
- `ProbabilityTheory.condEntropy_of_injective`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
- `ProbabilityTheory.condMutualInfo_eq`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : I[X : Y|Z;μ] = H[X | Z ; μ] + H[Y | Z ; μ] - H[⟨X, Y⟩ | Z ; μ]`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`

### `ProbabilityTheory.mutualInfo` (definition)
Lean: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
Docstring: The mutual information `I[X : Y]` of two random variables is defined to be `H[X] + H[Y] - H[X ; Y]`.

### `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
Docstring: `I[X : Y] = H[X] - H[X|Y]`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport`: `(κ : Kernel T S) (μ : Measure T) : Prop`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`: `(κ : Kernel T S) : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.FiniteKernelSupport.aefiniteKernelSupport`

### `ProbabilityTheory.mutualInfo_eq_zero` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
Docstring: `I[X : Y] = 0` iff `X, Y` are independent.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.measureMutualInfo`: `(μ : autoParam (Measure (S × T)) measureMutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.measureMutualInfo_nonneg_aux`: `0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.prod_of_full_measure_finset`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Measure.ext_iff_measureReal_singleton_finiteSupport`

### `ProbabilityTheory.IndepFun.condEntropy_eq_entropy` (theorem)
Lean: `(h : IndepFun X Y μ) (hX : Measurable X) (hY : Measurable Y) : H[X | Y ; μ] = H[X; μ]`
Proof uses:
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
Helper lemmas folded into the proof: `ProbabilityTheory.IndepFun.mutualInfo_eq_zero`

### `ProbabilityTheory.condEntropy_two_eq_kernel_entropy` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : H[X | ⟨Y, Z⟩ ; μ] = Hk[(condDistrib (fun a => (Y a, X a)) Z μ).condKernel , (Measure.map Z μ).compProd (condDistrib (fun a => (Y a, X a)) Z μ).fst]`
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
- `ProbabilityTheory.condKernel_condDistrib_ae_eq`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : ⇑(condDistrib (fun a => (X a, Y a)) Z μ).condKernel =ᵐ[Measure.map (fun ω => (Z ω, X ω)) μ] ⇑(condDistrib Y (fun ω => (Z …`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.comap_real_apply`, `MeasureTheory.Measure.map_prod_comap_swap`, `MeasureTheory.Measure.support`, `MeasureTheory.lintegral_eq_tsum`

### `ProbabilityTheory.cond_chain_rule` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : H[⟨X, Y⟩ | Z ; μ] = H[Y | Z ; μ] + H[X | ⟨Y, Z⟩ ; μ]`
Docstring: `H[X, Y | Z] = H[Y | Z] + H[X | Y, Z]`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib`: `(X : Ω → S) (Y : Ω → T) (μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
- `ProbabilityTheory.condEntropy_two_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) : H[X | ⟨Y, Z⟩ ; μ] = Hk[(condDistrib (fun a => (Y a, X a)) Z μ).condKernel , (Measure.map Z μ).compProd (condDistrib (fun …`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.Kernel.entropy_congr`, `ProbabilityTheory.condDistrib_apply'`, `ProbabilityTheory.condDistrib_fst_ae_eq`

### `ProbabilityTheory.entropy_eq_sum_finset` (theorem)
Lean: `(hA : (Measure.map X μ) (↑A)ᶜ = 0) : H[X; μ] = ∑ x ∈ A, ((Measure.map X μ).real {x}).negMulLog`
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure`: `(μ : Measure S) : Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
Helper lemmas folded into the proof: `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_eq_sum`

### `ProbabilityTheory.IsUniform.entropy_eq` (theorem)
Lean: `(hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
Docstring: If `X` is uniformly distributed on `H`, then `H[X] = log |H|`.
Proof uses:
- `ProbabilityTheory.IsUniform.measureReal_preimage_of_mem`: `(h : IsUniform (↑A) X μ) (hX : Measurable X) (hs : s ∈ A) : μ.real (X ⁻¹' {s}) = 1 / ↑A.card`
- `ProbabilityTheory.entropy_eq_sum_finset`: `(hA : (Measure.map X μ) (↑A)ᶜ = 0) : H[X; μ] = ∑ x ∈ A, ((Measure.map X μ).real {x}).negMulLog`
Helper lemmas folded into the proof: `ProbabilityTheory.IsUniform.full_measure`, `ProbabilityTheory.IsUniform.measureReal_preimage_of_mem'`, `ProbabilityTheory.IsUniform.measureReal_preimage_of_nmem`, `ProbabilityTheory.IsUniform.measure_preimage_compl`, `ProbabilityTheory.IsUniform.measure_preimage_of_nmem`, `ProbabilityTheory.entropy_eq_sum_finset'`

### `ProbabilityTheory.entropy_submodular` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : H[X | ⟨Y, Z⟩ ; μ] ≤ H[X | Z ; μ]`
Docstring: `H[X | Y, Z] ≤ H[X | Z]`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport`: `(κ : Kernel T S) (μ : Measure T) : Prop`
- `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib`: `(X : Ω → S) (Y : Ω → T) (μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.mutualInfo`: `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.mutualInfo_nonneg`: `(hκ : κ.AEFiniteKernelSupport μ) : 0 ≤ Ik[κ , μ]`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `ProbabilityTheory.Kernel.entropy_condKernel_le_entropy_snd`, `ProbabilityTheory.Kernel.entropy_congr`, `ProbabilityTheory.Kernel.mutualInfo_eq_snd_sub`, `ProbabilityTheory.condDistrib_apply'`

### `ProbabilityTheory.entropy_triple_add_entropy_le` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : H[⟨X, ⟨Y, Z⟩⟩; μ] + H[Z; μ] ≤ H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ]`
Docstring: The submodularity inequality: `H[X, Y, Z] + H[Z] ≤ H[X, Z] + H[Y, Z]`.
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
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.FiniteKernelSupport.aefiniteKernelSupport`

### `ProbabilityTheory.entropy_sub_mutualInfo_eq_condEntropy` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X; μ] - I[X : Y ; μ] = H[X | Y ; μ]`
Docstring: `H[X] - I[X : Y] = H[X | Y]`.
Proof uses:
- `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`

### `ProbabilityTheory.prob_ge_exp_neg_entropy` (theorem)
Lean: `(X : Ω → S) (μ : Measure Ω) (hX : Measurable X) : ∃ s, μ Set.univ * ↑(Real.exp (-H[X; μ])).toNNReal ≤ (Measure.map X μ) {s}`
Docstring: If `X` is an `S`-valued random variable, then there exists `s ∈ S` such that `P[X = s] ≥ \exp(- H[X])`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.finiteSupport_of_finiteRange`, `ProbabilityTheory.measureEntropy_eq_sum`

### `ProbabilityTheory.mutualInfo_nonneg` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : 0 ≤ I[X : Y ; μ]`
Docstring: Mutual information is non-negative.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.measureMutualInfo_nonneg`: `0 ≤ Im[μ]`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `ProbabilityTheory.finiteSupport_of_finiteRange`, `instFiniteRangeProdMk`

### `ProbabilityTheory.condMutualInfo_eq_zero` (theorem)
Lean: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y|Z;μ] = 0 ↔ CondIndepFun X Y Z μ`
Docstring: `I[X : Y| Z]=0` iff `X, Y` are conditionally independent over `Z`.
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.integrable_of_finiteSupport`: `(μ : Measure S) : Integrable f μ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `ProbabilityTheory.mutualInfo_nonneg`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : 0 ≤ I[X : Y ; μ]`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `ProbabilityTheory.condIndepFun_iff`, `ProbabilityTheory.condMutualInfo_eq_integral_mutualInfo`, `ProbabilityTheory.entropy_zero_measure`, `ProbabilityTheory.finiteSupport_of_finiteRange`, `ProbabilityTheory.measureEntropy_zero`

### `ProbabilityTheory.ent_of_cond_indep` (theorem)
Lean: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : CondIndepFun X Y Z μ) : H[⟨X, ⟨Y, Z⟩⟩; μ] = H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ] - H[Z; μ]`
Docstring: If `X, Y` are conditionally independent over `Z`, then `H[X, Y, Z] = H[X, Z] + H[Y, Z] - H[Z]`.
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
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`, `ProbabilityTheory.Kernel.FiniteKernelSupport.aefiniteKernelSupport`
